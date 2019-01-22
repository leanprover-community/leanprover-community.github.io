---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88174HowmanyuniversesdidIuse.html
---

## [general](index.html)
### [How many universes did I use?](88174HowmanyuniversesdidIuse.html)

#### [Kevin Buzzard (May 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046011):
I proved a theorem in Lean (that an affine scheme is a scheme). Along the way I understood a little more about universes. In particular, I realised that the ZFC proof I knew that an affine scheme was a scheme "took place entirely within Type", by which I mean that every term I used was "good" -- here "good" is defined thus: (1) Type is good; (2) If X is a term of type Y and Y is good then X is good; (3) that's it. Once I realised this I went through a lot of files in my project that had lines of the form "universes u v w" and replaced them with "universe u", I also replaced many "Type v" and "Type *" with "Type u".

#### [Kevin Buzzard (May 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046019):
How do I check that I caught all of them?

#### [Patrick Massot (May 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046082):
What do you gain from these modifications?

#### [Mario Carneiro (May 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046330):
Agreed - these modifications do nothing toward your goal of eliminating unverse use

#### [Mario Carneiro (May 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046359):
What would help is using `Type` instead of `Type u` or `Type*`, but I don't recommend this

#### [Chris Hughes (May 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046363):
Doesn't changing Type v to Type u just make the theorem less general, and just worse?

#### [Mario Carneiro (May 24 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046428):
But your definition good is overly restrictive - `ring` is not good, not even `ring.{0}`, so `ring A` is also not good

#### [Mario Carneiro (May 24 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046459):
In fact clearly delineating what parts of DTT make sense in ZFC is rather delicate

#### [Patrick Massot (May 24 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127046470):
We should have asked how many questions he marked before answering this thread

#### [Kevin Buzzard (May 25 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073702):
You're right that my definition of good is bad. I definitely don't want to put everything into Type because then other people won't want to use my code. But there *is* an underlying question here, and perhaps the answer is in Mario's comment "In fact clearly delineating what parts of DTT make sense in ZFC is rather delicate". I want to know the answer though. Is there any way I can find out whether my definition "would go through if I went through every file I used and removed all mention of universes, and changed all `Type u` and `Type*` to `Type`"?

#### [Chris Hughes (May 25 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073805):
It would go through, but nobody would be able to define a scheme structure on anything outside Type if I understand the question. So it would just be a less general definition.

#### [Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073876):
"It would go through" -- how do you know this?

#### [Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073878):
Cardinals wouldn't, right?

#### [Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073882):
I agree that it would be a bad idea to do so

#### [Kevin Buzzard (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073883):
however I know people who care about this question.

#### [Kevin Buzzard (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073893):
People whose _definition_ of mathematics is ZFC could argue that I am not doing mathematics if I use two universes.

#### [Mario Carneiro (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073894):
I've attempted to do this in my lean type theory paper

#### [Chris Hughes (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073895):
I misunderstood the question.

#### [Mario Carneiro (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073896):
several natural definitions were tried and dismissed

#### [Kevin Buzzard (May 25 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073936):
There are parts of mathlib which really use more than one universe, right?

#### [Mario Carneiro (May 25 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How many universes did I use?/near/127073948):
All parts of mathlib are universe polymorphic, so it's often hard to say, the answer is "yes trivially" if you don't ask carefully

