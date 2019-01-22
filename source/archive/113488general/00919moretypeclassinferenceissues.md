---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00919moretypeclassinferenceissues.html
---

## [general](index.html)
### [more type class inference issues](00919moretypeclassinferenceissues.html)

#### [Kevin Buzzard (Apr 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320059):
It seems to me that for classes like `ring`defined in core lean or mathlib, you are kind of supposed to use type class inference to make them work.

#### [Kevin Buzzard (Apr 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320070):
For example, `class is_ring_hom {α : Type u} {β : Type v} [ring α] [ring β] (f : α → β) : Prop := ...` is now in mathlib

#### [Kevin Buzzard (Apr 19 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320128):
now I don't actually know how to make type class inference work in all cases, so I spend some of my time working around it.

#### [Kevin Buzzard (Apr 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320162):
Here's an example. I have the following structure in my code:

#### [Kevin Buzzard (Apr 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320181):
```lean
structure presheaf_of_rings (α : Type*) [T : topological_space α] extends presheaf_of_types α :=
(Fring : ∀ {U} (OU : T.is_open U), comm_ring (F OU))
(res_is_ring_morphism : ∀ (U V : set α) (OU : T.is_open U) (OV : T.is_open V) (H : V ⊆ U),
  is_ring_hom (res U V OU OV H))
```

#### [Kevin Buzzard (Apr 19 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320267):
Yesterday, `is_ring_hom` was about `comm_ring`, and I used it in my code via `@is_ring_hom _ _ (FPR.Fring HU) (GPR.Fring HU) ...`, explicitly giving the proof that something was a comm_ring.

#### [Kevin Buzzard (Apr 19 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320275):
But now it's changed to ring and so either I figure out a way of explicitly turning a comm_ring into a ring

#### [Kevin Buzzard (Apr 19 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320318):
or I ask here about how I should be doing this properly.

#### [Kevin Buzzard (Apr 19 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320334):
In short, Lean / mathlib seems to want me, by default, to prove that things are rings by type class inference.

#### [Kevin Buzzard (Apr 19 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320369):
How do I ensure that every time I access a `presheaf_of_rings` as defined above, `presheaf_of_rings.Fring` is added to the type class inference system?

#### [Kevin Buzzard (Apr 19 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320463):
Is there some clever trick involving an `instance` statement directly after the definition of `presheaf_of_rings`?

#### [Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320625):
Oh yeah :-)

#### [Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320629):
```lean
instance presheaf_of_rings_Fring (α : Type*) [T : topological_space α] {U : set α} (FPR : presheaf_of_rings α) (OU : T.is_open U) : comm_ring (FPR.F OU) :=
FPR.Fring OU
```

#### [Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320631):
As you were :-)

#### [Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322233):
What does this mean?

#### [Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322237):
```lean
structure presheaf_of_rings (α : Type*) [T : topological_space α] extends presheaf_of_types α :=
[Fring : ∀ {U} (OU : T.is_open U), comm_ring (F OU)]
(res_is_ring_morphism : ∀ (U V : set α) (OU : T.is_open U) (OV : T.is_open V) (H : V ⊆ U),
  is_ring_hom (res U V OU OV H))
```

#### [Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322241):
Is that a thing? It doesn't seem to be a thing.

#### [Chris Hughes (Apr 19 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322275):
`comm_ring.to_ring` might help

#### [Chris Hughes (Apr 19 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322379):
`attribute [instance] presheaf_of_rings.Fring` might also help

#### [Chris Hughes (Apr 19 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322454):
Just add that ^ line after the definition of `presheaf_of_rings`

#### [Kevin Buzzard (Apr 19 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125323095):
Oh that's a better way :-) Thanks Chris, I'm glad I asked now.

#### [Kevin Buzzard (Apr 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125323244):
I specifically wanted to avoid `comm_ring.to_ring` as I am pretty sure that the whole point of type class inference is that the end user shouldn't have to use such functions.

#### [Kevin Buzzard (Apr 19 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324599):
Actually, is the following a potential problem with the type class system:

#### [Kevin Buzzard (Apr 19 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324670):
My understanding (incomplete) of something Johannes was saying a few days ago to Patrick, was that the reason `topological_space` is defined as a `structure` with the `class` attribute added later, rather than a `class` directly, was that there were occasions when you might want to consider more than one topological space structure on a given type.

#### [Kevin Buzzard (Apr 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324680):
but ring is defined as a class in core lean

#### [Kevin Buzzard (Apr 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324721):
so what about the person who wants to prove theorems about putting different ring structures on a type?

#### [Kevin Buzzard (Apr 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324728):
Are they forced to abandon the type class system, and then they really would have to learn the names of all the theorems mapping a ring to an additive group etc?

#### [Kevin Buzzard (Apr 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324903):
And here's another question: what if the ring instance is in the same structure?

#### [Kevin Buzzard (Apr 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324906):
```lean
structure presheaf_of_rings_on_basis {X : Type u} [TX : topological_space X] 
  {B : set (set X)} (HB : topological_space.is_topological_basis B) extends presheaf_of_types_on_basis HB :=
(Fring : ∀ {U} BU, comm_ring (F BU))
(res_is_ring_morphism : ∀ {U V} (BU : U ∈ B) (BV : V ∈ B) (H : V ⊆ U),
  @is_ring_hom _ _ (@Fring U BU) (Fring BV) (@res U V BU BV H))
```

#### [Kevin Buzzard (Apr 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324987):
Here a `presheaf_of_rings_on_basis` has `Fring` saying something is a commutative ring, and then `res_is_ring_morphism` which immediately wants to use type class inference to deduce that `Fring U BU` is a ring. Now do I really have to use `comm_ring.to_ring`?

#### [Kevin Buzzard (Apr 19 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325099):
```lean
structure presheaf_of_rings_on_basis {X : Type u} [TX : topological_space X] 
  {B : set (set X)} (HB : topological_space.is_topological_basis B) extends presheaf_of_types_on_basis HB :=
(Fring : ∀ {U} (BU : U ∈ B), comm_ring (F BU))
(res_is_ring_morphism : ∀ {U V} (BU : U ∈ B) (BV : V ∈ B) (H : V ⊆ U),
  @is_ring_hom _ _ (@comm_ring.to_ring _ (Fring BU)) (@comm_ring.to_ring _ (Fring BV)) (@res U V BU BV H))
```

#### [Kevin Buzzard (Apr 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325160):
Type class inference is failing me badly here. Sorry for no MWE, hopefully people can see the problem; Lean wants me to use type class inference to prove that commutative rings are rings but I don't know how to make this happen in this situation.

#### [Mario Carneiro (Apr 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325164):
that's what the brackets inside the structure are for

#### [Kevin Buzzard (Apr 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325231):
?

#### [Kevin Buzzard (Apr 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325233):
Oh!

#### [Kevin Buzzard (Apr 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325247):
:-)

#### [Kevin Buzzard (Apr 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325251):
```lean
structure presheaf_of_rings_on_basis {X : Type u} [TX : topological_space X] 
  {B : set (set X)} (HB : topological_space.is_topological_basis B) extends presheaf_of_types_on_basis HB :=
[Fring : ∀ {U} (BU : U ∈ B), comm_ring (F BU)]
(res_is_ring_morphism : ∀ {U V} (BU : U ∈ B) (BV : V ∈ B) (H : V ⊆ U),
  is_ring_hom (@res U V BU BV H))
```

#### [Kevin Buzzard (Apr 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325270):
So just to be clear -- the square brackets inside the structure trigger type class inference only within the structure definitions?

#### [Mario Carneiro (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325325):
I think they also mark it as an instance, but you should `#print` to be sure

#### [Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325334):
I don't think they do

#### [Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325344):
because that was what prompted the question about why the square brackets within the structure definition was even a thing

#### [Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325345):
earlier

#### [Mario Carneiro (Apr 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325421):
you shouldn't need `@res` either

#### [Kevin Buzzard (Apr 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325481):
yes, that's gone now

