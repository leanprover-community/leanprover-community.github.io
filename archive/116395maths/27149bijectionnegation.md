---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/27149bijectionnegation.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [bijection negation](https://leanprover-community.github.io/archive/116395maths/27149bijectionnegation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (May 17 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126694854):
<p>Is there a property like <code>∀ ⦃a₁ a₂⦄, f a₁ ≠ f a₂ → a₁ ≠ a₂</code> for a <code>bijective f</code>?</p>

#### [ Chris Hughes (May 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126694907):
<p>It doesn't need to be bijective.</p>

#### [ Sean Leather (May 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695019):
<p>True. So, I have a function that already needs to be an injection. Would be it be preferable to use the above property directly, or, if it I make a bijection, can I derive that property?</p>

#### [ Sean Leather (May 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695026):
<p>Or perhaps something simpler.</p>

#### [ Mario Carneiro (May 17 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695084):
<p>That theorem is true for any function whatsoever. It is <code>mt (congr_arg f)</code></p>

#### [ Kevin Buzzard (May 17 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695085):
<p>This is just a rw.</p>

#### [ Sean Leather (May 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bijection%20negation/near/126695099):
<p>Ah, right. Silly me!</p>


{% endraw %}
