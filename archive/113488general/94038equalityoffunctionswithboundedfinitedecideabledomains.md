---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94038equalityoffunctionswithboundedfinitedecideabledomains.html
---

## Stream: [general](index.html)
### Topic: [equality of functions with bounded finite decideable domains](94038equalityoffunctionswithboundedfinitedecideabledomains.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gavid Liebnich (Nov 20 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148032872):
Is `eq_of_yield` provable? Do I need to lose computability with functional extensionality? 
```lean
import data.vector data.list utils

variables {α : Type}

def between [decidable_linear_order α] (a b : α) :=
  {x : α // a ≤ x ∧ x < b}

class c_mapper (α : Type*) :=
  (n       : α → ℕ)
  (h       : Πm, 0 < n m)
  (data    : Πm, between 0 (n m) → ℕ)

variables [c_mapper α]

def yield (m : α) :=
  (list.range $ c_mapper.n m).attach.map $ λn,
  c_mapper.data m ⟨n, nat.zero_le _, list.mem_range.1 n.2⟩

theorem eq_of_yield {m₁ m₂ : α} (h : yield m₁ = yield m₂) : m₁ = m₂ := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148033325):
```lean
import data.vector data.list data.set.intervals

class c_mapper (α : Type*) :=
(n : α → ℕ)
(h : ∀ m, 0 < n m)
(data : Π m, set.Ico 0 (n m) → ℕ)

def yield {α : Type*} [c_mapper α] (m : α) :=
(list.range $ c_mapper.n m).attach.map $ λ n,
c_mapper.data m ⟨n, nat.zero_le n, list.mem_range.1 n.2⟩

theorem not_yield_inj :
  ¬ ∀ (α : Type) [c_mapper α] {m₁ m₂ : α} (h : by resetI; exact yield m₁ = yield m₂), m₁ = m₂ :=
λ H, absurd (@H bool ⟨λ _, 1, λ _, dec_trivial, λ _ _, 0⟩ ff tt rfl) dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148033328):
@**Gavid Liebnich** it's false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 20 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148033795):
also function extensionality doesn't affect computability because it's a prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 20 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148033820):
unlike some other constructive systems we have a proof irrelevant universe of propositions which are not used in computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gavid Liebnich (Nov 20 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148035327):
Oh, thanks! I think It's starting to make sense now - of course it's not an injection, the `Πm, between 0 (n m) → ℕ` can be whatever mapping I want.

So, if I were to define one such concrete mapping, for example:
```lean
structure mapper := (n : ℕ) (h : 0 < n) (data : vector ℕ n)

instance indexed_mapper_is_c_mapper :
  c_mapper mapper := {
    n       := λm, m.n,
    h       := λm, m.h,
    data    := λm x, m.data.nth ⟨x.1, x.2.2⟩
  }
```
I could then prove (somehow)
```lean
theorem eq_of_yield {m₁ m₂ : mapper} (h : yield m₁ = yield m₂) : m₁ = m₂
```
because the `data` of `c_mapper` would be the function `vector.data.nth`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gavid Liebnich (Nov 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148035891):
So the theorem is true if I give it two extensionally equivalent functions as `data`? For example, if I were to define a mapper that completely mirrors the `class`, that would make the theorem true by virtue of the functions used as `data` in `m1` and `m2` being equivalent? As such:

