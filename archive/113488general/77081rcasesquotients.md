---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77081rcasesquotients.html
---

## Stream: [general](index.html)
### Topic: [rcases + quotients](77081rcasesquotients.html)

---

#### [Reid Barton (Sep 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133602376):
I just saw this a moment ago but I think this commit by Johannes needs to be advertised: https://github.com/leanprover/mathlib/commit/5613d2ecc92ce8fae9555745bd94756dec61a323

#### [Kevin Buzzard (Sep 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133604475):
I look at that commit and I see (1) a commit (2) a title which I don't quite understand and no examples (3) 11 changed files so it's very difficult for me to see the wood from the trees. I find this with many commits to be honest -- things have changed a bit, I don't really know what has happened, I don't have time to look in detail and don't even know whether I will understand what I find. So many commits happen and I get emails about them all but this is not a viable system for me, I need something more digestible. I propose a new thread "this week's commits in mathlib" in the #maths stream, where people can summarise things which they think the community might find useful. I'm not suggesting that people should post to this thread when they make a commit -- on the contrary -- in fact I think I'm suggesting that every few days when I delete a bunch more emails I post myself to the thread trying to summarise what happened and then people who know better correct me. Do you think this sounds workable? I don't see any harm in trying.

#### [Reid Barton (Sep 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133604818):
In this case most of those changed files are the examples. I was going to copy an example diff here, but it was hard to find one which would be immediately understandable without context. The basic idea is that you can use `rcases` (instead of `quot.induction_on` and its variants) to extract a representative from a value of a quotient type (as long as you're proving a Prop).
I do agree that some kind of periodical "what's new" announcements would be great to have--maybe not restricted to mathlib, but also other projects going on in the community like perfectoid spaces.

#### [Johannes Hölzl (Sep 09 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605832):
In this case I hoped it would be enough to just look into the changes to the documentation. The idea is very simple: We see quotient types as type you can do cases on, like datatypes. A quotient types only stores one element from the base type, this is what you match on.

Now instead of writing:
```lean
assume x, quotient.induction_on x $ assume a, ...
```
 you just write
```lean
by rintro ⟨a⟩; exact ...
```
(or even shorter if you stay in tactic mode.

The biggest difference to usual the usual case on datatypes is that this only works in proofs.

#### [Johannes Hölzl (Sep 09 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605888):
And of course it gets much more important when you have multiple variables:
```lean
assume x y z, quotient.induction_on x $ assume a, quotient.induction_on y $ assume b, quotient.induction_on z $ assume c, ...
```
is just
```lean
by rintro ⟨a⟩ ⟨b⟩ ⟨c⟩; exact ...
```

#### [Kevin Buzzard (Sep 09 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605932):
I'm sure it's easy to find out what's going on if you know where to look. One issue with the system is that whilst I get email notifications for all PR's, I don't think I get notifications when you or Mario make commits (and if memory serves I think I raised this issue before and I don't think anyone knew how to make this happen). So in practice I find these things easy to miss. 

Thanks for the summary Johannes!

#### [Johannes Hölzl (Sep 09 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133606111):
Hm, yeah direct commits are hard to follow. The announcement channel you just started is a good idea, I will try to announce stuff there.

#### [Kevin Buzzard (Sep 09 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133606375):
Let's see how it goes. Reid's comment about perfectoids made me realise that I am not the only one who realises that they can't see the big picture. There has been no chat in the perfectoid stream for a while but all my recent work on Noetherian stuff is all related and I didn't even mention that my first non-trivial PR had been accepted because currently the direct link to the perfectoid stuff is weak -- what we are aiming for is integral closure of a ring and there's still some way to go.

#### [Mario Carneiro (Sep 09 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133617771):
Re email notifications, RSS has basically emerged as a standard for this kind of thing. I have an RSS reader installed in my browser, and just about every website offers RSS, including github projects. There are also RSS to email services available on the internet

