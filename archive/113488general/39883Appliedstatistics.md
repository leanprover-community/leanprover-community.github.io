---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39883Appliedstatistics.html
---

## Stream: [general](index.html)
### Topic: [Applied statistics](39883Appliedstatistics.html)

---


{% raw %}
#### [ Simon Hudon (Jul 06 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172046):
<p>I haven't done any statistics in a while. Can someone point me to a formula I can use to calculate the probability that <code>x ≤ y</code> if both are normally distributed random variables?</p>

#### [ Kenny Lau (Jul 06 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172106):
<p>mean and variance?</p>

#### [ Simon Hudon (Jul 06 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172114):
<p>Yes using the mean and variance.</p>

#### [ Simon Hudon (Jul 06 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172989):
<p>Do you have a formula for that?</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176063):
<p>This is like taking the 2D Gaussian and drawing a line across the distribution; if you project parallel to that line the projected distribution is another Gaussian so the answer should be Erf of some simple term involving the mean and variance</p>

#### [ Simon Hudon (Jul 06 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176241):
<p>I'm not knowledgeable enough to make sense of that answer</p>

#### [ Simon Hudon (Jul 06 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176391):
<p>Maybe it would be useful to reveal more context of my problem. I have two tactics. I'm running them each ~30 times, measuring average running time and variance. I'd like to check if one is actually faster than the other</p>

