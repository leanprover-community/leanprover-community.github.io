---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04864Trigonometricfunctions.html
---

## Stream: [new members](index.html)
### Topic: [Trigonometric functions](04864Trigonometricfunctions.html)

---


{% raw %}
#### [ Sebastian Zimmer (Sep 29 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883106):
<p>I'd like to learn how to use lean, by attempting to prove something nontrivial. Looking through the potential projects wiki page, trigonometric functions seems like the most promising (in that I can confidently prove the basic identies, facts about pi, etc. from first principles).</p>
<p>I don't have much experience with theorem provers (I've used idris and coq in the past, but not terribly successfully).</p>
<p>The wiki links to some progress on the exponential function <a href="https://github.com/leanprover/mathlib/pull/41/commits/6b1f85b149329be0c9084081668230c2d622f387" target="_blank" title="https://github.com/leanprover/mathlib/pull/41/commits/6b1f85b149329be0c9084081668230c2d622f387">https://github.com/leanprover/mathlib/pull/41/commits/6b1f85b149329be0c9084081668230c2d622f387</a><br>
but I can't tell if anything came of that.</p>
<ul>
<li>Does this seem feasible?</li>
<li>What is the state of power series / exponential functions / trigonometric functions in mathlib?</li>
<li>What would I build on top of? Are there other things in development that would be helpful to me?</li>
</ul>

#### [ Kevin Buzzard (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883199):
<p>There was a whole bunch of stuff formalised recently. I think we got exp, log, pi, sin, cos, tan</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883200):
<p>and double angle formulae etc. All of this is about a week old</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883209):
<p>Apparently we have cos(pi/2)=0 but we can only deduce that sin(pi/2)=+-1 ;-)</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883524):
<p>Is that available in a public repo somewhere?</p>

#### [ Chris Hughes (Sep 29 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883587):
<p><a href="https://github.com/leanprover-community/mathlib/tree/exp" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/exp">https://github.com/leanprover-community/mathlib/tree/exp</a></p>

#### [ Sebastian Zimmer (Sep 29 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883592):
<p>awesome thanks</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884169):
<p>It's surprising how much  you can prove without calculus</p>

#### [ Johan Commelin (Sep 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884522):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> When will you PR <code>exp</code>? Is there some list of things you still want to add to it?</p>

#### [ Chris Hughes (Sep 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884529):
<p>I still need sin(p/2)=1, and the inverses of all 14 functions</p>

#### [ Chris Hughes (Sep 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884530):
<p>After that I'll PR it.</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887265):
<p>Just out of interest <span class="user-mention" data-user-id="110044">@Chris Hughes</span> , how are you planning on proving sin(pi / 2) &gt; 0? I can't see a way of doing it without a bit of calculus.</p>

#### [ Chris Hughes (Sep 29 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887449):
<p>I think I should be able to prove some bounds on it in a similar way to the bounds on cos. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> told me the method <br>
sin (2*x) is positive for all 0&lt;x&lt;=1 because sin x and cos x are<br>
x - x^3/3 &lt; sin x &lt; x and 1 - 2/3 * x^2 &lt; cos x &lt; 1 - x^2/3 on (0, 1] by infinite series bounds</p>

#### [ Kevin Buzzard (Sep 29 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887684):
<p>Chris I mentioned the general result from which this follows to you the other day. If you have a sequence a1,a2,a3,... with the signs of the terms alternating, and the terms tending to zero, then not only does the sum of the sequence converge, but the sum is &lt;= all the odd partial sums (if a1&gt;0) and &gt;= all the even ones.</p>

#### [ Kevin Buzzard (Sep 29 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887725):
<p>This is a fabulous tool for getting bounds for anything. You don't even need 0&lt;x&lt;=1, it will work for any real x because after sufficiently many terms they will start alternating in sign and decreasing</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887734):
<p>that gives you x - x^3/3 &lt; sin(x) but  I don't see why 1 - 2/3 x^2 &lt; cos(x)</p>

