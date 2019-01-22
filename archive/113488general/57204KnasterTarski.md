---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57204KnasterTarski.html
---

## [general](index.html)
### [Knaster-Tarski](57204KnasterTarski.html)

#### [Kenny Lau (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351778):
https://github.com/kckennylau/Lean/blob/master/Knaster-Tarski.lean
@**Mario Carneiro** por favor diz que nao fazias isso

#### [Kenny Lau (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351819):
pooh favoh jeez ki now fazeeaish eesoo

#### [Kenny Lau (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124351820):
(that's how I pronounce it)

#### [Kenny Lau (Mar 29 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352028):
@**Kevin Buzzard** if you're interested

#### [Kenny Lau (Mar 29 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352029):
it's related to the link I pm'ed you

#### [Mario Carneiro (Mar 29 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352073):
Actually I'm a bit surprised it's not there

#### [Kenny Lau (Mar 29 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352074):
bom!

#### [Mario Carneiro (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352082):
I'm certain there's something like it somewhere, but maybe it's not stated on complete lattices

#### [Kenny Lau (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352084):
I thought it's a theorem of complete lattices

#### [Mario Carneiro (Mar 29 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352085):
There is a `lfp` function in ordinal with a similar proof attached

#### [Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352126):
nice

#### [Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352127):
that's the theorem about normal ordinal functions right

#### [Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352131):
does it have a name?

#### [Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352132):
maybe you can prove your `lfp` using this :D

#### [Kenny Lau (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352134):
nvm it isn't a complete lattice

#### [Mario Carneiro (Mar 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352135):
`is_normal.nfp_fp` is what I was thinking of

#### [Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352141):
Dunno, it's not a complete lattice

#### [Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352143):
interesting

#### [Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352144):
Maybe that means there's a hidden abstraction?

#### [Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352147):
well to be fair

#### [Mario Carneiro (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352149):
like a sup-continuous monotone function

#### [Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352151):
your set is well-ordered

#### [Kenny Lau (Mar 29 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352152):
hmm

#### [Kenny Lau (Mar 29 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352196):
but my function isn't sup-continuous

#### [Mario Carneiro (Mar 29 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352209):
Are you sure? Seems like it follows from the assumptions

#### [Mario Carneiro (Mar 29 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352257):
Anyway, I think this is why it isn't abstracted :)

#### [Kenny Lau (Mar 29 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352258):
look at my aux 3

#### [Mario Carneiro (Mar 29 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352320):
Why do `next` and `previous` take an unused proof argument?

#### [Mario Carneiro (Mar 29 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352371):
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?

#### [Mario Carneiro (Mar 29 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352372):
Then you could skip the `subtype.val ''` part

#### [Kenny Lau (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352417):
then how can I use it

#### [Kenny Lau (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352420):
```quote
Why do `next` and `previous` take an unused proof argument?
```
fixed

#### [Mario Carneiro (Mar 29 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352423):
For the big ol `complete_lattice` proof, I don't think that's the claim you want. Rather, `fixed_points f` is a complete sublattice of the powerset

#### [Kenny Lau (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352463):
sublattice?

#### [Mario Carneiro (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352465):
and then you have that construction generally for all sublattices

#### [Kenny Lau (Mar 29 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352466):
I'm not aware of the existence of sublattices in Lean?

#### [Mario Carneiro (Mar 29 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352473):
I don't think they exist

#### [Mario Carneiro (Mar 29 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352482):
But you could just skip the complete_lattice construction and just prove that the sup of fixed points is a fixed point

#### [Kenny Lau (Mar 29 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352530):
```quote
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?
```
nope, unprovable

#### [Kenny Lau (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352533):
wait, misinterpreted

#### [Kenny Lau (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352537):
```quote
But you could just skip the complete_lattice construction and just prove that the sup of fixed points is a fixed point
```
they aren't

#### [Mario Carneiro (Mar 29 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352545):
oh, I see, you need that `next` thing in the middle

#### [Mario Carneiro (Mar 29 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352585):
Hm, it's something like a retract from `set A` to `fixed_points f`

#### [Mario Carneiro (Mar 29 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352591):
It still strikes me as a generic construction

#### [Kenny Lau (Mar 29 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352638):
https://github.com/kckennylau/Lean/blob/master/Knaster-Tarski.lean

#### [Kenny Lau (Mar 29 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352645):
```quote
Wouldn't it be nicer to state `aux3` for subsets of `fixed_points f` rather than sets in the subtype?
```
done. compare aux3 and aux4. aux4 has not been changed. which one is better?

#### [Mario Carneiro (Mar 29 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352756):
`Sup (f '' A)` is also expressible as an indexed sup, `⨆ x ∈ A, f x`

#### [Kenny Lau (Mar 29 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124352871):
oh

#### [Kenny Lau (Mar 29 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353364):
@**Mario Carneiro** so what is the verdict?

#### [Mario Carneiro (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353373):
I prefer aux3 since it is more likely to be used as a lemma

#### [Kenny Lau (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353374):
and in general?

#### [Kenny Lau (Mar 29 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353375):
do you find ways of abstracting Knaster-Tarski?

#### [Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353414):
Not anything obvious

#### [Kenny Lau (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353416):
and is it worth pushing?

#### [Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353417):
I wonder if it works in conditionally complete lattices

#### [Mario Carneiro (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353418):
yes, PR it

#### [Kenny Lau (Mar 29 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353419):
what is cc lattices?

#### [Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353420):
@**Johannes Hölzl** should also weigh in, he's more involved in complete lattice theory than me

#### [Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353427):
real numbers, basically

#### [Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353428):
sup of nonempty bounded sets

#### [Kenny Lau (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353429):
bot uses top, top uses bot

#### [Mario Carneiro (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353432):
?

#### [Kenny Lau (Mar 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353433):
I think they can do without each other then

#### [Kenny Lau (Mar 29 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353475):
the least fixed point is from the top element of the original lattice

#### [Kenny Lau (Mar 29 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353478):
f(x)=x+1 has no fixed points

#### [Mario Carneiro (Mar 29 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353489):
sounds legit

#### [Kenny Lau (Mar 29 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353495):
[0,infty) is downward complete right

#### [Kenny Lau (Mar 29 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353536):
same example applies

#### [Kenny Lau (Mar 29 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353642):
[0,1] is complete right

#### [Mario Carneiro (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353655):
yes

#### [Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353658):
hmm

#### [Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353661):
you don’t even need continuity

#### [Mario Carneiro (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353663):
wait, doesn't that imply banach's fp theorem in 1D?

#### [Kenny Lau (Mar 29 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353665):
😮

#### [Kenny Lau (Mar 29 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124353708):
maths is beautiful

#### [Kenny Lau (Mar 29 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124354180):
https://github.com/leanprover/mathlib/pull/88

#### [Johannes Hölzl (Mar 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355353):
There is already `order/fixed_points.lean` in mathlib. It contains `lattice.lfp` and `lattice.gfp` to compute the least and greatest fixed point of a function. For conditionally complete lattices: we could add a subtype instance for intervals on conditionally complete lattices. Then  $$[0, 1] : \mathbb{R}$$ would be a complete lattice.

#### [Kenny Lau (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355402):
fair enough

#### [Johannes Hölzl (Mar 29 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355578):
Your `next` and `previous` function can be represented using the `gfp` and `lfp`: e.g. `gfp (λz, x ⊔ f z) = Sup {z | z ≤ x ⊔ f z}`. Then you can use the lfp and gfp properties.

#### [Kenny Lau (Mar 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355580):
so you're just going to close my PR?

#### [Johannes Hölzl (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355626):
No, I don't want to close it. I would like to see the fixed point lattice in `order/fixed_points.lean`. And using the constants and proofs we already have.

#### [Kenny Lau (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355628):
oh ok

#### [Kenny Lau (Mar 29 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355629):
are you going to edit it or am I going to edit it?

#### [Johannes Hölzl (Mar 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124355684):
Of course, if you want you can edit it! I have a couple more changes: rename `aux1..4` to something useful and replace `is_ord_hom` by the assumption `monotone f`, also going from type class to just assumption.

#### [Kenny Lau (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358216):
how would you rename `aux1..4`? @**Johannes Hölzl**

#### [Johannes Hölzl (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358372):
something like `sup_le_f_sup_of_fixed_points`?

#### [Kenny Lau (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358375):
ach fur gottesliebe

#### [Kenny Lau (Mar 29 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358377):
that's 10 times as long

#### [Kevin Buzzard (Mar 29 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358387):
and more descriptive too ;-)

#### [Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358437):
do you use `f` in names?

#### [Kevin Buzzard (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358438):
Wait -- aren't you and I editing some schemes files with function names like `structure_sheaf_of_rings_on_affine_scheme` ?

#### [Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358439):
my mind replaces `f` with `apply` in names

#### [Kenny Lau (Mar 29 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358442):
yes, and it's always you who type it :P

#### [Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358452):
`definition  structure_sheaf_of_rings_on_affine_scheme (R : Type*) [comm_ring R] : is_sheaf_of_rings (structure_presheaf_of_rings_on_affine_scheme R) :=...` :-)

#### [Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358453):
well Mario told me I couldn't use `tag00EJ`...

#### [Kenny Lau (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358454):
I never typed it :P

#### [Kevin Buzzard (Mar 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358459):
Perhaps `tag00EJ` is as bad as `aux1` right? ;-)

#### [Kenny Lau (Mar 29 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Knaster-Tarski/near/124358499):
right

