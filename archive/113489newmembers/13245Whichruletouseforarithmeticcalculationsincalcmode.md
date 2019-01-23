---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13245Whichruletouseforarithmeticcalculationsincalcmode.html
---

## Stream: [new members](index.html)
### Topic: [Which rule to use for arithmetic calculations in calc mode?](13245Whichruletouseforarithmeticcalculationsincalcmode.html)

---

#### [Yufan Lou (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135641895):
I am trying to prove for any odd number n, 3n + 5 is even as a practice. In the calc steps I have:
3 * n + 5 = ...
            ... = 3 * 2 * k + 3 + 5 : by rw mul_assoc
            ... = 3 * 2 * k + 8        : by ?

What do I need to put in place of the question mark? I wrote the proof this way so as to closely track how I would write it manually, in hope I may introduce this to my classmates as a tool, so I don’t need to simplify it further.

#### [Kenny Lau (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135641906):
by rw add_assoc

#### [Mario Carneiro (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642081):
`rfl`

#### [Mario Carneiro (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642100):
`norm_num` is the correct answer though

#### [Yufan Lou (Oct 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642393):
norm_num is unknown identifier tho

#### [Yufan Lou (Oct 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642396):
I am using the online version

#### [Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642442):
```quote
norm_num is unknown identifier tho
```
Just import tactic.norm_num

#### [Mario Carneiro (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642532):
I'm not sure if the online version has `tactic.norm_num`, it's got a quite old version of mathlib

#### [Yufan Lou (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642552):
import went through

#### [Yufan Lou (Oct 12 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642587):
curiously it still doesn't work. rw add_assoc works btw

#### [Yufan Lou (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642644):
Given by norm_num: `⊢ 3 + (5 + 6 * k) = 8 + 6 * k`

#### [Mario Carneiro (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642649):
You have to reassociate first

#### [Kenny Lau (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642651):
```quote
`norm_num` is the correct answer though
```
I would prefer `rfl` over `norm_num`

#### [Mario Carneiro (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642664):
`norm_num` will evaluate closed term expressions but they have to all be gathered together

#### [Mario Carneiro (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642673):
`rfl` works in small cases, especially on `nat`

#### [Yufan Lou (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642678):
Problem I have with rfl is that the error is not helpful at all

#### [Mario Carneiro (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642734):
But stuff like `3 + 5 = 8` on `real` needs `norm_num`

#### [Kenny Lau (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642744):
```quote
Problem I have with rfl is that the error is not helpful at all
```
it just means they are not definitionally equal

#### [Yufan Lou (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642753):
oh for my case I only work with int and nat

#### [Yufan Lou (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642759):
no need for real here

#### [Mario Carneiro (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642768):
Also stuff like `100 * 35 = 3500` should not be done by `rfl`

#### [Kenny Lau (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642770):
sure

#### [Mario Carneiro (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642782):
but for numbers less than 10 you should be fine

#### [Yufan Lou (Oct 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642836):
cuz `rfl` does induction?

#### [Mario Carneiro (Oct 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642841):
It calculates both sides to a normal form in unary

#### [Mario Carneiro (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642842):
so it's exponentially slower than `norm_num` in large cases

#### [Yufan Lou (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642851):
gotcha

#### [Yufan Lou (Oct 12 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643128):
```quote
You have to reassociate first
```
this kinda beats the purpose of replacing `rw add_assoc` tho

#### [Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643205):
that's true

#### [Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643207):
`ring` will actually solve the whole goal in this case

#### [Yufan Lou (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643211):
```
... = 3 * 2 * k + 8            : by rw add_assoc
 ... = 2 * 3 * k + 8            : by rw mul_comm
```
gives me `⊢ k * (3 * 2) + 8 = 2 * 3 * k + 8`

#### [Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643221):
you can do `mul_comm 2`

#### [Mario Carneiro (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643229):
to give lean a bit of a hint of which mul to comm

#### [Yufan Lou (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643233):
gotcha

#### [Mario Carneiro (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643244):
that's one that `norm_num` can solve btw... or `rfl`

