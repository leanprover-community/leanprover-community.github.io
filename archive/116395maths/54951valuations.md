---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54951valuations.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [valuations](https://leanprover-community.github.io/archive/116395maths/54951valuations.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 26 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105553):
<p>Both the Fibonacci Squares project and the Adic Space project need valuations on rings -- one in rather more generality than the other. But let's start at the beginning. Does Lean have p-adic valuations on Z? In other words, is the function <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mo>⋅</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">v_p(\cdot)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord">⋅</span><span class="mclose">)</span></span></span></span> on the non-zero integers (or even rationals) sending <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>p</mi><mi>n</mi></msup><mi>N</mi></mrow><annotation encoding="application/x-tex">p^nN</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> (with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> coprime to the prime <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span>) to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>? The key theorems are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>a</mi><mi>b</mi><mo>)</mo><mo>=</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>a</mi><mo>)</mo><mo>+</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>b</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">v_p(ab)=v_p(a)+v_p(b)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mord mathit">b</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">b</span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo><mo>≥</mo><mi>min</mi><mo>{</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>a</mi><mo>)</mo><mo separator="true">,</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>b</mi><mo>)</mo><mo>}</mo></mrow><annotation encoding="application/x-tex">v_p(a+b)\geq\min\{v_p(a),v_p(b)\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mbin">+</span><span class="mord mathit">b</span><span class="mclose">)</span><span class="mrel">≥</span><span class="mop">min</span><span class="mopen">{</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">b</span><span class="mclose">)</span><span class="mclose">}</span></span></span></span> (where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mn>0</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">v_p(0)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathrm">0</span><span class="mclose">)</span></span></span></span> is usually taken to be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>+</mo><mi mathvariant="normal">∞</mi></mrow><annotation encoding="application/x-tex">+\infty</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord">+</span><span class="mord mathrm">∞</span></span></span></span>).</p>

#### [ Kevin Buzzard (May 26 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105607):
<p>Perfectoid space valuations would take values in a certain kind of totally ordered monoid</p>

#### [ Kevin Buzzard (May 26 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105620):
<p>(and are of a slightly different nature -- they are really norms not valuations, so the total function <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi><mo>↦</mo><msup><mi>p</mi><mrow><mo>−</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>M</mi><mo>)</mo></mrow></msup></mrow><annotation encoding="application/x-tex">M \mapsto p^{-v_p(M)}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.0824399999999998em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mrel">↦</span><span class="mord"><span class="mord mathit">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.16454285714285716em;"><span style="top:-2.357em;margin-left:-0.03588em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2818857142857143em;"></span></span></span></span></span><span class="mopen mtight">(</span><span class="mord mathit mtight" style="margin-right:0.10903em;">M</span><span class="mclose mtight">)</span></span></span></span></span></span></span></span></span></span></span></span> with target the non-negative reals would be an example).</p>

#### [ Reid Barton (May 26 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106671):
<p>I have approximately this lying around somewhere</p>

#### [ Reid Barton (May 26 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106845):
<p><a href="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea" target="_blank" title="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea">https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea</a></p>

#### [ Reid Barton (May 26 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106894):
<p>I guess <code>ord_add</code> is missing, but it should be easy to prove from the other stuff</p>

#### [ Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107157):
<p>line 91 should now be</p>

#### [ Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107159):
<p><code>         ...   = p * (p^r * k)   : by unfold pow nat.pow; ac_refl,</code></p>

#### [ Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107162):
<p>[adding pow, probably because of some relatively recent change with <code>^</code>]</p>

#### [ Kevin Buzzard (May 26 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107276):
<p>Thanks so much! This is exactly what I wanted!</p>

#### [ Kevin Buzzard (May 26 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107285):
<p>What a great little community we are getting here!</p>

#### [ Kevin Buzzard (May 26 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107301):
<p>I'm just going to dump it in a subdirectory in my project called <code>Reid_Barton</code>. Is that OK?</p>

#### [ Kevin Buzzard (May 26 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107340):
<p>Is there a better way of doing things?</p>

#### [ Reid Barton (May 26 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107625):
<p>Sure, no problem.<br>
The better way is probably to try to PR things into mathlib, but that's more effort.</p>

#### [ Kevin Buzzard (May 26 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107925):
<p><code>example : has_le (ℕ+) := by apply_instance -- fails</code></p>

#### [ Kevin Buzzard (May 26 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107937):
<p>Noticed this along the way. You've not proved the valuation of a + b but you've proved everything but. I've never worked with <code>\N+</code> before.</p>

#### [ Kevin Buzzard (May 26 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107991):
<p>Is there a good reason for not having le on <code>\N+</code>? I am making a little collection of random short mathlib proposals. I understand how mathlib works much better after my schemes exercise.</p>

#### [ Reid Barton (May 26 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108119):
<p>I doubt there is any good reason. <code>pnat</code> isn't used that much, it seems. I remember finding it a little more annoying to use than I would have liked</p>

#### [ Reid Barton (May 26 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108122):
<p>Particularly as there are coercions in both directions between <code>nat</code> and <code>pnat</code></p>

#### [ Kevin Buzzard (May 26 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108166):
<p>Is <code>ord_pow</code> broken?</p>

#### [ Kevin Buzzard (May 26 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108167):
<p>Or did I break it myself?</p>

#### [ Reid Barton (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108177):
<p>It's quite possibly broken because it is about 2.5 months old</p>

#### [ Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108178):
<p>do computer scientists really need a _coercion_ from <code>nat</code> to <code>pnat</code>?</p>

#### [ Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108180):
<p>I just can't even guess what it would be</p>

#### [ Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108183):
<p>"any one of a couple of random examples"</p>

#### [ Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108278):
<p><code>lemma ord_pow {k : ℕ} {a : ℕ+} : ord p (a^k) = k * ord p a := ord_ppow</code></p>

#### [ Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108279):
<p>:-)</p>

#### [ Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108281):
<p>I think some coercion magic happened?</p>

#### [ Kevin Buzzard (May 26 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109528):
<p>Is there a type Nat union {infinity}? I mean, it's option Nat but I want the obvious le, add and min functions (and don't want to write them if they're already there). The reason I ask is to extend p-adic valuation to zero, and I think I do have to add infinity, because the standard CS answer of just defining it to be 37 or whatever and ploughing on regardless doesn't seem to work here, because then things like min are wrong.</p>

#### [ Kenny Lau (May 26 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109552):
<p>it's called the ordinal omega+1 :D</p>

#### [ Kevin Buzzard (May 26 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109604):
<p>:D</p>

#### [ Kevin Buzzard (May 26 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109613):
<p>Things which I want to be there, are more and more often beginning to be there :D</p>

#### [ Kevin Buzzard (May 26 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109668):
<p>Anyone fancy univariate polynomials over a field (division algorithm, degree function with the usual problems at 0, gcd, unique factorization?)</p>

#### [ Kevin Buzzard (May 26 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109673):
<p>I'm seeing that pop up more and more. Lean has multivariate polynomials but I think these deserve to be a special class rather than constantly carrying around the type "unit" for your list of variables.</p>

