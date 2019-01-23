---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69065exactandnewgoals.html
---

## Stream: [general](index.html)
### Topic: [exact and new goals](69065exactandnewgoals.html)

---


{% raw %}
#### [ Reid Barton (Nov 26 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20and%20new%20goals/near/148372280):
How come `exact` makes `_`s appearing inside record constructors into new goals?
```lean
structure C := (x : ℕ)
example : C := by exact ⟨_⟩ -- error on _, "don't know how to synthesize placeholder"
example : C := by exact { x := _ } -- error on exact, "tactic failed, there are unsolved goals"
```


{% endraw %}
