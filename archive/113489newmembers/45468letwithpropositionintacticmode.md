---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/45468letwithpropositionintacticmode.html
---

## Stream: [new members](index.html)
### Topic: [let with proposition in tactic mode](45468letwithpropositionintacticmode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616438):
```lean
import tactic.interactive

open function

meta def tactic.interactive.result : tactic unit :=
do e ← tactic.result, tactic.trace e

theorem cantor_surjective
  (X : Type) (f : X → set X) (Hf : surjective f) : false :=
begin
  let H := Hf {x | x ∉ f x},
  cases H with D e,
  result
  -- ⊢ (let H : ∃ (a : X), f a = {x : X | x ∉ f x} := Hf {x : X | x ∉ f x} in false) (Exists.intro D e)
end

/-
let H : ∃ (a : X), f a = {x : X | x ∉ f x} := _,
    H_1 : ∃ (a : X), f a = {x : X | x ∉ f x} := _
in Exists.dcases_on H_1 (λ (D : X) (e : f D = {x : X | x ∉ f x}), ?m_1[H, H_1, D, e])
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616481):
somehow there's a strange goal if we use `let` instead of `have` with a proposition in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616542):
compare this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616547):
```lean
import tactic.interactive

open function

meta def tactic.interactive.result : tactic unit :=
do e ← tactic.result, tactic.trace e

theorem cantor_surjective
  (X : Type) (f : X → set X) (Hf : surjective f) : false :=
begin
  have H := Hf {x | x ∉ f x},
  cases H with D e,
  result
  -- ⊢ false
end

/-
Exists.dcases_on (Hf {x : X | x ∉ f x})
  (λ (D : X) (e : f D = {x : X | x ∉ f x}), ?m_1[Hf {x : X | x ∉ f x}, Hf {x : X | x ∉ f x}, D, e])
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 13 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151618247):
Moral: don't use `let` with propositions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 13 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151618280):
Background: Kenny just watched me giving a live Lean talk and I used `let` with a proposition :P

