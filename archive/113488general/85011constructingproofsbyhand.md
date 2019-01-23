---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85011constructingproofsbyhand.html
---

## Stream: [general](index.html)
### Topic: [constructing proofs by hand](85011constructingproofsbyhand.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867540):
If I have `X Y Z : expr`, and a `P : expr` representing a proof that `X = Y`, how do I make the expression that says `(X = Z) = (Y = Z)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867582):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867698):
`to_expr ``(congr_arg (λ x, x = %%Z) %%P)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867800):
woah, okay, that's much better than what I was doing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867805):
I was trying things along the lines of 
````
eq ← mk_const `eq,
prf' ← mk_congr_arg eq prf,
prf' ← mk_congr_fun prf' rhs,
 ````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867808):
but quotations are much nicer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867815):
so people are making programs that program

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867818):
@**Kenny Lau**, this has been happening since the dawn of time :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867819):
you might even call them... *metaprograms*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124868318):
I guess now is a good time to bring up the Curry-Howard-Lambek correspondence and point out that, similarly, you can use a logical system to show that another logic is sound or complete. You can also use category theory to study the category of categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872852):
Whoa, slow down there, @**Simon Hudon**. Next thing you know, we'll be using English to describe... English. (Or choose your preferred self-describing language of choice.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872856):
isn't that what dictionaries do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872858):
Also, hi, everyone. :wave: I've been away for a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872864):
@**Kenny Lau** OMG! You mean it's already happening?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872866):
The end of the world is nigh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872868):
Hi Sean! We missed you! I hope you still managed to get your daily recommended dose of math and nerdiness ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872909):
I tried here and there, but nothing came close to this. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872918):
i'm high rn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872919):
high on homological algebra / wedderburn's theorem