#### [Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643287):
```lean
import data.real.basic tactic.norm_num

theorem test : (3:ℝ) + 5 = 8 :=
by norm_num

#print test

theorem test1 : (3:ℝ) + 5 = 8 :=
by rw [norm_num.bit1_add_bit1, norm_num.one_add_bit0,
norm_num.add1_bit1, norm_num.add1_one]

#print test1

theorem test2 : (3:ℝ) + 5 = 8 :=
calc  (3:ℝ) + 5
    = bit0 (norm_num.add1 ((1:ℝ) + 2)) : norm_num.bit1_add_bit1 _ _
... = bit0 (norm_num.add1 (bit1 (1:ℝ))) : congr_arg _ (congr_arg _ (norm_num.one_add_bit0 _))
... = bit0 (bit0 (norm_num.add1 (1:ℝ))) : congr_arg _ (norm_num.add1_bit1 _)
... = bit0 (bit0 (bit0 (1:ℝ))) : congr_arg _ (congr_arg _ norm_num.add1_one)

#print test2
```
```lean
theorem test : 3 + 5 = 8 :=
eq.mpr
  (id
     (eq.trans
        ((λ (a a_1 : ℝ) (e_1 : a = a_1) (a_2 a_3 : ℝ) (e_2 : a_2 = a_3), congr (congr_arg eq e_1) e_2) (3 + 5) 8
           (norm_num.subst_into_sum 3 5 3 5 8 (eq.refl 3) (eq.refl 5)
              (norm_num.bit1_add_bit1_helper 1 2 3 4 (norm_num.one_add_bit0 1)
                 (norm_num.add1_bit1_helper 1 2 norm_num.add1_one)))
           8
           8
           (eq.refl 8))
        (eq_true_intro (eq.refl 8))))
  trivial

theorem test1 : 3 + 5 = 8 :=
eq.mpr (id (eq.rec (eq.refl (3 + 5 = 8)) (norm_num.bit1_add_bit1 1 2)))
  (eq.mpr (id (eq.rec (eq.refl (bit0 (norm_num.add1 (1 + 2)) = 8)) (norm_num.one_add_bit0 1)))
     (eq.mpr (id (eq.rec (eq.refl (bit0 (norm_num.add1 3) = 8)) (norm_num.add1_bit1 1)))
        (eq.mpr (id (eq.rec (eq.refl (bit0 (bit0 (norm_num.add1 1)) = 8)) norm_num.add1_one)) (eq.refl 8))))

theorem test2 : 3 + 5 = 8 :=
eq.trans
  (eq.trans (eq.trans (norm_num.bit1_add_bit1 1 2) (congr_arg bit0 (congr_arg norm_num.add1 (norm_num.one_add_bit0 1))))
     (congr_arg bit0 (norm_num.add1_bit1 1)))
  (congr_arg bit0 (congr_arg bit0 norm_num.add1_one))
```

#### [Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643290):
@**Mario Carneiro** Can Lean be better at golfing?

#### [Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643294):
or is that actually pointless?

#### [Mario Carneiro (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643310):
Lean doesn't make it easy to golf proofs in tactics

#### [Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643315):
I see

#### [Yufan Lou (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643321):
nevermind... the import seems successful but norm_num is not actually imported

#### [Mario Carneiro (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643376):
I would prefer that lean produced kind of short proofs (i.e. not obviously stupid things) but unfortunately `dsimp` ignores proof arguments

#### [Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643444):
btw `rfl` didn't work on the replacement of `rw mul_comm 2`either

#### [Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643450):
`rfl` is less powerful than I thought

#### [Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643457):
or is it just in calc mode

#### [Mario Carneiro (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643458):
that's surprising

#### [Mario Carneiro (Oct 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643471):
this works for me in the web editor:
```lean
import tactic.norm_num
example : 3 + 5 = 8 := by norm_num
```

#### [Mario Carneiro (Oct 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643482):
do you have a MWE with your unrflable proof?

#### [Yufan Lou (Oct 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643603):
Maybe I had a typo... a minute

#### [Yufan Lou (Oct 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643691):
```lean
example {n : nat} (h1 : is_odd n) : is_even (n + 1) :=
exists.elim h1 (assume k, assume hw : n = 2 * k + 1,
  exists.intro (k + 1)
    (calc
      n + 1 = 2 * k + 1 + 1 : by rw [hw]
        ... = 2 * k + 2     : by rw rfl
        ... = 2 * (k + 1)   : by rfl)
```

#### [Yufan Lou (Oct 12 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643806):
`rfl` doesn't work anytime I need to adjust association right

#### [Yufan Lou (Oct 12 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643807):
same as `norm_num`

#### [Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643819):
`rfl` works iff the two expressions are definitionally equal

#### [Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643823):
`2*(n+1)` for natural numbers is defined to be `2*n+2`

#### [Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643826):
that's unfolding definition of natural number multiplication

#### [Yufan Lou (Oct 12 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643888):
it doesn't work tho