#### [ Simon Hudon (Jul 06 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176399):
<p>The difference is not big but I'd like to know where I'm heading with the optimization</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176445):
<p>If the variables are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>∼</mo><mi>N</mi><mo>(</mo><mi>a</mi><mo separator="true">,</mo><msub><mi>σ</mi><mi>X</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">X \sim N(a, \sigma_X)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">∼</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi><mo>∼</mo><mi>N</mi><mo>(</mo><mi>b</mi><mo separator="true">,</mo><msub><mi>σ</mi><mi>Y</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">Y \sim N(b, \sigma_Y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="mrel">∼</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mopen">(</span><span class="mord mathit">b</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span> then let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>=</mo><mi>a</mi><mo>+</mo><msub><mi>σ</mi><mi>X</mi></msub><msup><mi>X</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">X = a + \sigma_X X'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">=</span><span class="mord mathit">a</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi><mo>=</mo><mi>b</mi><mo>+</mo><msub><mi>σ</mi><mi>Y</mi></msub><msup><mi>Y</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">Y = b + \sigma_Y Y'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="mrel">=</span><span class="mord mathit">b</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>X</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">X'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>Y</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">Y'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> are standard normal variables; then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>+</mo><msub><mi>σ</mi><mi>X</mi></msub><msup><mi>X</mi><mo mathvariant="normal">′</mo></msup><mo>≤</mo><mi>b</mi><mo>+</mo><msub><mi>σ</mi><mi>Y</mi></msub><msup><mi>Y</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">a+\sigma_X X' \le b + \sigma_Y Y'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit">a</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">≤</span><span class="mord mathit">b</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> iff <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>σ</mi><mi>Y</mi></msub><msup><mi>Y</mi><mo mathvariant="normal">′</mo></msup><mo>−</mo><msub><mi>σ</mi><mi>X</mi></msub><msup><mi>X</mi><mo mathvariant="normal">′</mo></msup><mo>≥</mo><mi>a</mi><mo>−</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">\sigma_Y Y' - \sigma_X X' \ge a - b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">≥</span><span class="mord mathit">a</span><span class="mbin">−</span><span class="mord mathit">b</span></span></span></span>. But <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>σ</mi><mi>Y</mi></msub><msup><mi>Y</mi><mo mathvariant="normal">′</mo></msup><mo>−</mo><msub><mi>σ</mi><mi>X</mi></msub><msup><mi>X</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">\sigma_Y Y' - \sigma_X X'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is a Gaussian with SD <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msqrt><mrow><msubsup><mi>σ</mi><mi>X</mi><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>σ</mi><mi>Y</mi><mn>2</mn></msubsup></mrow></msqrt></mrow><annotation encoding="application/x-tex">\sqrt{\sigma^2_X + \sigma^2_Y}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9361885000000001em;"></span><span class="strut bottom" style="height:1.24em;vertical-align:-0.3038114999999999em;"></span><span class="base"><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:0.9361885000000001em;"><span style="top:-3.2em;"><span class="pstrut" style="height:3.2em;"></span><span class="mord" style="padding-left:1em;"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7959080000000001em;"><span style="top:-2.4064690000000004em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span><span style="top:-3.0448000000000004em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29353099999999993em;"></span></span></span></span></span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7959080000000001em;"><span style="top:-2.4064690000000004em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span><span style="top:-3.0448000000000004em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29353099999999993em;"></span></span></span></span></span></span></span><span style="top:-2.8961885em;"><span class="pstrut" style="height:3.2em;"></span><span style="height:1.2em;"><svg height="1.2em" width="100%"><br>
<svg preserveAspectRatio="xMinYMin slice" viewBox="0 0 400000 1200"><path d="M263 601c.667 0 18 39.667 52 119s68.167  158.667 102.5 238 51.833 119.333 52.5 120C810 373.333 980.667 17.667 982 11 c4.667-7.333 11-11 19-11h398999v40H1012.333L741 607c-38.667 80.667-84 175-136  283s-89.167 185.333-111.5 232-33.833 70.333-34.5 71c-4.667 4.667-12.333 7-23  7l-12-1-109-253c-72.667-168-109.333-252-110-252-10.667 8-22 16.667-34 26-22  17.333-33.333 26-34 26l-26-26 76-59 76-60zM1001 0h398999v40H1012z"></path></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3038114999999999em;"></span></span></span></span></span></span></span>, so the probability is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">f</mi></mrow><mfrac><mrow><mi>a</mi><mo>−</mo><mi>b</mi></mrow><mrow><msqrt><mrow><msubsup><mi>σ</mi><mi>X</mi><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>σ</mi><mi>Y</mi><mn>2</mn></msubsup></mrow></msqrt></mrow></mfrac></mrow><annotation encoding="application/x-tex">\mathrm{erf}\frac{a-b}{\sqrt{\sigma^2_X + \sigma^2_Y}}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8801079999999999em;"></span><span class="strut bottom" style="height:1.7301079999999998em;vertical-align:-0.8499999999999999em;"></span><span class="base"><span class="mord"><span class="mord mathrm">e</span><span class="mord mathrm">r</span><span class="mord mathrm" style="margin-right:0.07778em;">f</span></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8801079999999999em;"><span style="top:-2.4455250000000004em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord sqrt mtight"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:1.0635357142857143em;"><span style="top:-3.428571428571429em;"><span class="pstrut" style="height:3.428571428571429em;"></span><span class="mord mtight" style="padding-left:1.19em;"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8051142857142857em;"><span style="top:-2.160707142857143em;margin-left:-0.03588em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span><span style="top:-2.8448em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3392928571428572em;"></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8051142857142857em;"><span style="top:-2.160707142857143em;margin-left:-0.03588em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathit mtight" style="margin-right:0.22222em;">Y</span></span></span><span style="top:-2.8448em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3392928571428572em;"></span></span></span></span></span></span></span><span style="top:-3.006392857142857em;"><span class="pstrut" style="height:3.428571428571429em;"></span><span class="mtight" style="height:1.4285714285714286em;"><svg height="1.4285714285714286em" width="100%"><br>
<svg preserveAspectRatio="xMinYMin slice" viewBox="0 0 400000 1000"><path d="M95 622c-2.667 0-7.167-2.667-13.5 -8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s 65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173 378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333 -9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19 7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z"></path></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.4221785714285716em;"></span></span></span></span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">a</span><span class="mbin mtight">−</span><span class="mord mathit mtight">b</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.8499999999999999em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></p>

#### [ Mario Carneiro (Jul 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176560):
<p>At the first order the answer to your question is easy: If the mean is less then it's probably an improvement</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176562):
<p>but the larger the standard deviation the less confidence you have in this assertion</p>

#### [ Simon Hudon (Jul 06 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176570):
<p>Right. One of them has a pretty large standard deviation</p>

#### [ Simon Hudon (Jul 06 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176571):
<p>Is it weird that it only started making sense when you brought up the formula? :)</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176636):
<p>By the way there is a square root in the last two math blocks there, but in my mathjax display I only see a conspicuous space</p>

#### [ Simon Hudon (Jul 06 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176681):
<p>I see the same. You were missing a bracket and a $ so I ended up compiler your latex myself. I see both square roots</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176734):
<p>I think I've fixed all the delimiter problems above, but the square root still isn't rendering. You know how to fix it?</p>