#### [Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325517):
But your change of is_ring_hom from [comm_ring] to [ring] has thrown up one final type class inference issue which I can't solve

#### [Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325520):
possibly because it's not solvable

#### [Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325528):
I think I do need an MWE for this one

#### [Kevin Buzzard (Apr 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325814):
Oh no it's Ok, indeed I am now pretty convinced that the square brackets in the structure definition do not insert anything into the type class inference system globally

#### [Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325890):
because my final problem was solved by Chris' instance trick.

#### [Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325902):
Oh this is great. I got stuck on these problems before and blamed it on the type class inference system not being smart enough.

#### [Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325907):
I should have asked for help earlier.

#### [Kevin Buzzard (Apr 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325924):
Patrick said the same thing -- I told him to give up on coercions because they weren't smart enough

#### [Kevin Buzzard (Apr 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325932):
and he pointed out that whenever he'd got stuck before, you (Mario) had had a trick which got him through.

#### [Kevin Buzzard (Apr 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326155):
Here's a weird question. It feels to me like `comm_ring.to_ring` should not be the kind of function which end users have to worry about, because when the devs made `ring` a typeclass they are somehow declaring that Lean will automatically take care of inferences of this nature.

#### [Kevin Buzzard (Apr 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326166):
Am I right in thinking that an end user should only have to invoke `comm_ring.to_ring` in exceptional circumstances?

#### [Kevin Buzzard (Apr 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326183):
(says the person who just managed to avoid all uses of it when his code broke in lots of places)

#### [Kevin Buzzard (Apr 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326192):
(when a comm_ring changed to a ring)

#### [Kevin Buzzard (Apr 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326297):
Aah, more generally should an end user never have to explicitly invoke any theorem tagged with the `instance` attribute?

#### [Kevin Buzzard (Apr 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326358):
(unless they are putting more than one structure of a typeclass onto one type, say)

#### [Chris Hughes (Apr 20 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328614):
Sorry to hijack your thread, but I have a typeclass issue of my own
```lean
import data.int.modeq

instance Zmod_setoid {n : ℤ} : setoid ℤ := 
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

def Zmod (n : ℤ) : Type := quotient (@Zmod_setoid n)

private def add_aux {n : ℤ} (a b : Zmod n) : Zmod n := 
quotient.lift_on₂ a b (λ a b, ⟦a + b⟧) sorry
```
It cannot infer the `setoid` instance, probably because it requires an argument. Not sure of a good solution to this.

#### [Mario Carneiro (Apr 20 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328872):
This is a common problem; I think the `lift_on` recursor does not correctly deliver the expected type to the lambda. The usual solution is to add an ascription at the lambda:
```
private def add_aux {n : ℤ} (a b : Zmod n) : Zmod n :=
quotient.lift_on₂ a b (λ a b, (⟦a + b⟧ : Zmod n)) sorry
```

#### [Chris Hughes (Apr 20 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328985):
Still not working I'm getting this message
```
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  Zmod_setoid n
```

#### [Kevin Buzzard (Apr 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331043):
```lean
import data.int.modeq

instance Zmod_setoid {n : ℤ} : setoid ℤ :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

example : setoid ℤ := by apply_instance -- fails
```

#### [Kevin Buzzard (Apr 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331049):
I'm not sure that I understand how parametrized instances work.

#### [Kevin Buzzard (Apr 20 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331179):
```lean
import data.int.modeq

instance Zmod_setoid {n : ℤ} : setoid ℤ :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

def Zmod (n : ℤ) : Type := quotient (@Zmod_setoid n)

#check (⟦3⟧ : Zmod 5) -- failed to synthesize type class instance for setoid ℤ
```

#### [Kevin Buzzard (Apr 20 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331180):
I'm even less sure now

#### [Kevin Buzzard (Apr 20 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331268):
`#check (⟦(3 : ℤ)⟧ : Zmod 5` gives

#### [Kevin Buzzard (Apr 20 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331299):
`⁇ : Zmod 5` for information check result (in green)

#### [Kevin Buzzard (Apr 20 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331303):
and fails to synthesize the instance

#### [Simon Hudon (Apr 20 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331410):
Try:

```
import data.int.modeq

@[reducible]
def Zmod (n : ℤ) : Type := ℤ 

instance Zmod_setoid {n : ℤ} : setoid (Zmod n) :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

example {n : ℤ} : setoid (Zmod n) := by apply_instance

#check ⟦ (3 : Zmod 5) ⟧ 
```

#### [Simon Hudon (Apr 20 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331465):
The problem is that instance inference is only working with `ℤ` (in your example) to find a setoid instance. It's not enough information to infer the `n` parameter. Now, I added a synonym for `ℤ` which provides that information.

#### [Kevin Buzzard (Apr 20 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331928):
```lean
import data.int.modeq

@[reducible]
def Z_aux (n : ℤ) : Type := ℤ

instance Zmod_setoid {n : ℤ} : setoid (Z_aux n) :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

example {n : ℤ} : setoid (Z_aux n) := by apply_instance

def Zmod (n : ℤ) : Type := quotient (@Zmod_setoid n)

#check (⟦ 3 ⟧ : Zmod 5) -- 3 is interpreted as being in Z_aux 5 and this works

private def add_aux {n : ℤ} (a b : Zmod n) : Zmod n :=
quotient.lift_on₂ a b (λ a b, (⟦a + b⟧ : Zmod n)) sorry -- no error yet
```

#### [Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331934):
As a mathematician I'm a bit uneasy about having a thing which is Z but which is called Zmod n

#### [Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331935):
so I renamed it Z_aux, but your trick is excellent all the same :-)

#### [Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331939):
I was worried the check would fail because Lean wouldn't push 3 into Z_aux 5

#### [Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332001):
`setoid` is a class and this is in core lean.

#### [Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332004):
I think this means that it's quite hard to have more than one instance of a setoid structure on a given type

#### [Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332006):
Simon's trick shows how to get around this, by making lots of types, one for each structure

#### [Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332009):
it's evil :-)

#### [Simon Hudon (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332056):
In general, if you need more than one instance of a class for a given type, it should make you suspicious

#### [Mario Carneiro (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332058):
it's also a good way to handle the multiple rings problem

#### [Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332059):
yes

#### [Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332060):
I don't think I'd seen it before

#### [Simon Hudon (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332061):
But you can also name the quotient instead of `Z`:

#### [Simon Hudon (Apr 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332069):
```lean
instance Zmod_setoid (n : ℤ) : setoid (Zmod n) :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

def Zmod' (n : ℤ) : Type := quotient (Zmod_setoid n)

#check (⟦ 3 ⟧ : Zmod' 5)
```

#### [Simon Hudon (Apr 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332072):
And if you equip `Zmod' 5` with `has_one`, `has_zero` and `has_add`, `#check (3 : Zmod' 5)` should work

#### [Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332189):
```lean
variables (Y : Type) [has_add Y] [has_one Y]
#check (3 : Y)
```

#### [Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332191):
no need for zero ;-)

#### [Simon Hudon (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332193):
Even better!

#### [Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332195):
sort of...

#### [Kevin Buzzard (Apr 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332198):
:-)

#### [Simon Hudon (Apr 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332241):
```quote
Simon's trick shows how to get around this, by making lots of types, one for each structure

it's evil :-)
```

I disagree. If you want the structure to be inferred implicitly, the information must be somewhere. The alternative is to have a different `+` / `*` operator for each one of those structures: `+_mod_5` / `*_mod_5`. That would be ugly and evil!

#### [Kevin Buzzard (Apr 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332255):
If setoid were a structure rather than a class, do you think Chris' code would be OK?

#### [Kevin Buzzard (Apr 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332260):
The quotient knows the equivalence relation, and the information distinguishing the quotient types is in the equivalence relation

#### [Kevin Buzzard (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332359):
`variables (Y : Type) [has_add Y] [has_one Y]`

#### [Kevin Buzzard (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332360):
I think I just defined the positive integers :-)

