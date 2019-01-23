---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/06287divposiffmulposgolf.html
---

## Stream: [maths](index.html)
### Topic: [div_pos_iff_mul_pos golf](06287divposiffmulposgolf.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700596):
```lean
import analysis.real

lemma div_pos_iff_mul_pos (x y : ℝ) (Hy : y ≠ 0) : 0 < x * y ↔ 0 < x / y :=
begin
  have H : 0 < y * y := mul_self_pos Hy,
  split,
    intro H1,
    have H2 : (x * y) / (y * y) = x / y,
      rw div_eq_div_iff (ne_of_gt H) Hy,
      rw mul_assoc,
    rw ←H2,
    apply div_pos H1 H,
  intro H1,
  have H2 : (x / y) * (y * y) = x * y,
    rw div_mul_eq_mul_div_comm,
    rw mul_div_cancel _ Hy,
  rw ←H2,
  exact mul_pos H1 H,
end
```
I was surprised this wasn't already in, for preordered semimonoids with bot or whatever

#### [ Mario Carneiro (Nov 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700710):
I'm not, that's a weird theorem

#### [ Kevin Buzzard (Nov 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700874):
what about `0 < x * y iff (x < 0 and y < 0) or (x > 0 and y > 0)`?

#### [ Kevin Buzzard (Nov 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700885):
and similarly for `0 < x / y`

#### [ Kenny Lau (Nov 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700919):
`pos_and_pos_or_neg_and_neg_of_mul_pos`?

#### [ Kevin Buzzard (Nov 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700945):
Oh, you found it?

#### [ Kenny Lau (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701006):
I found x*y>0 implies x,y>0 or x,y<0

#### [ Mario Carneiro (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701014):
I guess the best decomposition of it is something like
```
0 < x * y
    ↔ (0 < x ∧ 0 < y ∨ x < 0 ∧ y < 0)
... ↔ (0 < x ∧ 0 < y⁻¹ ∨ x < 0 ∧ y⁻¹ < 0)
... ↔ 0 < x * y⁻¹
... ↔ 0 < x / y
```

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701017):
ha ha it's in core

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701044):
I think you should use `pos_and_pos_or_neg_and_neg_of_mul_pos`

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701046):
just for the name

#### [ Mario Carneiro (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701071):
whenever the name gets that long my eyes cross trying to read it

#### [ Kevin Buzzard (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701091):
we should think of a more rigorous encrypted way to name lemmas

#### [ Kevin Buzzard (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701096):
to keep them shorter

#### [ Mario Carneiro (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701110):
have you seen metamath naming conventions? :D

#### [ Mario Carneiro (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701173):
it would probably be called `mulanor` or the like

#### [ Reid Barton (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701204):
that's a cool name

#### [ Kevin Buzzard (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701205):
the md5sum of `pos_and_pos_or_neg_and_neg_of_mul_pos` is shorter, maybe we should use that

#### [ Mario Carneiro (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701225):
lol that's a bad sign

#### [ Mario Carneiro (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701257):
probably gzip can do better

#### [ Kevin Buzzard (Nov 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702518):
```quote
I'm not, that's a weird theorem
```
How would you do
```lean
theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x < 4 } = 
  {x : ℝ | x < 0 ∨ ((1 : ℝ) / 3 < x ∧ x < 1)} :=
```
? I used this along the way to clear denominators but it was still an annoying case bash

#### [ Kenny Lau (Nov 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702583):
oh god

#### [ Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702659):
yes it's M1F sheet 3

#### [ Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702670):
you should have seen my proof last year!

#### [ Kevin Buzzard (Nov 14 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702771):
It took me 25 lines to get to `⊢ 0 < (1 - x) * x * (3 * x - 1) ↔ x < 0 ∨ 1 / 3 < x ∧ x < 1`

#### [ Kevin Buzzard (Nov 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702785):
and now the case bash is much easier

#### [ Kevin Buzzard (Nov 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702799):
but I had to clear denominators along the way

#### [ Kenny Lau (Nov 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702914):
how about no

#### [ Kevin Buzzard (Nov 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702958):
If it's a reasonable M1F question and if you want formal proof verification systems to be taken seriously by mathematicians, this has to be relatively straightforward

#### [ Reid Barton (Nov 14 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703048):
Someone want to implement a cylindrical algebraic decomposition tactic?

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703084):
Is that what's necessary?

#### [ Mario Carneiro (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703089):
it's a case bash

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703092):
Can we make it an issue or is this unreasonable?

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703100):
It's a cylindrical algebraic decomposition Mario

