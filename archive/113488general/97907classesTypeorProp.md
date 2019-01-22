---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97907classesTypeorProp.html
---

## [general](index.html)
### [classes Type or Prop](97907classesTypeorProp.html)

#### [Reid Barton (Apr 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747081):
Is there any particular reason not to make `t2_space` and similar classes a Prop?
```lean
class t2_space (α : Type u) [topological_space α] :=
(t2 : ∀x y, x ≠ y → ∃u v : set α, is_open u ∧ is_open v ∧ x ∈ u ∧ y ∈ v ∧ u ∩ v = ∅)
```

#### [Reid Barton (Apr 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747084):
I actually had sort of assumed that a structure with only Prop fields would automatically be a Prop by default.

#### [Kevin Buzzard (Apr 27 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747703):
I noticed earlier this week that this wasn't happening

#### [Kevin Buzzard (Apr 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747761):
As I'm sure you know, if you are defining your own class you can just tell it to be a Prop

#### [Kevin Buzzard (Apr 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747764):
but that won't help you here

#### [Reid Barton (Apr 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747940):
I don't really need it to be a Prop, I just tried to use it as a Prop and was surprised when it didn't work, but it's easy enough for me to avoid doing that.

#### [Reid Barton (Apr 27 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747991):
I came across this comment later in the same file which makes me think the statuses of these structures are a bit accidental:
```lean
/- countability axioms

For our applications we are interested that there exists a countable basis, but we do not need the
concrete basis itself. This allows us to declare these type classes as `Prop` to use them as mixins.
-/
```

#### [Reid Barton (Apr 27 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125748028):
(It's followed by a structure which is indeed declared to be a Prop.)

#### [Mario Carneiro (Apr 27 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125751920):
I think that's a typo. I'll change it