#### [ Kevin Buzzard (Sep 29 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887785):
<p>1-x^2/2&lt;cos(x) for 0&lt;x&lt;1 by this result</p>

#### [ Kevin Buzzard (Sep 29 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887786):
<p>which is stronger</p>

#### [ Kevin Buzzard (Sep 29 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887838):
<p>these tricks tell you that the partial sums are good approximations to sin and cos for x small, and because you know where the roots are you can start proving goofy things like sum 1/n^2 = pi^2/6 like this, but the details are messy</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887849):
<p>Can we show that e.g. sin has only one root close to \pi without calculus?</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887890):
<p>actually I can see how to do it using some identities that are already proven</p>

#### [ Chris Hughes (Sep 30 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134914917):
<blockquote>
<p>Chris I mentioned the general result from which this follows to you the other day. If you have a sequence a1,a2,a3,... with the signs of the terms alternating, and the terms tending to zero, then not only does the sum of the sequence converge, but the sum is &lt;= all the odd partial sums (if a1&gt;0) and &gt;= all the even ones.</p>
</blockquote>
<p>But it's only less than the partial sums after the sequence starts decreasing right. Which complicates proofs a lot without <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>≤</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">x \le 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">≤</span><span class="mord mathrm">1</span></span></span></span></p>

#### [ Kevin Buzzard (Sep 30 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134915402):
<p>yes exactly. So e.g. for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>4</mn></mrow><annotation encoding="application/x-tex">0\le x \le4</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">≤</span><span class="mord mathit">x</span><span class="mrel">≤</span><span class="mord mathrm">4</span></span></span></span> maybe you only know that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>−</mo><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>≤</mo><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>≤</mo><mi>x</mi><mo>−</mo><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">x-\frac{x^3}{3!} \le \sin(x)\le x-\frac{x^3}{3!}+\frac{x^5}{5!}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:1.01792em;"></span><span class="strut bottom" style="height:1.36292em;vertical-align:-0.345em;"></span><span class="base"><span class="mord mathit">x</span><span class="mbin">−</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.01792em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">3</span><span class="mclose mtight">!</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathit mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mrel">≤</span><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">≤</span><span class="mord mathit">x</span><span class="mbin">−</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.01792em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">3</span><span class="mclose mtight">!</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathit mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mbin">+</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.01792em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">5</span><span class="mclose mtight">!</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathit mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">5</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>. But if people want to know things like cos(pi) then this approach will work.</p>

#### [ Chris Hughes (Sep 30 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134933965):
<p>I now have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\sin(x)&gt;0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">&gt;</span><span class="mord mathrm">0</span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mi>π</mi></mrow><annotation encoding="application/x-tex">0&lt;x&lt;\pi</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.68354em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">&lt;</span><span class="mord mathit">x</span><span class="mrel">&lt;</span><span class="mord mathit" style="margin-right:0.03588em;">π</span></span></span></span>, and therefore <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mrow><mo fence="true">(</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo fence="true">)</mo></mrow><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">\sin\left(\frac{\pi}{2}\right)=1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.85em;"></span><span class="strut bottom" style="height:1.20001em;vertical-align:-0.35001em;"></span><span class="base"><span class="mop">sin</span><span class="minner"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.695392em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span></p>

#### [ Sebastian Zimmer (Sep 30 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134934076):
<p>Are you going to do <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn><mspace width="0.277778em"></mspace><mo>⟺</mo><mspace width="0.277778em"></mspace><mi>x</mi><mo>=</mo><mi>k</mi><mo>∗</mo><mi>π</mi></mrow><annotation encoding="application/x-tex">\sin(x) = 0 \iff x = k * \pi</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">0</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟺</span></span><span class="mord mathit"><span class="mspace thickspace"></span><span class="mord mathit">x</span></span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03148em;">k</span><span class="mbin">∗</span><span class="mord mathit" style="margin-right:0.03588em;">π</span></span></span></span>?</p>

#### [ Sebastian Zimmer (Sep 30 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134934115):
<p>Probably would be easy from what you have already done</p>