#### [ Simon Hudon (Jul 06 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176781):
<p>You're right, it's now rendering almost properly. I haven't played with mathjax so I wouldn't know where to start</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176801):
<p>MSE uses mathjax and there isn't much trouble using <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msqrt><mi>x</mi></msqrt></mrow><annotation encoding="application/x-tex">\sqrt x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8002800000000001em;"></span><span class="strut bottom" style="height:1.04em;vertical-align:-0.23972em;"></span><span class="base"><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:0.8002800000000001em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="padding-left:0.833em;">x</span></span><span style="top:-2.76028em;"><span class="pstrut" style="height:3em;"></span><span style="height:1em;"><svg height="1em" width="100%"><br>
<svg preserveAspectRatio="xMinYMin slice" viewBox="0 0 400000 1000"><path d="M95 622c-2.667 0-7.167-2.667-13.5 -8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s 65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173 378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333 -9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19 7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z"></path></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.23972em;"></span></span></span></span></span></span></span> there</p>

#### [ Reid Barton (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176803):
<p>Zulip actually uses katex, not mathjax</p>

#### [ Simon Hudon (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176804):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span></p>

#### [ Mario Carneiro (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176844):
<p>you have to use double dollar delimiter</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176847):
<p>does \[\sqrt x\] work?</p>

#### [ Simon Hudon (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176848):
<p>Nice thanks!</p>

#### [ Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176855):
<p>\[ \sqrt x \]</p>

#### [ Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176856):
<p>No</p>

#### [ Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176857):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msqrt><mi>x</mi></msqrt></mrow><annotation encoding="application/x-tex">\sqrt x </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8002800000000001em;"></span><span class="strut bottom" style="height:1.04em;vertical-align:-0.23972em;"></span><span class="base"><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:0.8002800000000001em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="padding-left:0.833em;">x</span></span><span style="top:-2.76028em;"><span class="pstrut" style="height:3em;"></span><span style="height:1em;"><svg height="1em" width="100%"><br>
<svg preserveAspectRatio="xMinYMin slice" viewBox="0 0 400000 1000"><path d="M95 622c-2.667 0-7.167-2.667-13.5 -8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s 65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173 378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333 -9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19 7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z"></path></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.23972em;"></span></span></span></span></span></span></span></p>

#### [ Mario Carneiro (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176858):
<p>Not sure how to do display math either</p>

#### [ Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176862):
<p><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msqrt><mi>x</mi></msqrt></mrow><annotation encoding="application/x-tex">\sqrt  x</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:0.8491550000000001em;"></span><span class="strut bottom" style="height:1.04em;vertical-align:-0.190845em;"></span><span class="base"><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:0.8491550000000001em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="padding-left:0.833em;">x</span></span><span style="top:-2.809155em;"><span class="pstrut" style="height:3em;"></span><span style="height:1em;"><svg width='100%' height='1em'>
            <svg viewBox='0 0 400000 1000' preserveAspectRatio='xMinYMin
slice'><path d='M95 622c-2.667 0-7.167-2.667-13.5
-8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s
65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173
378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333
-9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19
7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z'/></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.190845em;"></span></span></span></span></span></span></span></span></p>

#### [ Mario Carneiro (Jul 06 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176863):
<p>oh, there it is</p>

#### [ Simon Hudon (Jul 06 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176915):
<p>If you do "three ticks" math (like you would for Lean code), then it seems to work</p>

#### [ Simon Hudon (Jul 06 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177084):
<p>If I try my tactic on three problems, I evaluate the formula you gave me for each problem, how do you recommend I aggregate the data (if I need to)?</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177639):
<p>To make it a bit easier, you can subtract the two times for each problem, resulting in a random variable that you want to compare to zero</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177647):
<p>then you take an average weighted by how many trials were performed in each problem</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177736):
<p>the standard deviation would be the sqrt-sum of the individual SDs, divided by 3 since there are three subproblems (assuming equal weights on the three problems)</p>

#### [ Simon Hudon (Jul 06 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177788):
<p>Does it matter than one of the problem is much harder than the others? It has a run time around 16s while the others are around 7s and 3s</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177798):
<p>Oh, I see, yes that changes things</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177858):
<p>I'm assuming in this analysis that we have two gaussian variables X and Y and want to estimate them</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177859):
<p>but this supposes that the mean and SD are fixed across the sample</p>

#### [ Simon Hudon (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177861):
<p>That sounds right</p>

#### [ Simon Hudon (Jul 06 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177865):
<p>I don't understand your last sentence. What's the opposite of fixed?</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177921):
<p>We can assume that problem 1 has a gaussian distrib of times for each tactic, but there is no reason to believe that this same gaussian describes the times for problem 2</p>

