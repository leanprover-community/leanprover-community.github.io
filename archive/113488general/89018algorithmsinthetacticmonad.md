---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89018algorithmsinthetacticmonad.html
---

## [general](index.html)
### [algorithms in the tactic monad](89018algorithmsinthetacticmonad.html)

#### [Scott Morrison (Sep 09 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593072):
I need some remedial help with functional programming. 

Say I have `f : X -> tactic X`, and `x : X`. Suppose that `f` is possibly very expensive to compute. I would like to recursively apply `f` to `x`, and produce an iterator-like object that can traversed elsewhere in the program, in such a way that `f` is never needlessly computed twice.

#### [Scott Morrison (Sep 09 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593112):
What am I meant to do?

#### [Scott Morrison (Sep 09 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593119):
(Oh, and `f` will eventually fail, and the iterator-like object needs to be able to report termination.)

#### [Scott Morrison (Sep 09 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593162):
I would love to be able to package this up as merely a `tactic X`, whose every invocation magically produces the next element of the sequence, and handles piping the value of `f f f x` into the calculation of `f f f f x` "behind the scenes".

#### [Scott Morrison (Sep 09 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593166):
But that seems unlikely. :-)

#### [Mario Carneiro (Sep 09 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593215):
Use a `lazy_list`

#### [Scott Morrison (Sep 09 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593221):
How does that interact with working in the tactic monad?

#### [Simon Hudon (Sep 09 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593223):
I think something is missing in `lazy_list` to allow this: the function is monadic. But I think we can make a monadic lazy list

#### [Mario Carneiro (Sep 09 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593273):
```

meta inductive mllist (m : Type u → Type u) (α : Type u) : Type u
| nil : mllist
| cons : α → m mllist → mllist
```

#### [Mario Carneiro (Sep 09 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593274):
sadly this has to be meta, since it's not necessarily positive

#### [Simon Hudon (Sep 09 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593332):
You could do something like:

```lean
inductive mlazy_list (m : Type u -> Type u) (a : Type u) : Type (u+1)
| nil : mlazy_list
| cons (b : Type u)  : m (a x b) -> (b -> mlazy_list) -> mlazy_list
```

#### [Scott Morrison (Sep 09 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593374):
Can you explain your one, Simon? I'm not understanding how to use it. :-)

#### [Mario Carneiro (Sep 09 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593489):
eww, you have to package up the whole state to use that

#### [Mario Carneiro (Sep 09 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593493):
also, that in no way resembles a list

#### [Scott Morrison (Sep 09 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593536):
Mario, I'm failing to write `iterates` for your version... A hint?

#### [Simon Hudon (Sep 09 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593537):
@**Mario Carneiro** you have to squint and cock your head left

#### [Simon Hudon (Sep 09 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593542):
@**Scott Morrison** Sure, let's have a look

#### [Mario Carneiro (Sep 09 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593546):
```
meta inductive mllist (m : Type u → Type u) (α : Type u) : Type u
| nil {} : mllist
| cons : α → m mllist → mllist

meta def fix {m : Type u → Type u} [monad m] [alternative m]
  {α} (f : α → m α) : α → m (mllist m α)
| x := (do a ← f x, return (mllist.cons a (fix a))) <|> pure mllist.nil
```

#### [Mario Carneiro (Sep 09 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593591):
the typeclass instances are a bit of a lie since the `monad` and `alternative` instances could potentially be giving different map operations, but since there are no axioms it doesn't matter

#### [Mario Carneiro (Sep 09 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593598):
oh wait
```
meta def fix {m : Type u → Type u} [alternative m]
  {α} (f : α → m α) : α → m (mllist m α)
| x := (λ a, mllist.cons a (fix a)) <$> f x <|> pure mllist.nil
```

#### [Scott Morrison (Sep 09 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593629):
Ah, okay, I'd just worked out a version of `fix`, but forgotten to check for failure...

#### [Mario Carneiro (Sep 09 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593650):
if you skip that you have a valid infinite list representation a la haskell

#### [Mario Carneiro (Sep 09 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593869):
```
meta def f : nat → tactic nat
| 0 := tactic.failed
| (n+1) := tactic.trace n $> n

run_cmd fix f 10 -- prints only 9

meta def mllist.force {m} [monad m] {α} : mllist m α → m (list α)
| mllist.nil := pure []
| (mllist.cons a l) := list.cons a <$> (l >>= mllist.force)

run_cmd (fix f 10 >>= mllist.force >>= tactic.trace) -- prints 9,...,0 and [9, ..., 0]
```

#### [Scott Morrison (Sep 09 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593870):
Oooh, and look at that:
```
meta inductive mllist (m : Type u → Type u) (α : Type u) : Type u
| nil {} : mllist
| cons : α → m mllist → mllist

open mllist

meta def fix {m : Type u → Type u} [alternative m]
  {α} (f : α → m α) : α → m (mllist m α)
| x := (λ a, mllist.cons a (fix a)) <$> f x <|> pure mllist.nil

meta def g (n : ℕ) : tactic ℕ :=
do trace n,
   return (n*n)

meta def foo : tactic unit :=
do L ← fix g 2,
   mllist.cons n L ← return L,
   trace "!",
   mllist.cons n L ← L,
   trace "!",
   mllist.cons n L ← L,
   trace "!",
   skip

example : 1 = 1 :=
begin
  foo,
  refl
end
```
Printing: "2 ! 4 ! 16 !"

#### [Simon Hudon (Sep 09 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133593967):
If you stay in tactics, Mario's version is simpler. Mine is getting tricky because of universes

#### [Scott Morrison (Sep 09 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594092):
Thanks, Simon. I'm trapped in the bottom universe anyway,, `expr`-munging,  so I'll go with Mario's for now.

#### [Mario Carneiro (Sep 09 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594099):
Basically you get into the standard universe issues with coinductive types. I don't know any way to avoid packing the entire state into the type

#### [Simon Hudon (Sep 09 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594113):
:) good I wish I could have made something that fits in a short snippet. But now, I have to bring in a whole F-algebra which I haven't implemented yet :)

#### [Mario Carneiro (Sep 09 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594114):
You can mathematically reason about the entire completed infinite process, but this has poor code behavior

#### [Simon Hudon (Sep 09 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594158):
Doesn't Lean allow you to substitute pure code with something that will be efficient?

#### [Mario Carneiro (Sep 09 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594162):
:four_leaf_clover:

#### [Simon Hudon (Sep 09 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133594222):
:) since you mention coinductive types, you mentioned bounded natural functors a while back. Now I'm thinking my current approach might be getting out of hand so I think I'll give them a try

#### [Reid Barton (Sep 09 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133603765):
> bounded natural functors

Interesting. What you need to construct the initial algebra of a functor F : Set -> Set by transfinite induction is that F is accessible, that is, F commutes with $$\kappa$$-filtered colimits for some **regular cardinal** $$\kappa$$. For example, FX = (S -> X) is $$\kappa$$-accessible if $$|S| < \kappa$$. So I guess this "bounded" condition is related. Do CS people use regular cardinals too?
I found some paper on the topic which contains a lemma which bounds the cardinality of minimal algebras and the formula involves a successor cardinal, so I guess it is the same idea.

#### [Simon Hudon (Sep 09 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/algorithms in the tactic monad/near/133618942):
Thanks for the attempt at giving me an introduction. I'm afraid I'm more of a noob than that when it comes to category theory