#### [ Kevin Buzzard (Sep 30 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935322):
<p>One can probably prove that if sin (t)=0 then sin (x+2t)=sin(x) I guess? And the periods of a function are a subgroup of the reals so there's a pure thought approach to the result -- pi is in and no positive real less than pi, so it's the multiples of pi</p>

#### [ Patrick Massot (Sep 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935371):
<p>I don't thing mathlib has the classification of subgroups of reals</p>

#### [ Kevin Buzzard (Sep 30 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935390):
<p>This one isn't hard though, write any x in the group as n*pi +r with 0&lt;=r&lt;pi and then sin(r)=0 so by Chris's result r=0</p>

#### [ Mario Carneiro (Sep 30 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134936122):
<p>yes, this is basically how I sketched the proof that 2&lt;pi &lt; 4 with the alternate definition of pi as the least positive zero of sin. The addition formula of sin shows that zeros of sin are closed under Z module operations</p>

#### [ Chris Hughes (Oct 01 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134983929):
<p>Today I did arctan, arcsin and arccos, for reals, and proved that they are two-sided inverses within the appropriate intervals. Not sure how to do the same for complexes.</p>

#### [ Mario Carneiro (Oct 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134984026):
<p>Do you have complex log?</p>

#### [ Mario Carneiro (Oct 01 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134984071):
<p>How far in <a href="#narrow/stream/141825-kbb/subject/sine.20and.20cosine.20and.20pi/near/134258931" title="#narrow/stream/141825-kbb/subject/sine.20and.20cosine.20and.20pi/near/134258931">https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/subject/sine.20and.20cosine.20and.20pi/near/134258931</a> have you got?</p>

#### [ Chris Hughes (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985180):
<p><code>complex.log</code> is my next target. I think that can just be done with <code>real.log</code> and <code>real.arctan</code></p>

#### [ Mario Carneiro (Oct 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985360):
<p>hm, I guess you are right... I didn't have inverse trig when I did log</p>

#### [ Mario Carneiro (Oct 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985447):
<p>still, you want the injectivity statement anyway (<code>exp z = 0 &lt;-&gt; z/2 pi i</code> is an integer)</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000763):
<p>Wait -- what is <code>complex.log</code>? It'll be discontinuous, right? <code>log</code> is multi-valued (except at zero, where it's 37).</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000872):
<p>Geometrically, the map <code>exp</code> from the complexes to themselves is an infinite sheeted unramified cover from the complex numbers to the non-zero complex numbers. Unramified means that given any non-zero complex number in the target, you can draw a tiny disc around it and the pre-image of that tiny disc in the source is lots of copies of the tiny disc (in this case countably infinitely many, and a Z-torsor). What information does a presumably non-computable log give you about this picture? Isn't the correct definition of "log" just literally the subset of the complexes whose exp is the thing you're trying to take the log of? <code>complex.log</code> is ugly. Is it actually used in pure mathematics?</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000922):
<p>It could map to the product of the reals and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow><mi mathvariant="normal">/</mi><mn>2</mn><mi>π</mi><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}/2\pi\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span><span class="mord mathrm">/</span><span class="mord mathrm">2</span><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span></p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000942):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>log</mi><mo>(</mo><mi>r</mi><msup><mi>e</mi><mrow><mi>i</mi><mi>θ</mi></mrow></msup><mo>)</mo><mo>=</mo><mo>(</mo><mi>log</mi><mo>(</mo><mi>r</mi><mo>)</mo><mo separator="true">,</mo><mi>θ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\log(re^{i\theta})=(\log(r),\theta)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:1.099108em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.02778em;">θ</span></span></span></span></span></span></span></span></span><span class="mclose">)</span><span class="mrel">=</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.02778em;">θ</span><span class="mclose">)</span></span></span></span>.</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001106):
<blockquote>
<p>complex.log is ugly. Is it actually used in pure mathematics?</p>
</blockquote>
<p>Yes, absolutely yes. Trying to make sense of "multivalued functions" is a hundred times harder than just picking a branch cut and being consistent about it</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001214):
<p>My proposed mangling of this function: <code>log x</code> is the unique value with <code>exp (log x) = x</code> and <code>-pi &lt; Im (log x) &lt;= pi</code>, with <code>log 0 = 0</code></p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001264):
<p>You guys think about maths in such an ugly way. I painted a beautiful picture and you just rip a branch out of it.</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001271):
<p>I'll have you know mathematicians invented branch cuts</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001283):
<p>And yet actually Lean taught me a much more beautiful proof of the Hilbert Basis Theorem.</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001285):
<p>Maybe I just don't like the definitions.</p>

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001292):
<p>I've been grumpy about 1/0 since day 1.</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001585):
<p>I don't understand why mathematicians have such a hard time coming to grips with the fact that not all functions are continuous</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001652):
<p>and when faced with evidence to the contrary they assume that points of discontinuity aren't in the domain</p>

