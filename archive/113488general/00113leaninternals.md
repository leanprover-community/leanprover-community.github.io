---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00113leaninternals.html
---

## [general](index.html)
### [lean internals](00113leaninternals.html)

#### [VinothKumar Raman (Mar 13 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123659092):
Is there any good reference to learn how to elaborate implicit arguments to a coc like core? Like how lean does? I am trying to build a coc like language
http://godel.yellowflash.in/
I want to introduce implicit arguments, I have some idea in my head but I couldn't put it down clearly, Its mostly based on resolution in simple basic types. But I have a feeling that it won't work

#### [VinothKumar Raman (Mar 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123659153):
The idea is more like completely apply the explicit arguments and run unification of simple basic types to infer the missing arguments.

#### [Andrew Ashworth (Mar 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123660760):
is godel your effort?

#### [Gabriel Ebner (Mar 13 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123661404):
```quote
The idea is more like completely apply the explicit arguments and run unification of simple basic types to infer the missing arguments.
```
This is almost exactly how Lean's elaborator works.  Essentially you keep around a unification state ("metavar_context", basically a partial assignment of metavariables to expressions).  Now you go recursively through the pre-expression (abstract syntax tree, without implicit arguments) and convert it to an expression.  For every application you fill in the implicit arguments as metavariables, and solve the appropriate unfication constraints so that the application type-checks.  At the end, hopefully all metavariables are filled in and you can instantiate all metavariables in the produced expression.

#### [Gabriel Ebner (Mar 13 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123661424):
Except that `unification of simple basic types` is more like first-order unification + several pages of heuristics.

#### [VinothKumar Raman (Mar 14 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693401):
```quote
is godel your effort?
```
Yea it is my effort. I read a bit about COC and built it

#### [VinothKumar Raman (Mar 14 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693506):
I was reading a bit about the unification on COC. Some claim it `might` be undecidable. But it seem really possible to have implicit arguments and really decide on it right? I don't understand how it could be undecidable.

#### [Mario Carneiro (Mar 14 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693552):
Higher order unification is undecidable

#### [VinothKumar Raman (Mar 14 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693553):
What kind of heuristics does lean use? Is it in general not decidable? Is there any reference to read about tha?

#### [Mario Carneiro (Mar 14 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693572):
Lean doesn't do full higher order unification, it uses a few simpler strategies and mostly sticks to first order unification

#### [VinothKumar Raman (Mar 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693872):
So lean's type checking is guaranteed to terminate? I have a noob question, does making the type checking semi-decidable, affects the soundness in any way?

#### [Mario Carneiro (Mar 14 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694088):
Lean's typechecker is guaranteed to halt, but is not complete - some definitional equalities will not be discovered by the typechecker, and it is impossible for it to do so without becoming undecidable.

#### [Mario Carneiro (Mar 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694112):
The guarantee is of soundness only - if lean verifies a type derivation, then it is correct, but it may error on a correct type derivation

#### [VinothKumar Raman (Mar 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694184):
So its also possible to take the alternate route to have soundness intact by doing a higher order unification, which might not halt but if it did its correct type derivation.

#### [VinothKumar Raman (Mar 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694194):
Thanks, I would read about higher order unification, Is `Huet` algorithm the only one?

#### [Mario Carneiro (Mar 14 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694261):
Note that unification is irrelevant to type checking; there is no unifier in the kernel

#### [Mario Carneiro (Mar 14 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694309):
it is definitional equality itself that is undecidable, due to some complications with subsingleton elimination and proof irrelevance

#### [VinothKumar Raman (Mar 14 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694328):
If the core language doesnt have the notion of `implicit` how do you know that certain arguments are marked implicit?

#### [Mario Carneiro (Mar 14 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694381):
The actual type of expressions `expr` has an annotation field on lambda and pi that marks implicitness, but the kernel ignores it

#### [Mario Carneiro (Mar 14 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694411):
unification and implicit parameters are all the domain of the elaborator, which is a giant untrusted piece of code

