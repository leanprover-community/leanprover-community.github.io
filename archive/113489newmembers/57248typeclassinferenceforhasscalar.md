---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/57248typeclassinferenceforhasscalar.html
---

## Stream: [new members](index.html)
### Topic: [type class inference for has_scalar](57248typeclassinferenceforhasscalar.html)

---

#### [Jan-David Salchow (Nov 05 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20class%20inference%20for%20has_scalar/near/146801378):
The type class mechanism doesn't seem be able to figure out that functions to a normed space can be multiplied by scalars. Does anybody know why?

```
import analysis.normed_space algebra.pi_instances

-- works
example {α E : Type*} [vector_space ℝ E] (c : ℝ) (f : α → E) : ∀ x : α, (c • f) x  = c • (f x) := by simp

-- works
example {α E : Type*} [normed_space ℝ E] (c : ℝ) (f : α → E) :
  ∀ x : α, (@has_scalar.smul _ _ (@pi.has_scalar _ _ _ _) c f) x  =  c • (f x) :=
by simp 

-- doesn't work
example {α E : Type*} [normed_space ℝ E] (c : ℝ) (f : α → E) : ∀ x : α, (c • f) x  = c • (f x) := by simp
```

#### [Mario Carneiro (Nov 05 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20class%20inference%20for%20has_scalar/near/146801595):
what is `c • f`?

#### [Mario Carneiro (Nov 05 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20class%20inference%20for%20has_scalar/near/146801642):
oh I see it's the pi instance

