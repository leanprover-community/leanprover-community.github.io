---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/968692variablesfunctions.html
---

## Stream: [maths](index.html)
### Topic: [2 variables functions](968692variablesfunctions.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 15 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852102):
Is it evil to do something like:
```lean
def function.comp₂ (f : α → β → γ) (g : γ → δ) : α → β → δ := λ  x y, g (f x y)

notation g `∘₂` f := function.comp₂ f g

def uniform_continuous₂ (f : α → β → γ) := uniform_continuous (function.uncurry f)

lemma uniform_continuous₂.comp {f : α → β → γ} {g : γ → δ}
  (hf : uniform_continuous₂ f) (hg : uniform_continuous g) :
uniform_continuous₂ (g ∘₂ f)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 15 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852103):
etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 15 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852144):
It seems to be very convenient, but I fear there may be a reason why such a thing is not already used in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854577):
you will notice that even regular `∘` is rarely used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854580):
because it doesn't unfold as eagerly as one would like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854627):
it's not particularly evil to make the definition (although you could use the crazy version `(∘) ∘ (∘)`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151874113):
Cue link to my blog post

