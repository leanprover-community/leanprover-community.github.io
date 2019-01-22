---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49995quiversanddiagrams.html
---

## [maths](index.html)
### [quivers and diagrams](49995quiversanddiagrams.html)

#### [Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937757):
I've got the following snippet
```lean
import data.list

universes u v w

structure quiver :=
(V : Type u)
(E : Type v)
(s : E → V)
(t : E → V)

variable {Q : quiver}

definition is_a_path : (list Q.E) → Prop
| [] := true
| [e] := true
| (e₁ :: e₂ :: es) := Q.s e₁ = Q.t e₂ ∧ is_a_path (e₂ :: es)

structure diagram :=
(D : Q.V → Type w)
(m : Π (e : Q.E), D (Q.s e) → D (Q.t e))
```

#### [Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937763):
But now I realise that I actually only want to consider finite lists

#### [Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937765):
why don't you use chain lol

#### [Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937766):
aha

#### [Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937771):
How would I best go about that

#### [Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937772):
but lists are all finite

#### [Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937774):
Why?

#### [Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937778):
because they're defined inductively

#### [Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937785):
```lean
inductive list : Type u → Type u
constructors:
list.nil : Π {T : Type u}, list T
list.cons : Π {T : Type u}, T → list T → list T
```

#### [Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937788):
and I can inductively prove that they are finite :P

#### [Johan Commelin (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937790):
I see

#### [Johan Commelin (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937797):
Crazy...

#### [Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937835):
you want lazy lists?

#### [Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937838):
I see you want everything to be lazy

#### [Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937839):
maybe that's why you think they're crazy

#### [Johan Commelin (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937844):
Hmm, maybe now I'm happy that they aren't lazy (-;

#### [Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937846):
maybe your ideas are a bit hazy

#### [Johan Commelin (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937849):
That.

#### [Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937853):
http://www.rhymezone.com/r/rhyme.cgi?Word=lazy&typeofrhyme=perfect

#### [Johan Commelin (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937857):
That is definitely true. It's one of my defining properties

#### [Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937859):
not many words rhyme with lazy though

#### [Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937861):
so I'm done coz I can't use daisy

#### [Mario Carneiro (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937865):
I guess you just did

#### [Johan Commelin (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937867):
And you don't wanna look like jay z

#### [Johan Commelin (May 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937919):
Anyway... I am going to try and define the set of all paths, and then try to figure out how to define commutative diagrams

#### [Kenny Lau (May 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937924):
hmm... I would rather use categories to define diagrams

#### [Kenny Lau (May 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937968):
https://github.com/kckennylau/category-theory/blob/master/src/natural_transformation.lean

#### [Kenny Lau (May 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937970):
```lean
@[reducible] def product {α} (C : category.{u v} α) (ι) (f : ι → α) :=
limit (discrete ι) C (functor.of_discrete C f)
```

#### [Kenny Lau (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937973):
product is the limit of the discrete diagram

#### [Johan Commelin (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937978):
But that is not how we use them, I think

#### [Kenny Lau (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers and diagrams/near/125937981):
is it not?