#### [ Simon Hudon (Oct 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001667):
<blockquote>
<p>I've been grumpy about 1/0 since day 1.</p>
</blockquote>
<p>I'm not too fond of that either. PVS has a nice answer to that, you always have to prove that the denominator is <code>\ne 0</code>. I'm wondering if we could do that nicely with notation like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="n">x</span> <span class="bp">`</span> <span class="bp">/</span> <span class="bp">`</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">div&#39;</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">)</span>
</pre></div>


<p>This way, <code>x / y</code> would only be type correct if one of your assumption is <code>y ≠ 0</code></p>

#### [ Mario Carneiro (Oct 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001673):
<p>0^0 is another example</p>

#### [ Mario Carneiro (Oct 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001742):
<p>partial functions are possible but a bad idea in dtt</p>

#### [ Kevin Buzzard (Oct 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002497):
<p>I'm hapoy not to open this can of worms again. My point is simply that it is still a surprise to me that CS guys think about mathematics in different ways to mathematicians. I really do not ever run into discontinuous functions in my work, and if you think I do (given that I run into division but am careful never to divide by zero) then in some sense I regard this as evidence that you're thinking about it wrongly, but conversely I think Mario's point is far more relevant in this context than what I think beautiful maths looks like. We are thinking about the same things but in some sense the mathematician seems to carry around some extra nuance, or perhaps some unwritten instructions on how to use the function properly and how to avoid the sharp edges. "Warning -- if you're dividing by zero you're probably doing it wrong".</p>

#### [ Mario Carneiro (Oct 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002787):
<p>I think that's fair. Essentially, myself and other logicians / computer scientists are calling the mathematicians out when they talk about functions that don't meet the chapter 1 definition</p>

#### [ Mario Carneiro (Oct 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002812):
<p>mathematical aesthetics decrees that everything interesting is continuous, and so this causes some cognitive dissonance in the mind of the mathematician that requires some additional equivocation on these setups when pressed</p>

#### [ Mario Carneiro (Oct 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002859):
<p>but as soon as you stop pressing they go back to treating <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>log</mi></mrow><annotation encoding="application/x-tex">\log</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span></span></span></span> like a plain function</p>

#### [ Mario Carneiro (Oct 02 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002984):
<p>I think that there absolutely are other construals of this function as a Riemann surface or smooth manifold, but when it gets down to plain calculation you want to be able to pick a locally coherent section of the function and know what's going on there</p>

#### [ Mario Carneiro (Oct 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135003054):
<p>Note that from this "principal log", you can still have your manifold by rotating the reference frame so that your point of interest is on the real line</p>

#### [ Patrick Massot (Oct 02 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135017970):
<p>Is there any point in pushing this low-tech trigonometry further? I agree that having <code>pi</code>, and real trigonometry functions is nice for teaching. But who will teach complex logarithm without the basics of holomorphic functions? If someone does Cauchy theory then we can properly state that holomorphic functions have primitive on simply connected open subsets of their domain of definition. Then<code>1/z</code> will have a primitive function on any simply connected open set not containing zero, and we'll be able to easily relate those primitive to exponential.</p>

