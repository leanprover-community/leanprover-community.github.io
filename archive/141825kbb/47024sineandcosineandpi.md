---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/47024sineandcosineandpi.html
---

## Stream: [kbb](index.html)
### Topic: [sine and cosine and pi](47024sineandcosineandpi.html)

---


{% raw %}
#### [ Chris Hughes (Sep 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134008790):
<p>I've started working on sine and cosine. I have cleaned the proofs up until <code>exp (x + y)</code> and I'm currently working on things like <code>sin (x + y)</code>. I have no idea how to define pi however. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what's the best way to do this?</p>

#### [ Patrick Massot (Sep 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134009489):
<p>Do you have complex exp or only real?</p>

#### [ Chris Hughes (Sep 15 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134010115):
<p>complex. I'll define real.exp in terms of complex.exp</p>

#### [ Patrick Massot (Sep 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011693):
<p>Ok, so <code>sin (x + y)</code> and friends follow immediately from <code>exp(x+y)</code>.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011700):
<p>You're such a mathematician.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011706):
<p>Remember that you get a <code>/2</code> in those expressions. You need to convince Lean that you aren't dividing by zero.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011751):
<p>But Chris is pushing progress to the <code>exp</code> branch on community mathlib</p>

#### [ Patrick Massot (Sep 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011752):
<p>For <code>pi</code> you can prove that cos vanishes somewhere between 0 and 2 using the intermediate value theorem, and define pi as twice the first zero of cos. This is cheap but I guess proving other properties from that is painful. A better solution is probably to prove the classification of subgroups of (R, +), and define 2pi as the positive generator of ker(t mapsto exp(i*t)) (this kernel cannot be dense because exp is continuous and non-constant)</p>

#### [ Johan Commelin (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011758):
<p>Rights, so we need continuity of <code>exp</code>.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011759):
<p>For either definition.</p>

#### [ Patrick Massot (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011760):
<p>I both cases yes</p>

#### [ Johan Commelin (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011807):
<p>What is the best way to do this continuity proof?</p>

#### [ Johan Commelin (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011809):
<p>Generalise to arbitrary power series?</p>

#### [ Patrick Massot (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011813):
<p>We could also cheat and define pi using a random series, but then the link with exp and cos would be harder to establish</p>

#### [ Johan Commelin (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011817):
<p>I like your second definition.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011821):
<p>We should probably just check what Coq/Mizar/Isabelle do</p>

#### [ Reid Barton (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011825):
<p>If you have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><msup><mi>e</mi><mi>y</mi></msup></mrow><annotation encoding="application/x-tex">e^{x+y} = e^x e^y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">x</span><span class="mbin mtight">+</span><span class="mord mathit mtight" style="margin-right:0.03588em;">y</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">y</span></span></span></span></span></span></span></span></span></span></span> then it suffices to show that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding="application/x-tex">e^x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span></span></span></span></span></span></span></span> is continuous at 0, and for this you can use a crude bound on the power series.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011879):
<p>Ok, sounds good.</p>

#### [ Reid Barton (Sep 15 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011923):
<p>Patrick, you still have to prove that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mrow><mi>i</mi><mi>t</mi></mrow></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">e^{it} = 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:0.824664em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mord mathit mtight">t</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span> for some nonzero real <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi></mrow><annotation encoding="application/x-tex">t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">t</span></span></span></span> first, right?</p>

#### [ Patrick Massot (Sep 15 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011977):
<p>indeed we must exclude that the kernel is trivial</p>

#### [ Reid Barton (Sep 15 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012154):
<p>Does the definition of pi really rely on some explicit estimate like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mn>2</mn><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\cos 2 &lt; 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.68354em;vertical-align:-0.0391em;"></span><span class="base"><span class="mop">cos</span><span class="mord mathrm">2</span><span class="mrel">&lt;</span><span class="mord mathrm">0</span></span></span></span>? <br>
I guess if you have differential calculus at your disposal, you could show that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">\sin t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.66786em;"></span><span class="strut bottom" style="height:0.66786em;vertical-align:0em;"></span><span class="base"><span class="mop">sin</span><span class="mord mathit">t</span></span></span></span> is bounded, and then conclude that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">\cos t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mop">cos</span><span class="mord mathit">t</span></span></span></span> cannot be positive everywhere... wait no, I don't even see how to make this work.</p>

#### [ Patrick Massot (Sep 15 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012167):
<p><a href="https://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html" target="_blank" title="https://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html">https://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html</a> seems to use my first method</p>

#### [ Reid Barton (Sep 15 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012218):
<p>Okay--if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">\cos t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mop">cos</span><span class="mord mathit">t</span></span></span></span> was positive everywhere then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">\sin t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.66786em;"></span><span class="strut bottom" style="height:0.66786em;vertical-align:0em;"></span><span class="base"><span class="mop">sin</span><span class="mord mathit">t</span></span></span></span> would be increasing, and then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mi>t</mi></mrow><annotation encoding="application/x-tex">\cos t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mop">cos</span><span class="mord mathit">t</span></span></span></span> would have to lie below some line of negative slope, a contradiction.<br>
Not sure if one can extract an "elementary" (no differential calculus) proof along these lines.</p>

#### [ Patrick Massot (Sep 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012328):
<p>This all looks super tedious</p>

#### [ Patrick Massot (Sep 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012331):
<p>Let's do perfectoid spaces</p>

#### [ Johan Commelin (Sep 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012706):
<p>Hmmm, <span class="user-mention" data-user-id="110032">@Reid Barton</span> I can easily follow your maths proof that <code>exp</code> is continuous if it is ctu at <code>0</code>.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012709):
<p>But how do I put this into Lean?</p>

#### [ Patrick Massot (Sep 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012791):
<p><a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289</a> may help</p>

#### [ Johan Commelin (Sep 15 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012906):
<p>Aah thanks, that indeed looks useful.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012930):
<p>Do we know that <code>(exp x) \ne 0</code>?</p>

#### [ Patrick Massot (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012932):
<p>It's not yet merged in mathlib, but doesn't depend on much</p>

#### [ Johan Commelin (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012936):
<p>Because then we know that <code>exp</code> is a group hom, which might also help.</p>

#### [ Chris Hughes (Sep 15 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012999):
<p>We do know exp \ne 0</p>

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013589):
<p>Hmmm, I'm horrible with these continuity proofs...</p>

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013597):
<p>So there is <code>squeeze_zero</code>, but I don't think there is a generic squeeze lemma, right?</p>

#### [ Patrick Massot (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013604):
<p>there is</p>

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013612):
<p>Ooh, my VScode didn't find it.</p>

#### [ Johan Commelin (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013653):
<p>Let me try again</p>

#### [ Johan Commelin (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013665):
<p>Aah, it only has squeeze in its docstring</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013667):
<p>grep for sandwich in mathlib</p>

#### [ Patrick Massot (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013671):
<p><a href="https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/analysis/topology/topological_structures.lean#L438" target="_blank" title="https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/analysis/topology/topological_structures.lean#L438">https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/analysis/topology/topological_structures.lean#L438</a></p>

#### [ Patrick Massot (Sep 15 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013680):
<p>grep for squeeze also works</p>

#### [ Patrick Massot (Sep 15 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013687):
<p>but grep for gendarme doesn't work</p>

#### [ Johan Commelin (Sep 15 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013912):
<p>Hmm snap, of course that doesn't help for continuity of the complex version.</p>

#### [ Patrick Massot (Sep 15 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013997):
<p>Anyway, the long term reasoning is clear: we don't want a trick, we want general results on power series</p>

#### [ Johan Commelin (Sep 15 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014067):
<p>Right. And I think I'dd rather work on the long term</p>

#### [ Johan Commelin (Sep 15 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014074):
<p>So, should we create <code>power_series.lean</code> on cocalc?</p>

#### [ Johan Commelin (Sep 15 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014085):
<p>Maybe Kevin will see it. I think I don't care</p>

