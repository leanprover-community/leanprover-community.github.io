---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42165limitofaseriesofsets.html
---

## Stream: [general](index.html)
### Topic: [limit of a series of sets](42165limitofaseriesofsets.html)

---


{% raw %}
#### [ Simon Hudon (Apr 06 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124704503):
I have an infinite series of sets that each include their successor and such that each is non-empty. How do I prove that the intersection of all sets is also non-empty?

```lean
variables
   (s : stream (set α))
   (h₀ : ∀ i, s i ≠ ∅)
   (h₁ : ∀ i, s (i+1) ⊆ s i)
example : (⋂ i, s i) ≠ ∅ := ...
```

#### [ Mario Carneiro (Apr 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705712):
it's false? For example take `s n := {m : nat // n <= m}`

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705718):
right, it’s false

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705719):
i was thinking for 5 minutes whether it is true or false

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705721):
take (0,1/n)

#### [ Simon Hudon (Apr 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124716057):
Damn it! You guys are right! I was hoping to generalize a theorem. I guess I'll have to keep thinking about restrictions

#### [ Chris Hughes (Apr 06 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124719698):
(deleted)


{% endraw %}
