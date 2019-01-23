---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26111interfacefordite.html
---

## Stream: [general](index.html)
### Topic: [interface for dite](26111interfacefordite.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125812949):
```lean
noncomputable def succ (C : set (set α)) : set (set α) :=
if H : ∃ A, A ∈ (hat S C) \ C then insert (classical.some H) C else C

@[elab_as_eliminator] noncomputable def succ.rec {C : set (set α) → set (set α) → Sort*}
  (H1 : ∀ t, ∀ A ∈ (hat S t) \ t, C t (insert (classical.some (⟨A, H⟩ : ∃ A, A ∈ (hat S t) \ t)) t))
  (H2 : ∀ t, (∀ A ∈ (hat S t) \ t, false) → C t t)
  (t : set (set α)) : C t (succ S t) :=
if H : ∃ A, A ∈ (hat S t) \ t then
  have succ S t = insert (classical.some H) t, from dif_pos H,
  eq.drec_on this.symm $ H1 _ (classical.some H) (classical.some_spec H)
else
  have succ S t = t, from dif_neg H,
  eq.drec_on this.symm $ H2 t $ λ A h, H ⟨A, h⟩

@[elab_as_eliminator] noncomputable def succ.rec_on {C : set (set α) → set (set α) → Sort*}
  (t : set (set α))
  (H1 : ∀ t, ∀ A ∈ (hat S t) \ t, C t (insert (classical.some (⟨A, H⟩ : ∃ A, A ∈ (hat S t) \ t)) t))
  (H2 : ∀ t, (∀ A ∈ (hat S t) \ t, false) → C t t) :
  C t (succ S t) :=
succ.rec S H1 H2 t

theorem succ.subset (C : set (set α)) : C ⊆ succ S C :=
succ.rec_on S C
  (λ t A H, show t ⊆ insert (classical.some _) t, from λ z, or.inr)
  (λ t H z, id)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125813006):
```lean
noncomputable def succ (C : set (set α)) : set (set α) :=
if H : ∃ A, A ∈ (hat S C) \ C then insert (classical.some H) C else C

@[elab_as_eliminator] noncomputable def succ.rec {C : set (set α) → set (set α) → Sort*}
  (H1 : ∀ t, ∀ A ∈ (hat S t) \ t, C t (insert A t))
  (H2 : ∀ t, (∀ A ∈ (hat S t) \ t, false) → C t t)
  (t : set (set α)) : C t (succ S t) :=
if H : ∃ A, A ∈ (hat S t) \ t then
  have succ S t = insert (classical.some H) t, from dif_pos H,
  eq.drec_on this.symm $ H1 _ (classical.some H) (classical.some_spec H)
else
  have succ S t = t, from dif_neg H,
  eq.drec_on this.symm $ H2 t $ λ A h, H ⟨A, h⟩

@[elab_as_eliminator] noncomputable def succ.rec_on {C : set (set α) → set (set α) → Sort*}
  (t : set (set α))
  (H1 : ∀ t, ∀ A ∈ (hat S t) \ t, C t (insert A t))
  (H2 : ∀ t, (∀ A ∈ (hat S t) \ t, false) → C t t) :
  C t (succ S t) :=
succ.rec S H1 H2 t

theorem succ.subset (C : set (set α)) : C ⊆ succ S C :=
succ.rec_on S C
  (λ t A H, show t ⊆ insert A t, from λ z, or.inr)
  (λ t H z, id)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125813007):
which one is better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125813201):
why does elaborator fail for this one?
```lean
type mismatch, term
  succ.rec_on S C ?m_2 ?m_3
has type
  ?m_1 C (succ S C) : Sort ?
but is expected to have type
  is_chain C → is_chain (succ S C) : Prop
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821121):
`dite` stinks and I would strongly encourage you to work on this until it stinks less.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821160):
`dite` is such a normal thing coming from procedural languages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821164):
and it's so hard to eliminate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821165):
I did write an interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821166):
I know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/interface%20for%20dite/near/125821167):
but the elaborator fails lol

