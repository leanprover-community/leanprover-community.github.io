---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57204KnasterTarski.html
---

## Stream: [general](index.html)
### Topic: [Knaster-Tarski](57204KnasterTarski.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351778):
https://github.com/kckennylau/Lean/blob/master/Knaster-Tarski.lean
@**Mario Carneiro** por favor diz que nao fazias isso

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351819):
pooh favoh jeez ki now fazeeaish eesoo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351820):
(that's how I pronounce it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352028):
@**Kevin Buzzard** if you're interested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352029):
it's related to the link I pm'ed you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352073):
Actually I'm a bit surprised it's not there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352074):
bom!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352082):
I'm certain there's something like it somewhere, but maybe it's not stated on complete lattices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352084):
I thought it's a theorem of complete lattices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352085):
There is a `lfp` function in ordinal with a similar proof attached

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352126):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352127):
that's the theorem about normal ordinal functions right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352131):
does it have a name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352132):
maybe you can prove your `lfp` using this :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352134):
nvm it isn't a complete lattice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352135):
`is_normal.nfp_fp` is what I was thinking of

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352141):
Dunno, it's not a complete lattice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352143):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352144):
Maybe that means there's a hidden abstraction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352147):
well to be fair

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352149):
like a sup-continuous monotone function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352151):
your set is well-ordered

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352152):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352196):
but my function isn't sup-continuous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352209):
Are you sure? Seems like it follows from the assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352257):
Anyway, I think this is why it isn't abstracted :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352258):
look at my aux 3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352320):
Why do `next` and `previous` take an unused proof argument?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352371):
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352372):
Then you could skip the `subtype.val ''` part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352417):
then how can I use it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352420):
```quote
Why do `next` and `previous` take an unused proof argument?
```
fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352423):
For the big ol `complete_lattice` proof, I don't think that's the claim you want. Rather, `fixed_points f` is a complete sublattice of the powerset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352463):
sublattice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352465):
and then you have that construction generally for all sublattices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352466):
I'm not aware of the existence of sublattices in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352473):
I don't think they exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352482):
But you could just skip the complete_lattice construction and just prove that the sup of fixed points is a fixed point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352530):
```quote
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?
```
nope, unprovable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352533):
wait, misinterpreted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352537):
```quote
But you could just skip the complete_lattice construction and just prove that the sup of fixed points is a fixed point
```
they aren't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352545):
oh, I see, you need that `next` thing in the middle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352585):
Hm, it's something like a retract from `set A` to `fixed_points f`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352591):
It still strikes me as a generic construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352638):
https://github.com/kckennylau/Lean/blob/master/Knaster-Tarski.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352645):
```quote
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?
```
done. compare aux3 and aux4. aux4 has not been changed. which one is better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352756):
`Sup (f '' A)` is also expressible as an indexed sup, `⨆ x ∈ A, f x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352871):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353364):
@**Mario Carneiro** so what is the verdict?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353373):
I prefer aux3 since it is more likely to be used as a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353374):
and in general?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353375):
do you find ways of abstracting Knaster-Tarski?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353414):
Not anything obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353416):
and is it worth pushing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353417):
I wonder if it works in conditionally complete lattices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353418):
yes, PR it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353419):
what is cc lattices?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353420):
@**Johannes Hölzl** should also weigh in, he's more involved in complete lattice theory than me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353427):
real numbers, basically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353428):
sup of nonempty bounded sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353429):
bot uses top, top uses bot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353432):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353433):
I think they can do without each other then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353475):
the least fixed point is from the top element of the original lattice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353478):
f(x)=x+1 has no fixed points

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353489):
sounds legit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353495):
[0,infty) is downward complete right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353536):
same example applies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353642):
[0,1] is complete right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353655):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353658):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353661):
you don’t even need continuity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353663):
wait, doesn't that imply banach's fp theorem in 1D?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353665):
😮

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353708):
maths is beautiful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124354180):
https://github.com/leanprover/mathlib/pull/88

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355353):
There is already `order/fixed_points.lean` in mathlib. It contains `lattice.lfp` and `lattice.gfp` to compute the least and greatest fixed point of a function. For conditionally complete lattices: we could add a subtype instance for intervals on conditionally complete lattices. Then  $$[0, 1] : \mathbb{R}$$ would be a complete lattice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355402):
fair enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355578):
Your `next` and `previous` function can be represented using the `gfp` and `lfp`: e.g. `gfp (λz, x ⊔ f z) = Sup {z | z ≤ x ⊔ f z}`. Then you can use the lfp and gfp properties.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355580):
so you're just going to close my PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355626):
No, I don't want to close it. I would like to see the fixed point lattice in `order/fixed_points.lean`. And using the constants and proofs we already have.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355628):
oh ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355629):
are you going to edit it or am I going to edit it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355684):
Of course, if you want you can edit it! I have a couple more changes: rename `aux1..4` to something useful and replace `is_ord_hom` by the assumption `monotone f`, also going from type class to just assumption.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358216):
how would you rename `aux1..4`? @**Johannes Hölzl**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358372):
something like `sup_le_f_sup_of_fixed_points`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358375):
ach fur gottesliebe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358377):
that's 10 times as long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358387):
and more descriptive too ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358437):
do you use `f` in names?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358438):
Wait -- aren't you and I editing some schemes files with function names like `structure_sheaf_of_rings_on_affine_scheme` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358439):
my mind replaces `f` with `apply` in names

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358442):
yes, and it's always you who type it :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358452):
`definition  structure_sheaf_of_rings_on_affine_scheme (R : Type*) [comm_ring R] : is_sheaf_of_rings (structure_presheaf_of_rings_on_affine_scheme R) :=...` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358453):
well Mario told me I couldn't use `tag00EJ`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358454):
I never typed it :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358459):
Perhaps `tag00EJ` is as bad as `aux1` right? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358499):
right