#### [Simon Hudon (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332361):
Yeah I think that would be good. Maybe rather than making `setoid` a structure, just make `Zmod_setoid` into a definition because it is not unique

#### [Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332379):
then you'll lose access to the \[[ notation

#### [Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332381):
this goes back to the thing I was talking about earlier

#### [Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332382):
once setoid is deemed to be a class

#### [Kevin Buzzard (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332385):
then pretty much whenever it's mentioned in a definition or theorem, it's in a square bracket

#### [Simon Hudon (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332386):
```quote
I think I just defined the positive integers :-)
```
That looks like the Church numerals

#### [Simon Hudon (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332428):
Sorry, I kind of jumped in the middle your conversation

#### [Kevin Buzzard (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332434):
so it's a pain to work with if you decide not to use the type class inference system

#### [Simon Hudon (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332443):
Yes, I see now

#### [Kevin Buzzard (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332444):
As Mario points out, it's the same sort of thing as the (hypothetical but not completely impossible) possibility of having more than one ring structure on a type

#### [Simon Hudon (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332445):
Is it ever necessary to have it inferred?

#### [Kevin Buzzard (Apr 20 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332492):
it's just inconvenient not to have it inferred, if Lean wants it to be inferred.

#### [Kevin Buzzard (Apr 20 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332499):
That was what I discovered when I had a commutative ring earlier -- if you use the type class inference system then you also automatically have a ring, an additive group, and a whole bunch of other things

#### [Kevin Buzzard (Apr 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332504):
and if you don't then you're stuck making all of these yourself

#### [Simon Hudon (Apr 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332521):
What if you skip `\[[` and instead rely on `coe` to convert integers to `Zmod` and `has_one` / `has_add` to use numerals?

#### [Kevin Buzzard (Apr 20 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332584):
I guess the proof of the pudding would be in the eating

#### [Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332628):
I was fine explictly writing my proofs that various types were commutative rings up to a point

#### [Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332632):
and then it got inconvenient and then I figured out how to use type class inference.

#### [Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332637):
Those things aren't quite church numerals

#### [Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332638):
as far as I can see at least

#### [Kevin Buzzard (Apr 20 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332647):
but they do have a similar flavour

#### [Kevin Buzzard (Apr 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332757):
```lean
def hudon_numeral := Π (Y : Type), (Y → Y → Y) → Y → Y
def one : hudon_numeral := λ Y h_add h_one, h_one 
def two : hudon_numeral := λ Y h_add h_one, h_add h_one h_one 
```

#### [Kevin Buzzard (Apr 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332760):
etc

#### [Simon Hudon (Apr 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332812):
Ah yes I see! 0 is missing and Church encodes `succ` rather than `add`

#### [Chris Hughes (Apr 20 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125443745):
Any advice about how to deal with this issue? 
```lean
def Zmod_fintype {n : ℤ} (hn : n ≠ 0) : fintype (Zmod n) :=
fintype.of_equiv _ (equiv_fin hn).symm
```
I can't make this an instance, because it's only true if `n ≠ 0`

#### [Kevin Buzzard (Apr 20 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125444830):
Why not let n be in pnat (positive integers) instead of Z?

#### [Chris Hughes (Apr 20 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125444960):
Probably the best thing. Alternative is to define the equivalence relation differently in the case `n = 0`, so `Zmod 0` is a fintype.

#### [Chris Hughes (Apr 20 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445223):
Then there's also the issue of proving it's a field in the case `prime p`

#### [Kenny Lau (Apr 20 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445230):
`fintype (Zmod $ nat.succ m)`

#### [Chris Hughes (Apr 20 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445289):
`n` is an int currently

#### [Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458960):
I have another type class inference issue and this one is rather frustrating.

#### [Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458969):
I am making a definition, so I really want to stay in term mode.

#### [Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458971):
I wrote down something which should work

#### [Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458983):
and Lean complained that it could not prove that a certain composition of two maps was a ring homomorphism.

#### [Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458987):
So I tried again in tactic mode

#### [Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459006):
(each map is a ring hom, with an instance, and the composite of two ring homs is a ring hom, and this is an instance too, so it should work)

#### [Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459058):
and in tactic mode I have managed to get Lean into a state where the goal is to show that the map is a ring hom (I did this using `refine`)

#### [Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459059):
and `apply_instance` fails

#### [Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459063):
but `show ([cut and paste the goal])`

#### [Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459066):
followed by `apply_instance` succeeds.

#### [Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459079):
In term mode, the proof should look like this:

#### [Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459080):
`to_fun := away.extend_map_of_im_unit ((of_comm_ring (away f) _) ∘ (of_comm_ring R (powers f))) H,`

#### [Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459087):
(it's some part of a structure I'm defining)

#### [Kevin Buzzard (Apr 20 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459144):
but `away.extend_map_of_im_unit` requires that the map (a composite of two ring homs) is a ring hom

#### [Kevin Buzzard (Apr 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459165):
So here it feels to me like Lean is not working as well as it could be.

#### [Kevin Buzzard (Apr 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459169):
But I don't have any feeling as to why not

#### [Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459242):
If I set `pp.all true` I can see that the `show` command is doing something

#### [Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459251):
but unfortunately these are complex maps defined between complex rings

#### [Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459257):
and so I am having trouble figuring out what I have done wrong

#### [Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459260):
and whether it's Lean's fault or mine

#### [Kevin Buzzard (Apr 20 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459438):
Here are the two (rather lengthy) goals.

#### [Kevin Buzzard (Apr 20 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459440):
https://gist.github.com/kbuzzard/a09dc87e290c0497db65c4c702b37c2f

#### [Kevin Buzzard (Apr 20 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459524):
Just to be clear: my problem is that I need to prove something in term mode because it's part of a definition. Type class inference fails me and I don't know why. In tactic mode I can make type class inference succeed.

#### [Kevin Buzzard (Apr 20 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459544):
I could go down the awful route of adding `@`s and explicitly chasing up the proof, but I would rather let type class inference do its job properly and just add hints.

#### [Simon Hudon (Apr 20 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459604):
if it's a proof (i.e. it's type is a `Prop`) I think you can use a tactic:

```
to_fun := 
have local_proof : something, by ...,
definition_using_local_proof,
```

#### [Simon Hudon (Apr 20 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459924):
To my memory, `local_proof` gets compiled to an auxiliary definition / lemma and you'll have `to_fun := definition_using_local_proof` with a reference to that auxiliary definition (which will not be displayed because of proof erasure).

#### [Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460308):
Unfortunately this fails, because my local proof is not a proof of the correct thing.

#### [Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460313):
My local proof is a proof of the second monstrous expression in the gist, which can be proved by type class inference.

#### [Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460320):
I have two maps phi and psi

#### [Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460361):
and I can prove `is_ring_hom (phi comp psi)` with `apply_instance`

#### [Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460370):
but when I write `foo (phi comp psi)`

#### [Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460372):
for some function foo which needs (phi comp psi) to be a ring hom

#### [Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460374):
then type class inference fails

#### [Kevin Buzzard (Apr 20 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460384):
well, this is my understanding of the situation.

#### [Kevin Buzzard (Apr 20 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460405):
I tried to create a MWE but I could not reproduce the problem in a controlled environment

#### [Simon Hudon (Apr 20 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460490):
What do you know about `phi comp psi` that makes it a `is_ring_hom`? Could you create:

```
instance [... some context about (phi comp psi) ...] : is_ring_hom (phi comp psi) := ...
```

right before the structure you're trying to define?

#### [Johan Commelin (Apr 20 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460538):
`phi` and `psi` are both ring homs themselves, if I understand Kevin correctly

#### [Kevin Buzzard (Apr 20 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460635):
Type class inference will make it a ring hom

#### [Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460684):
Here is a very clear explanation of the situation I find myself in:

#### [Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460694):
```lean
  to_fun := have XXX : is_ring_hom 
    (of_comm_ring (away f) (powers (of_comm_ring R (powers f) g)) ∘ (of_comm_ring R (powers f)) )
    := by apply_instance,
  away.extend_map_of_im_unit 
              (of_comm_ring (away f) (powers (of_comm_ring R (powers f) g)) ∘ (of_comm_ring R (powers f)))
              sorry, 
```