```lean
structure mapper₂ := (n : ℕ) (h : 0 < n) (data : between 0 n → ℕ)

instance :
  c_mapper mapper₂ := {
    n    := λm, m.n,
    h    := λm, m.h,
    data := λm x, x.1
  }

theorem eq_of_yield {m₁ m₂ : mapper₂} (h : yield m₁ = yield m₂) : m₁ = m₂ := sorry
```
Now the theorem is true?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148036999):
just because it typechecks doesn't mean it's correct... I've corrected your code:
```lean
instance c_mapper_mapper₂ : c_mapper mapper₂ :=
{ n := λ m, m.n,
  h := λ m, m.h,
  data := λ m x, m.data x }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148037009):
it's `m.data x` not `x.1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148037037):
I think we would appreciate it if you check your questions before asking them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148037055):
I've proved both theorems:
```lean
import data.vector data.list data.set.intervals

open set

class c_mapper (α : Type*) :=
(n : α → ℕ)
(h : ∀ m, 0 < n m)
(data : Π m, Ico 0 (n m) → ℕ)

structure mapper :=
(n : ℕ)
(h : 0 < n)
(data : vector ℕ n)

instance c_mapper_mapper : c_mapper mapper :=
{ n := λ m, m.n,
  h := λ m, m.h,
  data := λ m x, m.data.nth ⟨x.1, x.2.2⟩ }

variables {α : Type*} [c_mapper α]

def yield (m : α) : list ℕ :=
(list.range $ c_mapper.n m).attach.map $ λ n,
c_mapper.data m ⟨n, nat.zero_le n, list.mem_range.1 n.2⟩

theorem yield_inj {m₁ m₂ : mapper} (h : yield m₁ = yield m₂) : m₁ = m₂ :=
begin
  have hy1 : (yield m₁).length = m₁.n,
  { rw [yield, list.length_map, list.length_attach, list.length_range]; refl },
  have hy2 : (yield m₂).length = m₂.n,
  { rw [yield, list.length_map, list.length_attach, list.length_range]; refl },
  cases m₁ with n1 h1 d1, cases m₂ with n2 h2 d2,
  have hn : n1 = n2,
  { convert congr_arg list.length h, exacts [hy1.symm, hy2.symm] },
  subst n2, congr' 1, cases d1 with L1 H1, cases d2 with L2 H2, congr' 1,
  dsimp only at hy1 hy2,
  refine list.ext_le (H1.trans H2.symm) (λ i hi1 hi2, _),
  have : ∀ h3, list.nth_le (yield ({n := n1, h := h1, data := ⟨L1, H1⟩} : mapper)) i h3
    = list.nth_le (yield ({n := n1, h := h2, data := ⟨L2, H2⟩} : mapper)) i (hy2.symm ▸ H2 ▸ hi2),
  { rw h, intro, refl },
  specialize this (hy1.symm ▸ H1 ▸ hi1),
  simp only [yield, list.nth_le_map', c_mapper.data, vector.nth] at this,
  unfold coe lift_t has_lift_t.lift coe_t has_coe_t.coe coe_b has_coe.coe at this,
  simpa only [list.nth_le_attach, list.nth_le_range]
end

structure mapper₂ :=
(n : ℕ)
(h : 0 < n)
(data : Ico 0 n → ℕ)

instance c_mapper_mapper₂ : c_mapper mapper₂ :=
{ n := λ m, m.n,
  h := λ m, m.h,
  data := λ m x, m.data x }

theorem yield_inj' {m₁ m₂ : mapper₂} (h : yield m₁ = yield m₂) : m₁ = m₂ :=
begin
  have hy1 : (yield m₁).length = m₁.n,
  { rw [yield, list.length_map, list.length_attach, list.length_range]; refl },
  have hy2 : (yield m₂).length = m₂.n,
  { rw [yield, list.length_map, list.length_attach, list.length_range]; refl },
  cases m₁ with n1 h1 d1, cases m₂ with n2 h2 d2,
  have hn : n1 = n2,
  { convert congr_arg list.length h, exacts [hy1.symm, hy2.symm] },
  subst n2, congr' 1, ext i, rcases i with ⟨i, hi1, hi2⟩,
  dsimp only at hy1 hy2,
  have : ∀ h3, list.nth_le (yield ({n := n1, h := h1, data := d1} : mapper₂)) i h3
    = list.nth_le (yield ({n := n1, h := h2, data := d2} : mapper₂)) i (hy2.symm ▸ hi2),
  { rw h, intro, refl },
  specialize this (hy1.symm ▸ hi2),
  simp only [yield, list.nth_le_map', c_mapper.data, vector.nth] at this,
  unfold coe lift_t has_lift_t.lift coe_t has_coe_t.coe coe_b has_coe.coe at this,
  simpa only [list.nth_le_attach, list.nth_le_range]
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148037125):
@**Gavid Liebnich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gavid Liebnich (Nov 20 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20functions%20with%20bounded%20finite%20decideable%20domains/near/148037550):
Thank you, @**Kenny Lau** . I appreciate your help. The transition from nondependent `range` to the bounded mapping is a step I'm having difficulties with. There's a bit of magic in `convert` it would appear, I'll have to take a closer look. Thanks again, I'm going to step over the proofs.

