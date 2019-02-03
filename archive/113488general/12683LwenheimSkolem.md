---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12683LwenheimSkolem.html
---

## Stream: [general](index.html)
### Topic: [Löwenheim-Skolem](12683LwenheimSkolem.html)

---


{% raw %}
#### [ Kenny Lau (Oct 09 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492014):
<p>Is Löwenheim-Skolem true in Lean?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492142):
<p>isn't that 2 theorems?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492171):
<p>wait this is a theorem about model theory, right? Is model theory in Lean?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492186):
<p>Can you formalise your question?</p>

#### [ Kenny Lau (Oct 09 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492286):
<p>Is there a countable model of ZFC in Lean?</p>

#### [ Floris van Doorn (Oct 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135553994):
<p>This should be true. It shouldn't matter that the metatheory is type theory instead of set theory to prove Löwenheim-Skolem. <br>
There are students at the university of Pittsburgh who want to formalize forcing in Lean, and want to prove Löwenheim-Skolem along the way: <a href="https://github.com/flypitch/flypitch" target="_blank" title="https://github.com/flypitch/flypitch">https://github.com/flypitch/flypitch</a>.</p>

#### [ Reid Barton (Oct 11 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135583543):
<p>oh, this is neat! I wanted to formalize independence of CH too at one point, so I'll definitely check this out</p>

#### [ Kenny Lau (Oct 11 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135593457):
<p>well there are a lot more sentences in Lean than in classical mathematical logic</p>

#### [ Floris van Doorn (Oct 11 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135615282):
<blockquote>
<p>well there are a lot more sentences in Lean than in classical mathematical logic</p>
</blockquote>
<p>Oh, you meant is Lowenheim-Skolem true for Lean as <em>object language</em>.<br>
I thought you were talking about having Lean as meta language, and a regular first-order theory as object language. I have never heard of Lowenheim-Skolem for higher-order logics, but it is probably false for those, right?</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616391):
<p>Kenny still has not formalised what he means, so we can but conjecture.</p>

#### [ Kenny Lau (Oct 11 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616522):
<p>that means we can define <code>r : nat -&gt; nat -&gt; Prop</code> such that the axioms of ZFC (interpreted using Lean) are satisifed with interpreting the membership symbol as <code>r</code></p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616749):
<p>You want it computable? ;-)</p>

#### [ Kenny Lau (Oct 11 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616786):
<p>there's no computable model of ZFC</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616815):
<p>So you're worried about that the "axiom schemes"?</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616833):
<p>You should ask Lotte or David Evans. They are actually real life model theorists who are easily accessible to you.</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616896):
<p>Maybe Mario or Gabriel or one of the other experts that hang around here will just come and tell us the answer though</p>

#### [ Jeremy Avigad (Oct 11 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135617765):
<p>For higher-order logic with standard semantics, of course, Löwenheim-Skolem is false; we can write down categorical axiomatizations of the reals. <br>
If you think of higher-order logic in a first-order way -- i.e. a model of higher-order logic is just a many-sorted theory (so each type is a sort) with operations for application and lambda abstraction satisfying the requisite comprehension axioms, Löwenheim-Skolem is true. These are sometimes called "Henkin models". I am sure all this will carry over to dependent type theory. The hard part is saying what a model is. But e.g. the usual term model is a countable model.</p>


{% endraw %}
