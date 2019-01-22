---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92424findgoal.html
---

## [general](index.html)
### [#find goal](92424findgoal.html)

#### [Johan Commelin (May 01 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#find goal/near/125929630):
I occasionally find myself in the situation where I would like to know if there is a theorem that I can apply to the current goal (in tactic mode). It would be nice if I could run a tactic `find_goal` that does not change the proof state, but just prints messages of the theorems that I could apply. Is this reasonable?

#### [Reid Barton (May 01 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#find goal/near/125929697):
Interesting idea. But I bet there would be too many theorems that would always apply, like `eq.symm` or `iff.symm`. How to reject the uninteresting ones?

#### [Mario Carneiro (May 01 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#find goal/near/125929901):
An idea I have contemplated as a crude relevance filter is measuring the degree to which the target matches the theorem (i.e. how many exact symbol matches before it starts instantiating metavariables). This could be combined with a (harsh?) penalty for the number of new metavariables not in the goal

#### [Mario Carneiro (May 01 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#find goal/near/125929940):
But the only obvious way I see to implement this is literally to `try{apply T}` for all T in the environment, so it will be very slow

#### [Kenny Lau (May 01 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#find goal/near/125931438):
@**Johan Commelin**
```lean
import tactic.find

open nat

#find _ + _ = _ + _
```