#### [ Simon Hudon (Jul 06 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177970):
<p>I think that's reasonable</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178035):
<p>So we have to make some assumption about what we are estimating. Let's say we have good data on each problem, so we can say things like problem 1 is 2s +- .1s for tac 1 and 4s +- 1s for tac 2, and similarly for problem 2. If the goal is to minimize total run time over all future uses of tac1 vs tac2, then we need to assume that problem 1 and problem 2 are somehow representative of those future uses</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178038):
<p>If we think problem 2 is more common than problem 1, then it will get a higher weight in the average</p>

#### [ Simon Hudon (Jul 06 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178079):
<p>The three problems are deriving transportable for monoids, groups and rings. Rings are very expensive</p>

#### [ Simon Hudon (Jul 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178085):
<p>We could believe that the complexity is linear in the number of fields of the structure</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178090):
<p>I think it is safe to say that each of those will be run only once, but perhaps you want to extrapolate to even larger examples, or smaller?</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178132):
<p>In other words you should estimate the common use case size</p>

#### [ Simon Hudon (Jul 06 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178183):
<p>Digression: should there be an absolute value in your formula? It's giving me negative numbers</p>

#### [ Simon Hudon (Jul 06 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178187):
<p>I think as you say there will be an average size for the problems where this is used</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178349):
<p>You mean the a-b/sqrt(sd) formula?</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178421):
<p>there should not be an absolute value, although I think I may have a sign error in there - one sign means tac1 is better, the other means tac2 is better</p>

#### [ Simon Hudon (Jul 06 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178474):
<p>Ah I see! The highest probability I get is 50%. I'll keep the optimization in but that doesn't seem conclusive</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178477):
<p>when you use erf it turns the number into a probability which is close to 100% for positive numbers and close to 0 for negative numbers</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178484):
<p>50% means you have a very small difference, of course</p>

#### [ Simon Hudon (Jul 06 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178486):
<p>Really? I don't get that. Maybe I should be suspicious of my erf implementation.</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178523):
<p>you can report the number without the erf, that gives the number of SDs away from the mean</p>

#### [ Mario Carneiro (Jul 06 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178532):
<p>wait, did you just push some haskell to mathlib?</p>

#### [ Simon Hudon (Jul 06 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178535):
<p>On my branch yes. I'll take it out before pushing for a merge</p>

#### [ Simon Hudon (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178711):
<p>I checked with another <code>erf</code> implementation, the results are consistent. I get the following numbers, one for each problem:</p>
<div class="codehilite"><pre><span></span>0.3548605107843447
0.392231363819503
0.5018422725422864
</pre></div>

#### [ Simon Hudon (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178714):
<p>Is the last one 50% or 0.50%?</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178716):
<p>I would assume 50%</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178755):
<p>erf returns numbers in the range 0-1</p>

#### [ Simon Hudon (Jul 06 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178759):
<p>Ok, I got confused when you said:</p>
<blockquote>
<p>when you use erf it turns the number into a probability which is close to 100% for positive numbers and close to 0 for negative numbers</p>
</blockquote>

