---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59343overridingdecidableinstances.html
---

## [general](index.html)
### [overriding decidable instances](59343overridingdecidableinstances.html)

#### [Scott Morrison (Sep 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134423873):
Can someone point me to an example of overriding a `decidable` instance with a faster algorithm?

#### [Scott Morrison (Sep 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134423881):
The implementation of `nodup_decidable` is too slow. :-)

#### [Simon Hudon (Sep 22 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424056):
You create your own instance and you give it higher priority than `nodup_decidable`. Is this for lists? Be sure that the culprit `nodup_decidable` and not the fact that comparing objects (e.g. `nat`) is slow

#### [Simon Hudon (Sep 22 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424102):
One more consideration: is this for a proof or for a program? If it's for a proof, you can write a tactic that does the comparison faster.

#### [Mario Carneiro (Sep 22 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424115):
`decidable_prime` has two implementations

#### [Mario Carneiro (Sep 22 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424265):
For checking `nodup` of big things like those lists of numbers, it helps if you've put them in order. `list.chain` is linear time

#### [Mario Carneiro (Sep 22 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424560):
Oh, wait this doesn't work for cycles, since the order matters. You can still improve on the n^2 performance of the default implementation by utilizing the order. If you sort the list then you can check for duplicates in linear time

