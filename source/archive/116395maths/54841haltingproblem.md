---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54841haltingproblem.html
---

## [maths](index.html)
### [halting problem](54841haltingproblem.html)

#### [Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964377):
https://github.com/leanprover/mathlib/commit/d62bf5605ec8971d446a01af40abf9183447cb42#diff-6650f7dae83be3a52c8eb036a23d7b26R175

#### [Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964379):
holy mother you did it @**Mario Carneiro**

#### [Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964380):
congratulations

#### [Mario Carneiro (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964383):
You can see it's just a corollary of a much stronger theorem

#### [Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964401):
oh and which commit should i checkout?

#### [Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964425):
you didn't bother to build any

#### [Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964426):
I think Rice's theorem is cool

#### [Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964427):
?

#### [Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964428):
I eat them every day

#### [Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964429):
https://github.com/leanprover/mathlib/commits

#### [Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964430):
there are no green ticks after April 29

#### [Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964434):
that's weird

#### [Mario Carneiro (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964442):
travis usually kicks in automatically

#### [Kenny Lau (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964445):
so which commit should i use?

#### [Mario Carneiro (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964450):
I have been building locally so they should work, but I guess I should find out what's up with travis

#### [Kenny Lau (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964490):
and which lean version?

#### [Mario Carneiro (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964491):
3.4.1

#### [Gabriel Ebner (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964492):
Travis is broken on the other packages as well. "This is not an active repository
You don't have sufficient rights to enable this repo on Travis. 
Please contact the admin to enable it or to receive admin rights yourself." @**Sebastian Ullrich** ?

#### [Mario Carneiro (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964497):
I always get that message, but it did not affect the build itself

#### [Gabriel Ebner (May 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964505):
Either way, `super` does not get built by travis either at the moment.

#### [Sebastian Ullrich (May 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126965515):
I'll have to ask Leo

#### [Kevin Buzzard (May 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126965572):
you have a halting problem

#### [Sebastian Ullrich (May 23 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126979574):
https://travis-ci.org/leanprover/mathlib now looks more promising

