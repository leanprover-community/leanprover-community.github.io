---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05512Transferhomomorphism.html
---

## [maths](index.html)
### [Transfer homomorphism](05512Transferhomomorphism.html)

#### [Kenny Lau (Jun 15 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127678):
Let G be a group and H a subgroup of finite index. Then, pick a set-theoretic section s:G/H->G where G/H is the right cosets. Then, the transfer homomorphism G^ab -> H^ab is defined by sending [[g]] to prod[x in G/H] s(x) g s(xg)^-1.

#### [Kenny Lau (Jun 15 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127688):
The wonderful thing about this homomorphism is that it is independent of the section s

#### [Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127734):
but this also means that I will be lifting arbitrarily many quotients.

#### [Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127738):
How should I do that?

#### [Mario Carneiro (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127753):
using choice

#### [Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127757):
but it will be noncomputable

#### [Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127765):
obviously

#### [Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127769):
can I make it computable?

#### [Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127773):
nothing about what you said sounds remotely computable

#### [Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127776):
it seems computable to me

#### [Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127781):
the map is independent of s

#### [Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127784):
there is only finitely many choices to make

#### [Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127789):
How do you even know such a function `s` exists?

#### [Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127833):
you don't need the function s. you just need to lift finitely many quotients

#### [Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127837):
obviously s is noncomputable

#### [Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127839):
but the transfer homomorphism should be computable

#### [Mario Carneiro (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127843):
How is G^ab defined

#### [Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127847):
G quotient G commutator

#### [Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127851):
G/[G,G]

#### [Mario Carneiro (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127866):
And in what sense is G/H finite

#### [Kenny Lau (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127881):
in the sense that H is a finite-index subgroup of G

#### [Kenny Lau (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127885):
so G/H is a fintype

#### [Mario Carneiro (Jun 15 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127954):
I mean, how are you expressing "finite index"

#### [Kenny Lau (Jun 15 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127956):
[fintype G/H]

#### [Mario Carneiro (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127976):
And how do you construct a section?

#### [Kenny Lau (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127978):
I don't

#### [Mario Carneiro (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127979):
Any section at all

#### [Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128127982):
section is noncomputable

#### [Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128022):
but the transfer homomorphism is independent of section

#### [Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128025):
so I need finitely many lifts

#### [Mario Carneiro (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128034):
Even ignoring the lifts

#### [Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128046):
I can't construct any section computably

#### [Kenny Lau (Jun 15 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128053):
if that's what you mean

#### [Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128081):
I think I see what you mean with iterating lifts, that might be possible

#### [Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128113):
hmm

#### [Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128118):
but it will be very hard

#### [Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128119):
But you will have to redo the work of `finset.pi`

#### [Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128120):
each element of the product is not well-defined

#### [Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128123):
it is the product itself which is well-defined

#### [Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128127):
You have a single quotient in the output

#### [Mario Carneiro (Jun 15 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128148):
or even a `trunc`, if you express the section property in a subtype

#### [Mario Carneiro (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128197):
Do you have decidable equality on G/H?

#### [Kenny Lau (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128202):
is that necessary?

#### [Kenny Lau (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128210):
I feel that it is already computable

#### [Mario Carneiro (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128212):
it comes up in the construction of the functions

#### [Kenny Lau (Jun 15 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128247):
how would you do it?

#### [Mario Carneiro (Jun 15 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128310):
I am reminded of a discussion with @**Gabriel Ebner** about generalizing the quotient axioms to allow for indexed families of quotients

#### [Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128314):
but everything is finite here

#### [Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128321):
the axioms should be enough

#### [Mario Carneiro (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128324):
But it's provable in the finite case, and that's what I would prove

#### [Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128328):
hmm

#### [Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128330):
this is very hard

#### [Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128332):
can I even do this in 3 days

#### [Mario Carneiro (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128339):
It's less than 100 lines for sure

#### [Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128430):
Also, decidable equality is definitely necessary for constructing sections

#### [Kenny Lau (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128439):
I don't want to construct any section

#### [Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128445):
You do, that's the whole point

#### [Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128453):
You are lifting stuff from a quotient but that's not so important

#### [Kenny Lau (Jun 15 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128510):
hmm

#### [Mario Carneiro (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128520):
Are you suggesting that there is a way to define the transfer that avoids reference to any section?

#### [Kenny Lau (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128525):
If I do a product indexed by a fintype do I need decidable equality?

#### [Mario Carneiro (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128530):
I assume you have to make coordinated choices in order to define the sums

#### [Kenny Lau (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128535):
but everything is finite

#### [Mario Carneiro (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128620):
No, products of elements in a commutative group over a finset does not require decidable_eq

#### [Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128626):
then why do I need it now

#### [Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128629):
even if the choice is coordinated

#### [Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128631):
it's still finite

#### [Mario Carneiro (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128637):
to define the section that coordinates the choices

#### [Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128642):
but everything is well-defined

#### [Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128690):
How are you going to remember your finitely many choices if not with a function? And how is that function indexed?

#### [Kenny Lau (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128694):
isn't it the philosophy of quotient that if your choices are well-defined then you are computable?

#### [Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128703):
That's not the problem

