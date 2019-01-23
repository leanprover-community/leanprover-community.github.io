---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82120constructivisingusingtruncsubtypeiswellorder.html
---

## Stream: [general](index.html)
### Topic: [constructivising using `trunc (subtype (is_well_order _))`](82120constructivisingusingtruncsubtypeiswellorder.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204645):
How many things can we constructivise with a `trunc (subtype (is_well_order _))` hypothesis? I'm sure we can make a truncated basis this way... Maybe if it can constructivise a lot of stuff, I would imagine making it as wide-used as `decidable_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204651):
well this surely implies `decidable_eq` to start with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204672):
(on second thought maybe we need a decidable prop to do so, but we can fix this by requiring our function to have codomain `bool` instead?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204807):
and how about making `trunc (equiv _ _)` an instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204852):
congratulations then, you got yourself into an instance loop with a fintype having decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148208342):
I think `is_well_order` is not as useful constructively as it is in classical maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148208346):
in particular `is_well_order.min` is not constructive


{% endraw %}