#### [Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460701):
(the sorry at the end is just to save you from having to look at another term)

#### [Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460708):
So this definition fails

#### [Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460711):
there's a red squiggle under `away`

#### [Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460715):
and the error is

#### [Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460727):
```lean
failed to synthesize type class instance for
R : Type u,
_inst_1 : comm_ring R,
f g : R,
H : Spec.D' g ⊆ Spec.D' f,
XXX : is_ring_hom (of_comm_ring (away f) (powers (of_comm_ring R (powers f) g)) ∘ of_comm_ring R (powers f))
⊢ is_ring_hom (of_comm_ring (away f) (powers (of_comm_ring R (powers f) g)) ∘ of_comm_ring R (powers f))
```

#### [Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460736):
Note that the goal looks exactly like `XXX`

#### [Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460745):
and what is even more frustrating is that the goal and `XXX` were both created in the same way

#### [Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460790):
by typing the same string twice

#### [Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460794):
namely the string which appears in the goal

#### [Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460800):
however if I set pp.all true

#### [Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460808):
then XXX and the goal expand into the two distinct, but defeq, monsters

#### [Kevin Buzzard (Apr 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460830):
and note that XXX was proved by type class inference

#### [Kevin Buzzard (Apr 20 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460885):
What I need to understand to proceed, I think, is that I'd like to understand how Lean can unfold the same string in two different ways in these two situations.

#### [Kevin Buzzard (Apr 20 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460896):
I am scared to use a let to define the function, because I am scared it will cause me problems further down the line

#### [Kevin Buzzard (Apr 20 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460917):
I am trying to prove that a map is a bijection and if I do something screwy when defining the map then I'm worried I won't be able to use it later

#### [Simon Hudon (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460977):
The problem might be in the two terms that are defeq but not identical. Cosmetic differences in the syntax can take the instance inference process in a different direction. Do you think you can make them exactly identical?

#### [Kevin Buzzard (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460979):
this is exactly what I cannot do

#### [Kevin Buzzard (Apr 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460982):
because as you can see from my term

#### [Kevin Buzzard (Apr 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460989):
I created `XXX` and the input to `away.extend_map_of_im_unit ` by typing exactly the same string of characters.

#### [Simon Hudon (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460992):
including the `@`?

#### [Kevin Buzzard (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461035):
aah I see

#### [Kevin Buzzard (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461038):
I can try to be more persuasive

#### [Simon Hudon (Apr 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461051):
It will probably not be concise but we can work on that once we know it works

#### [Kevin Buzzard (Apr 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461063):
by the way, am I right in thinking that I should not be using `let` in a defintion of a map?

#### [Kevin Buzzard (Apr 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461117):
Many thanks Simon

#### [Kevin Buzzard (Apr 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461123):
Explicitly telling Lean what the type of the composition was has solved the problem

#### [Kevin Buzzard (Apr 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461141):
Thanks a *lot* for persevering with this very awkward problem which was completely blocking me.

#### [Kevin Buzzard (Apr 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461152):
Many thanks indeed.

#### [Simon Hudon (Apr 20 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461200):
You're very welcome :)

#### [Simon Hudon (Apr 20 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461268):
```quote
by the way, am I right in thinking that I should not be using `let` in a defintion of a map?
```
I would avoid it especially if you're going to prove stuff about it. Maybe you're asking about the ùmathlibù style though. I haven't seen that mentioned anywhere but facilitating proofs using your definitions is likely to make you popular with the `mathlib` team.

#### [Mario Carneiro (Apr 21 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125472229):
Have you tried using `by exact` in your definition? There is nothing wrong with using tactics in the definition of a term, although you may need to be more conscientious about junk added to your term by lean (or use `by clean`)

#### [Mario Carneiro (Apr 21 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125472249):
there is not a problem with using `let` or other techniques in defining a complicated function, although you will probably want to write simp lemmas providing your interface so you don't need to rely on definitional expansion

#### [Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504684):
Gaargh I have another one. Here's a MWE.

#### [Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504686):
```lean
import algebra.ring
universes u v w uu 

structure is_unique_R_alg_hom {R : Type u} {α : Type v} {β : Type w} [comm_ring R] [comm_ring α] [comm_ring β] 
(sα : R → α) (sβ : R → β) (f : α → β) [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom f] :=
(R_alg_hom : sβ = f ∘ sα)
(is_unique : ∀ g : α → β, is_ring_hom g → sβ = g ∘ sα → g = f)

lemma comp_unique {R : Type u} {α : Type v} {β : Type w} {γ : Type uu} 
  [comm_ring R] [comm_ring α] [comm_ring β] [comm_ring γ]
  (sα : R → α) (sβ : R → β) (sγ : R → γ) (f : α → β) (g : β → γ) (h : α → γ)
  [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom sγ] [is_ring_hom f] [is_ring_hom g] [is_ring_hom h] :
  is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ h → g ∘ f = h :=
λ Uf Ug Uh, Uh.is_unique (g ∘ f : α → γ) (by apply_instance) (by simp [Uf.R_alg_hom,Ug.R_alg_hom])
```

#### [Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504689):
Note the `by apply_instance` on the last line!

#### [Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504698):
If I replace that with `_` then I get

#### [Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504699):
```
don't know how to synthesize placeholder
context:
R : Type u,
α : Type v,
β : Type w,
γ : Type uu,
_inst_1 : comm_ring R,
_inst_2 : comm_ring α,
_inst_3 : comm_ring β,
_inst_4 : comm_ring γ,
sα : R → α,
sβ : R → β,
sγ : R → γ,
f : α → β,
g : β → γ,
h : α → γ,
_inst_5 : is_ring_hom sα,
_inst_6 : is_ring_hom sβ,
_inst_7 : is_ring_hom sγ,
_inst_8 : is_ring_hom f,
_inst_9 : is_ring_hom g,
_inst_10 : is_ring_hom h,
Uf : is_unique_R_alg_hom sα sβ f,
Ug : is_unique_R_alg_hom sβ sγ g,
Uh : is_unique_R_alg_hom sα sγ h
⊢ is_ring_hom (g ∘ f)
```

#### [Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504701):
How does type class inference work? Is `_` something other than `by apply_instance`?

#### [Mario Carneiro (Apr 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504758):
yes

#### [Kevin Buzzard (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504796):
I guess I just proved that :-)

#### [Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504799):
`_` only does unification

#### [Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504804):
when it is omitted and the binder type is `[tc A]` it uses typeclass inference

#### [Patrick Massot (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504805):
You need `is_unique_R_alg_hom.is_unique` to take a square bracket argument

#### [Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504807):
`by apply_instance` does the same thing but manually

#### [Kevin Buzzard (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504815):
So "don't know how to synthesize placeholder" -- what did it try??

#### [Mario Carneiro (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504817):
unification

#### [Mario Carneiro (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504820):
and nothing else

#### [Kevin Buzzard (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504822):
I don't know what unification means

#### [Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504860):
isn't that something to do with finding something of the right type?

#### [Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504865):
Oh

#### [Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504866):
I remember

#### [Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504869):
it means "I will call this ?m_6"

#### [Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504871):
"and sort it out later"

#### [Kevin Buzzard (Apr 21 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504884):
Thanks Patrick:

#### [Kevin Buzzard (Apr 21 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504885):
```lean
structure is_unique_R_alg_hom {R : Type u} {α : Type v} {β : Type w} [comm_ring R] [comm_ring α] [comm_ring β] 
(sα : R → α) (sβ : R → β) (f : α → β) [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom f] :=
(R_alg_hom : sβ = f ∘ sα)
(is_unique : Π (g : α → β) [is_ring_hom g], sβ = g ∘ sα → g = f)

lemma comp_unique {R : Type u} {α : Type v} {β : Type w} {γ : Type uu} 
  [comm_ring R] [comm_ring α] [comm_ring β] [comm_ring γ]
  (sα : R → α) (sβ : R → β) (sγ : R → γ) (f : α → β) (g : β → γ) (h : α → γ)
  [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom sγ] [is_ring_hom f] [is_ring_hom g] [is_ring_hom h] :
  is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ h → g ∘ f = h :=
λ Uf Ug Uh, Uh.is_unique (g ∘ f : α → γ) (by simp [Uf.R_alg_hom,Ug.R_alg_hom])
```

