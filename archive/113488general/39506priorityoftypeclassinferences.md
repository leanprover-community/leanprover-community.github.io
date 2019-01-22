---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39506priorityoftypeclassinferences.html
---

## [general](index.html)
### [priority of typeclass inferences](39506priorityoftypeclassinferences.html)

#### [Kenny Lau (Apr 21 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473385):
If I proved `A.to_B` and `A.to_C` and `B.to_D` and `C.to_D`, when I want to coerce `A` to `D`, how does Lean judge which path to use?

#### [Mario Carneiro (Apr 21 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473768):
Unless you explicitly set priorities using `@[priority n]`, the highest priority goes to the last declared instance. So if it's looking for a `D` and `C.to_D` was declared second, it uses that and looks for a `C`, finding `A.to_C`.

That said, it is possible to end up with the other path if you perform a typeclass search before the second instance is declared, or if you compose typeclass proofs, so this is why I recommend `B.to_D (A.to_B inst)` be defeq to `C.to_D (A.to_C inst)` in this circumstance.

#### [Kenny Lau (Apr 21 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473817):
is it even possible to make them defeq?

#### [Mario Carneiro (Apr 21 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473893):
sure... most "forgetful functor" type instances will have this property

#### [Kenny Lau (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473944):
aha, my functors are usually free functors though

#### [Kenny Lau (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473946):
I'm making a free group ^^

#### [Mario Carneiro (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473949):
do you have a particular diamond in mind?

#### [Kenny Lau (Apr 21 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474065):
aha, I had one when I analyzed onote.repr wrongly

#### [Kenny Lau (Apr 21 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474112):
i.e. providing a constructive path that `nat.lt` is computably well-founded

#### [Mario Carneiro (Apr 21 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474123):
By the way if you are on a quest to remove `noncomputable` you should start with the `ordinal` file which contains tons of `noncomputable` things

#### [Kenny Lau (Apr 21 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474124):
you're right

#### [Mario Carneiro (Apr 21 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474170):
I think you will hit your head against some hard problems and realize it's impossible eventually, but feel free to try :)

#### [Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505702):
Kenny, did you follow the metric space / topological space story a couple of months ago?

#### [Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505705):
Patrick was horrified to find that the _definition_ of metric space was a structure which included the metric _and_ the topology!

#### [Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505713):
It turned out that it was because the mathlib people wanted the coercion from a metric space to a top space to be a forgetful functor!

#### [Kevin Buzzard (Apr 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505759):
Now they have the clever solution of putting the topology as part of the structure, but auto-generating it from the metric :-)

#### [Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505767):
https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md

#### [Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505768):
Unfinished notes

#### [Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505770):
Maybe I should add something from this thread

