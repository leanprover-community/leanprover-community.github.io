---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86899constructingaclassforih.html
---

## [general](index.html)
### [constructing a class for ih](86899constructingaclassforih.html)

#### [Gavid Liebnich (Nov 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147882679):
Could anyone point me in a right direction in this proof?
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

lemma yield_len (m : α) : list.length (yield m) = c_mapper.n m :=
begin
  generalize h : yield m = l,
  induction l with x xs ih generalizing m,
    {
      -- yield m = [] is contradictory
      admit
    },
    {
      -- How to construct α for ih?
    }
end
```
I don't suppose there is at all a way to construct a new `α` here for the `ih` in `yield_len`  - it's a `class`. Do I need to reformulate the entire statement? Or do I need to do induction over something different there?

#### [Kenny Lau (Nov 17 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147883055):
```lean
import data.vector data.list

universe u

variables {α : Type u}

def between [decidable_linear_order α] (a b : α) :=
{x : α // a ≤ x ∧ x < b}

class c_mapper (α : Type u) :=
(n : α → ℕ)
(h : Π m, 0 < n m)
(data : Π m, between 0 (n m) → ℕ)

structure mapper :=
(n : ℕ)
(h : 0 < n)
(data : vector ℕ n)

instance indexed_mapper_is_c_mapper : c_mapper mapper :=
{ n    := λ m, m.n,
  h    := λ m, m.h,
  data := λ m x, m.data.nth ⟨x.1, x.2.2⟩ }

variables [c_mapper α]

def yield (m : α) :=
(list.range $ c_mapper.n m).attach.map $ λ n,
c_mapper.data m ⟨n, nat.zero_le _, list.mem_range.1 n.2⟩

lemma yield_len (m : α) : list.length (yield m) = c_mapper.n m :=
(list.length_map _ _).trans $ (list.length_attach _).trans $ list.length_range _
```

#### [Gavid Liebnich (Nov 17 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884558):
Alright this works in this particular case, however, what if I actually need to do induction on something that will require a value of some class type - such as occurs in this case if I do happen to do induction and I get to a state with ih `∀ (m : α), yield m = xs → list.length xs = c_mapper.n m`. Providing this `m` doesn't seem possible to me, because it's just some `α` that's known to be `[c_mapper α]`.

#### [Kenny Lau (Nov 17 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884574):
I don't think induction on `yield m` is a good idea in this case anyway

#### [Gavid Liebnich (Nov 17 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884616):
What would one do induction on then?

