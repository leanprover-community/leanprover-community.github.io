---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88287tryingtounderstandcc.html
---

## Stream: [general](index.html)
### Topic: [trying to understand cc](88287tryingtounderstandcc.html)

---

#### [Johan Commelin (Apr 24 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602905):
I had hoped this would work:
```lean
universes u

variables
{A : Type u} [group A]
{B : Type u} [group B]
{f : A → B} [is_group_hom f]

lemma test (hf : ∀ x, (f x = 1 → x = 1)) (x : A) (hfx : f x = 1) : x = 1 :=
begin
cc
end 
```

#### [Johan Commelin (Apr 24 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602950):
So which tactic do I need here?

#### [Simon Hudon (Apr 24 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602958):
That's not the kind of stuff it does. Try:

```
import tactic -- from mathlib

lemma ... := by solve_by_elim
```

#### [Johan Commelin (Apr 24 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603006):
Next goal: just have `hf : function.injective f` as hypothesis

#### [Johan Commelin (Apr 24 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603018):
Instead of unpacking that definition myself...

#### [Simon Hudon (Apr 24 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603023):
Have you tried it?

#### [Johan Commelin (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603067):
Yes. Then it fails:
```lean
universes u

variables
{A : Type u} [group A]
{B : Type u} [group B]
{f : A → B} [is_group_hom f]

lemma test (hf : function.injective f) (x : A) (hfx : f x = 1) : x = 1 :=
begin
solve_by_elim
end 
```

#### [Johan Commelin (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603074):
squiggles under `solve_by_elim`

#### [Simon Hudon (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603076):
What error message does it give you?

#### [Johan Commelin (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603130):
```
assumption tactic failed
state:
A : Type u,
_inst_1 : group A,
B : Type u,
_inst_2 : group B,
f : A → B,
_inst_3 : is_group_hom f,
hf : function.injective f,
x : A,
hfx : f x = 1
⊢ x = 1
```

#### [Kenny Lau (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603131):
to be fair the proof needs to go like f x = f 1 and then x = 1

#### [Kenny Lau (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603133):
and it needs is_group_hom.one

#### [Johan Commelin (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603138):
Yeah, there is a bit more to be done... but I think there should be a tactic that can do that for me

#### [Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603146):
Ideally there is a `diagram_chase` tactic

#### [Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603147):
And I think `cc` is very close to that

#### [Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603149):
It only needs to know little facts like this lemma and some similar stuff.

#### [Kenny Lau (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603150):
try mixing is_group_hom.one into the ingredient

#### [Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603152):
And then it would be able to prove the five lemma on its own

#### [Kenny Lau (Apr 24 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603198):
have := is_group_hom.one f; solve_by_elim

#### [Johan Commelin (Apr 24 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603210):
That's not enough

#### [Johan Commelin (Apr 24 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603215):
Alas

#### [Simon Hudon (Apr 24 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603273):
This one should work:

```lean
lemma test (hf : function.injective f) (x : A) (hfx : f x = 1) : x = 1 :=
begin
  have := is_group_hom.one f,
  apply hf, cc,
end
```

#### [Johan Commelin (Apr 24 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603276):
Ok, so `have := \fo x, (fx = 1 \to x = 1)`. How should I prove that? Is it a one-liner?

#### [Johan Commelin (Apr 24 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603286):
@**Simon Hudon** Nice!

#### [Kenny Lau (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603335):
@**Simon Hudon** I don’t get it at all

#### [Simon Hudon (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603337):
If you want to go fully anonymous (not name your assumptions like `this` and `hf`) you can do:

```
begin
  have := is_group_hom.one f,
  apply_assumption, cc
end
```

#### [Kenny Lau (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603339):
how does apply hf even succeed

#### [Kenny Lau (Apr 24 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603349):
oh nvm I thought wrongly

#### [Simon Hudon (Apr 24 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603401):
You apply it to `x = 1` and `hf ` is `hf : ∀ x y, f x = f y → x = y`. When you apply it, you instantiate it with `x := x, y := 1` so the antecedent becomes `f x = f 1`. Your idea with `have` gets us `this : f 1 = 1`

#### [Kenny Lau (Apr 24 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603402):
I mean, I would just write the proof in term mode

#### [Simon Hudon (Apr 24 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603410):
I think I would keep `cc` at the very least.