#### [ Patrick Massot (Oct 02 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135018034):
<p>Of course we could also do Riemann surfaces if someone prioritizes this, but I don't see happening soon</p>

#### [ Kevin Buzzard (Oct 02 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135018266):
<p>My personal stance on this is very clear: there is an essentially random amount of this stuff which I personally wanted to see in Lean, which is the stuff which shows up in my elementary course. For example <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mrow><mi>i</mi><mi>θ</mi></mrow></msup><mo>=</mo><mi>cos</mi><mo>(</mo><mi>θ</mi><mo>)</mo><mo>+</mo><mi>i</mi><mi>sin</mi><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">e^{i\theta}=\cos(\theta)+i\sin(\theta)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:1.099108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.02778em;">θ</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">θ</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathit">i</span><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">θ</span><span class="mclose">)</span></span></span></span>. But now we have all of this, because Chris took my course last year and has now covered everything, so I am no longer pushing for any more of this stuff. I just needed enough to be able to formalise the questions I ask the students. Maybe in the future we will need more but I am not pressing for any of it right now -- I feel that we have enough to look respectable to mathematicians.</p>

#### [ Reid Barton (Oct 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135027840):
<p>One of the standard proofs of the fundamental theorem of algebra requires as input the fact that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>z</mi><mi>n</mi></msup><mo>=</mo><mi>a</mi></mrow><annotation encoding="application/x-tex">z^n = a</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathit">a</span></span></span></span> has a root for any complex <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">a</span></span></span></span>, which needs about this level of trig. Or to prove <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><mo>↦</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>π</mi><mi>i</mi><mi>t</mi></mrow></msup></mrow><annotation encoding="application/x-tex">t \mapsto e^{2\pi i t}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:0.835664em;vertical-align:-0.011em;"></span><span class="base"><span class="mord mathit">t</span><span class="mrel">↦</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mord mathit mtight">i</span><span class="mord mathit mtight">t</span></span></span></span></span></span></span></span></span></span></span></span> is a local homeomorphism from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> to the unit circle is similar (which also implies FTA via covering space theory).</p>

#### [ Patrick Massot (Oct 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135027892):
<p>Indeed it would be nice to have FTA</p>

#### [ Kevin Buzzard (Oct 02 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028042):
<p>This is one of those theorems for which there are about 20 proofs, isn't it. Before embarking on one in Lean I guess it's important to see how it is proved in other provers and what other options there are. The proof I saw used complex analysis and integration around a big circle if I remember correctly. But maybe I saw some completely different one years later which went via a real-analytic proof that every polynomial over the reals factored into terms of degree at most 2.</p>

#### [ Reid Barton (Oct 02 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028274):
<p>metamath uses <a href="https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus" target="_blank" title="https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus">this proof</a> as far as I can tell</p>

#### [ Reid Barton (Oct 02 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028386):
<p>I know this because someone on my Twitch stream mentioned that they were trying to prove FTA in Lean, working from the metamath proof. Kevin I am guessing it is a student of yours based but I'm not sure</p>

#### [ Patrick Massot (Oct 02 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028550):
<p>I saw dozens of proofs of this theorem. Of course all the nice ones are more or less openly based on elementary algebraic topology. But I also saw a proof using only algebra and existence of roots for odd degree real polynomials (easy consequence of limits and intermediate value theorem)</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049069):
<p>The metamath proof of FTA is my favorite (of course, I wrote it!). It is based on <a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra#Topological_proofs" target="_blank" title="https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra#Topological_proofs">this wikipedia proof</a>. The main topological prerequisite is the extreme value theorem: A large closed ball about zero in C is compact, so <code>abs (p z)</code> takes a minimum value somewhere. The rest is just reasoning about finite sums</p>