#### [VinothKumar Raman (Mar 14 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694416):
Ah it makes sense. I have one more trivial question which I faced 
How do you rewrite `definition x = y` where `x` is not annotated with type to some `(\x:A,Z)y`?

#### [Mario Carneiro (Mar 14 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694467):
I don't quite follow your notation

#### [Mario Carneiro (Mar 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694478):
are you asking how to infer the type of an expression `y`?

#### [VinothKumar Raman (Mar 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694488):
so any `let x = y in z` can be rewritten to `(\lambda x, z) y` so definition is very similar to let right?

#### [Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694534):
a definition doesn't have a scope

#### [Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694536):
also `let` is not the same as a lambda application

#### [VinothKumar Raman (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694538):
But how do you rewrite your definitions to core calculus with just lambda abstraction, when you dont have type annotation

#### [Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694546):
there is a type annotation

#### [Mario Carneiro (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694555):
the syntax is `let x : t := p in e`

#### [VinothKumar Raman (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694561):
`definition x = y` is allowed right? Not just `definition x: z = y` right?

#### [VinothKumar Raman (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694572):
That type annotation is not optional?

#### [Mario Carneiro (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694573):
no, it's only `def x : t := e`. If you leave out the `t` it is inferred and filled in

#### [VinothKumar Raman (Mar 14 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694617):
So elaborator runs type checking before it turns to core calculus?

#### [Mario Carneiro (Mar 14 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694623):
Many type annotations are "optional" in the sense that you don't have to write them, but they are inserted by the elaborator

#### [VinothKumar Raman (Mar 14 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694640):
I was thinking elaborator writes out a new lambda term in the core calculus and type checking is completely different step.

#### [Mario Carneiro (Mar 14 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694646):
the parser produces a `pexpr`, this is a representation that roughly follows the AST of the user's input, all missing type information is absent, and the elaborator inserts metavariables in the holes, performs unification, and results an `expr` that has all type information filled in

#### [Mario Carneiro (Mar 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694699):
After this is done, the expr is sent to the kernel where it is typechecked (again, since the elaborator also has a typechecker that does other stuff on the side)

#### [VinothKumar Raman (Mar 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694710):
Its not very linear as I imagined it to be.

#### [VinothKumar Raman (Mar 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694719):
I think I understand the complexity very well now after trying to implement one :)

#### [Mario Carneiro (Mar 14 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694756):
Writing an elaborator is no joke

#### [VinothKumar Raman (Mar 14 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694770):
There is no concrete theory to it? Like lambda calculus substitution.

#### [Mario Carneiro (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694777):
That's what the kernel does

#### [VinothKumar Raman (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694780):
Its very messy in lot of ways.

#### [VinothKumar Raman (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694789):
I mean the elaborator doesnt have concrete theory?

#### [Mario Carneiro (Mar 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694835):
Parts of it do, I'm sure

#### [Mario Carneiro (Mar 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694851):
like the first order unification algorithm is pretty well understood at this point

#### [VinothKumar Raman (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694863):
Yea, I tried implementing first order unification on simple basic types with `let` polymorphism once
https://github.com/yellowflash/hindley

#### [Mario Carneiro (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694864):
Most of the complication has to do with when to unfold definitions, I think

#### [VinothKumar Raman (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694865):
Its was super clear

#### [VinothKumar Raman (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694915):
But definitions are normalizing right? Which mean you could find normal form and unify them

#### [Mario Carneiro (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694916):
lol sure if you want to wait until the end of the universe

#### [VinothKumar Raman (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694917):
Ah wait, I understand. It could go both directions on beta reduction

#### [Mario Carneiro (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694920):
DTT "terminates", but it's not remotely practical

#### [Mario Carneiro (Mar 14 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694929):
so there are lots of heuristics for when to unfold something

#### [VinothKumar Raman (Mar 14 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123695033):
Oh ok

