---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52941fromfinsettoset.html
---

## Stream: [general](index.html)
### Topic: [from finset to set](52941fromfinsettoset.html)

---

#### [Johan Commelin (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256617):
I can't find a way to go from `finset` to `set` in the `finset.lean` file. How do I do this?

#### [Kenny Lau (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256619):
`{x | x \in s}`

#### [Johan Commelin (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256622):
Ok... there is no `lift_to_set S` thing or such?

#### [Kenny Lau (May 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256662):
not that I am aware of

#### [Johan Commelin (May 08 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256812):
Ok, then I'll use curly braces {-;

#### [Chris Hughes (May 08 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126258082):
There's a `has_lift` instance for finset to set in `data.set.finite`

