---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74562sigmapsigma.html
---

## Stream: [new members](index.html)
### Topic: [sigma/psigma](74562sigmapsigma.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116492):
What's the reason for having types like sigma/psigma, sum/psum at the same time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116506):
Is it to do with universes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 03 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116556):
Like, when would I want to use psigma instead of sigma/Exists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116602):
psigma instead of Exists: because you want to keep the information of what the things are whose existence you claim

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116613):
psigma with a Prop is basically the same as subtype, whereas Exists is like nonempty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116617):
psigma instead of sigma: if you want to use a Prop instead of a Type, or you might want either a Prop or a Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116664):
The equation compiler uses `psigma` a lot. `| (a : nat) (b : nat) (h : 0 < b)` is essentially matching on `Σ' a b : ℕ, 0 < b` underneath.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116741):
I've found psigma most useful in conjunction with the `Σ'` binder notation with multiple variables where the eventual "body" is a Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116857):
isn't that exists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116861):
like "a pair consisting of an open set U and a function f : U -> R which sends x to 0" = `Σ' (u : set α) (hu : is_open u) (f : u → ℝ), f x = 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116878):
What's the point of using `sigma` instead of `psigma`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116924):
`psigma` has a difficult target universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116939):
`Sort (max u 1)` is hard to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116949):
because it's not algebraic: `max u 1 = 1` does not have a unique solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116960):
so lean will often give up on otherwise solvable universe unification problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116964):
where `Type u = Sort u+1` has the much easier solution `u+1 = 1 ->  u = 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117028):
In fact, there are some expressions which do not have any solution, although you might think it does: `max u 1 = v+1` has no solution for u

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117277):
hmm, that `max 1` is coming from Lean bumping up the level of a structure I guess? Is it actually wanted? Why should `psigma.{0 0}` not be a Prop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117417):
That was deliberate. You can define your own `psigma'` that lives in `Sort (max u v)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117429):
but you will find it's not all it's cracked up to be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117444):
in particular, it has a recursor like `exists`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117492):
it's not "data"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117639):
and if you specialize to `u > 0` you get the [`mystery` type](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/nearly.20no_confusion/near/124133073), which is neither proof nor data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117691):
```quote
In fact, there are some expressions which do not have any solution, although you might think it does: `max u 1 = v+1` has no solution for u
```
why does `max u 1 = v+1` not have any solutions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117726):
because there is no universe expression that gives the solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117727):
Actually, I can't :)
```lean
structure ppsigma {α : Sort u} (β : α → Sort v) : Sort (max u v) := mk :: (fst : α) (snd : β fst)
-- invalid universe polymorphic structure declaration, the resultant universe is not Prop (i.e., 0), but it may be Prop for some parameter values (solution: use 'l+1' or 'max 1 l')
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117736):
But I guess it's because otherwise I would be in the situation you describe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117799):
That's because you used `structure`, it tried and failed to define the projections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117845):
Oh, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117869):
Why doesn't singleton elimination help here?
If I manually replace `u = v = 0`, then I get an eliminator to any sort

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117873):
@**petercommand** for each fixed `v` there is a solution for `u`, but there is no solution function `u(v)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117929):
Just a weird edge case that Lean doesn't support?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117940):
because you need one recursor that is polymorphic in u,v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117970):
and that recursor will have one extra universe variable depending on whether `max u v = 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118003):
there is no way to do that with universe expressions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118073):
you could have two recursors, but this breaks parametricity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118109):
I'm trying out different `u` and `v` values and in every case I get an eliminator which goes to any sort.
However there is a difference when `u = v = 0`, which is that the `C` doesn't take the `ppsigma` value as an argument then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118122):
singleton elimination doesn't help because `A` and `B` aren't subsingletons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118185):
That's just a convenience thing, the usual recursor is at `drec_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118220):
for small eliminating props the dependent and nondependent recursors are interdefinable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118506):
```lean
inductive ppsigma00 {α : Sort 0} (β : α → Sort 0) : Sort (max 0 0) | m (fst : α) (snd : β fst) : ppsigma00
#check @ppsigma00.drec_on
│ ppsigma00.drec_on :
│   Π {α : Prop} {β : α → Prop} {C : ppsigma00 β → Sort u_1} (n : ppsigma00 β),
│     (Π (fst : α) (snd : β fst), C _) → C n

inductive ppsigma11 {α : Sort 1} (β : α → Sort 1) : Sort (max 1 1) | m (fst : α) (snd : β fst) : ppsigma11
#check @ppsigma11.rec_on
│ ppsigma11.rec_on :
│   Π {α : Type} {β : α → Type} {C : ppsigma11 β → Sort u_1} (n : ppsigma11 β),
│     (Π (fst : α) (snd : β fst), C (ppsigma11.m fst snd)) → C n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118544):
They look the same to me (especially with `set_option pp.proofs true`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118748):
I would maybe believe that the VM can't (easily) implement such a thing, though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118764):
`rec_on` is an axiom, right? Or one of the related things is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120246):
`rec_on` is `rec` with the arguments in a different order. `rec` is an axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120259):
to be pedantic, it's an axiom schema

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120303):
What's an axiom schema?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120315):
it isn't one single axiom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120317):
it's one axiom per inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120323):
Right, I meant `[whatever].rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Nov 05 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146795757):
```quote
In fact, there are some expressions which do not have any solution, although you might think it does: `max u 1 = v+1` has no solution for u
```
I'm confused. Lean doesn't know that `max (v+1) 1 = v+1`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Nov 05 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146795876):
I presume you misspoke, and meant that there is no solution for `v`? (I agree with that.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146796140):
oh, yes you are right


{% endraw %}