#### [ Mario Carneiro (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703112):
the generalization of this to more vars is CAD

#### [ Reid Barton (Nov 14 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703177):
Yeah you don't really need it for one variable & rational roots.

#### [ Kevin Buzzard (Nov 14 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703194):
`theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x < 4 } =
  {y : ℝ | y < 0 ∨ ((1 : ℝ) / 3 < y ∧ y < 1)}` you mean like this?

#### [ Kevin Buzzard (Nov 14 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703243):
It's still a pain to prove that if `1/3 < x` and `x < 1` then `3 * x + 1 / x < 4`

#### [ Kevin Buzzard (Nov 14 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703262):
My reworking to `⊢ 0 < (1 - x) * x * (3 * x - 1) ↔ x < 0 ∨ 1 / 3 < x ∧ x < 1` is definitely paying dividends

#### [ Kenny Lau (Nov 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703268):
I think you should just let the IC gang prove that

#### [ Mario Carneiro (Nov 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703323):
in general you have to figure out ordering of real algebraic numbers which is a pain

#### [ Mario Carneiro (Nov 14 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703366):
and the best known algorithm is double exponential, a great *improvement* over the previous algorithm

#### [ Kenny Lau (Nov 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703451):
what a pity, I was going to use it in my next gce exam

#### [ Kevin Buzzard (Nov 14 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704530):
```lean
theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x < 4 } = 
  {x : ℝ | x < 0 ∨ ((1 : ℝ) / 3 < x ∧ x < 1)} :=
begin
  ext x,
  show x ≠ 0 ∧ 3 * x + 1 / x < 4 ↔ x < 0 ∨ 1 / 3 < x ∧ x < 1,
  cases classical.em (x = 0) with H0 Hn0,
  { -- junk case x = 0
    rw H0,
    norm_num,
  },
  rw (show x ≠ 0 ↔ true, by simp [Hn0]),
  rw true_and,
  show (3 : ℝ) * x + 1 / x < 4 ↔ x < 0 ∨ 1 / 3 < x ∧ x < 1,
  have this : (3 : ℝ) * x + 1 / x < 4 ↔ 0 < 4 - (3 * x + 1 / x)
    := (@sub_pos ℝ (by apply_instance) (4 : ℝ) ((3 : ℝ) * x + 1 / x)).symm,
  rw this,
  rw ←sub_sub,
  rw ←mul_one (4 - 3 * x),
  -- annoying rewrite
  have H : 0 < (4 - 3 * x) * 1 - 1 / x ↔ 0 < (4 - 3 * x) * (x / x) - 1 / x,
    rw div_self Hn0,
  rw H,  
  rw ←mul_div_assoc,
  rw ←sub_div,
  rw ←mul_pos_iff_div_pos Hn0,
  replace H : x * x > 0 := mul_self_pos Hn0,
  rw (show ((4 - 3 * x) * x - 1) * x = (1 - x) * x * (3 * x - 1), by ring),
  -- goal now 
  -- ⊢ 0 < (1 - x) * x * (3 * x - 1) ↔ x < 0 ∨ 1 / 3 < x ∧ x < 1
  cases lt_or_ge x 0 with h h1,
  -- x < 0
    rw (show x < 0 ↔ true, by simp [h]),
    rw true_or,
    rw iff_true,
    apply mul_pos_of_neg_of_neg,
      refine mul_neg_of_pos_of_neg _ h,
      apply sub_pos_of_lt,
      apply lt_trans h zero_lt_one,
    apply sub_neg_of_lt,
    refine lt_trans _ zero_lt_one,
    apply mul_neg_of_pos_of_neg _ h,
    norm_num,
  rw (show x < 0 ↔ false, by rw iff_false; exact not_lt_of_ge h1),
  rw false_or,
  cases le_or_gt x ((1 : ℝ) / 3) with h2 h2,
    rw (show (1 : ℝ) / 3 < x ↔ false, by rw iff_false; exact not_lt_of_ge h2),
    rw false_and,
    rw iff_false,
    apply not_lt_of_ge,
    refine mul_nonpos_of_nonneg_of_nonpos _ _,
      refine mul_nonneg _ h1,
      show 0 ≤ 1 - x,
      rw sub_nonneg,
      exact le_trans h2 (by norm_num),
    rw sub_nonpos,
    rw mul_comm,
    apply mul_le_of_le_div (by norm_num) h2,
  cases lt_or_ge x 1,
    rw (iff_true ((1 : ℝ) / 3 < x)).2 h2,
    rw (iff_true (x < 1)).2 h,
    rw true_and,
    rw iff_true,
    refine mul_pos _ _,
      refine mul_pos _ _,
        show 0 < (1 - x),
        rwa sub_pos,
      refine lt_trans (by norm_num) h2,
    show 0 < 3 * x - 1,
    rw sub_pos,
    rwa ←div_lt_iff',
    norm_num,
  rw (show x < 1 ↔ false, by rw iff_false; exact not_lt_of_ge h),
  rw and_false,
  rw iff_false,
  apply not_lt_of_ge,
  refine mul_nonpos_of_nonpos_of_nonneg _ _,
    refine mul_nonpos_of_nonpos_of_nonneg _ h1,
    simp [h], exact h,
  show 0 ≤ 3 * x - 1,
  rw sub_nonneg,
  rw mul_comm,
  apply le_mul_of_div_le,
    norm_num,
  apply le_trans _ h,
  norm_num,
end
```
Much better than last year's effort

