---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19645caseseliminatingintotype.html
---

## [general](index.html)
### [cases eliminating into type](19645caseseliminatingintotype.html)

#### [Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691805):
I've just managed to internalise something Mario told me a couple of weeks ago.

#### [Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691809):
Here's the `cases` tactic in action.

#### [Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691811):
```lean
theorem T (γ : Type) (P : γ → Prop) (H : ∃ g : γ, P g) : 2 + 2 = 4 :=
begin
cases H with g Pg,
/- context now has
g : γ,
Pg : P g
-/
admit,
end 
```

#### [Kevin Buzzard (Apr 25 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691818):
Now here's an example of it failing because we need to use the axiom of choice.

#### [Kevin Buzzard (Apr 25 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691829):
```lean
definition D (γ : Type) (P : γ → Prop) (H : ∃ g : γ, P g) : Type :=
begin
-- cases H with g Pg -- fails as we can only eliminate into Prop
admit
end
```

#### [Kevin Buzzard (Apr 25 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691862):
But of course us classical people want to run cases anyway.

#### [Kevin Buzzard (Apr 25 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691880):
```lean
definition D (γ : Type) (P : γ → Prop) (H : ∃ g : γ, P g) : Type :=
begin
-- cases H with g Pg -- fails as we can only eliminate into Prop
let g := classical.some H,
have Pg : P g := classical.some_spec H, 
/- ... but I made it anyway. Context now 
g : γ := ...
Pg : P g 
-/
admit 
end 
```

