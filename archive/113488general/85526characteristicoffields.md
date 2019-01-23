---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85526characteristicoffields.html
---

## Stream: [general](index.html)
### Topic: [characteristic of fields](85526characteristicoffields.html)

---


{% raw %}
#### [ Kenny Lau (Oct 16 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921382):
@**Mario Carneiro** @**Johan Commelin** @**Kevin Buzzard** how should we define the `char` of a field?

#### [ Mario Carneiro (Oct 16 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921432):
I think your definition should be on semirings instead of zero/one/mul classes

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921541):
I guess it could be on rings, since a nonzero characteristic semiring is a ring

#### [ Chris Hughes (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921546):
Should it be a class or just a Prop?

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921574):
a prop, it is a prop

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921587):
oh wait you aren't asking about `char_p`

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921653):
both

#### [ Chris Hughes (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921654):
I'm asking about `char`.

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921657):
I'm asking about this thing in general

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921670):
how did metamath / other languages deal with this?

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921676):
and is char(Q) 0 or 1?

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921705):
char(Q) is 0

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921712):
in where?

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921720):
in metamath

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921723):
and in math

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921730):
but how is char defined?

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921736):
I feel like there's 1,000,000 subtleties

#### [ Mario Carneiro (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921739):
the order of 1

#### [ Kenny Lau (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921811):
how is order defined?

#### [ Chris Hughes (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921818):
We don't have `order_of` on non finite groups

#### [ Mario Carneiro (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921840):
and the order of a group element is the smallest nonzero power of the element that is 1

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921850):
or 0 if it doesn't exist

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921852):
so that's a `def` not a `prop`?

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921861):
ok I don't like this

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921866):
metamath doesn't care about computability tho

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921867):
do we have another approach?

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921873):
there is a computable definition yielding a `roption nat`

#### [ Mario Carneiro (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921939):
and if we define `get_or_else` for `roption` then we can make it 0 otherwise

#### [ Kenny Lau (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921988):
would it be usable?

#### [ Mario Carneiro (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922050):
I am a fan of `roption` definitions; it would give you a relational interface

#### [ Mario Carneiro (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922054):
`p \in char R`

#### [ Kevin Buzzard (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922092):
The characteristic of a ring is the kernel of the canonical ring homomorphism from the integers to the ring.

#### [ Mario Carneiro (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922108):
there is also the ideal option

#### [ Kenny Lau (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922114):
```quote
The characteristic of a ring is the kernel of the canonical ring homomorphism from the integers to the ring.
```
next

#### [ Kevin Buzzard (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922123):
That's the best definition.

#### [ Mario Carneiro (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922145):
that's just restating x^n = 0 though

#### [ Mario Carneiro (Oct 16 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922199):
maybe a better question is not what is the characteristic but what is it for

#### [ Mario Carneiro (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922241):
We have PID defined, right? Is it constructive exists?

#### [ Kenny Lau (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922259):
```lean
class is_principal_ideal (S : set α) : Prop :=
(principal : ∃ a : α, S = {x | a ∣ x})

class principal_ideal_domain (α : Type*) extends integral_domain α :=
(principal : ∀ (S : set α) [is_ideal S], is_principal_ideal S)
```

#### [ Kenny Lau (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922262):
yes

#### [ Mario Carneiro (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922273):
well no

#### [ Kevin Buzzard (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922280):
That looks right to me. Is Mario asking about whether there's a function from ideals to generators though?

#### [ Mario Carneiro (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922284):
yeah

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922332):
A maths PID is what Kenny just quoted.

#### [ Mario Carneiro (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922341):
I guess there is no constructive proof that Z is a PID then?

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922345):
Of course the notion of PID was not invented by constructivists.

#### [ Kenny Lau (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922350):
nothing involving arbitrary sets can be constructive

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922351):
History is written by the victors

#### [ Mario Carneiro (Oct 16 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922383):
that's not exactly true kenny, it's possible that the ideal structure can be leveraged to give a generator

#### [ Kevin Buzzard (Oct 16 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922388):
```quote
I guess there is no constructive proof that Z is a PID then?
```
The standard proof in textbooks ("if the ideal is zero then done, if not then choose the smallest positive integer") is constructive.

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922440):
well, constructive with LEM

#### [ Kenny Lau (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922465):
you can't decide if the ideal is zero

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922466):
you can't determine if an arbitrary ideal is zero

#### [ Kevin Buzzard (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922471):
In Z??

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922475):
that's exactly the problem with defining characteristic

