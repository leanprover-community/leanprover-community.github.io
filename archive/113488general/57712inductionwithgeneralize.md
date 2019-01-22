---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57712inductionwithgeneralize.html
---

## [general](index.html)
### [induction with generalize](57712inductionwithgeneralize.html)

#### [Sarah Mameche (Nov 16 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147851332):
Hi, I want to do induction over the following predicate `types`:

```lean
inductive types : Π {m}, (fin m → type) → tm m → type → Prop (...)
```

The predicate expresses `Γ  ⊢ x : A`, where the typing context `Γ` is a function `(fin m→ type) `, and expression `x` has type `tm m` (but I think the details are not important). My induction is over the empty context:
```lean
definition empty_ctx : fin 0 → type :=  λ (x : Fin 0), match x with end
```
Here's the lemma: 
```lean
lemma preservation (A : type) (e₁ : tm 0) : 
  types empty_ctx e₁ A → 
      forall e₂, e₁ › e₂ → types empty_ctx e₂ A :=
begin intros H₁ e H₂, 
  induction H₁ (...)
```
This gives the following error:
```lean 
[check] application type mismatch at
  types ∅
argument type
  Fin 0 → type
expected type
  Fin _x → type`induction with generalize
```
In Coq, the induction works. I assume Lean is more strict about generalizing numbers before doing an induction?  I'm not sure about how to generalize in this case, as 0 appears in the type of the empty context. So the standard way of adding an assumption `h : X = empty_ctx` and substituting X doesn't work because X again has type `fin 0 → type`. Could you give me some details or tell me if I'm on the wrong track?

#### [Kenny Lau (Nov 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147851364):
what is `Fin`?

#### [Kenny Lau (Nov 16 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147851438):
could you provide an MWE?

#### [Sarah Mameche (Nov 16 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147851814):
```lean 
def Fin : nat → Type
  | 0 := empty
  | (n+1) := option (Fin n)
```
```lean
inductive tm  : nat -> Type 
  | var_tm : Π {ntm : nat}, Fin ntm -> tm ntm
  | app : Π {ntm : nat}, tm ntm -> tm ntm -> tm ntm
  | lam : Π {ntm : nat}, tm (nat.succ ntm) -> tm ntm
open tm
```
```lean
inductive type : Type
| tint : type
| tarrow : type → type → type
open type
```
```lean
inductive types : Π {m}, (Fin m → type) → tm m → type → Prop
| tvar {m} Γ (x : Fin m) : types Γ (var_tm x) (Γ x)
| tapp {m} Γ (e₁ : tm m) e₂ (A B) : types Γ e₁ (tarrow A B) → types Γ e₂ A → types Γ (app e₁ e₂) B
--| tlam {m} Γ (e : tm (nat.succ m)) (A B) : types (@scons _ m  A Γ) e B → types Γ (lam e) (tarrow A B) requires some more definitions
```
```lean
definition empty_ctx : Fin 0 → type :=  λ (x : Fin 0), match x with end
```
```lean
def step {n} (t t' : tm n) := tt. --(..)
```
```lean
lemma preservation (A : type) (e₁ : tm 0) : 
  types empty_ctx e₁ A → 
      forall e₂, step e₁  e₂ → types empty_ctx e₂ A :=
begin intros H₁ e H₂, 
  induction H₁ 
```

#### [Reid Barton (Nov 17 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147852574):
I'm not sure how to do it with induction, but I would probably try using the equation compiler

#### [Chris Hughes (Nov 17 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147852628):
Changing the definition of `types` to this works.
```lean
inductive types {m : ℕ} : (Fin m → type) → tm m → type → Prop
| tvar Γ (x : Fin m) : types Γ (var_tm x) (Γ x)
| tapp Γ (e₁ : tm m) e₂ (A B) : types Γ e₁ (A ⤏ B) → types Γ e₂ A → types Γ (app e₁ e₂) B
```

#### [Reid Barton (Nov 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147852765):
but that won't work for `tlam`, which increases the size of the context

#### [Chris Hughes (Nov 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147852773):
I see.

#### [Chris Hughes (Nov 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147853368):
`destruct H\1` also works.

#### [Chris Hughes (Nov 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147853439):
Although I don't think that gives the goal you want. It didn't choose a very good motive.

#### [Chris Hughes (Nov 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147853454):
This is a nasty method that hopefully does get the right goal at least
```lean
lemma preservation (A : type) {n} (ctx : Fin n → type) (e₁ : tm 0) :
  types empty_ctx e₁ A →
      forall e₂, step e₁ e₂ → types empty_ctx e₂ A :=
λ H₁, @types.rec_on
  (λ m ctx e₁ t, m = 0 → ctx == empty_ctx → ∀ e₂ : tm m, step e₁ e₂ → types ctx e₂ A) 0 empty_ctx e₁ A H₁
    begin
      intros m Γ _ hm hΓ,
      subst hm,
      have := eq_of_heq hΓ,
      subst this,

    end sorry rfl (heq.refl _)
```

#### [Mario Carneiro (Nov 17 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147860085):
here are a few more options:
```lean
lemma preservation (A : type) (e₁ : tm 0)
  (H₁ : types empty_ctx e₁ A) (e₂) (H₂ : step e₁ e₂) : types empty_ctx e₂ A :=
begin
  revert e₁ e₂,
  generalize : empty_ctx = ctx,
  revert ctx,
  generalize h : 0 = n,
  intros,
  induction H₁ generalizing h; subst h,
  { cases H₁_x },
  { sorry }
end

lemma preservation' (A : type) : ∀ (e₁ : tm 0),
  types empty_ctx e₁ A → ∀ e₂, step e₁ e₂ → types empty_ctx e₂ A :=
suffices ∀ {n}, n = 0 → ∀ {ctx} (e₁ : tm n), types ctx e₁ A → ∀ e₂, step e₁ e₂ → types ctx e₂ A,
from this rfl,
begin
  introv h H₁ H₂,
  induction H₁ generalizing h; subst h,
  { cases H₁_x },
  { sorry }
end
```

#### [Mario Carneiro (Nov 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147860093):
in this case it doesn't matter that you have `empty_ctx` since it's unique anyway

#### [Sarah Mameche (Nov 17 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction with generalize/near/147868864):
Great, thanks!

