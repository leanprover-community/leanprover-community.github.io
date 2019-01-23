---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03125Leanlibraryfixes.html
---

## Stream: [general](index.html)
### Topic: [Lean library fixes](03125Leanlibraryfixes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 04 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150883678):
The lean3 repo indicates that only major bugfixes will be accepted.  Are there any official or semi-official repos for more minor fixes that could be merged, but aren't?  e.g. make a `monad_except` instance for `except`, add missing `decidable` instances for predicates?
I currently just add them as needed to my code, but figure they could be worth sharing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 04 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150884566):
If you're talking about additions, not changes, then definitely. https://github.com/leanprover/mathlib/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 04 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150884621):
Most of the discussions here assume you're using mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 04 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150884644):
Despite the name, it has more than just math.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 04 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150886027):
Ok, if I have enough I'll make a PR to mathlib.
I was thinking it may be useful to have a smaller set of additions that make the standard library more consistent, rather than mathlib which has a mix of useful additions and definitions to fill out the standard library.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 04 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150886477):
mathlib is admittedly a big monolith, but it's not clear what advantage splitting off parts of it would have, and it would certainly add a bunch of administrative overhead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 05 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150886862):
I'm not proposing to partition mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150890159):
I think what you are proposing usually falls under the header of "forking lean", which was a bad idea when lean was under active development. Now that lean3 is effectively EOL, it seems more reasonable but I think it is still a major decision that we wouldn't take lightly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150890244):
mathlib is currently right at the edge of what you can do to improve lean solely with an add on library and zero modifications to core lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 05 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892454):
I was looking for a more conservative staging library than mathlib for library improvements/generalizations that could be ported to Lean 4 once it is ready for library improvements.  With Lean 3 EOL, and Lean 4 in active development, there isn't a good way to share minor improvements to Lean 3 without distracting Lean 4 development.
The Lean 4 improvements are essential for the project I'm working on, so I don't want to distract from that.  I've only used parts of mathlib, and it's great, but my impression is that's the bulk of it won't be integrated into the Lean standard library.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892782):
I think that mathlib would be a good staging area for things you want to eventually move to lean 4, however it ends up looking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892805):
right now we don't know enough of the basics to really plan a port in any more than very general terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892838):
but a lot of mathlib is tactics and basic programming that "morally" should have been in the core library, and isn't because of human reasons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892898):
while at the same time lean 4 is planning on outsourcing much of what is now core into the user space / lean 4 mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150892958):
so all in all I don't know what will end up where, but mathlib is actively being developed and used so it's a good place to test out changes in the meantime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 05 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/150893056):
Right now mathlib *is* the lean standard library. Lean core lacks a lot of basic stuff that one would expect in a standard library, much of it deliberately so. Mathlib was built to fill that gap

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/151404787):
To follow up on this, I'm currently putting our generic additions here https://github.com/GaloisInc/reopt-vcg/tree/master/lean/deps/galois_stdlib/src/galois.
They aren't particularly substantial, but are Apache 2 licensed, so feel free to pull to mathlib if you'd like.   If they get more substantial, then maybe it makes sense for me to add a PR to mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 11 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/151433862):
Nice, `reopt-vcg` is Lean in the wild stuff!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 11 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20library%20fixes/near/151468629):
Yeah, I'm really interested in being able to use Lean as another programming language for developing verification/satisfiability checking tools, and then being able to prove soundness.


{% endraw %}