#### [ Kenny Lau (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922477):
give me an algorithm

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922490):
the set of periods of an element is an ideal of Z

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922500):
but you can't tell if it is zero

#### [ Kevin Buzzard (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922506):
I'm not going to talk about this any more. It's silly.

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922511):
I think we have our answer Kenny

#### [ Kevin Buzzard (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922516):
:-)

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922518):
totalize it

#### [ Kenny Lau (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922565):
could you summarize the answer?

#### [ Kevin Buzzard (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922575):
Are you going to assume LEM?

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922576):
char Q = 0

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922579):
`noncomputable`

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922584):
live with it

#### [ Kenny Lau (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922598):
no roption?

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922599):
if you insist, you can define `char' A : roption nat`

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922611):
and define `char` in terms of it

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922615):
but most of the theory will be about `char`

#### [ Kenny Lau (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922618):
it won't be a class then

#### [ Patrick Massot (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922620):
`kenny_char : roption Prop` (because who knows?)

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922637):
also, `char` is a type

#### [ Kenny Lau (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922640):
but every ring has a unique char

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922649):
characters

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922699):
there is also the ideal definition, dunno how useful it is but that's constructive too

#### [ Patrick Massot (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922704):
Let's write it in French then! `car`

#### [ Kenny Lau (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922705):
I mean, it's useful to make "char A = p" into a class

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922710):
I agree on that

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922715):
`char_p` is fine and unproblematic

#### [ Kenny Lau (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922719):
oh ok

#### [ Reid Barton (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922722):
```quote
but every ring has a unique char
```
isn't this not true constructively? or am I really confused

#### [ Mario Carneiro (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922744):
no, that's true

#### [ Kenny Lau (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922750):
I'm talking about the reason to make it into a typeclass

#### [ Mario Carneiro (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922760):
if a ring has two characteristics then they are equal

#### [ Kenny Lau (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922763):
```lean
class char_p (α : Type u) [has_zero α] [has_one α] [has_add α] (p : ℕ) : Prop :=
(cast_eq_zero : (p:α) = 0)
```
Do we all agree that this definition is deficit?

#### [ Reid Barton (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922770):
It's the "has" part I am worried about

#### [ Reid Barton (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922780):
I agree "unique" is okay.

#### [ Mario Carneiro (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922831):
no you can't prove existence of a characteristic (number) in general without LEM

#### [ Mario Carneiro (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922835):
the ideal is fine of course

#### [ Reid Barton (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922838):
right, okay

#### [ Reid Barton (Oct 16 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923259):
```quote
I guess there is no constructive proof that Z is a PID then?
```
I think you can even prove constructively that "Z is a PID" => LEM

#### [ Reid Barton (Oct 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923313):
by taking a proposition P and defining the ideal I = {x | x = 0 \/ P}

#### [ Reid Barton (Oct 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923331):
and then looking at whether its generator is zero or not

#### [ Kenny Lau (Oct 16 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923475):
```lean
class char_p (α : Type u) [semiring α] (p : ℕ) : Prop :=
(cast_eq_zero_iff : ∀ x:ℕ, (x:α) = 0 ↔ p ∣ x)
```

#### [ Kenny Lau (Oct 16 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923477):
how about this

#### [ Kenny Lau (Oct 16 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923619):
```lean
class char_p (α : Type u) [semiring α] (p : ℕ) : Prop :=
(cast_eq_zero_iff : ∀ x:ℕ, (x:α) = 0 ↔ p ∣ x)

theorem char_p.cast_eq_zero {α : Type u} [semiring α] {p : ℕ} [char_p α p] : (p:α) = 0 :=
(char_p.cast_eq_zero_iff α p p).2 (dvd_refl p)

theorem char_p.eq (α : Type u) [semiring α] (p q : ℕ) [char_p α p] [char_p α q] : p = q :=
nat.dvd_antisymm
  ((char_p.cast_eq_zero_iff α p q).1 char_p.cast_eq_zero)
  ((char_p.cast_eq_zero_iff α q p).1 char_p.cast_eq_zero)
```

#### [ Kenny Lau (Oct 16 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923715):
```quote
I think your definition should be on semirings instead of zero/one/mul classes
```
but `char_zero` is defined on `[add_monoid \a] [has_one \a]`?

#### [ Mario Carneiro (Oct 16 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135924255):
or that

