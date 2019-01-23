---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52204powpow.html
---

## Stream: [maths](index.html)
### Topic: [pow_pow](52204powpow.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667339):
I just spent 60 seconds looking for `pow_pow : (a ^ b) ^ c = a ^ (b * c)` for a tactic mode rewrite, before I realised that it was actually called `←pow_mul`. I'm always a little worried when I see those `←` signs, it feels like I'm not going in the recommended direction. Is there a case for `pow_pow`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667525):
it's not a simp lemma, so you can use it whichever way you want to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667561):
I agree that both directions have some claim to reasonableness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_pow/near/147667611):
So the left-arrow is fine?


{% endraw %}
