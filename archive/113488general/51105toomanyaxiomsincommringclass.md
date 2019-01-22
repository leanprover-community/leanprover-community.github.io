---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51105toomanyaxiomsincommringclass.html
---

## [general](index.html)
### [too many axioms in comm_ring class](51105toomanyaxiomsincommringclass.html)

#### [Kevin Buzzard (Mar 07 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389686):
I have to put a ring structure on a slightly complicated type (a subtype, consisting of functions with some properties). Every verification is going to be quite messy -- even defining zero and one will take some effort. So I really want to minimise the amount of stuff I want to prove. I am sure that Lean is asking me to do too much by default -- for example it wants a proof of add_comm, add_zero and zero_add, and the same story with multiplication and one. Of course I can deduce zero_add from add_zero once I've proved add_comm but in some sense I'm wondering why I am even being asked to do this, because this is true for every commutative ring. Is there a way of "fixing" this?

#### [Mario Carneiro (Mar 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389751):
The usual solution is to write a variant on `mk` that asserts only the properties you want to prove and proves the rest. This can be done generally for `comm_ring`, to provide several interfaces depending on which axioms you want.

#### [Mario Carneiro (Mar 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389795):
Warning: you can get into trouble if you do this for data fields, like we've discussed about deriving a topology from a metric

#### [Kevin Buzzard (Mar 07 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389808):
Aah I see. So there's an argument for `comm_ring.mk'` which takes what I need and builds the rest. I remember seeing this in the construction of the rationals -- I think there are about 4 constructors in the end.

#### [Kevin Buzzard (Mar 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389869):
Re: data fields. Once you have one and neg you can define zero ;-) so perhaps I should be careful here.

#### [Mario Carneiro (Mar 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389984):
If you want to derive zero or something else, one option is to have it be an optional argument, so that the user can still set up their desired choice of defeq equivalence class here

#### [Mario Carneiro (Mar 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389986):
that's what many structures do by default

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123389991):
Oh, something annoying has happened.

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390000):
```
    Fring := λ U OU,{
      add := _,
      zero := _,
      add_comm := _,
      add_assoc := _,
      one := _,
      zero_add := _,
      neg := _,
      add_left_neg := _,
      mul := _,
      mul_assoc := _,
      add_zero := _,
      one_mul := _,
      mul_one := _,
      left_distrib := _,
      right_distrib := _,
      mul_comm := _ 
    },
```

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390004):
There's my set-up (I'm not going to do mk' right now, I'm going to prove it's a ring and see what happens)

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390010):
and I was expecting red underlines on all the _s

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390012):
but I only have one under add_assoc

#### [Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390015):
I mean on the _ of add_assoc

#### [Kevin Buzzard (Mar 07 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390058):
Am I expected to remember that addition takes two inputs? I thought Lean was going to tell me that.

#### [Mario Carneiro (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390070):
Hm, I can probably explain why add_assoc specifically, but it's not all that relevant. They are all actually required, but lean won't be able to even contemplate the later stuff until you finish the early stuff

#### [Kevin Buzzard (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390082):
add_assoc is telling me I have a type mismatch!

#### [Mario Carneiro (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390085):
with what?

#### [Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390126):
Wooah -- maybe type class inference is randomly doing stuff? How do I check that?

#### [Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390130):
```
type mismatch at field 'add_assoc'
  ?m_1
