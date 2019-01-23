---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05739namingequivalencerelation.html
---

## Stream: [new members](index.html)
### Topic: [naming equivalence relation](05739namingequivalencerelation.html)

---

#### [Ali Sever (Jul 18 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879693):
I have a function `eqd : point → point → point → point → Prop`, and I have made an equivalence relation on `point × point`. Instead of using `setoid.r (a,b) (c,d)`, is it possible to change the notation to be `(a,b) ≡ (c,d)`?

#### [Reid Barton (Jul 18 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879836):
Yes.
You can already use `≈` as notation for `setoid.r`, if you don't mind using that instead.

#### [Reid Barton (Jul 18 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879955):
Otherwise, you can define `local infix ≡ := setoid.r`, or a number of variations on this.

#### [Reid Barton (Jul 18 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879991):
`local` is optional, depending on whether you want the notation to be in effect everywhere or only in the current file/section

#### [Ali Sever (Jul 18 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129881273):
I'm assuming it's not possible to make the notation `a b ≡ c d`.

#### [Kevin Buzzard (Jul 18 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882842):
I don't know if the parser can handle that. You want more than an infix operator -- you want an operator which eats two things on both sides. I wonder if `(a b ≡ c d)` would be possible somehow?

#### [Patrick Massot (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882911):
Depends on your alignment. Chaotic evil players are allowed to use tricky unicode blank characters to achieve what you want.

#### [Reid Barton (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882947):
I don't think you can have two arguments to the notation separated only by whitespace.
The way to test this is to try out things like ``notation a b ` ≡ ` c d := a + b``. That gives an error on `b`.

#### [Reid Barton (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882955):
Yes, I should have been more careful and specified which sort of whitespace I meant. :)

#### [Reid Barton (Jul 18 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129883881):
Another option for the chaotic player is to define a `has_coe_to_fun` from `point` to `point -> (point, point)` which sends `a` to `\lam b, (a, b)`.

