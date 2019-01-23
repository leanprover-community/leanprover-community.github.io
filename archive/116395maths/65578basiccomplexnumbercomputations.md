---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65578basiccomplexnumbercomputations.html
---

## Stream: [maths](index.html)
### Topic: [basic complex number computations](65578basiccomplexnumbercomputations.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129477726):
@**VeraZZ** is doing basic computations with complex numbers and I'm still not 100% sure that we're doing it right.

If the goal looks like this:

```
z₁ z₂ : ℂ
⊢ ↑(z₁.re * z₂.re + z₁.im * z₂.im) + ↑(z₁.re * z₂.re + z₁.im * z₂.im) =
    z₁ * conj z₂ + z₂ * conj z₁
```

then currently our strategy is the (probably rather inefficient)

```lean
   apply complex.ext,
   simp,ring,simp,ring,
```

After Chris' complex number PR I realised that I am not at all sure how I'm supposed to be working with complex numbers. The strategy above is to check that two complex numbers are equal it suffices to check their real and imag parts are equal, and then use a dangerous non-finishing `simp` to unravel all the real and imaginary stuff followed by `ring`. Are there better approaches?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478308):
I think a non-finishing `simp` is not dangerous here, since `ring` is not sensitive to the precise state of the goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 11 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478419):
you could also define a tactic doing `apply complex.ext ; {simp, ring}`, and you wouldn't see `simp` :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 11 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478472):
By the way, if `ext` cannot replace `apply complex.ext` then the extensionality attribute needs to be added somewhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 11 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478613):
and, as usual with non finishing simp, you can use `suffices : stuff := by simp,`, where stuff is what you currently see as after simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478748):
That sounds like a tactic I might be able to write.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 11 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478809):
sure: ``meta def cplx_ring : tactic unit := `[apply complex.ext ; {simp, ring}]``


{% endraw %}
