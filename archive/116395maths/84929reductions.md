---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/84929reductions.html
---

## Stream: [maths](index.html)
### Topic: [reductions](84929reductions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179083):
What are alpha, beta, delta, zeta, eta, iota reudctions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179138):
http://www.aplusplus.net/lcintro.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179139):
it might not have some of the fancier reductions, but its got the basics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179146):
ncatlab has the rest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179148):
ncatlab :o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179191):
i, too, dislike going to ncatlab first, but for some reason the people there really like dtt and hott and so they have a decent encyclopedia of concepts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179193):
i didn't say i don't like ncatlab

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179200):
heh, cross out my 'too' then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179341):
the lambda calculus has alpha, beta, eta, and they have the same meaning in DTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179349):
delta is definition reduction, replace a definition with its definiens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179351):
zeta is let reduction, let x := t in s -> s[t/x]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179361):
iota is for inductive types, a T.rec where the major premise is a constructor of the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179403):
actually alpha is not a reduction, and eta is not usually used as a reduction either, they are just equalities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179406):
and alpha isn't even needed in lean because de bruijn indices make alpha equivalent expressions syntactically equal


{% endraw %}
