---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28860seqandcoinduction.html
---

## [general](index.html)
### [seq and coinduction](28860seqandcoinduction.html)

#### [Kenny Lau (Mar 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124283402):
I see this comment in `data.seq.seq`:
```
/-
coinductive seq (α : Type u) : Type u
| nil : seq α
| cons : α → seq α → seq α
-/
 ```
Does this mean that `seq` is intended to be coinductive? Does that mean we can have co-fixed points?

#### [Mario Carneiro (Mar 27 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285523):
`seq` is intended to be coinductive, and it has co-fixed points. It has all the same properties you would expect of such a `coinductive` def, if it existed

#### [Mario Carneiro (Mar 27 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285526):
except possibly the computation rules

#### [Kenny Lau (Mar 27 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285604):
and what is the name of the fixed point function?

#### [Mario Carneiro (Mar 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285665):
`corec` I think, depending on what you mean by co-fixed point

#### [Kenny Lau (Mar 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285736):
I mean the sequence (1,2,1,2,...) being defined as X := 1,2,X

#### [Mario Carneiro (Mar 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285760):
We would need a better compiler to implement such a thing, but you can do it manually with a list storing the cycle

#### [Kenny Lau (Mar 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285815):
and then doing what?

#### [Mario Carneiro (Mar 27 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124287806):
Here's an implementation of `cycle` for `stream`: `cycle 1 [2, 3] = [1, 2, 3, 1, 2, 3, ...]`
```
def  cycle {α} (a : α) (l : list α) : stream α :=
stream.corec' (λ al, match al with
| (b, []) := (b, a, l)
| (b, c::l') := (b, c, l')
end) (a, l)
```

#### [Kenny Lau (Mar 27 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124287865):
no `cycle [1,2,3]`?

#### [Mario Carneiro (Mar 27 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288072):
You could, but then what is `cycle []`?

#### [Mario Carneiro (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288086):
this way that's syntactically impossible to give as input

#### [Kevin Buzzard (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288092):
if you did it in meta you wouldn't have to worry about this sort of thing, right?

#### [Kevin Buzzard (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288096):
and then you could just promise not to put [] in

#### [Kenny Lau (Mar 27 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288142):
I see

#### [Mario Carneiro (Mar 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288176):
You can promise not to put `[]` in in cycle as well: you could have an assumption `l != []` which would be no fun to work with, or you could have `A` be inhabited so that it returns `[default, default, ...]` in that case, or you could return a `seq` so that this produces an empty seq

