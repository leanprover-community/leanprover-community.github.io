---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24215inequalitygolfrequest.html
---

## [new members](index.html)
### [inequality golf request](24215inequalitygolfrequest.html)

#### [Bryan Gin-ge Chen (Nov 21 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148130620):
I'm curious to see how simple a lean proof of this can be:
```lean
-- Thm 1.3 in Hopcroft, Motwani and Ullcroft's book
example (x : ℕ) (h : x ≥ 4) : 2 ^ x ≥ x ^ 2 := sorry
```
For comparison, here's my ugly rewrite proof:
```lean
import tactic.linarith

open nat

lemma h4 : (4 : ℚ) = ↑(4 : ℕ) := by simp
lemma h5 : (5 : ℚ) = ↑(5 : ℕ) := by simp

lemma hne {a : ℕ} : 0 < (↑((a+4)^2) : ℚ) :=
begin
  -- simp, ring,
  rw [nat.cast_pos],
  exact pow_pos (succ_pos _) _
end

lemma this'' {a : ℕ} : (5 : ℚ)^2 / (4 : ℚ)^2 ≥ (↑((a+5)^2) / ↑((a+4)^2): ℚ) :=
begin
  refine (div_le_iff hne).2 _,
  rw [mul_comm_div, ←mul_div_assoc],
  refine (le_div_iff (by norm_num)).2 _,
  -- simp, ring, simp,
  rw [h4, h5, cast_pow, cast_pow, ←_root_.mul_pow, ←_root_.mul_pow, ←cast_mul, ←cast_mul],
  refine _root_.pow_le_pow_of_le_left _ _ _,
  { exact nat.cast_nonneg _ },
  { rw [nat.cast_le], linarith }
end

lemma this' {a : ℕ} : 2 ≥ (↑((a+5)^2) / ↑((a+4)^2): ℚ) :=
calc 2 ≥ (5 : ℚ)^2 / (4 : ℚ)^2 : by norm_num
... ≥ _ : this''

example (x : ℕ) (h : x ≥ 4) : 2 ^ x ≥ x ^ 2 :=
match x, h with
| 0, _ := dec_trivial
| 1, _ := dec_trivial
| 2, _ := dec_trivial
| 3, h := by norm_num at h
| 4, _ := dec_trivial
| (a+5), hₐ :=
begin
  have : 2 ^ (a + 4) ≥ (a + 4) ^ 2 := _match (a+4) dec_trivial,
  have thisQ : (↑(2 ^ (a+4)) : ℚ) ≥ (↑((a+4)^2) : ℚ) :=
    nat.cast_le.2 this,
  have goalQ : (↑(2 ^ (a+5)) : ℚ) ≥ (↑((a+5)^2) : ℚ) :=
    begin
      rw [nat.pow_succ, mul_comm, cast_mul, mul_mul_div (↑((a+5)^2)) (ne_of_gt hne)],
      conv_rhs { rw [mul_comm, ←mul_assoc, mul_comm_div, one_mul] },
      exact mul_le_mul this' thisQ (le_of_lt hne) (by norm_num)
    end,
  exact nat.cast_le.1 goalQ
end
end
```
I tried using `linarith` at the commented lines but it didn't seem to know how to deal with coercions from `nat`, even after I put `↑a  ≥ 0` as a hypothesis. A related question: what's the easiest way to turn a goal like this:
```
(160 + 16 * ↑a) * ↑a ≤ (200 + 25 * ↑a) * ↑a
```
into an inequality over `nat`s (e.g. by getting it into a form where I can use `nat.cast_le`)?

