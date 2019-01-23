---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45148erwinconv.html
---

## Stream: [general](index.html)
### Topic: [erw in conv](45148erwinconv.html)

---

#### [Reid Barton (Nov 13 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erw%20in%20conv/near/147565415):
Is it intentional that you have to import `tactic.converter.interactive` to get the new `conv` goodies?

#### [Reid Barton (Nov 13 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erw%20in%20conv/near/147565958):
It's not mentioned in the docs

#### [Keeley Hoek (Nov 13 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erw%20in%20conv/near/147566154):
That's true, it should be
I just put them where the already existing extras were
But you'll always have to import something

