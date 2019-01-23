---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48331isthischoicecomputable.html
---

## Stream: [general](index.html)
### Topic: [is this choice computable?](48331isthischoicecomputable.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133307935):
Can the two `sorry`s be filled in?
```lean
variables (ι : Type*) (β : ι → Type*) [Π i, has_zero (β i)]

def pointed_sigma.aux : Type* :=
option Σ i, β i

inductive pointed_sigma.r : pointed_sigma.aux ι β → pointed_sigma.aux ι β → Prop
| refl : Π x, pointed_sigma.r x x
| zero_left : Π i, pointed_sigma.r none (some ⟨i, 0⟩)
| zero_right : Π i, pointed_sigma.r (some ⟨i, 0⟩) none
| zero : Π i j, pointed_sigma.r (some ⟨i, 0⟩) (some ⟨j, 0⟩)

instance pointed_sigma.setoid : setoid (pointed_sigma.aux ι β) :=
{ r := pointed_sigma.r ι β,
  iseqv := begin
    refine ⟨λ x, _, λ x y h, _, λ x y z h1 h2, _⟩,
    { constructor },
    { cases h; constructor },
    { cases h1; cases h2; constructor }
  end }

def pointed_sigma : Type* :=
quotient (pointed_sigma.setoid ι β)

namespace pointed_sigma

instance : has_zero (pointed_sigma ι β) :=
⟨⟦none⟧⟩

def of (i : ι) (x : β i) : pointed_sigma ι β :=
⟦some ⟨i, x⟩⟧

def choice : Π (i j : ι) (x : β i) (H : ∃ y, of ι β i x = of ι β j y), β j := sorry
theorem choice_eq (i j : ι) (x : β i) (H) : of ι β i x = of ι β j (choice ι β i j x H) := sorry

end pointed_sigma
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133307990):
So I have a bunch of pointed types, indexed by the type `ι`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308002):
I'm building the pointed union of these pointed types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308007):
(The point is represented by zero.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308016):
So for each `i : ι`, I have a function from the pointed set indexed by `i` to the union.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308037):
I'm wondering if I can reverse this operation, i.e. given an element of the pointed union, with a proof that it is from some element of the pointed set indexed by `i`, I would like to give back this element of the pointed set.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 04 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133312135):
I suspect you need decidable equality on I

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133312361):
that's also what I suspect, but I can't prove


{% endraw %}
