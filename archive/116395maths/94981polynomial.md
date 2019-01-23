---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94981polynomial.html
---

## Stream: [maths](index.html)
### Topic: [polynomial](94981polynomial.html)

---

#### [Patrick Massot (Jul 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921310):
What's happening with polynomials? I see ce990c59d authored by Chris and merged by Johannes but PR171 is still open and active

#### [Mario Carneiro (Jul 19 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921367):
I think Johannes is currently working on merging the Mason Stothers work with Chris's

#### [Patrick Massot (Jul 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921787):
That's really nice

#### [Patrick Massot (Jul 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921893):
It's really important part of elementary maths that was missing.

#### [Patrick Massot (Jul 19 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921961):
It makes me think of my normed space work again. Do you think I should PR https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean (after removing the type class inference nightmare at the end). Would it help in getting more motivation to fix the issues?

#### [Mario Carneiro (Jul 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129922019):
I think that's a good idea. I know Johannes has his own plans for this stuff, but I think a mathlib PR is the best place to coordinate

#### [Patrick Massot (Jul 19 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129922166):
Ok, I'll try to do that today

#### [Patrick Massot (Jul 19 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129939330):
https://github.com/leanprover/mathlib/pull/208

#### [Nicholas Scheel (Jul 19 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941187):
@**Patrick Massot** I’m curious if you could just define `norm` as `dist 0`? seems like you spend a lot of time converting between the two ...

#### [Patrick Massot (Jul 19 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941308):
I don't think you would get the expected properties

#### [Nicholas Scheel (Jul 19 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941390):
how so? you have `lemma norm_dist { g : G} : dist g 0 = ∥g∥` already ... (plus commutativity gets you my definition)

#### [Patrick Massot (Jul 19 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941440):
I mean: there are distances on groups such that `dist 0` is not a norm

#### [Patrick Massot (Jul 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941492):
Think of the trivial distance for instance

#### [Patrick Massot (Jul 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941508):
maybe this is not a good example actually

#### [Nicholas Scheel (Jul 19 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941536):
I think you need `dist x y = dist 0 (x - y)`, as the equivalent of the property you already have, but I think `norm` adds nothing to the definition – it must be equal to `dist 0`

#### [Patrick Massot (Jul 19 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941552):
yes, somthing like this is needed

