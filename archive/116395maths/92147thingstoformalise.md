---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/92147thingstoformalise.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [things to formalise](https://leanprover-community.github.io/archive/116395maths/92147thingstoformalise.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Aug 07 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056409):
<p>Dear all, I've dabbled with Lean about a year ago. I worked through _theorem proving with lean_ but I didn't go much beyond that. I would like to formalise some easy undergraduate maths just to get back in to it. Any recommendations? I was thinking of doing just some basic groups, ring theory or linear algebra. Last time I looked at Lean they didn't have a formalisation of the reals. Is that still the case? If the reals have been formalised then perhaps doing some simple real analysis. What active existing libraries should I look at for this kind of thing? I am aware of Xena and the official lean library repo.</p>

#### [ Patrick Massot (Aug 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056440):
<p><a href="https://github.com/leanprover/mathlib/" target="_blank" title="https://github.com/leanprover/mathlib/">https://github.com/leanprover/mathlib/</a></p>

#### [ Patrick Massot (Aug 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056445):
<p>is the main place</p>

#### [ Edward Ayers (Aug 07 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056659):
<p>thanks. I now realise I should have put this in <a class="stream" data-stream-id="113489" href="/#narrow/stream/113489-new-members">#new members</a></p>

#### [ Patrick Massot (Aug 07 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056737):
<p>see also <a href="https://www.youtube.com/watch?v=5tS4j_A1ZvU" target="_blank" title="https://www.youtube.com/watch?v=5tS4j_A1ZvU">https://www.youtube.com/watch?v=5tS4j_A1ZvU</a></p>
<div class="youtube-video message_inline_image"><a data-id="5tS4j_A1ZvU" href="https://www.youtube.com/watch?v=5tS4j_A1ZvU" target="_blank" title="https://www.youtube.com/watch?v=5tS4j_A1ZvU"><img src="https://i.ytimg.com/vi/5tS4j_A1ZvU/default.jpg"></a></div>

#### [ Kevin Buzzard (Aug 07 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057164):
<p>I hear from my undergrads that they are one lemma shy of proving det(AB)=det(A)det(B)</p>

#### [ Kevin Buzzard (Aug 07 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057204):
<p>There is still no definition of the derivative of a function so no chain rule or product rule</p>

#### [ Kevin Buzzard (Aug 07 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057291):
<p>There is still no proof that a power series is continuous within its radius of convergence which is the main holdup for defining pi</p>

#### [ Patrick Massot (Aug 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057313):
<p>The chain rule is waiting for the norms PR</p>

#### [ Kevin Buzzard (Aug 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057343):
<p>What is the problem with the norms PR?</p>

#### [ Patrick Massot (Aug 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057674):
<p>Mario and Johannes want to work on it</p>

#### [ Patrick Massot (Aug 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057680):
<p>that's all I know</p>

#### [ Edward Ayers (Aug 07 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065103):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> can you point me to the relevant files in mathlib for the power series proof please?</p>

#### [ Johan Commelin (Aug 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065196):
<p>I don't think power series are in mathlib.</p>

#### [ Johan Commelin (Aug 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065209):
<p>So most likely there is no particular file to point to.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065405):
<p>Hmm. Did <span class="user-mention" data-user-id="110044">@Chris Hughes</span> 's work on the exponential function get accepted yet?</p>

#### [ Patrick Massot (Aug 07 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065515):
<p>no. I think it tries to become the most venerable PR in mathlib</p>

#### [ Kevin Buzzard (Aug 07 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065602):
<p>We are really bad at basic analysis. When Patrick says that the chain rule will come after normed spaces, he means the correct general chain rule for functions <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">R</mi><mi>a</mi></msup><mo>→</mo><msup><mi mathvariant="double-struck">R</mi><mi>b</mi></msup></mrow><annotation encoding="application/x-tex">\mathbb{R}^a \to\mathbb{R}^b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">a</span></span></span></span></span></span></span></span><span class="mrel">→</span><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span></span></span></span> but there's some hold-up with normed spaces that I'm not clear about. Johan might be right -- there might not even be a basic theory of power series in mathlib, although Chris must have done something because I'm pretty sure he defined <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>↦</mo><msup><mi>e</mi><mi>x</mi></msup><mo>:</mo><mrow><mi mathvariant="double-struck">C</mi></mrow><mo>→</mo><mrow><mi mathvariant="double-struck">C</mi></mrow></mrow><annotation encoding="application/x-tex">x\mapsto e^x : \mathbb{C}\to\mathbb{C}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.69989em;vertical-align:-0.011em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">↦</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span></span></span></span></span><span class="mrel">:</span><span class="mord"><span class="mord mathbb">C</span></span><span class="mrel">→</span><span class="mord"><span class="mord mathbb">C</span></span></span></span></span>. There was some hold-up with that PR as well -- I think that Mario and Johannes had different opinions about it and for a while at least we were just stuck in an impasse.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065666):
<p>Oh! Looking at the comments, it seems that people were concerned that the PR did not use enough filters :-)</p>

#### [ Patrick Massot (Aug 07 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065875):
<p>Come on Kevin. I mean functions between normed spaces, not  <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">R</mi><mi>a</mi></msup><mo>→</mo><msup><mi mathvariant="double-struck">R</mi><mi>b</mi></msup></mrow><annotation encoding="application/x-tex">\mathbb{R}^a \to\mathbb{R}^b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">a</span></span></span></span></span></span></span></span><span class="mrel">→</span><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span></span></span></span>. And I don't mean finite dimensional</p>

#### [ Kevin Buzzard (Aug 07 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131066937):
<blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> can you point me to the relevant files in mathlib for the power series proof please?</p>
</blockquote>
<p><code>data/real/cau_seq.lean</code> and <code>data/real/basic.lean</code> in mathlib are what seem to be the state of the art for sequences. I am not even sure that there is a theory of infinite sums in mathlib, although the definition of a convergent infinite sum (that the finite sums converge) could easily be put into mathlib; the thing is that the moment you put this in, you have to prove a whole bunch of lemmas. Over at the xena project we are a bit less fussy than mathlib, you can look at <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/chris_hughes_various/exponential" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/chris_hughes_various/exponential">https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/chris_hughes_various/exponential</a> to see some theorems about limits which aren't written in the language of filters and a whole bunch of unofficial theorems like sum of a geometric series written in what might not be the maximal generality.</p>

#### [ Patrick Massot (Aug 07 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131066961):
<p>GT III.5</p>

#### [ Patrick Massot (Aug 07 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131067009):
<p>That's how people in the arithmetic and algebraic geometry group talk in Orsay. Except they rather start with AC (yes they refer to the French version too)</p>


{% endraw %}
