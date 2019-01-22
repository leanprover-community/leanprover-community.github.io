---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17447readablesubquotients.html
---

## [general](index.html)
### [readable subquotients](17447readablesubquotients.html)

#### [Johan Commelin (Oct 01 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968883):
So, let me return to my original question.

#### [Johan Commelin (Oct 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968900):
I've got
```lean
definition Spa (A : Huber_pair) : set (Spv A) :=
Spv.lift (λ v, v.is_continuous ∧ ∀ r, r ∈ A⁺ → v.val.val r ≤ 1)
(λ v₁ v₂ heq, sorry)

-- fake
definition Spa' (A : Huber_pair) : set (Spv A) :=
{v : Spv A | v.is_continuous ∧ ∀ r, r ∈ A⁺ → v.val.val r ≤ 1}
which_is_well_defined (λ v₁ v₂ heq, sorry)
```

#### [Johan Commelin (Oct 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968965):
Maybe it is really minor to people who have seen Lean for 367 days in the last year, but I think `Spa'` is a lot more readable than `Spa`.

#### [Johan Commelin (Oct 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134969006):
Of course any mathematician who takes a first look is already brain-blocked by `set (Spv A)`, which means "subset" instead of "set". But never mind...

#### [Kevin Buzzard (Oct 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134974894):
Can't you put the work into the definition of `v.is_continuous`?

#### [Johan Commelin (Oct 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134975038):
I'm not sure if that would help. Or do you mean that you want to define `Spa` as intersection of two subsets? Namely `Cont` and the other condition.

#### [Johan Commelin (Oct 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134975061):
Still feels like moving the problem around...

