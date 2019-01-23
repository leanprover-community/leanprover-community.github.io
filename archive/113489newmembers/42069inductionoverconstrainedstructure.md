---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/42069inductionoverconstrainedstructure.html
---

## Stream: [new members](index.html)
### Topic: [induction over constrained structure](42069inductionoverconstrainedstructure.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gavid Liebnich (Nov 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147588184):
I am slightly stuck on a proof, could anyone point me in the right direction? The tl;dr is that I have a structure `X` holding `n` and a proof that `h : 0 < n`. However, `h` makes it impossible to do induction on `n`, because my inductive hypotheses requires me to construct a new `X` such that `h` holds, which is untrue for an arbitrary `n`.

Here's a hopefully small example:
```lean
import data.vector data.list

variables {α : Type} 

def between [decidable_linear_order α] (a b : α) :=
  {x : α // a ≤ x ∧ x < b}

class c_mapper (α : Type*) :=
  (n       : α → ℕ)
  (h       : Πm, 0 < n m)
  (data    : Πm, between 0 (n m) → ℕ)

structure mapper := (n : ℕ) (h : 0 < n) (data : vector ℕ n)

instance indexed_mapper_is_c_mapper :
  c_mapper mapper := {
    n       := λm, m.n,
    h       := λm, m.h,
    data    := λm x, m.data.nth ⟨x.1, x.2.2⟩
  }

variables [c_mapper α]

def yield (m : α) :=
  list.map (
      c_mapper.data m ∘ λn : {x // x ∈ list.range (c_mapper.n m)}, ⟨n, sorry⟩
    )
    (list.attach $ list.range $ c_mapper.n m)

lemma yield_eq_data {m : mapper} : yield m = m.data.to_list :=
begin
  cases m with n h data,
  induction n with n ih generalizing data,
    { cases h },
    {
      -- ih : ∀ (h : 0 < n)..., which I will never show
    }
end
```

The resulting state has the inductive hypothesis: `∀ (h : 0 < n) (data : vector ℕ n), yield {n := n, h := h, data := data} = vector.to_list ({n := n, h := h, data := data}.data)`, which is not usable, because I can't show `h`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589062):
You can case on whether `0 < n` or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589079):
if not, then `n = 0`, and this is your "actual" base case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Nov 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589595):
(deleted)

