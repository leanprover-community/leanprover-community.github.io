---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52204powpow.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [pow_pow](https://leanprover-community.github.io/archive/116395maths/52204powpow.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667339):
<p>I just spent 60 seconds looking for <code>pow_pow : (a ^ b) ^ c = a ^ (b * c)</code> for a tactic mode rewrite, before I realised that it was actually called <code>←pow_mul</code>. I'm always a little worried when I see those <code>←</code> signs, it feels like I'm not going in the recommended direction. Is there a case for <code>pow_pow</code>?</p>

#### [ Mario Carneiro (Nov 14 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667525):
<p>it's not a simp lemma, so you can use it whichever way you want to</p>

#### [ Mario Carneiro (Nov 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667561):
<p>I agree that both directions have some claim to reasonableness</p>

#### [ Kevin Buzzard (Nov 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667611):
<p>So the left-arrow is fine?</p>


{% endraw %}