#### [ Kenny Lau (Nov 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704744):
"much better"

#### [ Kevin Buzzard (Nov 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704761):
thanks

#### [ Kenny Lau (Nov 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706417):
```lean
import analysis.real

theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x < 4 } =
  {x : ℝ | x < 0 ∨ ((1 : ℝ) / 3 < x ∧ x < 1)} :=
begin
  ext x,
  rcases lt_trichotomy x 0 with hxneg | hx0 | hxpos,
  { refine iff_of_true ⟨ne_of_lt hxneg, _⟩ (or.inl hxneg),
    refine lt_trans (add_neg (mul_neg_of_pos_of_neg _ hxneg) (one_div_neg_of_neg hxneg)) _;
    norm_num },
  { subst x, norm_num },
  show x ≠ 0 ∧ 3 * x + 1 / x < 4 ↔ x < 0 ∨ ((1 : ℝ) / 3 < x ∧ x < 1),
  rw [eq_true_intro (ne_of_gt hxpos)],
  rw [true_and],
  rw [eq_false_intro (not_lt_of_gt hxpos)],
  rw [false_or],
  rw [← mul_lt_mul_right hxpos],
  rw [add_mul],
  rw [one_div_mul_cancel (ne_of_gt hxpos)],
  rw [div_lt_iff (show (0:ℝ) < 3, by norm_num)],
  split,
  { assume h : 3 * x * x + 1 < 4 * x,
    replace h := sub_neg_of_lt h,
    rw [show 3 * x * x + 1 - 4 * x = (1 - x * 3) * (1 - x), by ring] at h,
    have : 1 < x * 3,
    { apply lt_of_not_ge,
      assume h2 : x * 3 ≤ 1,
      replace h := neg_of_mul_neg_left h (sub_nonneg_of_le h2),
      refine not_lt_of_le h2 _,
      refine lt_trans (show (1:ℝ) < 3, by norm_num) _,
      replace h := lt_of_sub_neg h,
      rw [← mul_lt_mul_right (show (0:ℝ) < 3, by norm_num)] at h,
      rwa [one_mul] at h },
    refine ⟨this, lt_of_sub_pos _⟩,
    apply lt_of_not_ge,
    assume h3 : 1 - x ≤ 0,
    apply not_le_of_lt h,
    exact mul_nonneg_of_nonpos_of_nonpos (le_of_lt (sub_neg_of_lt this)) h3 },
  { assume h : 1 < x * 3 ∧ x < 1,
    cases h with h1 h2,
    apply lt_of_sub_neg,
    rw [show 3 * x * x + 1 - 4 * x = (1 - x * 3) * (1 - x), by ring],
    exact mul_neg_of_neg_of_pos (sub_neg_of_lt h1) (sub_pos_of_lt h2) }
end
```

#### [ Kenny Lau (Nov 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706420):
@**Kevin Buzzard**

#### [ Kenny Lau (Nov 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706433):
half your size

#### [ Kevin Buzzard (Nov 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706502):
It's still a lot longer than what most of the first years produce with pen and paper though isn't it :-/

#### [ Kevin Buzzard (Nov 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706584):
you did the case split at the start. I worked on the goal first. Is your way better or would you have written half as much as me if you'd used my strategy too?

