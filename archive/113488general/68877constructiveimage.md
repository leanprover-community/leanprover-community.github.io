---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68877constructiveimage.html
---

## Stream: [general](index.html)
### Topic: [constructive image](68877constructiveimage.html)

---

#### [Kenny Lau (Mar 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124280837):
Maybe we should define the image of a map f:X->Y to be X quotient by the relation that x~y iff f(x)=f(y)

#### [Kenny Lau (Mar 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124280848):
is this how it is done in HoTT?

#### [jmc (Mar 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124281324):
That is usually called the coimage, I think: https://en.wikipedia.org/wiki/Coimage

#### [Kenny Lau (Mar 27 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124281847):
hmm, I've never heard of coimage.

#### [Kenny Lau (Mar 27 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124281852):
I think using this instead of the usual image will make things more constructive

#### [jmc (Mar 27 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282326):
O.o... you are heading down the constructive path? It seems that happens to every one who starts doing formal proofs...

#### [jmc (Mar 27 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282343):
Anyway, even in classical maths you need the isomorphism theorem to tell you that coimage = image

#### [jmc (Mar 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282402):
In certain settings that theorem might fail

#### [jmc (Mar 27 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282428):
E.g. in topology: you will get the same set, but the quotient topology on the coimage may be finer then the subset topology on the image

#### [Kenny Lau (Mar 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282660):
@**jmc** "you are heading down the constructive path?"

#### [Kenny Lau (Mar 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282669):
I've been walking in this path for some time

#### [jmc (Mar 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124282734):
Ok, never mind (^; I am wandering back and forth between constructive and classical maths as well

#### [Patrick Massot (Mar 27 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124285270):
Kenny, you should search for coimage on this Zulip forum

#### [Patrick Massot (Mar 27 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124285326):
(usable search is part of the reason why we switched from Gitter to Zulip)

#### [Patrick Massot (Mar 27 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124285335):
You should also stop this constructive madness but this is another story

#### [Kenny Lau (Mar 27 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124285475):
lol

#### [Kenny Lau (Mar 27 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructive%20image/near/124285605):
@**Patrick Massot** I searched it and saw you crap-talking about constructivism :P

