---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32035Physics.html
---

## [general](index.html)
### [Physics?](32035Physics.html)

#### [Wojciech Nawrocki (Sep 27 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134742787):
Hey, I'm curious - are there any physicists here looking at formalising some of the vector algebra for quantum theory? I couldn't find anything related to e.g. Hilbert spaces.

#### [Kevin Buzzard (Sep 27 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743245):
A first year undergraduate student of mine formalised the definition of Hilbert spaces as part of their summer project, but I don't think there's anything in the official maths library.

#### [Sean Leather (Sep 27 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743354):
I don't recall any physicists coming forward openly. But if you are one, you'd better [beware](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/physics.20attack/near/134230265).

#### [Kevin Buzzard (Sep 27 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743483):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Banach%20spaces.lean and and there are inner product spaces too, but actually I don't see Hilbert space yet.

#### [Andreas Swerdlow (Sep 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134746069):
I’m pretty sure I fixed the issue with Hilbert space so hope to PR soon

#### [Andreas Swerdlow (Sep 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134746268):
Although I only have one trivial lemma about Hilbert Spaces specifically

#### [Wojciech Nawrocki (Sep 28 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134777737):
Ok, thanks! I was looking at (maybe) formalising some results that require notions of a Hilbert space.
@**Andreas Swerdlow** do you mean it might be included in mathlib at some point?

#### [Andreas Swerdlow (Sep 28 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134779717):
Hopefully, but it probably needs some cleaning up