#### [ Kevin Buzzard (May 26 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109730):
<p><span class="user-mention" data-user-id="111651">@Nicholas Scheel</span> do you want to try this? I'm going to show your work on Z[alpha] to the British Maths Olympiad squad tomorrow! See what they make of it.</p>

#### [ Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109786):
<p>Some stuff is there by a student of Johannes in his mason-stother directory but I don't think it's all there. And didn't someone do some Euclidean Algorithm stuff recently? Some student of Scott maybe? That might help I guess.</p>

#### [ Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109793):
<p>We need univariate polynomials for the Fibonacci project, as you know.</p>

#### [ Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109800):
<p>Or maybe Kenny or Chris will do it now their exams are over.</p>

#### [ Kevin Buzzard (May 26 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109843):
<p>A fair amount of this stuff should be tidied up and put in mathlib, so it's all in one place.</p>

#### [ Andrew Ashworth (May 26 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109967):
<p>hah, won't you soon have your own army of undergraduates working for you over the summer?</p>

#### [ Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109993):
<p>Over 20 undergrads now</p>

#### [ Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109997):
<p>They start 2nd July</p>

#### [ Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109998):
<p>It's going to be a crazy summer!</p>

#### [ Kevin Buzzard (May 26 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110000):
<p>2 months!</p>

#### [ Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110674):
<p>I am so rubbish at coe</p>

#### [ Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110679):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">pgcd_coe_something</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">pgcd</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">gcd</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">unfold</span> <span class="n">pgcd</span><span class="o">,</span>
<span class="c1">--rw pnat.coe_nat_coe a, -- I am so rubbish at coe</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110681):
<p>This is Reid's pgcd from his gist from earlier</p>

#### [ Kevin Buzzard (May 26 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111216):
<blockquote>
<p><a href="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea" target="_blank" title="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea">https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea</a></p>
</blockquote>

#### [ Mario Carneiro (May 26 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111362):
<blockquote>
<p>Is there a type Nat union {infinity}?</p>
</blockquote>
<p>As of this morning, there is a <code>with_top A</code> structure that adds an infinity element to any order. So <code>with_top nat</code> is just what you want.</p>

#### [ Kenny Lau (May 26 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111551):
<p>wow what a coincidence lol</p>

#### [ Mario Carneiro (May 26 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111894):
<blockquote>
<p>do computer scientists really need a _coercion_ from nat to pnat?</p>
</blockquote>
<p>Hm, my original concern was that if you wanted to write 5 as a pnat you would need to write &lt;5, dec_trivial&gt; which is obviously cumbersome. But actually since pnat has <code>has_one</code> and <code>has_add</code> that's actually enough for <code>bit0</code> and <code>bit1</code> to work, meaning that <code>(5 : pnat)</code> works fine (being defined as <code>bit1 (bit0 1)</code> where the 1 and addition are interpreted in <code>pnat</code>). So maybe this isn't needed. I'll see what breaks if I remove it, I agree it's not great to have a non-identity looking coercion</p>

#### [ Mario Carneiro (May 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111903):
<p>I was thinking of using <code>pnat</code> for the domain of <code>Z/nZ</code> btw, which will give it a better algebraic theory than <code>fin n</code></p>

#### [ Kevin Buzzard (May 26 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112038):
<blockquote>
<blockquote>
<p>Is there a type Nat union {infinity}?</p>
</blockquote>
<p>As of this morning, there is a <code>with_top A</code> structure that adds an infinity element to any order. So <code>with_top nat</code> is just what you want.</p>
</blockquote>
<p>Mario -- did you see Remark 1.5 of <a href="http://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf" target="_blank" title="http://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf">www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf</a> (page 4)? There is a fundamental construction in adic spaces -- adding a "bottom" element zero to a a totally ordered group (e.g the group of positive reals) and creating a totally ordered monoid. Is this sort of thing easy to do now?</p>

#### [ Nicholas Scheel (May 26 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112046):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I could spend an hour or two on it ... should I use multivariate polynomials, should I use finsupp, or just do a direct list encoding?</p>

#### [ Mario Carneiro (May 26 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112134):
<p>Actually your comment got me thinking about this. There is a related construction, let's say <code>with_zero A</code>, which adds a unit to any additive semigroup; and if the zero and bottom coincide then you get a composite structure which works well on some kinds of ordered groups, I would imagine. Similarly you can make sense of addition with infinity, and that structure coheres with the order of <code>with_top</code>, so that you can add an infinity element to an ordered additive semigroup.</p>

#### [ Mario Carneiro (May 26 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112177):
<p>This could be used to factor <code>ennreal</code> into <code>with_top nnreal</code></p>

#### [ Kenny Lau (May 26 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112184):
<p>rip ennreal 2017-2018</p>

#### [ Kenny Lau (May 26 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112217):
<p>born <a href="https://github.com/leanprover/mathlib/commit/51042cde36e3ff513866c7ee6a1909650ba7396e#diff-47b6fc31ab3cbab9a5353881776d1008" target="_blank" title="https://github.com/leanprover/mathlib/commit/51042cde36e3ff513866c7ee6a1909650ba7396e#diff-47b6fc31ab3cbab9a5353881776d1008">Aug 30, 2017</a></p>

#### [ Mario Carneiro (May 26 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112226):
<p>It probably wouldn't go away as a definition, it has enough properties on its own that make it worthy of study, but it would simplify and generalize some theorems</p>

#### [ Mario Carneiro (May 26 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112232):
<p>But to answer your question, currently <code>with_bot</code> and <code>with_top</code> only deal with the order structure, they don't have any monoid stuff</p>

#### [ Kevin Buzzard (May 27 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163781):
<blockquote>
<blockquote>
<p>do computer scientists really need a _coercion_ from nat to pnat?</p>
</blockquote>
<p>Hm, my original concern was that if you wanted to write 5 as a pnat you would need to write &lt;5, dec_trivial&gt; which is obviously cumbersome. But actually since pnat has <code>has_one</code> and <code>has_add</code> that's actually enough for <code>bit0</code> and <code>bit1</code> to work, meaning that <code>(5 : pnat)</code> works fine (being defined as <code>bit1 (bit0 1)</code> where the 1 and addition are interpreted in <code>pnat</code>). So maybe this isn't needed. I'll see what breaks if I remove it, I agree it's not great to have a non-identity looking coercion</p>
</blockquote>
<p>Is it possible to keep the coercion but demand that the type class resolution system produces a proof of positivity before it is applied? I think that this would very much mirror the way a mathematician thought about the issue.</p>

#### [ Kevin Buzzard (May 27 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163783):
<p>You might find that if proofs of positivity are carried around</p>

#### [ Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163787):
<p>with instances like "a &gt; 0 and b &gt; 0 implies a + b &gt; 0"</p>

#### [ Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163792):
<p>then the coercions work fine.</p>

#### [ Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163793):
<p>With the current system you just occasionally see these \u \u x things</p>

#### [ Kevin Buzzard (May 27 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163833):
<p>and it's only at the point where you go to cancel them and they won't cancel that you realise you've made a mathematical slip</p>

