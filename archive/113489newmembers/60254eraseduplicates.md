---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60254eraseduplicates.html
---

## Stream: [new members](index.html)
### Topic: [erase_duplicates](60254eraseduplicates.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 24 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267520):
Does mathlib have a function which erases list duplicates?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 24 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267854):
Maybe `list.pw_filter`?
```lean
import data.list.basic

#eval list.pw_filter (≠) [1,2,3,5,5,5,5,2,1,4,1] -- [3, 5, 2, 4, 1]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 24 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267993):
Oh, `list.erase_dup` is defined to be `pw_filter (≠)`. But its docstring is wrong:
```lean
/- `erase_dup l` removes duplicates from `l` (taking only the first occurrence).

     erase_dup [1, 2, 2, 0, 1] = [1, 2, 0] -/

#eval list.erase_dup [1, 2, 2, 0, 1] -- [2, 0, 1]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268163):
It removed the first "1" and the first "2"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268210):
Should it say "...leaving only the last occurrence"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268668):
yeah, obviously I meant first from the right end ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269503):
I'm putting together a PR that fixes this and also improves the other docstrings in `data.list.basic`. I found that the example given for `list.sigma` is also wrong:
```lean
/- `sigma l₁ l₂` is the list of dependent pairs `(a, b)` where `a ∈ l₁` and `b ∈ l₂ a`.

     sigma [1, 2] (λ_, [5, 6]) = [(1, 5), (1, 6), (2, 5), (2, 6)] -/

#eval list.sigma [1, 2] (λ_, [5, 6]) 
/- don't know how to synthesize placeholder
context:
⊢ ℕ → Type ?
-/
```
The following works, but I don't think this would make a good example:
```lean
#eval @list.sigma _ (λ_, ℕ) [1, 2] (λ_, [5,6]) --[(1, 5), (1, 6), (2, 5), (2, 6)]
```
Any suggestions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269615):
hm, that's weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269616):
does a type ascription on `[5,6]` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269622):
or even just on `5`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269665):
Ah, yes, that works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148271040):
https://github.com/leanprover/mathlib/pull/493

