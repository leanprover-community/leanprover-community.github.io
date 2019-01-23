---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17888CoercionsNZQRC.html
---

## Stream: [maths](index.html)
### Topic: [Coercions N->Z->Q->R->C](17888CoercionsNZQRC.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130849802):
My students want to move freely between these five basic objects, sometimes because they have made poor design decisions but sometimes for genuine reasons. I figured I'd try to get to the bottom of why they were having problems.

```lean
import data.complex.basic 

definition has_coe_NZ : has_coe ℕ ℤ := by apply_instance
definition has_coe_NQ : has_coe ℕ ℚ := by apply_instance 
definition has_coe_NR : has_coe ℕ ℝ := by apply_instance 
definition has_coe_NC : has_coe ℕ ℂ := by apply_instance 
definition has_coe_ZQ : has_coe ℤ ℚ := by apply_instance 
definition has_coe_ZR : has_coe ℤ ℝ := by apply_instance
definition has_coe_ZC : has_coe ℤ ℂ := by apply_instance
-- definition has_coe_QR : has_coe ℚ ℝ := by apply_instance -- fails
noncomputable definition has_coe_QR : has_coe ℚ ℝ := by apply_instance
-- definition has_coe_QC : has_coe ℚ ℂ := by apply_instance -- fails
noncomputable definition has_coe_QC : has_coe ℚ ℂ := by apply_instance
definition has_coe_RC : has_coe ℝ ℂ := by apply_instance 

definition coe_NZ : ℕ → ℤ := has_coe_NZ.coe
definition coe_NQ : ℕ → ℚ := has_coe_NQ.coe 
definition coe_NR : ℕ → ℝ := has_coe_NR.coe 
definition coe_NC : ℕ → ℂ := has_coe_NC.coe 
definition coe_ZQ : ℤ → ℚ := has_coe_ZQ.coe 
definition coe_ZR : ℤ → ℝ := has_coe_ZR.coe
definition coe_ZC : ℤ → ℂ := has_coe_ZC.coe 
noncomputable definition coe_QR : ℚ → ℝ := has_coe_QR.coe
noncomputable definition coe_QC : ℚ → ℂ := has_coe_QC.coe 
definition coe_RC : ℝ → ℂ := has_coe_RC.coe 

-- The ten theorems below are what I would like to access easily in Lean.
-- I don't know what to call them; the current names are just placeholders.

-- N to Z is never a problem
theorem NZQ (x : ℕ) : coe_ZQ (coe_NZ x) = coe_NQ x := rfl 
theorem NZR (x : ℕ) : coe_ZR (coe_NZ x) = coe_NR x := rfl
theorem NZC (x : ℕ) : coe_ZC (coe_NZ x) = coe_NC x := rfl

-- the problems start now
theorem ZQR (x : ℤ) : coe_QR (coe_ZQ x) = coe_ZR x := sorry -- simp fails
theorem QRC (x : ℚ) : coe_RC (coe_QR x) = coe_QC x := sorry -- simp fails
theorem ZRC (x : ℤ) : coe_RC (coe_ZR x) = coe_ZC x := sorry -- simp fails

theorem NQR (x : ℕ) : coe_QR (coe_NQ x) = coe_NR x := by rw [←NZQ,ZQR,←NZR]
theorem ZQC (x : ℤ) : coe_QC (coe_ZQ x) = coe_ZC x := by rw [←QRC,←ZRC,←ZQR]
theorem NQC (x : ℕ) : coe_QC (coe_NQ x) = coe_NC x := by rw [←NZC,←NZQ,←ZQC]
theorem NRC (x : ℕ) : coe_RC (coe_NR x) = coe_NC x := by rw [←NQC,←QRC,←NQR]

-- cool stuff my stuents constantly want to be able to do 
example (x : ℤ) : ((x : ℚ) : ℝ) = x := ZQR x 
example (x : ℤ) : let (y : ℚ) := ↑x in let (z : ℝ) := ↑y in z = ↑x := ZQR x 

```

Q1) Is there a good reason for the noncomputable coercions being noncomputable? 

Q2) How do I prove the sorried coercion theorems?

Q3) What are the correct names for these theorems that enable me to cancel `↑↑` in these specific cases?

#### [ Gabriel Ebner (Aug 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130850810):
You need to use the right syntax, then everything works out of the box :smile: 
```lean
theorem ZQR (x : ℤ) : ((x : ℚ) : ℝ) = (x : ℝ) := by simp
theorem QRC (x : ℚ) : ((x : ℝ) : ℂ) = (x : ℂ) := by simp
theorem ZRC (x : ℤ) : ((x : ℝ) : ℂ) = (x : ℂ) := by simp
```

