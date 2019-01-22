---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66011performanceofassumption.html
---

## [general](index.html)
### [performance of `assumption`](66011performanceofassumption.html)

#### [Sebastien Gouezel (Oct 31 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136852607):
I just encountered a weird performance issue. In the middle of a rather long proof, I have just proved a fact that I want to use next. If I use `exact this`, this takes less than 3ms. But `assumption` takes 7 seconds... Of course, in this specific case this is not a problem, but first I was using a tactic that calls `assumption`, several times in the proof, and the whole proof then took more than 30s. Is there a way to understand what is going on?

My goal looks like `dist (⇑f x') (⇑g x') ≤ ε / 4`. The output of the profiler on `assumption` is
```lean
elaboration: tactic compilation took 3.03ms
essai.lean:520:29: information tactic profile data

elaboration: tactic execution took 7.06s
num. allocated objects:  153
num. allocated closures: 126
 7060ms   100.0%   tactic.find_same_type._main._lambda_1
 7060ms   100.0%   tactic.find_same_type
 7060ms   100.0%   tactic.assumption._lambda_1
 7060ms   100.0%   tactic.unify
 7060ms   100.0%   tactic.istep
 7060ms   100.0%   _interaction._lambda_2
 7060ms   100.0%   scope_trace
 7060ms   100.0%   interaction_monad_orelse
 7060ms   100.0%   tactic.istep._lambda_1
 7060ms   100.0%   tactic.step
```

For the record, here is the list of the local facts I have. The issue is probably coming from one of them...
```lean
β : Type v,
_inst_2 : metric_space β,
α : Type u,
_inst_4 : metric_space α,
_inst_5 : compact_space α,
_inst_6 : compact_space β,
b : ℝ → ℝ,
ε : ℝ,
εpos : ε > 0,
εpos8 : ε / 8 > 0,
b_lim : ∀ (ε : ℝ), ε > 0 → (∃ (δ : ℝ) (H : δ > 0), ∀ {x : ℝ}, dist x 0 < δ → dist (b x) 0 < ε),
δ : ℝ,
δpos : δ > 0,
hδ : ∀ {x : ℝ}, dist x 0 < δ → dist (b x) 0 < ε / 8,
tα : set α,
this_h_w : tα ⊆ univ,
finite_tα : finite tα,
htα : univ ⊆ ⋃ (x : α) (H : x ∈ tα), ball x δ,
tβ : set β,
this_h_w_1 : tβ ⊆ univ,
finite_tβ : finite tβ,
htβ : univ ⊆ ⋃ (y : β) (H : y ∈ tβ), ball y (ε / 8),
fin_univ : finite univ,
F : β → β,
hF : ∀ (y : β), F y ∈ tβ ∧ dist y (F y) < ε / 8,
approx : bounded_continuous_map α β → ↥tα → ↥tβ := λ (f : bounded_continuous_map α β) (a : ↥tα), ⟨F (⇑f ↑a), _⟩,
f g : bounded_continuous_map α β,
f_eq_g : approx f = approx g,
hg : ∀ (x y : α), dist (⇑g x) (⇑g y) ≤ b (dist x y),
hf : ∀ (x y : α), dist (⇑f x) (⇑f y) ≤ b (dist x y),
x x' : α,
x'tα : x' ∈ tα,
hx' : dist x x' < δ,
F_f_g : F (⇑f x') = F (⇑g x'),
this : b (dist x x') ≤ ε / 8,
this : b (dist x' x) ≤ ε / 8,
this : dist (⇑f x') (⇑g x') ≤ ε / 4
```
(one bonus point for you if you can guess which theorem I am proving from this output :)

#### [Rob Lewis (Oct 31 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136854109):
You could try `clear`ing hypotheses one by one until `assumption` succeeds quickly. This would at least point out which hypothesis is causing the problem.

#### [Rob Lewis (Oct 31 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136854136):
Just to check -- if you remove the hypothesis that you want it to find, it takes 7 seconds and then fails, right?

#### [Sebastien Gouezel (Oct 31 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136855236):
Excellent idea. Here is the minimized outcome, which really looks like a bug somewhere.
```lean
lemma foo {x y z ε : ℝ} (a : x ≤ ε/8) (b : y ≤ ε/8) (c : z ≤ ε/4) : z ≤ ε/4 := by assumption
```
takes 8 seconds. Remove `a` or `b`, it goes down by 4 seconds. Without any of them, 3ms...

#### [Sebastien Gouezel (Oct 31 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136855749):
The problem is that 4 and 8 are big numbers for reals. You can trigger the same problem with rationals if you increase slightly the numbers:
```lean
lemma foo {x z ε : ℚ} (a : x ≤ ε/2) (b : z ≤ ε/100) : z ≤ ε/100 := by assumption
```
triggers a timeout on my machine...

#### [Floris van Doorn (Oct 31 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136856013):
If I make the definition of inequality irreducible in `real.basic`:
```
protected def le (x y : ℝ) : Prop := x < y ∨ x = y
instance : has_le ℝ := ⟨real.le⟩
[...]
attribute [irreducible] real.le
```
then `assumption` is instant again. Apparently `assumption` had to do an awful lot of unfolding. 
Probably `lt` and `le` in `real` should be irreducible, after some basic facts have been proven about it.

