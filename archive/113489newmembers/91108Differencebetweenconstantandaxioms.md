---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/91108Differencebetweenconstantandaxioms.html
---

## [new members](index.html)
### [Difference between constant and axioms](91108Differencebetweenconstantandaxioms.html)

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074362):
I just noticed that `propext` is defined as a constant:

```lean
constant propext {a b : Prop} : (a ↔ b) → a = b
```

Is this an alternative to `axiom`? What would change if I made it an axiom?

#### [Kenny Lau (Dec 31 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074420):
nothing at all

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074521):
Why are there two different commands then? I would think it may make sense to use `axiom` for things whose type has type `Prop` and `constant` for things whose type has some other type (like a function), but the two examples I've seen are exactly the opposite.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074573):
I.e. `choice` defines a function and is an `axiom` but `propext` defines a (unproven) proof and is a `constant`.

#### [Kevin Buzzard (Dec 31 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154078889):
There's no difference between `theorem` and `lemma` of course. But for constants and axioms I thought the rule of thumb was that constants were for data and axioms for propositions. As you spotted, this convention does not seem to be being followed here

#### [Kevin Buzzard (Dec 31 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154079192):
The main difference between data and propositions in Lean is that Lean remembers how you constructed data but throws away your proof of a proposition and just remembers that it's proved. But of course here with constants and axioms this information doesn't exist, so they feel a lot more similar to each other than theorems and definitions do. If you're brave enough to look at Lean's source code and know enough C++ to understand it then you could maybe just check to see what the difference is.

#### [Gabriel Ebner (Dec 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154079304):
Interestingly enough, `propext` was an `axiom` four years ago: https://github.com/leanprover/lean/blob/0da4f191fc2a37e34d53179d5cf924021de4fd15/library/logic/axioms/propext.lean
But yeah, it doesn't matter that much.  In the C++ code, you could tell the difference between axiom and constant, but this is not really used and not exposed to lean either.  Another difference is that you can do `meta constant` but not `meta axiom`.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080836):
By the way, `propext` and `funext` together prove that all proofs (of a proposition) are equal, don't they? Since `propext` shows that `f(trivial) = trivial, g(trivial) = trivial` for any two functions `f : true \to P` and `g : true \to P`. So does that mean type theories in which proofs are distinct lack `propext`?

#### [Chris Hughes (Dec 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080842):
You don't need any axioms to prove that.

#### [Kevin Buzzard (Dec 31 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080884):
I think the extra "axiom" is not just that all proofs of P are equal, but that they are definitionally equal.

#### [Chris Hughes (Dec 31 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080886):
look at the theorem `proof_irrel`.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080899):
Oh. `rfl` is just anti-climactic.

#### [Kevin Buzzard (Dec 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080938):
:-)

#### [Chris Hughes (Dec 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080939):
But I see actually, even if it wasn't definitional, then propext would imply that anyway.

#### [Chris Hughes (Dec 31 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080950):
Because every true `Prop` would be equal to `true` and `true` has only one proof.

#### [Chris Hughes (Dec 31 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081030):
Proof relevant type theories tend to lack the type `Prop` altogether I think. Proof irrelevance is the only thing distinguishing `Prop` and `Type` so propositions tend to be defined using `Type` and some of them I think have an `is_Prop` predicate that says that the type has only one element.

#### [Kevin Buzzard (Dec 31 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081033):
My recent thoughts about `quot`, and Mario's comments about them (sparked by Chris' observation that I used quot.sound to prove quot'.sound) made all this a bit clearer to me. There is just a whole bunch of stuff which, if you don't have it, would make maths basically impossible to do, and the CS people have made what appears to a mathematician to be a random small set of this stuff into axioms and then deduced all the rest of it. I'm not sure that the fact that propext is an axiom is remotely important.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081242):
```quote
Because every true `Prop` would be equal to `true` and `true` has only one proof.
```
 When I try writing that proof, though, Lean just changes it to `eq.refl H1` (when I print it).

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081244):
```lean
lemma proof_irrel' {a : Prop} (H1 H2 : a) : H1 = H2 :=
begin
  have ta : a = true,
    apply propext, split, { intro, trivial }, { intro, exact H1 },
  rw ta at H1 H2,
end
```

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081245):
(deleted)

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081246):
(deleted)

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081247):
Oh wait, I'm using a rewrite so it tries refl.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081294):
Wasn't there a version of `rw` that didn't try `refl`?

