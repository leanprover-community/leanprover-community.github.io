---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62075elabaseliminator.html
---

## Stream: [general](index.html)
### Topic: [elab_as_eliminator](62075elabaseliminator.html)

---

#### [Reid Barton (Jun 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740170):
Is there an explanation of what `elab_as_eliminator` actually does somewhere? I once tried reading the source, but wasn't enlightened.
I know there is a selection bias at work here, in that I never notice when it does the right thing, but several times I've found that it fails to infer apparently obvious type parameters, where `elab_with_expected_type` succeeds.

#### [Reid Barton (Jun 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740610):
Here is a toy example where `elab_as_eliminator` fails but `elab_with_expected_type` succeeds:
```lean
def equal_mod (n : ℤ) (a b : ℤ) : Prop :=
∃ c, a - b = n * c

def mod_setoid (n : ℤ) : setoid ℤ :=
{ r := equal_mod n, iseqv := sorry }
   
def Z_mod (n : ℤ) := quotient (mod_setoid n)
   
local attribute [elab_with_expected_type] quot.lift_on

def mod_dvd (n k : ℤ) : Z_mod (n * k) → Z_mod n :=
λ x, quot.lift_on x
  (λ a, quot.mk _ a)
  (λ a a' ⟨c, h⟩, quot.sound ⟨k * c, by rw ←mul_assoc; exact h⟩)
```

#### [Mario Carneiro (Jun 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740763):
`elab_as_eliminator` is meant for eliminators, where lean has to infer a higher order argument, namely the "motive"

#### [Mario Carneiro (Jun 27 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740806):
It's not a good fit for nondependent elimination since you can just use the usual first order unification

#### [Reid Barton (Jun 27 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740842):
OK, that was what I suspected, but wasn't sure. So ideally, methods like `lift` and `lift_on` shouldn't have that attribute, since they are nondependent

#### [Mario Carneiro (Jun 28 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740909):
something like `quot.rec_on` would be better

#### [Reid Barton (Jun 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740977):
Even then, this strategy is only appropriate when you want to infer the motive from the types of the arguments, rather than from the return type, right?

#### [Reid Barton (Jun 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740984):
Assuming the return type is something like `β q`, for which the higher-order unification problem is trivial

#### [Mario Carneiro (Jun 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741005):
The motive is inferred from the return type, not the types of the arguments

#### [Reid Barton (Jun 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741010):
Oh hmm, I see

#### [Reid Barton (Jun 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741014):
but even then the problem is not necessarily trivial

#### [Mario Carneiro (Jun 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741071):
it finds instances of the value being inducted on and replaces them with a variable

#### [Mario Carneiro (Jun 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741075):
and that becomes the motive

#### [Mario Carneiro (Jun 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741148):
```
example (x y : ℕ) : x + y = y + x :=
nat.rec_on (x + y)
  _ -- ⊢ 0 = y + x
  _ -- ⊢ ∀ (n : ℕ), n = y + x → nat.succ n = y + x
```

#### [Reid Barton (Jun 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741162):
So why does it fail on the `mod_dvd` example? Wouldn't it conclude that `quot.mk _ a : Z_mod n`?

#### [Mario Carneiro (Jun 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741233):
vs:
```
local attribute [elab_with_expected_type] nat.rec_on
example (x y : ℕ) : x + y = y + x :=
nat.rec_on (x + y) _ _
-- unexpected argument at application
--   nat.rec_on (x + y)
-- given argument
--   x + y
-- expected argument
--   y + x
```
The reason this error is reported is since the output type is `C n`, without doing higher order unification it matches against `eq (x + y) (y + x)` so it expects the major premise to be `y+x`

#### [Reid Barton (Jun 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741235):
it seems to figure this out if I give less detail in the last argument, for example replacing it by `(λ a a' h, sorry)`

#### [Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741405):
You have to put a `by exact` in the right place, to delay the elaboration of the let match

#### [Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741408):
```
def mod_dvd (n k : ℤ) : Z_mod (n * k) → Z_mod n :=
λ x, quot.lift_on x
  (λ a, quot.mk _ a)
  (by exact λ a a' ⟨c, h⟩, quot.sound ⟨k * c, by rw ←mul_assoc; exact h⟩)
```

#### [Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741411):
this works

