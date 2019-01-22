---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10902lagrangetheorem.html
---

## [new members](index.html)
### [lagrange theorem](10902lagrangetheorem.html)

#### [Leonid Kimelfeld (Jan 22 2019 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/lagrange theorem/near/156586958):
Dear all, could you help me. Where is formalization of Lagrange theorem (group theory) in mathlib?

#### [Mario Carneiro (Jan 22 2019 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/lagrange theorem/near/156587176):
`card_subgroup_dvd_card`, I guess? https://github.com/leanprover/mathlib/blob/master/src/group_theory/order_of_element.lean#L56-L58

#### [Mario Carneiro (Jan 22 2019 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/lagrange theorem/near/156587186):
there are a few ways you could state the theorem

#### [Leonid Kimelfeld (Jan 22 2019 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/lagrange theorem/near/156587441):
```quote
`card_subgroup_dvd_card`, I guess? https://github.com/leanprover/mathlib/blob/master/src/group_theory/order_of_element.lean#L56-L58
```
 Yes, thank you!

