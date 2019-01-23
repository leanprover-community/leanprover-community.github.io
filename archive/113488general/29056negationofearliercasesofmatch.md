---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29056negationofearliercasesofmatch.html
---

## Stream: [general](index.html)
### Topic: [negation of earlier cases of match](29056negationofearliercasesofmatch.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618723):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618804):
How should I change the following code, so in the second case I know `a` is not `aa`?
```lean
inductive ind | aa | bb
open ind
example : ind → ind → ind → ind → nat 
| aa _  _ _ := 0
| a  aa _ _ := sorry
| _  _  _ _ := 0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618858):
you can change the title next time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618863):
type `bb` instead of `a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618872):
(it can't know inside a match what conditions are not yet matched)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618929):
How do I change the title?
what if I have 
```inductive ind | aa | bb | cc | dd```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618945):
maybe could you give us the whole context? I sense some [XY problem](https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem) going on here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618947):
sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618950):
```quote
How do I change the title?
```
Just edit the post. There will be a field to edit the title as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619007):
```quote
what if I have 
```inductive ind | aa | bb | cc | dd```
```
I think you'd need an `if _ then _ else _` and a `match` inside one of the branches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619020):
ite is hard to destruct. I don't recommend using it at all unless necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619022):
I'm sure his situation has other ways out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619041):
It would help if you derived `decidable_eq`:

```
@[derive decidable_eq]
inductive ind | aa | bb | cc | dd
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619119):
Kenny, the alternative would be to match on all branches.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619180):
one can't be so sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619276):
So if I have a **sparse** match on many variables, and in each case I want to use the fact that previous cases were not a match, I would be better off with if-then-else. Right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619323):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619332):
Thanks


{% endraw %}
