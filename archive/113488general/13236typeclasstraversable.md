---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13236typeclasstraversable.html
---

## Stream: [general](index.html)
### Topic: [type class traversable](13236typeclasstraversable.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123421044):
I have written a type class `traversable` similar to that of Haskell. Universe polymorphism has made the task challenging but I think I have reached a reasonable compromise. I'd love to hear what the community thinks of it: 

https://github.com/cipher1024/mathlib/commit/2f4aa9ed9c0e83d26ea3ae876b801851db6fb8ec

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123421354):
To the non-haskellers: `traversable` is a way of generalizing Lean's `mmap : (α → m β) → list α → m (list β)` so that it works with more collections than just `list`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426715):
heh, i haven't used mmap either, unfortunately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426731):
is this similar to `Iterable` or `Sequence` in other languages?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426744):
It is similar. The big difference is that is has a nice specification

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426797):
If you compare to `map`, `map` allows you to replace any element of a list but does not allow you to perform any effect (updating state, performing, I/O, raising exceptions, etc) in the process. Having a monad `m` (actually, we only need `m` to be an applicative) allows you to perform arbitrary effects in the process of replacing the elements of the collection.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426843):
so for example, how might I traverse the rb-tree implementation in lean core?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426847):
is it easy to adapt an arbitrary data structure to fit the interface?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426854):
If you have `ask_age : string -> io nat` which prompts the user for their age using stdin and stdout, `mmap ask_age user_list` creates the list of the age of all users

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426998):
```quote
is it easy to adapt an arbitrary data structure to fit the interface?
```
It would be tricky for `rbtree` because we have an assumption, the ordering, on the type parameter. `functor`, `foldable`, `traversable`, `applicative` and `monad` requires that any type can be substituted for the type variable. But if you have `rbmap`, you can traverse the value and you can extend the interface to `indexed_traversable` so that when you traverse the value, you can read the key as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427054):
interesting, i wish i could provide feedback, but I think I'd need to sit down with haskell for awhile first and learn how these all work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 08 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427109):
but i can see how useful it would be to have a uniform interface for any data-structure, and traverse it in some deterministic order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427167):
I find it very useful in Haskell and easier to reason about than the iterable patterns that I have encountered. I'm hoping having access to traversable laws will make them awesomer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427268):
What is the difference between a traversable and something that coerces to a list?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427279):
I'm not so sure about how you dealt with the universe stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427328):
If you're looking at `my_collection`, `traverse : (α → m β) → my_collection α → m (my_collection β)`. You're getting a `my_collection` back afterwards. Coercible to `list` would be the weaker `foldable`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427392):
And it is still better than coercible from list because structures like vectors, matrices and even pairs cannot be made from arbitrary lists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427567):
Although it is a little limiting, I think you should make all the universes the same in `traversable`, similar to how `monad` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427725):
I have considered that. With monad, we have `Type u -> Type v` (two universes) which constrains the type variable to be of type `Type u` and not to change. If I take a similar approach, the collection has to be of type `Type u -> Type u` (only one universe) and also limits the type of applicative used. I thought of separating  `has_traverse` and `traversable` to limit the polymorphism in `traversable` but not in `has_traverse`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427734):
Another option is to limit the polymorphism in both but provide type classes like `can_traverse my_appl my_collection` to provide more flexible traversals and laws

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428079):
Right, I think the monad/applicative also has to be `Type u -> Type u` for the statement of `has_traverse` to make sense. The way this has been done in things like `list.bind` is to have the definition itself be fully polymorphic, but the definition that gets used in the instance is universe monomorphic. So the polymorphic functions are still available, you just don't get the typeclass niceties in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428085):
Luckily, almost all programming stuff fits in `Type 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428126):
except existential types, but these have their own issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428246):
That makes sense. Thinking back, the reason I was obstinate about making `traversable` as polymorphic as possible is that I was trying to mimic the `bound` Haskell library which encodes de Bruijn indices in type parameters. That gave me something of type `Type 0 -> Type 1` but luckily, on the google group, someone proposed a nicer encoding. I think I will survive making `traversable` universe monomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123458480):
@**Sebastian Ullrich** Would this be more at home in the core library?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 08 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464546):
@**Simon Hudon** Not sure. Almost all recent additions to core lib are things we actually need there, but I wouldn't mind having access to `sequence`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464625):
My thinking was that `traversable` is such an organizing principle in the Haskell base library that supporting right from the start might generalize a good portion of the machinery there. There was a recent version of the base library (I think 4.9) that made that step and de facto reduced some of the redundancy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464676):
And `sequence` is a fun thing to have when you need `f` and `g` to commute in any `f (g a)` type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123468370):
(deleted)


{% endraw %}
