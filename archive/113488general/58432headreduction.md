---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58432headreduction.html
---

## Stream: [general](index.html)
### Topic: [head reduction](58432headreduction.html)

---


{% raw %}
#### [ Floris van Doorn (Oct 23 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136343289):
<p>Is there a way to do head reduction on a term until the head changes? So I want to do something very similar to <code>whnf</code>, except I want to stop reducing as soon as the head changes.<br>
Alternatively, I want a tactic which does a <em>single</em> head reduction step.<br>
If I have to write this myself, is there any way to do the reduction <code>@nat.rec P h₀ h₁ (succ n) ⟶ h₁ n (@nat.rec P h₀ h₁ n)</code>without reducing too much?</p>

#### [ Floris van Doorn (Oct 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136345069):
<p>Here is the backstory, because maybe I'm approaching it wrong.<br>
The <code>induction</code> tactic has some flaws, and has one restriction which is very annoying for the HoTT library: all user-defined recursors have to eliminate to <strong>all</strong> universes, including <code>Prop</code>, which is unacceptable for HoTT. Therefore, I'm writing my own <code>hinduction</code> tactic, which tries to do essentially the same as <code>induction</code>tactic.</p>
<p>Now I'm having trouble with the following case. I write <code>hinduction x using my_rec</code>. Suppose the type of <code>x</code> is <code>F a b c</code> and the type of <code>my_rec</code> expects something of type <code>G ? ?</code>. Now I want to check whether by unfolding <code>F</code> and reducing, I can get something with head <code>G</code> (and figure out the arguments of <code>G</code>). I <em>do</em> want to support the case where <code>G</code> is a definition, so I <em>cannot</em> use the weak-head normal form of <code>F a b c</code>. There are a couple possible approaches:</p>
<ul>
<li>What I described above: repeatedly do a single head reduction and see if the head is now <code>G</code>.</li>
<li>Maybe I can do <code>whnf</code> but unfold all definitions, except <code>G</code>?</li>
<li>I could try to unify <code>F a b c</code> with <code>G _ _</code>. This last approach is something I think I know how to do, so maybe that is the best solution.</li>
</ul>

#### [ Sebastian Ullrich (Oct 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136347162):
<p><code>whnf</code> should already stop at definitions that are irreducible. Do you really want to support user recursors on (semi-)reducible definitions?</p>

#### [ Floris van Doorn (Oct 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136348052):
<p>I think so. In the HoTT library we define higher inductive types in terms of other higher inductive types. For example, the suspension is defined as a homotopy pushout, and the circle is defined as a suspension. <br>
Every higher inductive type comes with its own custom induction principle, but I still want to be able to apply theorems about suspensions for the circle. So I don't think I want the circle to be irreducible.<br>
This is how it worked in Lean 2, and it was fine in practice.</p>

#### [ Mario Carneiro (Oct 23 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136349422):
<p>I think you should try to unify the types for this</p>

#### [ Mario Carneiro (Oct 23 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136349454):
<p>You can figure out the number of underscores by adding them until you get something that is a type</p>


{% endraw %}