#### [Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128708):
You want a function G/H -> G

#### [Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128717):
list.rec is computable

#### [Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128718):
multiset.rec is computable

#### [Mario Carneiro (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128719):
that means distinguishing elements of G/H when they are sent to different members of G

#### [Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128721):
finset.rec is computable

#### [Kenny Lau (Jun 15 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128128806):
hmm

#### [Mario Carneiro (Jun 15 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129541):
Here's a way to state the section property without groups:
```
def choices {ι : Type*} [fintype ι] {α : ι → Type*} (R : ∀ i, α i → α i → Prop)
    (f : ∀ i, quot (R i)) : quot (λ (a b : Π i, α i), ∀ i, R i (a i) (b i)) := sorry
```

#### [Kenny Lau (Jun 15 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129595):
I only have one quotient though

#### [Kenny Lau (Jun 15 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129601):
it's just G/H

#### [Mario Carneiro (Jun 15 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129610):
That doesn't make too much of a difference

#### [Mario Carneiro (Jun 15 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129673):
The point here is the interchanging of pi and quot

#### [Kenny Lau (Jun 15 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129683):
I see

#### [Mario Carneiro (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129782):
It seems reasonable to have that function as a computable axiom, this is what Gabriel and I discussed

#### [Kenny Lau (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129786):
I see

#### [Mario Carneiro (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129787):
because it has an obvious VM interpretation

#### [Kenny Lau (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129793):
but is it provable?

#### [Mario Carneiro (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129794):
but you can only prove it for I finite

#### [Mario Carneiro (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128129806):
and even then I believe it implies decidable equality of I

#### [Kevin Buzzard (Jun 15 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130433):
Kenny, if you are under time constraints, why not just make it noncomputable, make sure everything else is done, and come back to it later if you have time?

#### [Mario Carneiro (Jun 15 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130542):
I will look into this theorem, and report back if I can prove it. Feel free to assume it

#### [Reid Barton (Jun 15 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130568):
This version is not quite right though, because for example one of the `R i` could be the empty relation, and then the "product relation" is also empty

#### [Reid Barton (Jun 15 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130653):
You need to assume the `R i` are at least reflexive, or build the "product relation" differently, like the Cartesian product of graphs

#### [Mario Carneiro (Jun 15 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130733):
That's fine, `quot` implicitly takes the equivalence closure of the given relation

#### [Mario Carneiro (Jun 15 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130750):
`quotient` is the variant that explicitly assumes the relation is an equivalence already

#### [Reid Barton (Jun 15 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130797):
But, say, `R 1` might be nontrivial, while `R 2` is empty, and then `λ (a b : Π i, α i), ∀ i, R i (a i) (b i)` is empty, so we haven't made any identifications in `\a 1 \x \a 2`

#### [Reid Barton (Jun 15 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130830):
then we'd have a map `quot (R 1) \to \a 1`. Or is that okay?

#### [Mario Carneiro (Jun 15 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130903):
I see, yes that's bad

#### [Mario Carneiro (Jun 15 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130919):
So maybe just replace`quot` with `quotient` everywhere

#### [Mario Carneiro (Jun 15 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128130929):
although then I have to show that the pi of equivalences is an equivalence

#### [Mario Carneiro (Jun 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128131542):
Here's the noncomputable version:
```
instance pi_setoid {ι : Type*} {α : ι → Type*} [∀ i, setoid (α i)] : setoid (Π i, α i) :=
{ r := λ a b, ∀ i, a i ≈ b i,
  iseqv := ⟨
    λ a i, setoid.refl _,
    λ a b h i, setoid.symm (h _),
    λ a b c h₁ h₂ i, setoid.trans (h₁ _) (h₂ _)⟩ }

noncomputable def quotient.choice {ι : Type*} {α : ι → Type*} [S : ∀ i, setoid (α i)]
  (f : ∀ i, quotient (S i)) : @quotient (Π i, α i) (by apply_instance) :=
⟦λ i, (f i).out⟧

theorem quotient.choice_eq {ι : Type*} {α : ι → Type*} [∀ i, setoid (α i)]
  (f : ∀ i, α i) : quotient.choice (λ i, ⟦f i⟧) = ⟦f⟧ :=
quotient.sound $ λ i, quotient.mk_out _
```

#### [Mario Carneiro (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136633):
> Let G be a group and H a subgroup of finite index. Then, pick a set-theoretic section s:G/H->G where G/H is the right cosets. Then, the transfer homomorphism G^ab -> H^ab is defined by sending [[g]] to prod[x in G/H] s(x) g s(xg)^-1.

Shouldn't there be a [[]] in the definition there somewhere?

#### [Kenny Lau (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136644):
by sending [[g]] to [[prod[x in G/H] s(x) g s(xg)^-1]].

#### [Mario Carneiro (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136655):
Does `[[g h]] = [[g]][[h]]`?

#### [Kenny Lau (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136663):
yes

#### [Mario Carneiro (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136679):
Then don't the `s(x)` parts cancel?

#### [Kenny Lau (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136684):
@**Kevin Buzzard**

