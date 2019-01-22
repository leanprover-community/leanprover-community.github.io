---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56940piinstancewoes.html
---

## [general](index.html)
### [pi_instance woes](56940piinstancewoes.html)

#### [Kevin Buzzard (Jun 14 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076746):
A product of topological groups is a topological group.

#### [Kevin Buzzard (Jun 14 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076751):
That doesn't sound too hard!

#### [Kevin Buzzard (Jun 14 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076814):
Attempt 1:

#### [Kevin Buzzard (Jun 14 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076840):
```lean
import analysis.topology.topological_structures

example (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_group (F i)] : ...
```

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076846):
unknown identifier: topological_group!

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076852):
We have topological monoids, topological rings...

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076856):
but no topological groups :-)

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076863):
After some digging, I find that we have `topological_add_group`

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076866):
and given that we also have the insane convention that addition isn't commutative

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076869):
this will do

#### [Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076883):
Attempt 2:

#### [Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076925):
```lean
import analysis.topology.topological_structures

example (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_add_group (F i)] : ...

```

#### [Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076937):
```
failed to synthesize type class instance for
γ : Type,
F : γ → Type,
i : γ
⊢ add_group (F i)
```

#### [Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076940):
(and topological_space too)

#### [Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076941):
*sigh*

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076965):
Attempt 3:

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076968):
```lean
import analysis.topology.topological_structures

example (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
topological_add_group (Π i, F i) := sorry 
```

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076979):
```
failed to synthesize type class instance for
γ : Type,
F : γ → Type,
_inst_1 : Π (i : γ), topological_space (F i),
_inst_2 : Π (i : γ), add_group (F i),
_inst_3 : ∀ (i : γ), topological_add_group (F i)
⊢ add_group (Π (i : γ), F i)
```

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076981):
gaargh

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076994):
Oh but this is done in pi_instances, right?

#### [Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076996):
Attempt 4

#### [Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077047):
```lean
import analysis.topology.topological_structures algebra.pi_instances

example (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
topological_add_group (Π i, F i) := {}

```

#### [Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077058):
```
maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')
```

#### [Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077062):
*bangs head on table*

#### [Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077199):
Here's how far I have got:

#### [Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077205):
```lean
import analysis.topology.topological_structures algebra.pi_instances

set_option trace.class_instances true
example (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
topological_add_group (Π i, F i) := {
continuous_neg := sorry 
}

```

#### [Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077213):
and the trace looks like this:

#### [Kevin Buzzard (Jun 14 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077316):
https://gist.github.com/kbuzzard/762adae68d4cbe240f4098968b14fe2e

#### [Kevin Buzzard (Jun 14 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078022):
Oh!

#### [Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078031):
That trace is just tracing along not looking like anything too serious is happening in terms of loops

#### [Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078038):
and then right at the end it randomly explodes

#### [Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078061):
```
[class_instances] (4) ?x_28 : ring ?x_27 := @pi.ring ?x_30 ?x_31 ?x_32
[class_instances] (5) ?x_32 i : ring (?x_31 i) := @pi.ring (?x_33 i) (?x_34 i) (?x_35 i)
[class_instances] (6) ?x_35 i i_1 : ring (?x_34 i i_1) := @pi.ring (?x_36 i i_1) (?x_37 i i_1) (?x_38 i i_1)
[class_instances] (7) ?x_38 i i_1 i_2 : ring (?x_37 i i_1 i_2) := @pi.ring (?x_39 i i_1 i_2) (?x_40 i i_1 i_2) (?x_41 i i_1 i_2)
```

#### [Kevin Buzzard (Jun 14 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078080):
and it just keeps getting bigger and bigger

#### [Simon Hudon (Jun 14 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078153):
What instance are you expecting will resolve this?

#### [Kevin Buzzard (Jun 14 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078207):
you are that instance

#### [Kevin Buzzard (Jun 14 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078218):
my question certainly seems to have nothing to do with rings