#### [Kevin Buzzard (Nov 21 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132450):
```lean
import data.nat.basic
import tactic.ring

lemma helpful {d : ℕ} (h4 : 4 ≤ d) : 2 * d + 1 ≤ d * d :=
calc 2 * d + 1 ≤ 2 * d + d : nat.add_le_add_left (le_trans dec_trivial h4) _
... = (2 + 1) * d : by rw [add_mul,one_mul]
... ≤ d * d : nat.mul_le_mul_right _ (le_trans dec_trivial h4)

example (x : ℕ) (h : x ≥ 4) : 2 ^ x ≥ x ^ 2 :=
begin
  induction x with d Hd,exact dec_trivial,
  cases nat.eq_or_lt_of_le h with h4 h5,
  rw ←h4,exact dec_trivial,
  have h4 : 4 ≤ d := nat.le_of_lt_succ h5, 
  exact calc 2 ^ (d + 1) = 2 ^ d * 2 : by rw nat.pow_succ
  ... ≥ d ^ 2 * 2 : nat.mul_le_mul_right 2 (Hd h4)
  ... = d * d + d * d : by rw [mul_two,nat.pow_two]
  ... ≥ 2 * d + 1  + d * d : nat.add_le_add_right (helpful h4) _
  ... = (d + 1) ^ 2 : by ring
end
```

#### [Kevin Buzzard (Nov 21 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132461):
Did I misunderstand the question? I don't understand why you are using rationals.

#### [Bryan Gin-ge Chen (Nov 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132551):
Yeah, in hindsight that strategy wasn't so smart (I was following the proof from that book which first showed that $$2 \geq (x+1)^2/x^2$$ for $$x\geq4$$).

#### [Kevin Buzzard (Nov 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132566):
For `(160 + 16 * ↑a) * ↑a ≤ (200 + 25 * ↑a) * ↑a` I would try proving the things you want to rewrite with `simp`. I wrote some stuff about this sort of thing here https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md , maybe that helps.

#### [Kevin Buzzard (Nov 21 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132622):
I showed that goal too, but I kept everything in nat and showed 2x^2>=(x+1)^2

#### [Bryan Gin-ge Chen (Nov 21 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132674):
I was looking at that doc but it didn't say anything about inequalities. But maybe you're saying that I'll have to transform the numbers individually.

#### [Bryan Gin-ge Chen (Nov 21 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132748):
Or I guess I can probably get simp to do the LHS / RHS all at once.

#### [Kevin Buzzard (Nov 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136108):
I mean you could try things like `rw (show (160 + 16 * ↑a) * ↑a = ((160 + 16 * a) * a : nat), by simp)`

#### [Kevin Buzzard (Nov 21 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136373):
```lean
import data.rat

example (a : ℕ) (H : ((160 : ℚ) + 16 * ↑a) * ↑a ≤ (200 + 25 * ↑a) * ↑a) :
(160 + 16 * a) * a ≤ (200 + 25 * a) * a :=
begin
  rw (show ((160 : ℚ) + 16 * ↑a) * ↑a = ((160 + 16 * a) * a : nat), by simp) at H,
  rw (show ((200 : ℚ) + 25 * ↑a) * ↑a = ((200 + 25 * a) * a : nat), by simp) at H,
  rw nat.cast_le at H,
  assumption
end
```

#### [Kevin Buzzard (Nov 21 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136439):
I had to deal with a gazillion of these sorts of things when I was doing my own undergraduate example sheets, and ended up with what I hope is a robust set of techniques. I still sometimes think about a typeclass solution though.

#### [Bryan Gin-ge Chen (Nov 22 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148147836):
Thanks, this has been very helpful!

#### [Kevin Buzzard (Nov 22 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148160788):
So here's a question that came up on my undergraduate example sheets. "Show that the rationals are unbounded above in the reals". In maths we would perhaps say "it's a standard result that for all real x there exists a natural n with n > x, so done". As you can imagine, porting this proof to Lean is a great example of how things are harder than they look here (or how they should be)? @**Bryan Gin-ge Chen** you might want to try proving `theorem rationals_unbounded (r : ℝ) : ∃ s : ℚ, r < s` from `exists_nat_gt : ∀ (x : ℝ), ∃ (n : ℕ), x < ↑n`. It's just the same sort of kerfuffle. Some idle coding from earlier in the week:

