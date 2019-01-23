---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70493Unexpectedoccurenceofrecursivefuntion.html
---

## Stream: [general](index.html)
### Topic: [Unexpected occurence of recursive funtion](70493Unexpectedoccurenceofrecursivefuntion.html)

---

#### [Minchao Wu (Jul 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129302165):
Hi friends, I'm wondering what's the right way to let Lean accept recursive calls with list.map?
For example:

```lean
def bar : ℕ → ℕ
| 0     := 0
| (n+1) := list.length $ list.map bar [n, n, n]
```

Lean is not happy with the above one.

#### [Chris Hughes (Jul 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129306754):
This works for this example. In general I think you pretty cannot do recursive calls with `list.map` and you have to find some different way of defining the function.
```lean
def bar : ℕ → ℕ
| 0     := 0
| (n+1) := list.length $ [bar n, bar n, bar n]
```

#### [Minchao Wu (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307191):
Yes, your solution definitely works. But I am curious about why it cannot be done with maps.

#### [Chris Hughes (Jul 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307283):
It might be possible, but it's not easy. The equation compiler knows your function is well-founded if the recursive call applies it to a nat less than `n + 1`. Here your function `bar` is not actually applied to anything, so it cannot prove it is well founded.

#### [Minchao Wu (Jul 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307398):
That's true. Usually if Lean cannot prove well-foundedness then it throws a different error asking me for a proof, but for this one it just gives up. I guess the reason is exactly that `bar` is not applied to anything as you said.

#### [Chris Hughes (Jul 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307555):
I found a way 
```lean
import data.list.basic
def bar : ℕ → ℕ
| 0     := 0
| (n+1) := list.length 
  (list.pmap (λ m (hm : m < n + 1), bar m) [n, n, n] 
  (by simp [nat.lt_succ_self]))
```

#### [Minchao Wu (Jul 08 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307790):
Great, this looks like a general solution. Thanks!

