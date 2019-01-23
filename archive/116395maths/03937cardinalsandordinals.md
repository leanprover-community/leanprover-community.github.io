---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/03937cardinalsandordinals.html
---

## Stream: [maths](index.html)
### Topic: [cardinals and ordinals](03937cardinalsandordinals.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132580778):
In lean they are not sets? i.e. `set_theory/zfc.lean` and `set_theory/cardinal.lean` are independent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132583263):
so I've written my embedding:
```lean
import set_theory.zfc set_theory.ordinal

universe u

noncomputable def ordinal.to_Set (o : ordinal.{u}) : Set.{u+1} :=
quotient.mk $ ordinal.limit_rec_on o ∅ (λ _ s, insert s s) $ λ L _ ih,
pSet.Union $ pSet.mk { o // o < L } $ λ o', ih o'.1 o'.2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132583279):
and I wonder if I can do it in `pSet.{u}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132599529):
```lean
import set_theory.zfc set_theory.ordinal

universe u

attribute [elab_as_eliminator] well_founded.induction

def Well_order.to_pSet (w : Well_order.{u}) : pSet.{u} :=
pSet.mk w.1 $ well_founded.fix (@is_well_order.wf w.1 w.2 w.3) $ λ x ih,
pSet.mk { y | w.r y x } $ λ p, ih p.1 p.2

theorem ordinal.to_Set.aux (v w : Well_order.{u}) (e : v.2 ≃o w.2) (x : v.1) :
  (Well_order.to_pSet v).func x ≈ (Well_order.to_pSet w).func (e x) :=
show pSet.equiv
  (well_founded.fix (@is_well_order.wf v.1 v.2 v.3)
    (λ x ih, pSet.mk { y | v.r y x } $ λ p, ih p.1 p.2) x)
  (well_founded.fix (@is_well_order.wf w.1 w.2 w.3)
    (λ x ih, pSet.mk { y | w.r y x } $ λ p, ih p.1 p.2) (e x)),
from well_founded.induction (@is_well_order.wf v.1 v.2 v.3) x $ λ x ih,
by rw [well_founded.fix_eq, well_founded.fix_eq];
from ⟨λ ⟨y, hy⟩, ⟨⟨e y, (order_iso.ord e).1 hy⟩, ih y hy⟩,
λ ⟨y, hy⟩, ⟨⟨e.symm y, by simpa using (order_iso.ord e.symm).1 hy⟩,
  by have := ih (e.symm y) (by simpa using (order_iso.ord e.symm).1 hy); rw [order_iso.apply_inverse_apply] at this; from this⟩⟩

def ordinal.to_Set (o : ordinal.{u}) : Set.{u} :=
quotient.lift_on o (λ w, ⟦Well_order.to_pSet w⟧) $ λ ⟨v1, v2, v3⟩ ⟨w1, w2, w3⟩ ⟨e⟩, quotient.sound
⟨λ x, ⟨e x, ordinal.to_Set.aux _ _ e x⟩,
λ x, ⟨e.symm x, by simpa using ordinal.to_Set.aux ⟨v1, v2, v3⟩ ⟨w1, w2, w3⟩ e (e.symm x)⟩⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132599537):
and I did it in the same universe @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132599597):
and I still don't think it's a good idea to destruct the `Well_order` in the definition of the setoid of ordinal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132601476):
and after 38 minutes, the other direction:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132601478):
```lean
def pSet.type.setoid (p : pSet.{u}) : setoid p.type :=
⟨λ i j, ⟦p.func i⟧ = ⟦p.func j⟧, λ i, rfl, λ i j, eq.symm, λ i j k, eq.trans⟩

local attribute [instance] pSet.type.setoid