#### [ Johan Commelin (Sep 15 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014151):
<p>Is that ok with others? Then we could multiplayer power series into existence.</p>

#### [ Johan Commelin (Sep 15 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014152):
<p>I'm quite addicted to that experience.</p>

#### [ Patrick Massot (Sep 15 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014192):
<p>I would wait until <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> tells us about how this is done in Isabelle (they have a lot of analysis there)</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014543):
<p>I will take a look</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014907):
<p>So, continuity of <code>exp</code> is proved using derivability. There is a section "Term-by-Term Differentiability of Power Series" in <a href="http://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html" target="_blank" title="http://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html">http://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html</a> where most of it is proved. The central part is <code>termdiffs</code> which states: <code>DERIV (λx. ∑n. c n * x^n) x :&gt; (∑n. (diffs c) n * x^n)</code>.  Where <code>diffs c := (λn. of_nat (Suc n) * c (Suc n))</code> (<code>Suc</code> is <code>nat.succ</code> and <code>of_nat</code> is the coercion nat to a real_algebra).</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014963):
<p>The lemma <code>termdiffs</code> assumes that various power series converge.</p>

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015048):
<p>So it would make sense to define power series, and then we need to change the definition of exp to use those power series.</p>

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015049):
<p>Is that right?</p>

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015051):
<p>I mean, there won't change that much</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015240):
<p>Yes, I think it would make sense to define power series. Also derivatives...</p>

#### [ Johan Commelin (Sep 15 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015325):
<p>Ok, and this is purely algebraic stuff, right?</p>

#### [ Johan Commelin (Sep 15 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015338):
<p>Or do you also mean the analytic derivative?</p>

#### [ Johannes Hölzl (Sep 15 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015355):
<p>I guess we need to analytic derivative to prove continuity</p>

#### [ Johan Commelin (Sep 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015413):
<p>Hmmm, ok</p>

#### [ Johan Commelin (Sep 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015419):
<p>And we really need all of this to define pi?</p>

#### [ Johan Commelin (Sep 15 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015436):
<p>Well, we will need this stuff anyway</p>

#### [ Johan Commelin (Sep 15 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015498):
<p>I'm going to create a <code>power_series.lean</code> on CoCalc</p>

#### [ Johannes Hölzl (Sep 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015586):
<p>In Isabelle:<br>
<code>pi = 2 * (THE x. 0 ≤ x ∧ x ≤ 2 ∧ cos x = 0)</code> <br>
and then even more algebric facts about <code>cos</code> and <code>sin</code></p>

#### [ Johan Commelin (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015647):
<p>Right, but I guess there is a hidden proof that such <code>x</code> exists, not?</p>

#### [ Johannes Hölzl (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015653):
<p>of course</p>

#### [ Johannes Hölzl (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015655):
<p><code>cos_is_zero: "∃!x::real. 0 ≤ x ∧ x ≤ 2 ∧ cos x = 0"</code></p>

#### [ Johannes Hölzl (Sep 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015666):
<p>it uses IVT</p>

#### [ Johan Commelin (Sep 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015678):
<p>Right, so we need continuity</p>

#### [ Johannes Hölzl (Sep 15 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015726):
<p>it also uses derivative of <code>cos</code> and that <code>sin 2 &gt; 0</code></p>

#### [ Johan Commelin (Sep 15 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015749):
<p>Ok</p>

#### [ Chris Hughes (Sep 15 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134021725):
<p>I just pushed a load of stuff to the <code>exp</code> branch of community mathlib. It's about as far as I can go without continuity of <code>exp</code> and I'm not sure what the best approach for that is.</p>

#### [ Mario Carneiro (Sep 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023255):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> In metamath we used a very low brow approach to exp (it comes before analysis), which I think worked quite well.</p>
<ul>
<li>I assume you already have things like the addition formula and other algebraic stuff on sin and cos.</li>
<li><code>exp</code> is continuous iff it is continuous at each point. By facts about multiplying functions continuous at a point, you can show that it suffices to prove <code>exp</code> is continuous at zero.</li>
<li><code>1 + x &lt;= exp x</code> for positive <code>x</code> by taking away the rest of the summands; <code>exp x &lt;= 1/(1-x)</code> by comparing the infinite series of these two. Thus <code>exp</code> is continuous and even differentiable at zero by the sandwich lemma.</li>
<li>It follows from basic topological ring action that <code>sin</code> is continuous.</li>
<li><code>pi</code> is the infimum of the positive zeros of the <code>sin</code> function. We need to show this is well defined and a zero of the sin function.</li>
<li>Suppose <code>a</code> is a zero of <code>sin</code> in the range <code>(2,4)</code>, and <code>b</code> is a positive zero of sin. Show that if <code>pi &lt; a</code> then <code>(pi + a) / 2 &lt;= b</code>, because <code>2*a - b</code> is also a zero of <code>sin</code>.</li>
<li>By the intermediate value theorem applied to <code>sin</code>, and <code>sin 2 &gt; 0</code> and <code>sin 4 &lt; 0</code>, there is a zero <code>a</code> in this range, and <code>pi</code> exists. if <code>pi &lt; a</code>, then <code>(pi + a) / 2 &lt;= pi</code> by the above lemma, since <code>pi</code> is the infimum of all positive roots of sin. Thus <code>a &lt;= pi</code> and thus <code>pi</code> is the unique zero of sin in this range.</li>
</ul>

#### [ Chris Hughes (Sep 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023510):
<p>Can you point me to the sandwich lemma, and the facts about multiplying functions continuous at points? I've never touched anything in the analysis folder before now.</p>

#### [ Mario Carneiro (Sep 15 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023552):
<p>For the bounds:</p>
<ul>
<li><code>sin 4 = 2 * sin 2 * cos 2</code> is negative because <code>sin 2</code> is positive and <code>cos 2</code> is negative</li>
<li><code>-7/9 &lt; cos 2 &lt; -1/9</code> because <code>cos 2 = 2 * (cos 1)^2 - 1</code> and <code>1/3 &lt; cos 1 &lt; 2/3</code></li>
<li><code>sin (2*x)</code> is positive for all <code>0&lt;x&lt;=1</code> because <code>sin x</code> and <code>cos x</code> are</li>
<li><code>x - x^3/3 &lt; sin x &lt; x</code> and <code>1 - 2/3 * x^2 &lt; cos x &lt; 1 - x^2/3</code> on <code>(0, 1]</code> by infinite series bounds</li>
</ul>

#### [ Mario Carneiro (Sep 15 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023609):
<p>I'm not sure we have it, but it should be easy to show over the reals (or whatever generalization best encompasses the reals)</p>

#### [ Mario Carneiro (Sep 15 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023667):
<p>By the way, metamath used to have a direct proof before analysis was developed, but now continuity of exp follows from differentiability, and continuity uses various topological notions and proofs. I think the definition of <code>exp</code> can be in <code>data.{real,complex}.basic</code>, but <code>pi</code> and other facts that depend on continuity should go in the topological part, at <code>analysis.{real,complex}</code></p>

#### [ Chris Hughes (Sep 15 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023818):
<p>Where are the relevant theorems in the lean library? Do we have IVT?</p>

#### [ Mario Carneiro (Sep 15 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023917):
<p>I don't think we do. I would want to just prove it over the reals for now</p>

#### [ Chris Hughes (Sep 15 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024102):
<p>How do I state continuous at a point?</p>

#### [ Mario Carneiro (Sep 15 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024208):
<p>In topology, <code>f : X -&gt; Y</code> is continuous at <code>x</code> if <code>tendsto f (nhds x) (nhds (f x))</code></p>

#### [ Chris Hughes (Sep 15 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024352):
<p>And what are the lemmas that let me prove that it's continuous everywhere if it's continuous at 0?</p>

#### [ Chris Hughes (Sep 15 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024397):
<p>I'm not even sure why that's true.</p>

