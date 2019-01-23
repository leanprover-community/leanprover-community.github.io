---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60371theoremAreaofCircle.html
---

## Stream: [new members](index.html)
### Topic: [theorem Area_of_Circle](60371theoremAreaofCircle.html)

---


{% raw %}
#### [ Mii Nguyen (Nov 28 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720034):
Hello. I'm My, a very new beginner of Lean user.  I come from Formal Abstract's group in Hanoi. Recently I try to formalize the theorem of  'Area of a circle'. So far I have

```
theorem Area_of_Circle (x: ℝ × ℝ) (r :ℝ) (r ≥ 0) [measure_theory.measure_space (ℝ × ℝ)] [measure_theory.measure_space (closed_ball (x) (r))]: measure_theory.volume(closed_ball (x) (r)) = 2 * real.pi * r^2 :=sorry 
```

It seems to work. But if I defined the Circle, then use it in the theorem, it sends me an error 'don't know how to synthesize placeholder'

```
variables {x: ℝ × ℝ }{r: ℝ}

def Circle{x: ℝ × ℝ }{r: ℝ} {r ≥ 0} := closed_ball (x) (r)

theorem Area (r ≥ 0) [measure_theory.measure_space (ℝ × ℝ)] [measure_theory.measure_space (Circle)]: measure_theory.volume(Circle) = 2 * real.pi * r^2 :=sorry 
#print Area
```

Could anyone please explain it to me?  How can I defind a set the use it in theorem? Thank you very much for your time,
My

#### [ Johan Commelin (Nov 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720601):
The `[measure_theory.measure_space (ℝ × ℝ)]` introduces a new measure (about which you can't say anything).

#### [ Kevin Buzzard (Nov 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720622):
Yes -- you should delete this

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720633):
You would want to use the existing measure. And probably you want to use integration to calculate the area.

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720691):
So far there is very little about integration, as far as I know.

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720705):
So I fear this is going to be a pretty hard exercise.

#### [ Johan Commelin (Nov 28 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721396):
Or well, if you only want to state the theorem (not prove it), that should be possible.

#### [ Johan Commelin (Nov 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721494):
@**Mii Nguyen** I think you should also make the `x` and `r` arguments to `Circle` explicit. (By using `()` instead of `{}`.) That way it is clearer about which circle you are talking.

#### [ Patrick Massot (Nov 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721933):
I just had a look, it seems we have Lebesgue measure for R, but no product instance for measurable spaces, so that would be needed in order to state this theorem. It shouldn't be hard. As Johan wrote,  you also need better understanding of implicit vs explicit arguments. A better starting point would be:
```lean
import analysis.measure_theory.lebesgue_measure
import analysis.exponential
open real

def Circle (x: ℝ × ℝ) (r: ℝ)  := closed_ball x r

theorem Area (x : ℝ × ℝ) {r : ℝ} (H : r ≥ 0) : measure_theory.volume(Circle x r) = some ⟨2 * pi * r^2, _⟩ :=sorry
```

#### [ Patrick Massot (Nov 28 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722012):
The underscore at the very end is an exercise to fill in, it must be replaced by a proof of `0 <= 2 * pi * r^2`

#### [ Patrick Massot (Nov 28 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722176):
After filling in this proof, Lean will still complain it doesn't know what measure to use on ℝ × ℝ but, as  I wrote, this require adding something to mathlib

#### [ Patrick Massot (Nov 28 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722321):
The `some` is a bit annoying, it's there in order to indicate that this disk has finite measure. I guess the interface is still very rough here

#### [ Chris Hughes (Nov 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722740):
I thought the area of a circle was $$\pi r^2$$ not $$2\pi r^2$$

#### [ Patrick Massot (Nov 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722777):
also

#### [ Patrick Massot (Nov 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722858):
And also I would call this a disk, not a circle, but that may be only in France

#### [ Patrick Massot (Nov 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148723572):
@**Mii Nguyen** do you want to work on the exercise of stating this theorem after admitting the existence of some relevant measure on the plane, or do you want to get an answer? I did the exercise, so I wouldn't cost me anything, but I don't want to ruin your training plan.

#### [ Mii Nguyen (Nov 28 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148724576):
Thank you for your advices!
@**Johan Commelin**  I  tried to use integration at the first time but I lost in the maze of `intergration.lean`
@**Johan Commelin**  @**Patrick Massot**  by that, I know that I need to work more in arguments. Thank you
I need to declare that Circle (dist) is measurable, so I use [measure_theory.measure_space (Circle)]
The exercise is good for me. So I will try to instance Lebesgue measure for RxR in mathlib.

#### [ Patrick Massot (Nov 28 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148724821):
Let me insist that correctly instantiating `measure_space (ℝ × ℝ)` is much harder than admitting its existence and finishing stating the disk area theorem. I suggest the later as a first exercise


{% endraw %}
