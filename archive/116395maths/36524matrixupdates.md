---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36524matrixupdates.html
---

## Stream: [maths](index.html)
### Topic: [matrix updates](36524matrixupdates.html)

---

#### [Sean Leather (Sep 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133716760):
@**Kevin Buzzard** I worked a bit on matrices on the side. I don't know if you'll be happy with the differences with [#334](https://github.com/leanprover/mathlib/pull/334), so I PR'd [#2](https://github.com/leanprover-community/mathlib/pull/2) to your branch on `leanprover-community/mathlib`. Let me know what you think.

#### [Sean Leather (Sep 11 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133716918):
BTW, to view the diff while ignoring whitespace changes, see https://github.com/leanprover-community/mathlib/pull/2/files?w=1 . There are still a lot of changes. :concerned: But I believe all of the major stuff that was in your original PR is still there.

#### [Johan Commelin (Sep 11 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133720033):
Cool, so now matrices are even a ring. Nice work Sean!

#### [Johan Commelin (Sep 11 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133720056):
I agree that the diff looks a bit daunting. But I think that is mostly because of some syntactic changes that don't represent a very big change in mathematics.

#### [Kevin Buzzard (Sep 11 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133721556):
I am completely happy with any changes. I am just tired of matrices not being in Lean (as are some of my "clients", as Mario once referred to them).

#### [Kevin Buzzard (Sep 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133722723):
PS @**Johan Commelin** Ellen proved they were a ring :P . @**Sean Leather** I should also add -- thanks a lot!

#### [Sean Leather (Sep 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133723059):
Yes, all the credit should go to people who worked on it before me. I just build on the shoulders of giants. Also, I think the `fintype` idea was due to Johannes and Johan. Since Kevin is happy, I merged the PR.

#### [Johan Commelin (Sep 12 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133778267):
Somehow Travis is now failing (and it is not a timeout). It didn't receive any output for 10min.