#### [ Kevin Buzzard (May 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163838):
<p>Can we make the coercion part of type class resolution better?</p>

#### [ Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164025):
<p>this isn't how coercions work</p>

#### [ Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164032):
<p>they are functions <code>A -&gt; B</code>, nothing else is allowed in there</p>

#### [ Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164033):
<p>in particular, coercions cannot be partial</p>

#### [ Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164037):
<p>except the coercion <code>Prop -&gt; bool</code> which is magical</p>

#### [ Kevin Buzzard (May 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164524):
<p>CS 101 question alert :-/</p>

#### [ Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164526):
<p>What's the theorem <code>\&lt;a,h\&gt;.val = a</code> called for subtypes?</p>

#### [ Mario Carneiro (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164565):
<p>rfl</p>

#### [ Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164567):
<p>I was trying not to use rfl</p>

#### [ Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164570):
<p>I was looking at the proof that \u \u a =a</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164578):
<p>I just figured that I had a bunch of stuff about coercions that I needed to understand better before I said too much more about this</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164581):
<p>and then I ended up going down a rabbit hole watching the type class resolution system unfold :-/</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164582):
<p>Actually I don't understand.</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164583):
<p>How do I rewrite \u \u a as a?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164586):
<p>Wait</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164589):
<p>I was asking for the name of the theorem</p>

#### [ Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164590):
<p>not the proof</p>

#### [ Mario Carneiro (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164634):
<p>you haven't given me enough info to answer the question</p>

#### [ Kevin Buzzard (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164638):
<p>I'll formulate something precise.</p>

#### [ Mario Carneiro (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164639):
<p>lots of theorems look like \u \u a = a</p>

#### [ Mario Carneiro (May 27 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164641):
<p>I need to know what is the type of a, and the type of \u a</p>

#### [ Kevin Buzzard (May 27 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164650):
<p>[pause whilst we discover if Kevin is talking nonsense]</p>

#### [ Kevin Buzzard (May 27 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164817):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">what_am_i_called</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">a</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (May 27 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164818):
<p>The question.</p>

#### [ Kevin Buzzard (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164862):
<p>because I want to use you in a rewrite</p>

#### [ Kevin Buzzard (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164864):
<p>so I need to know your name</p>

#### [ Mario Carneiro (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164867):
<p>the theorem doesn't have a name, it is done automatically by dsimp</p>

#### [ Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164876):
<p>And there's you guys saying our naming conventions are bad</p>

#### [ Mario Carneiro (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164877):
<p>same as how beta reduction isn't a named theorem</p>

#### [ Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164879):
<p>dsimp is what?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164881):
<p>I used it a couple of times recently</p>

#### [ Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164882):
<p>Kenny told me "just use dsimp" and I'm like "ooh my goal has gone from 1 page to 5 lines"</p>

#### [ Mario Carneiro (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164920):
<p>it's <code>simp</code> for definitional rewrites</p>

#### [ Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164924):
<p>which way does it go?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164925):
<p>What does it actually do?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164927):
<p>If it sees my subtype.mk.val stuff it just says "ooh I'll remove that"</p>

#### [ Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164929):
<p>but does it ever add it?</p>

#### [ Mario Carneiro (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164932):
<p>it does exactly the same sort of thing as simp</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164937):
<p>oh great :-)</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164940):
<p>Another black box :-)</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164944):
<p>I see</p>

#### [ Mario Carneiro (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164945):
<p>it cancels projections applied to structure mk</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164947):
<p>What else does it do?</p>

#### [ Mario Carneiro (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164948):
<p>this is the structure iota rule</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164951):
<p>What's a complete list of what it does?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164952):
<p>Would I be able to understand the source code?</p>

#### [ Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164955):
<p>Kenny says that Lean does not do magic but this is still magic to me</p>

#### [ Mario Carneiro (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164995):
<p>dsimp has a config too</p>

#### [ Kevin Buzzard (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164997):
<p>53 extra options?</p>

#### [ Mario Carneiro (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165001):
<p>that has a fairly complete list of the kinds of automatic reductions it does, beta, eta, zeta, iota etc</p>

#### [ Mario Carneiro (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165007):
<p>and it also uses <code>@[simp]</code> lemmas that are also rfl lemmas</p>

#### [ Mario Carneiro (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165013):
<p>as well as definition unfolding when you give it to the bracket list or use <code>!</code></p>

#### [ Kevin Buzzard (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165014):
<p>I would be really interested in watching a video or seeing an article about what dsimp and/or simp do. If I understood what they were doing I wouldn't still just be hopefully typing simp every now and then just to see if I can make the goal go away</p>

#### [ Mario Carneiro (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165046):
<p>Haven't we had this conversation before?</p>

#### [ Mario Carneiro (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165057):
<p>I'm pretty sure you wrote that article</p>

#### [ Kevin Buzzard (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165060):
<p>I feel like there's still a whole bunch of things I don't fully understand with all this business</p>

#### [ Kevin Buzzard (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165061):
<p>I'll read my own docs and see if this enlightens me</p>

#### [ Andrew Ashworth (May 27 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165117):
<p>The textbook "term rewriting and all that" is pretty good on this subject, if your uni library has it</p>

#### [ Nicholas Scheel (May 27 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165171):
<p>simplification using definition equalities, I believe</p>

#### [ Kevin Buzzard (May 27 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165225):
<p>So my real question was "how do I do a definitional rewrite in tactic mode", and the answer is "don't use rw, use show"</p>

#### [ Mario Carneiro (May 27 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165231):
<p><code>change with</code> is literally definitional rw</p>

#### [ Kevin Buzzard (May 27 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165232):
<blockquote>
<p>The textbook "term rewriting and all that" is pretty good on this subject, if your uni library has it</p>
</blockquote>
<p>Thanks Andrew. My university can get any book for me.</p>

#### [ Mario Carneiro (May 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165274):
<p>but <code>dsimp</code> is nice for just cleaning up some common patterns</p>

#### [ Kevin Buzzard (May 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165275):
<p>Equality is asymmetric for you people, isn't it</p>

#### [ Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165278):
<p>This is only just dawning on me</p>

#### [ Mario Carneiro (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165281):
<p>yes, with term rewrites direction really matters</p>

#### [ Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165282):
<p>If you write a = b, and if one side was more complicated than the other</p>

#### [ Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165283):
<p>you would put the more complicated side first</p>

#### [ Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165284):
<p>Is this just some general principle?</p>

#### [ Mario Carneiro (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165287):
<p>yeah, simp simplifies</p>

#### [ Mario Carneiro (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165288):
<p>it's not called complexify</p>

#### [ Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165330):
<p>I had not realised that = was asymmetric</p>

#### [ Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165331):
<p>in any way whatsoever</p>

#### [ Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165332):
<p>I have a different definition of = to you</p>

#### [ Mario Carneiro (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165333):
<p>= itself is symmetric</p>

#### [ Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165334):
<p>symmetric in some theorem sense</p>

#### [ Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165336):
<p>but you have to decide which goes first</p>

#### [ Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165340):
<p>and we don't care</p>