#### [ Patrick Massot (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024517):
<p>I think I already answered that earlier today</p>

#### [ Chris Hughes (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024523):
<p>I think I've worked out vaguely why it's true in maths, but not in lean.</p>

#### [ Patrick Massot (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024526):
<p><a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289</a></p>

#### [ Patrick Massot (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024575):
<p>Importing that and apply it to reals prove that <code>tendsto f (nhds x) (nhds (f x))</code> iff <code>tendsto (lambda h, f (x+h)) (nhds 0) (nhds (f x))</code></p>

#### [ Mario Carneiro (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024581):
<p>this is a consequence of <code>(\lam x, x + h)</code> being a homeo</p>

#### [ Patrick Massot (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024583):
<p>In case of exp you can rewrite f (x+h) as exp(x)*exp(h), use exp(x) converges (it's constant) and the result at zero</p>

#### [ Chris Hughes (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024634):
<p>Is this the correct statement of <code>exp</code> is continuous at x = 0 </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_exp</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">exp</span> <span class="o">(</span><span class="n">nhds</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024638):
<p>yes, hopefully you know <code>exp 0 = 1</code> already by algebraic stuff</p>

#### [ Patrick Massot (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024640):
<p>The name is bad, but the statement is ok</p>

#### [ Patrick Massot (Sep 15 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024646):
<p>assuming you know exp 0</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024648):
<p>that's true, it should say <code>tendsto_exp_zero</code> or something</p>

#### [ Patrick Massot (Sep 15 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024700):
<p>We should probably prove the lemma for general homomorphisms between topological group (continuity at zero implies continuity)</p>

#### [ Chris Hughes (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024770):
<p>And this only works for <code>real.exp</code> right?</p>

#### [ Patrick Massot (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024810):
<p>Why?</p>

#### [ Patrick Massot (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024811):
<p>Didn't you prove the addition formula for complex numbers?</p>

#### [ Chris Hughes (Sep 15 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024860):
<p>Yes, but <code>tendsto_of_tendsto_of_tendsto_of_le_of_le</code> requires a partial order on complexes, unless I'm doing something wrong.</p>

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024868):
<p>Oh, I meant that continuity at zero in C implies continuity everywhere</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024869):
<p>The metamath comment says that the key step is <code>abs (exp x - x - 1) &lt;= (abs x) ^ 2 * 3/4</code></p>

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024871):
<p>But Mario's idea to prove continuity at zero works in R</p>

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024882):
<p>but he seems to have a new idea</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024883):
<p>this bound works on complexes too</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024925):
<p>it is a special case of the tail bound on exp</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024939):
<p><code>abs (sum k = m,...,infty (x ^ n / n!)) &lt;= (abs a)^m * ((m + 1) / (m! * m))</code></p>

#### [ Mario Carneiro (Sep 15 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024982):
<p>when <code>abs x &lt;= 1</code></p>

#### [ Patrick Massot (Sep 15 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024988):
<p>I need to go, sorry</p>

#### [ Chris Hughes (Sep 15 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024991):
<p>How does the bound work on the complexes when they don't have linear order? What's the correct statement? <code>abs ∘ exp</code> is continuous doesn't seem like enough to prove <code>exp</code> is continuous. Bear in mind I know very little about analysis.</p>

#### [ Chris Hughes (Sep 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025095):
<p>If I manage to turn my goal into something in terms of functions I recognize, I;m sure I'll be fine, but I just need to work out how to get from <code>nhds</code> to something I recognize.</p>

#### [ Kenny Lau (Sep 15 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025197):
<p>you should go revise M1P1 :P</p>

#### [ Chris Hughes (Sep 15 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025204):
<p>That doesn't mention anything to do with complex numbers.</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025251):
<p>The statement <code>abs (exp x - x - 1) &lt;= (abs x) ^ 2 * 3/4</code> is enough to prove that <code>exp</code> is differentiable at 0</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025253):
<p>here <code>x</code> is a complex number</p>

#### [ Chris Hughes (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025255):
<p>I could probably manage that.</p>

#### [ Chris Hughes (Sep 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025261):
<p>You'll have to help me turn that into anything about continuity.</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025263):
<p>For continuity you could probably just do the zeroth order tail bound, which is <code>abs (exp x - 1) &lt;= (abs x) * 2</code></p>

#### [ Kenny Lau (Sep 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025306):
<p>is it realistic to develop a general theory of complex power series?</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025308):
<p>maybe, but I'd prefer to defer it</p>

#### [ Patrick Massot (Sep 17 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134088538):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> are you currently working on exp?</p>

#### [ Chris Hughes (Sep 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134088612):
<p>No, and I am doing other things today. I might work on it tomorrow.</p>

#### [ Chris Hughes (Sep 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117371):
<p>I made some progress. I proved IVT, though I'm not sure if there is some clever simple proof.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">IVT</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hy</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hxy</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">z</span> <span class="bp">∧</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">f</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">z</span> <span class="o">:=</span> <span class="n">Sup</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">hz₁</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">},</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hz₂</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hxy</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">le_Sup</span> <span class="bp">_</span> <span class="n">hz₁</span> <span class="bp">⟨</span><span class="n">hx</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hxy</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="o">(</span><span class="n">Sup_le</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="n">hz₂</span> <span class="n">hz₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
  <span class="n">eq_of_forall_dist_le</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε0</span><span class="o">,</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">δ</span><span class="o">,</span> <span class="n">hδ0</span><span class="o">,</span> <span class="n">hδ</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">continuous_iff_tendsto</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hf</span> <span class="n">z</span><span class="o">)</span> <span class="n">ε</span> <span class="n">ε0</span> <span class="k">in</span>
    <span class="o">(</span><span class="n">le_total</span> <span class="mi">0</span> <span class="o">(</span><span class="n">f</span> <span class="n">z</span><span class="o">))</span><span class="bp">.</span><span class="n">elim</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hfε</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">dist_0_eq_abs</span><span class="o">,</span> <span class="n">abs_of_nonneg</span> <span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">hfε</span><span class="o">,</span>
        <span class="n">refine</span> <span class="n">mt</span> <span class="o">(</span><span class="n">Sup_le</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="n">hz₂</span> <span class="n">hz₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span>
          <span class="o">(</span><span class="n">not_le_of_gt</span> <span class="o">(</span><span class="n">sub_lt_self</span> <span class="n">z</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">)))</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span> <span class="n">le_of_not_gt</span>
            <span class="o">(</span><span class="bp">λ</span> <span class="n">hgδ</span><span class="o">,</span> <span class="n">not_lt_of_ge</span> <span class="n">hg</span><span class="bp">.</span><span class="mi">1</span>
              <span class="o">(</span><span class="n">lt_trans</span> <span class="o">(</span><span class="n">sub_pos_of_lt</span> <span class="n">hfε</span><span class="o">)</span> <span class="o">(</span><span class="n">sub_lt_of_sub_lt</span>
                <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span><span class="o">))))),</span>
        <span class="n">rw</span> <span class="n">abs_sub</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">hδ</span> <span class="o">(</span><span class="n">abs_sub_lt_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">sub_nonpos</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">le_Sup</span> <span class="bp">_</span> <span class="n">hz₁</span> <span class="n">hg</span><span class="o">))</span> <span class="n">hδ0</span><span class="o">,</span>
          <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">z</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">linarith</span><span class="bp">⟩</span><span class="o">)</span>
        <span class="kn">end</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hfε</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">dist_0_eq_abs</span><span class="o">,</span> <span class="n">abs_of_nonpos</span> <span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">hfε</span><span class="o">,</span>
        <span class="n">refine</span> <span class="n">mt</span> <span class="o">(</span><span class="n">le_Sup</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">})</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">k</span><span class="o">,</span> <span class="n">k</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="bp">→</span> <span class="n">k</span> <span class="bp">≤</span> <span class="n">z</span><span class="o">,</span>
            <span class="n">not_le_of_gt</span> <span class="o">((</span><span class="n">lt_add_iff_pos_left</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))</span>
              <span class="o">(</span><span class="n">h</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">le_trans</span> <span class="o">(</span><span class="n">le_sub_iff_add_le</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">le_trans</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span>
                    <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">hδ</span> <span class="err">$</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dist_eq</span><span class="o">,</span> <span class="n">add_sub_cancel</span><span class="o">,</span> <span class="n">abs_of_nonneg</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))]</span><span class="bp">;</span>
                      <span class="n">exact</span> <span class="n">half_lt_self</span> <span class="n">hδ0</span><span class="o">))))</span>
                  <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="n">hfε</span><span class="o">)),</span>
                <span class="n">le_trans</span> <span class="o">(</span><span class="n">le_Sup</span> <span class="bp">_</span> <span class="n">hz₁</span> <span class="bp">⟨</span><span class="n">hx</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hxy</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">((</span><span class="n">lt_add_iff_pos_left</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))),</span>
                <span class="n">le_of_not_gt</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hδy</span><span class="o">,</span> <span class="n">not_lt_of_ge</span> <span class="n">hy</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="k">show</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">f</span> <span class="n">z</span> <span class="bp">-</span> <span class="n">ε</span><span class="o">,</span> <span class="k">by</span> <span class="n">linarith</span><span class="o">)</span>
                  <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span>
                    <span class="o">(</span><span class="bp">@</span><span class="n">hδ</span> <span class="n">y</span> <span class="o">(</span><span class="n">abs_sub_lt_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">z</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">linarith</span><span class="o">,</span>
                      <span class="n">sub_lt_iff_lt_add</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">add_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">lt_add_of_le_of_pos</span>
                        <span class="o">((</span><span class="n">Sup_le</span> <span class="bp">_</span> <span class="n">hz₂</span> <span class="n">hz₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="n">hδ0</span><span class="o">)</span><span class="bp">⟩</span><span class="o">))))))</span><span class="bp">⟩</span><span class="o">))</span> <span class="n">hz₁</span>
        <span class="kn">end</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117436):
