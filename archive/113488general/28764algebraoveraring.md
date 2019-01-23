---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28764algebraoveraring.html
---

## Stream: [general](index.html)
### Topic: [algebra over a ring](28764algebraoveraring.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193725):
@**Mario Carneiro** Can we do algebra over a ring now? Can we prove that every ring is an Z-algebra? every abelian group is a Z-module?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193798):
Why should this be a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193803):
We can just define the category of `R`-algebras. That shouldn't be hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193819):
typeclass problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193921):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/ring.20algebras/near/133299335

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151193922):
look, nobody gives a second look at this problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151194214):
I haven't looked at it because all my Lean time is currently going to sheaves. But I'm certainly interested in this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151194240):
I think that in the case of algebras I would go category-theoretic straight away. The more you bundle, the less likely you run into crazy type-class diamonds.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 08 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algebra%20over%20a%20ring/near/151194272):
Unfortunately I'm not sure we got enough module refactor yet. As far as I understand, Mario still has to work on getting modules over several base rings to behave nicely

