---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/20349UniformlyContinuousonMetricSpaces.html
---

## [maths](index.html)
### [Uniformly Continuous on Metric Spaces](20349UniformlyContinuousonMetricSpaces.html)

#### [Rohan Mitta (Sep 26 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666418):
Have I formalised this right and is it in mathlib?

```lean
import analysis.metric_space 

example {X : Type*} {Y : Type*} [metric_space X] [metric_space Y] (f : X → Y) : 
uniform_continuous f ↔ ∀ ε, ε > 0 → ∃ δ (H : δ > 0), ∀ x₁ x₂ : X, 
  dist x₁ x₂ < δ → dist (f x₁) (f x₂) < ε := sorry
```

#### [Johannes Hölzl (Sep 26 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666547):
looks good to me, and I don't think we have it in mathlib yet

#### [Johannes Hölzl (Sep 26 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666569):
sorry, just found it `uniform_continuous_of_metric `

#### [Kevin Buzzard (Sep 26 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666760):
Thanks Johannes!

#### [Patrick Massot (Sep 26 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668357):
Rohan, note that `∀ ε, ε > 0` can be written `∀ ε > 0` like you would do on paper

#### [Patrick Massot (Sep 26 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668427):
Lean will parse that exactly as you originally wrote

#### [Rohan Mitta (Sep 26 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668976):
Thanks everyone!

#### [Kenny Lau (Sep 26 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134673009):
```quote
Lean will parse that exactly as you originally wrote
```
well not exactly...