<p>Well done!</p>

#### [ Johan Commelin (Sep 17 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117495):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I guess you could quite easily change the <code>0</code>s in the statement into a parameter, right?</p>

#### [ Johan Commelin (Sep 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117550):
<p>Hmm, but you are use <code>half_pos</code> and things like that.</p>

#### [ Johan Commelin (Sep 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117558):
<p>So maybe you should just leave this like it is.</p>

#### [ Chris Hughes (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117956):
<p>I can deduce the general statement from this quite easily I imagine.</p>

#### [ Johan Commelin (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117967):
<p>Yes, agreed.</p>

#### [ Chris Hughes (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117976):
<p>The more important generalisation is that it only needs to be continuous on the interval.</p>

#### [ Kenny Lau (Sep 17 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118217):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> how much topology do you know?</p>

#### [ Chris Hughes (Sep 17 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118244):
<p>More or less none.</p>

#### [ Kenny Lau (Sep 17 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118305):
<p>if x&lt;y and f(x)&lt;0 and f(y)&gt;0, then {t | f(t) &lt; 0} and {t | f(t) &gt; 0} are two disjoint open subsets of [x,y]. Since [x,y] is connected, the union of those two sets can't be the entirety of [x,y], so there must be something not belonging to those two sets, i.e. t such that f(t) = 0</p>

#### [ Johan Commelin (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118524):
<p>Do we know that intervals are connected?</p>

#### [ Johan Commelin (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118620):
<p>Does Lean even know what an interval is?</p>

#### [ Reid Barton (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118624):
<p>I don't think we have connectedness yet</p>

#### [ Reid Barton (Sep 17 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118642):
<p>We do have intervals though and Lean knows closed ones are compact</p>

#### [ Reid Barton (Sep 17 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118740):
<p>Basically it's a similar proof to the one above I think, except the set {a | f a &lt;= 0 ...} is now called U</p>

#### [ Kenny Lau (Sep 17 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118868):
<p>right, we know they're compact but not that they're connected...?</p>

#### [ Mario Carneiro (Sep 17 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119204):
<p>right, the meat of this proof is showing that R is connected</p>

#### [ Mario Carneiro (Sep 17 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119343):
<p>I think you can pretty trivially generalize the assumption to <code>∀ x, a &lt; x → x &lt; b → tendsto f (nhds x) (nhds (f x))</code></p>

#### [ Mario Carneiro (Sep 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119442):
<p>If you prefer, you can prove the version assuming <code>continuous f</code> as a corollary</p>

#### [ Mario Carneiro (Sep 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119455):
<p>other than that, I think this is fine for the first cut</p>

#### [ Chris Hughes (Sep 17 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120625):
<p>I almost generalized it to <code>∀ x, a &lt; x → x &lt; b → tendsto f (nhds x) (nhds (f x))</code>. I have <code>lt</code> instead of <code>le</code>. Generalizing it to <code>lt</code> seems to add quite a bit of complication.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">IVT</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">tendsto</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)))</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hy</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hxy</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">z</span> <span class="bp">∧</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">f</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">z</span> <span class="o">:=</span> <span class="n">Sup</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">hz₁</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">},</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hz₂</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hxy</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hxz</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">z</span><span class="o">,</span> <span class="k">from</span> <span class="n">le_Sup</span> <span class="bp">_</span> <span class="n">hz₁</span> <span class="bp">⟨</span><span class="n">hx</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hxy</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hzy</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="o">(</span><span class="n">Sup_le</span> <span class="bp">_</span> <span class="n">hz₂</span> <span class="n">hz₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
<span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">hxz</span><span class="o">,</span> <span class="n">hzy</span><span class="o">,</span>
  <span class="n">eq_of_forall_dist_le</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε0</span><span class="o">,</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">δ</span><span class="o">,</span> <span class="n">hδ0</span><span class="o">,</span> <span class="n">hδ</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">hf</span> <span class="bp">_</span> <span class="n">hxz</span> <span class="n">hzy</span><span class="o">)</span> <span class="n">ε</span> <span class="n">ε0</span> <span class="k">in</span>
    <span class="o">(</span><span class="n">le_total</span> <span class="mi">0</span> <span class="o">(</span><span class="n">f</span> <span class="n">z</span><span class="o">))</span><span class="bp">.</span><span class="n">elim</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hfε</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">dist_0_eq_abs</span><span class="o">,</span> <span class="n">abs_of_nonneg</span> <span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">hfε</span><span class="o">,</span>
        <span class="n">refine</span> <span class="n">mt</span> <span class="o">(</span><span class="n">Sup_le</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="n">hz₂</span> <span class="n">hz₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span>
          <span class="o">(</span><span class="n">not_le_of_gt</span> <span class="o">(</span><span class="n">sub_lt_self</span> <span class="n">z</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">)))</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span> <span class="n">le_of_not_gt</span>
            <span class="o">(</span><span class="bp">λ</span> <span class="n">hgδ</span><span class="o">,</span> <span class="n">not_lt_of_ge</span> <span class="n">hg</span><span class="bp">.</span><span class="mi">1</span>
              <span class="o">(</span><span class="n">lt_trans</span> <span class="o">(</span><span class="n">sub_pos_of_lt</span> <span class="n">hfε</span><span class="o">)</span> <span class="o">(</span><span class="n">sub_lt_of_sub_lt</span>
                <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span><span class="o">))))),</span>
        <span class="n">rw</span> <span class="n">abs_sub</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">hδ</span> <span class="o">(</span><span class="n">abs_sub_lt_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">sub_nonpos</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">le_Sup</span> <span class="bp">_</span> <span class="n">hz₁</span> <span class="n">hg</span><span class="o">))</span> <span class="n">hδ0</span><span class="o">,</span>
          <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">z</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">linarith</span><span class="bp">⟩</span><span class="o">)</span>
        <span class="kn">end</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hfε</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">dist_0_eq_abs</span><span class="o">,</span> <span class="n">abs_of_nonpos</span> <span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">hfε</span><span class="o">,</span>
        <span class="n">refine</span> <span class="n">mt</span> <span class="o">(</span><span class="n">le_Sup</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">})</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">k</span><span class="o">,</span> <span class="n">k</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">}</span> <span class="bp">→</span> <span class="n">k</span> <span class="bp">≤</span> <span class="n">z</span><span class="o">,</span>
            <span class="n">not_le_of_gt</span> <span class="o">((</span><span class="n">lt_add_iff_pos_left</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))</span>
              <span class="o">(</span><span class="n">h</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">le_trans</span> <span class="o">(</span><span class="n">le_sub_iff_add_le</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">le_trans</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span>
                    <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">hδ</span> <span class="err">$</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dist_eq</span><span class="o">,</span> <span class="n">add_sub_cancel</span><span class="o">,</span> <span class="n">abs_of_nonneg</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))]</span><span class="bp">;</span>
                      <span class="n">exact</span> <span class="n">half_lt_self</span> <span class="n">hδ0</span><span class="o">))))</span>
                  <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="n">hfε</span><span class="o">)),</span>
                <span class="n">le_trans</span> <span class="n">hxz</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">((</span><span class="n">lt_add_iff_pos_left</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">half_pos</span> <span class="n">hδ0</span><span class="o">))),</span>
                <span class="n">le_of_not_gt</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hδy</span><span class="o">,</span> <span class="n">not_lt_of_ge</span> <span class="n">hy</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="k">show</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">f</span> <span class="n">z</span> <span class="bp">-</span> <span class="n">ε</span><span class="o">,</span> <span class="k">by</span> <span class="n">linarith</span><span class="o">)</span>
                  <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">le_abs_self</span> <span class="bp">_</span><span class="o">)</span>
                    <span class="o">(</span><span class="bp">@</span><span class="n">hδ</span> <span class="n">y</span> <span class="o">(</span><span class="n">abs_sub_lt_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">z</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">linarith</span><span class="o">,</span>
                      <span class="n">sub_lt_iff_lt_add</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">add_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">lt_add_of_le_of_pos</span>
                        <span class="n">hzy</span> <span class="n">hδ0</span><span class="o">)</span><span class="bp">⟩</span><span class="o">))))))</span><span class="bp">⟩</span><span class="o">))</span> <span class="n">hz₁</span>
        <span class="kn">end</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Chris Hughes (Sep 17 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120816):
