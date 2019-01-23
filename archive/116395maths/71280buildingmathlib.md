---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71280buildingmathlib.html
---

## Stream: [maths](index.html)
### Topic: [building mathlib](71280buildingmathlib.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125292006):
I'm trying to build the mathlib master with the Lean master. Should this work? I currently get this as the first error (followed by others):

```lean
mathlib/data/finset.lean:846:12: error: rewrite tactic failed, did not find instance of the pattern in the target expression
  ?m_2 ∈ multiset.to_finset ?m_4
state:
α : Type u_1,
δ : α → Type u_4,
_inst_1 : decidable_eq α,
_inst_2 : Π (a : α), decidable_eq (δ a),
t : Π (a : α), finset (δ a),
s_val : multiset α,
s_nodup : multiset.nodup s_val,
f : Π (a : α), a ∈ {val := s_val, nodup := s_nodup} → δ a
⊢ f ∈ multiset.to_finset (multiset.pi ({val := s_val, nodup := s_nodup}.val) (λ (a : α), (t a).val)) ↔
    ∀ (a : α) (h : a ∈ {val := s_val, nodup := s_nodup}), f a h ∈ t a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125292113):
mathlib is currently building against nightly 04-06. I've been waiting for the 3.4.0 nightly to be released, which happened yesterday; I'll take a look at updating later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 25 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125662029):
Yay! I can build lean and mathlib. :person_doing_cartwheel: Thanks, @**Mario Carneiro**!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 26 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125714983):
Wow! I just upgraded my Lean and mathlib from February to the latest, and I didn't have to change a thing in my code. :astonished:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125715047):
that must be a record, two months without a backward incompatibility

