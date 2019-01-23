---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42057listnotation.html
---

## Stream: [general](index.html)
### Topic: [list notation](42057listnotation.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jason Dagit (Aug 23 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132651314):
I saw this snippet in the tutorial in the "inductive types" section:

```
notation `[` l:(foldr `,` (h t, cons h t) nil) `]` := l
```

I'm used to functional programming (but still very new to lean) so I think I understand what the above is morally doing, but I'm really struggling to parse it and make sense of it beyond a high-level understanding. Is there a reference for understanding `notation`? Or even a one-off explanation of this case.

Some example questions I have: How does `notation` bring things into scope? What does `:` mean in the above context? The backticks appear where I would expect an argument to `foldr` to go, so I guess `notation` supports mixing of syntactic elements and the expression you're defining?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132651483):
I don't believe such a reference exists. I should probably write one. 

The back ticks are only for delimiting tokens. `foldl` and `foldr` are special keywords in the `notation` syntax. You can look at it as: `v:(foldr _ (v v, e) e)`. I used `v` to denote bound variables and `e` as expressions. `_` stands for tokens that you use to separate expressions in the list.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132651948):
In `(v0 v1, e)`, you can see it as a lambda abstraction that you are forced to use (you don't have a choice to use different functions). In this case `v0` stands for the expression most recently parsed `v1` is an accumulator. `e` should be the next value of the accumulator and, eventually, the final value of that accumulator will be bound to `l` (in your example)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jason Dagit (Aug 23 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132652176):
Ah. Interesting. It didn't occur to me that it might be a special `foldr`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jason Dagit (Aug 23 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132652251):
Thanks for the explanation, I think that makes sense and answers all the questions I have right now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20notation/near/132652449):
Let me know if you need more. It might be useful if you find other information I could include in the documentation.


{% endraw %}
