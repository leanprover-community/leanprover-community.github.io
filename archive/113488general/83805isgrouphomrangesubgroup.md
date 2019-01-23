---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83805isgrouphomrangesubgroup.html
---

## Stream: [general](index.html)
### Topic: [is_group_hom.range_subgroup](83805isgrouphomrangesubgroup.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.range_subgroup/near/125304068):
```lean
instance is_group_hom.range_subgroup : is_subgroup (set.range f) :=
@set.image_univ _ _ f ▸ is_group_hom.image_subgroup f set.univ
```
Could you add this to mathlib? @**Mario Carneiro**


{% endraw %}
