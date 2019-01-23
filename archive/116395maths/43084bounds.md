---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43084bounds.html
---

## Stream: [maths](index.html)
### Topic: [bounds](43084bounds.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 17 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874320):
This is more of a funny story than anything else.

This week just gone at Imperial, we were looking at the real numbers and the completeness axiom in my class. Some of the students were involved in a (maths not Lean) project of constructing the real numbers as Dedekind cuts. The sheet started by defining totally ordered sets (the `linear_order` class in Lean) and the "least upper bound property" -- any non-empty bounded-above subset has a least upper bound. The sheet then remarked something I'd never realised -- there is no point defining also the "greatest lower bound property", because this follows from the least upper bound property. For the reals I had always imagined that this was proved by just considering $$\{-x\,\mid\,x\in S\}$$ but actually there is a direct proof which only uses total orders. 

```lean
-- from order/bounds.lean

variables {α : Type*} [preorder α]
def upper_bounds (s : set α) : set α := { x | ∀a ∈ s, a ≤ x }
def lower_bounds (s : set α) : set α := { x | ∀a ∈ s, x ≤ a }
def is_least (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ lower_bounds s
def is_greatest (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ upper_bounds s
def is_lub (s : set α) : α → Prop := is_least (upper_bounds s)
def is_glb (s : set α) : α → Prop := is_greatest (lower_bounds s)

theorem warm_up (S : Type) [linear_order S] :
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ upper_bounds E) → ∃ s : S, is_lub E s) →
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ lower_bounds E) → ∃ s : S, is_glb E s) := sorry
```

Of course the proof requires a mathematical idea -- knowing any non-empty bounded-above set has a sup, and given a non-empty bounded-below set, we need to produce an inf without this involution which we have on the reals.

#### [ Kevin Buzzard (Nov 17 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874402):
So I could see what the idea must be, and knocked up a tactic proof without too much trouble.

And then because the bounds definitions applied not just to `linear_order` but to `preorder`, Chris asked whether my proof also worked for partial orders or preorders. So the question became -- what do you actually need to assume about your order to prove this warm-up question? I'll post our conclusions later on today if nobody else fancies trying to figure this out :-)

#### [ Kevin Buzzard (Nov 17 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874403):
No spoilers Kenny/Chris, if you're reading :-)

#### [ Johannes Hölzl (Nov 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147875349):
This is a standard construction at least for complete lattices, there often one defines the supremum or infimum and derives the other exterma. And these structures where the extrema only exists for non-empty bounded sets are called "conditionally complete lattices"

#### [ Kevin Buzzard (Nov 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878523):
Right. So the question is: you might well know already that if, in a lattice, all non-empty bounded-above sets have a sup, then all non-empty bounded-below sets have an inf. This is a pleasant exercise. The question is whether you can get away with less than a lattice.

#### [ Mario Carneiro (Nov 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878636):
if every set has a least upper bound, then it's already a lattice

#### [ Kevin Buzzard (Nov 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878638):
I am only demanding on my order that every non-empty bounded above set has a least upper bound.

#### [ Mario Carneiro (Nov 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878687):
then you get a conditionally complete lattice

#### [ Kevin Buzzard (Nov 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878690):
but I need enough from my order to be able to deduce from this that every non-empty bounded-below set has a greatest lower bound.

#### [ Mario Carneiro (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878699):
You might have to be careful about how you say bounded below, but the usual proof should go through

#### [ Kevin Buzzard (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878709):
I explain exactly what I mean by all of these terms in the original post

#### [ Kevin Buzzard (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878711):
The question is how much you can relax the typeclasses and still be able to fill in the sorry

#### [ Kevin Buzzard (Nov 17 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878753):
e.g. can you prove

