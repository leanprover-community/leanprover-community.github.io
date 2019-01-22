---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/18975notationforgroupaction.html
---

## [kbb](index.html)
### [notation for group action](18975notationforgroupaction.html)

#### [Johan Commelin (Sep 14 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932189):
I think we should just group actions an instance of `has_smul`. What do others think?

#### [Mario Carneiro (Sep 14 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932247):
it *probably* won't cause problems

#### [Johan Commelin (Sep 14 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932291):
And then we get `group_module G A` with an instance to `module (group_ring G) A` and we will have to versions of `has_smul` :scream:

#### [Johan Commelin (Sep 14 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133933127):
Ooo, I guess it just means we will always have to explicitly write the coercion `G → (group_ring G)` to distinguish which action we mean.

