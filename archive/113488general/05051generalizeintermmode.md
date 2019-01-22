---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05051generalizeintermmode.html
---

## [general](index.html)
### [generalize in term mode](05051generalizeintermmode.html)

#### [Kenny Lau (Apr 21 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497304):
```lean
@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x
```
I have made a `generalize` in term mode

#### [Kenny Lau (Apr 21 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497307):
let's say this is the goal:
```lean
refl_trans red x z → (∃ (w : α), refl_trans (refl_trans red) y w ∧ refl_trans (refl_trans red) z w)
```

#### [Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497313):
doing `generalize z _` will give you this on the underscore:

#### [Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497314):
```lean
⊢ ∀ (x_1 : α),
    refl_trans red x x_1 → (∃ (w : α), refl_trans (refl_trans red) y w ∧ refl_trans (refl_trans red) x_1 w)
```

#### [Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497315):
is this a good idea?

#### [Kenny Lau (Apr 21 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497412):
example:
```lean
@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

variables {α : Type*} (red : α → α → Prop) {x y z : α}

inductive refl_trans : α → α → Prop
| refl {x} : refl_trans x x
| step_trans {x y z} : red x y → refl_trans y z → refl_trans x z

@[trans] theorem refl_trans.trans (H : refl_trans red x y) :
  refl_trans red y z → refl_trans red x z :=
generalize z $ refl_trans.rec_on H (λ x z H, H) $ λ x y z hxy hyz ih w hzw,
refl_trans.step_trans hxy $ ih w hzw
```

#### [Kenny Lau (Apr 21 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497413):
@**Simon Hudon** @**Patrick Massot** what do you guys think?

#### [Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497453):
I'm afraid I still have to learn what the tactic mode `generalize` is good for

#### [Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497454):
I'm very curious because it came up a lot recently

#### [Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497455):
But I can't learn everything at the same time

#### [Kenny Lau (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497456):
well you know how `induction` works with `generalizing` right

#### [Patrick Massot (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497457):
No I don't

#### [Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497462):
hmm

#### [Patrick Massot (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497463):
I only do induction on natural numbers

#### [Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497464):
so when you're proving that natural number addition is commutative

#### [Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497465):
you want to prove that x+y=y+x

#### [Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497466):
you induct on the proposition `\forall y, x+y=y+x` instead

#### [Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497467):
(and you prove the base case and inductive step both by induction)

