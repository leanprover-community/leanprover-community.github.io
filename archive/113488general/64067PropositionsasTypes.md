---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64067PropositionsasTypes.html
---

## [general](index.html)
### [Propositions as Types](64067PropositionsasTypes.html)

#### [Lyle Kopnicky (Apr 16 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125127870):
I'm not clear why the definition of `p1` below is not a type error. What can it possibly mean for `p1` to be a proof of a proof of a proposition?

```
constant U : Type
constant u0 : U
constant u1 : u0 -- type error

constant p0 : Prop
constant p1 : p0 -- no type error!
constant p2 : p1 -- type error
```

I thought of `U` and `Prop` as being of the same "universe level", but apparently they're not.

#### [Simon Hudon (Apr 16 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125127979):
@**Lyle Kopnicky** Before I answer, do you mind editing the topic to your post (and don't forget to select "Change later messages to this topic"). Maybe set it to "Propositions as Types"

#### [Simon Hudon (Apr 16 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128027):
Let's have a look at what kind of beast `Prop` is. `Prop` is actually synonymous with `Sort 0`, that is, a sort in universe 0. `Sort 0` has type `Sort 1` and `Sort 1` has type `Sort 2`:

```
Prop : Sort 1
Sort 1 : Sort 2
Sort 2 : Sort 3
...
```

#### [Simon Hudon (Apr 16 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128076):
For `e0 : e1` (a type judgement) to make sense, e1 must be a sort, i.e. there must be a universe `u` such that `e1 : Sort u`.

#### [Simon Hudon (Apr 16 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128126):
Thanks!

We can see that `p1 : p0` satisfies this constraint because `p0 : Sort 0`. Similarly, `u0 : U` because there is a `u` (1), such that `U : Sort u`. Note that `Type u = Sort (u+1)`

#### [Simon Hudon (Apr 16 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128133):
We have the same problem for `u1 : u0` as for `p1 : p0`

#### [Kenny Lau (Apr 16 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128230):
```quote
I'm not clear why the definition of `p1` below is not a type error. What can it possibly mean for `p1` to be a proof of a proof of a proposition?
```
No, `p0` is the proposition and `p1` is the proof.

#### [Simon Hudon (Apr 16 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128238):
If we omit universes for a moment, a type `t` is a term (or expression) such that `t : Sort` and that allows you to type expressions `e`: `e : t`.

That means that `Sort` must somehow be a type. This is where universes become important. If we still ignore them we have `Sort : Sort` but that invites paradoxes so we have to rank sorts: `Sort u : Sort (u+1)`

#### [Lyle Kopnicky (Apr 16 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128244):
Ah, that makes sense, @**Kenny Lau** , thanks.

#### [Lyle Kopnicky (Apr 16 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128296):
Thanks, @**Simon Hudon** . If `Prop` is `Sort 0`,  what sort does `p0` have? Is it `Sort (-1)`?

#### [Kenny Lau (Apr 16 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128337):
`p0` is not a sort

#### [Lyle Kopnicky (Apr 16 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128345):
Is `Type` a sort?

#### [Kenny Lau (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128383):
Type = Sort 1

#### [Simon Hudon (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128384):
I see why you would think that. `Sort u` is inhabited by sorts. They are not necessarily inhabited by sorts themselves.

```quote
p0 is not a sort
```

p0 is a sort but it is not equal to `Sort u` for any u.

#### [Kenny Lau (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128390):
what ***sort*** of nonsense is this

#### [Simon Hudon (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128395):
It is a sort, it can be on the right hand side of `:`

#### [Simon Hudon (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128399):
It is not a type of sorts though

#### [Kenny Lau (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128401):
now I'm having jamais vu on sort

#### [Lyle Kopnicky (Apr 16 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128459):
I guess I am thinking that everything has some "universe level", where `Sort 1` is level 1, `Sort 2` is level 2, etc.  Then if you can write `a : b`, `a` is one level lower than `b`. And you bottom out at some point, so that you can no longer write `a : b` if `b`'s level is too low.

#### [Lyle Kopnicky (Apr 16 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128525):
So, if `Type` is at level 1, `U` is at level 0 (though it's not synonymous with `Sort 0`), and `u0` is at level -1, and we can't write `u1 : u0` because `u0` has too low of a level. Does that make any sense?

#### [Simon Hudon (Apr 16 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128530):
You could think of it that way, that's true. It's important to note that "too low a level" makes a term not a type. We normally reserve that universe terminology for types. There is a problem with thinking of level -1 though

#### [Lyle Kopnicky (Apr 16 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128574):
I think of `u0` as the value level.

#### [Lyle Kopnicky (Apr 16 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128578):
Even though that can be confusing because types are values too.

#### [Lyle Kopnicky (Apr 16 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128594):
So, `Sort 0` is the lowest level of types, and just below that is the value level. Things that are not types.

#### [Simon Hudon (Apr 16 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128595):
We can have some data `d` of type `t` with `t : Sort 3`. You would probably think of it as being in universe 2 but `d` is still not the type of any other terms.

#### [Lyle Kopnicky (Apr 16 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128648):
OK, yeah, I guess my analogy breaks down there.

#### [Lyle Kopnicky (Apr 16 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128703):
But what confuses me is, if `Prop : Sort 1`, then `Prop` would be at the same level as `U`... level 0. So you should be able to have `p0 : Prop`, but not `p1 : p0`.

#### [Lyle Kopnicky (Apr 16 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128707):
That would be going to "too low of a level".

#### [Lyle Kopnicky (Apr 16 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128719):
So I guess my concept of "too low of a level" doesn't really work, either.

#### [Simon Hudon (Apr 16 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128736):
So think of it this way: we're talking about a formal system focused on terms. Some terms `t` are types. Every term `t'` has a type such that `t' : t`. Every type has type `t : Sort u` for some universe `u`

#### [Lyle Kopnicky (Apr 16 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128828):
Then in `p1 : p0`, `p0` must be a type. And `p0 : Prop`, but `Prop` is synonymous with `Sort 0`, so that works.

#### [Simon Hudon (Apr 16 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128841):
Exactly

#### [Lyle Kopnicky (Apr 16 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128893):
But is `Type` synonymous with some sort?

#### [Kenny Lau (Apr 16 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128895):
sort 1

#### [Lyle Kopnicky (Apr 16 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128905):
OK

#### [Lyle Kopnicky (Apr 16 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128945):
And `Type 1 = Sort 2`, `Type 2 = Sort 3`, and so on?

#### [Simon Hudon (Apr 16 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128946):
That's right

#### [Lyle Kopnicky (Apr 16 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125128997):
So, `Prop` is just the universe below `Type`.

#### [Simon Hudon (Apr 16 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129003):
Yep!

#### [Lyle Kopnicky (Apr 16 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129065):
Coming from Haskell, where we have a value level, and a type level (which is like `Type`), and a kind level (which is like `Type 1`), and then... well, they've sort of unified the levels from `Type 1` up... I'm trying to figure out what the analogy is to `Prop` there.

#### [Lyle Kopnicky (Apr 16 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129072):
What does it mean to have another type level, *below* what I thought of as the lowest level?

#### [Simon Hudon (Apr 16 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129115):
Haskell doesn't really have a type `Prop`. types in `Prop` are a bit like data type that are guaranteed to be erased at run time

#### [Lyle Kopnicky (Apr 16 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129131):
Haskell erases all the types at runtime anyway. Well, except maybe if you use existential types.

#### [Simon Hudon (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129135):
What I'm saying is that the values of a type in `Prop` are erased at run time, not just the type itself

#### [Lyle Kopnicky (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129175):
Gotcha.

#### [Simon Hudon (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129179):
Have you ever used the singleton library in Haskell?

#### [Lyle Kopnicky (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129183):
No, but I've seen it demonstrated.

#### [Lyle Kopnicky (Apr 16 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129251):
Are you saying that the singletons are also values that are erased at runtime?

#### [Simon Hudon (Apr 16 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129267):
Not quite no. So far as I know they haven't added erasure for those types. There's still an interesting comparison

#### [Lyle Kopnicky (Apr 16 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129270):
I'll take a look at it sometime, thanks.

#### [Simon Hudon (Apr 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129361):
`singleton` hinges on the idea of having type level natural numbers (and other objects). If you have `n0` and `n1` are type level natural numbers, `n0 .<= n1` is the type of a proof that shows that `n0 ≤ n1`. It is a data type and it is uninhabited (except for `undefined`) unless the value of `n0` is less or equal to that of `n1`. As types `n0` and `n1` have only one value (again, except for `undefined`): the number they represent.

#### [Simon Hudon (Apr 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129363):
`Prop`s are a bit like those `.<=` types (I'm not sure of the exact syntax, sorry)

#### [Simon Hudon (Apr 16 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129369):
Correction: the singleton operator is `%<=`, not `.<=`

#### [Simon Hudon (Apr 16 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129370):
Does it clarify things?

#### [Lyle Kopnicky (Apr 16 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129566):
It seems analogous to Prop, yes. But I'm struggling to line it up with the universes.

#### [Simon Hudon (Apr 16 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129575):
When you're getting started, you can mostly ignore universes. You can simply use `Type` and `Prop`. Higher universes become necessary when you bring in existential types.

#### [Lyle Kopnicky (Apr 16 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129632):
OK. I meant that I'm imagining what the universes are in Haskell, and trying to figure out which level these propositions defined with the singleton library live at.

#### [Simon Hudon (Apr 16 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129682):
I think the analogy with Haskell's term, type and kind is somewhat wobbly.

#### [Lyle Kopnicky (Apr 16 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129732):
I was thinking that Haskell's "type" is like `Type`, and the lowest-level kind is like `Type 1`.

#### [Lyle Kopnicky (Apr 16 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129746):
Or... maybe `Type` is a kind, so instances of that are types.

#### [Simon Hudon (Apr 16 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129787):
The need for universes in Lean comes from a requirement that the language be a consistent logic. Haskell doesn't have that requirement. I believe the requirement for Haskell to separate terms and types is historical. It started off with an ML style language and made a lot of changes over time including `RankNTypes` and higher kinded types.

#### [Lyle Kopnicky (Apr 16 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129789):
Right.

#### [Simon Hudon (Apr 16 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129797):
If we forget about Haskell's existential types and GADTs, I think its types are `Type 0` and its kinds are `Type 1`

#### [Lyle Kopnicky (Apr 16 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129843):
Yeah, makes sense. Except now they have unified `Type 1`, `Type 2`, and so forth...

#### [Lyle Kopnicky (Apr 16 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129894):
So, these type-level naturals would have type `Type 1`?

#### [Lyle Kopnicky (Apr 16 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129941):
Maybe this will all make more sense if I look at Idris. It should have similar power to Lean but be easier to compare to Haskell.

#### [Lyle Kopnicky (Apr 16 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129987):
So, translate concept from Lean to Idris, then from Idris to Haskell. Or vice versa.

#### [Simon Hudon (Apr 16 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129989):
Let me give you an example where `Type 1` is needed in Lean.

#### [Lyle Kopnicky (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125129997):
OK

#### [Mario Carneiro (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130000):
Hi Lyle,
There are three kinds of things in Haskell: terms, types, and kinds. The same trichotomy appears in Lean, but kinds have kinds too

#### [Simon Hudon (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130001):
`(Σ t : Type 0, list t) : Type 1`. This is basically an existential type. Because it "contains" a `Type 0`, it has to live in universe 1

#### [Simon Hudon (Apr 16 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130039):
Mario to the rescue! Thanks!

#### [Mario Carneiro (Apr 16 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130043):
Also kinds are types and types are terms so it forms a subset relation

#### [Mario Carneiro (Apr 16 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130049):
A kind (or a sort) is a term of the form `Sort u` for some `u`. A type is a term whose type is a kind, and a term is anything which is well typed

#### [Mario Carneiro (Apr 16 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130051):
Any term has a type which is a type, which means that if `e : t` then `t : Sort u` for some `u`

#### [Mario Carneiro (Apr 16 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130098):
Here `e` and `t` are both logically related to `u`, which you might call the level of the expression, but obviously their relation to `u` is slightly different. `t` is level 1 means that `t : Sort 1` while `e` has type in level 1 since `e : t : Sort 1`

#### [Lyle Kopnicky (Apr 16 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130101):
Right, that was my understanding so far.

#### [Mario Carneiro (Apr 16 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130146):
In Haskell, there are values, types, and kinds which correspond roughly to terms in types of level 1, types in level 1, and `Sort 1` with maybe some variations on it

#### [Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130153):
The algebra of kinds in Haskell is not as rich as Lean's, they only have one universe

#### [Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130155):
I think they call it `*`

#### [Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130158):
but it is closest to `Sort 1` aka `Type`

#### [Lyle Kopnicky (Apr 16 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130246):
Yeah, they actually call it `Type` now, in newer versions

#### [Lyle Kopnicky (Apr 16 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130254):
So, how do the type-level nats fit into this?

#### [Simon Hudon (Apr 16 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130255):
@**Mario Carneiro** I think it's closer to `Type*` because of existential types and GADTs

#### [Mario Carneiro (Apr 16 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130296):
It's one universe, but it's system F so it is impredicative

#### [Mario Carneiro (Apr 16 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130297):
and somehow contradiction is avoided by a hair

#### [Simon Hudon (Apr 16 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130342):
I thought because of `undefined` you couldn't consider the whole thing a consistent logic

#### [Mario Carneiro (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130355):
That's true too, but System F itself is consistent if you leave out bottom

#### [Mario Carneiro (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125130402):
there are lots of extensions that break consistency because Haskell wants to be turing complete

#### [Lyle Kopnicky (Apr 16 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131020):
http://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#kind-polymorphism-and-type-in-type

The `TypeInType` extension allows kinds to be as intricate as types, allowing explicit quantification over kind variables, higher-rank kinds, and the use of type synonyms and families in kinds, among other features.

#### [Mario Carneiro (Apr 16 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131031):
I am not a haskell expert, but from what I can tell, type level nats are a way to have nats as types, so that you can quantify over them without breaking the value/type distinction (and thus get dependent types over nats)

#### [Mario Carneiro (Apr 16 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131168):
In lean this is not necessary because it's fully dependent anyway. Haskell is getting closer and closer to dependent type theory as time goes on, but it's not there yet

#### [Lyle Kopnicky (Apr 16 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131214):
Yeah, since in Haskell you can't write a function from values to types, but you can write a function from types to types, these type-level nats stand in for values, but can be used in functions that produce types.

#### [Mario Carneiro (Apr 16 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131264):
`array A : nat -> Type` is an example of a dependent type family in lean

#### [Lyle Kopnicky (Apr 16 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131313):
I see what you're saying about the one universe in Haskell. Traditionally in Haskell, you have kind `*`, which is Lean's `Sort 1`, and you have types whose type is `*`, and you have values of those types. With the `TypeInType` extension, the kinds can be treated like types that now have their own types, but it's all still one universe.

#### [Mario Carneiro (Apr 16 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131354):
Oh right, there was something else I wanted to say about your earlier example: `U : Type` and `Prop : Type`, so these can be equated (`U = Prop` is well formed), but they are nevertheless treated differently, since if `u : U` then `e : u` is malformed but if `p : Prop` then `h : p` is okay.

#### [Mario Carneiro (Apr 16 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131362):
You can't prove that a type "is" a universe, it must be so syntactically

#### [Lyle Kopnicky (Apr 16 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131404):
Hmm, OK. Well that's because `Prop` is also a sort.

#### [Mario Carneiro (Apr 16 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131405):
exactly

#### [Mario Carneiro (Apr 16 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131410):
It is possible to consider type in type in dependent type theory, this would be a relatively small change to a lean-like language, but it is inconsistent by Girard's paradox so it is not usually used in languages that aspire to a sound proof theory

#### [Mario Carneiro (Apr 16 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131444):
In fact, forgetting the universes is the first step in compiling lean programs

#### [Lyle Kopnicky (Apr 16 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131499):
Right

#### [Lyle Kopnicky (Apr 16 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131502):
In Haskell you can have kind `* -> *`, e.g. `List : * -> *`. So in Lean would `List` have type `Type -> Type`? Then what's the type of `Type -> Type`? Is that `Type 1`?

#### [Mario Carneiro (Apr 16 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131512):
Indeed, `list` has type `list : Type u -> Type u`, which itself has type `Type (u+1)`

#### [Lyle Kopnicky (Apr 16 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131514):
Ah, I see

#### [Lyle Kopnicky (Apr 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131556):
Well, that helps. I have a lot more to learn about Lean. I've been working through *Logic & Proof*.

#### [Mario Carneiro (Apr 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131558):
Most type families are universe polymorphic like this, but if we restrict to `Type`, we have `list.{0} : Type -> Type : Type 1`

#### [Mario Carneiro (Apr 16 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131567):
Most things that you think of as kinds will have type `Type 1` if you replace `*` with lean's `Type` everywhere

#### [Lyle Kopnicky (Apr 16 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125131614):
Thanks!

#### [Kevin Buzzard (Apr 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions as Types/near/125138177):
```quote
In lean this is not necessary because it's fully dependent anyway. Haskell is getting closer and closer to dependent type theory as time goes on, but it's not there yet
```
I watched a talk by Edward Kmett on youtube recently -- "typeclasses against the world" (about Haskell and typeclasses) and, if I understood correctly, Kmett said at some point that a problem with typeclasses in DTT was that you get diamonds, and in Haskell these couldn't occur.