#### [Kevin Buzzard (Apr 25 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691969):
Using this trick (classical some and some_spec, *plus* the thing which I think Mario was trying to explain to me, which was that the moment you run `classical.some` you should make something _useful_ from `classical.some_spec` rather than just `have Pg := classical.some_spec H` which is a statement about `classical.some _` and hence harder to work with.

#### [Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691997):
I am going to use this idiom again and again

#### [Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692002):
but surely this should just be a tactic

#### [Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692011):
`classical_cases H with g Pg`

#### [Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692082):
I have been fretting a bit over things like the fact that the "obvious in maths" statement that if there's a surjection `X -> Y` then there's an injection `Y -> X` looks so convoluted in Lean.

#### [Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692096):
But this tactic is probably trivial to write and just looks like an extension of `cases`, which the students learn very early on when learning Lean anyway

#### [Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692105):
Is this there already?

#### [Kevin Buzzard (Apr 25 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692161):
If not -- I _really_ think it should be! It is far more natural to write than all this classical.some_spec or indefinite_confusion or whatever it's called

#### [Kevin Buzzard (Apr 25 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692256):
Let me stress that the trick is that you force the type of `Pg` to be `P g`, the thing you want it to be, by explicitly making it of this type when you construct it. Just writing `have Pg := classical.some_spec H` doesn't work.

#### [Reid Barton (Apr 25 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692355):
Maybe `choose` for the tactic name?

#### [Simon Hudon (Apr 25 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692512):
Have a look at https://github.com/unitb/lean-lib/blob/master/test/tactic/classical.lean . It is not quite behaving like `cases` but it does make `some` and `epsilon` easier to work with. (I linked to the test case so that you see how I use it rather than how it works).

#### [Kevin Buzzard (Apr 25 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693176):
How do I use `apply_some_spec` Simon? I mean how do I get it running on my machine?

#### [Simon Hudon (Apr 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693242):
```
leanpkg add unitb/lean-lib
```

and don't forget:

```
import util.classical
```

#### [Kevin Buzzard (Apr 25 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693530):
```lean
open function
theorem inj_of_surj (X Y : Type) (f : X → Y) (Hf : surjective f) : ∃ g : Y → X, f ∘ g = id :=
begin
existsi _, --slightly weird first move
tactic.swap, -- ha ha, swap is now overloaded because I opened function!
{ intro y,
  --classical_cases (Hf y) with x Hx,
  let x := classical.some (Hf y),
  have Hx : f x = y := classical.some_spec (Hf y),
  exact x
},
{ funext y,
  --classical_cases (Hf y) with x Hx,
  let x := classical.some (Hf y),
  have Hx : f x = y := classical.some_spec (Hf y),
  exact Hx
}
end 
```

#### [Kevin Buzzard (Apr 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693535):
I think my way looks a bit less intimidating for the newbie

#### [Simon Hudon (Apr 26 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125695647):
You can do it like this:

```lean
namespace tactic
namespace interactive

open interactive interactive.types

meta def ccases (e : parse cases_arg_p) (ids : parse with_ident_list) :=
do cases (e.1,``(classical.indefinite_description _ %%(e.2))) ids

end interactive
end tactic

open function
theorem inj_of_surj (X Y : Type) (f : X → Y) (Hf : surjective f) : ∃ g : Y → X, f ∘ g = id :=
begin
split, --slightly weird first move
tactic.swap, -- ha ha, swap is now overloaded because I opened function!
{ intro y,
  ccases (Hf y) with x Hx,
  exact x
},
{ funext y,
  ccases (Hf y) with x Hx,
  -- let x := classical.some (Hf y),
  -- have Hx : f x = y := classical.some_spec (Hf y),
  simp,
  exact Hx
}
end
```

#### [Mario Carneiro (Apr 26 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696083):
Lol @ indefinite_confusion. But the right way to do this is to do cases on the pair `some, some_spec`, which is indeed `classical.indefinite_description`.

#### [Mario Carneiro (Apr 26 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696468):
Here's an idea that might help:
```
@[elab_as_eliminator]
noncomputable def classical.rec_on
  {α} {p : α → Prop} {C : Sort*}
  (h : ∃ a, p a) (H : ∀ a, p a → C) : C :=
H (classical.some h) (classical.some_spec h)
```

#### [Mario Carneiro (Apr 26 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696509):
You can `apply` that theorem to do cases on an exists without making `cases` complain

#### [Kenny Lau (Apr 26 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696540):
@**Kevin Buzzard** what if I told you “surjective functions have right inverse” is already in mathlib as `inv_fun`

#### [Mario Carneiro (Apr 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696553):
But in the case of `inj_of_surj`, this is the wrong approach (same for `ccases` or cases on indefinite description), because you are doing the case twice, once to define the function and again to give its properties. That means that you will have to unfold whatever proof term you constructed in the first half, i.e. `classical.rec_on` or `subtype.rec_on` or something

#### [Mario Carneiro (Apr 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696594):
The right solution here is to use `axiom_of_choice`

#### [Mario Carneiro (Apr 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696615):
```
theorem inj_of_surj (X Y : Type) (f : X → Y) (Hf : surjective f) : ∃ g : Y → X, f ∘ g = id :=
let ⟨g, h⟩ := classical.axiom_of_choice Hf in ⟨g, funext h⟩

#### [Mario Carneiro (Apr 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696623):
(Also this theorem already exists in core IIRC)

#### [Mario Carneiro (Apr 26 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125697084):
For the golfers:
```
(classical.axiom_of_choice Hf).imp $ λ g, funext
```

#### [Kevin Buzzard (Apr 26 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711834):
The inj of surj example was pedagogical -- I know it's there, but I want to teach students how to write it without pain. There are other times this comes up too. I suspect a lot of undergraduate mathematicians will be very confused by constructive maths so I want to hide it from them. Many thanks for the tactic Simon and for the comments everyone.

#### [Mario Carneiro (Apr 26 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711847):
I think in particular that you should add `axiom_of_choice` to your toolkit

#### [Kevin Buzzard (Apr 26 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711911):
You are certainly right in that it's not currently in my toolkit.

#### [Kevin Buzzard (Apr 26 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711913):
I remember really struggling with all of this the first time around.

#### [Kevin Buzzard (Apr 26 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711954):
It's only revisiting it now I'm older and wiser that I understand it well enough to try and manipulate it into a form which I think beginners with no programming background might find more comprehensible.

#### [Mario Carneiro (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711961):
I would think that `axiom_of_choice` is the version of choice people are most used to

#### [Mario Carneiro (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711965):
`classical.some` is more like global choice, which ZFC doesn't usually admit so most proofs aren't framed that way

#### [Kevin Buzzard (Apr 26 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712014):
The problem is that most mathematicians apply the axiom of choice without noticing, and those that are aware of it believe that it says that an infinite product of non-empty sets is non-empty.

#### [Kevin Buzzard (Apr 26 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712015):
Mathematicians don't know the difference between the different kinds of non-empty

#### [Mario Carneiro (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712022):
I'm not talking about LEM here though

#### [Kevin Buzzard (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712027):
right

#### [Mario Carneiro (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712028):
all notions of nonempty are basically the same modulo LEM

#### [Kevin Buzzard (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712031):
they don't know what LEM is either

#### [Mario Carneiro (Apr 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712063):
I'm talking about how to use AC proper

#### [Mario Carneiro (Apr 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712073):
I think it is not a good thing that lean thinks LEM and AC are the same

#### [Mario Carneiro (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712074):
mathematicians certainly don't

#### [Mario Carneiro (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712081):
you can argue that mathematicians think both are true, but I think they admit LEM implicitly and don't see the need for AC until they reach a certain level

#### [Kevin Buzzard (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712082):
exactly

#### [Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712084):
LEM is part of the logic

#### [Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712121):
AC has some content

#### [Mario Carneiro (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712127):
Lean kind of gives you the ability to distinguish the two, since LEM is computable but AC is not