```lean
import algebra.archimedean

import data.real.basic

class is_nat (r : ℝ) : Prop :=
(pf : ∃ n : ℕ, r = n)

class is_rat (r : ℝ) : Prop :=
(pf : ∃ q : ℚ, r = q)

definition S : set ℝ := {r : ℝ | is_rat r}

instance nat_is_rat (r : ℝ) [H : is_nat r] : is_rat r :=
begin
  tactic.unfreeze_local_instances,
  rcases H with ⟨⟨n,Hn⟩⟩,
  refine ⟨⟨n,_⟩⟩, -- some stupid refining happening here out of the way
  rw Hn, simp
end

-- better than exists_nat_gt
-- can it be written by a machine?
theorem real.exists_nat_gt' (x : ℝ) :
    ∃ (n : ℝ) [is_nat n], x < n :=
let ⟨n,Hn⟩ := exists_nat_gt x in ⟨n,⟨⟨⟨n,rfl⟩⟩,Hn⟩⟩

theorem rationals_unbounded (r : ℝ) : ∃ s : S, r < s :=
let ⟨n,Hn,Hx⟩ := real.exists_nat_gt' r in
begin
  haveI := Hn,
  refine ⟨⟨n,show is_rat n, by apply_instance⟩,_⟩,
  assumption,
end
```

There's some noise earlier on, but the main proof at the end there is very short, and probably could be shorter (it was one of the things that started me off on the `use` rant on another thread). I've always wondered whether there is something in these typeclasses I'm setting up here.

#### [Mario Carneiro (Nov 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162299):
I'm confused. What's the difference between `exists_nat_gt` and what you want?

#### [Kevin Buzzard (Nov 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162349):
I want a version of exists_nat_gt which only uses real numbers. The problem which I as a number theorist run into is having to switch between nat, rat and real all the time in a way which is very non-intuitive to a mathematician. I am proposing putting nat and rat (and int) typeclasses on real, meaning that you can reason only with real numbers and avoid having to deal with all the casts.

#### [Kevin Buzzard (Nov 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162417):
The issue is not exists_nat_gt, the issue is proving `(r : ℝ) : ∃ s : ℚ, r < s` using it, which is more than one line in Lean and only one line in maths.

#### [Kevin Buzzard (Nov 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162507):
```lean
import algebra.archimedean

import data.real.basic

definition S : set ℝ := {r : ℝ | ∃ q : ℚ, r = q}

theorem rationals_unbounded : ∀ r : ℝ, ∃ s : S, r < s :=
begin
  intro r,
  have H := exists_nat_gt r,
  cases H with n Hn,
  refine ⟨⟨n,_⟩,_⟩,
    refine ⟨n,_⟩,
    simp,
  show r < n,
  assumption
end
```

That is sort-of horrible.

#### [Mario Carneiro (Nov 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162510):
perhaps you should use `exists_rat_gt` then

#### [Mario Carneiro (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162559):
also notice that the proof of that is a one liner

#### [Kevin Buzzard (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162574):
These one-liners are hard for beginner mathematicians to write. Of this I am certain.

#### [Kevin Buzzard (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162577):
That's the problem.

#### [Kevin Buzzard (Nov 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162620):
You can say "well, that's the nature of dependent type theory" or "mathematicians are cheats", but at the end of the day they struggle to see what the issue is.

#### [Kevin Buzzard (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162701):
My typeclass suggestion, which clearly needs work and may never fly, is just an idea I had for trying to make it easier for mathematicians.

#### [Mario Carneiro (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162708):
that's probably true, but you've already written lots of documentation about it. What more are you going for?

#### [Kevin Buzzard (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162718):
I want to make it easy for beginners.

#### [Kevin Buzzard (Nov 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162761):
I want the proof of `rationals_unbounded (r : ℝ) : ∃ s : rat, r < s` to *be* `exists_nat_gt` rather than being this plus several lines of faffing around.

#### [Kevin Buzzard (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162810):
`:= by standard_typeclass_faff using [exists_nat_gt]`

#### [Mario Carneiro (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162816):
they aren't literally the same thing, so you can't completely eliminate the faffing, but you can get it down to one line

#### [Mario Carneiro (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162822):
well, you can if you use the library lemma :)

#### [Kevin Buzzard (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162824):
They are literally the same thing to a mathematician, and whilst I completely understand that they are not the same thing at all, I want to make this transparent.

#### [Mario Carneiro (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162836):
no they are not the same to a mathematician either... one is talking about nats and the other is talking about rats