#### [ Kenny Lau (Oct 16 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135924367):
existe uma diferencia?

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925799):
```lean
class char_p (α : Type u) [semiring α] (p : ℕ) : Prop :=
(cast_eq_zero_iff : ∀ x:ℕ, (x:α) = 0 ↔ p ∣ x)

theorem char_p.cast_eq_zero (α : Type u) [semiring α] (p : ℕ) [char_p α p] : (p:α) = 0 :=
(char_p.cast_eq_zero_iff α p p).2 (dvd_refl p)

theorem char_p.eq (α : Type u) [semiring α] (p q : ℕ) [char_p α p] [char_p α q] : p = q :=
nat.dvd_antisymm
  ((char_p.cast_eq_zero_iff α p q).1 (char_p.cast_eq_zero _ _))
  ((char_p.cast_eq_zero_iff α q p).1 (char_p.cast_eq_zero _ _))

instance char_p.of_char_zero (α : Type u) [semiring α] [char_zero α] : char_p α 0 :=
⟨λ x, by rw [zero_dvd_iff, ← nat.cast_zero, nat.cast_inj]⟩

theorem char_p.exists (α : Type u) [semiring α] : ∃ p, char_p α p :=
by letI := classical.dec_eq α; exact
classical.by_cases
  (assume H : ∀ p:ℕ, (p:α) = 0 → p = 0, ⟨0,
    ⟨λ x, by rw [zero_dvd_iff]; exact ⟨H x, by rintro rfl; refl⟩⟩⟩)
  (λ H, ⟨nat.find (classical.not_forall.1 H), ⟨λ x,
    ⟨λ H1, nat.dvd_of_mod_eq_zero (by_contradiction $ λ H2,
      nat.find_min (classical.not_forall.1 H)
        (nat.mod_lt x $ nat.pos_of_ne_zero $ not_of_not_imp $
          nat.find_spec (classical.not_forall.1 H))
        (not_imp_of_and_not ⟨by rwa [← nat.mod_add_div x (nat.find (classical.not_forall.1 H)),
          nat.cast_add, nat.cast_mul, of_not_not (not_not_of_not_imp $ nat.find_spec (classical.not_forall.1 H)),
          zero_mul, add_zero] at H1, H2⟩)),
    λ H1, by rw [← nat.mul_div_cancel' H1, nat.cast_mul,
      of_not_not (not_not_of_not_imp $ nat.find_spec (classical.not_forall.1 H)), zero_mul]⟩⟩⟩)

theorem char_p.exists_unique (α : Type u) [semiring α] : ∃! p, char_p α p :=
let ⟨c, H⟩ := char_p.exists α in
⟨c, H, λ y H2, by resetI; apply char_p.eq α⟩
```

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925803):
How does this look? @**Mario Carneiro** @**Patrick Massot**

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925816):
@**Kevin Buzzard**

#### [ Kevin Buzzard (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925950):
```quote
```lean
class char_p (α : Type u) [semiring α] (p : ℕ) : Prop :=
(cast_eq_zero_iff : ∀ x:ℕ, (x:α) = 0 ↔ p ∣ x)
```
```
I see you went for the ideal idea after all ;-)

#### [ Mario Carneiro (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925962):
`char_p.eq` should definitely not have square brackets

#### [ Kevin Buzzard (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925979):
`is_char_p`?

#### [ Mario Carneiro (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926065):
Maybe it should be a property of Z, then you can literally say `is_ideal (char_p A)`

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926427):
wait I'm confused

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926429):
```lean
theorem char_p.eq (α : Type u) [semiring α] (p q : ℕ) (c1 : char_p α p) (c2 : char_p α q) : p = q :=
nat.dvd_antisymm
  ((char_p.cast_eq_zero_iff α p q).1 (char_p.cast_eq_zero _ _))
  ((char_p.cast_eq_zero_iff α q p).1 (char_p.cast_eq_zero _ _))
```

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926434):
how can the proof still work now that I turned `[]` to `()`?

#### [ Mario Carneiro (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926462):
maybe kevin knows... I told him the solution to this puzzle a few weeks ago