#### [Kenny Lau (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081304):
I think you can tweak the settings

#### [Kevin Buzzard (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081307):
I completely agree that it's a pain to experiment with stuff using `rw` becasue of this refl thing. I think "dunfold" and "delta" unfold functions without trying refl at the end but I don't know about rw.

#### [Chris Hughes (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081313):
I'm not sure this proof would actually work. Substitutions using equality of types are far more complicated and subtle than they might appear.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081426):
```quote
I'm not sure this proof would actually work. Substitutions using equality of types are far more complicated and subtle than they might appear.
```
? Surely rewrite works on `↔`, which is equality of types. E.g.

```lean
example (P Q : Prop) (HP : P) (HPQ : P = Q) : sorry := by { rw HPQ at HP, sorry }
```

#### [Chris Hughes (Dec 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081485):
Actually, it definitely does work.

#### [Chris Hughes (Dec 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081500):
This is the easiest way.
```lean
lemma proof_irrel' {a : Prop} (H1 H2 : a) : H1 = H2 :=
begin
  have ta : a = true,
    apply propext, split, { intro, trivial }, { intro, exact H1 },
  revert H1 H2,
  rw ta,
  
end
```

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081565):
And then use `no_confusion`? Hm, `true` doesn't have no_confusion.

#### [Chris Hughes (Dec 31 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081610):
That's because it's unnecessary. But if there was no proof irrelevance there would be.

#### [Chris Hughes (Dec 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081617):
Actually, this is what you should do.
```lean
lemma proof_irrel' {a : Prop} (H1 H2 : a) : H1 = H2 :=
begin
  have ta : a = true,
    apply propext, split, { intro, trivial }, { intro, exact H1 },
  revert H1 H2,
  rw ta,
  assume H1 H2,
  cases H1, cases H2,
  refl
  
end
```

#### [Chris Hughes (Dec 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081619):
`no_confusion` is usually good for proving things are not equal.

#### [Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081671):
Yeah, I got confused (between the uniqueness of the constructors and their exhaustiveness)