#### [Mario Carneiro (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162839):
clearly not the same

#### [Kevin Buzzard (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162842):
And my conclusions were that when it suits them, mathematicians *redefine* the rationals to be the subset of the reals which are rational

#### [Kevin Buzzard (Nov 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162884):
and similarly they redefine the naturals. Mathematicians only work with objects up to canonical isomorphism so they don't even notice that this is happening.

#### [Mario Carneiro (Nov 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162893):
In that case you have to make an analogous observation that `nat` is a subset of `rat` ... it's not zero step no matter how you do it

#### [Kevin Buzzard (Nov 22 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162907):
I know it's not zero step, but it's perhaps one tactic.

#### [Kevin Buzzard (Nov 22 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162988):
Ultimately I'll just say the same thing one more time -- if in a maths lecture you prove that for all reals x there exists a natural n with n > x, and then you want to deduce that for all reals x there exists a rational q with q > x, the proof in a maths lecture is "what are you talking about? We just did this!" It's 0 lines.

#### [Kevin Buzzard (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163003):
Because conveniently at this point in the lecturer's brain, a natural *is* a rational.

#### [Kevin Buzzard (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163009):
I am hoping that one day we'll have an interface which will enable mathematicians to keep this pretence up.

#### [Mario Carneiro (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163015):
```lean
definition S : set ℝ := {r : ℝ | ∃ q : ℚ, r = q}

theorem rationals_unbounded (r : ℝ) : ∃ s : S, r < s :=
let ⟨q, h⟩ := exists_rat_gt r in ⟨⟨_, ⟨q, rfl⟩⟩, h⟩
```

#### [Kevin Buzzard (Nov 22 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163062):
you cheated, you used `exists_rat_gt`. And already that line is hard for beginners, who work in tactic mode, to write.

#### [Mario Carneiro (Nov 22 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163072):
```
theorem rationals_unbounded (r : ℝ) : ∃ s : S, r < s :=
let ⟨n, h⟩ := exists_nat_gt r in ⟨⟨_, n, rfl⟩, by simpa⟩
```

#### [Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163085):
Can we get rid of all pointy brackets?

#### [Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163094):
With my type class idea, I wanted to get pointy bracket usage down to 0

#### [Mario Carneiro (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163102):
you have to inhabit an exists

#### [Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163104):
I wanted the output to be a *real* with a typeclass proving it's a nat.

#### [Kevin Buzzard (Nov 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163150):
Right. So I want to use `use` to inhabit the exists.

#### [Mario Carneiro (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163230):
```lean
theorem rationals_unbounded (r : ℝ) : ∃ s : S, r < s :=
begin
  cases exists_nat_gt r with n h,
  split, swap,
  { split, split,
    { refl },
    { exact n } },
  { simpa }
end
```

#### [Kevin Buzzard (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163232):
This basically is the culmination of my thoughts so far on this silly issue. That's why I wanted `use` and that's why I'm thinking about `[is_rat r]`. But we've moved on from least upper bounds now, so next week I'll be fussing about something else :-) It was just some thoughts on how this part of my course was more difficult than I wanted it to be in Lean, and Bryan's post is another indication of this -- his original post in this thread is a clear indication that mathematicians find it difficult to work with this extra layer of difficulty when nat, rat and real all become different objects, because we are not used to thinking of them like this.

#### [Mario Carneiro (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163242):
arguably that is more like a newbie proof

#### [Mario Carneiro (Nov 22 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163245):
just lots of splitting and bashing

#### [Kevin Buzzard (Nov 22 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163260):
This simpa proof is my favourite so far. I still don't know what simpa does. Whenever I read the description I still get confused. First we simplify the hypotheses, then the conclusion using some hypotheses, then we look for the conclusion in the hypotheses, or something. Maybe I should work on my `simpa` understanding.

#### [Kevin Buzzard (Nov 22 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163313):
Thanks for the `simpa` proof. I will look at it.

#### [Mario Carneiro (Nov 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163393):
`simpa using h` simplifies `h` with the lemmas, then simplifies the goal using the lemmas, then applies `assumption` to match `h` with the goal

