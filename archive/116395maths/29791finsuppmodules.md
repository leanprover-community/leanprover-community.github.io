---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29791finsuppmodules.html
---

## Stream: [maths](index.html)
### Topic: [finsupp modules](29791finsuppmodules.html)

---

#### [Johan Commelin (Nov 22 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finsupp%20modules/near/148149210):
I think the module part of finsupp is broken. For example in
```lean
lemma sum_smul_index [ring β] [add_comm_monoid γ] {g : α →₀ β} {b : β} {h : α → β → γ}
  (h0 : ∀i, h i 0 = 0) : (b • g).sum h = g.sum (λi a, h i (b * a)) :=
finsupp.sum_map_range_index h0
```
the `g` takes values in the ring `\beta`. But what is realy interesting is if `g` takes values in a module over the ring.

