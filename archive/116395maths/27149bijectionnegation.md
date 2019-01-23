---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/27149bijectionnegation.html
---

## Stream: [maths](index.html)
### Topic: [bijection negation](27149bijectionnegation.html)

---


{% raw %}
#### [ Sean Leather (May 17 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126694854):
Is there a property like `∀ ⦃a₁ a₂⦄, f a₁ ≠ f a₂ → a₁ ≠ a₂` for a `bijective f`?

#### [ Chris Hughes (May 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126694907):
It doesn't need to be bijective.

#### [ Sean Leather (May 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695019):
True. So, I have a function that already needs to be an injection. Would be it be preferable to use the above property directly, or, if it I make a bijection, can I derive that property?

#### [ Sean Leather (May 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695026):
Or perhaps something simpler.

#### [ Mario Carneiro (May 17 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695084):
That theorem is true for any function whatsoever. It is `mt (congr_arg f)`

#### [ Kevin Buzzard (May 17 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695085):
This is just a rw.

#### [ Sean Leather (May 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695099):
Ah, right. Silly me!


{% endraw %}
