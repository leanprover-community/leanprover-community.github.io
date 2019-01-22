---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/20928CauchySchwarzcalc.html
---

## [maths](index.html)
### [Cauchy-Schwarz calc](20928CauchySchwarzcalc.html)

#### [Patrick Massot (May 29 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276213):
Sometimes when someone new comes here to ask maths questions, I wonder if we have a new mathematician interested in Lean. So I googled @**Patrick Stevens**  and found https://www.patrickstevens.co.uk/cauchy-schwarz-proof/

#### [Patrick Massot (May 29 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276218):
So I thought: good opportunity to try again to compute with Lean

#### [Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276275):
And of course I'm disappointed

#### [Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276280):
```lean
import tactic.ring
import analysis.real


lemma key (a b x y : real) : x > 0 →  y > 0 → (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
begin
  intros x_pos y_pos,
  have : x + y > 0 := add_pos_of_pos_of_nonneg x_pos (le_of_lt y_pos),
  suffices : (a+b)^2 ≤ (x+y)*(a^2/x + b^2/y),
  { apply div_le_of_le_mul ; assumption  },
  apply le_of_sub_nonneg,
  apply le_of_mul_le_mul_right _ x_pos,
  apply le_of_mul_le_mul_right _ y_pos,
  rw mul_sub_right_distrib,
  rw mul_sub_right_distrib,
  suffices : 0 ≤ -((a + b) ^ 2 * x * y) + (x + y) * (a ^ 2 / x + b ^ 2 / y) * x * y,
  by simp [*],
  conv
  { to_rhs,
    congr,
    skip,
    rw mul_assoc,
    rw mul_assoc,
    congr, 
    skip,
    rw right_distrib,
    rw ←mul_assoc,
    rw div_mul_cancel _ (ne_of_gt x_pos), 
    rw (show b ^ 2 / y * (x * y) = b ^ 2 / y * (y*x), by simp[mul_comm]),
    rw ←mul_assoc,
    rw div_mul_cancel _ (ne_of_gt y_pos) },
  have : -((a + b) ^ 2 * x * y) + (x + y) * (a ^ 2 * y + b ^ 2 * x) = (a*y-b*x)^2 :=
    begin
      ring,ring,
    end,
  rw this,
  suffices : 0 ≤ (a * y - b * x)*(a * y - b * x),
  { rw pow_succ,
    finish },
  apply mul_self_nonneg,
end
```

#### [Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276289):
It's not only about the banana phone issue

#### [Patrick Massot (May 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276311):
Everything has been painful

#### [Patrick Massot (May 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276316):
How should I write such proofs?

#### [Patrick Stevens (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276375):
That's quite a collection - it's a direct conversion of the one I linked, isn't it, which is very slick for human consumption

#### [Patrick Stevens (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276383):
Presumably there are easier proofs to transcribe for Lean

#### [Andrew Ashworth (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276389):
someday, https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition might show up in Lean

#### [Patrick Massot (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276393):
only the key lemma "Naturally, this lemma is trivial — once it is conceived."

#### [Patrick Massot (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276408):
My interest was not in proving Cauchy-Schwarz. It was this sentence "Naturally, this lemma is trivial — once it is conceived."

#### [Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276413):
use better theorems

#### [Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276424):
e.g. you can use `add_pos` instead of that business

#### [Patrick Massot (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276425):
I did the exercise on paper in 30 seconds and thought I would try in Lean

#### [Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276433):
`add_pos_of_pos_of_nonneg x_pos (le_of_lt y_pos)`

#### [Kenny Lau (May 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276482):
and e.g. there is a theorem linking `(x+y)^-1` to `x^-1` and `y^-1`

#### [Patrick Massot (May 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276498):
I couldn't find add_pos because I was looking for add_pos_of_pos_of_pos

#### [Patrick Massot (May 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276519):
The question is: I stare at my paper proof, how can I get a Lean proof?

#### [Kenny Lau (May 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276524):
a lot of training and familiarity with existing theorems

#### [Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276578):
I did that as training indeed

#### [Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276580):
But probably Andrew is right

#### [Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276581):
We need more automation

#### [Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276583):
nothing else is viable

#### [Patrick Massot (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276598):
Note that the situation would be much worse without `ring`

#### [Andrew Ashworth (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276621):
there are limits to algorithms such as the above though. they will take forever to run if you have a particularly giant set of real inequalities since the time it takes to run increases exponentially vs the number of terms

#### [Kenny Lau (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276622):
I disagree