#### [ Mario Carneiro (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165343):
<p>but simp and dsimp takes the list of simp lemmas and use them as a rewrite graph</p>

#### [ Mario Carneiro (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165344):
<p>and this is directed</p>

#### [ Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165345):
<p>Right, I've just been learning this from my own notes</p>

#### [ Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165347):
<p>Aah!</p>

#### [ Kevin Buzzard (May 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165349):
<p>I've just realised what my question actually is.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165394):
<p>My question is this: "I never ever tag anything with @[simp]. I make loads of structures. Can you give me some basic advice over which trivial lemmas I should be (a) proving and (b) tagging with simp?"</p>

#### [ Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165403):
<p>Unfortunately, the answer is "depends on the structure"</p>

#### [ Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165406):
<p>some axioms of a structure should be simp lemmas</p>

#### [ Kevin Buzzard (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165407):
<p>subtype</p>

#### [ Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165408):
<p>like <code>zero_add</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165409):
<p>A type and a proof</p>

#### [ Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165449):
<p>I don't think subtype has any simp lemmas</p>

#### [ Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165451):
<p>which is to say, there is nothing that sticks out as necessary</p>

#### [ Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165453):
<p>oh, &lt;a, h1&gt; = &lt;b, h2&gt; &lt;-&gt; a = b should be a simp lemma</p>

#### [ Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165455):
<p>What about presheaf of types on a topological space?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165459):
<p>I made that structure once</p>

#### [ Mario Carneiro (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165461):
<p>but actually I think simp might do that automatically anyway</p>

#### [ Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165462):
<p>I'll find you a link</p>

#### [ Mario Carneiro (May 27 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165499):
<p>simp will already do a few things by default on all structures, which more or less covers all the general recommendations</p>

#### [ Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165503):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/6617de7dd5f11af46f0c7e0d2223ee065d71b9f3/src/tag006E.lean#L4" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/6617de7dd5f11af46f0c7e0d2223ee065d71b9f3/src/tag006E.lean#L4">https://github.com/kbuzzard/lean-stacks-project/blob/6617de7dd5f11af46f0c7e0d2223ee065d71b9f3/src/tag006E.lean#L4</a></p>

#### [ Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165511):
<p>I am proud to say that I did actually write a simp lemma for that</p>

#### [ Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165512):
<p>My simp lemma says "crap, I made a poor design decision when designing that structure, but I can't be bothered to change it now"</p>

#### [ Mario Carneiro (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165514):
<p>that's just what I would have recommended</p>

#### [ Mario Carneiro (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165555):
<p>except possibly for the dependent args</p>

#### [ Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165556):
<p>You would recommend the change in the structure?</p>

#### [ Mario Carneiro (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165558):
<p>that doesn't matter so much</p>

#### [ Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165559):
<p>Oh!</p>

#### [ Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165562):
<p>You don't care which definition I use if they're all equivalent?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165567):
<p>I was going to bite the bullet one day and edit the definition of that structure. You're saying that's a crazy idea?</p>

#### [ Mario Carneiro (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165568):
<p>it affects the proof goals when defining structures with <code>{ stuff := ... }</code></p>

#### [ Mario Carneiro (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165569):
<p>so it depends on how you usually prove such goals</p>

#### [ Kevin Buzzard (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165570):
<p>I was going to change "f = g circ h" with "forall x, g (h x) = f x"</p>

#### [ Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165571):
<p>if the first thing you do is always funext, then that's a hint</p>

#### [ Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165608):
<p>Note the equality "f = g circ h"</p>

#### [ Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165611):
<p>the more complicated side on the right</p>

#### [ Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165612):
<p>is that also unwise?</p>

#### [ Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165613):
<p>actually here I recommend that ordering</p>

#### [ Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165615):
<p>The thing about funext was that there were a few times when the fact that it was comp was really useful, it made some proofs really nice and short</p>

#### [ Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165616):
<p>because the argument to f is getting simpler</p>

#### [ Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165617):
<p><em>boggle</em></p>

#### [ Kevin Buzzard (May 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165622):
<p>I don't understand</p>

#### [ Mario Carneiro (May 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165623):
<p>think of it as <code>f (comp a b) = f a o f b</code></p>

#### [ Mario Carneiro (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165670):
<p>here simp will want to go left to right to make the argument to <code>f</code> as simple as possible</p>

#### [ Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165671):
<p>It's <code>res U W x = res V W (res U V x)</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165672):
<p>that's what it is really</p>

#### [ Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165673):
<p>You still want it that way round?</p>

#### [ Mario Carneiro (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165680):
<p>that's not a good simp lemma</p>

#### [ Kevin Buzzard (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165681):
<p>"restriction of a function on U down to V and then down to W equals restriction directly down to W"</p>

#### [ Kevin Buzzard (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165684):
<p>Either way round?</p>

#### [ Mario Carneiro (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165726):
<p>Okay, I guess in this case since it's a proof arg it shouldn't be a metric of simplicity</p>

#### [ Mario Carneiro (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165727):
<p>so in that case you want <code>res V W (res U V x) = res U W x</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165729):
<p>This is the thing I don't understand. It takes two functions <code>res U V</code> and <code>res W V</code> and it returns one function. It's made it simpler. I don't understand what should be a simp lemma.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165735):
<p>Aah so you do want to switch the order?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165736):
<p>And then make a simp lemma?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165781):
<blockquote>
<p>Okay, I guess in this case since it's a proof arg it shouldn't be a metric of simplicity</p>
</blockquote>
<p>I don't understand that either :-/</p>

#### [ Mario Carneiro (May 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165790):
<p>You have this extra argument that has a big term in it</p>

#### [ Mario Carneiro (May 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165795):
<p>I've mentioned that proof args are bad for rewrites before</p>

#### [ Kevin Buzzard (May 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165838):
<p>Why?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165839):
<p>proof args are fundamental statements about the situation</p>

#### [ Kevin Buzzard (May 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165850):
<p>Are you saying that associativity of addition should not be a simp lemma?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165892):
<p>associativity of addition is both a simp lemma and seems to have the more complicated side on the right.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165901):
<p>None of it adds up to me. I am still nowhere near understanding what should be a simp lemma.</p>

#### [ Mario Carneiro (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165904):
<p>assoc is a special case</p>

#### [ Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165906):
<p><em>boggle</em></p>

#### [ Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165908):
<p>I'll add it to the docs</p>

#### [ Mario Carneiro (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165909):
<p>simp has special handling for comm/assoc operations</p>

#### [ Kevin Buzzard (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165948):
<p>which uses a convention which goes against the "simpler argument on the right" convention?</p>

#### [ Mario Carneiro (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165950):
<p>it would not normally be a good simp lemma, because it doesn't simplify the term</p>

#### [ Kevin Buzzard (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165958):
<p><code>mul_one</code> is a simp lemma and it's a proof arg, if I've understood the last term correctly</p>

#### [ Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165959):
<p>But simp will notice if you give it a lemma that looks like associativity and apply special algorithms to do smart things with that</p>

#### [ Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165971):
<p>None of those have proof args</p>

#### [ Kevin Buzzard (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165973):
<p><em>oh</em></p>