#### [Simon Hudon (Apr 24 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603418):
```quote
Ok, so `have := \fo x, (fx = 1 \to x = 1)`. How should I prove that? Is it a one-liner?
```
Did you find an answer for this?

#### [Johan Commelin (Apr 24 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603474):
Not yet, Lean doesn't like that expression

#### [Simon Hudon (Apr 24 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603523):
Error message?

I would expect it to work but I don't think that's what you're looking for

#### [Johan Commelin (Apr 24 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603526):
And the problem is not `fx`, I changed that to `f x`

#### [Johan Commelin (Apr 24 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603532):
`invalid expression starting at xx:y`

#### [Simon Hudon (Apr 24 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603536):
`have := expr` uses `expr` as a proof of an unnamed proposition. That proposition is just the type of the expression. If `expr` is the proposition you want to prove, you write `have : expr`

#### [Simon Hudon (Apr 24 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603582):
Can you show me the whole proof? Maybe you missed a comma

#### [Johan Commelin (Apr 24 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603594):
```lean
universes u

variables
{A : Type u} [group A]
{B : Type u} [group B]
{f : A → B} [is_group_hom f]

lemma test (hf : function.injective f) (x : A) (hx : x ∈ ker f) : x = 1 :=
begin
have := is_group_hom.one f,
have : (∀ x, (f x = 1 → x = 1)),
```

#### [Simon Hudon (Apr 24 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603643):
Do you have an `end` keyword after that?

#### [Johan Commelin (Apr 24 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603648):
yes

#### [Johan Commelin (Apr 24 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603653):
several lines lower

#### [Simon Hudon (Apr 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603719):
Can you show me what the rest of the proof is?

#### [Simon Hudon (Apr 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603720):
Also, do you have imports?

#### [Johan Commelin (Apr 24 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603992):
```lean
import tactic
import init.function
import algebra.group
import group_theory.subgroup

universes u

variables
{A : Type u} [group A]
{B : Type u} [group B]
{f : A → B} [is_group_hom f]

lemma test (hf : function.injective f) (x : A) (hx : x ∈ ker f) : x = 1 :=
begin
have := is_group_hom.one f,
have : (∀ x, (f x = 1 → x = 1))
end
```

#### [Johan Commelin (Apr 24 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604019):
All the other stuff in that file is wrapped withing a section

#### [Kenny Lau (Apr 24 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604129):
hf $ hx.trans $ eq.symm $ is_group_hom.one f

#### [Johan Commelin (Apr 24 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604198):
I first need to get rid of an error message: `invalid expression starting at <coords>`

#### [Johan Commelin (Apr 24 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604201):
the `<coords>` are of the `\fo`

#### [Simon Hudon (Apr 24 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604257):
I don't see a problem there. Try restarting your Lean server

#### [Johan Commelin (Apr 24 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604365):
Yay, that did it (-;

#### [Simon Hudon (Apr 24 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604377):
Unfortunately, that's a common solution to problems :stuck_out_tongue_winking_eye:

#### [Johan Commelin (Apr 24 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604527):
Ok, need to go now

#### [Johan Commelin (Apr 24 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604528):
Thanks!

#### [Patrick Massot (Apr 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125609972):
I think this happens more frequently since @**Gabriel Ebner** enabled the new "region of interest" thing

#### [Patrick Massot (Apr 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125610009):
It's nice to have Lean reacting quicker but I did get quite a lot of those random `invalid expression starting at <coords>` yesterday

#### [Gabriel Ebner (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125610074):
Do you have a reproducible test case?

#### [Kenny Lau (Apr 25 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672053):
Oh so `cc` deals with commutativity and associativity also?

#### [Simon Hudon (Apr 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672100):
No. Why do you say that?

#### [Kenny Lau (Apr 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672103):
apparently it did

#### [Kenny Lau (Apr 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672486):
```lean
theorem test (m n : nat) : m + n = n + m := by cc
#print test
/-
theorem test : ∀ (m n : ℕ), m + n = n + m :=
λ (m n : ℕ),
  of_eq_true (eq_true_intro (eq.symm (eq.trans (eq.refl (n + m)) (eq.symm (is_commutative.comm has_add.add m n)))))
-/
```

#### [Simon Hudon (Apr 25 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672553):
Oh interesting! I didn't think it would