#### [Simon Hudon (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078250):
`apply_instance` doesn't have my phone number ;-)

#### [Kevin Buzzard (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078253):
I want to prove that the product of top groups is a top group

#### [Kevin Buzzard (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078256):
The instance isn't there yet

#### [Kevin Buzzard (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078261):
but I haven't even got to defining the instance

#### [Kevin Buzzard (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078303):
because of some random type class explosion

#### [Simon Hudon (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078305):
You can try `by pi_instance`

#### [Simon Hudon (Jun 14 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078339):
You will need more arguments, we'll see what errors we get

#### [Kevin Buzzard (Jun 14 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078402):
I'm on it

#### [Simon Hudon (Jun 14 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078425):
If you use my `refine_struct` branch, that should be all you need.

#### [Kevin Buzzard (Jun 14 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078439):
ooh

#### [Kevin Buzzard (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078442):
so you mean don't use algebra.pi_instances?

#### [Kevin Buzzard (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078486):
Apparently I should prove pi.topological_add_monoid first

#### [Simon Hudon (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078495):
No I mean you write `by pi_instance` and it figures it all out on its own without you having to give more information

#### [Simon Hudon (Jun 14 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078506):
(if you use `refine_struct`)

#### [Kevin Buzzard (Jun 14 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078695):
so can you give me more clues about exactly what to type, so I can "use `refine_struct`"?

#### [Simon Hudon (Jun 14 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078748):
certainly

#### [Simon Hudon (Jun 14 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078852):
1. delete your `_target` directory
2. go in your `leanpkg.toml` file
3. replace the `mathlib` entry with
    `mathlib = {git = "https://github.com/cipher1024/mathlib", rev = "e1c15f02a62a0343e5497ae380355e966be9b3e4"}`
4. in a terminal, call `leanpkg build` on your project

#### [Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078880):
You know what

#### [Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078881):
I think the problem might be

#### [Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078883):
that pi_instances doesn't do any topology

#### [Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078887):
and I rather think that putting a topological space structure on a product of types

#### [Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078926):
is actually something which requires an idea

#### [Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078933):
at least if you want to put the correct top space structure on it

#### [Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078941):
Aah sorry

#### [Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078950):
By "don't use algebra.pi_instances"

#### [Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078959):
I mean "don't use official mathlib's algebra.pi_instances"?

#### [Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078966):
OK I will switch.

#### [Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078972):
It will be interesting to see what happens!

#### [Kevin Buzzard (Jun 14 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079136):
building

#### [Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079149):
But I don't think your pi_instances tactic is going to put a topological space structure on a product of topological spaces

#### [Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079154):
This isn't formal, like a ring structure on a product of rings

#### [Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079165):
I think this needs to be written by hand.

#### [Simon Hudon (Jun 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079374):
Yes, that's right. If the instance relies on any kind of insight that is not already present in the more basic instance, my tactic won't do.

#### [Simon Hudon (Jun 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079509):
`refine_struct` might still be helpful, especially if many of the proofs are of the same shape

#### [Kevin Buzzard (Jun 14 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080056):
```lean
instance topological_space [∀ i, topological_space $ f i] : topological_space (Π i : I, f i) :=
topological_space.generate_from { U : set (Π i : I, f i) | ∃ u : Π i : I, set (f i), 
set.finite {i : I | u i ≠ set.univ} ∧ ∀ g : Π i, f i, U g = ∀ i, g i ∈ u i}
```

#### [Kevin Buzzard (Jun 14 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080077):
But now I have this -- assuming I got it right (and I am not entirely sure that introducing both U and u was necessary) -- I wonder if I can persuade pi_instances to go further.

#### [Simon Hudon (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080143):
Now I think there's a chance

#### [Kevin Buzzard (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080147):
Actually this might just be hard. Now I can prove that a product of topological groups is a topological space and a group

#### [Kevin Buzzard (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080150):
but a topological group is more than this