#### [ Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165976):
<p>I'm talking about proofs as arguments to functions you want to rewrite</p>

#### [ Mario Carneiro (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166014):
<p>so in this case that would be like proof arguments to <code>mul</code> or <code>one</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166015):
<p>I thought you were talking about proofs as arguments used to create a structure</p>

#### [ Mario Carneiro (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166021):
<p>in your case I'm talking about <code>res</code> which has three proof args</p>

#### [ Kevin Buzzard (May 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166027):
<p>Would your opinion change if made them all work magically using type class resolution?</p>

#### [ Mario Carneiro (May 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166028):
<p>yes</p>

#### [ Mario Carneiro (May 27 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166066):
<p>that's an interesting idea, I'd have to see how messy the arguments can get</p>

#### [ Kevin Buzzard (May 27 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166073):
<p>The reason I didn't use type class resolution for those things was that when I wrote that code I had no idea how typeclass resolution system worked</p>

#### [ Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166074):
<p>so I just over-rode it and would always pass the proofs manually</p>

#### [ Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166082):
<p>and then later on in the project I was forced to work with rings and ring homs</p>

#### [ Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166083):
<p>so I was forced to learn the system</p>

#### [ Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166086):
<p>and we had that long thread with me moaning and learning about <code>letI</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166279):
<p>Ok so coercions.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166280):
<p><code>theorem eew (Y : ℕ+) : ((Y : ℕ) : ℕ+) = Y := rfl -- fails</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166282):
<p>That's not good, right?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166286):
<p>Should that be a simp lemma?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166295):
<p><code>ℕ+</code> is one of my favourite sets in ZFC</p>

#### [ Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166296):
<p>Why is it so hard to work with here?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166333):
<p>Just because it's not a stupid semiring</p>

#### [ Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166339):
<p>maybe it's a demisemiring</p>

#### [ Mario Carneiro (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166349):
<p>that is a simp lemma, I think</p>

#### [ Kevin Buzzard (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166350):
<p>Aah here's a question.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166351):
<p>Let's say we ripped out the definition of pnat</p>

#### [ Mario Carneiro (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166352):
<p><code>coe_nat_coe</code></p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166390):
<p>and replaced it with a straight inductive structure with one and succ</p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166396):
<p>Would that make <em>any</em> difference to <em>anything</em></p>

#### [ Mario Carneiro (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166397):
<p>not really</p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166398):
<p>or you just write the new interface</p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166399):
<p>and that's it</p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166400):
<p>No issue with compile time or running time</p>

#### [ Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166401):
<p>or simp not working as well</p>

#### [ Mario Carneiro (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166402):
<p>anything not using the interface would be affected, of course</p>

#### [ Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166404):
<p>Aah</p>

#### [ Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166410):
<p>anything accessing the innards of the structure</p>

#### [ Mario Carneiro (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166411):
<p>i.e. if someone creates a pnat by writing &lt;2, dec_trivial&gt;</p>

#### [ Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166413):
<p>instead of (2 : pnat)</p>

#### [ Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166414):
<p>then they should be punished?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166415):
<p>How does that work?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166454):
<p>"You only use official constructors"</p>

#### [ Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166456):
<p>"not inbuilt stuff"</p>

#### [ Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166458):
<p>Oh wait -- surely anyone writing a proof in term mode with pnat will have constructors like that everywhere</p>

#### [ Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166463):
<p>because it's a super-cool way of being fancy in fancy term mode</p>

#### [ Kenny Lau (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166464):
<p>right</p>

#### [ Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166465):
<p>eew</p>

#### [ Mario Carneiro (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166466):
<p>well, the thing is that I don't want to avoid structure constructors, because they are very nice</p>

#### [ Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166467):
<p>So there <em>is</em> a question left</p>

#### [ Mario Carneiro (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166468):
<p>you can't replicate that functionality with an interface</p>

#### [ Mario Carneiro (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166515):
<p>unless the interface is to pass in a specially defined structure</p>

#### [ Mario Carneiro (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166518):
<p>like simp_config</p>

#### [ Kevin Buzzard (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166519):
<p>you've lost me now</p>

#### [ Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166524):
<p>but I do see that there is a huge argument for structure constructors and this presumably has some bearing on exactly which constructors you choose and maybe even in which order?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166527):
<p>maybe order irrelevant</p>

#### [ Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166528):
<p>but you never know</p>

#### [ Mario Carneiro (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166529):
<p>yes</p>

#### [ Mario Carneiro (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166530):
<p>order is relevant for anonymous constructors</p>

#### [ Mario Carneiro (May 27 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166572):
<p>Here are my currrent thoughts on presheaf fyi:</p>
<div class="codehilite"><pre><span></span>structure order_presheaf (α : Type u) [preorder α] :=
(F : α → Type u)
(res : ∀ x {y}, x ≤ y → F y → F x)
(Hid : ∀ x h a, res x h a = a)
(Hcomp : ∀ x y z h₁ h₂ (a : F z),
  res x h₁ (res y h₂ a) = res x (le_trans h₁ h₂) a)
</pre></div>

#### [ Kenny Lau (May 27 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166574):
<p>what is an <code>order_presheaf</code>?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166577):
<p>Would you want presheaves in mathlib?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166581):
<p>oh eew</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166582):
<p>what just happened there</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166583):
<p>with the open sets</p>

#### [ Kenny Lau (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166584):
<p>oh, they form a preorder under inclusion!</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166586):
<p>he thinks he's being clever</p>

#### [ Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166587):
<p>but we need the etale site ;-)</p>

#### [ Kevin Buzzard (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166588):
<p>so he's still not general enough ;-)</p>

#### [ Mario Carneiro (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166627):
<p>if you add enough axioms to the preorder you can capture exactly the open sets of some topology</p>

#### [ Kevin Buzzard (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166628):
<p>yeah, I was just remarking that at some point later on algebraic geometry needs the notion of sheaf on something more general than a topological space</p>

#### [ Mario Carneiro (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166630):
<p>but this part of the definition only needs a preorder</p>

#### [ Kenny Lau (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166636):
<blockquote>
<p>yeah, I was just remarking that at some point later on algebraic geometry needs the notion of sheaf on something more general than a topological space</p>
</blockquote>
<p>what do you need?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166638):
<p>sheaf on a site</p>

#### [ Reid Barton (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166639):
<p><code>[category \a]</code></p>

#### [ Kenny Lau (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166640):
<p>i.e. there may be more than one morphisms?</p>

#### [ Mario Carneiro (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166641):
<p>if you want a category then this is just <code>functor</code></p>

#### [ Reid Barton (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166643):
<p>Right</p>

#### [ Kevin Buzzard (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166644):
<p>but it has to satisfy the sheaf axiom</p>

#### [ Mario Carneiro (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166645):
<p>point me to that</p>

#### [ Kevin Buzzard (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166677):
<p>and you need more than a category to formalise that</p>

#### [ Kenny Lau (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166686):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  so they may have two "proofs" of <code>x \le y</code> and they want the two things to be unequal</p>

#### [ Reid Barton (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166687):
<p>well, so far we are only talking about presheaf I thought</p>

#### [ Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166688):
<p>I am actually very fine with that</p>

