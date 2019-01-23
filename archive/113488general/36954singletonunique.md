---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36954singletonunique.html
---

## Stream: [general](index.html)
### Topic: [singleton / unique](36954singletonunique.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156348116):
It has been remarked before that we need a class that is `nonempty` + `subsingleton`. I guess the canonical name would be `singleton`. How would people want to define it?
```lean
class singleton (X : Type u) :=
(elem : X)
(uniq : \Pi (x,y : X), x = y)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jan 18 2019 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156348829):
why not just take nonempty and subsingleton as assumptions together?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349297):
I guess there are two options: either we make an inductive `Prop`, or we make a thing that lives in `Type*` but has an easy projector to the element.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349300):
I'm not sure what is best.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349909):
@**Johannes Hölzl** There is probably common wisdom on this in the wider community. What would you suggest?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349975):
Hm, this is a case which is not often used. But I would guess the `Type*` variant could be more helpful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349979):
It is not? Ooh, that surprises me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349989):
Up to now we didn't need it in mathlib...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350044):
Where would you put it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350048):
Somewhere in `data/`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350123):
Maybe even in `logic/basic.lean`? Plus the `unit` instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350136):
Is it ok to extend `inhabited`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350138):
Or is that wrong for semantic reasons?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350189):
I still don't know the semantics of all those types like `inhabited`, `default`, etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350275):
Yes, extend `inhabited` and derive `subsingleton`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351117):
Ooop :see_no_evil: the name `singleton` is of course already taken by singleton sets...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351184):
@**Kenny Lau** Do you have a good suggestion for a name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 18 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351186):
nope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351566):
Aahrg, `punit.inhabited` is only for `Type`, not `Type u`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351834):
I guess the name `contractible` is to HoTT, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 18 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351888):
Maybe `unique`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351908):
Yes, that might work. But I'dd like to also emphasise the existence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351921):
People might think that `unique` is a variant on `subsingleton`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352558):
#605 @**Johannes Hölzl**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352717):
what's wrong with just `inhabited` + `subsingleton` or `nonempty` + `subsingleton`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352733):
That it's longer to write?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352740):
not good enough, definitions are worth more than that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352747):
When I'm pulling a limit cone through and adjoint functor I want to spend as little time with these stupid classes...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352802):
aha, okay sure I've seen this. Are you perhaps saying this about a subtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352805):
No...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352807):
Why do you think that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352821):
That's the way it usually goes with universal properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352831):
there exists a unique map satisfying such and such property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352835):
Ok, maybe. I haven't thought of it like that. But there are no subtypes in sight with what I'm doing right now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352839):
Aah, but that's all packaged into `cone_morphism`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352901):
I want to say that `c` is a limit cone if `\Pi t, unique (cone_morphism c t)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352910):
why not say that in two conditions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352916):
you have a morphism and a proof of uniqueness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352918):
And then adjunctions give me `equiv`s, and `equiv.unique_of_equiv` will let me easily manipulate it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352929):
It's too unbundled.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352935):
I agree that that is also useful. And it is what we have right now in the library.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352937):
It's good when you are applying these things in concrete cases.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352990):
But for abstract category theory, I think it becomes a lot easier to manipulate these things when they are bundled.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353025):
I take it you don't want to use this like a typeclass then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353084):
Uuuh, I don't know?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353100):
what does `equiv.unique_of_equiv` say?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353116):
If `X \equiv Y` and you know `unique Y` then you get `unique X`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353117):
But you knew that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353119):
You want code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353124):
and that's all you intend to do with `unique`, besides using the projections directly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353126):
https://github.com/leanprover/mathlib/pull/605/files#diff-a714d761eac2ec5a2e4b0ed4592f9c46R474

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353185):
Eehm, yes, for the time being.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353191):
By the way, you can define `unique` in a simpler way, with only one quantifier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353197):
there is `x : A` and `\forall y, x = y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353208):
Yes, I've derived those versions. But I wanted to be as symmetric as possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353214):
Or is that not useful?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353269):
For the structure you want the axiom to be easy to prove. Probably when one picks a default it will be easy to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353286):
like how one shows a zero ring is `unique`, you show every element is 0, and hence every element is equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353291):
saves you a step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353310):
Ok, fine. I'll rewrite that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353313):
besides, the two quantifier version is available as `subsingleton.eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353468):
Ok, sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353487):
I don't have any better suggestions for the name than `unique`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353504):
but I think it might be usable as a regular type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353638):
Ok, so `structure` instead of `class`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353676):
maybe a `class` on some days? If you use `attribute [class] unique` after the definition you can use it as a class when you feel like it but the projections won't have inst implicit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353700):
Aah, maybe that helps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353753):
I guess I should make some simp-lemmas. And then hopefully `tidy` can work with this nicely.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353770):
Here are some interesting facts: `subsingleton (unique A)`, and `unique (unique A) <-> unique A`, `unique A -> unique B` if `f : A -> B` is a surjection (not required to be a bijection)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353798):
Yep... would you like all of those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353802):
if you are going to define a thing you should prove all the basic theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353873):
Where should those go?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353875):
`logic/basic`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353945):
how about `logic/unique` unless there is a reason to merge it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353950):
I don't think there are currently any new definitions in `logic/basic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353964):
but `logic/basic` probably needs a refactor, it's a bit of a grab bag

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353971):
it literally has a `miscellaneous` section, that's never a good sign

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354031):
Ok, I can start `logic/unique`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354050):
If I do the `attribute [class]` thing, and I assume `[unique X]` then it still doesn't infer `inhabited X`. So I have to state those inferences by hand?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354355):
@**Mario Carneiro** Should I include simp-lemmas like this?
```lean
instance : inhabited α := to_inhabited ‹unique α›

@[simp] lemma eq_default (a : α) : a = default α := uniq _ a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354405):
you have to mark `unique.to_inhabited` as `instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354416):
`eq_default` won't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354429):
neither will `default_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354443):
Why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354515):
It would be cool if `simp` would just simplify every element to the default.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354520):
simp lemmas with a variable on the left trigger on anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354529):
at least that's what lean says; I don't see why that's a problem but it's explicitly rejected by `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354548):
Aah, and simp doesn't know yet if the `unique X` instance will be found or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354584):
well, it could just try to apply it on every term... you know I think this is a bad idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354647):
```quote
you have to mark `unique.to_inhabited` as `instance`
```
 Like so: `attribute [instance] unique.to_inhabited`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354650):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354671):
But then
```lean

variables {α : Sort u} [unique α]

instance : inhabited α := by apply_instance
```
still fails.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156355179):
oh, I guess that's because the `unique` is explicit in `unique.to_inhabited`. So you will have to make an instance like you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156356937):
@**Mario Carneiro** Should the following be done with instances or not?
```lean
def of_surjective (f : α → β) (hf : surjective f) (h : inhabited α) : inhabited β :=
{ default := f h.default }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357666):
`hf` is not required...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357745):
Lol... I've been thinking too much about `unique` :grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357779):
@**Johannes Hölzl** @**Mario Carneiro** I pushed an update to #605

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156358134):
Woops, forgot to `git add` the new file.

