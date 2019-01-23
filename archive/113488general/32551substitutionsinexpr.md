---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32551substitutionsinexpr.html
---

## Stream: [general](index.html)
### Topic: [substitutions in `expr`](32551substitutionsinexpr.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 17 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125176108):
If I have `e : expr` and I have a pattern `p : expr` which I would like to substitute for a variable (a bit like `generalize` does for a proof goal) what is the best way to do it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 17 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125176166):
Is there something better than making a goal that contains `e` and calling `generalize p` on it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125177661):
`kabstract` is the core function that does this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 17 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125177712):
Nice! Thanks!

