---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60832listprod.html
---

## Stream: [general](index.html)
### Topic: [list.prod](60832listprod.html)

---


{% raw %}
#### [ Kenny Lau (Jun 20 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128334739):
Was there any point in time where `list.prod [t]` was definitionally equivalent to `t * 1`?

#### [ Kenny Lau (Jun 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335761):
and was there any point in time where `list.prod (x :: L) = x * list.prod L` was `rfl`?

#### [ Simon Hudon (Jun 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335831):
I think not. The foldl implementation is faster and Leo has been pretty aggressive with optimization from the start

#### [ Kenny Lau (Jun 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335838):
interesting. my category repo seems to answer yes to my questions

#### [ Kenny Lau (Jun 20 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335887):
i.e. a code worked some time ago, and now it doesn't

#### [ Simon Hudon (Jun 20 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335915):
You can have an even clearer answer and use `git blame` on the definition of `list.product`

#### [ Kenny Lau (Jun 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335924):
how do I do that?

#### [ Simon Hudon (Jun 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335941):
Do you use emacs and magit?

#### [ Kenny Lau (Jun 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335996):
eh... not really

#### [ Simon Hudon (Jun 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128336002):
You can get the instructions on using `git blame` by typing `man git-blame` in a terminal

#### [ Johan Commelin (Jun 20 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128347985):
Alternatively, you go to GitHub, and lookup the relevant line: https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054
Then you click on the `...` to the left of that line, and choose `git blame`. That gives you https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054

#### [ Johan Commelin (Jun 20 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128348026):
But I don't see an easy option to walk through the history of that line. On the command line you *can* do that, with `git log` and some options. See also https://flummox-engineering.blogspot.com/2016/05/view-specific-lines-of-source-code-in-git-history.html

#### [ Johannes Hölzl (Jun 20 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362377):
I traced it back, it was always `foldl`. I ported the definition from Lean2's library. I think we should change it to `foldr` then we get the expected equalities.

#### [ Simon Hudon (Jun 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362751):
Is there a way to use `foldr` as the definition but run `foldl` implementation in the VM?

#### [ Gabriel Ebner (Jun 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362770):
If you want to patch Lean, then yes.

#### [ Simon Hudon (Jun 20 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362903):
That sounds less trivial than the "yes" suggests :stuck_out_tongue_closed_eyes:

#### [ Reid Barton (Jun 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128364747):
`{-# RULES #-}`with a proof obligation would be neat...

#### [ Simon Hudon (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128364931):
you could probably write it `@[rule]` before a lemma

#### [ Chris Hughes (Jun 20 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128368155):
```quote
and was there any point in time where `list.prod (x :: L) = x * list.prod L` was `rfl`?
```
I don't think it was even equal to that with non commutative multiplication, `list.prod (x :: L) = list.prod L * x`at the moment.


{% endraw %}
