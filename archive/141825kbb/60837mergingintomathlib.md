---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/60837mergingintomathlib.html
---

## Stream: [kbb](index.html)
### Topic: [merging into mathlib](60837mergingintomathlib.html)

---

#### [Johan Commelin (Sep 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535620):
Clearly some parts of `kbb` are not mathlib-ready, but other parts are.

#### [Johan Commelin (Sep 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535629):
I think we should try to get those merged into mathlib.

#### [Johan Commelin (Sep 24 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535659):
For example, the remainder of the file on matrices. The monoid stuff, and determinants should also be merge-ready, I think.

#### [Johan Commelin (Sep 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535744):
I'll try to work on this when I'm back home. This is a mental note for me, and a hint for others to possible help with this (-;

#### [Johannes Hölzl (Sep 24 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134539311):
I will merge the PID -> UFD part

#### [Kevin Buzzard (Sep 25 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579577):
Just to note here that Chris defined log as the unique inverse of exp yesterday, and proved exp log = id, log exp = id on the appropriate domains. @**Chris Hughes** Is this file publically accessible?

#### [Mario Carneiro (Sep 25 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579668):
Nice! Is this the real version or the complex version?

#### [Kevin Buzzard (Sep 25 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579688):
real single-valued log from positive reals to reals

#### [Chris Hughes (Sep 25 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134621012):
@**Kevin Buzzard** Yes it is, on the `exp` branch of community mathlib.

#### [Johan Commelin (Sep 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727322):
@**Scott Morrison|110087** Do you want to PR the category of matrices? Or would you like me to do it (from community mathlib)?

#### [Johan Commelin (Sep 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727341):
@**Kenny Lau** Do you want to PR determinants? Or would you like me to do it (from community mathlib)?

#### [Scott Morrison (Sep 27 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727401):
I'm certainly happy if you want to do it. :-) I have a lot of open PRs at the moment...

#### [Scott Morrison (Sep 27 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727903):
I do kind of like the 
```
def free_module (α : Type v) [semiring α] : Type := ℕ
instance : category (free_module α) :=
{ hom  := λ m n, matrix (fin m) (fin n) α, ... }
```
 It's somehow alien and familiar at the same time.

#### [Mario Carneiro (Sep 27 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134728028):
I changed it to a large category over fintypes, what do you think?

#### [Johan Commelin (Sep 27 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729544):
@**Mario Carneiro** You also deleted a bunch of stuff on diagonal matrices, I think. Was that intentional?

#### [Mario Carneiro (Sep 27 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729550):
it all moved to mathlib

#### [Johan Commelin (Sep 27 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729823):
Hmmm, but not community mathlib...

#### [Mario Carneiro (Sep 27 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729915):
huh? just update master in that case

#### [Chris Hughes (Sep 27 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134730013):
Or update the matrix branch

#### [Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732181):
Aaah, I see what went wrong (and I was afk for 30 minutes)

#### [Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732188):
@**Mario Carneiro** Is there a reason why you didn't merge scalar matrices?

#### [Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732197):
Do you think they are not useful enough, because `diagonal` easily covers those cases?

#### [Kenny Lau (Sep 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134763925):
```quote
@**Kenny Lau** Do you want to PR determinants? Or would you like me to do it (from community mathlib)?
```
please do it

#### [Johan Commelin (Sep 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134764034):
I'll do it tomorrow

#### [Mario Carneiro (Sep 27 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134775734):
Aren't there two different definitions of permutation sign (one over `fin n`, one over a fintype) right now? I think one was developed in kbb by Kenny and the other was in a mathlib PR by Chris

#### [Kenny Lau (Sep 28 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134794434):
```quote
I'll do it tomorrow
```
the same time as when everyone does everything :p

#### [Johan Commelin (Sep 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134795246):
I promise!

#### [Johan Commelin (Sep 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134809097):
@**Kenny Lau** Done.

#### [Chris Hughes (Sep 28 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134810968):
@**Johan Commelin** @**Kenny Lau** fintype perm is in mathlib now by the way, I imagine you need that.

#### [Johan Commelin (Sep 28 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811181):
Aah, I just dumped Kenny's `sym` into the PR. Does this mean that stuff is duplicated?

#### [Chris Hughes (Sep 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811214):
Probably

#### [Chris Hughes (Sep 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811260):
Kenny did sign and stuff, which is also in mathlib.