has type
  ∀
  (a b c :
    (λ (U : set (X R))
     (HU :
       (λ (X_1 : set (X R)),
          set.mem (lattice.complete_boolean_algebra.neg X_1) {A : set (X R) | ∃ (E : set R), Spec.V E = A})
         U),
       {f // ∀ (u : X R),
          U u →
          (∃ (g : R),
             set.mem u (Spec.D' g) ∧
               set.subset (Spec.D' g) U ∧
                 ∃ (r : localization.away g),
                   ∀ (Q : X R) (HQQ : set.mem Q U) (H2 : set.mem Q (Spec.D' g)), f Q HQQ = canonical_map g Q H2 r)})
      U
      OU), ?m_1 (?m_1 a b) c = ?m_1 a (?m_1 b c)
but is expected to have type
  ∀
  (a b c :
    (λ (U : set (X R)) (HU : (λ (X_1 : set (X R)), -X_1 ∈ {A : set (X R) | ∃ (E : set R), Spec.V E = A}) U),
       {f // ∀ (u : X R),
          U u →
          (∃ (g : R),
             u ∈ Spec.D' g ∧
               Spec.D' g ⊆ U ∧
                 ∃ (r : localization.away g),
                   ∀ (Q : X R) (HQQ : Q ∈ U) (H2 : Q ∈ Spec.D' g), f Q HQQ = canonical_map g Q H2 r)})
      U
      OU), a + b + c = a + (b + c)
```

#### [Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390131):
So far I wrote nothing.

#### [Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390144):
what's all that about localizations? What's the theorem?

#### [Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390145):
What does that add even mean on the bottom line?

#### [Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390151):
The ?m_1 presumably means "you didn't tell me what add meant yet"

#### [Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390153):
it's `@has_add.add <your type> ?m_1 a b`

#### [Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390154):
which prints as `a + b`

#### [Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390158):
Oh I see it's just some pretty printer cuteness

#### [Kevin Buzzard (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390208):
I told you my objects were complicated ;-)

#### [Mario Carneiro (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390210):
this is probably some artifact of structure `notation` command

#### [Mario Carneiro (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390213):
are you familiar with making defs for things?

#### [Kevin Buzzard (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390216):
I have heard of `definition`

#### [Kevin Buzzard (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390223):
if that's what you mean

#### [Mario Carneiro (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390231):
I'm trying to understand why your goal is a mile long before you start the proof

#### [Kevin Buzzard (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390234):
In brief, my objects are functions which are well-behaved locally

#### [Mario Carneiro (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390236):
you left out the statement of the theorem above

#### [Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390241):
I am defining a ring structure

#### [Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390276):
on a complex type

#### [Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390279):
on what?

#### [Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390288):
give the type a name

#### [Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390289):
It's a subtype of a pi type

#### [Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390297):
Here's a toy example

#### [Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390299):
do not prove an instance for a messy type

#### [Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390301):
I want to consider functions on a topological space which are "locally well-behaved"

#### [Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390303):
it will make typeclass inference cry

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390305):
I am not using type class inference at all

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390311):
I gave up on it

#### [Mario Carneiro (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390313):
I'm not talking about the mathematical specifics of the type

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390314):
I don't need it

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390320):
I don't understand what you are asking but I am certainly interested in what you are thinking

#### [Mario Carneiro (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390321):
what's the theorem? like paste the statement here

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390323):
There is no theorem

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390324):
I don't know why you keep asking this

#### [Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390326):
I am trying to put a ring structure on a type

#### [Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390368):
I am making a 1000 line definition

#### [Mario Carneiro (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390369):
yes that

#### [Mario Carneiro (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390372):
instance, def, theorem, it's all the same

#### [Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390373):
:-)

#### [Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390376):
My type is a subtype of a pi type

#### [Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390390):
and the details involve a lot of commutative algebra

#### [Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390398):
what exactly do you want to know about it?

#### [Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390403):
and I have a convoluted way of adding and multiplying two such things

#### [Mario Carneiro (Mar 07 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390451):
Okay, toy example:
```
instance : ring {x // ∀ y, x is more awesome than y} :=
sorry
```
bad
```
def awesome_sauce := {x // ∀ y, x is more awesome than y}
instance : ring awesome_sauce :=
sorry
```
good

#### [Kevin Buzzard (Mar 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390471):
whatever is the difference?

#### [Mario Carneiro (Mar 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390472):
I am getting the sense you typed some big term after `ring`

#### [Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390473):
```
definition structure_presheaf_of_rings_on_affine_scheme (R : Type*) [comm_ring R] 
: presheaf_of_rings (X R)
:= { PT := structure_presheaf_of_types_on_affine_scheme R,
    Fring := λ U OU,{
      add := _,
      zero := _,
      add_comm := _,
      add_assoc := _,
      one := _,
      zero_add := _,
      neg := _,
      add_left_neg := _,
      mul := _,
      mul_assoc := _,
      add_zero := _,
      one_mul := _,
      mul_one := _,
      left_distrib := _,
      right_distrib := _,
      mul_comm := _ 
    },
    res_is_ring_morphism := sorry,
}
```

#### [Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390509):
I typed that

#### [Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390515):
I am right in the middle of a complex mathematical object

#### [Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390520):
and your simple example is too simple for me to currently make sense of

#### [Mario Carneiro (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390526):
In that case, you should probably define that `Fring` field in its own lemma

#### [Kevin Buzzard (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390531):
Why does this make any difference?

#### [Kevin Buzzard (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390538):
But of course I will do this now you tell me to

#### [Mario Carneiro (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390549):
My sense is that typeclass inference generally does poorly with inferring typeclasses on complicated things

#### [Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390553):
it needs to know when not to unfold

#### [Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390597):
and definitions are the best way to indicate this

#### [Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390599):
I am not ever using typeclass inference

#### [Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390602):
it causes me too much trouble

#### [Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390604):
you are, *inside the structure instance itself*

#### [Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390607):
?

#### [Mario Carneiro (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390616):
because it's actually proven in stages, a semigroup plus some more stuff to make it a monoid, group, ring, then comm_ring

#### [Kevin Buzzard (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390629):
this I knew

#### [Kevin Buzzard (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390639):
But is this really typeclass inference?

#### [Mario Carneiro (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390641):
and after the initial stages, it uses the semigroup instance to find the `+` which is used in later proofs

#### [Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390643):
It's not just "comm_ring extends ring so let's just copy the fields"?

#### [Mario Carneiro (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390686):
Actually, that depends on whether it is using the old or new structure command

#### [Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390688):
:-)

#### [Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390690):
I am using the default structure command

#### [Sebastian Ullrich (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390692):
It looks like we don't do error recovery after that field type mismatch error. I could change that, but a smaller example would be nice :) .

#### [Kevin Buzzard (Mar 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390699):
I feel like the definition of a ring is extremely small compared to the monster I am creating.

#### [Sebastian Ullrich (Mar 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390703):
Eh, I guess it shouldn't be hard to construct one by myself

#### [Kevin Buzzard (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390747):
This is not a big deal at this point

#### [Mario Carneiro (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390748):
Even if it doesn't make a difference, I would recommend making this a definition and proving in stages simply for proof engineering reasons

#### [Kevin Buzzard (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390750):
I see.

#### [Mario Carneiro (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390752):
you should try to keep your goal size down to something human readable

#### [Kevin Buzzard (Mar 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390767):
I thought I'd fix things up with `add_assoc := sorry` for the time being

#### [Kevin Buzzard (Mar 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390770):
I got

#### [Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390781):
```
type mismatch at field 'add_assoc'
  sorry
has type
  ∀
  (a b c :
    (λ (U : set (X R))
     (HU :
       (λ (X_1 : set (X R)),
          set.mem (lattice.complete_boolean_algebra.neg X_1) {A : set (X R) | ∃ (E : set R), Spec.V E = A})
         U),
...
```

#### [Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390811):
Wasn't expecting that!

#### [Mario Carneiro (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390821):
did you sorry the `add` field first?

#### [Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390824):
that fixes it

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390832):
Ok so here's a question

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390838):
First I have a red line under add_assoc.

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390840):
I can't fix it with a sorry

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390841):
I sorry the add and this fixes both.

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390842):
Q) Where does the new red line appear?

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390844):
And how do I fix it?

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390846):
A) zero_add

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390847):
I can fix it by sorrying the zero and zero_add.

#### [Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390849):
Now I have a type mismatch at add_left_neg

#### [Kevin Buzzard (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390890):
I love the randomness of it all

#### [Mario Carneiro (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390891):
it's whack a mole, I know

#### [Mario Carneiro (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390898):
Here's how you can derive the answer: First, find the first nested structure that is not complete

#### [Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390904):
so in the original case, that's `semigroup`

#### [Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390909):
next, find all fields that have nothing dependent on them

#### [Kevin Buzzard (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390913):
ha ha, I sorried all the data fields and now I have `don't know how to synthesize placeholder` on every other field apart from add_left_neg. ???

#### [Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390916):
so in this case `add_assoc` because `add` has `add_assoc` depending on it

#### [Mario Carneiro (Mar 07 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390967):
when you sorry it out, it is considered complete and you get the next error, because of the error recovery issue Sebastian mentioned

#### [Kevin Buzzard (Mar 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390980):
I have a grant deadline for Friday, I'd better go to work. Thanks for the comments. I will move the ring structure to a definition. Do I need to annotate the definition with reducible or irreducible or whatever?

#### [Mario Carneiro (Mar 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390981):
But if you sorry `add_assoc` without `add`, then I think the sorry macro gets into trouble because the type it needs to be has a metavariable in it

#### [Mario Carneiro (Mar 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123390986):
no, the regular reducibility is fine

#### [Kevin Buzzard (Mar 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391025):
I think I deserve another achievement for making sorry fail to find its own type

#### [Kevin Buzzard (Mar 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391044):
Thanks to Kenny's hard work on localisation lemmas we nearly have schemes, although not in a way Assia would approve of, as when I have defined this ring structure we will have a definition but no way of constructing examples :-)

#### [Kevin Buzzard (Mar 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391045):
I will then need to prove one more theorem and then we can have examples

#### [Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391085):
what's the most trivial scheme?

#### [Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391087):
Mario -- you always said that the test case for you was whether one could prove any lemmas about the object

#### [Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391088):
is a ring a scheme over itself?

#### [Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391091):
but I will work on Assia's comments first -- she wants to see examples first.

#### [Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391094):
The spectrum of a ring is an affine scheme

#### [Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391096):
and an affine scheme is a scheme

#### [Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391099):
voila

#### [Mario Carneiro (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391100):
do that

#### [Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391108):
but I will be able to define a scheme correctly in Lean

#### [Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391110):
without ever proving that an affine scheme is a scheme

#### [Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391111):
because a scheme is an object with property X that looks locally like an affine scheme

#### [Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391114):
and I did not prove that affine schemes have property X yet

#### [Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391155):
but one can formulate "I look locally like an affine scheme" without mentioning X

#### [Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391159):
so first I want the definition of a scheme

#### [Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391160):
and then I need to prove one more theorem

#### [Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391165):
I think you are not ready for assia's criterion yet

#### [Kevin Buzzard (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391170):
Thanks for the definition comments.

#### [Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391171):
she talked about examples in situations where you already have the fundamental theorem of mystuffoids

#### [Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391176):
you are still in the definition crafting stage

#### [Kevin Buzzard (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391177):
This is a fundamental issue

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391214):
which goes beyond Lean

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391220):
It's something I have found when lecturing

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391222):
You introduce a new concept in a lecture

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391224):
typically a new structure

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391226):
and then you want to do two things simultaneously:

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391227):
(1) give basic examples

#### [Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391232):
(2) prove basic lemmas (e.g. subsets, quotients,  products, whatever)

#### [Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391237):
(consequences of axioms)

#### [Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391241):
and whenever I do this in a lecture I never know whether to do (1) or (2) first

#### [Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391242):
because they are independent and both very important

#### [Mario Carneiro (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391245):
they are both important, of course. They are even closely related since (1) is basically stuff that implies X and (2) is stuff implied by X

#### [Kevin Buzzard (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391246):
They are both "the first thing you should do after you defined the concept"

#### [Kevin Buzzard (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391288):
Still, I should concentrate on defining the concept first. Cheers!

#### [Mario Carneiro (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391290):
:wave:

#### [Kevin Buzzard (Mar 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391305):
Current state of things at https://github.com/kbuzzard/lean-stacks-project/blob/master/src/scheme.lean

#### [Kevin Buzzard (Mar 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123391348):
probably lines 268 - 305 should be moved into a definition, if my understanding of what you're saying is correct. OK I really am gone now.

#### [Kevin Buzzard (Mar 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392619):
dammit I refactored into a definition and then started with `  add := λ f₁ f₂, ⟨_,_⟩,` and got an assertion violation. I am going to roll back a bit I think. Does anyone have any advice as to which version to pick?

#### [Mario Carneiro (Mar 07 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392672):
when I get an assertion violation in the middle of writing something, I try to finish writing it and see if it's okay once it is once again well-formed

#### [Johannes Hölzl (Mar 07 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392781):
@**Kevin Buzzard**  I think a simpler solution for you would be to first start defining the operations, i.e. `instance : has_add (Fring)`, ... do this for all the data. Then you see at least that this works. Then you proof stat it is a monoid, a group, a semiring etc. this allows you to have a clear overview what's happening.

#### [Kevin Buzzard (Mar 07 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392795):
In maths we care about refactoring to a far lesser degree.

#### [Kevin Buzzard (Mar 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392803):
I've seen lecturers write a proof and then in the middle stop and say "oh, hmm, Ok we will need this:" and then write "sublemma : ..." and just insert something in the middle, and then press on.

#### [Kevin Buzzard (Mar 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392808):
Either that or just splurge through everything.

#### [Kevin Buzzard (Mar 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392856):
And then we get "and as we see from the proof of Theorem B, X -> Y" later on

#### [Kevin Buzzard (Mar 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392859):
and everyone is fine with this

#### [Kevin Buzzard (Mar 07 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123392877):
PS I am not using instances at all. I wanted to completely avoid type class inference and also any coercions as much as possible, so I had a tight control over what was going on.

#### [Kevin Buzzard (Mar 07 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393347):
Oh this is a really nice way of doing it. Thanks. My definitions are getting smaller and smaller, apparently this is what I should be aiming at.

#### [Mario Carneiro (Mar 07 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393512):
> I've seen lecturers write a proof and then in the middle stop and say "oh, hmm, Ok we will need this:" and then write "sublemma : ..." and just insert something in the middle, and then press on.

You should view this as analogous to writing a proof, then in the middle editing the statement, and returning to the proof. The fact that lectures are limited to a linear format is simply because of practical concerns of blackboard presentation, but we often think about things out of order like this. A lean script should not reflect these amendations themselves, so that at the end everything fits together.

#### [Kevin Buzzard (Mar 07 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393622):
I added some of these comments to https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md

#### [Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393634):
Are you interested in a PR Mario? A lot of those WIPs are (a) works in progress and (b) already helpful for me in their current form.

#### [Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393638):
I am just letting them grow organically at this point rather than trying to tidy them.

#### [Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393643):
The advantage of a PR is that they become more visible to people. The disadvantage is that they become your problem.

#### [Kevin Buzzard (Mar 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393645):
I am happy either way; a lot depends on how seriously you take that docs directory.

#### [Kevin Buzzard (Mar 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393687):
My workflow now is much better now we're at zulip. If I have time I update my local docs. If I don't then I just star the messages and come back later.

#### [Kevin Buzzard (Mar 07 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123393693):
I'm talking about when people give me good advice which I would like to keep track of.

#### [Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394051):
o_O

#### [Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394054):
how clean is this:

#### [Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394057):
```
definition structure_presheaf_value_is_comm_ring {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U)
: comm_ring (structure_presheaf_value U HU)
:= {
  add := (structure_presheaf_value_has_add U HU).add,
  mul := (structure_presheaf_value_has_mul U HU).mul,
  zero := (structure_presheaf_value_has_zero U HU).zero,
  one := (structure_presheaf_value_has_one U HU).one,
  add_comm := by simp,
  zero_add := by simp,
  add_zero := by simp,
  neg := (structure_presheaf_value_has_neg U HU).neg,
  add_left_neg := by simp,
  add_assoc := by simp,
  mul_assoc := by simp [mul_assoc],
  one_mul := by simp,
  mul_one := by simp,
  left_distrib := by simp [left_distrib],
  right_distrib := by simp [right_distrib],
  mul_comm := by simp [mul_comm]
}
```

#### [Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394059):
:-)

#### [Kevin Buzzard (Mar 07 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394101):
My original proofs were worse

#### [Kevin Buzzard (Mar 07 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394112):
but because I wrote https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md

#### [Kevin Buzzard (Mar 07 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394122):
I remembered the "how to use simp better" thing -- i.e "if your proof looks like `funext (λ f,subtype.eq (funext (λ P,by simp)))`

#### [Kevin Buzzard (Mar 07 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394161):
then you might want to consider being more optimistic with when exactly you use simp"

#### [Mario Carneiro (Mar 07 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394226):
Why is there the messy thing with `(structure_presheaf_value_has_add U HU).add`? As it is currently, there should be no difficulty making this thing an instance, and then it will pick those fields up automatically

#### [Mario Carneiro (Mar 07 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394345):
even if you can't make them instances, you can use `..structure_presheaf_value_has_add U HU` etc to add the operations

#### [Mario Carneiro (Mar 07 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123394770):
Re: PRs, I'm okay with docs of any kind. My recommendation is to try to write them with an authoritative locution style; I will let you know if you say false things. If you don't know something, leave it out, say you don't know in the doc, or ask about it here and then put in whatever you find out.

#### [Kevin Buzzard (Mar 07 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123395558):
Messy thing: I am not concerned with such issues at the minute. I am completely avoiding instances simply because writing all this code is taking my Lean understanding to a new level and I realised that I did not trust myself to do all the clever things instances could do for me, and I would occasionally have problems with instances, so I decided to never use them just to see what like would be like without them. The advantage of doing it my way is that I can take one look and understand what is happening. I am still a learner.

#### [Kevin Buzzard (Mar 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123395617):
I am always muddled about this .. thing. I forget the syntax, I never know whether it has to go at the beginning or the end or whether it doesn't matter, just stupid things which people your age only need to be told once but people my age need to have a reference for and basic examples of. I don't have the time right now to fart around with .. trying to make it work and as you can see from https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md I have also not found the time to figure it out once and for all and then document it. I am afraid I need docs to work efficiently, and if stuff isn't documented properly then I shy away from it.

#### [Sebastian Ullrich (Mar 07 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123396002):
Instead of declaring `mk'`s, the algebraic hierarchy could be amended with superclass defaults like
```
class add_comm_monoid (α : Type u) extends add_monoid α, add_comm_semigroup α :=
(add_zero := by simp [add_comm, zero_add])
```

#### [Mario Carneiro (Mar 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123396500):
that doesn't actually work right now tho

#### [Sebastian Ullrich (Mar 07 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123396588):
It doesn't?

#### [Mario Carneiro (Mar 07 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123397155):
nvm, I misread what you are doing there

#### [Kevin Buzzard (Mar 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123402113):
```quote
Why is there the messy thing with `(structure_presheaf_value_has_add U HU).add`? As it is currently, there should be no difficulty making this thing an instance, and then it will pick those fields up automatically
```
My co-author got their hands on it and now it looks like this:

#### [Kevin Buzzard (Mar 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123402117):
```

definition structure_presheaf_value_is_comm_ring {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U)
: comm_ring (structure_presheaf_value U HU) :=
by refine {
  add := (+),
  zero := 0,
  neg := ((structure_presheaf_value_has_neg U HU).neg),
  mul := (*),
  one := 1,
  .. };
{simp [mul_assoc, left_distrib, right_distrib]} <|> simp [mul_comm]
```

#### [Scott Morrison (Mar 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123404579):
I really like @**Sebastian Ullrich**’s suggestion for putting in superclass defaults in the algebraic hierarchy, at least where they are “uncontroversial”. I didn’t even know you can do that.

#### [Sebastian Ullrich (Mar 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too many axioms in comm_ring class/near/123404588):
It's not a very old feature :)

