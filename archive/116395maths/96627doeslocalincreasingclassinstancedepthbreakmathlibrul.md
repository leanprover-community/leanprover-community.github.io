---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96627doeslocalincreasingclassinstancedepthbreakmathlibrul.html
---

## [maths](index.html)
### [does local increasing class instance depth break mathlib rul](96627doeslocalincreasingclassinstancedepthbreakmathlibrul.html)

#### [Chris Hughes (Aug 13 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/does local increasing class instance depth break mathlib rul/near/132068633):
So I'm doing Sylow's theorems in lean, and one of the proofs requires me to synthesize a `fintype` instance for the product of a subtype of a subtype of a finite type and a subtype of a quotient of a subtype of a finite type. This is complicated enough that the normal depth isn't good enough, but a deeper depth is good enough. Is it approved to increase the type class inference depth to deal with situations like these? The offending code is line 404 of https://github.com/dorhinj/mathlib/blob/sylow/group_theory/sylow.lean

#### [Chris Hughes (Aug 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/does local increasing class instance depth break mathlib rul/near/132072872):
Update. Proving one extra lemma has solved this problem.

