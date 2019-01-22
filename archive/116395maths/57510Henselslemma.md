---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/57510Henselslemma.html
---

## [maths](index.html)
### [Hensel's lemma](57510Henselslemma.html)

#### [Johan Commelin (Sep 11 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133747941):
@**Rob Lewis** has PR'd Hensel's lemma for the p-adics! :tada: :octopus: :muscle:
https://github.com/leanprover/mathlib/pull/337/files?w=1

#### [Johan Commelin (Sep 11 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133747982):
Rob, would you mind sharing a bit of your long term plans? It seems like you project and the perfectoid project could strengthen each other.

#### [Johan Commelin (Sep 11 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133748063):
I'm really excited to see all this stuff materialising.

#### [Kevin Buzzard (Sep 11 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133748199):
In terms of what is needed to do modern mathematics I guess one has to plough through Serre's book on local fields

#### [Rob Lewis (Sep 11 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750674):
There's not so much of a long term plan right now. I've just been talking to Sander Dahmen about what we'll need to start formalizing his work, like we promised in the Lean Forward project. This seemed like a good place to start.

#### [Johan Commelin (Sep 11 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750700):
It definitely is.

#### [Rob Lewis (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750750):
Short term, I want to see what I can do about cleaning up some of the annoying inequality proofs in that PR.

#### [Johan Commelin (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750776):
I am not intimately familiar with Sanders work, but I do worry a tiny little bit that in the near future you might need to do a lot of this again for completions of number fields.

#### [Rob Lewis (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750781):
I'm sure there's plenty of overlap between Lean Forward and the perfectoid project, maybe we could get everyone together and chat sometime.

#### [Johan Commelin (Sep 11 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750813):
I think starting from a slightly more general perspective might pay off in the long run.

#### [Johan Commelin (Sep 11 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750841):
Let me put it like this: I would be very surprised if the only local rings in Sanders work are p-adics. I would expect to also find finite extensions of those.

#### [Johan Commelin (Sep 11 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750853):
And usually the proofs are almost the same difficulty.

#### [Johan Commelin (Sep 11 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133750906):
This is absolutely not meant as criticism.

#### [Patrick Massot (Sep 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133757316):
```quote
Short term, I want to see what I can do about cleaning up some of the annoying inequality proofs in that PR.
```
Did you have a look at Simon's mono tactic? It's not yet merged but it's in the nursery

#### [Patrick Massot (Sep 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133757562):
@**Rob Lewis** would you mind documenting your p-adic work somewhere in https://github.com/leanprover/mathlib/tree/master/docs/theories?

#### [Johan Commelin (Sep 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel's lemma/near/133786975):
@**Rob Lewis** Thanks for the documentation!

