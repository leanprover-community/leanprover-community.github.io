---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21663behaviourofsimpachanged.html
---

## Stream: [general](index.html)
### Topic: [behaviour of simpa changed](21663behaviourofsimpachanged.html)

---

#### [Chris Hughes (Sep 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/behaviour%20of%20simpa%20changed/near/133365192):
A few of my proofs have broken since the recent changes to `simpa`. For example this one.
```lean
lemma zero_pow {α : Type*} [semiring α] {n : ℕ} (hn : 0 < n) : (0 : α) ^ n = 0 :=
by cases n; simpa [_root_.pow_succ, lt_irrefl] using hn
```
It fails if it solves the goal without using `hn`

#### [Mario Carneiro (Sep 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/behaviour%20of%20simpa%20changed/near/133392023):
You should just use `by cases n; simp [_root_.pow_succ, lt_irrefl, hn]` here. `simpa` is not supposed to be a replacement for `simp`