#### [ Kevin Buzzard (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166690):
<p>that's true but I am interested in more than presheaves here</p>

#### [ Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166691):
<p>that's the remaining problem with this definition</p>

#### [ Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166694):
<p>as I said, I don't like proof args</p>

#### [ Reid Barton (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166697):
<p>well then great! They won't be proofs once you generalize to a category <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166702):
<p>but you can't easily remove them from this... what's the structure of that argument otherwise?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166704):
<p><a href="https://stacks.math.columbia.edu/tag/00VH" target="_blank" title="https://stacks.math.columbia.edu/tag/00VH">https://stacks.math.columbia.edu/tag/00VH</a></p>

#### [ Mario Carneiro (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166705):
<p>I guess <code>Hom x y</code>?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166751):
<p>That's a site</p>

#### [ Reid Barton (May 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166756):
<p>Right, just a morphism in some category.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166765):
<p>Did you see <a href="https://stacks.math.columbia.edu/tag/00VI" target="_blank" title="https://stacks.math.columbia.edu/tag/00VI">https://stacks.math.columbia.edu/tag/00VI</a></p>

#### [ Kevin Buzzard (May 27 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166812):
<p>Mario, I think this says "if a computer scientist tries to do this, they will have universe issues. But in all the cases that a mathematican cares about, these issues can be avoided and we can do everything in Type"</p>

#### [ Mario Carneiro (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166822):
<p>Presheaves are already rather large</p>

#### [ Kevin Buzzard (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166824):
<p>"This definition uses two universes u and v, but when we apply it I claim that we can get away with one universe"</p>

#### [ Kevin Buzzard (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166825):
<p>How do you formalise that? ;-)</p>

#### [ Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166866):
<p>It looks like sites have to be small though</p>

#### [ Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166868):
<p>but what's a (pre)sheaf on a site?</p>

#### [ Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166873):
<p>all I see is a bunch of covering stuff</p>

#### [ Kevin Buzzard (May 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166884):
<p>Also relevant</p>

#### [ Kevin Buzzard (May 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166885):
<p><a href="https://stacks.math.columbia.edu/tag/00ZF" target="_blank" title="https://stacks.math.columbia.edu/tag/00ZF">https://stacks.math.columbia.edu/tag/00ZF</a></p>

#### [ Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166936):
<p><a href="https://stacks.math.columbia.edu/tag/00VL" target="_blank" title="https://stacks.math.columbia.edu/tag/00VL">https://stacks.math.columbia.edu/tag/00VL</a></p>

#### [ Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166937):
<p>sheaf!</p>

#### [ Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166938):
<p>Still no presheaf :-)</p>

#### [ Johan Commelin (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166940):
<p>Scott is doing sites in the his category stuff</p>

#### [ Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166942):
<p><a href="https://stacks.math.columbia.edu/tag/00V1" target="_blank" title="https://stacks.math.columbia.edu/tag/00V1">https://stacks.math.columbia.edu/tag/00V1</a></p>

#### [ Mario Carneiro (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166943):
<p>and what is the site corresponding to a top space?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166944):
<p>OK so presheaf on a category, sheaf on a site</p>

#### [ Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166945):
<p>The site corresponding to a top space is this</p>

#### [ Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166953):
<p>The category has an object for each open set</p>

#### [ Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166960):
<p>Homs from U to V are empty unless V sub U in which case there is one elment</p>

#### [ Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166966):
<p>Coverings: a set of morphisms U_i -&gt; U covers U iff the union of the image of the U_i is U</p>

#### [ Kevin Buzzard (May 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167004):
<p>The sheaf axiom says this.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167017):
<p>"If U is an open set, and it is covered by opens U_i, then to give a continuous function on U is to give a continuous function f_i on each U_i such that f_i and f_j agree on U_i intersect U_j"</p>

#### [ Reid Barton (May 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167025):
<p>You can equivalently describe the category like this. The objects are topological spaces equipped with a map to X which is an open immersion. A morphism is a continuous map which is compatible with the structural maps to X.</p>

#### [ Kevin Buzzard (May 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167027):
<p>They say "continuity can be checked locally"</p>

#### [ Mario Carneiro (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167071):
<p>isn't that just true?</p>

#### [ Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167072):
<p>Reid's changing of my category to an equivalent category was something which turned out to be really important</p>

#### [ Mario Carneiro (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167073):
<p>like as a statement of topology</p>

#### [ Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167074):
<p>It's precisely the statement that continuity is a local condition</p>

#### [ Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167081):
<p>So the <em>presheaf</em> of continuous functions on a topological space</p>

#### [ Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167082):
<p>is actually a sheaf!</p>

#### [ Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167083):
<p>But the presheaf of constant functions is not a sheaf</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167085):
<p>because if I have two disjoint open sets</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167091):
<p>and define a function to be 1 on one of them but 2 on the other one</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167093):
<p>it's locally constant</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167094):
<p>but not constant</p>

#### [ Mario Carneiro (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167095):
<p>ah okay, so locally constant functions is a sheaf</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167097):
<p>right</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167101):
<p>it's the sheafification of the presheaf of constant functions</p>

#### [ Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167102):
<p>sheafification is an adjoint to the forgetful functor</p>

#### [ Mario Carneiro (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167157):
<p>so how much does it matter that these are poset categories?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167158):
<p>Exactly</p>

#### [ Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167161):
<p>it doesn't matter at all</p>

#### [ Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167163):
<p>and in general they won't be</p>

#### [ Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167165):
<p>is a poset category one where the hom sets have size &lt;= 1?</p>

#### [ Mario Carneiro (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167166):
<p>yes</p>

#### [ Kevin Buzzard (May 27 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167175):
<p>so the etale site attached to a scheme does not have this property I guess</p>

#### [ Mario Carneiro (May 27 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167178):
<p>maybe it would be better to do this with honest categories</p>

#### [ Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167180):
<p>I think Scott said that quite a long time ago</p>

#### [ Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167223):
<p>but I just wanted to get on</p>

#### [ Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167230):
<p>Sheaves of sets on a site are a Mathematician's Topos Mario.</p>

#### [ Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167233):
<p>This is distinct to the CS topos</p>

#### [ Mario Carneiro (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167238):
<p>like in the literal sense?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167239):
<p>You have some more general notion I think</p>

#### [ Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167240):
<p>Topos is used to mean two different things, I believe</p>

#### [ Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167242):
<p>I like Grothendieck topoi</p>

#### [ Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167244):
<p>you like elmentary topoi</p>

#### [ Mario Carneiro (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167246):
<p>I am not sure I would say that...</p>

#### [ Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167247):
<p><a href="https://stacks.math.columbia.edu/tag/00X9" target="_blank" title="https://stacks.math.columbia.edu/tag/00X9">https://stacks.math.columbia.edu/tag/00X9</a></p>

#### [ Mario Carneiro (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167289):
<p>topoi is usually where I get off the bus</p>

#### [ Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167290):
<p>It took me a while, in the pre-Wikipedia age, to understand that the two uses of the word were distinct</p>

#### [ Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167293):
<p>I knew this guy as an UG who would go round saying "a topos is a category which is finitely complete, finitely cocomplete, has exponentiation and a subobject classifier"</p>

