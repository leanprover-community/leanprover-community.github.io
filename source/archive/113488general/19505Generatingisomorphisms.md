---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19505Generatingisomorphisms.html
---

## [general](index.html)
### [Generating isomorphisms?](19505Generatingisomorphisms.html)

#### [Kevin Buzzard (Mar 04 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269348):
I have some definition `definition foo (X : Type) : Type := blah`

#### [Kevin Buzzard (Mar 04 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269349):
If I have two types `X` and `Y` plus isomorphisms `f:X\to Y` and `g:Y\to X` (i.e. the composites both ways are the identity functions)

#### [Kevin Buzzard (Mar 04 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269389):
can I deduce that foo X is isomorphic to foo Y? Does this even make sense?

#### [Kevin Buzzard (Mar 04 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269490):
an isomorphism version of eq.subst?

#### [Kevin Buzzard (Mar 04 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269539):
Or does this have to somehow be proved on a case by case basis?

#### [Kevin Buzzard (Mar 04 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269552):
Mathematicians are so happy to identify objects which are canonically isomorphic and I find this much more of a struggle in Lean.

#### [Gabriel Ebner (Mar 04 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269600):
> can I deduce that foo X is isomorphic to foo Y?

Yes, if you define isomorphic as "there exist isomorphisms f and g such that ...". :smile:

This notion of isomorphism does not allow you to substitute isomorphic structures in arbitrary contexts, though.

#### [Kevin Buzzard (Mar 04 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269640):
yes this is absolutely how I want to define isomorphic.

#### [Kevin Buzzard (Mar 04 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269641):
How do I construct the map `foo X -> foo Y`?

#### [Gabriel Ebner (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269642):
The axiom of univalence would allow you to lift isomorphisms to equality, then you can substitute in arbitrary contexts.

#### [Gabriel Ebner (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269648):
Ooops, sorry missed the foo part.

#### [Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269649):
Oh great :-)

#### [Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269652):
I don't see any reason why I should be able to get a map foo X -> foo Y just given a map X -> Y

#### [Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269653):
but can I use the inverse somehow?

#### [Kevin Buzzard (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269654):
Or is what I want not even true?

#### [Gabriel Ebner (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269655):
So yeah, univalence is the axiomatic principle that would allow you to do that (in HoTT).

#### [Gabriel Ebner (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269713):
In Lean, you need to prove it yourself for each instance, such as `foo` here.

#### [Mario Carneiro (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269716):
It's definitely not true in general; for example if `foo X` was `X = nat`

#### [Mario Carneiro (Mar 04 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269727):
(not true without univalence that is)

#### [Mario Carneiro (Mar 04 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269789):
@**Gabriel Ebner** do you know if you can get a contradiction in classical lean from `X ~= Y -> X = Y`?

#### [Gabriel Ebner (Mar 04 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123270257):
This is an interesting question.  I think it is strictly weaker than univalence because it is not an isomorphism.  It looks inconsistent, but I don't immediately see how to derive a contradiction from it.

