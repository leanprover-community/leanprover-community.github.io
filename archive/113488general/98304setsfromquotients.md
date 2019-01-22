---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98304setsfromquotients.html
---

## [general](index.html)
### [sets from quotients](98304setsfromquotients.html)

#### [Chris Hughes (Feb 26 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123007417):
Sets from quotients. Is there a function in lean which basically gives me this `{a : α // setoid.r (quot.out x) a}`. Also is there any tutorial anywhere on how things like heq, eq.dcases_on, eq.rec_on etc work?

#### [Andrew Ashworth (Feb 26 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123007526):
you need to fire up your Coq installation and read http://adam.chlipala.net/cpdt/html/Equality.html :|

#### [Simon Hudon (Feb 26 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123007681):
Once you've learned about them, feel free to write a Lean documentation for them

#### [Chris Hughes (Feb 26 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123009408):
What I've discovered is typing `induction h` where h is the proof that the types are equal, help to solve heq goals very easily

#### [Patrick Massot (Feb 26 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123010391):
Yes, you're in the right mindset now! You can go and write some doc

#### [Mario Carneiro (Feb 27 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123019353):
This can also be expressed as `{a // ⟦a⟧ = x}`

#### [Chris Hughes (Feb 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets from quotients/near/123019369):
I just realised that. Probably more sensible.

