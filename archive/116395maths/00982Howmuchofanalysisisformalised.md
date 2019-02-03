---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00982Howmuchofanalysisisformalised.html
---

## Stream: [maths](index.html)
### Topic: [How much of analysis is formalised?](00982Howmuchofanalysisisformalised.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728233):
<p>How much of analysis is formalised right now? I'm guessing basic calculus -- limits, single-variable stuff, Riemann integrals -- are formalised. What about multivariable, complex analysis (e.g. the complex-analytic proof of the fundamental theorem of algebra), fractional calculus, variational calculus, etc.?</p>

#### [ Chris Hughes (Oct 13 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728461):
<p>Integrals are there, but very new, only arrived this week, No derivatives at all as far as I know. Complex analysis is currently very limited, no FTA, look through <code>analysis/complex</code> and you'll get the idea.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728573):
<p>Just simple Riemann integrals or are Lesbegue, etc. also there?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728621):
<p>Oh, ok, Lesbegue seems to be there -- analysis/lesbegue_measure.lean</p>

#### [ Chris Hughes (Oct 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728795):
<p>I haven't looked through it too much, but there's something called <code>lintegral</code> which I'm guessing is lebesgue integral, and something called <code>integral</code> and I don't know what that is.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135729077):
<p>What is the situation regarding differentiation <span class="user-mention" data-user-id="110031">@Patrick Massot</span> ? I am somehow always confused about whether someone is going to set up a theory of calculus for real-valued functions of one real variable or whether this is somehow all going to be subsumed by some massive multivariable possibly infinite-dimensional normed spaces because this was the correct generality that the theory should be developed in so that's how it has to work.</p>

#### [ Johannes Hölzl (Oct 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735421):
<p>hm, I see this is a little bit confusing <code>lintegral</code> is actually the lower Lebesgue integral (there might be later a upper Lebesgue integral). It is not the Lebesgue integral into the reals, but it is necessary to define it. My intention is to use this integral to define norms on measurable functions and then define the Bochner integral (which is an integral for functions into a separable Banch space, while the Lebesgue integral is integrating functions into reals)</p>

#### [ Johannes Hölzl (Oct 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735470):
<p>AFAIK, <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> wants now to start on multivariate analysis, so also derivative of functions etc.</p>

#### [ Jeremy Avigad (Oct 13 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735875):
<p>Yes, I have just gotten started. I'll push to <code>leanprover-community</code> as soon as there is anything worth seeing.</p>

#### [ Patrick Massot (Oct 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135742603):
<blockquote>
<p>What is the situation regarding differentiation Patrick Massot? I am somehow always confused about whether someone is going to set up a theory of calculus for real-valued functions of one real variable or whether this is somehow all going to be subsumed by some massive multivariable possibly infinite-dimensional normed spaces because this was the correct generality that the theory should be developed in so that's how it has to work.</p>
</blockquote>
<p>My hope was to do the possibly infinite dimensional stuff and deduce the 1-dimensional case, but we'll see what Jeremy does</p>

#### [ Kevin Buzzard (Oct 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135777542):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> I think it's worth pointing out the analogy here with the theory of polynomials. Johannes Hoelzl made a big library for polynomials in an arbitrary number of variables, and after that one could argue that "Lean had polynomials". However there were lots of basic facts about polynomials in _one_ variable which we did not have (many of which did not generalise to polynomials in an arbitrary number of variables) and eventually Chris decided to lead the development of a theory of polynomials in one variable <a href="https://github.com/leanprover/mathlib/blob/master/data/polynomial.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/polynomial.lean">https://github.com/leanprover/mathlib/blob/master/data/polynomial.lean</a> which turned out to be useful for my personal work on perfectoid spaces and also indirectly started to guide Mario towards how the theory of modules over a ring should actually be implemented in Lean (which has been an interesting open question for months). </p>
<p>In short -- don't let the fact that people are considering writing some huge library of multivariable calculus stop you developing the basic theory of calculus in one variable. Here are a bunch of things, many of which I believe we don't have, and which will be useful for doing M1M1 in Lean: definition of derivative of a function from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> and proof that it is linear (i.e. <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><mo>+</mo><mi>g</mi><msup><mo>)</mo><mo mathvariant="normal">′</mo></msup><mo>=</mo><msup><mi>f</mi><mo mathvariant="normal">′</mo></msup><mo>+</mo><msup><mi>g</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">(f+g)'=f'+g'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> etc), chain rule, product rule, quotient rule, the derivative of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding="application/x-tex">e^x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span></span></span></span></span></span></span></span> is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding="application/x-tex">e^x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span></span></span></span></span></span></span></span> and the derivative of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\cos(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span>. These last few things are maybe not even going to be covered by this general grand plan by experts to develop a theory of multivariable everything, but we're back to the same point: what would a _mathematician_ think when we tell them that we cannot prove that the derivative of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\cos(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span>? <span class="user-mention" data-user-id="110044">@Chris Hughes</span> am I right in thinking that we still cannot do this in Lean?</p>