#### [Mario Carneiro (Nov 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163411):
here I never said to use `h`, so it actually just simplified the goal and then applied assumption

#### [Mario Carneiro (Nov 22 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163423):
so it is identical to `simp; assumption` in this case

#### [Patrick Massot (Nov 22 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148171478):
@**Kevin Buzzard** I'm not sure I understand what you want. It seems to me that
```lean
theorem rationals_unbounded (r : ℝ) : ∃ s : ℚ, r < s :=
begin
  rcases exists_nat_gt r with ⟨n, _⟩,
  use n,
  simpa  
end
```
is not too bad

#### [Patrick Massot (Nov 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148173479):
I played a bit with your ideas and, of course, I don't have a really nice answer. Something not too bad that may be worth thinking about:
```lean
import data.real.basic

@[class] def is_rat (r : ℝ) : Prop := ∃ q : ℚ, r = q

instance nat_is_rat (n : ℕ) : is_rat n := ⟨n, by simp⟩

meta def come_on : tactic unit := `[repeat { assumption <|> apply_instance <|> split}]

theorem rationals_unbounded (r : ℝ) : ∃ s : ℝ, is_rat s ∧ r < s :=
begin
  cases exists_nat_gt r with n H,
  use n,
  come_on
end 
```

#### [Patrick Massot (Nov 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148173532):
I'm a bit disappointed that none of our general purpose automation tactic seem to be able to replace my ad hoc one.

#### [Kevin Buzzard (Nov 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175435):
Because none of them ask type class inference for any help? Surely the type class system is supposed to fix these problems before the user sees them?

#### [Kevin Buzzard (Nov 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175495):
I guess the challenge now is to prove Bryan's lemma using his proof strategy!

#### [Kevin Buzzard (Nov 22 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175677):
Of course it's a theorem about a rational number x with [is_nat x] or [is_int x] (changing the choice should not change the proof at all) and the hypothesis x ge 4. Ideally no actual nats should show up in the proof at all other than those buried in the typeclass system

#### [Kevin Buzzard (Nov 22 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175704):
That's the question. I shouldn't be telling Bryan "don't use rat" -- we should be making rat easier to use in this context.

#### [Kevin Buzzard (Nov 22 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175713):
Because that's what mathematicians do instinctively

#### [Scott Morrison (Nov 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268407):
Blech, dealing with inequalities is so awful. :-) I have been avoiding it for a long time!

#### [Scott Morrison (Nov 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268408):
```lemma le_pred_of_lt {n m : ℕ} (h : n < m) : n ≤ m - 1 := sorry```

#### [Scott Morrison (Nov 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268500):
ok...
```
lemma le_pred_of_lt {n m : ℕ} (h : n < m) : n ≤ m - 1 :=
pred_le_pred (succ_le_of_lt h)
```

#### [Kevin Buzzard (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269623):
One reason this is annoying is that it's the CS minus there, which doesn't behave as nicely as our minus

#### [Kenny Lau (Nov 24 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269675):
I think the horse is long dead...

#### [Scott Morrison (Nov 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269715):
Yeah, I'm happy enough about this other minus, just miserable that this stuff is still hard.

#### [Kevin Buzzard (Nov 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270331):
I'm just saying that one reason it's hard is that nat minus is poorly behaved, you're in a situation where (a-b)+b isn't a and this will surely make automation harder to write.

#### [Kevin Buzzard (Nov 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270337):
All the lemmas you need should be there somewhere -- the library does a really good job of being complete. Don't forget to import data.nat.basic .

#### [Mario Carneiro (Nov 24 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270503):
in a lot of ways, automation for nat subtraction is similar to automating stuff involving division - you have well definedness conditions that are generated by your statement and they have to be maintained when you rewrite the expression

#### [Kevin Buzzard (Nov 24 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270608):
Yes, that's an insightful comment. Mathematicians know that dividing by zero is something one "never does" so we're always prepared to supply that proof that the denominator is non-zero. But it's easy for us to forget the corresponding precondition for nat subtraction, because nat subtraction just doesn't exist in maths. You define division to be random where we don't define it, but you define nat subtraction to be the wrong thing when we have a perfectly good answer which just happens to be a number which is not a nat.