#### [Chris Hughes (Dec 31 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081681):
To illustrate how complicated proof relevant equality can be, try proving this `example` without using `eq` anywhere in the proof. (Hint: it's impossible)
```lean
inductive eq2 {α : Type*} (a : α) : α → Type
| refl : eq2 a

example {α : Type*} (a b : α) (h₁ h₂ : eq2 a b) : eq2 h₁ h₂ := sorry
```

#### [Kenny Lau (Dec 31 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154082070):
```lean
prelude

universe u

notation `Prop` := Sort 0

structure iff (a b : Prop) : Prop :=
(mp : a → b) (mpr : b → a)

inductive eq {α : Sort u} (a : α) : α → Prop
| refl : eq a

infix ` ↔ `:20 := iff
infix ` = `:50 := eq

@[elab_as_eliminator, subst]
lemma eq.subst {α : Sort u} {P : α → Prop} {a b : α} (h₁ : a = b) (h₂ : P a) : P b :=
eq.rec h₂ h₁

infixr ` ▸ `:75 := eq.subst

constant propext {a b : Prop} : (a ↔ b) → (a = b)

inductive true : Prop
| intro : true

lemma proof_irrel {a : Prop} (H1 H2 : a) : H1 = H2 :=
have true = a, from propext ⟨λ _, H1, λ _, true.intro⟩,
(this ▸ (λ H1 H2, true.drec_on H1 (true.drec_on H2 (eq.refl true.intro))) : ∀ H1 H2 : a, H1 = H2) H1 H2
```

#### [Chris Hughes (Dec 31 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154084763):
What does the `subst` attribute do?

#### [Kevin Buzzard (Dec 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154087217):
Where is a complete list of all attributes and their explanations? Oh -- is `[subst]` it only used in core? Are users not supposed to use it?

#### [Kenny Lau (Dec 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154087286):
I have no idea, I just copied the code out of the core library

#### [Patrick Massot (Dec 31 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154088165):
```quote
Proof relevant type theories tend to lack the type `Prop` altogether I think. Proof irrelevance is the only thing distinguishing `Prop` and `Type` so propositions tend to be defined using `Type` and some of them I think have an `is_Prop` predicate that says that the type has only one element.
```
 This is not true. Impredicativity is also an important difference. I think Coq has Prop for this reason, and no definitional proof irrelevance

#### [Chris Hughes (Dec 31 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089302):
What do you mean precisely by impredicativity?

#### [Kevin Buzzard (Dec 31 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089447):
Coq has no definitional proof irrelevance? But does it have proof irrelevance?

#### [Chris Hughes (Dec 31 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089637):
I heard once it was an optional extra like `propext`. Though I guess that means `Prop` would still be special in the sense that any two proofs are not provably unequal.

#### [Mario Carneiro (Dec 31 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096231):
right, you have to have this property if impredicativity is to be consistent

#### [Mario Carneiro (Dec 31 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096238):
because if a type has two elements, then you can build a cantor's paradox sort of thing using impredicativity

#### [Chris Hughes (Dec 31 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096291):
What does impredicativity mean precisely?

#### [Mario Carneiro (Dec 31 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096563):
`forall x : A, P : Prop` if `P : Prop`

#### [Mario Carneiro (Dec 31 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096566):
even if `A : Type`

#### [Mario Carneiro (Dec 31 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096610):
this means that propositions can quantify over themselves

#### [Kevin Buzzard (Dec 31 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096683):
`(forall x : A, P) : Prop` is what we're talking about here, presumably. The universe isn't the max, it's the imax.

#### [Mario Carneiro (Dec 31 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096698):
in a predicative universe, the pi type has level max of the universe levels of the parts

#### [Mario Carneiro (Dec 31 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096701):
but we have this funny imax thing for level 0

#### [Abhimanyu Pallavi Sudhir (Jan 01 2019 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114592):
```quote
this means that propositions can quantify over themselves
```
 Isn't that just `P → P`?

#### [Abhimanyu Pallavi Sudhir (Jan 01 2019 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114602):
Even with functions between types, the type of `P → Q` is the types of `P` and `Q`, so I don't understand why this makes `Prop` special.

#### [Mario Carneiro (Jan 01 2019 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114948):
I mean a function whose domain of quantification includes itself

#### [Mario Carneiro (Jan 01 2019 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154115111):
which permits self application
```lean
def p : ∀ ⦃p : Prop⦄, p → p = p := λ x _, rfl
def X := p p
```

#### [Mario Carneiro (Jan 01 2019 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154115115):
you can use this to do a variety of diagonalization type arguments

#### [Kenny Lau (Jan 01 2019 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154116038):
@**Abhimanyu Pallavi Sudhir** if you quantify over all `Type`, you get `Type 1`

#### [Reid Barton (Jan 01 2019 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129709):
A classic example of an impredicative definition of a Prop is defining the subgroup generated by a subset S of a group G to be the intersection of all the subgroups of G which contain S

#### [Reid Barton (Jan 01 2019 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129773):
which is to say `def belongs_to_subgroup_generated_by (S : set G) (x : G) : Prop := \forall (P : G \to Prop), is_subgroup P \and (\forall y, S y \to P y) \to P x`

#### [Reid Barton (Jan 01 2019 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129817):
If `Prop` had a universe hierarchy like `Type`, you wouldn't be allowed to use the same `Prop` on both sides of that equation

#### [Chris Hughes (Jan 01 2019 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129832):
It hadn't occurred to me how important this was.

#### [Kenny Lau (Jan 01 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129986):
of course it hadn't, you guys don't even care about foundations / of course it hadn't, this is hard core logic stuff

#### [Reid Barton (Jan 01 2019 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130031):
It's really hard to imagine from a classical perspective how anyone could object to the construction "take all the subsets of G, keep the ones which are subgroups containing S, and form their intersection".

#### [Reid Barton (Jan 01 2019 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130032):
Before using Lean, I was not convinced that "impredicative" meant anything at all.

#### [Kenny Lau (Jan 01 2019 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130044):
From a "classical perspective", you run into issues like Δ0-predicates are absolute

#### [Kenny Lau (Jan 01 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130092):
that somehow P(ω) (i.e. powerset of ω) is not absolute

#### [Kenny Lau (Jan 01 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130094):
because taking powerset is not a predicative thing to do

#### [Reid Barton (Jan 01 2019 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130151):
Right, well, so the conclusion is that caring about predicativity is not a math thing to do.

#### [Reid Barton (Jan 01 2019 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130166):
Especially since this example of an impredicative definition is something that one will encounter in a first course on algebra, it's not some scary thing involving universes or whatever.

#### [Kenny Lau (Jan 01 2019 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130173):
mathematicians have gone too far, doing impredicative stuff like that

#### [Kenny Lau (Jan 01 2019 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130179):
how are they going to compute their examples if their definitions are impredicative

#### [Kevin Buzzard (Jan 01 2019 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130229):
who cares about examples? We want theorems!

#### [Kenny Lau (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130240):
what do you want theorems for?

#### [Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130245):
fun

#### [Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130247):
and promotion

#### [Kenny Lau (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130248):
wasn't number theory created to solve diophantine equations

#### [Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130253):
yes but now its job is to create theorems explaining what the structure of the solutions is

#### [Kevin Buzzard (Jan 01 2019 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130292):
because solving them all turned out to be too hard

#### [Kenny Lau (Jan 01 2019 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130294):
but now your impredicative definitions are not helping us to solve the equations, because they are incomputable

#### [Kevin Buzzard (Jan 01 2019 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130303):
yes but we don't care about solving them because that's too hard. We now care about whether the solutions lie on some union of simple subvarieties or something. Nobody will get promoted for solving a Diophantine equation.

#### [Kenny Lau (Jan 01 2019 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130343):
Can you compute the integers of Q[X]/(X^3-3X+1)?

#### [Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130349):
sure, I read an algorithm to do that once

#### [Kenny Lau (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130358):
that doesn't mean you can compute it

#### [Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130359):
it's in Cohen's book on computational number theory

#### [Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130362):
sure it means I can compute it

#### [Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130364):
I just ask a PhD student to compute it for me

#### [Kenny Lau (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130367):
that isn't **you** computing it

#### [Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130372):
I think you have a lot to learn about the real world

#### [Chris Hughes (Jan 01 2019 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130934):
Lean is designed for computer science, so impredicative definitions can't be that useless from a computational perspective. You can't compute with them, but you can still use them to help prove your program does what it's supposed to.

#### [Mario Carneiro (Jan 01 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132613):
By the way, HoTT uses predicative universes only (in the usual setup), so if you thought it would be a great thing that solves all your problems then this is one place where it isn't all sunshine and roses

#### [Mario Carneiro (Jan 01 2019 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132623):
Also Agda makes a big deal about being 100% predicative

#### [Mario Carneiro (Jan 01 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132730):
It's true that in regular math predicativity doesn't really come up, but it shows up in non-absoluteness like Kenny says, or in model theory where adding more ordinals causes new subsets of nat to appear... you have this weird situation where you've built the set but not the elements, and that's where things like Cohen reals come from

#### [Mario Carneiro (Jan 01 2019 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132796):
Also, we've discussed impredicative encodings of inductive types before, like `xnat : Type := \all X : Type, X -> (X -> X) -> X`, which doesn't typecheck in lean because `Type` is predicative

#### [Mario Carneiro (Jan 01 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132846):
Or when we have an object that is "defined by a universal property" and we want to just write that property but it doesn't work because the universe quantifier isn't large enough, so instead we re-express it by some kind of construction "from below"... that's predicativity

