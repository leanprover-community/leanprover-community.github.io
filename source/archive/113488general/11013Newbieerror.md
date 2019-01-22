---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11013Newbieerror.html
---

## [general](index.html)
### [Newbie error](11013Newbieerror.html)

#### [Johan Commelin (May 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254021):
I've got the following code
```lean
import algebra.ring data.finsupp

variables {R : Type*} [ring R]

section free_module
definition free_module (S : Type*) := finsupp S R
variables {S : Type*}

instance : module R (free_module S) := sorry

end free_module
```

#### [Johan Commelin (May 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254025):
And this is the error
```
don't know how to synthesize placeholder
context:
R : Type u_1,
_inst_1 : ring R,
S : Type u_2
⊢ Type ?
```

#### [Johan Commelin (May 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254034):
Aah, I should point out that the red squiggles are under `free_module` in the line with `sorry`

#### [Mario Carneiro (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254076):
Shouldn't `R` be explicit in `free_module`? It is not inferrable

#### [Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254077):
I think the error means that it can't figure out in which universe `free_module S` lives

#### [Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254085):
Aah, Ok, is that the problem. I thought it was automatically included, since I declared it a variable

#### [Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254090):
Or should I then use `()` instead of `{}`

#### [Kenny Lau (May 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254096):
it isn't a parameter

#### [Mario Carneiro (May 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254097):
it is included, but the later use might refer to a different `R`

#### [Johan Commelin (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254154):
Ok... well, that fixed my problem. Thanks a lot!

#### [Kenny Lau (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254155):
no, don't use parameter

#### [Kenny Lau (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254158):
you won't be able to use it once you leave the section

#### [Johan Commelin (May 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254203):
Hmm, what do you mean?

#### [Johan Commelin (May 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254205):
I now have
```lean
import algebra.ring data.finsupp

variables {R : Type*} [ring R]

section free_module
definition free_module (R : Type*) [ring R] (S : Type*) := finsupp S R
variables {S : Type*}

instance : module R (free_module R S) :=
begin
split, -- tactic fails
end

end free_module
```

#### [Johan Commelin (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254209):
Is that wrong?

#### [Kenny Lau (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254214):
never mind

#### [Kenny Lau (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254216):
that isn't wrong

#### [Johan Commelin (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254219):
Ok, I don't mind learning a better way (-;

#### [Johan Commelin (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254265):
So, why is `split` failing? I expected to get 4 goals, according to the 4 axioms of a module

#### [Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254270):
constructor

#### [Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254273):
but you don't want to use it since it `extends` something

#### [Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254279):
maybe if you really want to stay in tactic mode, do `refine {..}`

#### [Johan Commelin (May 08 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254482):
Well, I don't *want* to stay in tactic mode. It is just that I have no clue how to do things in term mode. And tactic mode helps me a bit (-;

#### [Johan Commelin (May 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254761):
So what would be the proper way to prove this `instance`?

#### [Kenny Lau (May 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254774):
```lean
instance : module R (free_module R S) :=
{ smul := _,
  smul_add := _ }
```
etc

#### [Johan Commelin (May 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254830):
Ok, thanks! I'll try to do that.

#### [Johan Commelin (May 08 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126255445):
Lol, this is already in `finsupp`: `to_module`

#### [Kenny Lau (May 08 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126255448):
lol

#### [Johan Commelin (May 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256750):
The errors continue:
```lean
import algebra.ring data.finsupp

variables {R : Type*} [decidable_eq R] [ring R]

section free_module
definition free_module (R : Type*) [ring R] (S : Type*) := finsupp S R
variables {S : Type*} [decidable_eq S]

instance : add_comm_monoid (free_module R S) := finsupp.add_comm_monoid
instance : module R (free_module R S) := finsupp.to_module
end free_module

section generators
variables {M : Type*} [module R M]

definition natural_map (S : set M) : free_module R S → M :=
λ x, x.sum (λ s r, r • s)

definition generated_submodule (S : set M) := set.range (natural_map S) -- fails

definition is_finitely_generated (M : Type*) [module R M] : Prop :=
∃ S : finset M, generated_submodule {x | x ∈ S} = set.univ M -- fails

end generators
```

