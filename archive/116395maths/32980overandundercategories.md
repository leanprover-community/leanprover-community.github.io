---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/32980overandundercategories.html
---

## Stream: [maths](index.html)
### Topic: [over and under categories](32980overandundercategories.html)

---


{% raw %}
#### [ Johan Commelin (Dec 17 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/151910153):
Over and under categories show up all over the place (notably covers and structure maps can use over categories, and algebras can use under categories). I've written the definitions and a bunch of simp lemmas in https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L195
Now I would like to prove some facts about limits/colimits in these categories. What would be the right file in mathlib to put these?

#### [ Reid Barton (Dec 17 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/151911457):
I guess the current "convention" would be a new file `category_theory.limits.<something>`

#### [ Johan Commelin (Dec 17 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152007049):
Ok, I'll do that. So that would probably be `category_theory.limits.over`.

#### [ Chris Hughes (Dec 17 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152011380):
(deleted)

#### [ Johan Commelin (Dec 18 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152132709):
It seems I'm pushing the limits of the category library again.
I'm trying to prove an equivalence of two categories: https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L238
This is completely math-trivial: If I take `Y` in the category `over X`, then `over Y` is equivalent to `over (Y.left)`. There is almost no content... just composing some arrows. Still I'm running into deterministic timeouts and such. Is this just stuff that should wait?

#### [ Reid Barton (Dec 18 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152134163):
I think you should write out the components of the natural isomorphisms anyways

#### [ Patrick Massot (Dec 18 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152141717):
Does it mean that Scott's magic auto-param are failing here?

#### [ Johan Commelin (Dec 19 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152158162):
Partly, yes. Maybe that would be fixed once `back` and `rewrite_search` are part of mathlib. But another problem is that the code is just terribly slow. At some point I close a goal by `exact foobar` and this takes several seconds. I guess that is just exhibiting that we are stacking lots of stuff on top of each other. (In particular the `pp.all` output is usually not much fun to look at.)


{% endraw %}
