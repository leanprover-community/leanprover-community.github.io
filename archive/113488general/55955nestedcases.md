---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55955nestedcases.html
---

## [general](index.html)
### [nested cases](55955nestedcases.html)

#### [Reid Barton (Feb 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003168):
Is there a more convenient way to unpack the components of a conclusion of the form `∃ x y, p x ∧ q y ∧ r x y` in a tactics block than using multiple `cases` tactics?

#### [Andrew Ashworth (Feb 26 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003198):
you want mathlib's `rcases` or core's `cases_matching`

#### [Reid Barton (Feb 26 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003381):
oh yeah, `rcases` is what I want. Much better!

#### [Sean Leather (Feb 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123041049):
@**Reid Barton** Also, in case you didn't know, the anonymous constructor notation `⟨..., ...⟩` is right-associative for nested constructors. So, for example, you can do `rcases h with ⟨x, y, px, qy, rxy⟩` with your type. I learned this recently, and it's quite convenient.