<p>In fact generalizing to <code>lt</code> makes the statement false I think.</p>

#### [ Johan Commelin (Sep 17 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120937):
<p>Right, you need the closed interval.</p>

#### [ Mario Carneiro (Sep 17 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121041):
<p>ah yes, you're right. In order to properly say "continuous on [a, b]" you would need <code>tendsto f (nhds a ⊓ principal (Icc a b)) (nhds (f a))</code></p>

#### [ Chris Hughes (Sep 17 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121162):
<p>What does that mean, and how is it different from my assumption?</p>

#### [ Chris Hughes (Sep 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121414):
<p>Is it weaker or stronger than my assumption?</p>

#### [ Johan Commelin (Sep 17 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121530):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> you know about left/right-continuity at a point?</p>

#### [ Mario Carneiro (Sep 17 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121551):
<p>My predicate says that <code>f</code> restricted to <code>[a, b]</code> is continuous</p>

#### [ Mario Carneiro (Sep 17 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121563):
<p>so it might have discontinuity at a or b from outside the interval</p>

#### [ Chris Hughes (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121604):
<p>I see.</p>

#### [ Johan Commelin (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121609):
<p>Eg: <code>f x = if x \in [a,b] then 0 else 1</code></p>

#### [ Mario Carneiro (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121627):
<p>But you should be able to extend any continuous function on [a,b] to one continuous in your sense anyway, so I wouldn't make a big deal about it</p>

