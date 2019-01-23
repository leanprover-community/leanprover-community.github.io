---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31431Partialfunctions.html
---

## Stream: [new members](index.html)
### Topic: [Partial functions](31431Partialfunctions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005256):
Are there cases where partial functions are actually necessary? [Should probably make a new topic.]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005726):
Necessary for lean, or for mathematics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005767):
I can imagine that high school math (or some university math) definitely contains exercises with, for example, functions not defined for all real numbers.
"Find the domain of definition of blah-blah function, and it's range of values, etc."
"Find the solutions and don't forget about domain of definition."

Programming should have use for them too, imo (they could throws exceptions, errors or NaNs)

...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005768):
```quote
Necessary for lean, or for mathematics?
```
For math.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005836):
There are plenty of places where partial functions in all their guises are useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005877):
But there are many ways to interpret what "partial function" even means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005878):
There are definitely lots of circumstances when the domain of a function is only a subset of some initial set that we are interested in; I guess you might call that a partial function, though I think most of the time people prefer just to talk about functions with different domains.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005889):
In dependent type theory, you have the ability to specify such precise domains that it is not really necessary to have a partial function in the truest sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005934):
Usually when I talk about a partial function in lean I mean a function with an argument that is a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005943):
Every partial function is isomorphic to a total function, over the subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005954):
```quote
Usually when I talk about a partial function in lean I mean a function with an argument that is a proof
```
Like `F: forall x, P x -> A`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005957):
Right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006020):
Actually there are two ways to losslessly totalize the function. One is to "push the argument left" to form the subtype `{x // P x} -> A`, and the other is to push the argument right, into the output, as `X -> \Sigma p, p -> A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006025):
also known as `X -> roption A` or `X ->. A` which is the mathlib type of partial functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006076):
When working in a programming context, it is often reasonable to upgrade this to `X -> option A`. Here the function will "tell you" if you have gone out of domain, and will return a result if not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006085):
whereas `X -> roption A` will not "tell you" if you have got the domain right; you have to pass in a proof that you are allowed to call the function before you get a result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006134):
`X -> option A` is what people have at school. :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006139):
It looks like `roption` is only used in the computability stuff in mathlib, whereas `option` appears much more frequently.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006187):
That's mostly because we don't use partial functions that much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006189):
Most of the time you can avoid it one way or another

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006205):
Notice that with either approach, you get a plain nondependent function. This is important for stuff like rewriting to work smoothly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006216):
with the proof exposed version, you have a dependent function, and then `rw` will often fail and `simp` will produce huge goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006411):
How are square root or logarithms (staying with real numbers) done in lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006601):
Coq has that `positive := { x | x >= 0 }` approach and than square root works on them, if I remember correctly.
No idea about logarithms, should check if they're even in the Standard Library. It seems they're not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006655):
[Here's sqrt](﻿﻿﻿﻿https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L508) and [here's the in-progress fork with ln](https://github.com/leanprover-community/mathlib/blob/exp/analysis/exponential.lean#L119).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006734):
Most mathematical functions in mathlib are totalized, meaning that rather than preserving the proof part we just do something random when it's not true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006750):
e.g. a sqrt function might be defined to be the usual thing for nonnegative x and 0 for negative x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 02 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135013778):
unfortunately sqrt(-1) is not 37

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135016849):
And 1/0 isn't too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 02 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135016912):
Ok, then partial functions are used only if really necessary. We should do that at school math too :D.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135018459):
I am a mathematician and was very uncomfortable initially with the fact that sqrt(-1) was not `NaN`. But now I interpret it exactly as Mario says -- I have a mental note not to use the square root function on negative numbers in the statements of my theorems because I use it like a partial function even though it's total. Of course in the proofs I can do what I like. The fact that the square root function "should" only be used on non-negative integers is somehow something which a human uses for guidelines, but Lean doesn't need to be told this.


{% endraw %}