#### [Patrick Massot (Apr 21 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504929):
You're welcome

#### [Kevin Buzzard (Apr 21 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504934):
I have abstracted a standard trick :-)

#### [Kevin Buzzard (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504986):
I see, I was not even asking type class inference to do its job here. So this one is my bad.

#### [Patrick Massot (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504987):
Indeed

#### [Kevin Buzzard (Apr 22 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125508966):
How do I do this one:

#### [Kevin Buzzard (Apr 22 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125508967):
```lean
structure foo :=
(bar : ∀ (α : Type) [group α] (a b c : α), Prop)

definition X : foo :=
{bar := λ α Hα a b c, (mul_assoc a b c)}
```

#### [Kevin Buzzard (Apr 22 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509119):
Can I use type class inference here?

#### [Kenny Lau (Apr 22 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509132):
you need a prop

#### [Kenny Lau (Apr 22 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509133):
that isn't a prop

#### [Kenny Lau (Apr 22 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509135):
```lean
structure foo :=
(bar : ∀ (α : Type) [group α] (a b c : α), Prop)

definition X : foo :=
{bar := λ g Hg a b c, by letI := Hg; from mul_assoc a b c}
```

#### [Kenny Lau (Apr 22 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509173):
```lean
invalid type ascription, term has type
  a * b * c = a * (b * c) : Prop
but is expected to have type
  Prop : Type
state:
g : Type,
Hg : group g,
a b c : g,
_inst : group g := Hg
⊢ Prop
```

#### [Kevin Buzzard (Apr 22 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509187):
I have some type mismatch error, I think I have more than one problem here

#### [Kenny Lau (Apr 22 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509237):
which is?

#### [Kenny Lau (Apr 22 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509242):
```lean
structure foo :=
(bar : ∀ (α : Type) [group α] (a b c : α), Prop)

definition X : foo :=
{ bar := λ g Hg a b c, @mul_assoc _
    (@monoid.to_semigroup g $ @group.to_monoid g Hg) a b c }
```

#### [Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509394):
`mul_assoc a b c` isn't a prop, it's a proof.

#### [Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509395):
I know I can do it using @, I want to do it using type class inference

#### [Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509397):
I want to understand how to make type class inference work, not to understand how to work around it (which I already know)

#### [Kevin Buzzard (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509405):
```lean
structure foo :=
(bar : ∀ (α : Type) [group α] (a : α), 1 * a = a)

definition X : foo :=
{bar := λ α Hα a, group.one_mul a}
```

#### [Kevin Buzzard (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509406):
```
failed to synthesize type class instance for
α : Type,
Hα : group α,
a : α
⊢ group α
```

#### [Kenny Lau (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509408):
then just letI

#### [Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509445):
Where do I put the letI?

#### [Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509448):
I am in the middle of a structure

#### [Kenny Lau (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509449):
`by letI := H\a; from group.one_mul a`

#### [Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509450):
What if I don't want to go into tactic mode because I am actually defining something?

#### [Kevin Buzzard (Apr 22 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509455):
What exactly are yuo suggesting?

#### [Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509461):
```lean
definition X : foo :=
{bar := λ α Hα a, by letI := Hα; from group.one_mul a}
```

#### [Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509493):
?

#### [Kenny Lau (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509494):
yes

#### [Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509499):
7 errors

#### [Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509502):
including "unknown identifier `letI`"

#### [Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509506):
But even if we can get this to work

#### [Kenny Lau (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509509):
import anything from mathlib

#### [Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509512):
I would rather just make type class inference work.

#### [Kenny Lau (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509514):
```lean
import algebra.group

structure foo :=
(bar : ∀ (α : Type) [group α] (a : α), 1 * a = a)

definition X : foo :=
{bar := λ α Hα a, by letI := Hα; from group.one_mul a}

#print X._proof_1

/-
theorem X._proof_1 : ∀ (α : Type) (Hα : group α) (a : α), 1 * a = a :=
λ (α : Type) (Hα : group α) (a : α), let _inst : group α := Hα in group.one_mul a
-/
```

#### [Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509518):
?!

#### [Kenny Lau (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509520):
!?

#### [Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509561):
which version of Lean are you using?

#### [Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509562):
aah

#### [Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509563):
I have no import

#### [Kevin Buzzard (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509568):
`letI` is some mathlib magic I guess

#### [Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509569):
it is.

#### [Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509571):
it is Mario's workaround of Leo's changes.

#### [Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509572):
So it's in mathlib.

#### [Kevin Buzzard (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509573):
Well thank you for your answer, which kind of stinks

#### [Kevin Buzzard (Apr 22 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509612):
Your answer seems to indicate that `[group \a]` is useless in my structure

#### [Kevin Buzzard (Apr 22 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509614):
i.e. it didn't insert H\a into the type class inference system anyway

#### [Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509622):
but wait a minute, isn't this what Patrick told me to do earlier?

#### [Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509623):
only typeclasses before the colon are inserted

#### [Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509624):
that is Leo's changes

#### [Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509626):
I am writing another localization interface by the way

#### [Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509627):
rewriting your universal properties

#### [Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509628):
heh

#### [Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509979):
you don't need to use `letI`, `by exactI` is the right solution for this application

#### [Kenny Lau (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510034):
aha

#### [Kevin Buzzard (Apr 22 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510848):
https://github.com/kbuzzard/lean-stacks-project/blob/master/src/localization_UMP.lean

#### [Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510887):
I have finally battled through all my typeclass inference issues.

#### [Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510888):
Kenny, I wrote an even better interface for localization

#### [Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510889):
I put all the stuff which makes up the universal properties into one structure

#### [Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510892):
`is_unique_R_alg_hom`

#### [Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510895):
Mario, it's not quite mathlib-ready, but one day this should probably be in mathlib in some form if localization is in

#### [Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510897):
because this file makes the localization stuff usable without ever having to touch the quotient type itself

#### [Kevin Buzzard (Apr 22 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510936):
I know because I'm using localization all the time in my schemes work and this work is what led me to the formalisation and the instances in the file I just linked to

#### [Kevin Buzzard (Apr 22 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510937):
There's one more instance of the structure which is commonly used which we still have to fill in

#### [Mario Carneiro (Apr 22 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125511151):
Shouldn't `comp_unique` read something like `is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)`?

#### [Mario Carneiro (Apr 22 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125511244):
> `by rw ←HR.symm`

what?

#### [Patrick Massot (Apr 22 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523403):
Nice one!

#### [Patrick Massot (Apr 22 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523409):
Kevin, is there is reason why your file doesn't have `open classical` towards the top? You write `classical.` quite a lot

#### [Kevin Buzzard (Apr 22 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523921):
```quote
Shouldn't `comp_unique` read something like `is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)`?
```
No. That's not even true in general. The standard use of the universal property to prove that certain maps are isomorphisms is via the following argument: "We are given maps X-> Y and Y -> X. The given map from X to Y is the only map X -> Y with a certain property (e.g. being an R-algebra map). The map given Y -> X is the only map Y -> X with a certain property. Composition of two maps with the property has the property. The identity map X -> X is the only map X -> X with the property. Hence X -> Y -> X is the identity map by comp_unique. Furthermore the identity map Y -> Y is the only map Y -> Y with the property. Hence Y -> X -> Y is also the identity. So X isomorphic to Y".

#### [Kevin Buzzard (Apr 22 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523973):
The reason your suggestion is not true is that there could be plenty of maps from A to C which don't factor through B.

