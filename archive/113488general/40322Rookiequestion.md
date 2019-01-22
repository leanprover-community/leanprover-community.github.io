---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40322Rookiequestion.html
---

## [general](index.html)
### [Rookie question](40322Rookiequestion.html)

#### [Frank Mobler (May 22 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie question/near/126907865):
I'm stumped proving `example {V : Type}{n : V} : n ∈ ({n} : set V)`. Please without tactics first. I want to see how to construct proof terms explicitly for types like this.

#### [Mario Carneiro (May 22 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie question/near/126908079):
`or.inl rfl` is a proof term for that

#### [Mario Carneiro (May 22 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie question/near/126908090):
because the goal is defeq to `n = n \/ false`:
```
example {V : Type} {n : V} : n ∈ ({n} : set V) :=
show n = n ∨ false, from or.inl rfl
```

#### [Frank Mobler (May 22 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie question/near/126908144):
Aha. This helps a lot. Light bulbs going on. Thanks.

