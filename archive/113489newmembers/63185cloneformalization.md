---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63185cloneformalization.html
---

## [new members](index.html)
### [clone formalization](63185cloneformalization.html)

#### [Miroslav Olšák (Oct 23 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136329846):
Hello everybody, we tried a testing formalization of a simple proposition about clones in several ITP's for comparison. LEAN seems pretty nice so far. However, I believe that there should be a better approach to certain parts the proof (if we just knew LEAN better).
You can see the task description,  together with my complains (/ TODO) under the link.
http://atrey.karlin.mff.cuni.cz/~mirecek/formal-math/clones.lean

#### [Johan Commelin (Oct 23 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136331045):
@**Miroslav Olšák** I'm having trouble with certain symbols. I think unicode is being messed up or something. Could you post your code again with correct encoding? Maybe as a Github Gist, or something... (Don't know if you use github...)

#### [Bryan Gin-ge Chen (Oct 23 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136334848):
In Firefox you can set the text encoding manually to unicode (View... Text Encoding...) and then the page displays properly. Apparently that feature no longer exists in Chrome.

#### [Miroslav Olšák (Oct 23 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136357974):
All right, there it is on GitHub:
https://github.com/mirefek/clones-lean/blob/master/clones.lean
Any suggestions to the code? Is there a better way for case analysis through fin 3? Or a tactic that can do  all the rewrite at the end of the code?

#### [Mario Carneiro (Oct 23 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136358074):
I think you should use ternary functions rather than arrays

#### [Mario Carneiro (Oct 23 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136358153):
or products, but curried will be nicer

#### [Miroslav Olšák (Oct 23 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360087):
```quote
I think you should use ternary functions rather than arrays
```
Definitely not. Sure, it suffices for this simple example but it does not correspond to the definition of clone at all.

#### [Miroslav Olšák (Oct 23 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360141):
```quote
or products, but curried will be nicer
```
Show me.

#### [Miroslav Olšák (Oct 23 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360748):
@**Mario Carneiro** What do you mean by curried products?

#### [Johan Commelin (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360856):
You can write a function `X × Y → Z` as `X → Y → Z`.

#### [Johan Commelin (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360866):
This is known as "currying"

#### [Kenny Lau (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360871):
aka product is left-adjoint of hom

#### [Kenny Lau (Oct 23 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136360917):
(sorry)

#### [Miroslav Olšák (Oct 23 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361131):
I see.
But how to define the general composition for operations written like this?
I really think it is better to interpret them as functions A^n -> A, in the case of clones, as mathematicians usually do.

#### [Johan Commelin (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361197):
I tend to agree (I'm also a mathematician). But these CS people have really crazy operators that will do what you want.

#### [Johan Commelin (Oct 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361225):
And they can explain the benefits. (The disadvantage is that it no longer looks like what you are used to, although you can prove it is the same thing.)

#### [Abhimanyu Pallavi Sudhir (Oct 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361233):
I guess the advantage of the CS approach is that you can just give a single input and get a function.

#### [Johan Commelin (Oct 23 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361300):
I don't know what a clone is exactly, but what I saw on wiki looks like it is related operads. @**Miroslav Olšák** Is that right?

#### [Reid Barton (Oct 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361938):
nlab claims clones are analogous to operads but I think the relationship is less obvious than it looks at first glance

#### [Reid Barton (Oct 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136361968):
The composition operation for operads takes a $$k$$-ary operation and $$k$$ operations of arity $$n_1$$, ..., $$n_k$$ and gives you an operation of arity $$n_1 + \cdots + n_k$$

#### [Reid Barton (Oct 23 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136362014):
where the picture is that the $$k$$ operations each have access to disjoint subsets of the input variables

#### [Reid Barton (Oct 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136362084):
here, each of the composed operations has access to all the input variables. I guess maybe it is the same thing as saying that you have the power to duplicate variables.

#### [Miroslav Olšák (Oct 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136362172):
I understand the advantages of functional programming, but not in this case. If anybody feels that defining a clone by curried functions would be better, it would be nice to see such an approach.

Concerning to operads, I don't know them very well. From what I see on Wiki right now, operads are more general than abstract clones since they does not have projections (and also, operads don't glue variables). I think Reid Barton is right, just faster than me :-)

#### [Mario Carneiro (Oct 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136384717):
The fact that you can partially apply a curried function is not actually that important in this case, it's just the way lean naturally deals with n-ary functions

#### [Mario Carneiro (Oct 24 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136385067):
@**Miroslav Olšák** Okay, I see now. I thought that you only had to deal with ternary functions, but now I see that the statement involves membership in a clone, which involves arbitrary arity functions

#### [Mario Carneiro (Oct 24 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136385128):
In this case, I will point you to [`nat.primrec'`](https://github.com/leanprover/mathlib/blob/master/computability/primrec.lean#L1132-L1141), which is somewhat similar in needing to deal with collections of n-ary functions and n-ary composition. I use functions of type `vector n A -> A`, and n-ary composition is `λ a, f (of_fn (λ i, g i a))`

#### [Miroslav Olšák (Oct 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/clone formalization/near/136396537):
Interesting. Do you think that vectors behave in Lean better than arrays in general? (even though they are mathematically the same).