#### [ Gabriel Ebner (Aug 03 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130850898):
You can use `set_option trace.simplify.rewrite true` to find the corresponding lemmas.

#### [ Kevin Buzzard (Aug 03 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130851433):
Oh many thanks Gabriel! I think I can take it from here

#### [ Chris Hughes (Aug 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130852441):
Q - > R is noncomputable, I'm guessing because it's defined to any field using division and the integer coercion and division is noncomputable on the reals. There is a computable function Q->R, the constant sequence, but that would be less general than the current Q coercion, and computable reals are useless anyway.

#### [ Kevin Buzzard (Aug 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882150):
"computable reals are useless anyway" -- maybe to you. But to a beginner, I think

```lean
def x : ℝ := 1/2 
/-
definition 'x' is noncomputable, it depends on 'real.division_ring'
-/

```

is very confusing. What's so noncomputable about 1/2?

#### [ Kenny Lau (Aug 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882160):
I hear they have a computable division by positive numbers

#### [ Mario Carneiro (Aug 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882206):
there is a manual coercion from Q if you really care about defining 1/2 computably, but the point is that it's not the object but the way it is defined that makes it noncomputable

#### [ Kevin Buzzard (Aug 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882208):
The default coercion from nat to int isn't the generic one from nat to any semiring, it's the constructor, and my understanding was that this decision was made for efficiency reasons.

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882217):
Is there a similar argument saying that the default coercion from Q to R should be the one that's staring you in the face rather than the generic one?

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882218):
i.e. the constant series

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882221):
These are implementation issues I guess, which I of course know nothing about in practice

#### [ Mario Carneiro (Aug 04 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882261):
Short answer yes

#### [ Mario Carneiro (Aug 04 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882268):
But this road leads to the same confusion as why `int.coe_nat_*` and `nat.cast_*` have parallel but apparently identical statements

#### [ Mario Carneiro (Aug 04 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882313):
look ma, no `noncomputable`
```
import data.real.basic
def one_half : ℝ := real.of_rat (1/2)
theorem one_half_eq : one_half = 1/2 := by simp [one_half]
```

#### [ Kevin Buzzard (Aug 04 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882432):
```quote
But this road leads to the same confusion as why `int.coe_nat_*` and `nat.cast_*` have parallel but apparently identical statements
```
Right. And as you know I've been thinking about this recently (I'm trying to write some undergraduate example sheets which look like maths but are actually not hard to do in Lean for a beginner). A decision was made to not use the generic coercion, this then causes some issues like `int.coe_nat...` v `nat.cast...`, these are solved by the devs, the right simp lemmas are proved, people like me learn (in my case, yesterday) that if you use `\u` then everything should be fine, and then we move on. The devs could do the same for Q -> R, right? Chris seems to think there's no point because who cares about computable reals, but I'm suggesting that there might be a point which has something to do with efficiency somehow.

#### [ Mario Carneiro (Aug 04 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882438):
> this decision was made for efficiency reasons

Actually it's the opposite. Efficiency would dictate using `real.of_rat` because it has the more natural implementation, and is exponentially faster if you actually run it. The decision was made for uniformity of the library - in the lean 2 library we had all 10 coercions N->Z->Q->R->C and 10 sets of lemmas about them (plus some extras for the 15 ways to combine them), while the `nat.cast` approach requires only 4 coercions and sets of lemmas

#### [ Kevin Buzzard (Aug 04 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882490):
```lean
def one_half : ℝ := real.of_rat (1/2)
theorem one_half_eq : one_half = 1/2 := by simp [one_half]

noncomputable def real_half : ℝ := 1 / 2 

example : one_half = real_half := by simp [one_half] -- fails
```
aargh. Lean why u hate me

#### [ Mario Carneiro (Aug 04 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882491):
If you work with reals and don't want to be surprised by `noncomputable` markings, just put `noncomputable theory` at the top. It's not worth the digression for newbies

#### [ Kevin Buzzard (Aug 04 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882497):
Oh that's a good idea.

#### [ Mario Carneiro (Aug 04 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882536):
you have to unfold both

#### [ Kevin Buzzard (Aug 04 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882544):
```quote
you have to unfold both
```
I know that `rw` won't unfold. `simp` is the same? If I had to simplify something, I think I'd be tempted to start unfolding right at the start.

