---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/89394Writingrationals.html
---

## Stream: [new members](index.html)
### Topic: [Writing rationals](89394Writingrationals.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984699):
How can I rewrite a known rational `r : \Q` in the form `rat.mk (...) (...)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984779):
I expected something like `change rat.mk (rat.num) (rat.denom) at r,` but that doesn't work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984790):
Try cases on r?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984796):
Yep, just tried that, works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984816):
I agree that `rat.num / rat.denom = r` but that looks to me like a theorem rather than something which is true by definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984846):
\Q is an inductive type, so you can always do cases on it. It only has one constructor so the number of goals won't change.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135984872):
I just found `theorem rat.num_denom : ∀ (a : ℚ), a = rat.mk (a.num) ↑(a.denom)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135985882):
If you want _anything_ other than what `cases` provides (and you might well find that you want what @**Scott Olson** says rather than what I said -- I am breaking the interface) then my advice to you is to open `data/rat.lean` and pore through it until you spot what you need. Either that or get good at guessing the names of theorems (there are tips for doing this).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Writing%20rationals/near/135985883):
By the way, the actual construtor `rat.mk'` needs a couple of proofs, and that's what you'll get with `cases`. The reason the initial constructor is so inconvenient is that it guarantees that two rationals are equal if and only if they're made with the same data (remember that all proofs of a proposition are equal by definition).