#### [Yufan Lou (Oct 12 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643945):
```lean
example {n : nat} (h1 : is_odd n) : is_even (n + 1) :=
exists.elim h1 (assume k, assume hw : n = 2 * k + 1,
  exists.intro (k + 1)
    (calc
      n + 1 = 2 * k + 1 + 1 : by rw [hw]
        ... = 2 * k + 2     : by rw add_assoc
        ... = 2 * k + 2 * 1 : by rw mul_one
        ... = 2 * (k + 1)   : by rw mul_add
        ))
```
without `rfl` this works, but I can't seem to replace any of them with `rw rfl`or `rfl`

#### [Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644025):
`rfl` is a term not a tactic

#### [Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644031):
so there is no `by`

#### [Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644036):
also `by rw rfl` is always redundant (does nothing)

#### [Yufan Lou (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644042):
ah i see

#### [Yufan Lou (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644080):
didn't think to replace by as well

#### [Yufan Lou (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644090):
works now

#### [Mario Carneiro (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644091):
there is a tactic version, called `refl`

#### [Mario Carneiro (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644093):
so `by refl` and `rfl` are usually interchangeable

#### [Yufan Lou (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644154):
okay for simple calc proofs I can just put `: rfl` after each step nice

#### [Yufan Lou (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644160):
thx y'all

#### [Mario Carneiro (Oct 12 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644176):
actually a `: rfl` calc step can usually just be deleted entirely

#### [Yufan Lou (Oct 12 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644221):
I know, writing out just for demonstration

#### [Mario Carneiro (Oct 12 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644224):
right

#### [Yufan Lou (Oct 12 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644568):
while we are at it is there a one-line proof of that theorem

#### [Mario Carneiro (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644653):
what are the definitions?

#### [Mario Carneiro (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644664):
MWE please

#### [Yufan Lou (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644674):
```lean
def is_even (a : nat) := ∃ b, a = 2 * b
def is_odd (a: nat) := ∃ b, a = 2 * b + 1
example {n : nat} (h1 : is_odd n) : is_even (n + 1)
```

#### [Mario Carneiro (Oct 12 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644698):
```lean
example : ∀ {n : nat}, is_odd n → is_even (n + 1)
| _ ⟨n, rfl⟩ := ⟨n+1, rfl⟩
```

#### [Mario Carneiro (Oct 12 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644753):
turns out the important part of the theorem is `2 * n + 1 + 1 = 2 * (n + 1)` which is true by definition

#### [Yufan Lou (Oct 12 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644768):
cool

#### [Yufan Lou (Oct 12 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644777):
what does `|` do and why `_` following it?

#### [Mario Carneiro (Oct 12 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644786):
I'm using the equation compiler to pattern match on the exists

#### [Mario Carneiro (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644831):
the `_` is the `n` from the statement

#### [Yufan Lou (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644838):
ahh pattern matching thx

#### [Mario Carneiro (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644851):
but it is matched against `2*n+1` because I matched on the equality too

#### [Yufan Lou (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644929):
using `rfl` in pattern matching is pretty eye opening

#### [Yufan Lou (Oct 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645149):
Could you explain the pattern matching more thoroughly?

#### [Yufan Lou (Oct 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645163):
```lean
| _ ⟨n, rfl⟩ := ⟨n + 1, rfl⟩
```

#### [Mario Carneiro (Oct 12 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645594):
Since exists and eq are both inductive types, you can match on them, meaning you have to give a case for each constructor. Both only have one constructor, so there is only one case, where the exists is the `Exists.mk` function (which can also be written using the angle pair bracket) and the eq has the contstructor for equality which is `rfl`. If you put in both of those for the second argument, the first argument is forced to be `(2*n+1)` (Lean can figure this out, but if you want you can replace the `_` with `.(2*n+1)`, where the dot means that this argument's value is forced by later arguments.)

So in this case of the match, we have to prove the statement with `n` replaced with `2*n+1`, that is, `is_even (2 * n + 1 + 1)`. This is defeq to an exists, so I use the angle brackets to supply the witness, which is `n+1`, and the proof of equality, of type `2 * n + 1 + 1 = 2 * (n + 1)`, which as I said is true by reflexivity because both sides are defeq.

#### [Mario Carneiro (Oct 12 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645685):
the defeq chain looks like this btw:
```
2 * (n + 1)
= 2 * succ n
= 2 * n + 2
= 2 * n + succ 1
= succ (2 * n + 1)
= succ (succ (2 * n))
```
```
2 * n + 1 + 1
= succ (2 * n + 1)
= succ (succ (2 * n))
```

#### [Kenny Lau (Oct 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645733):
```
2 * (n + 1)
= 2 * (succ (n + 0))
= 2 * (succ n)
= 2 * n + 2
= ...
```

#### [Mario Carneiro (Oct 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645741):
I'll omit the steps that unfold the definition of `+`. :)

