---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90420sortvstype.html
---

## [general](index.html)
### [sort vs type](90420sortvstype.html)

#### [Johan Commelin (Jul 03 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129031745):
I realise that I don't actually quite understand what the distinction is between sort and type. Somehow I treat them as interchangeable, but of course that is not a very solid strategy. So, what exactly is a sort, and when should I use it?

#### [Reid Barton (Jul 03 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129032001):
Basically, `Sort*` = `Prop` union `Type*`. `Sort 0 = Prop`, and `Sort (u+1) = Type u`.

#### [Johan Commelin (Jul 03 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129032574):
Hmm, so that kind explains my thinking that I could equate `Sort*` and `Type*`. But it doesn't explain why we have these two notions that are almost the same. Lean seems to prefer to have only 1 concept when 1 suffices...

#### [Sean Leather (Jul 04 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129068181):
@**Johan Commelin** Here's some of the [design discussion](https://github.com/leanprover/lean/issues/1341).

#### [Johan Commelin (Jul 04 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129068681):
Thanks!

