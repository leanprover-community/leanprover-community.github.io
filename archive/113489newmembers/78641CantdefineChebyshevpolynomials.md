---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78641CantdefineChebyshevpolynomials.html
---

## Stream: [new members](index.html)
### Topic: [Can't define Chebyshev polynomials](78641CantdefineChebyshevpolynomials.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 12 2019 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154992565):
Why doesn't this work?
```lean
def chebyshev : ℕ → polynomial ℝ
| 0 := polynomial.C 1
| 1 := polynomial.X
| (n + 2) := 2 * polynomial.X * chebyshev (n + 1) - chebyshev n
```
Lean tells me the definition relies on `classical.choice`. Indeed putting `noncomputable` at the front fixes things, but why is it noncomputable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993140):
The definition of `polynomial X` is "functions from nat to X which vanish outside a finite set"; "vanish" means "equals zero", and equality is undecidable in the reals. This might be something to do with it. Try `polynomial int` and see if it fixes things!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993205):
NB `import analysis.polynomial` to make it work, but indeed int fixes things, and is probably the "correct" thing to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993404):
```lean
import analysis.polynomial

def chebyshev : ℕ → polynomial ℤ
| 0 := polynomial.C 1
| 1 := polynomial.X
| (n + 2) := 2 * polynomial.X * chebyshev (n + 1) - chebyshev n

#eval chebyshev 17 -- just about works on my desktop
/-
C (65536) * X ^ 17 + C (-278528) * X ^ 15 + C (487424) * X ^ 13 + C (-452608) * X ^ 11 + C (239360) * X ^ 9 + C (-71808) * X ^ 7 + C (11424) * X ^ 5 + C (-816) * X ^ 3 + C (17) * X
-/

#eval chebyshev 19 -- (deterministic) timeout
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993597):
you can probably get farther with a list based representation of the polynomials

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993606):
I guess the reason lists aren't used in general is that the leading term might be 0, which causes problems in general; however it will not cause problems here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993616):
well, it would make it harder to print if the leading term was 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993617):
and get the degree and other things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993618):
In general I guess one could define some more computationally efficient but slightly broken "non-zero polynomials" with addition only defined if you can prove that the degrees are unequal, and multiplication OK over an integral semi-domain :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993669):
But even lists are inefficient, right, because they're linked lists in reality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993672):
If you want to forgo the equality checks, you can define a polynomial as a quotient of representations with some zeros at the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993681):
then addition and multiplication are easy and degree needs equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993690):
yes lists are linked lists which aren't so great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993744):
you could use buffer for really good VM performance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993749):
but they are better than functions which is what is currently used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993751):
I think the polynomials become big if else chains

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993815):
in fact, they probably aren't even reduced, you get these big thunks for calculating the coefficients

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993822):
the advantage of lists is they are a strict data structure, you calculate all the values before recursing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993836):
also -- should have mentioned this before -- `chebyshev` there has an exponential time implementation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993839):
just like the naive fib algorithm


{% endraw %}