#### [ Kenny Lau (Oct 02 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049190):
<p>I've seen a short proof using a clever contour integral</p>

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049241):
<p>but I recall it has cosine so maybe it isn't suitable</p>

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049243):
<p>wait, which thread am I on</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049247):
<p>it also has contour integrals</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049251):
<p>which we don't have</p>

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049252):
<p>yes, I mean the proof I saw uses one contour integral</p>

#### [ Kenny Lau (Oct 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049275):
<p>actually I think the proof from Galois theory may have some potential</p>

#### [ Chris Hughes (Oct 03 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135127077):
<p>PRed <a href="https://github.com/leanprover/mathlib/pull/386" target="_blank" title="https://github.com/leanprover/mathlib/pull/386">https://github.com/leanprover/mathlib/pull/386</a>. I stopped at complex log. No inverse complex trig yet. Not sure whether a highbrow method is better for that.</p>

#### [ Mario Carneiro (Oct 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129185):
<p>The metamath definitions<br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>arcsin</mi><mi>z</mi><mo>=</mo><mo>−</mo><mi>i</mi><mi>log</mi><mo>(</mo><mi>i</mi><mi>z</mi><mo>+</mo><mo>(</mo><mn>1</mn><mo>−</mo><msup><mi>z</mi><mn>2</mn></msup><msup><mo>)</mo><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">\arcsin z = -i\log(iz + (1-z^2)^{1/2})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">arcsin</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mrel">=</span><span class="mord">−</span><span class="mord mathit">i</span><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mbin">−</span><span class="mord"><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span><br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>arccos</mi><mi>z</mi><mo>=</mo><mi>π</mi><mi mathvariant="normal">/</mi><mn>2</mn><mo>−</mo><mi>arcsin</mi><mi>z</mi></mrow><annotation encoding="application/x-tex">\arccos z = \pi/2-\arcsin z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">arccos</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mord mathrm">/</span><span class="mord mathrm">2</span><span class="mbin">−</span><span class="mop">arcsin</span><span class="mord mathit" style="margin-right:0.04398em;">z</span></span></span></span><br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>arctan</mi><mi>z</mi><mo>=</mo><mfrac><mi>i</mi><mn>2</mn></mfrac><mrow><mo fence="true">[</mo><mi>log</mi><mo>(</mo><mn>1</mn><mo>−</mo><mi>i</mi><mi>z</mi><mo>)</mo><mo>−</mo><mi>log</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>i</mi><mi>z</mi><mo>)</mo><mo fence="true">]</mo></mrow></mrow><annotation encoding="application/x-tex">\arctan z = \frac i2\left[\log(1-iz) - \log(1 + iz)\right]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.855664em;"></span><span class="strut bottom" style="height:1.200664em;vertical-align:-0.345em;"></span><span class="base"><span class="mop">arctan</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mrel">=</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.855664em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="minner"><span class="mopen delimcenter" style="top:0em;">[</span><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mbin">−</span><span class="mord mathit">i</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mclose">)</span><span class="mbin">−</span><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mbin">+</span><span class="mord mathit">i</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mclose">)</span><span class="mclose delimcenter" style="top:0em;">]</span></span></span></span></span><br>
make sure to put the branch cuts in the right places</p>

#### [ Kevin Buzzard (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129267):
<p>Chris is writing a calculator emulator.</p>

#### [ Mario Carneiro (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129334):
<p>(I don't see a sqrt in the first expression where the conspicuous space is, but pretend there is one)</p>

#### [ Kevin Buzzard (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129600):
<p>I've been fixing that on this forum by using <code>^{1/2}</code>. <code>\sqrt</code> never works for me.</p>

#### [ Reid Barton (Oct 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129648):
<p>Do we have enough now to show that every complex number can be written in the form <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi><msup><mi>e</mi><mrow><mi>i</mi><mi>θ</mi></mrow></msup></mrow><annotation encoding="application/x-tex">re^{i \theta}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.02778em;">θ</span></span></span></span></span></span></span></span></span></span></span></span>?</p>

#### [ Kevin Buzzard (Oct 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129757):
<p>This might boil down to showing that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">x^2+y^2=1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.008548em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span> then there exists <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>θ</mi></mrow><annotation encoding="application/x-tex">\theta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">θ</span></span></span></span> such that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mi>cos</mi><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">x=\cos(\theta)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">θ</span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi><mo>=</mo><mi>sin</mi><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">y=\sin(\theta)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mrel">=</span><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">θ</span><span class="mclose">)</span></span></span></span>. If only we'd defined <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi></mrow><annotation encoding="application/x-tex">\sin</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.66786em;"></span><span class="strut bottom" style="height:0.66786em;vertical-align:0em;"></span><span class="base"><span class="mop">sin</span></span></span></span> as opposite over hypotenuse :-)</p>

