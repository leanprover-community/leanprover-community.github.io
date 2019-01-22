---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08557howtouselinearcombination.html
---

## [general](index.html)
### [how to use linear combination](08557howtouselinearcombination.html)

#### [Blair Shi (Jul 23 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130142613):
```
variables {k : Type u} {V : Type v}
variable [field k]
variables [ring k] [module k V]
variables {a : k} {b : V}
include k 
variables (x y : V)
variable (fvs : finite_dimensional_vector_space k V) 

def is_in_vecsp (v : V) (fvs : finite_dimensional_vector_space k V) : Prop :=
v ∈ span {v₁ : V | v₁ ∈ fvs.ordered_basis}

lemma add_closed : is_in_vecsp x fvs ∧ is_in_vecsp y fvs → is_in_vecsp (x + y) fvs :=
begin
intro h₀,
cases h₀ with le ri,
have h₁ : ∃(lc₁ : lc k V), (∀ x∉fvs.ordered_basis, lc₁ x = 0) ∧ x = lc₁.sum (λb a, a • b), from le,
```
I don't know why for `lc₁` in `lc₁.sum (λb a, a • b)`, it reports 
```
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  no_zero_divisors.to_has_zero k
inferred
  mul_zero_class.to_has_zero k
```
Can anyone help me to solve this problem?

#### [Patrick Massot (Jul 23 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130143764):
Probably not until you give us a MWE (depending only on mathlib and not your own code).

#### [Patrick Massot (Jul 23 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130143772):
You can use gist or pasteall if it's too long

#### [Reid Barton (Jul 23 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130149943):
I think you should not have both `field k` and `ring k`

#### [Kevin Buzzard (Jul 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130170440):
Yes -- try deleting the `variable [field k]` line and see if it works. If it doesn't, then follow Patrick's advice and post some code which will work for everyone, if possible.

#### [Blair Shi (Jul 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how to use linear combination/near/130176920):
Yes, I deleted `variable [field k]`. now it works. Thx!