def Set.cardinal (s : Set.{u}) : cardinal.{u} :=
quotient.lift_on s (λ p, cardinal.mk $ quotient $ pSet.type.setoid p) $
λ ⟨p1, p2⟩ ⟨q1, q2⟩ H, quotient.sound $ nonempty.intro
{ to_fun := λ x, quotient.lift_on x (λ i, @@quotient.mk (pSet.type.setoid $ pSet.mk q1 q2) (classical.some (H.1 i))) $ λ i j H',
    quotient.sound $
    calc  ⟦q2 (classical.some (H.1 i))⟧
        = ⟦p2 i⟧ : eq.symm (quotient.sound $ classical.some_spec (H.1 i))
    ... = ⟦p2 j⟧ : H'
    ... = ⟦q2 (classical.some (H.1 j))⟧ : quotient.sound (classical.some_spec (H.1 j)),
  inv_fun := λ x, quotient.lift_on x (λ i, @@quotient.mk (pSet.type.setoid $ pSet.mk p1 p2) $ classical.some $ H.2 i) $ λ i j H',
    quotient.sound $
    calc  ⟦p2 (classical.some (H.2 i))⟧
        = ⟦q2 i⟧ : quotient.sound (classical.some_spec (H.2 i))
    ... = ⟦q2 j⟧ : H'
    ... = ⟦p2 (classical.some (H.2 j))⟧ : eq.symm (quotient.sound $ classical.some_spec (H.2 j)),
  left_inv := λ i, quotient.induction_on i $ λ i, quotient.sound $
    calc  ⟦p2 (classical.some (H.2 (classical.some (H.1 i))))⟧
        = ⟦q2 (classical.some (H.1 i))⟧ : quotient.sound (classical.some_spec (H.2 _))
    ... = ⟦p2 i⟧ : eq.symm (quotient.sound $ classical.some_spec (H.1 i)),
  right_inv := λ i, quotient.induction_on i $ λ i, quotient.sound $
    calc  ⟦q2 (classical.some (H.1 (classical.some (H.2 i))))⟧
        = ⟦p2 (classical.some (H.2 i))⟧ : eq.symm (quotient.sound $ classical.some_spec (H.1 _))
    ... = ⟦q2 i⟧ : quotient.sound (classical.some_spec (H.2 i)) }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 22 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132602524):
@**Mario Carneiro** should I develop on this and then PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132605696):
```lean
theorem Well_order.to_pSet.exact (w : Well_order.{u}) (x : w.1) :
  ∀ y, ⟦w.to_pSet.func x⟧ = ⟦w.to_pSet.func y⟧ → x = y :=
well_founded.induction (@is_well_order.wf w.1 w.2 w.3) x $ λ x ih y H,
begin
  replace H := quotient.exact H,
  rw [Well_order.to_pSet.def, Well_order.to_pSet.def] at H,
  letI := w.3,
  rcases is_trichotomous.trichotomous w.2 x y with h | h | h,
  { rcases H.2 ⟨x, h⟩ with ⟨⟨z, hzx⟩, h1⟩,
    specialize ih z hzx x (quotient.sound h1),
    exfalso,
    subst ih,
    exact is_irrefl.irrefl w.r _ hzx },
  { exact h },
  { rcases H.1 ⟨y, h⟩ with ⟨⟨z, hzy⟩, h1⟩,
    specialize ih y h z (quotient.sound h1),
    exfalso,
    subst ih,
    exact is_irrefl.irrefl w.r _ hzy }
end

example (c : cardinal.{u}) : c.ord.to_Set.to_cardinal = c :=
begin
  apply quotient.induction_on c,
  intro c,
  have := cardinal.ord_eq c,
  rcases this with ⟨r, wo, H⟩,
  simp [H, ordinal.type, ordinal.to_Set],
  rw [Set.mk, Set.to_cardinal, quotient.lift_on_beta],
  apply quotient.sound,
  split,
  fapply equiv.mk,
  { fapply quotient.lift,
    { exact id },
    { intros x y H,
      exact Well_order.to_pSet.exact _ _ _ H } },
  { exact quotient.mk },
  { intro x,
    apply quotient.induction_on x,
    intro x,
    refl },
  { intro x, refl }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 23 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinals%20and%20ordinals/near/132605703):
that's the round trip in one direction

