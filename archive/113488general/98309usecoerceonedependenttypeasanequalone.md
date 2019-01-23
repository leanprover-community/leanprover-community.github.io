---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98309usecoerceonedependenttypeasanequalone.html
---

## Stream: [general](index.html)
### Topic: [use/coerce one dependent type as an equal one?](98309usecoerceonedependenttypeasanequalone.html)

---

#### [Andrew Tindall (Sep 23 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479228):
I am trying to apply a function to a vector, and get the error message 
```
type mismatch at application
  f (vector.take j v)
term
  vector.take j v
has type
  vector (S.A) (min j (max j k))
but is expected to have type
  vector (S.A) j
```
`j` and `k` are `nat`s. I know that `j = min j (max j k)`, but I don't know how to use that equivalence to coerce `v` from one type to another. Should I just make a specific instance of `has_coe` and then use it to cast `v`?

#### [Keeley Hoek (Sep 23 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479329):
If it was me I would explicitly turn `vector.take j v` into something of type `vector (S.A) j` before applying the coercion

#### [Reid Barton (Sep 23 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479736):
Isn't `j = min j (max j k)` always true? Where is `vector.take` defined?

#### [Andrew Tindall (Sep 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479910):
Yes, it's always true. `vector.take`is in `data.vector`.

#### [Kenny Lau (Sep 23 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479962):
maybe you should change the type of `f` first

#### [Reid Barton (Sep 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479968):
Oh, in the core library! Right

#### [Kenny Lau (Sep 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479969):
also, MWE

#### [Reid Barton (Sep 23 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134480135):
If this is in a programming context, I would probably use the `convert` tactic or some `rw` and prove `j = min j (max j k)`.
If this is in a theorem-proving context, where I need to prove some fact about the result of this expression, I would just define my own `take'` with a more useful type like
```lean
def vec.take' (i n : ℕ) (h : i <= n) : vector α n → vector α i
```
(the implementation can probably even be the same)

