---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89414withinfty.html
---

## Stream: [general](index.html)
### Topic: [with_infty](89414withinfty.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383943):
I am looking at Sebastien's PR for emetric spaces. And I'm wondering, we have `with_top`, `with_bot` and `with_zero`. Would it make sense to have `with_infty`, or is it not worth it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383952):
that's `with_top`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383993):
I know. But why do we have `with_zero`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383994):
It is just `with_bot`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383999):
I think there are some algebraic definitions on `with_top`, and they correspond to treating it like infinity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384003):
`with_zero` and `with_bot` are not the same on algebra stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384004):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384012):
So if someone wants to use `∞` notation, they should just introduce it locally?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384016):
Because that might be nice...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384080):
yes, `∞` is not a notation associated to any typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384086):
indeed I was thinking of eliminating it from `ennreal` in favor of top everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384152):
Hmmm, I would vote for keeping the notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384210):
I think I hit a dependency problem anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384216):
but it's a local notation, use what you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135416708):
Do you ever add both a bottom and a top? In what order do you add them? Or do you build it as a `sum bool a`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135555509):
fyi: `∞` is only a local notation for top. https://github.com/leanprover/mathlib/blob/master/data/real/ennreal.lean#L19

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135555544):
I don't think we currently have a case where we add a top and a bot. But we add top to structures which already have a bot, like ennreal, or enat.


{% endraw %}
