---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57481LeanLaTeX.html
---

## Stream: [general](index.html)
### Topic: [Lean + LaTeX?](57481LeanLaTeX.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 23 2019 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156681378):
I've been reading work of Lamport about structured proofs.  Here's an extract from https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean :

```lean
-- We now prove that if aₙ → l and bₙ → m then aₙ + bₙ → l + m.
theorem tendsto_add (a : ℕ → ℝ) (b : ℕ → ℝ) (l m : ℝ)
  (h1 : is_limit a l) (h2 : is_limit b m) :
  is_limit (a + b) (l + m) :=
begin
  -- let epsilon be a positive real
  intros ε Hε,
  -- We now need to come up with N such that
  -- n >= N implies |aₙ + bₙ - (l + m)| < ε.
  -- Well, note first that epsilon / 2 is also positive.
  have Hε2 : ε / 2 > 0 := by linarith,
  -- Choose large M₁ such that n ≥ M₁ implies |a n - l| < ε /2,
  cases (h1 (ε / 2) Hε2) with M₁ HM₁,
  -- and similarly choose M₂ for the b sequence. 
  cases (h2 (ε / 2) Hε2) with M₂ HM₂,
  -- let N be the max of M1 and M2
  let N := max M₁ M₂,
  -- and let's use this value of N.
  use N,
  -- Of course N ≥ M₁ and N ≥ M₂.
  have H₁ : N ≥ M₁ := le_max_left _ _,
  have H₂ : N ≥ M₂ := le_max_right _ _,
  -- Now say n ≥ N.
  intros n Hn,
  -- Then obviously n ≥ M₁...
  have Hn₁ : n ≥ M₁ := by linarith,
  -- ...so |aₙ - l| < ε /2
have H3 : |a n - l| < ε / 2 := HM₁ n Hn₁,
...
```
and so on and so on. The point is that I am spelling out the proof I would tell mathematicians in comments, and writing Lean code, which is sometimes self-evident (`intros n Hn`) and sometimes much harder for beginners to understand (e.g. using `le_max_left` -- a student could look up what this did, but it's much harder for them to find this function for themselves, and there are far more contrived lines in other parts of this repo). 

I would like to make this look really sexy and I am almost sure that this should be possible with known technology. My dream would be to have what looks like a LaTeX document (perhaps viewed through a web browser) and when you hover over e.g. "Then obviously n >= M_1" you get some transient box which says `have Hn₁ : n ≥ M₁ := by linarith,`, and if you click on it then you somehow end up viewing a Lean file, or part of a Lean file, where you can look at the goal and change / edit things and play around (and then hit the "reset" button when you've screwed everything up).

In other words, I'd like to have some sort of thing which I can present as a "formally verified, but looks like LaTeX, proof that the limit of the sum is the sum of the limits". 

I have no doubt that this sort of thing is possible. I've learnt sphinx but I am not quite sure if it is the tool for the job. Does anyone have any suggestions as to how one might be able to do this? There is no particular time frame and if it involves writing a bunch of code then maybe I can find people who will write this code for me. @**Edward Ayers** @**Patrick Massot** do either of you know about this kind of thing? 

When it comes to writing Lean code I am 100% convinced that I could write code in the above style which could become "online notes" for a beginning analysis course (such as, let's say, the beginning analysis course in Imperial's new curriculum which starts in October). The notes would have the advantage that they are formally verified. But I do not understand enough about how to build the app I envisage and I would dearly like to hear some suggestions!

#### [ Johan Commelin (Jan 23 2019 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156682310):
Do you remember Neil Stricklands demo? That might be a first approximation of what you want.

#### [ Johan Commelin (Jan 23 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156682399):
I meant this one: http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/

#### [ Kevin Buzzard (Jan 23 2019 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156683049):
Ooh -- thanks for digging that up! @**Neil Strickland** how did you make this? My plan would be to hide the Lean completely and just have standard maths proof prose visible initially, but one can somehow open up the Lean to see it if one wants to.


{% endraw %}
