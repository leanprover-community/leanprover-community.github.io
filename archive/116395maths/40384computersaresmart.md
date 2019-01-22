---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40384computersaresmart.html
---

## [maths](index.html)
### [computers are smart??](40384computersaresmart.html)

#### [Reid Barton (Jun 04 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127549305):
So I was going along constructing coequalizers in Top, like you do. A coequalizer is a kind of quotient, so I needed to prove that if $$Z$$ is the quotient of $$Y$$ by a relation, then the quotient map $$Y \to Z$$ is continuous, so that it's a morphism in Top.
I was all set to add the lemma for that to my `continuity` tactic, when I noticed the tactic had already succeeded before I did so! What happened?

#### [Reid Barton (Jun 04 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127549340):
It turns out that continuity of the quotient map $$Y \to Z$$ is *definitionally equivalent* to continuity of the identity map on $$Z$$, because a set is defined to be open in $$Z$$ if and only if its preimage is open in $$Y$$. So the tactic found that it could just apply `continuous_id`!

#### [Johan Commelin (Jun 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127554973):
Wunderbar!

#### [Johan Commelin (Jun 05 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127587246):
In fact, Reid, how did you define the topology on $$Z$$? Because there is a bunch of stuff on coinduced topologies in mathlib, and that would also give you continuity of the quotient map by definition.

#### [Reid Barton (Jun 05 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127595731):
I did use the coinduced topology (see PR at https://github.com/leanprover/mathlib/pull/155/commits/b60f3687e8692f118c385f958d48d31388593298#diff-1c17754b46d709d0b8e22318f94035cdR903)

#### [Johan Commelin (Jun 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers are smart??/near/127595747):
I see. So your `continuity` tactic is not in that PR?

