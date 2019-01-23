---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/38567leakingconstruction.html
---

## Stream: [maths](index.html)
### Topic: [leaking construction](38567leakingconstruction.html)

---


{% raw %}
#### [ Patrick Massot (Sep 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622397):
Sometimes I see things like: `quot.lift (λ (a₁ : cau_seq ℚ abs), quotient.lift (has_lt.lt a₁) _ ε) _` in my tactic state when playing with real numbers. It looks like internal details of the constructions are leaking. What does it mean? Can I avoid that?

#### [ Mario Carneiro (Sep 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622571):
how are you "playing"?

#### [ Mario Carneiro (Sep 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622577):
if you unfold stuff you can see this

#### [ Patrick Massot (Sep 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622621):
More precisely, I have:
```lean
α : Type u_2,
_inst_1 : metric_space α,
β : Type u_3,
u : β → α,
f : filter β,
ε : ℝ,
this : ball a ε ∈ (map u f).sets
```
If I do `have:= mem_map.2 this` then the new this is the horror
```lean
quot.lift (λ (a₁ : cau_seq ℚ abs), quotient.lift (has_lt.lt a₁) _ ε) _ ∈   (map (λ (y : α), dist y a) (map u f)).sets
```
but I can do instead `have : {b | u b ∈ ball a ε} ∈ f.sets := mem_map.2 this,` and Lean won't unfold it

#### [ Mario Carneiro (Sep 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622685):
You are going the wrong way

#### [ Mario Carneiro (Sep 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622686):
use `mem_map.1 this`

#### [ Mario Carneiro (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622735):
(it works because the two sides are defeq so it doesn't really matter if you apply it, but then the matching goes crazy)

#### [ Patrick Massot (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622736):
oh

#### [ Patrick Massot (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622737):
weird

#### [ Patrick Massot (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622751):
That's biconditional in action: try one direction at random and, if Lean is willing to apply it, never look back

#### [ Mario Carneiro (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622752):
notice that you have another `map` in the result

#### [ Mario Carneiro (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622755):
`(map (λ (y : α), dist y a) (map u f)).sets`

#### [ Patrick Massot (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622757):
true

#### [ Mario Carneiro (Sep 09 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622809):
so it tried to figure out how to read `ball a ε` as `{x | m x ∈ t}` for some `m, t` and chaos ensues

#### [ Patrick Massot (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622819):
That's wonderful. In the proof I posted earlier:
```lean
example (u : ℕ → α) (a : α) : tendsto u at_top (nhds a) ↔ 
  ∀ ε > 0, ∃ (N : ℕ), ∀ {n}, n ≥ N → dist (u n) a < ε :=
⟨λ H ε εpos, mem_at_top_sets.1 $ mem_map.2 $ H (ball_mem_nhds _ εpos),
 λ H s s_nhd, let ⟨ε, εpos, sub⟩ := mem_nhds_iff_metric.1 s_nhd in
   let ⟨N, H'⟩ := H ε εpos in mem_at_top_sets.2 ⟨N, λ n nN, 
   sub $ mem_ball.2 $ H' nN⟩⟩
```
There is a `$ mem_map.2 $ `. You can change 2 into 1, it still works. Then you can remove that bit entirely and it still works!

#### [ Mario Carneiro (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622825):
because the proof is `rfl`

#### [ Patrick Massot (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622827):
Yeah, I understand

#### [ Johannes Hölzl (Sep 10 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133633334):
`simp` can do this:
```lean
lemma tendsto_at_top_nhds_metric [metric_space α] {f : ℕ → α} {a : α} :
  tendsto f at_top (nhds a) ↔ (∀ε>0, ∃N, ∀n≥N, dist (f n) a < ε) :=
by simp [tendsto_infi, tendsto_principal, nhds_eq_metric]
```
The trick is to unfold `nhds_eq_metric` and rhen focus on the right side: An infimum is equal to a quantifier around the `tendsto`, until it reaches `principal`, then it is reduced to membership in `at_top`.
Other examples
```lean
lemma tendsto_at_top_at_top {f : ℕ → ℕ} :
  tendsto f at_top at_top ↔ (∀M, ∃N, ∀n≥N, M ≤ f n) :=
by conv { to_lhs, congr, skip, skip, rw [at_top] }; simp [tendsto_infi, tendsto_principal]
```
or
```lean
lemma tendsto_nhds_metric_nhds_metric [metric_space α] [metric_space β]
  {f : α → β} {a : α} {b : β}:
  tendsto f (nhds a) (nhds b) ↔ (∀ε>0, ∃δ>0, ∀x, dist x a < δ → dist (f x) b < ε) :=
begin
  conv { to_lhs, congr, skip, skip, rw [nhds_eq_metric] },
  simp [tendsto_infi, tendsto_principal, mem_nhds_iff_metric, set.subset_def]
end
```
Here the annoying part is that we need to focus on the right `nhds` or `at_top`.


{% endraw %}
