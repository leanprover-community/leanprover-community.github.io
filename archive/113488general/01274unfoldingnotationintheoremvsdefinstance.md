---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01274unfoldingnotationintheoremvsdefinstance.html
---

## Stream: [general](index.html)
### Topic: [unfolding notation in theorem vs def/instance](01274unfoldingnotationintheoremvsdefinstance.html)

---

#### [Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341302):
```lean
instance pi.comm_ring_i {I : Type*} {f : I → Type*} [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := λ x y i, x i * y i,
  mul_assoc := _, }

/-
⊢ ∀ (a b c : Π (i : I), f i),
    (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i))
        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a b)
        c =
      (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a
        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) b c)
-/

theorem pi.comm_ring_t {I : Type*} {f : I → Type*} [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := λ x y i, x i * y i,
  mul_assoc := _, }

/-
⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)
-/
```

#### [Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341307):
The extra unfolding in `def` and `instance` is making things harder (I did not include example of `def`)

#### [Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341309):
i.e. the `*` becoming `semigroup.mul`

#### [Kenny Lau (May 31 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341354):
how can I avoid this? is this a bug?

#### [Kenny Lau (May 31 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341357):
@**Mario Carneiro**

#### [Mario Carneiro (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341402):
@**Sebastian Ullrich**

#### [Kenny Lau (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341404):
thanks

#### [Kenny Lau (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341411):
temporary workaround: change it to `theorem` where it doesn't unfold, copy the goal, use `change`/`show`, and then switch back to `def`

#### [Sebastian Ullrich (May 31 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127348395):
I'm not sure what is happening just by looking at it... but I'll leave for a short trip until Sunday soon

#### [Patrick Massot (May 31 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127348933):
I see that all the time. It's indeed a bit annoying

#### [Kenny Lau (Jun 13 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128009463):
@**Sebastian Ullrich**

#### [Kenny Lau (Jun 15 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128094754):
@**Mario Carneiro**

#### [Sebastian Ullrich (Jun 15 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128110837):
I'd have to go back to a debug build of Lean 3 to diagnose this, but it won't be fixed for Lean 3 anyway...

#### [Kevin Buzzard (Jun 15 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128111464):
So just to be clear -- there is no point noting this down as an issue anywhere on github, because we all know it won't be fixed in Lean 3, and because Lean 4 is a complete rewrite it's very unlikely that the issue will remain in Lean 4? Or could it be the case that when Lean 4 comes, exactly the same issue will be there because chunks of code were basically copied from Lean 3, and then this issue should be marked as something which should be fixed in the future. What I'm trying to establish is whether this trickle of minor Lean 3 points which will not be fixed in Lean 3 should be recorded somewhere anyway, just to check Lean 4 does not suffer from the same problems. If the chances of Lean 4 suffering from the same problem is 0% then in this case there is no point recording anything formally.

#### [Sebastian Ullrich (Jun 15 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128113301):
It's hard to say in general. There seems to be some bug somewhere in the elaborator here, which may very well survive into Lean 4 if we don't fix it specifically. _However_, Kenny's example will likely work because Lean 4 will elaborate the type and body of a `def/instance` separately if the former is given explicitly - so just like for `theorem`.

#### [Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167974):
holy mother I found a workaround

#### [Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167975):
```lean
universes u v

instance pi.comm_ring_i {I : Type*} {f : I → Type*} [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := λ x y i, x i * y i,
  mul_assoc := _, }

/-
⊢ ∀ (a b c : Π (i : I), f i),
    (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i))
        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a b)
        c =
      (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a
        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) b c)
-/

instance pi.comm_ring_i_uv {I : Type u} {f : I → Type v} [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := λ x y i, x i * y i,
  mul_assoc := _, }

/-
⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)
-/

theorem pi.comm_ring_t {I : Type*} {f : I → Type*} [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := λ x y i, x i * y i,
  mul_assoc := _, }

/-
⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)
-/
```

#### [Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167978):
@**Patrick Massot** @**Sebastian Ullrich** @**Mario Carneiro** it can be avoided by using universes instead of `Type*`

#### [Sebastian Ullrich (Jun 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128168239):
Wow, nice find. Then I can probably explain it - there is some tricky code in the structure notation elaborator that needs to unfold terms that contain metavariables - apparently it also does that for universe mvars, which it probably shouldn't do. As I said above, when you use `theorem`, the body is elaborated separately from the type, so the mvars have already been solved.

#### [Mario Carneiro (Jun 16 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128169386):
well, that was unexpected

#### [Kenny Lau (Jun 16 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128169426):
finally something unexpected :P

#### [Johan Commelin (Jun 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128171397):
I'm going to check if this will also simplify my code, and if it removes some of the issues that I've been have lately.

#### [Johan Commelin (Jun 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128171404):
But it will have to wait till Monday before I get back to Lean.

#### [Kevin Buzzard (Jun 16 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128178398):
I write all my code just using Type. I believe in ZFC!

