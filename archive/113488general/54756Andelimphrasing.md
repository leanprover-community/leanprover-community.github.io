---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54756Andelimphrasing.html
---

## Stream: [general](index.html)
### Topic: [And-elim phrasing](54756Andelimphrasing.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Stevens (May 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218529):
Noob question here, trying to improve my mental model of Lean.
I have an inhabitant h of "and p q" in scope, and I want to create named inhabitants hp, hq of p and q respectively. I'm in tactic mode. One way to do this is "have hp : p, from h.left"; is that the one true way? Are there any other ways (that aren't just interchanging "and.left h" or "and.elim_left")?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218535):
`cases h with hp hq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218536):
cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218537):
almost fast enough!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218582):
It's unfair, I was staring at an infinite class resolution trace when the notification popped up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Stevens (May 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218585):
Thanks - it's nontrivial to search for this kind of thing in the docs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218591):
https://leanprover.github.io/theorem_proving_in_lean/tactics.html#more-tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218593):
Not trivial to find, I agree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218602):
But very important reading

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127218605):
Yeah, I recommend a few rounds of reading that chapter and then playing around with stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/And-elim%20phrasing/near/127222394):
We're trying to write docs, they appear in random places, but theorem proving in lean is where most of us started

