---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46077ordinals.html
---

## [maths](index.html)
### [ordinals](46077ordinals.html)

#### [Reid Barton (Oct 04 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135205944):
If I am interested in sequences indexed by $$\{\,\alpha \mid \alpha \le \gamma\,\}$$ for varying ordinals $$\gamma$$, is it likely to be more convenient to just work with sequences indexed by arbitrary well-ordered sets?
The problem I found is that if you just write down `{ \a // \a \le \g }`, it lives in the wrong universe.

#### [Reid Barton (Oct 04 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206295):
I think the alternative is to use `quot.out` to turn an ordinal into a well-ordered set of that order type, where in math I'd just use the set of smaller ordinals.

#### [Reid Barton (Oct 04 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206562):
But if I use `quot.out` then I basically get an arbitrary well-ordered set anyways, so I might as well just work with an arbitrary well-ordered set from the start, I guess.

#### [Johannes Hölzl (Oct 04 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206599):
Oh yes, I would expect that its far easier assume that `γ` is a type with well-order. And use the elements of the type as indices.

#### [Kenny Lau (Oct 04 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206662):
I wrote some code a month ago

#### [Reid Barton (Oct 04 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206675):
And if I use the variable name `γ`, then everyone is happy :)

#### [Kenny Lau (Oct 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206697):
I uploaded them [here](https://github.com/kckennylau/Lean/blob/master/zfc_ordinals.lean).

#### [Reid Barton (Oct 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206710):
Oh interesting, will take a look

#### [Reid Barton (Oct 04 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206928):
I'm going to need to take colimits indexed by these partially ordered sets of ordinals less than $$\gamma$$--that's why I need the type to live in the correct universe

#### [Reid Barton (Oct 04 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135207023):
I think the ZFC stuff would also leave me in the wrong universe, though maybe I could prove once and for all that categories which admit small colimits also admit colimits by "categories in ZFC", or something like that...

#### [Mario Carneiro (Oct 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135209373):
You can measure the cofinality of any preorder, I think. Maybe it's easier to work without even using well orders

#### [Mario Carneiro (Oct 04 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135209437):
but yes, you almost certainly want to reason about ordered types rather than ordinals directly