#### [ Chris Hughes (Sep 19 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256188):
<p>I managed to prove this today. </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">exp_continuous_aux</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">abs</span> <span class="o">(</span><span class="n">exp</span> <span class="n">x</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">/</span> <span class="mi">6</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>


<p>It's <code>5 / 6</code> instead of <code>3/4</code>, is that going to be a problem? I'm not sure where my extra <code>1/12</code> went</p>

#### [ Chris Hughes (Sep 19 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256238):
<p>I suppose it depends on whether I can still prove the cos inequalities</p>

#### [ Mario Carneiro (Sep 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256650):
<p>that's weird, how did you prove it?</p>

#### [ Mario Carneiro (Sep 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256727):
<p>I don't think we need any particular bound for this part, that's enough for continuity of course</p>

#### [ Chris Hughes (Sep 19 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256880):
<p>This is my proof. I think the lost information is probably in the step<br>
<code>sum (range (j - 3)) (λ m, 1 / (m + 3).fact) ≤ sum (range (j - 3)) (λ m, 1 / 6 * (1 / 2) ^ m)</code></p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">exp_continuous_aux</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">abs</span> <span class="o">(</span><span class="n">exp</span> <span class="n">x</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">/</span> <span class="mi">6</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">onesubhalf</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span>
<span class="k">have</span> <span class="n">abshalf</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:=</span>
  <span class="k">calc</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">abs</span> <span class="o">((</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">congr_arg</span> <span class="n">abs</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">of_real_div</span><span class="o">,</span> <span class="n">of_real_bit0</span><span class="o">,</span> <span class="n">of_real_inv</span><span class="o">]</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">abs_of_nonneg</span><span class="o">]</span><span class="bp">;</span> <span class="n">norm_num</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="k">in</span> <span class="o">(</span><span class="n">exp</span> <span class="n">x</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span><span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">lim_const</span> <span class="n">x</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">exp</span><span class="o">,</span> <span class="n">sub_eq_add_neg</span><span class="o">,</span> <span class="n">sub_eq_add_neg</span><span class="o">,</span> <span class="err">←</span> <span class="n">lim_const</span> <span class="mi">1</span><span class="o">,</span>
    <span class="err">←</span> <span class="n">lim_neg</span><span class="o">,</span> <span class="err">←</span> <span class="n">lim_neg</span><span class="o">,</span> <span class="n">lim_add</span><span class="o">,</span> <span class="n">lim_add</span><span class="o">,</span> <span class="err">←</span> <span class="n">lim_abs</span><span class="o">],</span>
  <span class="n">refine</span> <span class="n">real</span><span class="bp">.</span><span class="n">lim_le</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">le_of_exists</span> <span class="bp">⟨</span><span class="mi">3</span><span class="o">,</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">j</span> <span class="n">hj</span><span class="o">,</span> <span class="bp">_</span><span class="o">)</span><span class="bp">⟩</span><span class="o">),</span>
  <span class="k">show</span> <span class="o">(</span><span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">/</span> <span class="n">m</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">/</span> <span class="mi">6</span><span class="o">)),</span>
  <span class="n">exact</span> <span class="k">calc</span> <span class="n">abs</span> <span class="o">((</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="n">j</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">/</span> <span class="n">m</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span>
      <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">))</span> <span class="o">:</span>
    <span class="k">by</span> <span class="n">conv</span> <span class="o">{</span><span class="n">to_lhs</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_add_cancel</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_of_succ_le</span> <span class="n">hj</span><span class="o">),</span> <span class="n">sum_range_succ&#39;</span><span class="o">,</span> <span class="n">sum_range_succ&#39;</span><span class="o">]}</span><span class="bp">;</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">mul_sum</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">abs_mul</span><span class="o">,</span> <span class="n">mul_div_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">]</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span>
    <span class="k">by</span> <span class="n">conv</span> <span class="o">{</span><span class="n">to_lhs</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_sub_succ</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_sub</span> <span class="n">hj</span><span class="o">,</span> <span class="n">sum_range_succ&#39;</span><span class="o">]</span> <span class="o">}</span><span class="bp">;</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">fact</span><span class="o">,</span> <span class="n">bit0</span><span class="o">]</span>
  <span class="bp">...</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">/</span> <span class="mi">6</span><span class="o">)</span> <span class="o">:</span> <span class="n">mul_le_mul_of_nonneg_left</span>
    <span class="o">(</span><span class="k">calc</span> <span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span>
          <span class="bp">≤</span> <span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">))</span> <span class="bp">+</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span>
        <span class="n">abs_add</span> <span class="bp">_</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="bp">=</span> <span class="n">abs</span> <span class="o">(</span><span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">))</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="n">abshalf</span>
      <span class="bp">...</span> <span class="bp">≤</span> <span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">abs</span> <span class="o">(</span><span class="n">x</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">))</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">abv_sum_le_sum_abv</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="bp">≤</span> <span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="mi">1</span> <span class="bp">/</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">sum_le_sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="bp">_</span><span class="o">,</span>
          <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">abs_div</span><span class="o">,</span> <span class="n">is_absolute_value</span><span class="bp">.</span><span class="n">abv_pow</span> <span class="n">abs</span><span class="o">,</span> <span class="err">←</span> <span class="n">of_real_nat_cast</span><span class="o">,</span>
            <span class="n">abs_of_nonneg</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_nonneg</span> <span class="bp">_</span><span class="o">)]</span><span class="bp">;</span>
          <span class="n">refine</span> <span class="o">(</span><span class="n">div_le_div_right</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">fact_pos</span> <span class="bp">_</span><span class="o">)))</span><span class="bp">.</span><span class="mi">2</span>
            <span class="o">(</span><span class="n">pow_le_one</span> <span class="bp">_</span> <span class="o">(</span><span class="n">abs_nonneg</span> <span class="bp">_</span><span class="o">)</span> <span class="n">hx</span><span class="o">)))</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="bp">≤</span> <span class="n">sum</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">6</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="err">^</span> <span class="n">m</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">sum_le_sum</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">hn</span><span class="o">,</span> <span class="k">begin</span>
          <span class="n">clear</span> <span class="n">hn</span><span class="o">,</span>
          <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">bit0</span><span class="o">,</span> <span class="n">bit1</span><span class="o">,</span> <span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">]</span> <span class="o">},</span>
          <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">fact_succ</span><span class="o">,</span> <span class="n">pow_succ&#39;</span><span class="o">,</span> <span class="n">one_div_eq_inv</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="n">mul_inv&#39;</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_assoc</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">6</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)],</span>
            <span class="n">refine</span> <span class="n">mul_le_mul</span> <span class="o">(</span><span class="k">by</span> <span class="n">rwa</span> <span class="n">inv_eq_one_div</span><span class="o">)</span> <span class="bp">_</span>
              <span class="o">(</span><span class="n">inv_nonneg</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_nonneg</span> <span class="bp">_</span><span class="o">))</span>
              <span class="o">(</span><span class="n">mul_nonneg</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="o">(</span><span class="n">pow_nonneg</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="bp">_</span><span class="o">)),</span>
            <span class="n">rw</span> <span class="o">[</span><span class="n">one_div_eq_inv</span><span class="o">],</span>
            <span class="n">refine</span> <span class="o">(</span><span class="n">inv_le_inv</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_pos</span> <span class="bp">_</span><span class="o">))</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span>
              <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_two</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span><span class="bp">.</span><span class="mi">2</span> <span class="n">dec_trivial</span><span class="o">)</span> <span class="o">}</span>
        <span class="kn">end</span><span class="o">)</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">6</span> <span class="bp">*</span> <span class="o">((</span><span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="err">^</span> <span class="o">(</span><span class="n">j</span> <span class="bp">-</span> <span class="mi">3</span><span class="o">))</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">mul_sum</span><span class="o">,</span> <span class="n">geo_series_eq</span><span class="o">]</span><span class="bp">;</span> <span class="n">norm_num</span>
      <span class="bp">...</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">6</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span>
        <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_left</span> <span class="o">((</span><span class="n">div_le_div_right</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span>
          <span class="o">(</span><span class="n">sub_le_self</span> <span class="bp">_</span> <span class="o">(</span><span class="n">pow_nonneg</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="bp">_</span><span class="o">)))</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">))</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">/</span> <span class="mi">6</span> <span class="o">:</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span>
    <span class="o">(</span><span class="n">pow_two_nonneg</span> <span class="o">(</span><span class="n">abs</span> <span class="n">x</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256944):
<p>Oh, you really did the case n=1 directly</p>

#### [ Mario Carneiro (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256959):
<p>I was thinking you would just prove the general case, there is less stuff floating around that way</p>

#### [ Mario Carneiro (Sep 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256986):
<p>well, it's done now, we can revisit later</p>

#### [ Chris Hughes (Sep 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256999):
<p>Not sure what the general case is.</p>

#### [ Mario Carneiro (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257011):
<blockquote>
<p><code>abs (sum k = m,...,infty (x ^ n / n!)) &lt;= (abs a)^m * ((m + 1) / (m! * m))</code></p>
</blockquote>

#### [ Mario Carneiro (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257073):
<p>You can also write <code>exp x - finset.sum ...</code> instead of that tail sum if you prefer</p>

#### [ Chris Hughes (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257083):
<p>That makes way more sense.</p>

#### [ Reid Barton (Sep 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257611):
<p>By the way, how hard is it to get log once we have exp? Specifically how hard is it to show that every nonzero complex number is in the range of exp?</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134258931):
<p>This comes fairly late in the development.</p>
<ul>
<li>First you do the real log function. exp is easily seen to be increasing so you get an inverse by IVT. I can expand on this</li>
<li><code>sin</code> is a bijection from [-pi/2, pi/2] to [-1, 1]. Again, this has subparts</li>
<li>Injectivity of <code>exp</code>: <code>exp x = 1</code> iff <code>x = 2*pi*i*n</code> for some <code>n</code></li>
<li>The complex square root function exists. You can define it as <code>sqrt z = sqrt (abs z) * ((abs z + z) / abs (abs z + z))</code> off the negative real axis</li>
<li>If <code>D</code> is an interval of length 2pi, and <code>y : D</code> is chosen to be a multiple of 2 pi from <code>2 * arcsin (im (sqrt z))</code>, then <code>z = exp (I * y)</code>, which shows surjectivity of the imaginary part</li>
<li>By combining surjectivity on real and imaginary parts and injectivity, you get that <code>exp</code> is bijective in any domain of the form <code>{z | z.im \in D}</code></li>
</ul>

#### [ Chris Hughes (Sep 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264128):
<p>How do you get the bounds on cosine?</p>

#### [ Chris Hughes (Sep 19 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264158):
<p>specifically <code>1/3 &lt; cos 1 &lt; 2 / 3</code> the fact that <code>exp x - x - 1 \le abs x ^ 2 * 3 / 4</code> is only good enough for <code>1/4 \le cos 1 \le 7 / 4</code></p>

#### [ Chris Hughes (Sep 19 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264219):
<p>do you need bounds on sine 1 and use cos^2 + sin^2 = 1</p>

#### [ Mario Carneiro (Sep 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265225):
<p>The claim is that <code>abs (cos x - (1 - x^2 / 2)) &lt; x^2 / 6</code> for <code>x \in (0, 1]</code>. By the <code>m=4</code> case of the tail bound on exp, <code>cos x - (1 - x^2 / 2) = re (exp4 (I*x)) &lt;= abs (exp4 (I*x)) &lt;= x^4 * ((4 + 1) / (4! * 4)) &lt; x^4 / 6 &lt;= x^2 / 6</code>, where <code>exp4</code> is the tail of <code>exp</code> starting at 4.</p>

#### [ Mario Carneiro (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265277):
<p>(sorry! looks like you do need more of the tail bound)</p>

#### [ Mario Carneiro (Sep 19 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265313):
<p>in metamath, each inequality there is a sublemma (or instance of a lemma), probably don't pack it all together since it is independently useful</p>

#### [ Chris Hughes (Sep 20 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308558):
<p>Major progress. The following have now been proved. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how do I get continuous exp from the first one?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">exp_bound</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">)</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">abs</span> <span class="o">(</span><span class="n">exp</span> <span class="n">x</span> <span class="bp">-</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="bp">.</span><span class="n">succ</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">x</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">/</span> <span class="n">m</span><span class="bp">.</span><span class="n">fact</span><span class="o">))</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="n">x</span> <span class="err">^</span> <span class="n">n</span><span class="bp">.</span><span class="n">succ</span> <span class="bp">*</span> <span class="o">(</span><span class="n">n</span><span class="bp">.</span><span class="n">fact</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span><span class="bp">⁻¹</span>