#### [Kevin Buzzard (Apr 22 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125524012):
I don't open classical because I typically don't open anything. I am very bad at namespaces in general. A whole bunch of my code is incorrectly sitting in the root namespace. The whole thing needs a clear-up.

#### [Kevin Buzzard (Apr 22 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125524203):
```quote
> `by rw ←HR.symm`

what?
```
ha ha. I think it was getting late at that point. This was kind of stupid. I had that composition of f and g was h, but needed to show `forall x, f (g x) = h x`and I felt that this should just be an application of a standard lemma but I couldn't find it. So I just wrote "lambda x, by rw (proof that f circ g = h)" a few times, but then something was the other way round so I switched it and then something else was the other way around so I had to switch it back

#### [Kevin Buzzard (Apr 24 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628730):
```quote
Shouldn't `comp_unique` read something like `is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)`?
```
Maybe you'll like this one:

#### [Kevin Buzzard (Apr 24 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628734):
```lean
theorem unique_R_of_unique_R_of_unique_Rloc {R : Type u} {α : Type v} {β : Type w} {γ : Type uu} 
[comm_ring R] [comm_ring α] [comm_ring β] [comm_ring γ] 
(sα : R → α) [is_ring_hom sα] (fαβ : α → β) [is_ring_hom fαβ] (fβγ : β → γ) [is_ring_hom fβγ] :
is_unique_R_alg_hom sα (fβγ ∘ fαβ ∘ sα) (fβγ ∘ fαβ) 
→ is_unique_R_alg_hom fαβ (fβγ ∘ fαβ) fβγ 
→ is_unique_R_alg_hom (fαβ ∘ sα) (fβγ  ∘ fαβ ∘ sα) (fβγ) :=
```

#### [Kevin Buzzard (Apr 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628799):
If there's a unique R-alg hom from alpha to gamma and a unique alpha-alg hom from beta to gamma then there's a unique R-alg hom from beta to gamma (and it's the same map)

#### [Kevin Buzzard (Apr 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628813):
(oh, the R-alg hom from alpha to gamma must be the composite of a given map alpha -> beta and our given alpha-alg map from beta to gamma)

#### [Johan Commelin (Apr 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629917):
This feels like you want to hit it with Yoneda and reduce it to some basic set-theoretic fact... But that is only instinct

#### [Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629948):
You're looking at both R-alg-homs and alpha-alg-homs... so maybe it is not that straightforward actually

#### [Kenny Lau (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629956):
don't get him started on alpha

#### [Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629960):
What do you mean?

#### [Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629968):
There is alpha's everywhere in his code

#### [Johan Commelin (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630009):
I was actually surprised when I saw that

#### [Kenny Lau (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630023):
don't say "alpha" and any mathematical object in the same sentence in front of kevin buzzard

#### [Johan Commelin (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630032):
But he just did that himself!

#### [Kenny Lau (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630039):
it doesn't matter

#### [Kevin Buzzard (Apr 24 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630634):
Did you notice that when we were doing groups earlier I used alpha to be a group homomorphism just to wind up the CS folk?

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630639):
alpha : G to H

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630684):
The reason I am using alpha for a ring

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630687):
is that the most important ring is called R

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630689):
and then I needed three more

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630693):
but I couldn't face S T U

#### [Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630696):
so I thought alpha beta gamma was OK

#### [Kevin Buzzard (Apr 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630729):
```lean
begin
  intros Hαβ Hβγ,
  constructor,refl,
  intros gβγ Hgβγ H1,
  have Hαγ : fβγ ∘ fαβ = gβγ ∘ fαβ,
    exactI (Hαβ.is_unique (gβγ ∘ fαβ) H1).symm,
  exactI Hβγ.is_unique gβγ Hαγ,
end 
```

#### [Kevin Buzzard (Apr 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630733):
That was the proof

#### [Reid Barton (Apr 24 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631047):
Haha, I seriously thought up to now that an "alpha-alg-hom" was a map of rings equipped with some fancy extra additional structure, like $$\lambda$$-rings or divided power rings or something.

#### [Kevin Buzzard (Apr 24 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631446):
no, it's an alpha-algebra hom :-)

#### [Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631453):
YOU SEE YOU CS PEOPLE

#### [Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631456):
THE MOMENT YOU CALL RINGS ALPHA

#### [Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631461):
WE GET THINGS LIKE THIS HAPPENING

#### [Johan Commelin (Apr 24 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631555):
wow, that was pretty `α`-male

#### [Kevin Buzzard (Apr 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747509):
Here's today's type class inference issue:

#### [Kevin Buzzard (Apr 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747511):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
let H2 := (canonical_iso H).is_ring_hom in
is_unique_R_alg_hom sγ sα (canonical_iso H).to_fun := sorry
```

#### [Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747515):
that won't run

#### [Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747523):
but hopefully I can explain the issue

#### [Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747533):
I am trying to prove `is_unique_R_alg_hom sγ sα (canonical_iso H).to_fun`

#### [Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747592):
but the definition of `is_unique_R_alg_hom` expects H2 to be deduced from type class inference

#### [Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747595):
and I've only managed to prove it the line before

#### [Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747597):
so I can solve this with @

#### [Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747612):
but given that it would then look like

#### [Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747672):
...erm

#### [Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747674):
even that didn't work

#### [Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747690):
`@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun _ _ H2 `

#### [Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747691):
actually it did work, I now have an unrelated problem

#### [Kevin Buzzard (Apr 27 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747701):
So can I insert H2 into the type class inference system before I have even started my proof, because I need it to make my term typecheck?

#### [Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748084):
I have got it working with `@`

#### [Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748085):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
let H2 := (canonical_iso H).is_ring_hom in
let H3 : is_ring_hom sα := by apply_instance in
let H4 : is_ring_hom sγ := by apply_instance in
@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun H4 H3 H2 := sorry
```

#### [Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748090):
The first three lets are simply there to make the statement look clearer

#### [Kevin Buzzard (Apr 27 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748098):
the last three are there because type class inference asked for them all

#### [Reid Barton (Apr 27 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748163):
Change those last three `let`s to `letI` I think

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748209):
`letI` doesn't work there

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748210):
well, it doesn't work for me

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748212):
It works in a proof

#### [Reid Barton (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748213):
Sorry, I just noticed this was in term mode

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748214):
but this is before the proof

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748215):
the issue is that we're before the colon

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748216):
I think

#### [Reid Barton (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748217):
But I think `by letI ...; exact` is fine

#### [Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748219):
I have only seen letI after the colon

#### [Reid Barton (Apr 27 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748230):
Though, it does make me vaguely uneasy to put it in the theorem statement.

#### [Reid Barton (Apr 27 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748310):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
by letI H2 := (canonical_iso H).is_ring_hom; exact
is_unique_R_alg_hom sγ sα (canonical_iso H).to_fun := sorry
```
(untested, hopefully I deleted the right amount of stuff)

#### [Mario Carneiro (Apr 27 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125751156):
Using `letI` in theorem types is fine, and `by letI ...; exact` or `by exactI` is the recommended way to introduce a typeclass thing from the context in term mode

#### [Chris Hughes (Apr 27 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761174):
Don't use let in the statement of a theorem.

#### [Kevin Buzzard (Apr 27 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761407):
```quote
Don't use let in the statement of a theorem.
```
This is easy to fix -- the let is in some sense for my own sanity.

#### [Mario Carneiro (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761455):
Note that `haveI` when used in a tactic doesn't actually produce a `have` term, the result is just like you would get if it were actually inferred by regular tc inference

#### [Mario Carneiro (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761462):
If in doubt, just `#print` the statement to make sure it doesn't look weird

#### [Kevin Buzzard (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761464):
I can't get the syntax right for this

#### [Kevin Buzzard (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761465):
having tried for 10 seconds

#### [Kevin Buzzard (Apr 27 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761507):
I need to insert three hypotheses into the type class inference box

#### [Kevin Buzzard (Apr 27 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761511):
and I don't understand the syntax of this by thing

