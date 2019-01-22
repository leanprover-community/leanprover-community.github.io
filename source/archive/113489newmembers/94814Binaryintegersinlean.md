---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/94814Binaryintegersinlean.html
---

## [new members](index.html)
### [Binary integers in lean](94814Binaryintegersinlean.html)

#### [cbailey (Nov 15 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147753615):
WRT reasoning about programs, Is there any reason to use the binary integer representations in Mathlib ala ZArith in Lean outside of reasoning about bitwise operations? It says in the comments that their use is discouraged since Lean doesn't share Coq's reliance on kernel reduction; does Lean have some evaluation strategy for making functions written with Z and N run in non-linear time? Thanks for any help!

#### [Kenny Lau (Nov 15 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147764557):
so if you try to use `norm_num` to prove that `10+11=21` for real numbers, they use bitwise addition

#### [Andrew Ashworth (Nov 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147768966):
Lean's kernel has special optimized versions of nat and int when used with `#eval`

#### [Andrew Ashworth (Nov 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147768982):
iirc

#### [Andrew Ashworth (Nov 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147769022):
if you're trying to do meta-programming or reflection, then use zarith

#### [cbailey (Nov 15 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147780590):
Thank you.