#### [ Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167295):
<p>and I had no idea what any of those things meant</p>

#### [ Kevin Buzzard (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167301):
<p>and then years later I found some topoi I was actually interested in</p>

#### [ Mario Carneiro (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167303):
<p>that's about where I am</p>

#### [ Kenny Lau (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167304):
<p><em>as</em> an UG :o</p>

#### [ Kevin Buzzard (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167305):
<p>and then it turned out they were a different kind of topos</p>

#### [ Mario Carneiro (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167307):
<p>I learn and forget those things every year</p>

#### [ Kevin Buzzard (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167313):
<p>There was once some debate about whether Wiles/Taylor-Wiles used Grothendieck topoi in their proof of FLT</p>

#### [ Kevin Buzzard (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167353):
<p>and the answer turned out to be</p>

#### [ Mario Carneiro (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167354):
<p>because that means large universes, right?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167358):
<p>"well, mathematicians are always a bit vague about what exactly they are using, and there is no mention of set-theoretic difficulties, but Brian Conrad went away and checked every single cohomology group in the entire proof and verified that it was OK, everything happened within one universe"</p>

#### [ Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167366):
<p>Wiles most definitely used etale cohomology in his proof</p>

#### [ Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167368):
<p>and I am almost certain that he cited some papers which at some point use flat cohomology</p>

#### [ Kevin Buzzard (May 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167412):
<p>and they probably cite some papers which at some point mention fpqc cohomology</p>

#### [ Kevin Buzzard (May 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167423):
<p>so we really needed an expert who could come along and say "I know exactly which parts of the theory of etale cohomlogy and other cohomology theories he used and can verify that all the stuff he uses can be formalised in ZFC"</p>

#### [ Kevin Buzzard (May 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167430):
<p>before that debate died down</p>

#### [ Kevin Buzzard (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167484):
<p>Some people really care about universes. If Lean really cannot keep track of them then these people might be skeptical</p>

#### [ Kevin Buzzard (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167502):
<p>My current personal viewpoint on this is simply to accept the large cardinals. If they make maths easier and more fun to do then I'm in</p>

#### [ Mario Carneiro (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167503):
<p>For the most part, if it lives in <code>Type</code> it can be constructed in ZFC</p>

#### [ Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167552):
<p>Right, but any file which uses "universes u v" is open to question right?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167553):
<p>Or even "universe u" perhaps</p>

#### [ Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167557):
<p>if it uses Type as well</p>

#### [ Mario Carneiro (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167559):
<p>no, as long as at the end you build something in <code>Type</code></p>

#### [ Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167561):
<p>Oh</p>

#### [ Mario Carneiro (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167563):
<p>The part which makes this not quite true is impredicativity of Prop</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167566):
<p>aie</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167570):
<p>so you get a proof which lived in another universe</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167573):
<p>but you can't get a proof in your own universe</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167575):
<p>so you use propext</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167577):
<p>cunning</p>

#### [ Mario Carneiro (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167578):
<p>you can construct proofs of propositions in Prop in Type, which assert existence of large cardinals</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167580):
<p>ha ha</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167582):
<p>oh I hadn't realised that</p>

#### [ Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167585):
<p>Prop covers its tracks</p>

#### [ Mario Carneiro (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167587):
<p>that's what impredicativity does for you</p>

#### [ Kevin Buzzard (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167632):
<p>But still to <em>construct</em> the proof you need the extra universes, right?</p>

#### [ Kenny Lau (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167636):
<p>is <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> being impredicative?</p>

#### [ Mario Carneiro (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167637):
<p>you could talk about configurations in Type 63 and it wouldn't make the proof large</p>

#### [ Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167641):
<p>I am just interested in exactly what can go wrong with regards to translating a DTT proof into ZFC</p>

#### [ Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167648):
<p>right, there are large universes in the proof</p>

#### [ Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167651):
<p>Because one day someone serious is going to ask me about this</p>

#### [ Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167652):
<p>DTT</p>

#### [ Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167653):
<p>?</p>

#### [ Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167654):
<p>so that wouldn't translate</p>

#### [ Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167655):
<p>However, this sort of sleight of hand is very rare</p>

#### [ Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167656):
<p>And the problem is that the proof might not be mine</p>

#### [ Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167657):
<p>The theorem could be formulated about Type in some library</p>

#### [ Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167658):
<p>so they work in a system stronger than ZFC?</p>

#### [ Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167660):
<p>like how PA can't prove Goodstein?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167661):
<p>and I never look at the proof</p>

#### [ Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167699):
<p>Yes Kenny</p>

#### [ Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167704):
<p>they work in ZFC + infinitely many inaccessible cardinals here</p>

#### [ Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167707):
<p>It's infinitely less likely to be consistent than ZFC</p>

#### [ Mario Carneiro (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167709):
<p>which is weaker than Tarski Grothendieck set theory btw</p>

#### [ Kenny Lau (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167710):
<p>Grothendieck?!</p>

#### [ Mario Carneiro (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167713):
<p>which is what most category theorists use</p>

#### [ Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167718):
<p>That is equivalent to ZFC + proper class of inaccessible cardinals</p>

#### [ Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167720):
<p>here we only need omega many</p>

#### [ Kenny Lau (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167723):
<p>fascinating</p>

#### [ Kenny Lau (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167725):
<p>logic never fails to fascinate me</p>

#### [ Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167726):
<p>and for any particular proof you can say "this used 3 universes" or such</p>

#### [ Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167767):
<p>it's impossible to use all the universes in a proof</p>

#### [ Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167768):
<p>But I am specifically interested in the proofs which only use one universe</p>

#### [ Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167769):
<p>For example does FLT definitely only use one universe?</p>

#### [ Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167771):
<p>well, actually you want zero universes</p>

#### [ Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167772):
<p>Oh yes I just want Type</p>

#### [ Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167773):
<p>ZFC has zero universes</p>

#### [ Kenny Lau (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167776):
<blockquote>
<p>ZFC has zero universes</p>
</blockquote>
<p>zero built-in universes</p>

#### [ Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167781):
<p>So currently the reference for "Wiles/TW proof of FLT is in ZFC" is "Email from Conrad"</p>

#### [ Mario Carneiro (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167782):
<p>It's a bit tricky to work with DTT with zero universes</p>

#### [ Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167783):
<p>Why?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167784):
<p>Say I globally exchange all the type u for type</p>

#### [ Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167786):
<p>how far do I get before the errors appear?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167831):
<p>Start with core lean</p>

#### [ Mario Carneiro (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167834):
<p>you have to be careful: <code>Gamma |- A : Type</code> is okay, but <code>Type</code> is not a type, in the sense <code>Gamma |- Type : Type 1</code> doesn't exist</p>

#### [ Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167836):
<p>Yeah, I promise I will never ask Type its type.</p>

#### [ Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167837):
<p>ZFC people are used to making promises</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167838):
<p>and they're usually quite good at keeping them</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167845):
<p>This is the world I have lived in all my life</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167846):
<p>and you are claiming to offer me more</p>

#### [ Mario Carneiro (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167847):
<p>Also you can have things like <code>A : Type -&gt; Type</code> in ZFC</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167848):
<p>but I don't see anything of interest out there</p>

