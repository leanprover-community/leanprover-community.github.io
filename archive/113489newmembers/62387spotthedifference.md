---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/62387spotthedifference.html
---

## Stream: [new members](index.html)
### Topic: [spot the difference](62387spotthedifference.html)

---


{% raw %}
#### [ Kenny Lau (Jan 11 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913709):
```lean
invalid type ascription, term has type
  @function.injective.{1 1} (pre_von_Neumann n) (pre_von_Neumann m)
    (@nat.le_rec_on.{1} (λ (n : nat), pre_von_Neumann n) (λ (n : nat), @pre_von_Neumann.next n) n m H)
but is expected to have type
  @function.injective.{1 1} (pre_von_Neumann n) (pre_von_Neumann m)
    (@nat.le_rec_on.{1} pre_von_Neumann (λ (n : nat), @pre_von_Neumann.next n) n m H)

state:
n m : nat,
H : @has_le.le.{0} nat nat.has_le n m
⊢ @function.injective.{1 1} (pre_von_Neumann n) (pre_von_Neumann m)
    (@nat.le_rec_on.{1} pre_von_Neumann (λ (n : nat), @pre_von_Neumann.next n) n m H)
```

#### [ Johan Commelin (Jan 11 2019 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913801):
Ouch... that must hurt. `(λ (n : nat), pre_von_Neumann n)` ought to be defeq to `pre_von_Neumann`.

#### [ Kenny Lau (Jan 11 2019 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913885):
ok `convert [...]; ext; refl` worked

#### [ Kenny Lau (Jan 11 2019 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154914109):
@**Sebastian Ullrich** will this be fixed in Lean 4?

#### [ Kenny Lau (Jan 11 2019 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154915053):
MWE:
```lean
def A : ℕ → Type
| nat.zero     := empty
| (nat.succ n) := A n → empty

example : A = λ n, A n := rfl -- fails
```
@**Mario Carneiro**

#### [ Kevin Buzzard (Jan 11 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154923694):
"Probably a bug", says Sebastian


{% endraw %}