#### [ Patrick Massot (Oct 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129868):
<blockquote>
<p>If only we'd defined <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi></mrow><annotation encoding="application/x-tex">\sin</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.66786em;"></span><span class="strut bottom" style="height:0.66786em;vertical-align:0em;"></span><span class="base"><span class="mop">sin</span></span></span></span> as opposite over hypotenuse :-)</p>
</blockquote>
<p>Finally, someone having common sense!</p>

#### [ Patrick Massot (Oct 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129943):
<p>Now stop kidding: where is our sheaf theory?</p>

#### [ Kevin Buzzard (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129979):
<p>Hey, maybe <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mi>t</mi><mi>a</mi><mi>n</mi><mo>(</mo><mi>y</mi><mi mathvariant="normal">/</mi><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">atan(y/x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">a</span><span class="mord mathit">t</span><span class="mord mathit">a</span><span class="mord mathit">n</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathrm">/</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> (possibly plus <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>π</mi></mrow><annotation encoding="application/x-tex">\pi</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">π</span></span></span></span>) can be proved to work.</p>

#### [ Chris Hughes (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129997):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I didn't prove that directly, but we have <code>arg</code> and <code>cos (arg x) = x.re / abs x</code> and similar for sin, so it should be easy.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135130561):
<p>If we prove the product rule then mathlib might be able to pass A-level! (UK maths exam for 18 year olds)</p>

#### [ Patrick Massot (Oct 03 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135130643):
<p>We sort of have it in the holomorphic case <a href="https://github.com/semorrison/kbb/blob/master/src/holomorphic_functions.lean#L117" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/holomorphic_functions.lean#L117">https://github.com/semorrison/kbb/blob/master/src/holomorphic_functions.lean#L117</a></p>

#### [ David Michael Roberts (Oct 04 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135141531):
<blockquote>
<p>It's surprising how much  you can prove without calculus</p>
</blockquote>
<p>it might be worth formalising some of this, if possible: <a href="https://ncatlab.org/toddtrimble/published/Characterization+of+sine" target="_blank" title="https://ncatlab.org/toddtrimble/published/Characterization+of+sine">https://ncatlab.org/toddtrimble/published/Characterization+of+sine</a></p>

#### [ Mario Carneiro (Oct 04 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135141911):
<blockquote>
<p>and we get to invoke the theory of entire analytic functions.</p>
</blockquote>
<p>more like the entire theory of analytic functions</p>

#### [ Kevin Buzzard (Oct 04 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155372):
<p>I never quite know whether it's worth formalising "gimmicks". I mean, I've taught this stuff, and never once have I used or seen the use of this linked result -- the characterisation. It's very cute for sure. But does it deserve to be in mathlib? I genuinely don't know.</p>

#### [ Patrick Massot (Oct 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155563):
<p>I never heard of those characterizations before following the link yesterday</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155649):
<p>Presumably there are many math results worth formalizing that don't deserve to be in mathlib. I think a well-documented formalization of the above characterization of sine could potentially make a fun tutorial to the new functions that Chris is PRing.</p>

#### [ Kevin Buzzard (Oct 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135160643):
<p>I think that this is a really good way of looking at it.</p>

#### [ Chris Hughes (Oct 27 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/136599443):
<p>(deleted)</p>


{% endraw %}
