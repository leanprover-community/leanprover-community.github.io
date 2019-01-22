---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/99121natinequalities.html
---

## [new members](index.html)
### [nat inequalities](99121natinequalities.html)

#### [Scott Olson (Sep 25 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134592941):
What is the most efficient way to solve situations like this? I get a bit lost in all the details of lt, le, negations, and symmetries...

```lean
x : ℕ,
is_lt : x < 2,
h_zero : ¬x = 0,
h_one : ¬x = 1
⊢ false
```

#### [Kevin Buzzard (Sep 25 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134593248):
I am really bad at questions like this still, and I've been playing with Lean for a year. People come up with all sorts of tricks using tactics like `cc` or `finish` or a clever application of `dec_trivial` or whatever, which I never seem to spot.

#### [Reid Barton (Sep 25 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134593402):
Depending on how you obtained the hypotheses `h_zero` and `h_one`, it might have been more efficient to use `cases` on `x` earlier

#### [Scott Olson (Sep 25 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134593796):
I'm interested in the nat inequalites problem in general, but this came up while trying to match exhaustively on a `fin 2`. (It's a contrived example, I suppose, but I also run into `fin` troubles fairly often.)

The trouble there is I'm not sure how to make the pattern compiler understand I don't need any cases beyond 0 and 1, and if I do fill in the catch-all case, I wouldn't automatically even have `x != 0` and `x != 1` with which to prove this.

#### [Scott Olson (Sep 25 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594159):
Ohhh, I think I finally understood the useful way to match on them. If I use a `⟨n+2, is_lt⟩` pattern, I get the `is_lt : n + 2 < 2` contradiction.

#### [Reid Barton (Sep 25 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594218):
Yes exactly

#### [Reid Barton (Sep 25 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594230):
Now you need to prove that's false, probably something like (made up names) `not_lt_of_ge (le_add_self _ _)`

#### [Reid Barton (Sep 25 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594252):
and then combine that with `absurd is_lt ...`

#### [Reid Barton (Sep 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594422):
For your original question you could do `cases` on `x`, handle the first case with `h_zero`, then `cases` again and handle the first case with `h_one`, then you'd be at proving `n + 2 < 2 -> false` again. But those two `cases` steps are just repeating some case analysis that you've already done, it sounds like (that's why you have `h_zero` and `h_one` in the first place).

#### [Scott Olson (Sep 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594432):
Yep, that makes sense. At that point I would just be going the long way around to do the same thing.

#### [Chris Hughes (Sep 25 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134594920):
`example : ∀ x : ℕ, x < 2 → x ≠ 0 → x ≠ 1 → false := dec_trivial`

#### [Reid Barton (Sep 25 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595075):
Aha! sneaky...

#### [Reid Barton (Sep 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595259):
So I guess `revert x, exact dec_trivial` should work for the original question. That's a good trick, changing the goal to something with a bounded quantifier

#### [Scott Olson (Sep 25 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595295):
Interesting, I was having trouble making that work in context, didn't realize I needed `revert x`

#### [Scott Olson (Sep 25 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595371):
Does that work because `\all n < k, p n` has a `decidable` instance or something tricky like that?

#### [Scott Olson (Sep 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595456):
Heh, yeah, I see instances like `decidable (∀ (n_1 : ℕ) (h : n_1 < n), P n_1 h)`

#### [Reid Barton (Sep 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595469):
Yes exactly

#### [Scott Olson (Sep 25 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134595513):
Which is from mathlib, actually, so good thing I finally started using mathlib today...

#### [Scott Olson (Sep 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134596870):
Thanks for all the help. For the record, this is the exercise I gave myself, and it looks pretty minimal now:

```lean
def fin2_equiv_bool : fin 2 ≃ bool := {
    to_fun := λ x, x = 1,

    inv_fun := λ b, cond b 1 0,

    left_inv := λ x,
        match x with
        | ⟨0, _⟩ := rfl
        | ⟨1, _⟩ := rfl
        | ⟨n+2, is_lt⟩ := absurd is_lt (not_lt_of_le (nat.le_add_left _ _))
        end,

    right_inv := λ b, by cases b; refl,
}
```

#### [Scott Olson (Sep 25 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134596887):
Although now that we mentioned dec_trivial, it occurs to me I noticed `\all x : fin n, p x` is decidable...

#### [Kenny Lau (Sep 25 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134596982):
```lean
import data.equiv.basic data.fin

def fin2_equiv_bool : fin 2 ≃ bool := {
    to_fun := λ x, x = 1,
    inv_fun := λ b, cond b 1 0,
    left_inv := by unfold function.left_inverse; exact dec_trivial,
    right_inv := by unfold function.right_inverse function.left_inverse; exact dec_trivial,
}
```

#### [Scott Olson (Sep 25 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597033):
Thanks! The `unfold` is the only step I was missing in my attempt

#### [Kenny Lau (Sep 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597181):
```lean
import data.equiv.basic data.fin

def fin2_equiv_bool : fin 2 ≃ bool :=
{ to_fun := λ x, x = 1,
  inv_fun := λ b, cond b 1 0,
  left_inv := show ∀ x, _ = x, from dec_trivial,
  right_inv := show ∀ b, _ = b, from dec_trivial }
```

#### [Scott Olson (Sep 25 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597623):
It seems like the last part of these is failing for me because there's no instance of decidable for `\all b : bool, p b`

#### [Kenny Lau (Sep 25 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597665):
did you follow the imports?

#### [Scott Olson (Sep 25 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597733):
`data.equiv.basic` doesn't exist for me, I just have `data.equiv` in mathlib

#### [Scott Olson (Sep 25 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597737):
I do have `data.fin`

#### [Scott Olson (Sep 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597764):
I'll double-check my mathlib dependency... I just added it with `leanpkg add leanprover/mathlib` earlier today

#### [Scott Olson (Sep 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134597839):
I see, i think it gave me the branch named lean-3.4.1 instead of master

#### [Simon Hudon (Sep 25 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat inequalities/near/134619039):
Does `linarith` work for your kind of inequality?

