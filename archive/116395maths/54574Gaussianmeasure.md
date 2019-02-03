---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54574Gaussianmeasure.html
---

## Stream: [maths](index.html)
### Topic: [Gaussian measure](54574Gaussianmeasure.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 02 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135049503):
<p>Today the subject of formalising Gaussian measure in Lean came up at work. I asked Johannes about it privately and he seemed optimistic that it was within reach. But then he mentioned some work done at Dagstuhl on the Lebesgue integral which is...possibly not accessible at this point? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you have access to this stuff and is it in any state to be made public? As Patrick has pointed out in the past, our analysis is weak in places, and this probably simply because us number theorists / geometers are working on our pet projects where a bunch of foundational stuff has been done already, whereas any potential analysts will soon discover that there are still gaps in the coverage of 1st year undergraduate analysis (did anyone do the product rule yet??).</p>

#### [ Kevin Buzzard (Oct 02 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135049832):
<p>I guess we'll also need <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>π</mi></mrow><annotation encoding="application/x-tex">\pi</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">π</span></span></span></span> :-) Did it make it into mathlib yet? I glanced through recent commits and PRs and couldn't spot it.</p>

#### [ Reid Barton (Oct 02 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050032):
<p>You mean the product rule for the formal derivative of polynomials?</p>

#### [ Kevin Buzzard (Oct 02 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050222):
<p>heh, no, for differentiable functions <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow><mo>→</mo><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}\to\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span><span class="mrel">→</span><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> :-)</p>

#### [ Johan Commelin (Oct 02 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050692):
<p>We don't have derivatives yet, do we?</p>

#### [ Chris Hughes (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050771):
<p>No. There is something called <code>polynomial.derivative</code> or something, just for polynomials without mentioning analysis.</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135051272):
<p>Here's the integration file, which I've pushed to community mathlib: <a href="https://github.com/leanprover-community/mathlib/commit/10e3f42dc73fa9148e0f1847f6201bc608aa2488" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/10e3f42dc73fa9148e0f1847f6201bc608aa2488">https://github.com/leanprover-community/mathlib/commit/10e3f42dc73fa9148e0f1847f6201bc608aa2488</a></p>

#### [ Patrick Massot (Oct 02 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135055356):
<p>It looks like a good start. Let's hope algebra will soon leave you some time for working on this</p>


{% endraw %}
