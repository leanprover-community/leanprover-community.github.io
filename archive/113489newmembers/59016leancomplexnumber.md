---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/59016leancomplexnumber.html
---

## Stream: [new members](index.html)
### Topic: [#lean #complex number](59016leancomplexnumber.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) VeraZZ (Jul 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129414919):
hey I intend to write a proof of an equation where the RHS is real and LHS is a sum of a pair of  complex conjugates but it keeps telling the error that the terms on RHS should have type \real . how am I supposed to fix it ? thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415017):
you need to make the real number complex

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 10 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415049):
```lean
import data.complex.basic

#check λ x : ℝ, (x : ℂ)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415117):
Isn't there automatic coercion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415139):
If the LHS is complex, I would think that the RHS would be coerced automatically. (Otoh, if LHS is real and RHS is complex, then Lean will start complaining, or you have to coerce manually.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416182):
@**VeraZZ** if `x` is a real number then `(x : ℂ)` is an attempt to force `x` to be a complex number.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416642):
but the complex number isn't `x`, it's written `↑x : ℂ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416647):
because you applied a secret function to x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416650):
which almost certainly has a name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416653):
but `(x : ℂ)` shows that the coercion is automatic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416713):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416733):
it's `complex.of_real : ℝ → ℂ` of course. That's the name for the explicit injection from the reals to the complexes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) VeraZZ (Jul 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469902):
the LHS is actually a function which gives the inner product of two complex variables (so it is real).Is there a way to make the output of the function complex ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469962):
this is what the coercion does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469980):
just write `( ... : ℂ)` around your real term and then it will be "cast" to complex

#### [![Click to go to Zulip](../../assets/img/zulip2.png) VeraZZ (Jul 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129470001):
aha thanks !