#### [Kevin Buzzard (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761521):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
let H2 := (canonical_iso H).is_ring_hom in
let H3 : is_ring_hom sα := by apply_instance in
let H4 : is_ring_hom sγ := by apply_instance in
@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun H4 H3 H2 := 
```

#### [Kevin Buzzard (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761522):
This works

#### [Kenny Lau (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761524):
good luck proving that

#### [Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761562):
```lean
begin
letI := (canonical_iso H).is_ring_hom,
have H5 := unique_R_alg_from_loc (canonical_iso H).to_fun,
have H6 := (canonical_iso H).R_alg_hom.symm,
simp [H6] at H5,
exact H5,
end 
```

#### [Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761565):
done

#### [Kenny Lau (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761566):
ok you win

#### [Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761569):
Now I have good interface

#### [Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761570):
so all the proofs are "this canonical thing is canonical"

#### [Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761571):
or "this canonical thing is unique"

#### [Kevin Buzzard (Apr 27 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761573):
or "this unique thing is canonical"

#### [Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761635):
I was trying to put all three hypotheses into one "by"

#### [Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761638):
but I don't understand the syntax

#### [Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761644):
but I've got it working

#### [Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761645):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
by letI H2 := (canonical_iso H).is_ring_hom; exact
by letI H3 : is_ring_hom sα := by apply_instance; exact
by letI H4 : is_ring_hom sγ := by apply_instance; exact
@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun H4 H3 H2 := 
```

#### [Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761646):
I can't even parse that

#### [Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761649):
and now the moment of truth...

#### [Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761698):
wooah

#### [Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761699):
stop everything

#### [Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761701):
lean has silently crashed

#### [Kevin Buzzard (Apr 27 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761761):
OK great, when I restart Lean it just quietly exits

#### [Kevin Buzzard (Apr 27 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761771):
Restarting VS Code and I am back up and running

#### [Kevin Buzzard (Apr 27 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761814):
and it doesn't work after all

#### [Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761869):
```lean
theorem canonical_iso_is_canonical_hom {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
let gbar := of_comm_ring R (powers f) g in
let sα : R → loc (away f) (powers gbar) :=
  of_comm_ring (away f) (powers gbar) ∘ of_comm_ring R (powers f) in
let sγ := (of_comm_ring R (non_zero_on_U (Spec.D' g))) in
by letI H2 := (canonical_iso H).is_ring_hom; 
letI H3 : is_ring_hom sα := by apply_instance; 
letI H4 : is_ring_hom sγ := by apply_instance; exact
@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun H4 H3 H2 := 
```

doesn't work

#### [Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761871):
It's not a problem because my multi-let `@` solution works

#### [Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761872):
I'll construct a MWE. I think this is just a syntax thing

#### [Kevin Buzzard (Apr 27 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762346):
gaargh it's not a syntax thing, my MWE is too minimal and strings of `by letI ...; exact` work fine

#### [Kevin Buzzard (Apr 27 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762486):
My `by apply_instance` proofs seem to be failing when wrapped up in the outer `by`

#### [Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762657):
I am torn between giving up and constructing a MWE

#### [Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762659):
lemme help you

#### [Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762660):
give up.

#### [Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762661):
OK

#### [Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762662):
thanks

#### [Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762663):
no probs

#### [Mario Carneiro (Apr 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125763632):
Your `letI : ... := by apply_instance` lines are redundant. If the typeclass system can already find it, there's no reason to add it to the typeclass system. Unless you are trying to limit search depth?

#### [Mario Carneiro (Apr 27 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125763651):
Also I recommend `haveI` over `letI` when possible. The only time you need `letI` is if you are unfolding the exact definition of the inferred ring or whatever later on in the same proof

#### [Patrick Massot (Apr 27 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764739):
About type classes, let me quickly share https://gist.github.com/PatrickMassot/0d28b74be6f7bc9c0814a87393c91663 It's a draft of documentation of something that took me an embarrassingly long time to understand (I don't say it's directly related to your issues, it's only general knowledge about type class magic)

#### [Mario Carneiro (Apr 27 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764855):
I think the `..prod.has_op` on the last instance is unnecessary

#### [Mario Carneiro (Apr 27 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764861):
it is inferred if you don't specify

#### [Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764904):
oooh

#### [Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764906):
that's even better

#### [Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764909):
How does this new magic trick work?

#### [Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764911):
This file is all about understanding more magic

#### [Mario Carneiro (Apr 27 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764989):
The `comm_magma.mk` structure constructor has the `to_has_op` parent field as instance implicit, and in structure notation that translates to an optional field

#### [Mario Carneiro (Apr 27 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125765037):
same with anonymous constructor notation, you could write it as just `⟨proof of commutativity⟩` instead of `{op_comm := proof of commutativity}`

#### [Kevin Buzzard (Apr 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801928):
Today's typeclass tale of woe:

#### [Kevin Buzzard (Apr 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801930):
```lean
import data.equiv 
universes u v w u' v' w'
variables {α : Type u} {β : Type v} {γ : Type w} {α' : Type u'} {β' : Type v'} {γ' : Type w'}

structure canonically_isomorphic_add_group_homs (Cα : equiv α α') (Cβ : equiv β β') (f : α → β) (f' : α' → β')
[add_group α] [add_group β] [add_group α'] [add_group β']
[is_group_hom f] [is_group_hom f'] 
:= sorry
```

#### [Kevin Buzzard (Apr 28 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801936):
```
failed to synthesize type class instance for
α : Type u,
β : Type v,
α' : Type u',
β' : Type v',
Cα : α ≃ α',
Cβ : β ≃ β',
f : α → β,
f' : α' → β',
_inst_1 : add_group α,
_inst_2 : add_group β,
_inst_3 : add_group α',
_inst_4 : add_group β',
_inst_5 : is_group_hom f
⊢ group β'
```

#### [Kevin Buzzard (Apr 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802086):
dammit

#### [Kevin Buzzard (Apr 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802087):
```lean
import data.equiv 
universes u v w u' v' w'
variables {α : Type u} {β : Type v} {γ : Type w} {α' : Type u'} {β' : Type v'} {γ' : Type w'}

structure canonically_isomorphic_add_group_homs (Cα : equiv α α') (Cβ : equiv β β') (f : α → β) (f' : α' → β')
[Hα : add_group α] [Hβ : add_group β] [add_group α'] [Hβ' : add_group β']
[@is_group_hom α β Hα (by apply_instance) f] [@is_group_hom _ _ _ Hβ' f'] 
:= sorry
```

#### [Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802128):
```
type mismatch at application
  is_group_hom
term
  Hα
has type
  add_group α
but is expected to have type
  group α
```

#### [Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802133):
Damn you Lean

#### [Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802135):
finding out how to turn an `add_group` to a `group` is *exactly* the kind of question which you should be good at.

#### [Kevin Buzzard (Apr 28 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802141):
thus saving me from having to remember the details about names of instances.

#### [Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802181):
Why am I constantly running into type class inference issues @**Sebastian Ullrich** ? Is this sort of thing going to change in Lean 4, do you think?

#### [Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802182):
I find the whole `letI` stuff both essential and extremely confusing

#### [Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802185):
I probably need to write some `letI` docs

#### [Kevin Buzzard (Apr 28 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802192):
but am I right in thinking that `letI` is just a hack which we will be doing away with in Lean 4 as the amazing new type class inference system / syntax comes in?

#### [Kevin Buzzard (Apr 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802231):
I know that Mario has work hard to keep up with Leo's changes in the type class inference system

#### [Kevin Buzzard (Apr 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802232):
but that means that it's currently really confusing for end users

#### [Kevin Buzzard (Apr 28 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802234):
I believe in Lean so much

#### [Kevin Buzzard (Apr 28 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802239):
and I am really hoping for a beautiful solution.

#### [Kevin Buzzard (Apr 28 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802279):
Type class inference issues are stopping me from working right now.

#### [Kevin Buzzard (Apr 28 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802460):
```lean
variable (α : Type)
lemma to_group [H : add_group α] : group α := by apply_instance
```

