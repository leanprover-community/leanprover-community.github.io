---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28815performanceimprovementstoring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [performance improvements to ring](https://leanprover-community.github.io/archive/113488general/28815performanceimprovementstoring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Sep 02 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227901):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> The latest commit replaces some of the <code>mk_app</code> applications used in <code>ring</code>, and there was a <em>huge</em> performance gain. Now <code>ring</code> will solve <code>(x + y)^n = (x+y)^n</code> up to <code>n = 60</code> before hitting the timeout, compared to <code>n = 11</code> before</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227944):
<div class="codehilite"><pre><span></span>example (ε : ℚ) : ε / 3 + ε / 3 + ε / 3 = ε := by ring
</pre></div>


<p>takes a fraction of a second now</p>

#### [ Patrick Massot (Sep 02 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227959):
<p>Is this something we could learn from?</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227997):
<p><code>mk_app</code> sucks</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228008):
<p>There are still some <code>mk_app</code> uses in ring, but the problems seem to be when some of the arguments are (large) proof terms, even if they aren't used in type inference</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228011):
<p>I think it is typechecking the terms, which is a really bad idea since it gets done so often</p>

#### [ Kevin Buzzard (Sep 02 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228387):
<p>good catch Mario. I have had a lot of success with ring in the past but I usually cleared denominators myself and then applied the tactic when there were no divisions left.</p>

#### [ Mario Carneiro (Sep 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228677):
<p>the problem wasn't denominators per se. The major slowdown was in structural parts of the proof that are done in just about every proof. For example normalizing <code>(x+y)^n</code>uses no division</p>

#### [ Simon Hudon (Sep 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228678):
<p>I assume you're talking about <code>tactic.mk_app</code>. What do you replace it with? I was told it was preferable to use it to <code>to_expr</code>.</p>

#### [ Mario Carneiro (Sep 02 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228807):
<p><code>mk_app</code> will build an application while performing typeclass inference and typechecking (or at least inferring the types) of all passed arguments. The alternative is just to build the expr yourself, using <code>expr.app</code> or <code>expr.mk_app</code>, which does no typechecking or inference. I thought the inference might be slow, which is why <code>ring</code> uses an <code>instance_cache</code>, but I think that this was not the problem. Now I just do the typeclass inference directly and then put the app together manually.</p>

#### [ Mario Carneiro (Sep 02 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228852):
<div class="codehilite"><pre><span></span>meta def cache.mk_app (c : cache) (n inst : name) (l : list expr) : tactic expr :=
do m ← mk_instance ((expr.const inst [c.univ] : expr) c.α),
   return $ (@expr.const tt n [c.univ] c.α m).mk_app l
</pre></div>


<p>then</p>
<div class="codehilite"><pre><span></span>c.mk_app ``norm_num.subst_into_prod ``has_mul [l, e, tl, e, t, hl, hr, p₂],
</pre></div>

#### [ Rob Lewis (Sep 02 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133229004):
<p>That's awesome! I spent a little while profiling <code>linarith</code> earlier today and was also seeing performance problems with <code>mk_app</code>. It's not a straightforward story when to use it over <code>to_expr</code>, and yeah, making expressions by hand is probably the way to go for critical applications.</p>

#### [ Simon Hudon (Sep 02 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133229060):
<p>It would be nice to have a more systematic approach to finding bottle necks. One way I could think of is to use Travis to publish metrics for every build.</p>

#### [ Rob Lewis (Sep 03 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133230444):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm about to go to bed, so I'm going to leave this here for you to think about if you want to, otherwise I'll investigate tomorrow. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span> Compare the two profiles here:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>

<span class="kn">constants</span> <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">discrete_linear_ordered_field</span> <span class="n">T</span><span class="o">)</span>
<span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">h</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">ε</span> <span class="o">:</span> <span class="n">T</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">41</span><span class="bp">/</span><span class="mi">42</span><span class="o">)</span> <span class="bp">*</span> <span class="n">ε</span> <span class="bp">-</span> <span class="o">(</span><span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">7</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">ε</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">41</span><span class="bp">/</span><span class="mi">42</span><span class="o">)</span> <span class="bp">*</span> <span class="n">ε</span> <span class="bp">-</span> <span class="o">(</span><span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">7</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ring</span>
</pre></div>


<p>The second one takes twice as long and spends almost all its time in the final <code>exact</code>. It's evaluating rational arithmetic in the kernel. The first one spends 20x longer in <code>norm_num</code> but that's still better than kernel evaluation.</p>

#### [ Mario Carneiro (Sep 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133230451):
<p>My guess is that this is <code>tactic.norm_num</code>'s fault (the one built into core)</p>

#### [ Rob Lewis (Sep 03 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255709):
<p>After chasing down a few false leads: it isn't <code>tactic.norm_num</code>, although <code>tactic.norm_num</code> is surprisingly sensitive to typeclass short circuits. These commands take roughly the same amount of time if you add enough short circuits for <code>T</code>, otherwise the second takes 7x longer.</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">norm_num</span> <span class="bp">`</span><span class="o">((</span><span class="mi">5</span><span class="bp">/</span><span class="mi">60</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">70</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span>
<span class="n">run_cmd</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">norm_num</span> <span class="bp">`</span><span class="o">((</span><span class="mi">5</span><span class="bp">/</span><span class="mi">60</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">70</span><span class="o">)</span> <span class="o">:</span> <span class="n">T</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span>
</pre></div>


<p>I find this a little surprising since <code>norm_num</code> caches and pre-applies the instances, so it shouldn't be searching for any instance more than once. But this isn't what's causing the issue above.</p>

#### [ Rob Lewis (Sep 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255736):
<p>When <code>ring</code> solves <code>(41/42)*ε - (ε / 2 + ε / 3 + ε / 7) = 0</code>, it actually proves <code>(41/42)*ε +  -(ε / 2 + ε / 3 + ε / 7) = 0</code>. Unifying these over <code>ℚ</code> takes way longer than over <code>T</code> for some reason.</p>

#### [ Rob Lewis (Sep 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255823):
<p>There's an easy workaround: change the last lines of <code>ring1</code> to </p>
<div class="codehilite"><pre><span></span>  <span class="n">ntp</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">change</span> <span class="n">ntp</span> <span class="n">ff</span><span class="o">,</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">exact</span> <span class="n">p</span>
</pre></div>

#### [ Rob Lewis (Sep 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255908):
<p>The kernel is much faster at checking that the proof from <code>ring</code> has the expected type than <code>exact</code>.</p>

#### [ Mario Carneiro (Sep 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133278527):
<p>Argh, this is so annoying. I inserted explicit change proof terms in the proof. I think it is fixed but keep me appraised if you find anything else.</p>

#### [ Rob Lewis (Sep 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133295842):
<p>Thanks! Will do.</p>


{% endraw %}