<span class="kn">lemma</span> <span class="n">cos_one_bound</span> <span class="o">:</span> <span class="n">abs&#39;</span> <span class="o">(</span><span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">18</span>
</pre></div>

#### [ Kenny Lau (Sep 20 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308648):
<p>you might want to specialize the <code>n</code> first if you want to prove continuity</p>

#### [ Kenny Lau (Sep 20 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308663):
<p>and you want to prove continuity at 0 first</p>

#### [ Kenny Lau (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308717):
<p>(since exp(y)-exp(x) = exp(x) [exp(y-x)-1])</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308725):
<p>As I mentioned, if you take <code>n = 1</code> then you have <code>abs (exp x - 1) &lt;= abs x</code></p>

#### [ Kenny Lau (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308769):
<p>so combining our statements, <code>|exp(y)-exp(x)| &lt;= exp(x) |y-x|</code></p>

#### [ Kenny Lau (Sep 20 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308802):
<p>so set <code>delta = epsilon/exp(x)</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308914):
<p>wait, isn't the bound off by one? the claim was about <code>sum m=n ... infty (x^m/m!)</code> which should be <code>abs (exp x - (range n).sum (λ m, x ^ m / m.fact))</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308960):
<p>the RHS looks right</p>

#### [ Kenny Lau (Sep 20 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309088):
<p>well n=1 gives <code>|exp(x)-1-x| &lt;= |x|^2</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309323):
<p>I guess the order is right, the constant is a bit off</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309338):
<div class="codehilite"><pre><span></span>lemma exp_bound {x : ℂ} (hx : abs x ≤ 1) {n : ℕ} (hn : 0 &lt; n) :
  abs (exp x - (range n).sum (λ m, x ^ m / m.fact)) ≤ abs x ^ n * (n.succ / (n.fact * n)) := sorry
</pre></div>

#### [ Chris Hughes (Sep 20 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312362):
<p>Does it matter? We have everything we need for pi</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">cos_one_le</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="mi">5</span> <span class="bp">/</span> <span class="mi">9</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">18</span> <span class="o">:</span> <span class="n">sub_le_iff_le_add</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">abs_sub_le_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="n">cos_one_bound</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">/</span> <span class="mi">9</span> <span class="o">:</span> <span class="k">by</span> <span class="n">norm_num</span>

<span class="kn">lemma</span> <span class="n">le_cos_one</span> <span class="o">:</span> <span class="mi">4</span> <span class="bp">/</span> <span class="mi">9</span> <span class="bp">≤</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="mi">4</span> <span class="bp">/</span> <span class="mi">9</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">18</span> <span class="o">:</span> <span class="k">by</span> <span class="n">norm_num</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">1</span> <span class="o">:</span> <span class="n">sub_le_of_sub_le</span> <span class="o">(</span><span class="n">abs_sub_le_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="n">cos_one_bound</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span>

<span class="kn">lemma</span> <span class="n">cos_two_le</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="bp">-</span><span class="mi">31</span> <span class="bp">/</span> <span class="mi">81</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">congr_arg</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">bit0</span><span class="o">])</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="bp">_</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">cos_two_mul</span> <span class="mi">1</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">/</span> <span class="mi">9</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">1</span> <span class="o">:</span>
  <span class="n">sub_le_sub_right</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_left</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">pow_two</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span>
    <span class="n">mul_self_le_mul_self</span> <span class="o">(</span><span class="n">le_trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="n">le_cos_one</span><span class="o">)</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">))</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">31</span> <span class="bp">/</span> <span class="mi">81</span> <span class="o">:</span> <span class="k">by</span> <span class="n">norm_num</span>
</pre></div>

#### [ Patrick Massot (Sep 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312866):
<p>Wonderful! Can you get pi before tomorrow then?</p>

#### [ Chris Hughes (Sep 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312999):
<p>If someone tells me how to turn my inequalities about exp into a proof of continuity. I don't know what the lemma is.</p>

#### [ Patrick Massot (Sep 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313023):
<p>Did you push everything?</p>

#### [ Patrick Massot (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313051):
<p>Doesn't seem so</p>

#### [ Chris Hughes (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313053):
<p>Not yet</p>

#### [ Patrick Massot (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313077):
<p>It would be easier to see what inequalities you have</p>

#### [ Chris Hughes (Sep 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313314):
<p>Just pushing now</p>

#### [ Reid Barton (Sep 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313328):
<p>Do we know that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">C</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{C}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">C</span></span></span></span></span> is a normed group?</p>

#### [ Reid Barton (Sep 20 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313791):
<p>I guess it would be quite easy to add. Then you should be able to use <code>tendsto_iff_norm_tendsto_zero</code> and <code>tendsto_of_tendsto_of_tendsto_of_le_of_le</code> somehow</p>

#### [ Reid Barton (Sep 20 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313820):
<p>or maybe even <code>squeeze_zero</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313883):
<p>There should be a theorem about continuity on metric spaces</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313917):
<p><code>continuous_of_metric</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313943):
<p>oh wait, you just want continuity at zero, that is <code>tendsto_nhds_of_metric</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134314004):
<p>just rewrite <code>dist 0 x</code> to <code>abs x</code> and you should be set with a straight epsilon delta proof</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134314065):
<p>You shouldn't make your constants too precise, it makes the proof harder for norm_num and the gain is not that great. In particular you should weaken the second theorem to <code>cos 2 &lt; 0</code></p>

#### [ Chris Hughes (Sep 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327309):
<p>So I have <code>lemma tendsto_exp_zero_one : tendsto exp (nhds 0) (nhds 1) :=</code></p>

#### [ Chris Hughes (Sep 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327314):
<p>How do I get continuity?</p>

#### [ Kenny Lau (Sep 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327360):
<p>note that exp(x+h) = exp(x) exp(h)</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327365):
<p>do we know that C is a topological ring?</p>

#### [ Chris Hughes (Sep 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327446):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> yes</p>

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327484):
<p><code>\forall x, tendsto (\lambda h, exp x * exp h) (nhds 0) (nhds (exp x * 1))</code></p>

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327497):
<p><code>\forall x, tendsto (\lambda h, exp (x+h)) (nhds 0) (nhds (exp x))</code></p>

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327515):
<p><code>\forall x, tendsto exp (nhds x) (nhds (exp x))</code></p>

#### [ Chris Hughes (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327544):
<p>What lemmas are you applying Kenny?</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327620):
<p>Ah, found it: <code>continuous_mul</code> is what you want</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327646):
<p>to deduce the first of Kenny's statements</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327667):
<p>wait no, <code>tendsto_mul</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327741):
<p>the second one is easy/algebraic, and the third is that lemma that Patrick mentioned</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327920):
<p>Alternatively you could just use continuity of subtraction to avoid mentioning homeos</p>

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327987):
<p>from 2 to 3 can be easily done with epsilon-delta</p>

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327994):
<p>would not recommend epsilon-delta to deduce 1</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328003):
<p>don't listen to kenny, you are done with epsilons now</p>

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328021):
<p>we're in the post-epsilon stage of maths, right</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328141):
<p>if you know <code>tendsto (\lambda h, exp (x+h)) (nhds 0) (nhds (exp x))</code> then if you compose with <code>(\lambda y, y - x)</code> which is continuous then you get <code>tendsto (\lambda y, exp (x+(y - x))) (nhds x) (nhds (exp x))</code></p>