#### [Kenny Lau (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276626):
but I don't have time to disprove your claim

#### [Patrick Massot (May 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276696):
I should be sleeping anyway (of course I thought this calculation would be shorter...)

#### [Patrick Stevens (May 30 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276810):
Of course, "expand and clear denominators" should be mechanically easy, right? Is there some reason why an "expand" tactic couldn't exist? and "clear denominators" likewise, though that requires a bit of casewise am-i-negative reasoning in general

#### [Andrew Ashworth (May 30 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276908):
if you stuck the same equation into Sage math, what would its simplifier spit out?

#### [Patrick Stevens (May 30 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127276986):
Mathematica:
```
In[43]:= (a + b)^2/(x + y) <= a^2/x + b^2/y // 
 FullSimplify[#, x > 0 && y > 0] &

Out[43]= (b x - a y)^2 >= 0
```

#### [Patrick Stevens (May 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277039):
simplifies to True under the additional assumption that a,b are real

#### [Patrick Stevens (May 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277050):
don't know about sage, i'm afraid

#### [Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277668):
```lean
import data.real.basic tactic.ring

lemma key (a b x y : ℝ) (Hx : x > 0) (Hy : y > 0) :
  (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
have H : ((x+y)*x*y)*((a+b)^2/(x+y)) ≤ ((x+y)*x*y)*(a^2/x + b^2/y),
from calc ((x+y)*x*y)*((a+b)^2/(x+y))
    = x*(y*(a+b)^2) : by rw [← mul_div_assoc, mul_assoc, mul_assoc, mul_div_cancel_left];
  from ne_of_gt (add_pos Hx Hy)
... ≤ x*(y*(a+b)^2) + (a*y-b*x)*(a*y-b*x) : le_add_of_nonneg_right $ mul_self_nonneg _
... = (x+y)*(y*a^2) + (x+y)*(x*b^2) : by ring
... = ((x+y)*x*y)*(a^2/x + b^2/y) :
  by rw [mul_add, ← mul_div_assoc, mul_assoc, mul_assoc, mul_assoc, mul_assoc, mul_div_cancel' _ (ne_of_gt Hy), mul_div_assoc, mul_div_cancel_left _ (ne_of_gt Hx)],
le_of_mul_le_mul_left H $ mul_pos (mul_pos (add_pos Hx Hy) Hx) Hy
```

#### [Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277669):
ok I did use `ring`

#### [Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277672):
@**Patrick Massot**

#### [Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277675):
and I just burnt a lot of my time

#### [Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127277676):
I'm busy

#### [Mario Carneiro (May 30 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127278096):
```
import tactic.ring data.real.basic

theorem pow_two_nonneg {α} [linear_ordered_ring α] (a : α) : 0 ≤ a ^ 2 :=
by rw pow_two; exact mul_self_nonneg _

lemma key (a b x y : ℝ) (x0 : 0 < x) (y0 : 0 < y) : (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
begin
  apply (div_le_iff (add_pos x0 y0)).2,
  apply (mul_le_mul_left (mul_pos x0 y0)).1,
  apply sub_nonneg.1,
  refine calc x * y * ((a ^ 2 / x + b ^ 2 / y) * (x + y)) - x * y * (a + b) ^ 2
       = ((x / x * a ^ 2 * y + y / y * b ^ 2 * x) * (x + y)) - x * y * (a + b) ^ 2 : by ring
   ... = ((a ^ 2 * y + b ^ 2 * x) * (x + y)) - x * y * (a + b) ^ 2 : by simp [ne_of_gt x0, ne_of_gt y0]
   ... = (b * x - a * y) ^ 2 : by ring; ring
   ... ≥ 0 : pow_two_nonneg _
end
```

#### [Mario Carneiro (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127278173):
Since `ring` can handle everything except the divisions, I insert a step in the middle for `simp` to cancel the `x/x` terms, but otherwise this is all `ring`

#### [Mario Carneiro (May 30 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127278788):
or with a bit more up front cross multiplication:
```
lemma key (a b x y : ℝ) (x0 : 0 < x) (y0 : 0 < y) : (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
begin
  rw [div_add_div _ _ (ne_of_gt x0) (ne_of_gt y0),
    div_le_iff (add_pos x0 y0), div_mul_eq_mul_div, le_div_iff (mul_pos x0 y0),
    ← sub_nonneg],
  refine calc 0 ≤ (b * x - a * y) ^ 2 : pow_two_nonneg _
   ... = (a ^ 2 * y + x * b ^ 2) * (x + y) - (a + b) ^ 2 * (x * y) : by ring; ring
end
```

