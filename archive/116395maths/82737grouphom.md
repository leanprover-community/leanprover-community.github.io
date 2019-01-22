---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82737grouphom.html
---

## [maths](index.html)
### [group_hom](82737grouphom.html)

#### [Chris Hughes (Dec 12 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151505639):
Can we define `is_group_hom` to be `is_monoid_hom` and make it reducible? It would avoid cycles.

#### [Johan Commelin (Dec 12 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510233):
I would like this too. Especially if we could fill in the condition `f 1 = 1` using some default argument or auto_param. (Because for groups, as opposed to monoid, you can derive this condition from the multiplicativity.)

#### [Johan Commelin (Dec 12 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510242):
Whether it should be reducible, I don't know.

#### [Chris Hughes (Dec 12 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510669):
If it's reducible then every  group hom is automatically a monoid hom and vice versa