#### [ Mario Carneiro (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882591):
again, you should remember gabriel's advice from yesterday: `simp` cares about how you write things, so if you hide something behind a definition you can break some `simp` proofs

#### [ Kevin Buzzard (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882594):
yes exactly.

#### [ Mario Carneiro (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882595):
`simp` will only unfold things you tell it to

#### [ Kevin Buzzard (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882598):
I feel like I really understand how to use `rw` now but I'm still getting the hang of `simp`. There is an art to all these things.

#### [ Kevin Buzzard (Aug 04 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882643):
I don't want to work with reals at all, it's just that the 250 people in front of me in October are all familiar with them (at some level -- at some other level they don't have a clue what they are, and don't have a clue that they don't know, but I don't mean that; I mean they're not scared of them). So it's very natural to use them whenever I want a random big set. They show up on the first example sheet. I've been looking back at my work from last October when I was working on my own example sheets. It took me 150 lines of code to prove that 1/2 : real wasn't an integer :-)

#### [ Mario Carneiro (Aug 04 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882651):
I honestly think you can use `Q` for all those types of theorems and have a much better day

#### [ Kevin Buzzard (Aug 04 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882653):
I honestly believe you.

#### [ Kevin Buzzard (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882693):
I had a principle back then -- "don't change the example sheets; that would be a compromise"

#### [ Mario Carneiro (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882697):
just say "there are some complications with using reals so we'll use Q for now" at the start of class and come back to it when you are ready (or not at all)

#### [ Kevin Buzzard (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882704):
https://github.com/kbuzzard/xena/blob/master/M1F/2016-17/example_sheets/exsht1.pdf

#### [ Kevin Buzzard (Aug 04 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882712):
Sheet 1 Q6 -- I was told "this is not possible in Lean because your sets are stupid"

#### [ Kevin Buzzard (Aug 04 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882713):
I had to start compromising pretty quickly

#### [ Mario Carneiro (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882758):
Heh - I could show you how to define that using inductive types

#### [ Mario Carneiro (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882761):
or trees

#### [ Kevin Buzzard (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882762):
https://github.com/kbuzzard/xena/blob/2bf7737bc0fbcd3943ddadfb513bd19c1eea14a3/xenalib/half_not_an_integer.lean#L116

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882768):
triumphant proof that 1/2 wasn't an integer, so I could do Q7 part (i)

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882769):
Kind of amazing that I didn't give up there and then

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882772):
to do example sheet 2 I had to write my own square root function

#### [ Mario Carneiro (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882815):
it occurs to me that it is really easy to prove that over Q

#### [ Mario Carneiro (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882816):
since 1/2 has denom 2 and integers have denom 1

#### [ Kevin Buzzard (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882817):
right

#### [ Kevin Buzzard (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882821):
```lean
import data.real.basic tactic.interactive

lemma rational_half_not_an_integer : ¬ ∃ n : ℤ, (1/2 : ℚ) = ↑n :=
begin
  -- proof by contradiction
  rintros ⟨n,Hn⟩, -- n is an integer, Hn the proof that 1/2 = n
  -- goal is "false"
  have H := rat.coe_int_denom n, -- H says denominator of n is 1
  rw ←Hn at H, -- H now says denominator of 1/2 is 1...
  revert H,exact dec_trivial -- ...but denominator of 1/2 isn't 1.
end 

lemma real_half_not_an_integer : ¬ ∃ n : ℤ, (1/2 : ℝ) = ↑n :=
begin
  rintro ⟨n,Hn⟩, -- n is an integer, Hn the proof that it's 1/2
  apply rational_half_not_an_integer,
  existsi n,
  -- now our hypothesis is that 1/2 = n as reals, and we want to
  -- deduce 1/2 = n as rationals!
  -- This is possible by some messing around with coercionc
  -- from integers to rationals to reals.
  rw ←@rat.cast_inj ℝ _ _,
  rw (show ((n : ℚ) : ℝ) = (n : ℝ), by simp),
  rw ←Hn,
  simp
end 
```

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882823):
Current version of 2018 proof

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882828):
no having to define my own floor function in sight!

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882830):
and a lot less than 150 lines too

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882831):
and Gabriel's proof right there at the end

#### [ Mario Carneiro (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882870):
There is a name for that lemma

#### [ Mario Carneiro (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882872):
you don't have to `show by simp`

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882873):
yes, I even looked it up

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882875):
as Gabriel suggested

#### [ Kevin Buzzard (Aug 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882881):
in fact did you know that whenever you use simp, you can actually replace it with lemmas which have names?

#### [ Kevin Buzzard (Aug 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882883):
;-)