#### [ Kenny Lau (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926477):
anyway how is this now?
```lean
class char_p (α : Type u) [semiring α] (p : ℕ) : Prop :=
(cast_eq_zero_iff : ∀ x:ℕ, (x:α) = 0 ↔ p ∣ x)

theorem char_p.cast_eq_zero (α : Type u) [semiring α] (p : ℕ) [char_p α p] : (p:α) = 0 :=
(char_p.cast_eq_zero_iff α p p).2 (dvd_refl p)

theorem char_p.eq (α : Type u) [semiring α] {p q : ℕ} (c1 : char_p α p) (c2 : char_p α q) : p = q :=
nat.dvd_antisymm
  ((char_p.cast_eq_zero_iff α p q).1 (char_p.cast_eq_zero _ _))
  ((char_p.cast_eq_zero_iff α q p).1 (char_p.cast_eq_zero _ _))

instance char_p.of_char_zero (α : Type u) [semiring α] [char_zero α] : char_p α 0 :=
⟨λ x, by rw [zero_dvd_iff, ← nat.cast_zero, nat.cast_inj]⟩

theorem char_p.exists (α : Type u) [semiring α] : ∃ p, char_p α p :=
by letI := classical.dec_eq α; exact
classical.by_cases
  (assume H : ∀ p:ℕ, (p:α) = 0 → p = 0, ⟨0,
    ⟨λ x, by rw [zero_dvd_iff]; exact ⟨H x, by rintro rfl; refl⟩⟩⟩)
  (λ H, ⟨nat.find (classical.not_forall.1 H), ⟨λ x,
    ⟨λ H1, nat.dvd_of_mod_eq_zero (by_contradiction $ λ H2,
      nat.find_min (classical.not_forall.1 H)
        (nat.mod_lt x $ nat.pos_of_ne_zero $ not_of_not_imp $
          nat.find_spec (classical.not_forall.1 H))
        (not_imp_of_and_not ⟨by rwa [← nat.mod_add_div x (nat.find (classical.not_forall.1 H)),
          nat.cast_add, nat.cast_mul, of_not_not (not_not_of_not_imp $ nat.find_spec (classical.not_forall.1 H)),
          zero_mul, add_zero] at H1, H2⟩)),
    λ H1, by rw [← nat.mul_div_cancel' H1, nat.cast_mul,
      of_not_not (not_not_of_not_imp $ nat.find_spec (classical.not_forall.1 H)), zero_mul]⟩⟩⟩)

theorem char_p.exists_unique (α : Type u) [semiring α] : ∃! p, char_p α p :=
let ⟨c, H⟩ := char_p.exists α in
⟨c, H, λ y H2, char_p.eq α H2 H⟩
```

#### [ Mario Carneiro (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926549):
`char_p.exists` should be defining a function... called `char`

#### [ Kenny Lau (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926554):
we can functionize that

#### [ Kevin Buzzard (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926587):
He told Johannes too.

#### [ Kenny Lau (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926599):
```
invalid definition, a declaration named 'char' has already been declared
```

#### [ Kenny Lau (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926600):
hard luck

#### [ Kenny Lau (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926906):
```lean
noncomputable def ring_char (α : Type u) [semiring α] : ℕ :=
classical.some (char_p.exists_unique α)

theorem ring_char.spec (α : Type u) [semiring α] : ∀ x:ℕ, (x:α) = 0 ↔ ring_char α ∣ x :=
by letI := (classical.some_spec (char_p.exists_unique α)).1;
unfold ring_char; exact char_p.cast_eq_zero_iff α (ring_char α)

theorem ring_char.eq (α : Type u) [semiring α] {p : ℕ} (C : char_p α p) : p = ring_char α :=
(classical.some_spec (char_p.exists_unique α)).2 p C
```

#### [ Kenny Lau (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926909):
how is this?

#### [ Kevin Buzzard (Oct 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927432):
```quote
how can the proof still work now that I turned `[]` to `()`?
```
Type class inference just grabs anything it can find to the left of the colon. The round and square brackets are just for the signature of the theorem, they don't affect how type class inference works in the proof. This is not so well-known because it's not common to put a typeclass left of the colon and not in a square bracket.

#### [ Kevin Buzzard (Oct 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927447):
I discovered it a few weeks ago when I was trying to understand Patrick's type class hell with his completions and had exactly the same reaction.

#### [ Kevin Buzzard (Oct 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927490):
I've had to construct that argument from memory because my search for the conversation failed. Hopefully it's some sort of approximation to the truth.

#### [ Bryan Gin-ge Chen (Oct 16 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927856):
I guess it's [this conversation?](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261338) I found it by searching for "left of colon".

#### [ Kenny Lau (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927950):
@**Mario Carneiro** Could you help me with some typeclass problems? It's in L324 here: https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean#L324

#### [ Kenny Lau (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927966):
Lean can't figure out the coercion in `(↑x : perfect_closure α p)`

#### [ Kevin Buzzard (Oct 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928018):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261591

#### [ Kevin Buzzard (Oct 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928021):
You owe Mario a light bulb

#### [ Kenny Lau (Oct 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928069):
done

#### [ Kevin Buzzard (Oct 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928099):
(thanks Bryan)

#### [ Kenny Lau (Oct 16 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928788):
@**Mario Carneiro** never mind it's stupid


{% endraw %}
