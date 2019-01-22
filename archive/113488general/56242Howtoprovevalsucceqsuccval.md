---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56242Howtoprovevalsucceqsuccval.html
---

## [general](index.html)
### [How to prove val_succ_eq_succ_val](56242Howtoprovevalsucceqsuccval.html)

#### [Johan Commelin (May 15 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591309):
This feels almost defeq to me. But I am stumped how to prove this:
```lean
lemma val_succ_eq_succ_val (j : fin n) : j.succ.val = j.val.succ := sorry
```

#### [Sean Leather (May 15 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591395):
```lean
lemma val_succ_eq_succ_val {n : ℕ} (j : fin n) : j.succ.val = j.val.succ :=
by cases j; simp [fin.succ]
```

#### [Johan Commelin (May 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591498):
Aaaahaaa.

#### [Patrick Massot (May 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592224):
I think we should add this sentence to our bluff toolbox. Instead of saying "the following is trivial", as we always do, we could say "the following is almost defeq".

#### [Patrick Massot (May 15 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592283):
People may think we are a bit weird (at least until proof assistant manage to take over the world).

#### [Patrick Massot (May 15 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592313):
But it won't be worse than all those students who took Kevin's exam on Monday and will get as their only explanation for poor grade: this doesn't type check.

#### [Patrick Massot (May 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592377):
Actually I'm reading this because I procrastinate writing a referee report. I should send "this paper does not type check" and be done with it

#### [Kevin Buzzard (May 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592408):
I have taken off many points for solutions which don't type-check.

#### [Kevin Buzzard (May 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592466):
I ask them what `P_4(X)` is, and many people tell me that it is `8cos(theta)^4-8cos(theta)^2+1`

#### [Kevin Buzzard (May 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592475):
[P_n(X) satisfies P_n(cos(theta))=cos(n.theta)]

#### [Patrick Massot (May 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592507):
Right now I'm staring at some `wlog` without filling in the proof obligation in that paper I need to referee

#### [Kevin Buzzard (May 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592537):
One student wrote down the answer and said it was true "by symmetry"

#### [Kevin Buzzard (May 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592577):
and I thought "hmm, I don't think that will work in Lean"

#### [Kevin Buzzard (May 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592579):
but at least it typechecks

#### [Reid Barton (May 15 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126599292):
Replying to the original question; alternatively
```lean
by cases j; refl
```
which shows how almost-defeq it really is

#### [Johan Commelin (May 15 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601422):
@**Mario Carneiro** Should this be in mathlib?

#### [Johan Commelin (May 15 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601623):
And the analogue for `pred`.

#### [Johan Commelin (May 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601692):
More generally: should I just create PR's for such small additions, or is it too trivial for that?

#### [Mario Carneiro (May 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126610125):
Small additions are fine, since they are focused and usually don't have dependency problems they are easy to review. I think it is not a good idea to have a lower bound on "too trivial" because then you have to find other things to do in the PR or forget about your little fix. It's rules like that that make typos like `αdditive` persist in lean core for so long

#### [Mario Carneiro (May 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126610143):
I would call the theorem `succ_val` though

#### [Johan Commelin (May 16 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126660987):
Done: https://github.com/leanprover/mathlib/pull/138

