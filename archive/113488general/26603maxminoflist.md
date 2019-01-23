---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26603maxminoflist.html
---

## Stream: [general](index.html)
### Topic: [max/min of list](26603maxminoflist.html)

---


{% raw %}
#### [ Kenny Lau (May 01 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/125938032):
maybe you'll find this useful:
```lean
def list.max : α :=
list.foldr max (inhabited.default _) L

def list.min : α :=
list.foldr min (inhabited.default _) L

theorem list.le_max : ∀ x ∈ L, x ≤ L.max :=
list.rec_on L (λ _, false.elim) $ λ hd tl ih x hx,
or.cases_on hx
  (assume H : x = hd, H.symm ▸ le_max_left hd tl.max)
  (assume H : x ∈ tl, le_trans (ih x H) (le_max_right hd tl.max))

theorem list.min_le : ∀ x ∈ L, L.min ≤ x :=
list.rec_on L (λ _, false.elim) $ λ hd tl ih x hx,
or.cases_on hx
  (assume H : x = hd, H.symm ▸ min_le_left hd tl.min)
  (assume H : x ∈ tl, le_trans (min_le_right hd tl.min) (ih x H))
```

#### [ Johan Commelin (May 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/125938092):
I'll take look. First it's lunch time...

#### [ Chris Hughes (May 02 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/126002895):
@**Kenny Lau**  That doesn't take the max, it takes the max of the list and the default value. You won't be able to prove `L.max \in L` You should define it as default for nil, and then list.foldr max L.head otherwise.

#### [ Kenny Lau (May 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/126003001):
aha


{% endraw %}