#### [ Kenny Lau (Nov 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706587):
btw:
```lean
lemma div_pos_iff_mul_pos (x y : ℝ) (Hy : y ≠ 0) : 0 < x * y ↔ 0 < x / y :=
begin
  have := mul_self_pos Hy,
  rw ← @mul_lt_mul_right _ _ _ (x/y) _ this,
  rw zero_mul,
  rw ← mul_assoc,
  rw div_mul_cancel _ Hy
end
```

#### [ Kenny Lau (Nov 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706603):
```lean
lemma div_pos_iff_mul_pos (x y : ℝ) (Hy : y ≠ 0) : 0 < x * y ↔ 0 < x / y :=
by rw [← @mul_lt_mul_right _ _ _ (x/y) _ (mul_self_pos Hy)];
  rw [zero_mul, ← mul_assoc, div_mul_cancel _ Hy]
```

#### [ Kenny Lau (Nov 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706702):
```lean
lemma div_pos_iff_mul_pos (x y : ℝ) (Hy : y ≠ 0) : 0 < x * y ↔ 0 < x / y :=
by rw [← div_lt_div_right (mul_self_pos Hy), zero_div, ← div_div_eq_div_mul, mul_div_cancel _ Hy]
```

#### [ Kenny Lau (Nov 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706705):
(98 characters!)

#### [ Kenny Lau (Nov 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706769):
```quote
you did the case split at the start. I worked on the goal first. Is your way better or would you have written half as much as me if you'd used my strategy too?
```
 I mean, you also did case split at the start

#### [ Reid Barton (Nov 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706788):
Isn't that `Hy` hypothesis actually unneeded?

#### [ Reid Barton (Nov 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706795):
If `y = 0` then both things are 0

#### [ Kenny Lau (Nov 15 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706981):
great

#### [ Kenny Lau (Nov 15 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147707018):
"Lean helps me understand maths better"

#### [ Kenny Lau (Nov 15 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147707033):
"`y` doesn't need to be nonzero"

#### [ Mario Carneiro (Nov 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147713393):
```lean
import data.real.basic tactic.ring data.set.intervals

theorem mul_pos_iff {α} [linear_ordered_ring α] {a b : α} :
  0 < a * b ↔ 0 < a ∧ 0 < b ∨ a < 0 ∧ b < 0 :=
⟨pos_and_pos_or_neg_and_neg_of_mul_pos,
  or.rec (and.rec mul_pos) (and.rec $ by exact mul_pos_of_neg_of_neg)⟩

theorem or_iff_left {a b : Prop} (h : ¬ b) : a ∨ b ↔ a :=
or_iff_left_of_imp h.elim

theorem or_iff_right {a b : Prop} (h : ¬ a) : a ∨ b ↔ b :=
or_iff_right_of_imp h.elim

open set
theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x < 4 } = Iio 0 ∪ Ioo (1 / 3) 1 :=
begin
  ext x,
  rcases lt_trichotomy x 0 with x0|x0|x0,
  { refine iff_of_true ⟨ne_of_lt x0,
      lt_trans (add_neg
        (mul_neg_of_pos_of_neg _ x0)
        (one_div_neg_of_neg x0)) _⟩ (or.inl x0);
    norm_num },
  { subst x, norm_num },
  { dsimp [Iio, Ioo],
    rw [and_iff_right (ne_of_gt x0), or_iff_right (not_lt_of_gt x0),
      add_div_eq_mul_add_div _ _ (ne_of_gt x0),
      div_lt_iff x0, div_lt_iff' (by norm_num : 0 < (3:ℝ)), ← sub_pos,
      (by ring : 4*x - (3*x*x + 1) = (3*x - 1)*(1 - x)),
      mul_pos_iff, sub_pos, sub_pos, sub_lt_zero, sub_lt_zero,
      or_iff_left],
    rintro ⟨h₁, h₂⟩,
    refine absurd (lt_trans h₂ ((lt_div_iff' _).2 h₁)) _; norm_num }
end
```

#### [ Kevin Buzzard (Nov 15 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147716871):
I shall explode this proof tomorrow

#### [ Patrick Massot (Nov 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147728220):
Mario, why do you need to explicitly invoke all those `and_iff_right`, `or_iff_right`, `or_iff_left`? Isn't it something that the simplifier should do (using hypothesis `x0`)?

#### [ Patrick Massot (Nov 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147728438):
Makes me think: @**Simon Hudon** what happened to your monotonicity tactic?

#### [ Simon Hudon (Nov 15 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147754940):
Mario is still unhappy with it.


{% endraw %}
