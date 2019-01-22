---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/73085507functorialityofcocones.html
---

## [PR reviews](index.html)
### [#507 functoriality of (co)cones](73085507functorialityofcocones.html)

#### [Johan Commelin (Dec 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#507 functoriality of (co)cones/near/150766258):
I just created PR #507. This is something that I wanted to have for my work with presheaves. I don't know if I should expand things. Maybe it's better to keep things small. Feedback appreciated!

#### [Reid Barton (Dec 07 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#507 functoriality of (co)cones/near/151128674):
I really like these statements `lim_yoneda` and `colim_coyoneda` because they say at once everything there is to know about `lim` and `colim`. Of course we will still need to relate them to `limit` and `colimit`, for those cases in which one is not so fortunate to have all limits or colimits...

#### [Reid Barton (Dec 07 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#507 functoriality of (co)cones/near/151128797):
The "functoriality" stuff added here is really pointing out the asymmetry between `cones` and `cocones`. Can we make them more uniform?

#### [Reid Barton (Dec 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#507 functoriality of (co)cones/near/151128907):
I also wonder whether we should just define `cones` and `cocones` as functors in the first place