#### [Chris Hughes (Oct 31 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136856465):
I think I remember Mario saying something about `assumption` trying to reduce all the hypotheses. I guess `le` and division are hard to reduce on reals. This example takes 11s to fail on my machine.
```lean
example {x z ε : ℝ} : (x ≤ ε / 8) = (z ≤ ε / 4) := by refl
```
 Maybe `le` and division should be irreducible.

#### [Sebastien Gouezel (Oct 31 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136856827):
Your example is not specific to reals:
```lean
example {x z ε : ℚ} : (x ≤ ε /2) = (z ≤ ε / 100) := by refl
```
also fails.

#### [Rob Lewis (Oct 31 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136858710):
Making the orders on `rat` and `real` irreducible only breaks things at one spot in `analysis.complex`, and then all of these examples are instant. I think this is the correct setup. I'll PR this in a sec.

#### [Sebastien Gouezel (Oct 31 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136859630):
Thanks a lot!

#### [Kevin Buzzard (Oct 31 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136859919):
@**Kenny Lau** maybe it's about time you went through all of mathlib changing all `assumption`s to what they are supposed to say?

#### [Kenny Lau (Oct 31 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136859956):
good idea

#### [Kenny Lau (Oct 31 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136859973):
but why am I the only one to make mathlib faster?

#### [Johan Commelin (Oct 31 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136861850):
```quote
@**Kenny Lau** maybe it's about time you went through all of mathlib changing all `assumption`s to what they are supposed to say?
```
What is this? @**Kevin Buzzard** I really think we should improve the system. These things should be solved by making the computer smarter, instead of making our proofs more explicit. Automation is good.

#### [Kevin Buzzard (Oct 31 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136861889):
But `assumption` will never be as fast as `exact H57` ;-)

#### [Johan Commelin (Oct 31 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136861957):
It should be fast enough that we don't have to care. And caching should make sure that we also don't need to care about 10s proofs.

#### [Mario Carneiro (Nov 01 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136887687):
I think this is a major problem for Sebastien's proof style, which uses `<x ≤ ε /2>` in place of `h1` all over the place, and avoids labeling hypotheses. This is turned into `show x ≤ ε /2, by assumption` and hence can be very slow if there are "similar" hypotheses that require a lot of unfolding. This is one of the reasons I prefer naming hypotheses - it's shorter, and faster.

#### [Mario Carneiro (Nov 01 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136887835):
The short answer is "`assumption` considered harmful". This is why stuff like `rw [...], refl` sometimes succeeds where `rw [...]` fails, because `rw` tries to close with reflexivity but it doesn't try very hard for performance reasons. `assumption` has no such limiter.

#### [Johan Commelin (Nov 01 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136903475):
I am really unhappy with "`assumption` considered harmful". Is this a theoretical problem? Or could someone with enough skills and free time write a faster version of `assumption`?

#### [Andrew Ashworth (Nov 01 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136903672):
you could potentially write a "dumber" version of assumption that doesn't do as much definitional unfolding, and that would indeed be faster, but also potentially less useful

#### [Kenny Lau (Nov 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136907300):
... or we can dovetail it?

#### [Kevin Buzzard (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136907364):
Isn't `assumption` being asked to do the impossible? The claim is that there's a term in the local context whose type is that of the goal. A human might go through each of the terms and say "no, no, maybe, no, no, no, ...ooh! Yes!"

#### [Kevin Buzzard (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136907406):
but Lean gets interested in the "maybe" and what can you do?

#### [Kenny Lau (Nov 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136907846):
we can dovetail it.

#### [Johan Commelin (Nov 01 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136909675):
I think this is a good idea. But I have no idea how to implement the dovetailing in Lean. (For those who don't know what dovetailing is: basically just look at all the assumptions in parallel, if one works, stop looking at the others.)

#### [Kevin Buzzard (Nov 01 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136909782):
Ha ha, and then the one tactic which I understand the Lean code for will be gone :-)

#### [Mario Carneiro (Nov 01 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136910450):
Yes it's possible to do `assumption` in parallel, but it's overkill

#### [Mario Carneiro (Nov 01 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136910504):
`assumption` is one of the oldest and simplest tactics, and I think its simplicity is turning out to not be a good thing

#### [Mario Carneiro (Nov 01 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136910540):
The easy solution is just not to use full defeq in `assumption`

#### [Mario Carneiro (Nov 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136910568):
just set `md := semireducible` like all the newer tactics

#### [Reid Barton (Nov 01 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136920250):
The slow examples above aren't really specific to `le`, by the way--this one is also slow
```lean
example {x y z ε : ℝ} : (x + y = z + ε / 8) = (x + y = z + ε / 4) := by refl
```

#### [Reid Barton (Nov 01 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136920384):
With bigger numbers, even addition is slow.

#### [Floris van Doorn (Nov 01 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136923924):
```quote
just set `md := semireducible` like all the newer tactics
```
Looking at the implementation, it seems like `assumption` is already calling `unify` with the (implicit) argument `md := semireducible`.

#### [Floris van Doorn (Nov 01 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance of `assumption`/near/136923989):
I think a whole lot more should be irreducible, like `add`, `neg`, `mul` and `inv` for `cau_seq.completion`.

