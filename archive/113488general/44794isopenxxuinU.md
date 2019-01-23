---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44794isopenxxuinU.html
---

## Stream: [general](index.html)
### Topic: [is_open {x | x + u \in U}](44794isopenxxuinU.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133679397):
Given a topological additive monoid, I expected theorems that say that you can translate opens along addition by a given element. But I could not find those... is this in mathlib, or do I need to roll my own?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133679963):
continuous_add or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680126):
Are you sure Kenny? That seems to prove only that the pre-image of an open under the map lam x, x+c (c constant) is open. But you can't cancel in a monoid and Johan seems to want to show that the image, not the pre-image, of an open is open. @**Johan Commelin** are you sure that what you want to prove is true? What exactly do you want to prove?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680147):
and what exactly are you thinking about topological monoids for??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680161):
Hmmm, I probably over-generalised.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680168):
Let's assume it's a group.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680174):
then what Kenny said

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680177):
Huh, the title looks like a preimage

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680182):
That's good enough for applications, since I'm a mathematician.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680237):
oh yes, Kenny's comment answers the question in the title but not in the body.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680244):
Ok, somehow `continuous_add` didn't work straightaway. I'll try harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680273):
I'm assuming continuous_add is continuity of addition, so now you need to compose with the map from G to G x G sending g to g,c

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680277):
which is continuous for any topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680978):
```quote
Given a topological additive monoid, I expected theorems that say that you can translate opens along addition by a given element. But I could not find those... is this in mathlib, or do I need to roll my own?
```
I think this is not true. Consider the topological multiplicative monoid $$\Bbb R$$ and translation by 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681061):
bingo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 10 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681162):
Hmn, I could PR the `continuity` tactic now that tidy is in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681868):
Related: https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681885):
Reid: yes, please!


{% endraw %}
