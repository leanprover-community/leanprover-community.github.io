---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05743tacticforunfoldingdefinition.html
---

## [general](index.html)
### [tactic for unfolding definition](05743tacticforunfoldingdefinition.html)

#### [Kenny Lau (Mar 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764614):
If I've defined `def A := B` and my goal / hypothesis contains A, how do I replace A with B?

#### [Moses Schönfinkel (Mar 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764700):
`unfold` :)

#### [Kenny Lau (Mar 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764708):
I tried it already

#### [Kenny Lau (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764717):
here's the context that might help: I'm defining `A` in the middle of a structure

#### [Kenny Lau (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764727):
```
class foo :=
(A := B)
```

#### [Simon Hudon (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764731):
What happens when you try it?

#### [Kenny Lau (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764794):
```
unfold tactic failed, A does not have equational lemmas nor is a projection

#### [Moses Schönfinkel (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764801):
ok first let's eliminate one problem; try `delta` instead of `unfold`

#### [Moses Schönfinkel (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764806):
if that works, you're trying to unfold something you have no "business" unfolding

#### [Kenny Lau (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764810):
```
dsimplify tactic failed to simplify

#### [Reid Barton (Mar 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764838):
isn't `(A := B)` there just a default value?

#### [Kenny Lau (Mar 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764884):
oh... I can't define things inside a structure?

#### [Simon Hudon (Mar 15 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764908):
No, that's not possible

#### [Kenny Lau (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764913):
ok

#### [Simon Hudon (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764956):
That would be useful

#### [Simon Hudon (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764972):
They might consider it in the future. Recently, they have adopted implicit fields

#### [Reid Barton (Mar 15 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123765042):
You can sort of emulate it with multiple structures, like how the algebraic classes are build on top of `has_foo` classes and so can take advantage of intervening `notation` declarations

