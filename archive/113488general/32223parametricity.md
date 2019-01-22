---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32223parametricity.html
---

## [general](index.html)
### [parametricity](32223parametricity.html)

#### [Cyril Cohen (Nov 11 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147487744):
Hi, @**Johannes Hölzl** @**Mario Carneiro** @**Rob Lewis**,
I am debugging my -- very buggy -- parametricity plugin. Could you tell me the shortest way to get the name of an inductive type from the name of its recursor? (I found `environment.inductive_type_of` to get it from the name of a constructor, but I cannot find the same for the recursor, and taking just the namespace sounds dirty to me...)

#### [Johannes Hölzl (Nov 11 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147488000):
Hm, it looks like there is no other (easy) option. You can analyse the type of the recursor, and try to get the inductive type from this, but this is not easy: there is an arbitrary number of parameters, I guess you need to analyse the motive to figure out what is a parameter and what is the actual inductive value...

#### [Mario Carneiro (Nov 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491817):
For an arbitrary recursor accepted by `induction`, the type is a bunch of pis followed by `C a1 ... an` where `C` is a variable in the context. The type of this variable is a bunch of pis ending in `Type` or `Prop`, and the last argument should have the type `T b1 ... bn` where `T` is the type in question

#### [Mario Carneiro (Nov 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491835):
But if you know it's a builtin recursor the easiest way is just to knock off the last segment from the name

#### [Mario Carneiro (Nov 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491970):
Oh wait, that doesn't work for the nondependent recursors. I think you can always look at the last pi in the type, which will have type `T b1 ... bn`

#### [Mario Carneiro (Nov 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492002):
for example:
```
inductive T (α : Type) : Type → Prop
| mk1 : T nat
| mk2 : T α

#print T.rec
-- protected eliminator T.rec : ∀ {α : Type} {C : Type → Prop},
-- C ℕ → C α → ∀ {a : Type}, T α a → C a
#check @T.drec
-- T.drec : ∀ {α : Type} {C : Π (a : Type), T α a → Prop},
-- C ℕ _ → C α _ → ∀ {a : Type} (n : T α a), C a n
```
Note that the last pi in the type has `T α a` as its domain, where `T` is what you want

#### [Cyril Cohen (Nov 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492061):
Sure I know where to get the the type of the inductive from the type of the recursor, but I was looking for a primitive that I think is missing from the API... What does not work for nondependent recursors?

#### [Mario Carneiro (Nov 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492067):
I think if we can figure it out there is no need for an API function

#### [Mario Carneiro (Nov 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492068):
we can add it to mathlib

#### [Cyril Cohen (Nov 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492136):
an API function would always be more efficient than retro-engineering... since the recursor is generated when the inductive type is added it should be indexed in the same way the constructors are...

#### [Mario Carneiro (Nov 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492146):
the API function would do what I just said, this information is not stored

#### [Cyril Cohen (Nov 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492191):
at least it would be coded in C++... meh I guess for my use case efficiency does not matter, but it's a matter of uniformity

#### [Cyril Cohen (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492196):
anyway, take the number of parameters + 1 pis out, then take the next pi, take its head symbol, done

#### [Mario Carneiro (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492199):
sure but you could say that about anything

#### [Cyril Cohen (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492201):
oh + the number of constructors

#### [Mario Carneiro (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492203):
well you can't get the constructors until you know the type...

#### [Cyril Cohen (Nov 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492244):
oh right... so last pi then

#### [Mario Carneiro (Nov 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492249):
right

#### [Cyril Cohen (Nov 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492324):
```quote
sure but you could say that about anything
```
Since the API function is there for constructors, it should also be there for anything that is generated by adding an inductive, such as recursors. I think none or both should be part of the core api, that is all I am saying.

#### [Mario Carneiro (Nov 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492390):
I think that's reasonable, but, well, core is frozen

#### [Cyril Cohen (Nov 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492486):
Oh right, I forgot about that, sorry for the noise :thinking:

#### [Cyril Cohen (Nov 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147493073):
```lean
meta def environment.trailing_pi_type_of (env : environment) : expr → option name
 | (pi _ _ t b) := match b with
   | (pi _ _ _ _) := environment.trailing_pi_type_of b
   | _ := some t.get_app_fn.const_name
   end
 | _ := none

meta def environment.inductive_type_of_rec (env : environment) (n : name) : exceptional name := do
  decl ← env.get n,
  match env.trailing_pi_type_of decl.type with
  | some i := return i
  | none := exceptional.fail $ "inductive_type_of_rec: not a recursor " ++ to_string n
  end
```

#### [Cyril Cohen (Nov 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147493139):
or  for the second one:
```lean
meta def environment.inductive_type_of_rec (env : environment) (n : name) : option name :=
  match env.get n with
  | (exceptional.success decl) := env.trailing_pi_type_of decl.type
  | _ := none
  end
```

#### [Cyril Cohen (Nov 12 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147494991):
@**Mario Carneiro** @**Johannes Hölzl** @**Rob Lewis** I am confused by the output of `#print has_zero.zero` i.e. 
```lean
def has_zero.zero : Π (α : Type u) [c : has_zero α], α :=
λ (α : Type u) [c : has_zero α], [has_zero.zero c]
```
what construction is `[has_zero.zero c]` internally? I figured it is a "macro", but I cannot find its API... is it possible to get its expansion?

#### [Johannes Hölzl (Nov 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147495052):
its a projection. so the projection data you get out of `environment` should tell you what the inductive is and which position of the constructor it is from. The macro hides a application of the recursor.

#### [Cyril Cohen (Nov 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147496075):
Nevermind, I was looking for `environment.unfold_all_macros`

