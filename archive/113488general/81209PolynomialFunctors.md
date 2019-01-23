---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81209PolynomialFunctors.html
---

## Stream: [general](index.html)
### Topic: [Polynomial Functors](81209PolynomialFunctors.html)

---


{% raw %}
#### [ Kevin Buzzard (Feb 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006369):
Can someone remind me why have I got a 429 page pdf about polynomial functors open on my desktop?

#### [ Kevin Buzzard (Feb 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006427):
I think it was something to do with something someone said in the old chat

#### [ Andrew Ashworth (Feb 26 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006491):
@**Tim Carstens** the coolest thing about w-types (imho) is that they give an account of the whole "derivative of a type" thing (eg zippers), by way of their use of polynomial endofunctors, which themselves have a differential theory (best notes i've seen: http://mat.uab.es/~kock/cat/polynomial.pdf)
this is one of the things i wanted to show when i was studying the category of lean types last year, but i didn't make it all the way :(

#### [ Kevin Buzzard (Feb 26 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006559):
What is a zipper?

#### [ Andrew Ashworth (Feb 26 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006625):
that's a good question. I found this paper: https://www.st.cs.uni-saarland.de/edu/seminare/2005/advanced-fp/docs/huet-zipper.pdf

#### [ Simon Hudon (Feb 26 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006652):
The short version is that it's a data structure that allows you to record the state of traversal of another data structure. For instance, if you traverse a list, you can record the state of that traversal by keeping the list of elements you already visited, the current element and the list of elements to come.

#### [ Kevin Buzzard (Feb 26 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123006693):
Oh I knew I'd heard the phrase before. It's the very end bit of learnyouahaskell

#### [ Tim Carstens (Feb 26 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123007871):
sorry, i was in a meeting. yeah, years ago i read some stuff by Conor McBride about derivatives of types. basically, if you have a type T (X : Type) : Type (like T = list or T = binarytree or whatever), the derivative of T wrt X gives a new type that's "shaped like T but with an X-shaped hole." The derivative of T can be used to describe strategies for traversing data of type T.

#### [ Kevin Buzzard (Feb 26 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008176):
That's crazy stuff. I am hoping as a mathematician that I don't need to think too hard about these things...

#### [ Kevin Buzzard (Feb 26 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008180):
I am not used to traversing data

#### [ Tim Carstens (Feb 26 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008268):
The combinatorialists have a similar thing going on with generating functions and a thing they call "combinatorial schemes" (not related to scheme theory from algebraic geometry). It turns out that in this formulation, generating functions correspond to certain "analytic functors," and you can take a sort of formal derivative of such things. Turns out that analytic functors are examples of polynomial endofunctors, and the formal derivative of an analytic functor coincidences with the derivative of a polynomial endofunctor.

#### [ Kevin Buzzard (Feb 26 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008316):
That sounds like some crazy analogue of differentiating a power series term by term.

#### [ Kevin Buzzard (Feb 26 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008336):
We were talking about that back in the old days on gitter, with a ring theory result which needed differentiation term by term although @**Reid Barton** came up with a neat suggestion which I didn't fully chase up yet but which must surely work.

#### [ Tim Carstens (Feb 26 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008493):
So anyway, by definition every W-type T is the initial algebra of some functor F : C -> C. In Lean or similar environments, this functor will be polynomial (iirc it'll be functor adjoint to pullback along the coproduct of the term constructors, or something like that), and the derivative of the type T is none other than the initial algebra of the derivative of F

#### [ Tim Carstens (Feb 26 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Polynomial%20Functors/near/123008578):
this level of abstract nonsense is not useful for actually writing programs as far as I can tell; certainly it's a horrible way to work with inductive types in Lean, which already has good syntax for working with inductives


{% endraw %}