#### [Andrew Ashworth (May 30 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127279233):
^. I feel like whenever I have a complicated thing like this, `calc` is the way to go. And I solve the whole thing by hand on scratch paper, like I time-traveled back to high-school algebra class...

#### [Kenny Lau (May 30 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127279240):
throwbacks

#### [Andrew Ashworth (May 30 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127279293):
but if this stuff is super obvious, and you dislike proving it, why not use `sorry`?

#### [Patrick Massot (May 30 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294574):
Thank you very much Kenny and Mario. Kenny's proof is exactly what I don't want to do (and nobody should have to do if proof assistants want to become tools for mathematicians). Mario's proof is what I wanted to do (clear denominators and use ring). I think the most important thing I missed was:
```lean
example (a x y : ℝ) : x * y * (a^2 / x) =  y * (a^2 *x / x) := by ring
```
I thought that, in such a case, `ring` would see `(a^2 / x)` as atomic and fail. It makes it even harder for me to understand why `ring` couldn't be extended to do the whole computation, searching for `x > 0` or `x ≠ 0` in context

#### [Johan Commelin (May 30 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294647):
`ring` doesn't know anything about orders, right? So it doesn't know what to do with `x > 0`.

#### [Patrick Massot (May 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294690):
it could try to apply `ne_of_gt` and `ne_of_lt` on all hypotheses

#### [Patrick Massot (May 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294714):
One more question for Mario: why did you use `refine` instead of `exact`, which also works and is more explicit?

#### [Johan Commelin (May 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294715):
Buth it isn't meant to be a generic tactic. It only uses ring axioms.

#### [Patrick Massot (May 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294762):
Then give another name to the more general tactic

#### [Johan Commelin (May 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294765):
But you would want to do something like `by schoolkid using ring` or something like that

#### [Johan Commelin (May 30 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294825):
We want a `schoolkid` tactic that does the completely easy stuff, and it should have a feature that you can give it a specialised tactic like `ring` as a hint, so that all of a sudden the schoolkid is lord of the rings.

#### [Patrick Massot (May 30 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294906):
What about building a `clear_denominator` tactic? It would search for all divisions in the goal, generate sub-goals saying denominators are non-zero, try to discharge these goals using assumptions (and `ne_of_gt` and `ne_of_lt` of assumptions), check whether the goal is equality or inequality and apply `mul_le_mul_left` and its friend, followed by `ring` to simplify, and `simp [all stuff ≠ 0 gathered so far]`

#### [Patrick Massot (May 30 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294965):
We really need to get back Simon

#### [Patrick Massot (May 30 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127294967):
@**Simon Hudon** where are you?

#### [Johan Commelin (May 30 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127295049):
Right. A clear denominator tactic makes sense as well.

#### [Johan Commelin (May 30 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127295106):
So, here is a proposal for @**Kevin Buzzard** 's next "Live Zulip": walk through a tactic file, and teach mathematicians how to write tactics (-;

#### [Simon Hudon (May 30 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303161):
Hey @**Patrick Massot**! I haven't completely disappeared. Is it just me or has there been a whole lot more activity in here? It's getting hard to follow part time!

#### [Simon Hudon (May 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303262):
I'm not sure I get what `clear_denominator` would do exactly. How does `mul_le_mul_left` help with division?

#### [Sean Leather (May 30 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303516):
```quote
Is it just me or has there been a whole lot more activity in here?
```
It's not just you. Even being away from Zulip for a weekend leaves one with thousands of messages to either wade through or mark as read. :stuck_out_tongue_closed_eyes:

#### [Simon Hudon (May 30 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303597):
I thought the Zulip threads would help keeping track of stuff. I'm not sure what would make it easier

#### [Simon Hudon (May 30 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303640):
The plus side is, it's awesome that Lean is getting used like this

#### [Patrick Massot (May 30 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303852):
We have trouble with thread discipline

#### [Patrick Massot (May 30 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127303855):
But we try

#### [Simon Hudon (May 30 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127305130):
Yeah? What kind of trouble? It seems like specific threads are getting created for the right subjects. The problem might just be in the number of threads. I don't know if we need to categorize them better or something else

#### [Patrick Massot (May 30 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127305822):
Many thread actually mix different topics

#### [Mario Carneiro (May 30 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306593):
I think Kevin should speak in complete sentences

#### [Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306602):
instead of fragments

#### [Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306607):
of sentences

