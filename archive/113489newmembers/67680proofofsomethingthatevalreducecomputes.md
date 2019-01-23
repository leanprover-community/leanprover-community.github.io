---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/67680proofofsomethingthatevalreducecomputes.html
---

## Stream: [new members](index.html)
### Topic: [proof of something that #eval / #reduce computes](67680proofofsomethingthatevalreducecomputes.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 21 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134343915):
If I have:
```lean
import data.finset
open finset
#eval ({0,1,2} ⊆ range 4 : bool) -- tt
#reduce ({0,1,2} ⊆ range 4 : bool) -- tt
```
So lean clearly knows that this fact is true. How can I get lean to give me a proof of (something of the type) `{0,1,2}  ⊆ range 4` that I can then feed into some other function that takes that as a hypothesis? [Was this what `esimp` did in lean 2?]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344507):
My guess is that dec_trivial will work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344516):
you can't push a random Prop into bool, it has to be decidable. And if it's decidable then `dec_trivial` should decide it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344547):
```lean
import data.finset
open finset
lemma XYZ : {0,1,2} ⊆ range 4 := dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344589):
1 year ago I would have just assumed it was magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344595):
My eyes have been opened this year to how mathematics actually works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344599):
Great, that does make a lot of sense in hindsight. I've been using `dec_trivial` as a hammer for nat things without really thinking about what it does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344634):
I also found a good explanation of why the reals don't have decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344685):
https://mathoverflow.net/a/44933/1384

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344694):
Those two real numbers have been verified to be equal to 20000 decimal places, but because there is no algorithm for checking equality of real numbers, you can't use `dec_trivial` to prove it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 21 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344904):
Of course, from the way the claim is worded it's clear that everyone thinks it's true, like the RH is true. Physicists are happy with "equal to 100 decimals => equal"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 21 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134386256):
Are they computable reals though? Is the limit of a real Cauchy sequence computable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 21 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134386498):
not every.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 21 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134388931):
Yes, both those expressions are computable. Basically anything you can write down with a formula composing the usual constructions on reals is computable. The main exception is if you are writing something self referential or making explicit references to turing machines or other turing complete notions, and most math doesn't touch this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 21 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134388942):
But comparing computable numbers is also undecidable

