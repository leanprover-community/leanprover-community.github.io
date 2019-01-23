---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52473monotonicitylemma.html
---

## Stream: [general](index.html)
### Topic: [monotonicity lemma](52473monotonicitylemma.html)

---


{% raw %}
#### [ Rob Lewis (Sep 28 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotonicity%20lemma/near/134821924):
I feel like this lemma (or similar) must exist somewhere already, but I'm coming up empty -- anyone recognize this?
```lean
example {α} [partial_order α] (f : ℕ → α) (h : ∀ n, f (n+1) ≤ f n) : ∀ m n, m ≤ n → f n ≤ f m
```


{% endraw %}
