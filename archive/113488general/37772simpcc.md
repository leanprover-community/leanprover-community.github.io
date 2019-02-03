---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37772simpcc.html
---

## Stream: [general](index.html)
### Topic: [simp, cc](37772simpcc.html)

---


{% raw %}
#### [ Pablo Le Hénaff (Jun 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127657772):
<p>Hello everyone, I am an intern at VU Amsterdam, working under the supervision of Johannes (who is abroad now).<br>
I would like to know more about the status of the rsimp (?)/congruence closure implementation in Lean. Everything is not totally clear in my mind.<br>
I read the paper published by Leonardo de Moura and Daniel Selsam about cc from 2016 - the examples given don't work anymore due to syntax changes in the Lean language. The inst_simp tactic doesn't exist anymore and I guess rsimp/simp may be a new version of it.<br>
Do people actually use the rsimp tactic ? I tried it on a few examples and it does indeed some simplifications (eg in groups, although it seems it doesn't handle commutativity). It is however VERY slow and makes my Lean lag a lot, and sometimes eventually overflow the allocated memory. <br>
I know and used the ac_refl tactic which works really well. I am aware that AC rewriting coupled with another theory (for instance, the existence of an inverse in a group) is a complex topic. There are some papers out there about successful attempts though.  Are there any plans in implementing something similar / a better working version of (r)simp for specific theories ? I can imagine something targeted at some precise algebraic structures, with a small set of lemmas and good performances. I am asking the question after reading about the Knuth-Bendix completion which would maybe provide nice automation for some proofs (?). I already implemented a cancellation tactic for (comm_)groups, but I feel that there should be something more general.</p>
<p>Simp only won't simplify</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">x</span><span class="bp">⁻¹*</span><span class="n">y</span><span class="bp">*</span><span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="c1">-- fails</span>
<span class="kn">end</span>
</pre></div>


<p>Also, I don't know how to provide my own lemmas to the cc tactic / add lemmas to the cc_state / how the cc tactic can be tweaked to work with groups for instance.<br>
Thanks !</p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127657858):
<blockquote>
<p>inst_simp</p>
</blockquote>
<p>I didn't read the paper, but I think that is just congruence closure with E-matching in a saturation loop.  The current syntax should be <code>begin[smt] eblast end</code>.</p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127657894):
<blockquote>
<p>Do people actually use the rsimp tactic ?</p>
</blockquote>
<p>I am not aware of anybody who uses it.</p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127657978):
<blockquote>
<p>of (r)simp for specific theories</p>
</blockquote>
<p>I think simp with AC-matching is on the roadmap.</p>

#### [ Sean Leather (Jun 06 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658009):
<p>This is the <code>rsimp</code> usage in the mathlib repository:</p>
<div class="codehilite"><pre><span></span>$ git grep -n rsimp
data/list/basic.lean:342:  by intros l₁; induction l₁; intros; rsimp,
data/list/basic.lean:394:  induction l with hd tl ih; rsimp,
order/boolean_algebra.lean:44:  by rsimp,
order/boolean_algebra.lean:47:by rsimp
order/boolean_algebra.lean:67:neg_unique -- TODO: try rsimp if it supports custom lemmas
</pre></div>

#### [ Gabriel Ebner (Jun 06 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658012):
<p>Re: inst_simp.  Where did you see inst_simp?  I can't remember it from the IJCAR presentation, and now I can't find it in the paper either.</p>

#### [ Pablo Le Hénaff (Jun 06 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658090):
<p><a href="http://leanprover.github.io/ijcar16/examples/" target="_blank" title="http://leanprover.github.io/ijcar16/examples/">http://leanprover.github.io/ijcar16/examples/</a><br>
in those examples</p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658095):
<blockquote>
<p>Also, I don't know how to provide my own lemmas to the cc tactic</p>
</blockquote>
<p>The cc tactic doesn't use lemmas in any meaningful way, it just solves a goal if it can (essentially) be solved using just equational reasoning.</p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658107):
<blockquote>
<p>The tactic inst_simp uses E-matching to heuristically instantiate lemmas tagged as simplification rules (i.e., <code>[simp]</code> tag in Lean).</p>
</blockquote>
<p>So <code>begin[smt] eblast end</code></p>

#### [ Gabriel Ebner (Jun 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658205):
<p>For lemmas, use E-matching.  That is, tag lemmas as <code>@[ematch]</code> and then use <code>begin[smt] eblast end</code>; also check out <code>eblast_using [...]</code>.</p>

#### [ Pablo Le Hénaff (Jun 06 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20cc/near/127658300):
<p>i'll give it a try and tell you, thanks</p>


{% endraw %}
