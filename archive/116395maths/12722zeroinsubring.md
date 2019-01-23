---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12722zeroinsubring.html
---

## Stream: [maths](index.html)
### Topic: [zero in subring](12722zeroinsubring.html)

---


{% raw %}
#### [ Patrick Massot (Sep 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20in%20subring/near/134172339):
I just added to the perfectoid project:
```lean
instance subring_has_zero (R : Type*) [comm_ring R] (S : set R) [HS : is_subring S] : has_zero S :=
⟨⟨0, is_add_submonoid.zero_mem S⟩⟩
```
It seems this used to be unnecessary. Any idea what happened? Trying `apply_instance` loops forever


{% endraw %}
