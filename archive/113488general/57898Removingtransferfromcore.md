---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57898Removingtransferfromcore.html
---

## Stream: [general](index.html)
### Topic: [Removing transfer from core](57898Removingtransferfromcore.html)

---

#### [Gabriel Ebner (Jan 10 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154832021):
@**Johannes Hölzl** suggested removing transfer from core and move it into mathlib.  Maybe the biggest positive effect is that we could then use the ⇒ symbol in mathlib.
I tried just removing the file, but some theorems about integers and dlist are proving using transfer.  Any ideas?  Does anyone want to rewrite the proofs by hand?  Should we just remove the ⇒ notation for 3.4.2?

#### [Kevin Buzzard (Jan 10 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154832868):
Can one move those theorems about integers out of core as well?

#### [Gabriel Ebner (Jan 10 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154835519):
Probably not:
```lean
instance : comm_ring int :=
{ add            := int.add,
  add_assoc      := by int.transfer,
  zero           := int.zero,
  zero_add       := by int.transfer,
  add_zero       := by int.transfer,
  neg            := int.neg,
  add_left_neg   := by int.transfer,
  add_comm       := by int.transfer,
  mul            := int.mul,
  mul_assoc      := by int.transfer tt,
  one            := int.one,
  one_mul        := by int.transfer,
  mul_one        := by int.transfer,
  left_distrib   := by int.transfer tt,
  right_distrib  := by int.transfer tt,
  mul_comm       := by int.transfer}
```

#### [Simon Hudon (Jan 10 2019 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853060):
Can a more specific script handle them? E.g. search and replace mul with add and other lemmas similarly? Also Can we take dlist out of core?

#### [Gabriel Ebner (Jan 10 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853245):
`dlist` is not the problem.  Only three examples for `dlist` use `transfer`.

#### [Gabriel Ebner (Jan 10 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853346):
It's the integers that are problematic.  We prove that the integers form a commutative ring using transfer, I'm not sure we should remove that instance from core.

#### [Gabriel Ebner (Jan 10 2019 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853532):
Maybe I should clarify: `transfer` here switches between two isomorphic representations of the integers.  The definition of `int` is an inductive type with two constructors 1) non-negative natural number 2) negative number.  The `transfer` tactic then switches to the much nicer definition using pairs of natural numbers.

#### [Andrew Ashworth (Jan 10 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853971):
The proofs for `int` should be in the git history, iirc. They were not always proved via transfer, but maybe I am thinking of Lean 2.

#### [Gabriel Ebner (Jan 10 2019 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154854522):
Doesn't even look so bad.  I thought it was more horrible:
```lean
 protected lemma distrib_left (a b c : ℤ) : a * (b + c) = a * b + a * c :=
begin
  cases (int.left_total_rel_int_nat_nat a) with a' ha,
  cases (int.left_total_rel_int_nat_nat b) with b' hb,
  cases (int.left_total_rel_int_nat_nat c) with c' hc,
  apply (int.rel_eq (int.rel_mul ha (int.rel_add hb hc))
    (int.rel_add (int.rel_mul ha hb) (int.rel_mul ha hc)))^.mpr,
  simp [mul_add, add_mul]
end
```
https://github.com/leanprover/lean/commit/1f45995c169fb518177dfad5060b5a748e8a3b1f#diff-3e35acfba743354acb6f107e860bdb79

#### [Simon Hudon (Jan 10 2019 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154855637):
How are integers used in core? I thought only natural numbers were really needed there

#### [Reid Barton (Jan 10 2019 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154855944):
What about, in 3.4.2, simply freeing up the character ⇒ somehow, while leaving transfer and the instances in place?

#### [Simon Hudon (Jan 10 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154856174):
Actually @**Johannes Hölzl** and I would really like to move `transfer` to mathlib so that we can keep developing it

#### [Johannes Hölzl (Jan 10 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154860802):
well, `transfer` is not so important (we can copy it under another name). I guess `⇒` is more important for some people

#### [Mario Carneiro (Jan 10 2019 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154869086):
I can rewrite the proofs for `int` if required; do the previous proofs work?

#### [Gabriel Ebner (Jan 10 2019 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154869179):
Probably.

#### [Gabriel Ebner (Jan 11 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154931531):
See https://github.com/leanprover/lean/pull/1989

