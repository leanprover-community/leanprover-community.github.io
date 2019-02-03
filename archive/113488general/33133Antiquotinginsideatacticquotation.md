---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33133Antiquotinginsideatacticquotation.html
---

## Stream: [general](index.html)
### Topic: [Antiquoting inside a tactic quotation](33133Antiquotinginsideatacticquotation.html)

---


{% raw %}
#### [ Nicholas Scheel (Sep 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134069500):
<p>Hi!! So I'm trying to write my first tactic and I have something that looks like this:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">naturally</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
  <span class="n">iterate</span> <span class="bp">`</span><span class="o">[</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span> <span class="err">%%</span><span class="n">t</span><span class="o">]</span> <span class="o">]</span>
</pre></div>


<p>but I get this error:</p>
<div class="codehilite"><pre><span></span>kernel failed to type check declaration &#39;naturally&#39; this is usually due to a buggy tactic or a bug in the builtin elaborator
elaborated type:
  Type → tactic unit
elaborated value:
  λ (t : Type),
     .....................
</pre></div>


<p>I can write it without the antiquotation, but I realized I then have to have <code>t</code> in scope when I run <code>naturally</code> to get it to work that way <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span></p>

#### [ Nicholas Scheel (Sep 17 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134069543):
<p>Do you know what the issue is and how I could write it properly? :)</p>

#### [ Nicholas Scheel (Sep 17 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134069695):
<p>Background: I'm basically trying to write a tactic that converts statements about \N embedded in \R into statements about \N, like the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intro</span> <span class="n">n</span><span class="bp">;</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">zero_lt_succ</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span>
  <span class="k">begin</span>
  <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">t</span> <span class="o">:=</span> <span class="n">ℝ</span><span class="o">,</span>
  <span class="n">naturally</span> <span class="n">ℝ</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">add_comm</span> <span class="bp">_</span> <span class="n">n</span><span class="o">],</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_lt_succ</span>
  <span class="kn">end</span>
</pre></div>

#### [ Nicholas Scheel (Sep 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134069807):
<p>Why I’m trying to restrict it to a certain type is to prevent infinite recursion (e.g. 0 with lots of coercions from nat to nat); it would be cool if there was a better way to do this but I have not explored tactics much</p>

#### [ Mario Carneiro (Sep 17 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134070948):
<p><code>t</code> should have type <code>expr</code> not <code>Type</code></p>

#### [ Nicholas Scheel (Sep 17 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134072594):
<p>Hm ... I believe you, but it still doesn't seem to compile:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">naturally&#39;</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">iterate</span> <span class="n">none</span> <span class="bp">`</span><span class="o">[</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span> <span class="err">%%</span><span class="n">t</span><span class="o">]</span> <span class="o">]</span>
</pre></div>

#### [ Nicholas Scheel (Sep 17 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134072699):
<p>I'm using Lean v3.4.1 btw</p>

#### [ Nicholas Scheel (Sep 17 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134072755):
<p>it looks like this term is failing: <code>rule := expr.subst (to_pexpr t)</code> (it's missing the second argument)<br>
without the antiquotation it is: <code>rule := ``(@nat.cast_zero t)</code></p>

#### [ Nicholas Scheel (Sep 17 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134072861):
<p>I think it should be <code>rule := expr.subst ``(λ (_x_1 : _), @nat.cast_zero _x_1) (to_pexpr t)</code></p>

#### [ Simon Hudon (Sep 17 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134077733):
<p><code>rw</code> is tricky to use this way. Try not quoting it. You'll see its argument list is not a list of expr (in which case your attempt should work); it's a list of <code>rw_rules</code></p>

#### [ Nicholas Scheel (Sep 17 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134079385):
<p>yeah, this is what I ended up with (forgive the messy code): <a href="https://github.com/MonoidMusician/MATH361/blob/56b6b5df40598bddade40e973a400a67cb79d184/src/hw/hw2.lean#L380-L407" target="_blank" title="https://github.com/MonoidMusician/MATH361/blob/56b6b5df40598bddade40e973a400a67cb79d184/src/hw/hw2.lean#L380-L407">https://github.com/MonoidMusician/MATH361/blob/56b6b5df40598bddade40e973a400a67cb79d184/src/hw/hw2.lean#L380-L407</a></p>

#### [ Nicholas Scheel (Sep 17 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134079431):
<p>I wasn’t able to get it to parse an expression in interactive mode, so I just made an alias for applying it to reals haha</p>

#### [ Mario Carneiro (Sep 17 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134079528):
<p>I suggest you use the noninteractive rw tactic outside interactive mode</p>

#### [ Nicholas Scheel (Sep 17 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134079539):
<p>that would probably be a good idea :D</p>

#### [ Nicholas Scheel (Sep 17 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134079627):
<p>would that be <code>rewrite_target</code>?</p>

#### [ Simon Hudon (Sep 17 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting%20inside%20a%20tactic%20quotation/near/134108985):
<p>I was about to suggest <code>rewrite_target</code> but it requires that you encode <code>&lt;- </code> by hand</p>


{% endraw %}