#### [ Mario Carneiro (Jul 06 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178826):
<p>Oh, I just checked wikipedia and it looks like the normalization conventions are a bit different for erf</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178831):
<p>there is a factor sqrt 2 on the inputs, and it returns a value in the range -1 to 1</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178876):
<p>Maybe you should just leave the erf off and interpret the number of SDs away from the mean directly</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178888):
<p>what I really want there is the CDF of the standard normal distribution</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178899):
<p>which is basically erf but needs some preprocessing</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178978):
<p>wikipedia says the CDF is</p>
<p><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi><mi>D</mi><msub><mi>F</mi><mrow><mi>N</mi><mo>(</mo><mi>μ</mi><mo separator="true">,</mo><mi>σ</mi><mo>)</mo></mrow></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mo fence="true">[</mo><mn>1</mn><mo>+</mo><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">f</mi></mrow><mrow><mo fence="true">(</mo><mfrac><mrow><mi>x</mi><mo>−</mo><mi>μ</mi></mrow><mrow><mi>σ</mi><msqrt><mn>2</mn></msqrt></mrow></mfrac><mo fence="true">)</mo></mrow><mo fence="true">]</mo></mrow></mrow><annotation encoding="application/x-tex">CDF_{N(\mu,\sigma)}(x)=\frac{1}{2}\left[1+\mathrm{erf}\left(\frac{x-\mu}{\sigma\sqrt 2}\right)\right]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:1.45em;"></span><span class="strut bottom" style="height:2.40003em;vertical-align:-0.95003em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.34480000000000005em;"><span style="top:-2.5198em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.10903em;">N</span><span class="mopen mtight">(</span><span class="mord mathit mtight">μ</span><span class="mpunct mtight">,</span><span class="mord mathit mtight" style="margin-right:0.03588em;">σ</span><span class="mclose mtight">)</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3551999999999999em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.32144em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathrm">2</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathrm">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.686em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="minner"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size3">[</span></span><span class="mord mathrm">1</span><span class="mbin">+</span><span class="mord"><span class="mord mathrm">e</span><span class="mord mathrm">r</span><span class="mord mathrm" style="margin-right:0.07778em;">f</span></span><span class="minner"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size3">(</span></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.2603300000000002em;"><span style="top:-2.2027799999999997em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist svg-align" style="height:0.90722em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathrm" style="padding-left:0.833em;">2</span></span><span style="top:-2.86722em;"><span class="pstrut" style="height:3em;"></span><span style="height:1em;"><svg width='100%' height='1em'>
            <svg viewBox='0 0 400000 1000' preserveAspectRatio='xMinYMin
slice'><path d='M95 622c-2.667 0-7.167-2.667-13.5
-8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s
65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173
378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333
-9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19
7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z'/></svg></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.13278em;"></span></span></span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">x</span><span class="mbin">−</span><span class="mord mathit">μ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.93em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size3">)</span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size3">]</span></span></span></span></span></span></span></p>

#### [ Simon Hudon (Jul 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179041):
<p>The <code>erf</code> library in haskell has a function <code>normcdf</code> with <code>normcdf x = erfc(-x  sqrt 2) ^ 2</code> does that make sense?</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179053):
<p>based on the name that's likely to be the right one</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179062):
<p>try evaluating it at -1, 0, 1</p>

#### [ Simon Hudon (Jul 06 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179137):
<div class="codehilite"><pre><span></span>0.15865525393145705
0.5
0.8413447460685429
</pre></div>

#### [ Mario Carneiro (Jul 06 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179181):
<p>that's correct</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179192):
<p>use that in place of erf in the formula I gave before</p>

#### [ Simon Hudon (Jul 06 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179238):
<p>Thanks!</p>

#### [ Simon Hudon (Jul 06 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179256):
<p>That looks much better!</p>

#### [ Simon Hudon (Jul 06 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179263):
<div class="codehilite"><pre><span></span>0.6276517385920415
0.6416715838500027
0.6840264065071848
</pre></div>

#### [ Simon Hudon (Jul 06 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179303):
<p>And if I flip <code>a</code>and <code>b</code> in <code>a - b</code>, I get:</p>
<div class="codehilite"><pre><span></span>0.37234826140795846
0.3583284161499974
0.3159735934928151
</pre></div>

#### [ Simon Hudon (Jul 06 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179313):
<p>If we use <code>b - a</code>, that's the probability that <code>b ≥ a</code>, is correct?</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179356):
<p>yes</p>

#### [ Simon Hudon (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179359):
<p>Cool</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179362):
<p>The interpretation is something like "given the data you gathered, there is a 62% chance that in fact tac 1 is better than tac 2 on problem 1"</p>

#### [ Simon Hudon (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179367):
<p>Btw, <code>unfold_projs</code> yielded a big improvement in the end: Lean stopped crashing</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179372):
<p>ooh, what caused the crash?</p>

#### [ Simon Hudon (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179378):
<p>Timeout</p>

#### [ Simon Hudon (Jul 06 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179427):
<p>I suspect that definitions generated by a tactic don't play nicely with <code>simp</code> / <code>dsimp</code> / <code>unfold</code> / <code>dunfold</code> if you try to unfold them</p>

#### [ Mario Carneiro (Jul 06 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179477):
<p>you can write your own simp lemmas for them if you want</p>

#### [ Simon Hudon (Jul 06 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179494):
<p>Yes, I tried that. It did help a bit</p>

#### [ Simon Hudon (Jul 06 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179539):
<p>But not as much as <code>unfold_projs</code>. It removed the need to hard code <code>has_mul.mul</code> et cie</p>

#### [ Simon Hudon (Jul 06 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179778):
<p>I don't know about you but I'm having so much fun with that stuff (Lean) lately :D</p>

#### [ Kenny Lau (Jul 06 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129185447):
<blockquote>
<p>I haven't done any statistics in a while. Can someone point me to a formula I can use to calculate the probability that <code>x ≤ y</code> if both are normally distributed random variables?</p>
</blockquote>
<p>oh of course it's 50%, it's symmetric</p>

#### [ Kevin Buzzard (Jul 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129186725):
<blockquote>
<p>oh of course it's 50%, it's symmetric</p>
</blockquote>
<p>I think the means are different</p>


{% endraw %}
