---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/76959Canconvbeusedtousenestedhypotheses.html
---

## Stream: [new members](index.html)
### Topic: [Can conv be used to use nested hypotheses?](76959Canconvbeusedtousenestedhypotheses.html)

---

#### [Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150884801):
The situation is as follows: I have a proof of:
```lean
convertor :
  ∀ (h : ℝ),
    h ≠ 0 → (f (g (x + h)) - f (g h)) / h = (f (g (x + h)) - f (g h)) / (g (x + h) - g x) * (g (x + h) - g x) / h
```
And I have the following goal in which I need to perform a rewrite using `convertor`:
```lean
∀ (ε : ℝ),
    ε > 0 →
    (∃ (δ : ℝ) (H : δ > 0),
       ∀ (h : ℝ),
         h ≠ 0 → abs h < δ → abs ((f (g (x + h)) - f (g x)) / h - (λ (x : ℝ), f' (g x) * g' x) x) < ε)
```

Within the goal, we have the nested hypothesis ` ∀ (h : ℝ), h ≠ 0` which is needed to apply `convertor`. But I can't perform this rewrite without unfolding everything.

#### [Kenny Lau (Dec 04 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150884874):
`simp only [convertor]`

#### [Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885042):
Doesn't work.

#### [Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885084):
Oh wait, there's a typo in my convertor -- nope, still doesn't work.

#### [Kenny Lau (Dec 04 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885093):
`simp only [convertor] {contextual:=tt}`

#### [Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885178):
Still doesn't work.

#### [Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885310):
What exactly would `simp` be doing behind the scenes here? Something involving `conv`? Or something else? Is there any way that I can dig into it the way `simp` is supposed to work?

#### [Kevin Buzzard (Dec 04 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885899):
See if forall h, h ne 0 -> X = Y can ever be used to rewrite forall h, h ne 0 -> something else -> X = Z maybe?  I mean do some experiments. If the rewrite never works you could ask on #general...oh, I just noticed that you're asking on the main chat anyway :-) sorry.

#### [Patrick Massot (Dec 05 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150912877):
@**Abhimanyu Pallavi Sudhir** this is typically a case where you need to paste a MWE if you really want help. Reluctant rewriting is a complicated topic, and the answer very much depends on the specific situation. Meanwhile you can learn a couple of important lessons:

#### [Patrick Massot (Dec 05 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150912960):
When using Lean, you need to reconsider every side assumption. They will be a pain, whatever the situation, and we have all sorts of tricks to avoid them. One of Kevin's favorite ones is how division is totalized. You convertor lemma (without typos) does not need assumptions, thanks to the division trick:
```lean
lemma convertor (x : ℝ) (f g : ℝ → ℝ):
  ∀ (h : ℝ),
     (f (g (x + h)) - f (g x)) / h = (f (g (x + h)) - f (g x)) / (g (x + h) - g x) * (g (x + h) - g x) / h :=
begin
  intros,
  by_cases H : g (x+h) - g x = 0,
  { rw [H, mul_zero, zero_div, eq_of_sub_eq_zero H, sub_self, zero_div] },
  { rwa div_mul_cancel },
end
```

#### [Patrick Massot (Dec 05 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150913069):
The other lesson is that you shouldn't be doing all those computations, you should have better infrastructure. This is why I should be working on the big-O/little-o library, but I don't have enough time (but maybe you don't know yet [this technology](https://en.wikipedia.org/wiki/Big_O_notation))

#### [Kenny Lau (Dec 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150914237):
well I find it useful that `f` is differentiable at `p` iff `f(p+h) = f(p) + h f1(h)` for some `f1` continuous at `0` with `f1(0) = f'(p)`. Chain rule follows immediately:
1. `for all h, f(p+h) = f(p) + h f1(h)` with `f1` continuous and `f1(0) = f'(p)`
2. `for all h, g(f(p)+h) = g(f(p)) + h g1(h)` with `g1` continuous and `g1(0) = g'(f(p))`
3. `for all h, g(f(p+h)) = g(f(p) + h f1(h)) = g(f(p)) + h f1(h) g1(h f1(h))`, and then `f1(h) g1(h f1(h))` is continuous at `0`, and also `f1(0) g1(0 f1(0)) = f'(p) g'(f(p))`

#### [Patrick Massot (Dec 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150915954):
We already discussed that trick here. What you wrote is the full extent of what it can do, and you'll have to prove this is equivalent to the usual definition (which is more convenient for everything else) anyway, so the gain is not even that large.

#### [Patrick Massot (Dec 05 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150916063):
Of course all this (the explicit computation with quotient and the exotic definition of derivatives) is perfectly fine for experimentation purposes, what I'm describing is the library building point of view

#### [Kevin Buzzard (Dec 05 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150919265):
Abhi is (perhaps at my suggestion) working on a simple library for differentiating functions of one real variable. I know that others have promised some much better things, but Abhi is a first year undergraduate and we are just experimenting and learning as we go. Does anyone know how this stuff is done in Coq, or any other system which implements dependent type theory in pretty much the same general way as Lean? In fact, which other systems have this property? I'm sure Isabelle will have this stuff, but my understanding is that Isabelle has a very different kind of type theory. How do I go about finding out how this stuff is implemented in Coq? Is it easiest to just ask on some Coq mailing list? Is https://github.com/coq-contribs any use? I would like to know more about what has been done before. Is Coq the only system that is similar enough to Lean to make a comparison worthwhile?

#### [Abhimanyu Pallavi Sudhir (Dec 05 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150920025):
```quote
@**Abhimanyu Pallavi Sudhir** this is typically a case where you need to paste a MWE if you really want help. Reluctant rewriting is a complicated topic, and the answer very much depends on the specific situation. Meanwhile you can learn a couple of important lessons:
```
 Thanks @**Patrick Massot** -- I tried using `ring` and it didn't work, so I decided that the division by zero trick didn't work for some reason. I would've posted an MWE, but it was a bit large -- I'll try the experiments @**Kevin Buzzard** suggested to get a better feel of contextual rewrites.

#### [Patrick Massot (Dec 05 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150927121):
As I wrote, I know this is only experimentation, but I hope it's still useful to have information from the library point of view. The chain rule in Coq is at https://github.com/math-comp/analysis/blob/master/derive.v#L699-L702. I think Isabelle is already a bit too different for comparing here.

#### [Patrick Massot (Dec 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150927255):
Well, it's more honest to point to https://github.com/math-comp/analysis/blob/master/derive.v#L687-L697