#### [Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306617):
that create tons of messages and fill

#### [Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306622):
my screen

#### [Simon Hudon (May 30 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127306911):
Yeah I noticed that too. Also, write one message with one self contained question and wait for an answer. Right now, when I see his messages I don't know when he's going to be done writing and I eventually just stop reading. One message would help me (and I suspect others) decide whether the question is something I can help with

#### [Patrick Massot (May 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127312365):
Why did you provoked him?!

#### [Simon Hudon (May 30 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315830):
Provoke how?

#### [Patrick Massot (May 30 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315894):
Did you see how many times he hit return in the middle of a sentence since you posted that message?

#### [Patrick Massot (May 30 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315903):
That's all your fault :stuck_out_tongue_winking_eye:

#### [Simon Hudon (May 30 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315921):
Haha! I'm secretly a terrorist!

#### [Simon Hudon (May 30 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315925):
Sorry typo: theorist

#### [Simon Hudon (May 30 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127315967):
I don't follow that thread so I didn't suffer the consequences of that carnage

#### [Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317785):
```quote
So, here is a proposal for @**Kevin Buzzard** 's next "Live Zulip": walk through a tactic file, and teach mathematicians how to write tactics (-;
```
So I was just catching up in this thread, and you and Patrick were talking about tactics and "maybe Simon can write us a tactic" -- and who is the only mathematician who knows how to write tactics? I reckon it's @**Scott Morrison** . Scott -- how did you learn to write tactics? I don't want to keep pestering Simon. I see dumb stuff like the proof that pnat is a comm_monoid, and the proof of every axiom is "it's true for nat so done"

#### [Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317833):
and that happened to me several times myself when doing comm_ring stuff with schemse

#### [Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317842):
"I've got to prove this direct limit satisfies all the ring axioms"

#### [Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317843):
"let's see what this entails"

#### [Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317850):
"it entails invoking that same axiom for that other ring"

#### [Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317866):
It's about time I learnt to automate that. It comes up a lot.

#### [Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317878):
When we start on perfectoid spaces we'll be proving limits of topological rings are topological rings

#### [Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317892):
there's going to be a lot of "this proof is obvious but not rfl" stuff

#### [Kevin Buzzard (May 30 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127317937):
and this can surely be done with tactics

#### [Simon Hudon (May 30 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127320901):
I actually enjoy getting your automation challenges. I admit (sorry!) that I'm not as quick to address them as I'd like. And lately, I've only gotten slower as I took a part time job and stepped up my writing efforts

#### [Sebastien Gouezel (May 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127322540):
Just for fun, I checked it in Isabelle to see where next-level automation can get you. It did not work directly, but almost:
```
lemma
  fixes a b x y::real
  assumes "x > 0" "y > 0"
  shows "(a+b)^2/(x+y) ≤ a^2/x + b^2/y"
proof -
  have "(a * y - b * x)^2 ≥ 0" by simp
  then show ?thesis
    using assms by (simp add: algebra_simps divide_simps power2_eq_square)
qed
```
I first tried to show the goal just by applying `simp` with `divide_simps` and  `algebra_simps` (simplification rules which clear out divisors, and apply associativity, commutativity), but square expansion is not automatic so I had to add it simp. It reduced everything to something which clearly was equivalent to the positivity of `(ay-bx)^2`, so I added it as an intermediate step, and done. No piece of paper, no computation on my side (and no fancy tactic such as `ring` or `omega`, everything was done by the simplifier). I really hope Lean can do the same in the near future!

#### [Mario Carneiro (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127322647):
The main problem with using `simp` for ring equalities is that simp isn't good with cancelling negatives

#### [Sebastien Gouezel (May 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127323145):
To be honest, `simp` in Isabelle is in fact `simp` on steroids: it has built-in "simprocs" that will cancel out negatives, group together common factors, and things like that. I guess it makes `by (simp add: algebra_simps)` as powerful as the `ring`tactic in Lean. If I understand correctly, Johannes is working on simprocs for Lean, right?

#### [Johannes Hölzl (May 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127323497):
Yes, I'm working on a simplifier tactic with simp proc support.

#### [Johan Commelin (May 30 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127323678):
Is there a one-line explanation of what "simpprocs" are?

#### [Johannes Hölzl (May 30 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz calc/near/127324193):
instead of simp rules, it is a tactic which gets invoced by the simplifier. E.g. canellation would be a simproc which is called on a pattern of the form `_ = _` where the type of _  has a cancellative monoid, then it tries to find common elements on both sides of the equation and remove them.

