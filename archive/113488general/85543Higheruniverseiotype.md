---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85543Higheruniverseiotype.html
---

## Stream: [general](index.html)
### Topic: ["Higher universe" io type](85543Higheruniverseiotype.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131240824):
Consider the following silly lean program:
````
import system.io

structure the_structure :=
  (a_type : Type)
  (str : string)

def print_struct : io the_structure := do
  return (the_structure.mk nat "some-text")
````
The program fails to typecheck witht he following error:
````
type mismatch at application
  io the_structure
term
  the_structure
has type
  Type 1 : Type 2
but is expected to have type
  Type : Type 1
````
Is there anything that can be done to salvage this code?

I suppose I'm really asking: why am I prevented from doing this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131240924):
`the_structure` contains a `Type`, so it is a member of `Type 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241013):
On the other hand `io` is defined to only take `Type = Type 0` (for some reason...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241027):
Is there any reason why `io` should only take `Type`s?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241039):
Yes, that is what I was wondering!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241078):
not really, I think Leo just didn't think it would get used like that - programming stuff usually lives in Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241202):
Normally everything is universe polymorphic, `io` seems to be an exception

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241213):
@**Sebastian Ullrich** Do you know anything about the story here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241299):
Unfortunately even `meta` doesn't save you from universe checks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241455):
Here's a weird meta workaround:
```
meta structure the_structure : Type :=
(a_type : expr)
(str : string)

meta def print_struct : io the_structure := do
return (the_structure.mk `(nat) "some-text")
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241536):
I see. Thanks. I think what I'm doing isn't too ridiculous---I'd like to to have a few modules in a program which are different ways of performing the same "job", each needing their own internal types etc. I wanted to be able to fill a structure with their functions and the types they take so the calling code could be module-independent. I'm just trying to say I don't think I'm doing something toooo arcane

haha indeed, and once something is bumped up somewhere it is a cancer which proliferates through everything! :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241617):
existential types are one of the weak points of dependent type theory over a system F like type system such as Haskell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241655):
You can get many of the same benefits of existential types through typeclasses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241764):
Thanks for the workaround there---but am I right in thinking that without converting just everything into expressions, that I won't be able declare another member of that structure to be a function which takes something of type `a_type`?

ok thanks very much for your comments, I think i might resort to that even though there might be a bit more ugliness down the road!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241892):
Most of the currently available typeclasses have a mathematical bent, but consider for example `group A`. This is a typeclass on a type `A` providing it with a "multiplication" operation, which can be implemented however you like, provided it meets the axioms stated in the structure. This is lean's version of java type interfaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241919):
If you have an operation that can be implemented multiple ways, you define the operation as a typeclass and have multiple instances (implementations) of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242028):
> Thanks for the workaround there---but am I right in thinking that without converting just everything into expressions, that I won't be able declare another member of that structure to be a function which takes something of type a_type?

You can convert from expressions to objects and back in meta land using `eval_expr` and `reflect`, respectively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242075):
You lose typechecking though - it's just two `expr`s and it's up to you to make sure one is a function and the other is a value of the same type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242441):
I think I can make it weirder! So, it turns out (because of variable universes being allowed there) changing "io" to "tactic" above *does* work. But(!) now consider the following slight modification
````
structure the_structure :=
  (a_type : Type)
  (str : string)

#check the_structure

meta def print_struct : tactic the_structure := do
  t ← pure (the_structure.mk nat "some-text"),
  n ← pure "ello",
  return t
````
We now fail to typecheck because:
````
type mismatch at application
  pure "ello"
term
  "ello"
has type
  string : Type
but is expected to have type
  ?m_1 : Type 1
````
So `string` is too *low* in the universe hierarchy! This seems even weirder to me than the previous case---is there any why this shouldn't be allowed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242565):
This is due to the fact that everything lives in exactly one type - there is no type subsumption in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242585):
but it's easy to work around in this case  - the `ulift` function moves things from any universe to a higher one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242677):
so you should be able to replace that line with `⟨n⟩ ← pure (ulift.up.{1} "ello"),`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242720):
or `⟨n⟩ ← pure (⟨"ello"⟩ : ulift string),`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242795):
you're awesome, mario! cheers and thanks again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 10 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131243075):
```quote
you're awesome, mario! 
```
Without him, none of this would be happening.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131834807):
I believe a universe-polymorphic `io` would only make sense if we add a new primitive `io.ulift : io a -> io (ulift a)`. Otherwise you would not be able to use any io primitives from an `io` of a higher universe. Monads really seem to be one of the better arguments for universe cumulativity, though so far we haven't run into any unavoidable issues regarding that yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835355):
`io.ulift` is just `map ulift.up`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835390):
oh wait nvm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835397):
better yet, `io.map` should be a primitive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842156):
I came up with a type class `liftable` which I like for this kind of problem. With functors, this universe thing infects the types. I think this will help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842157):
https://github.com/cipher1024/slim_check/blob/f6c44cc48bc44c108ce88c4b1d5cad7b3f63445d/test/slim_check/liftable.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842166):
I can put it in the nursery