#### [Kevin Buzzard (Apr 28 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802462):
```
tactic.mk_instance failed to generate instance for
  group α
state:
α : Type,
H : add_group α
⊢ group α
```

#### [Sebastian Ullrich (Apr 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814582):
There are no plans to change class inference for Lean 4. On the other hand, lifting the distinction between `group` and `add_group` is the primary motivation behind refactoring the algebraic hierarchy.

#### [Kenny Lau (Apr 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814583):
but the algebraic hierarchy also has its own problems, right

#### [Kenny Lau (Apr 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814601):
```quote
Today's typeclass tale of woe:
```
look, I already wrote you an `is_add_group_hom`

#### [Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820595):
Oh, I see, I am an idiot. Lean regards the `add_group` hierarchy as completely different to, the `group` hierarchy. I have mixed my hierarchies without noticing

#### [Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820600):
The reason I have made this mistake

#### [Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820603):
is that the two heirarchies are canonically isomorphic

#### [Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820604):
and indeed there is a unique canonical isomorphism in each direction

#### [Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820609):
however the type class inference procedure might not use these canonical isomorphisms

#### [Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820610):
because neither of the hierarchies is "better" than the other one

#### [Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820611):
so it would be asymmetric to let type class inference move from one to the other

#### [Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820653):
and there is a risk of diamonds if we let it move between them freely

#### [Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820654):
On the other hand, to a mathematician, they are the same object

#### [Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820655):
canonical isomorphism is different to type class resolution

#### [Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820656):
and I was applying canonical isomorphism

#### [Johan Commelin (Jun 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128108229):
Does this mean I introduced a diamond:
```quote
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  subset.submodule 𝔥
inferred
  lie_algebra.to_module ↥𝔥
```

#### [Johan Commelin (Jun 15 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112522):
So the context is as follows:
```lean
instance subset.lie_algebra {𝔥 : set 𝔤} [H : @is_lie_subalgebra R ri 𝔤 la 𝔥] :
lie_algebra R 𝔥 :=
{ bracket := λ x y, ⟨[x.1,y.1], is_lie_subalgebra.closed _ x.2 y.2⟩,
  left_linear := begin
    intro y,
    constructor,
    { intros x₁ x₂,
      apply subtype.eq,
      simp,
      apply (lie_algebra.left_linear y).add, -- FAILS
      sorry },
    { intros r x,
      apply subtype.eq,
      -- apply (lie_algebra.left_linear y).smul, FAILS
      sorry }
  end,
  right_linear := sorry,
  alternating := assume ⟨x,_⟩, subtype.eq $ lie_algebra.alternating _,
  Jacobi_identity := assume ⟨x,_⟩ ⟨y,_⟩ ⟨z,_⟩, subtype.eq $ lie_algebra.Jacobi_identity _ _ _,
  anti_comm := assume ⟨x,_⟩ ⟨y,_⟩, subtype.eq $ lie_algebra.anti_comm _ _,
}
```

#### [Johan Commelin (Jun 15 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112567):
How do I tell Lean that it should infer `subset.submodule 𝔥`, instead of `lie_algebra.to_module ↥𝔥`.

#### [Johan Commelin (Jun 15 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112594):
I really don't get why the type class system is tripping up in this case. After all, the first instance unifies completely. The second instance has one meta-variable in it (and rightly so, because it can't infer that `𝔥` is a `lie_algebra` since that is exactly what I'm trying to prove.

#### [Johan Commelin (Jun 15 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112638):
So it seems to me like the type class inference went down a wrong path, but still got convinced that it did a good job. (While the correct path is actually there in Lean.)

#### [Johan Commelin (Jun 15 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114320):
Aaaahhrg.....
```lean
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : has_bracket 𝔤 := @commutator_bracket ?x_1 ?x_2 ?x_3 ?x_4 ?x_5 ?x_6
[class_instances] (1) ?x_2 : comm_ring ?x_1 := ri
[class_instances] (1) ?x_4 : @lie_algebra R ?x_3 ri := la
[class_instances] (1) ?x_6 : ring 𝔤 := @nonneg_ring.to_ring ?x_7 ?x_8
[class_instances] (2) ?x_8 : nonneg_ring 𝔤 := @linear_nonneg_ring.to_nonneg_ring ?x_9 ?x_10
[class_instances] (1) ?x_6 : ring 𝔤 := @domain.to_ring ?x_7 ?x_8
[class_instances] (2) ?x_8 : domain 𝔤 := @linear_nonneg_ring.to_domain ?x_9 ?x_10
[class_instances] (2) ?x_8 : domain 𝔤 := @to_domain ?x_9 ?x_10
[class_instances] (3) ?x_10 : linear_ordered_ring 𝔤 := @linear_nonneg_ring.to_linear_ordered_ring ?x_11 ?x_12
[class_instances] (3) ?x_10 : linear_ordered_ring 𝔤 := @linear_ordered_field.to_linear_ordered_ring ?x_11 ?x_12
[class_instances] (4) ?x_12 : linear_ordered_field 𝔤 := @discrete_linear_ordered_field.to_linear_ordered_field ?x_13 ?x_14
```
[the list goes on and on...]

#### [Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114327):
No stupid! It's a Lie algebra!

#### [Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114337):
Everywhere in this file it has realised immediately that `𝔤` is a Lie algebra, and therefore has a bracket.

#### [Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114338):
But somehow, here it messes up completely.

#### [Andrew Ashworth (Jun 15 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114684):
I notice type class inference issues are quite common in this chat. Maybe in the future a visualization aide would be helpful for people trying to debug  the process

#### [Andrew Ashworth (Jun 15 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114691):
Actually for myself I don't know any better method to debug it than to write out the expression in full, and then in order work forwards as if I was doing the search by hand...

#### [Johan Commelin (Jun 15 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114731):
Right... which is not really what you would expect in this "computer-era"

#### [Andrew Ashworth (Jun 15 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115009):
you'd be disappointed in how much paper I go through while using a computerized theorem prover... or programming in general

#### [Mario Carneiro (Jun 15 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115071):
I have mentioned this in previous instance issues, but `comm_ring ?x_1` is a bad sign in an instance trace, that will usually run away

#### [Mario Carneiro (Jun 15 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115074):
what is the type of `commutator_bracket`?

#### [Johan Commelin (Jun 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115592):
```lean
variables {S : Type*} [ring S]
instance commutator_bracket : has_bracket S := ⟨λ x y, x*y - y*x⟩
```

#### [Mario Carneiro (Jun 15 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115668):
That can't be right, the printout has six variables not two

#### [Mario Carneiro (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115709):
what does `#print commutator_bracket` show?

#### [Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115711):
Anyway, my point is that `𝔤` is a Lie algebra, and by definition that means it `extends has_bracket`. So I would hope that Lean could figure this one out.

#### [Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115718):
```lean
@[instance]
protected def commutator_bracket : Π {R : Type u_1} [ri : comm_ring R] {𝔤 : Type u_2} [la : lie_algebra R 𝔤] {S : Type u_3} [_inst_1 : ring S],
  has_bracket S :=
λ {R : Type u_1} [ri : comm_ring R] {𝔤 : Type u_2} [la : lie_algebra R 𝔤] {S : Type u_3} [_inst_1 : ring S],
  {bracket := λ (x y : S), x * y - y * x}
```

#### [Mario Carneiro (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115721):
there's your problem

#### [Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115722):
Which is crazy...

#### [Johan Commelin (Jun 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115728):
It pulls in way too much stuff.

#### [Mario Carneiro (Jun 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115732):
did you `include` stuff at the top maybe?

#### [Mario Carneiro (Jun 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115807):
try defining it outside the section, this instance has nothing to do with lie algebras

#### [Johan Commelin (Jun 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115819):
Yes... thanks for catching that!

#### [Johan Commelin (Jun 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115879):
Hmm, I need to run. In fact, I should try to get rid of those `include ri la`, but that seems to be non-trivial.

#### [Johan Commelin (Jun 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115887):
Anyway, I'll be back later. AFK

