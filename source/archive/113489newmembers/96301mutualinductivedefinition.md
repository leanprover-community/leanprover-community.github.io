---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96301mutualinductivedefinition.html
---

## [new members](index.html)
### [mutual inductive definition](96301mutualinductivedefinition.html)

#### [Shaun Steenkamp (Nov 16 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147808981):
can one of you explain why I cannot get this mutual inductive definition to work?
```lean
mutual inductive Foo, Bar
with Foo : Type
| bizz : Foo
| buzz {f : Foo} : Bar f → Foo
with Bar : Foo → Type
| baz (f : Foo) : Bar f
```
For reference, the following works in Agda
```agda
mutual
  data Foo : Set where
    bizz : Foo
    buzz : {f : Foo} → Bar f → Foo

  data Bar : Foo → Set where
    baz : (f : Foo) → Bar f
```

#### [Mario Carneiro (Nov 16 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809137):
this is called an inductive-recursive definition, and it is stronger than lean's axiomatics

#### [Mario Carneiro (Nov 16 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809215):
There may be another way to encode the type you want, but inductive recursive definitions can be used to prove DTT is consistent, so lean can't do it

#### [Keeley Hoek (Nov 16 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809656):
Incidentally, Mario, were you working on a Lean consistency project at some point?

#### [Shaun Steenkamp (Nov 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809895):
What is DTT?

#### [Patrick Massot (Nov 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147810111):
dependent type theory

#### [Patrick Massot (Nov 16 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147810119):
That's the name of the game we are playing

#### [Mario Carneiro (Nov 16 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811271):
yes, I'll be defending my masters thesis in a few weeks and lean consistency is in it

#### [Mario Carneiro (Nov 16 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811346):
https://github.com/digama0/lean-type-theory/releases/tag/v0.21

#### [Kenny Lau (Nov 16 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811386):
so, is lean consistent?

#### [Abhimanyu Pallavi Sudhir (Nov 16 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811742):
@**Kenny Lau** How is that not independent?

#### [Mario Carneiro (Nov 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147812715):
yes, assuming some large cardinal assumptions

#### [Mario Carneiro (Nov 16 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147812723):
which is the usual story with consistency proofs

#### [Johannes Hölzl (Nov 16 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813619):
I think this shape is called inductive-inductive: mutual inductive types where at least one is indexed by the other one, inductive-recursive means to mutually define inductive types and recursive definitions where at least one inductive type depends on the recursive definition.
I think inductive-inductive can be reduced to inductive, inductive-recursive cannot

#### [Mario Carneiro (Nov 16 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813885):
you might be right about the name, but I'm pretty sure inductive-inductive is also axiomatically strong

#### [Mario Carneiro (Nov 16 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813968):
because you can define the well typed terms of DTT by induction-induction with the set of well formed contexts and the set of types in a context

#### [Mario Carneiro (Nov 16 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147814054):
Inductive recursive can be reduced to inductive inductive, I think, where the recursive function becomes a functional relation

#### [Johannes Hölzl (Nov 16 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147814450):
Ah, or it was this way round

#### [Shaun Steenkamp (Nov 16 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147817435):
```quote
There may be another way to encode the type you want, but inductive recursive definitions can be used to prove DTT is consistent, so lean can't do it
```
 Consistent with respect to what?

#### [Johannes Hölzl (Nov 16 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147821293):
with respect to DTT with a larger type universe and inductive recursive definitions (I guess)

#### [Floris van Doorn (Nov 16 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147821961):
This is indeed an inductive-inductive definition. I think adding these won't increase the proof stength of the system. In extensional type theory, inductive-inductive definitions can be defined from indexed inductive types, but I don't think it's known in whether this is the case in intensional type theory.
Inductive-recursive definitions indeed do increase the proof stength of the system: you can build a (Tarski) universe using induction-recursion.
Ncatlab links:
https://ncatlab.org/nlab/show/inductive-inductive+type
https://ncatlab.org/nlab/show/inductive-recursive+type

