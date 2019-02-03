---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83804simplemmaabab.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp lemma `a + (b + -a) = b`?](https://leanprover-community.github.io/archive/113488general/83804simplemmaabab.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 05 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945303):
<p><span class="user-mention" data-user-id="120690">@Guillermo Barajas Ayuso</span> wanted</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">theorem</span> <span class="n">auxiliary_basic</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="mi">0</span><span class="o">))</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="mi">0</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
</pre></div>


<p>and <code>simp</code> didn't quite do it; it reduces the problem to <code>a + (b + -a) = b</code>. There's a non-simp lemma <code> add_sub_cancel'_right : a + (b - a) = b</code> but <code>by simp [add_sub_cancel'_right]</code> doesn't work either, presumably because <code>simp</code> decides that replacing all <code>sub</code>s with <code>neg</code>s is a good idea before it can spot how to apply <code>add_sub_cancel'_right</code>. On the other hand actually adding what <code>simp</code> gets stuck on works fine:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">add_bracket_add_neg_self_bracket_cancel</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="bp">-</span><span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span><span class="n">add_assoc</span><span class="o">,</span><span class="n">neg_add_self</span><span class="o">,</span><span class="n">add_zero</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">auxiliary_basic</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="mi">0</span><span class="o">))</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="mi">0</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>


<p>Should <code>a + (b + -a) = b</code> be a simp lemma? It's about time I got the hang of this stuff. It's passing all the rules of thumb I've picked up, but my rules of thumb are not yet watertight...</p>

#### [ Patrick Massot (Aug 06 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945623):
<p>It's funny, I came across the exact same problem yesterday. Don't forget you can also use <code>simp [-sub_eq_add_neg, ...]</code> to get rid of the annoying "simplification"</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945720):
<p>I'm okay with adding this as a simp lemma, but it doesn't really fix the problem - you will also need lemmas for <code>a + (b + (c + -a))</code> and <code>a + (b + (-a + c))</code> and so on. The problem is that simp doesn't make any attempt to bring negatives together, so at best you can get lucky if they don't have so far to migrate</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945760):
<p>This is in part what <code>ring</code> is for, and Jeremy suggested also focusing an <code>abel</code> type tactic focusing only on the additive stuff</p>

#### [ Patrick Massot (Aug 06 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945763):
<p>I also wanted to ask for a version of ring working in an abelian group</p>

#### [ Kevin Buzzard (Aug 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945764):
<p>removing <code>sub_eq_add_neg</code> stops Lean from simplifying <code>(1 - 1)</code> :-)</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945769):
<p>I think <code>sub_eq_add_neg</code> is a bad choice of simp lemma, but I know why it's there - it limits the expressivity of input statements so you need fewer simp lemmas overall</p>

#### [ Kevin Buzzard (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945809):
<p>I thought that simp internally put things into some secret ordering using associativity and commutativity?</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945810):
<p>of course if <code>sub_eq_add_neg</code> was not a simp lemma we would need <code>a - a = 0</code> to be a simp lemma</p>

#### [ Patrick Massot (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945812):
<p>Is this also part of what Johannes simplifier work is meant to address?</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945813):
<p>it does, but that ordering does not put <code>a</code> and <code>-a</code> close together</p>

#### [ Kevin Buzzard (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945815):
<blockquote>
<p>it does, but that ordering does not put <code>a</code> and <code>-a</code> close together</p>
</blockquote>
<p>Might I suggest a different secret ordering?</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945822):
<p>this is an active area of research</p>

#### [ Kevin Buzzard (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945824):
<p>Oh wow</p>

#### [ Kevin Buzzard (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945826):
<p>How come humans are so good at it?</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945827):
<p>because they use adaptive algorithms that pay attention to the right things</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945868):
<p>and that's really hard and complicated</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945870):
<p>keep in mind that <code>simp</code> is used in way more circumstances than doing algebra on commutative groups</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945878):
<p>and you need to keep up performance in the other areas too</p>

#### [ Mario Carneiro (Aug 06 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945930):
<p>I think Johannes was working on adding "simpprocs" to the simplifier, which would enable this kind of adaptivity. It would notice we are doing algebra and fire up the algebra module that knows to do cancellation and stuff</p>


{% endraw %}
