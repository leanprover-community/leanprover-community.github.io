---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04444instantiatingmetavariales.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [instantiating meta variales](https://leanprover-community.github.io/archive/113489newmembers/04444instantiatingmetavariales.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230234):
<p>Is there a way to instantiate meta variables.  Consider the theorem below:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">x</span><span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">=</span><span class="mi">5</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">..</span>
<span class="kn">end</span>
</pre></div>


<p>What should the ...  be replaced with?  In this theorem, we could just change the existsi _ but in more complex theorems, meta variables seem to appear in many other places and it would be nice to instantiate them.</p>

#### [ Kenny Lau (Jul 24 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230270):
<p>what information would you provide in order for the metavariables to be instantiated?</p>

#### [ Kenny Lau (Jul 24 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230286):
<p>replacing <code>..</code> with <code>refl</code> would prove the theorem, but I don't know if that is what you want</p>

#### [ Ken Roe (Jul 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130231216):
<p>refl is not what I want.  In Coq, you can provide a value using instantiate (meta_var := value).  Is there something similar in Lean?</p>

#### [ Patrick Massot (Jul 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130231266):
<p>Doesn't this meta variable appear as a new goal?</p>

#### [ Kevin Buzzard (Jul 24 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232163):
<p><code>existsi 7</code> will instantiate the metavariable. If you use a hole <code>_</code> then you get a new goal <code>⊢ ℕ</code> as Patrick says. You can make this the first goal with <code>show ℕ</code> or <code>swap</code> and then instantiate it with <code>exact 7</code>.</p>

#### [ Ken Roe (Jul 24 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232676):
<p>I've seen those new goals as holes--that is how to fill in the holes.  Can swap be used beyond the second goal or is there something similar to switch for example the first and third goal?</p>

#### [ Patrick Massot (Jul 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232717):
<p><a href="https://github.com/leanprover/mathlib/blob/master/tactic/interactive.lean#L159" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/interactive.lean#L159">https://github.com/leanprover/mathlib/blob/master/tactic/interactive.lean#L159</a></p>

#### [ Patrick Massot (Jul 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232719):
<p>as explained by Kevin</p>

#### [ Patrick Massot (Jul 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232781):
<p>You can also use <code>show</code> if you have only one goal of that type</p>


{% endraw %}