#### [Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497504):
(I call this "double induction')

#### [Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497509):
the very action of moving the goalpost from `x+y=y+x` to `\forall y, x+y=y+x` is called generalizing

#### [Kenny Lau (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497518):
https://math.stackexchange.com/a/2438135/328173

#### [Kenny Lau (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497520):
here is it in Fitch style (only part 1 is relevant)

#### [Simon Hudon (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497664):
@**Kenny Lau** I'll have to get back to you a bit later. My nephew just arrived

#### [Kenny Lau (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497665):
ok

#### [Patrick Massot (Apr 21 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497882):
I can understand why you used your Kenny identity to post such an answer

#### [Patrick Massot (Apr 21 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497883):
Thanks for the explanation

#### [Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497888):
```lean
@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

namespace xnat

def add : xnat → xnat → xnat
| x zero := x
| x (succ y) := succ $ add x y

theorem add_comm {x y : xnat} : add x y = add y x :=
generalize y $ xnat.rec_on x
  (λ y, xnat.rec_on y rfl $
     λ y ih, show succ _ = succ _, from congr_arg succ ih)
  (λ y ih1 z, xnat.rec_on z
     (show succ _ = succ _, from congr_arg succ $ ih1 zero)
     (λ z ih2, congr_arg succ $ ih2.trans $ eq.trans
       (show succ _ = succ _, from congr_arg succ (ih1 z).symm) (ih1 $ succ z)))

end xnat
```

#### [Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497890):
@**Patrick Massot** somehow it took me a long time to prove this

#### [Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497891):
but here you go

#### [Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497892):
why did I use my Kenny identity to post such an answer?

#### [Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497894):
and you can see that `generalize` is necessary because I used `ih1` twice

#### [Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497934):
I should make `show` a term-tactic

#### [Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497935):
well that won't really be necessary, forget that

#### [Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497936):
but I like my `generalize`

#### [Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497937):
a tactic in term mode

#### [Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497938):
(a tactic, here, is one which converts your goal to something useful)

#### [Kenny Lau (Apr 21 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497945):
@**Mario Carneiro** do you think it is a good idea? I have too many `aux` theorems in my `free_group.lean` that can be eliminated by my new invention :P

#### [Kenny Lau (Apr 21 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497946):
assuming that it is an invention

#### [Kenny Lau (Apr 21 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497988):
bonus points! `generalize` also works as `revert`

#### [Kenny Lau (Apr 21 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497993):
```lean
@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

example (x y : nat) (H : x = y) : false :=
generalize H _

/-
don't know how to synthesize placeholder
context:
x y : ℕ,
H : x = y
⊢ x = y → false
-/
```

#### [Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499063):
I think I made a mistake. What I have built is really `revert`

#### [Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499065):
Here's the real `generalize`:

#### [Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499066):
```lean
@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl

example (m n : nat) : m + n = 0 :=
generalize (m + n) _

/-
don't know how to synthesize placeholder
context:
m n : ℕ
⊢ ∀ (z : ℕ), m + n = z → z = 0
-/
```

#### [Chris Hughes (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499110):
I always wondered how to revert in term mode, however not sure I've ever had to do it.

#### [Kenny Lau (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499111):
thanks for your appreciation

#### [Kenny Lau (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499112):
so, for the sake of completeness:
```lean
@[elab_as_eliminator] def revert
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl
```

#### [Andrew Ashworth (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499155):
in the old days when we didn't have a tactic mode you'd revert using clever `heq` tricks

#### [Chris Hughes (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499158):
Usually I just do this.
```lean
theorem add_comm {x : xnat} : ∀ {y}, add x y = add y x :=
xnat.rec_on x
  (λ y, xnat.rec_on y rfl $
     λ y ih, show succ _ = succ _, from congr_arg succ ih)
  (λ y ih1 z, xnat.rec_on z
     (show succ _ = succ _, from congr_arg succ $ @ih1 zero)
     (λ z ih2, congr_arg succ $ ih2.trans $ eq.trans
       (show succ _ = succ _, from congr_arg succ (@ih1 z).symm) (@ih1 $ succ z)))
```

#### [Kenny Lau (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499159):
right, that's what I did in my free group file

#### [Kenny Lau (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499160):
until I realized that I can build tactics in term mode

#### [Andrew Ashworth (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499199):
does your generalize use `heq` under the hood?

#### [Chris Hughes (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499200):
Are there any examples where you can't just do that?

#### [Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499201):
@**Chris Hughes** so my file has a lot of auxiliary theorems

#### [Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499202):
```lean
theorem red.trans.aux (H12 : red L₁ L₂) : ∀ {L₃}, red L₂ L₃ → red L₁ L₃ :=
red.rec_on H12 (λ _ _, id) $ λ _ _ _ H1 H2 ih L₃ H23,
red.step_trans H1 $ ih H23

@[trans] theorem red.trans (H12 : red L₁ L₂) (H23 : red L₂ L₃) : red L₁ L₃ :=
red.trans.aux H12 H23
```

#### [Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499203):
now I can do it in one go:

#### [Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499204):
```lean
@[trans] theorem red.trans (H12 : red L₁ L₂) (H23 : red L₂ L₃) : red L₁ L₃ :=
revert H23 $ revert L₃ $
red.rec_on H12 (λ _ _, id) $ λ _ _ _ H1 H2 ih L₃ H23,
red.step_trans H1 $ ih _ H23
```

#### [Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499210):
@**Andrew Ashworth** are we talking about the same `heq`, i.e. the `heq` as in Lean? I don't know Coq at all. I showed you my code above though.

#### [Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499211):
@**Chris Hughes** not that I'm aware of

#### [Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499212):
I just built that an hour ago, I don't know everything about it

#### [Andrew Ashworth (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499213):
yeah, because in Coq it'd be `JMeq`, heh

#### [Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499214):
```lean
@[elab_as_eliminator] def revert
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl
```

#### [Kenny Lau (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499237):
I don't see any `heq` here

#### [Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499254):
when you print an example that uses generalize

#### [Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499255):
do you get a `heq` term

#### [Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499257):
it may or may not, i'm just curious

#### [Chris Hughes (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499259):
You can just do some extra lambdas. i.e
`theorem red.trans.aux  : ∀ {L₃}, red L₁ L₂ → red L₂ L₃ → red L₁ L₃`
What's wrong with that?

#### [Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499262):
I need to rec on the first red

#### [Chris Hughes (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499269):
I see. Makes a lot of sense then.

#### [Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499270):
```lean
@[elab_as_eliminator] def revert
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl

theorem test (m n : nat) : m + n = 0 :=
generalize (m + n) $ λ z hz, sorry

set_option pp.all true
#print test

/-
theorem test : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=
λ (m n : nat),
  @generalize.{1 0} nat (λ (_x : nat), @eq.{1} nat _x (@has_zero.zero.{0} nat nat.has_zero))
    (@has_add.add.{0} nat nat.has_add m n)
    (λ (z : nat) (hz : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)
-/
```

#### [Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499271):
@**Andrew Ashworth** is this what you're talking about?

#### [Chris Hughes (Apr 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499317):
@**Andrew Ashworth** Are you talking about Kenny's generalize or tactics mode generalize?

#### [Kenny Lau (Apr 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499320):
in that case:
```lean
@[elab_as_eliminator] def revert
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl

theorem test (m n : nat) : m + n = 0 :=
generalize (m + n) $ λ z hz, sorry

set_option pp.all true
#print test

/-
theorem test : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=
λ (m n : nat),
  @generalize.{1 0} nat (λ (_x : nat), @eq.{1} nat _x (@has_zero.zero.{0} nat nat.has_zero))
    (@has_add.add.{0} nat nat.has_add m n)
    (λ (z : nat) (hz : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)
-/

theorem test' (m n : nat) : m + n = 0 :=
begin
  generalize h : m + n = z,
  admit
end

#print test'

/-
theorem test' : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=
λ (m n : nat),
  (λ (z : nat) (h : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)
    (@has_add.add.{0} nat nat.has_add m n)
    (@rfl.{1} nat (@has_add.add.{0} nat nat.has_add m n))
-/
```

#### [Andrew Ashworth (Apr 21 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499409):
hm, interesting, i'd have to dig further when I have time

#### [Kenny Lau (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499416):
thanks for your appreciation

#### [Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499417):
`heq` is important when doing dependent case analysis, which is why i was expecting heq to show up in the term there somewhere

#### [Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499418):
it's probably buried in there somewhere... maybe... underneath one of the definitions

#### [Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499419):
it's quite a low-level idea

#### [Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499421):
or i could be really wrong about how lean works, and that also wouldn't surprise me

#### [Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499422):
so, eh, which one?

#### [Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499463):
`eq` is already an inductive type

#### [Andrew Ashworth (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499464):
i can't say because i'm a lean scrub

#### [Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499465):
it doesn't depend on `heq`

#### [Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499467):
I don't think it uses `heq` anywhere

#### [Chris Hughes (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499522):
Here's an alternative method
```lean
theorem add_comm {x y : xnat} : add x y = add y x :=
xnat.rec_on x
  (λ y, xnat.rec_on y rfl $
     λ y ih, show succ _ = succ _, from congr_arg succ ih)
  (λ y ih1 z, xnat.rec_on z
     (show succ _ = succ _, from congr_arg succ $ @ih1 zero)
     (λ z ih2, congr_arg succ $ ih2.trans $ eq.trans
       (show succ _ = succ _, from congr_arg succ (@ih1 z).symm) (@ih1 $ succ z))) y

```

#### [Andrew Ashworth (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499524):
sure, and why that might be is interesting to me, most other tactics in coq that do this sort of thing use `heq`

#### [Andrew Ashworth (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499525):
https://coq.inria.fr/refman/proof-engine/detailed-tactic-examples.html

#### [Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499568):
@**Chris Hughes** interesting. usually it fails if I put `y` at the end

#### [Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499571):
I still like my method more :P

#### [Chris Hughes (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499572):
I was expecting it not to work.

#### [Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499574):
did you do anything more than my eyes could see

#### [Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499575):
I can't really tell if you changed anything in the middle

#### [Chris Hughes (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499576):
No.

#### [Kenny Lau (Apr 21 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499579):
very curious indeed

#### [Kenny Lau (Apr 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500272):
more examples: https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a

#### [Patrick Massot (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500481):
Congratulations!

#### [Patrick Massot (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500485):
Two docstrings is a very good start!

#### [Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500486):
:P

#### [Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500488):
I was making docstrings

#### [Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500490):
and then I got carried away by `revert` and `generalize`

#### [Kenny Lau (Apr 22 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521584):
@**Mario Carneiro** do you like this?

#### [Kenny Lau (Apr 22 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521591):
recap:
```lean
@[elab_as_eliminator] def revert
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π x, β x) → β x :=
λ H, H x

@[elab_as_eliminator] def generalize
  {α : Sort*} {β : α → Sort*} (x : α) :
  (Π z, x = z → β z) → β x :=
λ H, H x rfl
```

#### [Mario Carneiro (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521631):
I'm not sure I buy the particular applications you've used it for, but this seems okay for `logic.basic`

#### [Mario Carneiro (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521632):
probably should be `reducible`

#### [Kenny Lau (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521633):
woohoo, tactics in term mode

#### [Mario Carneiro (Apr 22 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521638):
I mean, you can use `match` to the same effect

#### [Mario Carneiro (Apr 22 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521640):
but I usually just set up my intros in the right order so this isn't needed

#### [Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521641):
right, but setting up them make for a bunch of auxiliary theorems

#### [Mario Carneiro (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521682):
not in my experience

#### [Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521683):
https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a

#### [Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521684):
here

#### [Mario Carneiro (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521691):
why don't you use the equation compiler?

#### [Kenny Lau (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521693):
that also needs to be auxiliary

#### [Mario Carneiro (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521694):
for `red.trans`

#### [Kenny Lau (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521695):
because `rec_on` is shorter

#### [Mario Carneiro (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521739):
eww

#### [Kenny Lau (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521740):
I thought someone likes short proofs

#### [Mario Carneiro (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521742):
I like straightforward proofs

#### [Mario Carneiro (Apr 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521749):
the equation compiler makes it really clear how an induction proceeds, and what is the IH

#### [Mario Carneiro (Apr 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521751):
plus, I very much doubt you recouped the loss of having to state an auxiliary

#### [Mario Carneiro (Apr 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521794):
We haven't talked about it much since they appear to be going extinct, but it's possible to write brittle term proofs too

#### [Mario Carneiro (Apr 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521797):
this was a big problem in lean 2

#### [Mario Carneiro (Apr 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521838):
when you do a proof with lots of omitted type information relying on lean to pick up the pieces, if something changes in the unification algorithm or something it can be very difficult to understand the broken proof

