---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85011constructingproofsbyhand.html
---

## Stream: [general](index.html)
### Topic: [constructing proofs by hand](85011constructingproofsbyhand.html)

---

#### [Scott Morrison (Apr 10 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867540):
If I have `X Y Z : expr`, and a `P : expr` representing a proof that `X = Y`, how do I make the expression that says `(X = Z) = (Y = Z)`?

#### [Scott Morrison (Apr 10 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867582):
(deleted)

#### [Simon Hudon (Apr 10 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867698):
`to_expr ``(congr_arg (λ x, x = %%Z) %%P)`

#### [Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867800):
woah, okay, that's much better than what I was doing.

#### [Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867805):
I was trying things along the lines of 
````
eq ← mk_const `eq,
prf' ← mk_congr_arg eq prf,
prf' ← mk_congr_fun prf' rhs,
 ````

#### [Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867808):
but quotations are much nicer

#### [Kenny Lau (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867815):
so people are making programs that program

#### [Scott Morrison (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867818):
@**Kenny Lau**, this has been happening since the dawn of time :-)

#### [Mario Carneiro (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867819):
you might even call them... *metaprograms*

#### [Simon Hudon (Apr 10 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124868318):
I guess now is a good time to bring up the Curry-Howard-Lambek correspondence and point out that, similarly, you can use a logical system to show that another logic is sound or complete. You can also use category theory to study the category of categories

#### [Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872852):
Whoa, slow down there, @**Simon Hudon**. Next thing you know, we'll be using English to describe... English. (Or choose your preferred self-describing language of choice.)

#### [Kenny Lau (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872856):
isn't that what dictionaries do?

#### [Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872858):
Also, hi, everyone. :wave: I've been away for a while.

#### [Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872864):
@**Kenny Lau** OMG! You mean it's already happening?!

#### [Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872866):
The end of the world is nigh!

#### [Simon Hudon (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872868):
Hi Sean! We missed you! I hope you still managed to get your daily recommended dose of math and nerdiness ;-)

#### [Sean Leather (Apr 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872909):
I tried here and there, but nothing came close to this. :wink:

#### [Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872918):
i'm high rn

#### [Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872919):
high on homological algebra / wedderburn's theorem