#### [Kevin Buzzard (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080163):
you want the group structure maps like product and inverse to be continuous

#### [Kevin Buzzard (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080174):
and these might be lemmas rather than stuff which is formally true

#### [Reid Barton (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080184):
That Pi type topological space instance is already in `topological_space.lean` isn't it?

#### [Reid Barton (Jun 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080241):
```lean
instance Pi.topological_space {β : α → Type v} [t₂ : Πa, topological_space (β a)] : topological_space (Πa, β a) :=                                                            
⨆a, induced (λf, f a) (t₂ a)                                                                                                                                                  
```

#### [Kevin Buzzard (Jun 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080249):
Oh did I miss it?

#### [Kevin Buzzard (Jun 14 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080258):
Oh it's not in pi_instances!

#### [Reid Barton (Jun 14 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080261):
But it's in the same module that defines `topological_space`

#### [Reid Barton (Jun 14 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080275):
Oh okay, it looks like Lean never actually claimed it was missing?

#### [Kevin Buzzard (Jun 14 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080318):
No it just gave me terrifying errors

#### [Kevin Buzzard (Jun 14 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080358):
```lean
instance pi_topological_monoid (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_monoid (F i)]
[∀ i : γ, topological_add_monoid (F i)] : 
topological_add_monoid (Π i, F i) := sorry 
```

#### [Kevin Buzzard (Jun 14 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080370):
I get these `maximum class-instance resolution depth has been reached ` errors

#### [Reid Barton (Jun 14 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080442):
I see

#### [Kevin Buzzard (Jun 14 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080848):
```lean
instance pi_topological_add_monoid (γ : Type) (F : γ → Type) 
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_monoid (F i)]
[∀ i : γ, topological_add_monoid (F i)] : 
topological_add_monoid (Π i, F i) := by pi_instance [pi.add_monoid,Pi.topological_space]

```

#### [Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080900):
I don't know what is to be done about that instance resolution loop (I'm pretty sure it has been discussed here before), but as a workaround you can specify the instance you want:
```lean
instance pi_topological_monoid (γ : Type) (F : γ → Type)
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
@topological_add_group (Π i, F i) _ (pi.add_group) := sorry
```

#### [Kevin Buzzard (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080902):
my suggestion doesn't work

#### [Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080925):
`pi.add_monoid` doesn't actually exist, that's why I switched back to `add_group`

#### [Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080931):
Of course, you could probably add it

#### [Kevin Buzzard (Jun 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081015):
If you replace your sorry with `{}` do you get the runaway typeclass?

#### [Reid Barton (Jun 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081038):
Yes

#### [Reid Barton (Jun 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081074):
I guess that's because it tried to look up a `topological_add_monoid` "parent" instance to extend, and then that fell into the same loop

#### [Reid Barton (Jun 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081137):
If I specify both `continuous_add` and `continuous_neg` (as `sorry`) then I don't get a loop.

#### [Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081299):
you're right :-)

#### [Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081300):
I love living life on the edge

#### [Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081302):
one false move

#### [Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081303):
runaway typeclass

#### [Reid Barton (Jun 14 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081317):
actually, that was apparently the original issue, too.
```lean
instance pi_topological_monoid (γ : Type) (F : γ → Type)
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
topological_add_group (Π i, F i) := {
  continuous_add := sorry,
  continuous_neg := sorry,
}
```
also works

#### [Kenny Lau (Jun 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081464):
```lean
lemma continuous_pi [topological_space α] [∀i, topological_space (π i)] {f : α → Πi:ι, π i}
  (h : ∀i, continuous (λa, f a i)) : continuous f :=
continuous_supr_rng $ assume i, continuous_induced_rng $ h i
```

#### [Kenny Lau (Jun 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081466):
might be useful

