---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39790Noobmetaquestion.html
---

## Stream: [general](index.html)
### Topic: [Noob meta question](39790Noobmetaquestion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727546):
What's the "correct" way to efficiently implement finitely supported functions in Lean meta. Currently I'm using `list (α × β)` as `α →₀ β`, but this seems totally wrong. By finitely supported, I mean functions for which I only care about the result for finitely many `α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727560):
`data.rbmap`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727620):
that's the best way I know of

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727662):
https://github.com/spl/lean-finmap ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133728841):
`rbmap` looks about right. Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133730984):
Is there a `decidable` instance for `mem` in `rbmap` anywhere. This seems like something so fundamental that I feel like I must be doing something wrong by trying to use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 11 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133731062):
I don't think the `rbmap` theorem collection is very extensive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133734773):
I see there's `contains`, which I assume is the same thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133735259):
There doesn't seem to be an `erase` either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 11 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133737802):
Is `rbtree α` isomorphic to `finset α`, and is `rbmap α β` isomorphic to `Σ s : finset α, Π x, x ∈ s → β`


{% endraw %}