```lean
variables {α : Type*} [preorder α]
def upper_bounds (s : set α) : set α := { x | ∀a ∈ s, a ≤ x }
def lower_bounds (s : set α) : set α := { x | ∀a ∈ s, x ≤ a }
def is_least (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ lower_bounds s
def is_greatest (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ upper_bounds s
def is_lub (s : set α) : α → Prop := is_least (upper_bounds s)
def is_glb (s : set α) : α → Prop := is_greatest (lower_bounds s)

theorem warm_up (S : Type) [preorder S] :
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ upper_bounds E) → ∃ s : S, is_lub E s) →
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ lower_bounds E) → ∃ s : S, is_glb E s) := sorry

#### [ Mario Carneiro (Nov 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878808):
I think so

#### [ Kevin Buzzard (Nov 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878810):
so now begin dropping the axioms of a preorder

#### [ Kevin Buzzard (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878818):
and how far can you get?

#### [ Mario Carneiro (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878822):
if you take `E := lower_bounds E` then it's nonempty, and an element of `E` is an upper bound for `lower_bounds E`

#### [ Kevin Buzzard (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878825):
right. And which axioms for a preorder do you use in this proof?

#### [ Mario Carneiro (Nov 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878866):
if `a in E` and `b in lower_bounds E` then `b <= a` so `a` is an upper bound of `lower_bounds E`

#### [ Mario Carneiro (Nov 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878867):
it uses nothing

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878872):
```lean
variables {α : Type*} [has_le α]
def upper_bounds (s : set α) : set α := { x | ∀a ∈ s, a ≤ x }
def lower_bounds (s : set α) : set α := { x | ∀a ∈ s, x ≤ a }
def is_least (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ lower_bounds s
def is_greatest (s : set α) (a : α) : Prop := a ∈ s ∧ a ∈ upper_bounds s
def is_lub (s : set α) : α → Prop := is_least (upper_bounds s)
def is_glb (s : set α) : α → Prop := is_greatest (lower_bounds s)

theorem warm_up (S : Type) [has_le S] :
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ upper_bounds E) → ∃ s : S, is_lub E s) →
(∀ E : set S, (∃ a, a ∈ E) ∧ (∃ b, b ∈ lower_bounds E) → ∃ s : S, is_glb E s) :=
λ H E ⟨⟨a, haE⟩, ⟨b, hbuE⟩⟩,
let ⟨s, hs1, hs2⟩ := H (lower_bounds E) ⟨⟨b, hbuE⟩, ⟨a, λ s hs, hs a haE⟩⟩ in
⟨s, λ t htE, hs2 t (λ z hzLE, hzLE t htE), hs1⟩
```

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878874):
punchline achieved

#### [ Mario Carneiro (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878877):
it could be any relation

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878878):
This made me wonder why preorder was assumed in bounds.lean

#### [ Mario Carneiro (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878922):
because preorder is our weakest "lawful" order class

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878923):
surely has_le is weaker?

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878925):
It's surely an order class

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878926):
because of the notation

#### [ Kevin Buzzard (Nov 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878938):
you yourself know that has_add and has_mul are two completely different classes

#### [ Kevin Buzzard (Nov 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878939):
that's why you had to define groups twice

#### [ Mario Carneiro (Nov 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878994):
if it's not a preorder, you probably shouldn't be using `<=`

#### [ Mario Carneiro (Nov 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879007):
plus all the terminology there doesn't really make sense without some transitivity

#### [ Kevin Buzzard (Nov 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879514):
I am surprised that this is your attitude. I think the notation implies a "way of thinking" about the structure, but why can't I define the "upper bounds" of a set with has_le to be the obvious things? I thought that this was the mathlib philosophy -- you define things in the max generality that they parse, and for these definitions like upper_bounds we need nothing more than the predicate.

#### [ Kevin Buzzard (Nov 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879519):
Octonians aren't associative, and yet people still use `*` to multiply them

#### [ Mario Carneiro (Nov 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879616):
octonions aren't completely lawless though

#### [ Mario Carneiro (Nov 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879619):
If we cared about them we would define loops or power-associative monoids or whatever

#### [ Mario Carneiro (Nov 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879676):
I think it helps to be at least a little application-driven here. If it's only ever used on preorders then why the suprious generalization?

#### [ Mario Carneiro (Nov 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879678):
note also that typeclass inference is a bit longer for lower classes, although this is probably a small effect

#### [ Mario Carneiro (Nov 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879731):
I would recommend using pure notation classes only in lawless situations like `meta` programming

#### [ Kevin Buzzard (Nov 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147880123):
Oh that's an interesting comment. So there is a place for the has_lt typeclass beyond just a notational trick?

#### [ Kevin Buzzard (Nov 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147880125):
It's just in lawless metaland :-)


{% endraw %}
