---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/02588uniformcontinuouscontinuous.html
---

## Stream: [maths](index.html)
### Topic: [uniform_continuous.continuous](02588uniformcontinuouscontinuous.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242464):
Still trying to clean up topology stuff, I realized the proof that [uniform continuous functions are continuous](https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L487-L500) is pretty hard to read. @**Johannes Hölzl** how do you like the following proof:
```lean
lemma uniform_continuous.continuous [uniform_space β] {f : α → β}
  (hf : uniform_continuous f) : continuous f :=
begin
  rw continuous_iff_tendsto,
  intro a,
  have key : prod.mk (f a) ∘ f = (λ p : α×α, (f p.1, f p.2)) ∘ prod.mk a, by simp,
  rw [tendsto_iff_comap, nhds_eq_comap_uniformity, nhds_eq_comap_uniformity, comap_comap_comp, key],
  conv_rhs { rw ←comap_comap_comp },
  apply comap_mono,
  rw ←map_le_iff_le_comap,
  exact hf
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242558):
I don't like this at all. I'm okay with adding `show` or similar to the original proof. But replacing it with an arbitrary sequence of tactic calls doesn't make it more readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242570):
The main difference is I use [nhds x = uniformity.comap (prod.mk x)](https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L261) instead of [nhds x = uniformity.lift' (λs:set (α×α), {y | (x, y) ∈ s})](https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L267)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242582):
It's not all about using tactic instead of term mode, it's a math difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242624):
I can rewrite it using calc if you prefer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242626):
This is indeed a good change. But it would be nice if the proof structure wouldn't be hidden behind the tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242631):
Yes, this would be good!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242736):
The key annoyance (here and elsewhere in this corner of mathlib) is how Lean notation is far less legible that paper notation when it comes to pull-back and push-forward. And also we don't have notation for `(λ p : α×α, (f p.1, f p.2))` (this one is probably solvable) Compare $$U_\alpha \leq (f \times f)^*U_\beta$$ and `uniformity ≤ comap (λ p : α×α, (f p.1, f p.2)) uniformity`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242990):
isn't this `prod.map f f`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243305):
Indeed it is! But not by definition :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243322):
Johannes, do you think we should rewrite everything using this `prod.map` in the definition of uniform continuity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243445):
ouch, I think `prod.map` should have a different def, `(prod.map f g p).1 = f p.1` should be defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 20 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243470):
what about adding `def prod.map₂ {α β} (f : α → β) (p : α × α) : β × β := (f p.1, f p.2)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243537):
This clever guy noticed how  I love subscript 2 those days.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243552):
I guess this can be `map₂ f = map f f` once the definition of `map` is fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152244491):
I used prod.map for a reformulation of cauchy_seq in the contraction mapping stuff, but it didn't seem well-supported with theorems. I also had to define a partial order on products.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152245261):
@**Johannes Hölzl** see https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/calc.20iff/near/152245238


{% endraw %}
