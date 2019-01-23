---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/46145provingsimpleinductivetypesaredecidablyequal.html
---

## Stream: [new members](index.html)
### Topic: [proving simple inductive types are decidably equal](46145provingsimpleinductivetypesaredecidablyequal.html)

---


{% raw %}
#### [ Edward Ayers (Nov 06 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870382):
Suppose I make
```lean
inductive foo |A |B |C |D |E
```
How can I show that`foo` is decidably equal with minimal faff?

#### [ Floris van Doorn (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870461):
```
@[derive decidable_eq] inductive foo |A |B |C |D |E
```

#### [ Edward Ayers (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870516):
win for Lean

#### [ Edward Ayers (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870537):
What else can I `@[derive ...]`?

#### [ Floris van Doorn (Nov 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870660):
Not sure. In mathlib, if I search for derive, I only find `derive decidable_eq` and `derive has_reflect`.

#### [ Edward Ayers (Nov 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870661):
I found `has_sizeof` in the wild

#### [ Scott Morrison (Nov 06 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146895917):
I would love to write some "functorial" derive handlers, for automatically showing constructions are functorial with respect to either morphisms in their arguments, or isomorphisms in their arguments. This would be part of a bigger program to do transport of structure.

#### [ Patrick Massot (Nov 06 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146896228):
Today Cyril worked quite a lot on transport stuff.

#### [ Scott Morrison (Nov 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897672):
Ah, okay, what approach are they taking?

#### [ Patrick Massot (Nov 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897712):
parametricity for free, or something like that

#### [ Patrick Massot (Nov 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897752):
https://hal.inria.fr/hal-01559073

#### [ Scott Morrison (Nov 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897881):
I would really like some feedback on my `iso_induction` approach sketched in the comments of https://github.com/leanprover/mathlib/issues/408, and the very initial branch at https://github.com/leanprover-community/mathlib/commit/fc31a8c81040f2a7e087df890f1c848ff6d34eff. 

It needs more examples of definitions shown to be functorial in their arguments (hopefully automatically) before you can really see how it would work.


{% endraw %}
