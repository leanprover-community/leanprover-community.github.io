---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65578basiccomplexnumbercomputations.html
---

## Stream: [maths](index.html)
### Topic: [basic complex number computations](65578basiccomplexnumbercomputations.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 11 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129477726):
<p><span class="user-mention" data-user-id="120352">@VeraZZ</span> is doing basic computations with complex numbers and I'm still not 100% sure that we're doing it right.</p>
<p>If the goal looks like this:</p>
<div class="codehilite"><pre><span></span>z₁ z₂ : ℂ
⊢ ↑(z₁.re * z₂.re + z₁.im * z₂.im) + ↑(z₁.re * z₂.re + z₁.im * z₂.im) =
    z₁ * conj z₂ + z₂ * conj z₁
</pre></div>


<p>then currently our strategy is the (probably rather inefficient)</p>
<div class="codehilite"><pre><span></span>   <span class="n">apply</span> <span class="n">complex</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
   <span class="n">simp</span><span class="o">,</span><span class="n">ring</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span><span class="n">ring</span><span class="o">,</span>
</pre></div>


<p>After Chris' complex number PR I realised that I am not at all sure how I'm supposed to be working with complex numbers. The strategy above is to check that two complex numbers are equal it suffices to check their real and imag parts are equal, and then use a dangerous non-finishing <code>simp</code> to unravel all the real and imaginary stuff followed by <code>ring</code>. Are there better approaches?</p>

#### [ Chris Hughes (Jul 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478308):
<p>I think a non-finishing <code>simp</code> is not dangerous here, since <code>ring</code> is not sensitive to the precise state of the goal.</p>

#### [ Patrick Massot (Jul 11 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478419):
<p>you could also define a tactic doing <code>apply complex.ext ; {simp, ring}</code>, and you wouldn't see <code>simp</code> <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Jul 11 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478472):
<p>By the way, if <code>ext</code> cannot replace <code>apply complex.ext</code> then the extensionality attribute needs to be added somewhere</p>

#### [ Patrick Massot (Jul 11 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478613):
<p>and, as usual with non finishing simp, you can use <code>suffices : stuff := by simp,</code>, where stuff is what you currently see as after simp</p>

#### [ Chris Hughes (Jul 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478748):
<p>That sounds like a tactic I might be able to write.</p>

#### [ Patrick Massot (Jul 11 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/basic%20complex%20number%20computations/near/129478809):
<p>sure: <code>meta def cplx_ring : tactic unit := `[apply complex.ext ; {simp, ring}]</code></p>


{% endraw %}