#### [Mario Carneiro (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136736):
`[[prod[x in G/H] s(x) g s(xg)^-1]] = (prod[x in G/H] [[s(x)]]) (prod[x in G/H] [[g]]) (prod[x in G/H] [[s(xg)]]^-1)`

#### [Mario Carneiro (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136747):
and `prod[x in G/H] [[s(xg)]]^-1 = prod[x in G/H] [[s(x)]]^-1` by reindexing

#### [Kenny Lau (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136748):
oh you can't do that, g is not in H

#### [Kenny Lau (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136762):
s(x) g s(xg)^-1 is in H

#### [Mario Carneiro (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136768):
I know, but they should still be equal as members of G

#### [Kenny Lau (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128136779):
no, because H^ab is H/[H,H]

#### [Mario Carneiro (Jun 15 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128137621):
Okay, I think I have something close to a proof that decidable_eq of the coset relation is necessary. Suppose you know `fintype G/H`. Ignoring quotients for a moment, thinking "computationally", this is essentially a list of elements of G which chooses exactly one element of every coset (or, if you prefer, a bijection (not an equiv) from fin n to G/H). Now that looks like the section we want, but the problem is the computation of s(xg) that we need later. The function x |-> xg is a permutation of G/H which corresponds to a permutation of the list s, but computationally it's not that easy since if we take our representative s(x) and multiply by g we get s(x)g, which is in the same coset as s(xg) but is not usually the same. So we need a way of searching our list s to find the value that is in the same coset as s(x)g, and there is no way to do this from the given data.

#### [Kenny Lau (Jun 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128141785):
I see. Then I'll just come up with a section noncomputably then.

#### [Mario Carneiro (Jun 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128141854):
Here's the computable version of that theorem:
```
def quotient.fin_choice_aux {ι : Type*} [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)] :
  ∀ (l : list ι), (∀ i ∈ l, quotient (S i)) → @quotient (Π i ∈ l, α i) (by apply_instance)
| []     f := ⟦λ i, false.elim⟧
| (i::l) f := begin
  refine quotient.lift_on₂ (f i (list.mem_cons_self _ _))
    (quotient.fin_choice_aux l (λ j h, f j (list.mem_cons_of_mem _ h)))
    _ _,
  exact λ a l, ⟦λ j h,
    if e : j = i then by rw e; exact a else
    l _ (h.resolve_left e)⟧,
  refine λ a₁ l₁ a₂ l₂ h₁ h₂, quotient.sound (λ j h, _),
  by_cases e : j = i; simp [e],
  { subst j, exact h₁ },
  { exact h₂ _ _ }
end

theorem quotient.fin_choice_aux_eq {ι : Type*} [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)] :
  ∀ (l : list ι) (f : ∀ i ∈ l, α i), quotient.fin_choice_aux l (λ i h, ⟦f i h⟧) = ⟦f⟧
| []     f := quotient.sound (λ i h, h.elim)
| (i::l) f := begin
  simp [quotient.fin_choice_aux, quotient.fin_choice_aux_eq l],
  refine quotient.sound (λ j h, _),
  by_cases e : j = i; simp [e],
  subst j, refl
end

def quotient.fin_choice {ι : Type*} [fintype ι] [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)]
  (f : ∀ i, quotient (S i)) : @quotient (Π i, α i) (by apply_instance) :=
quotient.lift_on (@quotient.rec_on _ _ (λ l : multiset ι,
    @quotient (Π i ∈ l, α i) (by apply_instance))
    finset.univ.1
    (λ l, quotient.fin_choice_aux l (λ i _, f i))
    (λ a b h, begin
      have := λ a, quotient.fin_choice_aux_eq a (λ i h, quotient.out (f i)),
      simp [quotient.out_eq] at this,
      simp [this],
      let g := λ a:multiset ι, ⟦λ (i : ι) (h : i ∈ a), quotient.out (f i)⟧,
      refine eq_of_heq ((eq_rec_heq _ _).trans (_ : g a == g b)),
      congr' 1, exact quotient.sound h,
    end))
  (λ f, ⟦λ i, f i (finset.mem_univ _)⟧)
  (λ a b h, quotient.sound $ λ i, h _ _)


theorem quotient.fin_choice_eq {ι : Type*} [fintype ι] [decidable_eq ι]
  {α : ι → Type*} [∀ i, setoid (α i)]
  (f : ∀ i, α i) : quotient.fin_choice (λ i, ⟦f i⟧) = ⟦f⟧ :=
begin
  let q, swap, change quotient.lift_on q _ _ = _,
  have : q = ⟦λ i h, f i⟧,
  { dsimp [q],
    exact quotient.induction_on
      (@finset.univ ι _).1 (λ l, quotient.fin_choice_aux_eq _ _) },
  simp [this], exact setoid.refl _
end
```

#### [Kenny Lau (Jun 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128141861):
:o

#### [Kevin Buzzard (Jun 16 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer homomorphism/near/128164386):
Canceling s -- [[]] is being used for both the map G->Gab and H->Hab so they don't cancel. Spending the weekend in a field without much internet so don't expect too much from me until sun pm

