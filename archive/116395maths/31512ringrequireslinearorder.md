---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/31512ringrequireslinearorder.html
---

## [maths](index.html)
### [ring requires linear order](31512ringrequireslinearorder.html)

#### [Chris Hughes (Dec 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20requires%20linear%20order/near/150704740):
Is this a non-trivial upgrade? The support for division in ring only works on ordered fields.
```lean
import tactic.ring data.complex.basic

example (x : ℝ) : x / 3 + x / 2 = 5 * x / 6 := by ring --works

example (x : ℂ) : x / 3 + x / 2 = 5 * x / 6 := by ring --fails
```

#### [Kevin Buzzard (Dec 02 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20requires%20linear%20order/near/150717509):
I vaguely remember a conversation at one point where I asked Mario why something had to be ordered, and at the time it was because actually the thing had to be characteristic zero and there was no characteristic zero predicate at the time, but ordered implied it

