---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27607rationalsthatareactuallyintegers.html
---

## [general](index.html)
### [rationals that are actually integers](27607rationalsthatareactuallyintegers.html)

#### [Johan Commelin (Aug 08 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122581):
By some elaborate method I have defined a polynomial with coefficients in `rat`. Now there is a math theorem (which I hope to turn into a Lean theorem) that says that my polynomial actually has coefficients in `int`. But this is not at all clear from the definition. What is the best way to turn my polynomial into something with integral coefficients?
(For reference, my actual use case with mv_polynomials can be found here: https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215)
Here is a baby case version of this phenomenon:
Define $$x = {7 \choose 4}/7$$. A priori this is a rational number. But because $$7$$ is prime, it turns out that $$x$$ is an integer. This can be turned into Lean, so that we have some `x : rat`. Now I could do `define y := x.num`. And then try to prove that `(y : rat) = x`.
Is this the best way to go about this problem? How would this scale to (mv_)polynomials?

#### [Kevin Buzzard (Aug 08 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122654):
I guess you have to insert the maths somewhere. I think your question is asking how to insert the maths. Maybe the answer depends on the maths that needs to be inserted.

#### [Johan Commelin (Aug 08 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122794):
Right. That might very well be true. In maths-maths there would be just one theorem. "Look, this polynomial actually has `int` coeffients." In Lean-maths I guess there will be 6 stupid ways, and 1 clever way...

#### [Johan Commelin (Aug 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122901):
So maybe the clever way depends on the math that needs to be inserted. But so far I've usually seen that there is a CS-reason for choosing a particular method. And then the maths that needs to be inserted has to be pushed into the right form.

#### [Kevin Buzzard (Aug 08 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122937):
At the end of the day you have some object defined over Q (e.g. a polynomial or something) and you need to prove that there's some object defined over Z which coerces into it. Now of course _if you know the theorem is true_, then for every q in Q you could let z be floor(q) or ceil(q) or numerator(q) or whatever. But you'll still have to prove that \u z = q, and my guess is that the best choice of z will depend on what your proof that q is actually an integer will be.

#### [Kevin Buzzard (Aug 08 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122974):
What is the proof, by the way? I've not looked at the maths in your code yet...

#### [Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123019):
That is one argument. The other is that you later on want to use `z`.

#### [Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123045):
And that might be more important then getting a convenient form for the proof of `\u z = q`.

#### [Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123050):
There is no proof yet.

#### [Johan Commelin (Aug 08 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123085):
The proof that I've seen (in Serre's "Local fields") is not trivial. It will need quite some extra work to formalise it.

#### [Kevin Buzzard (Aug 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123187):
My gut feeling is that the best strategy is to figure out what the maths strategy is first. I think that's a more important question than asking about the endgame.

#### [Johan Commelin (Aug 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123317):
Ok. Then I'll have to do a bit of homework first (-;

#### [Simon Hudon (Aug 08 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129857):
If I had to try, I would try to not step through the rationals. I would use integer division and prove that 7 divides $$\binom{7}{4}$$ for later consumption (i.e. if you need to multiply x by 7 and prove that it lands back on $$\binom{7}{4}$$).

#### [Simon Hudon (Aug 08 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129914):
(do you use a `\begin{array} ...` for the choice operator?)

#### [Kenny Lau (Aug 08 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129971):
you mean `\binom`?

#### [Simon Hudon (Aug 08 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131130176):
Yes indeed, thanks

#### [Johan Commelin (Aug 09 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131148931):
Alternative: `{7 \choose 4}`.

#### [Johan Commelin (Aug 09 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131148978):
About your suggestion: In the baby case I agree that it is possible to avoid the rationals. But with my polynomial, I don't see how to do this.

#### [Simon Hudon (Aug 09 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131150412):
Can you show me why that isn't possible? I would have thought that using something like `↑(choose p q ÷ 7)` wouldn't pose a problem in a context with rational numbers.

#### [Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151838):
Simon, if you look at https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215 you see that I take some polynomial $$\Phi$$ with integral coefficients, and I build another (sequence of) polynomial `witt_structure_int \Phi` with integer coefficients.

#### [Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151844):
But the construction goes via the rationals.

#### [Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151851):
I first define `witt_structure_rat` in terms of `X_in_terms_of_W`. And those latter polynomials have honest rational coefficients.

#### [Johan Commelin (Aug 09 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151897):
There might be an entirely different way of defining `witt_structure_int`, but I don't know this.

