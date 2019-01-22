---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72652Isthereawaytocomplicatethingswithsimp.html
---

## [new members](index.html)
### [Is there a way to complicate things with simp?](72652Isthereawaytocomplicatethingswithsimp.html)

#### [Abhimanyu Pallavi Sudhir (Nov 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a way to complicate things with simp?/near/148315124):
I.e. is there a way to write `simp [←lemma, lemma, lemma]`?

#### [Kenny Lau (Nov 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a way to complicate things with simp?/near/148315168):
`simp [(lemma).symm, lemma, lemma]`

#### [Abhimanyu Pallavi Sudhir (Nov 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a way to complicate things with simp?/near/148315223):
That doesn't always work, though. For instance, I'm trying to do `simp [(polynomial.sum_C_mul_X_eq p).symm, finsupp.sum, polynomial.derivative_sum],` -- rewrites work, but `simp` doesn't.

#### [Kevin Buzzard (Nov 25 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a way to complicate things with simp?/near/148318355):
`simp` might be taking a wrong turn before it tries the rewrites you want. Switch logging on if you want to investigate further -- see the `simp` docs in mathlib for an explanation of how to do this.