#### [ Chris Hughes (Oct 14 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778093):
<p>We can't state it in Lean.</p>

#### [ Kenny Lau (Oct 14 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778240):
<p><code>forall x, tendsto (fun h, (sin(x+h)-sin(x))/h) (nbhd 0) (nbhd (cos x))</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778349):
<p>the division should go over the subtraction</p>

#### [ Kenny Lau (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778352):
<p>edited</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778353):
<p>also it's not true, because that function has a jump discontinuity at 0</p>

#### [ Kenny Lau (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778354):
<p>but it's true because 0/0=0</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778359):
<p>right, 0 not cos x</p>

#### [ Kenny Lau (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778360):
<p>ah</p>

#### [ Kenny Lau (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778362):
<p><code>forall x, tendsto (fun h, (sin(x+h)-sin(x)-h*cos(x))/h) (nbhd 0) (nbhd 0)</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778363):
<p>still 0</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778364):
<p>oh wait</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778417):
<p>okay that should work</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778419):
<p>at least, it's a true fact, it looks quite different from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>sin</mi><mo mathvariant="normal">′</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>cos</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin'(x) = \cos(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.809652em;"></span><span class="strut bottom" style="height:1.059652em;vertical-align:-0.25em;"></span><span class="base"><span class="mop"><span class="mop">sin</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.809652em;"><span style="top:-3.12076em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span></p>

#### [ Kenny Lau (Oct 14 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778459):
<p>say that to Patrick Massot</p>

#### [ Patrick Massot (Oct 14 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778661):
<p>What?</p>

#### [ Kenny Lau (Oct 14 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778668):
<p>that's how you defined complex derivative right</p>

#### [ Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778732):
<p>I'm not sure what you are talking about, but the definition of complex derivatives in kbb comes from Tom Hales</p>

#### [ Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778734):
<p>not from me</p>

#### [ Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778739):
<p>But it looked ok. Is the discussion around what happens at h=0?</p>

#### [ Kenny Lau (Oct 14 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778793):
<p>the discussion is that it looks quite different from sin'(x) = cos(x)</p>

#### [ Kevin Buzzard (Oct 14 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779619):
<p>it's one unfold away from sin' = cos</p>

#### [ Kevin Buzzard (Oct 14 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779665):
<p>so we are back to Chris' point.</p>

#### [ Kenny Lau (Oct 14 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779701):
<p>it isn't because this isn't defining a function</p>

#### [ Kevin Buzzard (Oct 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779776):
<p>oh, fair point.</p>

#### [ Sebastien Gouezel (Oct 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135784063):
<p>As far as I can see, there is no typeclass for compact spaces, right? (I have the impression that <code>compact</code> is only a predicate on subsets of topological spaces). Is there any problem with</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">compact_space</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">compact_univ</span> <span class="o">:</span> <span class="n">compact</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span>
</pre></div>


<p>?</p>

#### [ Reid Barton (Oct 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135784684):
<p>I think I suggested an identical definition on zulip a week or two ago. Haven't had much time for actual Lean recently though.</p>

#### [ Johannes Hölzl (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135792687):
<p><code>compact_space</code> is surely helpful</p>


{% endraw %}