#### [Reid Barton (Jun 14 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081723):
I tried writing the actual instance but the loop came back :(

#### [Reid Barton (Jun 14 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081810):
It should just be `continuous_add := continuous_pi $ λ i, continuous.comp continuous_add' (continuous_apply i)`

#### [Reid Barton (Jun 14 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081827):
Er wait, no

#### [Reid Barton (Jun 14 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081851):
that's totally wrong

#### [Reid Barton (Jun 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082090):
OK

#### [Reid Barton (Jun 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082107):
`continuous_apply` has a totally extraneous argument `α` which makes it unusable. It should be
```lean
section pi
variables {ι : Type*} {π : ι → Type*}
lemma continuous_apply' [∀i, topological_space (π i)] (i : ι) :
  continuous (λp:Πi, π i, p i) :=
continuous_supr_dom continuous_induced_dom
end pi
```

#### [Reid Barton (Jun 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082114):
```lean
  continuous_add := continuous_pi $ λ i,
    continuous_add
      (continuous.comp continuous_fst (continuous_apply' i))
      (continuous.comp continuous_snd (continuous_apply' i))
```

#### [Reid Barton (Jun 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082327):
Alternatively,
```lean
  continuous_add := continuous_pi $ λ i,
    continuous.comp
      (continuous.prod_mk
        (continuous.comp continuous_fst (continuous_apply' i))
        (continuous.comp continuous_snd (continuous_apply' i)))
      continuous_add'
```
shows the formal structure a little better, because `continuous_add'` is the actual class method `topological_add_monoid.continuous_add`

#### [Reid Barton (Jun 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082403):
`continuous.comp` reads from left to right. First you build a pair by (first taking the first component, and then the `i`th component of that; first taking the second component, and then the `i`th component of that), and then you add them.

#### [Kevin Buzzard (Jun 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082567):
`continuous_neg := continuous_pi (λ i, continuous.comp _ (continuous_neg continuous_id)`

#### [Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082573):
but I need to fill in the `_`

#### [Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082585):
`continuous (λ (x : Π (i : γ), F i), x i)`

#### [Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082586):
Projection is continuous

#### [Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082588):
is what I need

#### [Kevin Buzzard (Jun 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082764):
and then we're either done

#### [Kevin Buzzard (Jun 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082771):
or we have a runaway instance

#### [Kevin Buzzard (Jun 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082791):
The topological structure on the product is defined as the coarsest topology which makes all the projection maps continuous

#### [Kevin Buzzard (Jun 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083035):
aah I see this is exactly this apply'

#### [Kevin Buzzard (Jun 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083037):
what is going on with apply? :-)

#### [Kevin Buzzard (Jun 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083126):
```lean
instance pi_topological_group (γ : Type) (F : γ → Type)
[∀ i : γ, topological_space (F i)]
[∀ i : γ, add_group (F i)]
[∀ i : γ, topological_add_group (F i)] :
@topological_add_group (Π i, F i) (Pi.topological_space) (pi.add_group) := {
continuous_add := continuous_pi $ λ i,
    continuous_add
      (continuous.comp continuous_fst (continuous_apply' i))
      (continuous.comp continuous_snd (continuous_apply' i)),
continuous_neg := continuous_pi (λ i, continuous.comp (continuous_apply' i) (continuous_neg continuous_id)
)
}
```

#### [Kevin Buzzard (Jun 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083155):
rofl

#### [Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083197):
```
continuous_apply :
  ∀ {α : Type u_1} {ι : Type u_2} {π : ι → Type u_3} [_inst_1 : topological_space α]
  [_inst_2 : Π (i : ι), topological_space (π i)] (i : ι), continuous (λ (p : Π (i : ι), π i), p i)
```

#### [Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083198):
I see what Reid means

#### [Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083202):
It's going to be pretty tough inferring what alpha is given that it's never mentioned :-)

#### [Johan Commelin (Jun 15 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128106193):
```quote
It's going to be pretty tough inferring what alpha is given that it's never mentioned :-)
```
I fixed this in my simplicial branch. But it hasn't made it into mathlib yet.