#### [ Mario Carneiro (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882894):
the advantage of `simp` is when there are a lot of lemmas, applied in complicated positions

#### [ Kevin Buzzard (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882934):
I am sort-of confused by this. I never know whether to write `assumption` or `exact H27`...

#### [ Mario Carneiro (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882938):
when the theorem name is shorter than the statement I prefer `rw`

#### [ Kevin Buzzard (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882939):
...and I never know whether to write `simp` or to write `simp` and then look what it did and write that instead.

#### [ Kevin Buzzard (Aug 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882952):
Hmm, so maybe the answer is "it depends"

#### [ Mario Carneiro (Aug 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882959):
I prefer `exact H27` over `assumption`, indeed I rarely use `assumption` because it is longer, less descriptive, and possibly time consuming if it normalizes an irrelevant hypothesis

#### [ Kevin Buzzard (Aug 04 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883098):
This code above has a rather strange role to play. My current idea is to present the example sheet questions and at the top have a list of lemmas which the students might find helpful. This is example sheet 1 so I'll probably get a lot of people trying it; many will have given up by sheet 2. My plan as I say was to list useful lemmas at the top which they will need, and then hopefully they can prove all the parts of Q7 with rewrites and exact. One of the lemmas I was going to offer them was the proof that 1/2 wasn't an integer, because they need it for Q7(i). But I was going to say "don't worry about these lemmas, just assume them, however anyone interested in what is going on here might want to take a look at them". So I was thinking that the code above would only be seen by people who were interested in what Lean was doing but knew nothing about Lean at all; hence the comments everywhere and the decision to use simp instead of a lemma with a to-them-incomprehensible name

#### [ Kevin Buzzard (Aug 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883113):
My goal was to stick with R but to give them the lemmas they need and then to see how well they did.

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883158):
I was going to get my xena undergrads to test out the problems in Sept and report back.

#### [ Mario Carneiro (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883160):
example of `assumption` going wrong:
```
example {p : Prop} (h1 : if 10^4 = 10^4 then true else true)
  (hp : p) : p := by assumption
```

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883165):
I will happily never use `assumption` again.

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883168):
except for those funny cases when you prove lots of cases at once after a semicolon

#### [ Mario Carneiro (Aug 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883179):
a somewhat nicer form of `assumption` which you may not know is the french quotes `‹p›`

#### [ Kevin Buzzard (Aug 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883183):
Whenever I see people using that I always figure that they should be doing something else

#### [ Mario Carneiro (Aug 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883240):
I have started using the french quotes to refer to instances that I don't want to name, when I need to refer to them directly for some reason

#### [ Kevin Buzzard (Aug 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883243):
Actually I think that's not assumption going wrong

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883255):
```lean
example {p : Prop} (h1 : if 10^4 = 10^4 then true else true)
  (hp : p) : p := 
  begin
      
  end
```

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883259):
already times out

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883261):
but I do believe you

#### [ Mario Carneiro (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883269):
That is a recently discovered mystery for me

#### [ Mario Carneiro (Aug 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883340):
@**Sebastian Ullrich** Do you know what preprocessing is done on the context before a `begin end` block and why? This also came up with the person who was trying to pattern match on a beta redex in the goal only to find it was already reduced before the tactic got to it

#### [ Mario Carneiro (Aug 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883470):
this is a better example
```
example {n : ℕ} (h1 : (if 10^4 = 10^4 then 1 else 1) = 1)
  (hp : n = 1) : n = 1 := by assumption
```

#### [ Mario Carneiro (Aug 04 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883516):
in the original example the timeout is because `h1` has a type which is not obviously even a type, so it has to do the expensive evaluation to find out if it is a type

#### [ Mario Carneiro (Aug 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883597):
Wow, even this times out
```
def q : Prop := if 10^4 = 10^4 then true else true
example (h : q) : q := h
```

#### [ Mario Carneiro (Aug 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883599):
but `example : q → q := id` is okay

#### [ Mario Carneiro (Aug 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883891):
Here is an example of an interesting partial reduction:
```
example : (λ x, x ∧ x) ((λ x, x) true) :=
by tactic.target >>= tactic.trace
-- (λ (x : Prop), x) true ∧ (λ (x : Prop), x) true
```
It looks like the goal has whnf applied first

#### [ Sebastian Ullrich (Aug 04 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130898994):
I wouldn't even know where to start looking for the whnf

#### [ Mario Carneiro (Aug 04 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130899271):
My guess is that it is making sure it is a sort first


{% endraw %}
