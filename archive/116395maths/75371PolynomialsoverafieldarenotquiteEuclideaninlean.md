---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/75371PolynomialsoverafieldarenotquiteEuclideaninlean.html
---

## Stream: [maths](index.html)
### Topic: [Polynomials over a field are not quite Euclidean in lean](75371PolynomialsoverafieldarenotquiteEuclideaninlean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 28 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127196752):
I've been trying to prove polynomials over a field are a Euclidean domain. The only trouble is, they do not meet the axioms if I use degree as valuation since for two constant polynomials, degree (a % b) =  degree b. Does anyone have experience doing this in any other theorem prover and can recommend a sensible solution. The most obvious is to define`new_degree 0 = 0`, and `new_degree p = degree p + 1` for `p ≠ 0`. Is this the best option?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127196999):
In Isabelle the size is not degree `d` itself but `2^d`, and 0 for the 0 polynomial. See http://isabelle.in.tum.de/dist/library/HOL/HOL-Computational_Algebra/Polynomial_Factorial.html :
```isabelle
definition euclidean_size_field_poly :: "'a :: field poly ⇒ nat" where
  "euclidean_size_field_poly p = (if p = 0 then 0 else 2 ^ degree p)" 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 28 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197047):
Why `2^d`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197113):
I actually think that `valuation_remainder_lt` is not what mathematicians want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197124):
It is a lot stronger than the usual condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197126):
They swapped two quantifiers, so to speak

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197131):
what do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197179):
Quote from wiki: (EF1) If a and b are in R and b is nonzero, then there are q and r in R such that a = bq + r and either r = 0 or f(r) < f(b).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197180):
```quote
Why `2^d`?
```
I guess you get the nice rule: `E(p * q) = E(p) * E (q)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197186):
oh, you need `a % b != 0` also as a precondition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197187):
So it is about the existence of q and r, but this somehow requires it for all q and r

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197188):
(where `E  =  euclidean_size_field_poly`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197191):
Mario, I think that would also fix it, yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197194):
that's basically what wiki is saying, or you can have a disjunction at the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197246):
After all, the valuation of 0 is `37` according to @**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197254):
hey, with the new `with_zero` class you can now just say that `valuation` takes values in `with_zero nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197272):
Nooo! `with_zero nat` looks horrible... can we please have `with_bot` or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197317):
it's the absorbing element of multiplication...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197318):
there is also with_bot, which has no algebraic interpretation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197334):
actually `valuation` looks like it doesn't need any algebraic interpretation, so I guess `with_bot` is fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197383):
It could just be generalised to take any well founded relation, instead of a valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 28 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127215412):
```quote
hey, with the new `with_zero` class you can now just say that `valuation` takes values in `with_zero nat`
```
Where is this class defined? I definitely prefer the idea of option nat over 2^degree.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127218435):
`with_bot` is in `lattice.bounded_lattice`, `with_zero` is in `algebra.group`. Basically it should already be available if you have the basic mathlib lemmas