#### [Johan Commelin (May 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256792):
Errors:
```
generators.lean:19:57: error

failed to synthesize type class instance for
M : Type u_2,
S : set M
⊢ module ?m_1 M
generators.lean:19:57: error

don't know how to synthesize placeholder
context:
M : Type u_2,
S : set M
⊢ Type ?
```

#### [Johan Commelin (May 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256799):
But I am telling it that M is a module over R, so why can't it unify `?m_1` with `R`?

#### [Kevin Buzzard (May 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258817):
You started a new section so Lean has forgotten about the variable R

#### [Kevin Buzzard (May 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258821):
wait

#### [Kevin Buzzard (May 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258825):
that doesn't seem to be true

#### [Kevin Buzzard (May 08 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258898):
It seems to be because you don't ever mention R so the type class inference doesn't kick in

#### [Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258966):
`definition generated_submodule (S : set M) [module R M] := set.range (natural_map S) -- works`

#### [Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258971):
Type class inference is a strange thing

#### [Kenny Lau (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258973):
include R

#### [Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258974):
I would still not say I had completely got the hang of it

#### [Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258979):
```lean
include R
definition generated_submodule (S : set M) := set.range (natural_map S) -- works
```

#### [Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259016):
Kenny's fix

#### [Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259021):
What does `include` do?

#### [Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259026):
I thought this was for including variable names in tactic proofs

#### [Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259037):
As for the equality failing

#### [Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259038):
`set.univ : Π {α : Type u}, set α`

#### [Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259041):
`set.univ` doesn't take `M`, it guesses it.

#### [Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259081):
```lean
definition is_finitely_generated (M : Type*) [module R M] : Prop :=
∃ S : finset M, generated_submodule {x | x ∈ S} = set.univ -- works
```

#### [Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259083):
Recently I realised that I pretty fully understood most Lean errors

#### [Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259086):
i.e. I can look at the error and actually figure out what is wrong with my code, in many cases

#### [Kevin Buzzard (May 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259096):
```
type mismatch at application
  generated_submodule {x : M | x ∈ S} = set.univ M
term
  set.univ M
has type
  Prop : Type
but is expected to have type
  set M : Type ?
```

#### [Kevin Buzzard (May 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259103):
says "the right hand side is supposed to have type `set M` but it has type `Prop` so you have not written what you meant to write -- it doesn't typecheck."

#### [Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259146):
You are attempting to assert that two sets are equal

#### [Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259147):
so the correct type is `set M`

#### [Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259149):
so the problem is that `set.univ M` has type Prop instead of type `set M`

#### [Kevin Buzzard (May 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259156):
and now you look at what `set.univ` actually does by hovering your mouse over `set.univ`

#### [Kevin Buzzard (May 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259159):
and you see your error

#### [Kevin Buzzard (May 08 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259207):
I would urge you @**Johan Commelin** to learn to read errors so you can find out the problem.

#### [Kevin Buzzard (May 08 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259211):
Sometimes the problem is that type class inference has failed. Type class inference is just something you have to get the hang of and I had to ask and ask here about it -- see my typeclass inference woes thread

#### [Kevin Buzzard (May 08 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259224):
But for other errors, try and make it so that there is exactly one error (i.e put sorry everywhere else) and then try and read the error.

#### [Kevin Buzzard (May 08 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259266):
And then hope that you can fix it

#### [Johan Commelin (May 08 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259847):
Ok, thanks! I hope to get the hang of it as well...

#### [Chris Hughes (May 08 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126266575):
`set.univ : set M` should help

#### [Chris Hughes (May 08 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126266785):
Or perhaps `@set.univ M`