#### [ Mario Carneiro (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167850):
<p>but again you can't quantify over them</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167851):
<p>Yes</p>

#### [ Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167852):
<p>no</p>

#### [ Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167891):
<p>oh wait</p>

#### [ Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167894):
<p>I can quantify over them</p>

#### [ Mario Carneiro (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167895):
<p><code>A : (Type -&gt; Type) -&gt; Type</code> is starting to get weird</p>

#### [ Mario Carneiro (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167899):
<p><code>A : Type -&gt; Type</code> is a proper class function</p>

#### [ Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167900):
<p>I just have to write some footnote explaining about how it can all be done properly if you ask a set theorist</p>

#### [ Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167902):
<p>because no object I consider in my paper has size greater than 2^2^2^2^aleph_0 so it's all OK</p>

#### [ Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167903):
<p>who needs inaccessible cardinals</p>

#### [ Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167909):
<p>I just something closed under a few iterations of the power set axiom and I'll be fine</p>

#### [ Mario Carneiro (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167910):
<p>That's really hard to do formally</p>

#### [ Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167913):
<p>There will be people out there who care about this.</p>

#### [ Mario Carneiro (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167916):
<p>at least if you didn't literally do that in the proof</p>

#### [ Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167918):
<p>Right, and who wants to do that?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167919):
<p>We just wanna have fun</p>

#### [ Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167961):
<p>I don't see any reason why ZFC should stay as the prevalent model of mathematics</p>

#### [ Mario Carneiro (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167962):
<p>What you want is a way to take a proof and shrink all the things in it to ZFC things</p>

#### [ Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167964):
<p>but without a doubt it is the prevalent model of mathematics</p>

#### [ Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167965):
<p>I don't</p>

#### [ Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167968):
<p>but some people might</p>

#### [ Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167969):
<p>and I have them in mind</p>

#### [ Mario Carneiro (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167973):
<p>or 2^2^2^2^aleph_0 things</p>

#### [ Mario Carneiro (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167984):
<p>and it's my job to figure out how to make sense of your request</p>

#### [ Kevin Buzzard (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167989):
<p>There are theorems of the form "if you proved X using 3 universes then you could have done it in ZFC" I think</p>

#### [ Kevin Buzzard (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168008):
<p>I think someone might have told me that even though wiles <em>certainly</em> used AC in his proof, FLT was now known to be a theorem of ZF</p>

#### [ Kevin Buzzard (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168036):
<p>because one of these magic meta-theorem things</p>

#### [ Mario Carneiro (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168042):
<p>yes, it's a pi01 statement so magic happens</p>

#### [ Mario Carneiro (May 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168485):
<p>here's the sheaf axiom using the poset presheaf definition:</p>
<div class="codehilite"><pre><span></span>def gluing {α} [complete_lattice α] (F : order_presheaf α)
  (X : α) {ι : Type*} (Y : ι → α) (Hcov : X = ⨆ i, Y i)
  (r : F.F X) :
  {a : Π i, F.F (Y i) | ∀ (i j : ι),
    F.res (Y i ⊓ Y j) inf_le_left (a i) =
    F.res (Y i ⊓ Y j) inf_le_right (a j) } :=
⟨λ i, F.res (Y i) (by rw Hcov; apply le_supr) r,
 λ i j, by simp [F.comp]⟩

def is_order_sheaf {α : Type u} [complete_lattice α]
  (F : order_presheaf α) : Prop :=
∀ (X : α) {ι : Type u} (Y : ι → α) (Hcov : X = ⨆ i, Y i),
function.bijective (gluing F X Y Hcov)
</pre></div>

#### [ Kevin Buzzard (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168542):
<p>Did you look at what I did?</p>

#### [ Mario Carneiro (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168543):
<p>yes, it was based on your definition</p>

#### [ Kevin Buzzard (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168545):
<p>ha ha hope I didn't make a mistake :-)</p>

#### [ Mario Carneiro (May 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168585):
<p>I think probably <code>bijective</code> makes more axioms than you really need here</p>

#### [ Mario Carneiro (May 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168586):
<p>like it's probably already injective</p>

#### [ Mario Carneiro (May 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168592):
<p>I would just state the actual condition you want, and prove it implies this function is bijective</p>

#### [ Kevin Buzzard (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168644):
<p><a href="https://stacks.math.columbia.edu/tag/009I" target="_blank" title="https://stacks.math.columbia.edu/tag/009I">https://stacks.math.columbia.edu/tag/009I</a></p>

#### [ Kevin Buzzard (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168648):
<p>Actually I guess I just copied everything from the stacks project (and spotted a mistake or two along the way :-) )</p>

#### [ Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168688):
<p>no, injective needs checking</p>

#### [ Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168689):
<p>A presheaf is just a functor</p>

#### [ Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168690):
<p>It takes an open set to a type</p>

#### [ Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168694):
<p>I could easily replace its value on X with some gigantic type that maps to the old  value</p>

#### [ Kevin Buzzard (May 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168700):
<p>If you think of them as sheaves of functions then injectivity may well be obvious</p>

#### [ Kevin Buzzard (May 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168702):
<p>but this is a true pi type -- it takes an open set to a random type, not functions on U or anything</p>

#### [ Kevin Buzzard (May 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168739):
<p>and res is part of the data, not restriction of functions</p>

#### [ Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168747):
<p>So are you interested in putting this presheaf and sheaf stuff in mathlib?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168749):
<p>I'm not bothered either way</p>

#### [ Mario Carneiro (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168750):
<p>but it is compositional</p>

#### [ Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168753):
<p>yes but that's an axiom</p>

#### [ Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168754):
<p>one of the two axioms of functor</p>

#### [ Mario Carneiro (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168756):
<p>Of course, I'm assuming it's a presheaf already</p>

#### [ Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168757):
<p>gotcha</p>

#### [ Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168797):
<p>I don't know whether I should bother tidying everything up</p>

#### [ Mario Carneiro (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168798):
<p>I mean the condition of being a sheaf can be stated more directly given it's a presheaf</p>

#### [ Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168799):
<p>right</p>

#### [ Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168801):
<p>but you still don't get injectivity for free</p>

#### [ Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168802):
<p>because I can replace F X</p>

#### [ Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168805):
<p>with with a random type Y that mapped to the old F X</p>

#### [ Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168806):
<p>X the whole space</p>

#### [ Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168809):
<p>and then it's still a presheaf</p>

#### [ Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168813):
<p>but there's no reason Y -&gt; old F X is injective</p>

#### [ Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168814):
<p>so I broke the sheaf property precisely by breaking injectivity</p>

#### [ Sean Leather (May 28 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127191991):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Re: <code>@[simp]</code> and left-to-right rewriting, perhaps, by browsing through the <code>@[simp]</code> theorems in <a href="https://github.com/spl/tts/blob/32df31590e3f7a88eeea6d672981ac1de93c0af7/src/env/props.lean" target="_blank" title="https://github.com/spl/tts/blob/32df31590e3f7a88eeea6d672981ac1de93c0af7/src/env/props.lean">this file</a>, you can get an idea of why they are structured the way they are.</p>


{% endraw %}
