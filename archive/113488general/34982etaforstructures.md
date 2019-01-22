---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34982etaforstructures.html
---

## [general](index.html)
### [eta for structures](34982etaforstructures.html)

#### [Reid Barton (Aug 01 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734097):
Is definitional eta for structures something we are likely to get at some point?

#### [Gabriel Ebner (Aug 01 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734176):
I'd be surprised.

#### [Reid Barton (Aug 01 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734254):
In the absence of eta, another feature request would be "lazy matching" in lambdas and lets

#### [Reid Barton (Aug 01 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734272):
analogous to ~ patterns in Haskell

#### [Gabriel Ebner (Aug 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734477):
For everyone else, this means `λ \<x,y\>, x + y` gets desugared to `λ p, p.1 + p.2`.  I don't think it is planned, but you might be able to do the desugaring yourself.

#### [Reid Barton (Aug 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734478):
There are some definitions in data.equiv for example which I can't use conveniently, because they match on the input equivalence before producing a constructor.

#### [Reid Barton (Aug 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734545):
But rewriting them with the constructor outermost becomes quite ugly.

#### [Reid Barton (Aug 01 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734638):
(not at computer, and don't remember the specific names)

#### [Reid Barton (Aug 01 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734813):
Was imagining including a ~ in the syntax for lazy patterns, not changing the current semantics.

#### [Reid Barton (Aug 01 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130735589):
Though I wonder when you would ever want the "strict" version, figuratively speaking.

#### [Patrick Massot (Aug 01 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130742044):
```quote
For everyone else, this means `λ \<x,y\>, x + y` gets desugared to `λ p, p.1 + p.2`.  I don't think it is planned, but you might be able to do the desugaring yourself.
```
+1 I keep trying to type that and being disappointed.

#### [Mario Carneiro (Aug 04 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130879441):
Someone recently pointed out a mathlib definition that uses case analysis like this that was causing problems, but now I can't find it. Can anyone else find it?

#### [Chris Hughes (Aug 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130880063):
`+` and `*` in localization.

#### [Mario Carneiro (Aug 04 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130880926):
are you sure? I don't see that when I search in the chat

#### [Chris Hughes (Aug 04 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881181):
I definitely made a comment about it, but there's probably something else as well.

#### [Chris Hughes (Aug 04 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881189):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/match.20in.20defs

#### [Mario Carneiro (Aug 04 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881304):
ah, okay (I searched for "localization")

#### [Kenny Lau (Oct 10 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/135568699):
Should we replace those definitions with the better definitions?