#### [ Chris Hughes (Sep 20 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328347):
<p>My goal is <code>tendsto (λ (x_1 : ℂ), exp x) (nhds 0) (nhds 1)</code> I try <code>apply tendsto_exp_zero_one</code>, which looks like this <code>tendsto_exp_zero_one : tendsto (λ x : ℂ, exp x) (nhds (0 : ℂ)) (nhds (1 : ℂ))</code> and it hangs.</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328427):
<p>use exact</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328505):
<p>apply will go crazy unfolding pis because of a bug</p>

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328583):
<p><code>exact this</code> fails</p>
<div class="codehilite"><pre><span></span><span class="n">x</span> <span class="o">:</span> <span class="n">complex</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span> <span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">complex</span><span class="o">),</span> <span class="n">complex</span><span class="bp">.</span><span class="n">exp</span> <span class="n">x</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nhds</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">metric_space</span><span class="o">))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">has_zero</span><span class="bp">.</span><span class="n">zero</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">has_zero</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nhds</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">metric_space</span><span class="o">))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">has_one</span><span class="o">))</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span> <span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x_1</span> <span class="o">:</span> <span class="n">complex</span><span class="o">),</span> <span class="n">complex</span><span class="bp">.</span><span class="n">exp</span> <span class="n">x</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nhds</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">metric_space</span><span class="o">))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">has_zero</span><span class="bp">.</span><span class="n">zero</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">has_zero</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nhds</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">metric_space</span><span class="o">))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">complex</span> <span class="n">complex</span><span class="bp">.</span><span class="n">has_one</span><span class="o">))</span>
</pre></div>

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328600):
<p>I see the problem.</p>

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328612):
<p>Silly me</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328653):
<p>is that sarcasm? because I don't</p>

#### [ Chris Hughes (Sep 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328719):
<p><code>x_1</code> instead of <code>x</code> on first line</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328864):
<p>by the way, <code>convert</code> is a nice way to diagnose these bugs</p>

#### [ Chris Hughes (Sep 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134329021):
<p>What's the lemma I use for composing with sub</p>

#### [ Chris Hughes (Sep 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134329079):
<p><code>tends.comp</code> d'oh</p>

#### [ Chris Hughes (Sep 20 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330094):
<p>This must be easy surely</p>
<div class="codehilite"><pre><span></span><span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">),</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="mi">0</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Sep 20 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330122):
<p>by the way I suggest you do all your compositions at the start, getting something like <code>tendsto (\lam y, exp x * exp (y - x)) (nhds x) (nhds (exp x * exp (x - x)))</code></p>

#### [ Chris Hughes (Sep 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330209):
<p>I worked that bit out. Do I have to use <code>tendsto_sub</code> and the identity and constant functions?</p>

#### [ Mario Carneiro (Sep 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330229):
<p>yes</p>

#### [ Mario Carneiro (Sep 20 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330252):
<p>that's the easiest way, at least</p>

#### [ Chris Hughes (Sep 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331002):
<p>exp is continuous is now a fact.</p>

#### [ Kenny Lau (Sep 20 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331114):
<p>how much time do we still have?</p>

#### [ Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331370):
<p>Here it's 9:27pm</p>

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331423):
<p>So 8:27pm in London</p>

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331429):
<p>So we have 12 hours</p>

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331434):
<p>roughly</p>

#### [ Patrick Massot (Sep 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331458):
<p>Who's going to tell Kevin tomorrow? <span class="user-mention" data-user-id="112680">@Johan Commelin</span> ?</p>

#### [ Chris Hughes (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332215):
<p>How do you prove <code>continuous real.sin</code> from <code>continuous complex.sin</code>?</p>

#### [ Mario Carneiro (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332221):
<p>continuity of real part</p>

#### [ Mario Carneiro (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332228):
<p>and continuity of real injection</p>

#### [ Mario Carneiro (Sep 20 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332274):
<p>How did you define <code>real.sin</code>?</p>

#### [ Patrick Massot (Sep 20 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332761):
<p><a href="https://github.com/leanprover-community/mathlib/blob/4c670fc338c3e6cdff8c1f01e03f1279fd3926bd/data/complex/exponential.lean#L349" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/4c670fc338c3e6cdff8c1f01e03f1279fd3926bd/data/complex/exponential.lean#L349">https://github.com/leanprover-community/mathlib/blob/4c670fc338c3e6cdff8c1f01e03f1279fd3926bd/data/complex/exponential.lean#L349</a></p>

#### [ Chris Hughes (Sep 20 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332776):
<p>(complex.sin x).re</p>

#### [ Patrick Massot (Sep 20 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332789):
<p>So continuity should indeed follow as Mario wrote</p>

#### [ Chris Hughes (Sep 20 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332800):
<p>I couldn't find <code>continuous_re</code></p>

#### [ Patrick Massot (Sep 20 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332815):
<p>Do you want us to prove it, or did you do it already?</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134333423):
<p>I think there is a theorem that <code>re</code> is a contracting map, which is enough to prove continuity</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134333500):
<p><code>abs_re_le_abs</code></p>

#### [ Chris Hughes (Sep 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334686):
<p>I managed to work it out. I thought there was some simple proof without deltas, but deltas is really short anyway.</p>

#### [ Patrick Massot (Sep 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334711):
<p>How far are you from pi then?</p>

#### [ Chris Hughes (Sep 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334779):
<p>More or less there. Just have to apply IVT which I have already proved.</p>

#### [ Patrick Massot (Sep 20 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334986):
<p>So, who's writing to Kevin tomorrow?</p>

#### [ Chris Hughes (Sep 20 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134335942):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pi</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">exists_cos_eq_zero</span>
</pre></div>

#### [ Kenny Lau (Sep 20 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336002):
<p>then pi can be 3*3.14...?</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336024):
<p>have you proven that <code>cos (pi/2) = 0</code>?</p>

#### [ Chris Hughes (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336148):
<p><code>lemma exists_cos_eq_zero : ∃ x, 1 ≤ x ∧ x ≤ 2 ∧ cos x = 0 </code> <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336153):
<p>fair enough</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336162):
<p>also <code>sin (pi/2) = 1</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336172):
<p>the rest should be easy</p>

#### [ Kenny Lau (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336183):
<p>well sin(pi/2)=1 implies cos(pi/2)=0...</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336248):
<p>but it looks like he proved <code>cos (pi/2) = 0</code>, which only implies <code>sin(pi/2) = +- 1</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336301):
<p>Metamath uses the lemma that <code>sin x &gt; 0</code> on <code>(0, 2]</code> by double angle formulas on what you already have</p>

#### [ Chris Hughes (Sep 20 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336386):
<p>I'm sure that's all quite easily doable.</p>

#### [ Mario Carneiro (Sep 20 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336400):
<p>yes, it's mostly smooth sailing at this point</p>

#### [ Chris Hughes (Sep 20 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336439):
<p>I pushed.</p>

#### [ Kenny Lau (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337086):
<p>I'm afraid it's now 05:03 AM in Hong Kong and I must leave now...</p>

#### [ Kenny Lau (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337111):
<p>although I will wake up 4 hours later</p>

#### [ Mario Carneiro (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337124):
<p>ooh, you are 12 hours away from me</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343929):
<p>I've been 50 for about 10 minutes</p>

#### [ Chris Hughes (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343951):
<p>Happy Birthday!</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343958):
<p>Holey Moley we have pi!</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343964):
<p>I am so happy!</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134344081):
<p>I need to go to bed!</p>


{% endraw %}
