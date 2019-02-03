---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27607rationalsthatareactuallyintegers.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rationals that are actually integers](https://leanprover-community.github.io/archive/113488general/27607rationalsthatareactuallyintegers.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 08 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122581):
<p>By some elaborate method I have defined a polynomial with coefficients in <code>rat</code>. Now there is a math theorem (which I hope to turn into a Lean theorem) that says that my polynomial actually has coefficients in <code>int</code>. But this is not at all clear from the definition. What is the best way to turn my polynomial into something with integral coefficients?<br>
(For reference, my actual use case with mv_polynomials can be found here: <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215</a>)<br>
Here is a baby case version of this phenomenon:<br>
Define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><mi mathvariant="normal">/</mi><mn>7</mn></mrow><annotation encoding="application/x-tex">x = {7 \choose 4}/7</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8951079999999999em;"></span><span class="strut bottom" style="height:1.245118em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mord"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8951079999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">4</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">7</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span><span class="mord mathrm">/</span><span class="mord mathrm">7</span></span></span></span>. A priori this is a rational number. But because <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>7</mn></mrow><annotation encoding="application/x-tex">7</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.64444em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">7</span></span></span></span> is prime, it turns out that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> is an integer. This can be turned into Lean, so that we have some <code>x : rat</code>. Now I could do <code>define y := x.num</code>. And then try to prove that <code>(y : rat) = x</code>.<br>
Is this the best way to go about this problem? How would this scale to (mv_)polynomials?</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122654):
<p>I guess you have to insert the maths somewhere. I think your question is asking how to insert the maths. Maybe the answer depends on the maths that needs to be inserted.</p>

#### [ Johan Commelin (Aug 08 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122794):
<p>Right. That might very well be true. In maths-maths there would be just one theorem. "Look, this polynomial actually has <code>int</code> coeffients." In Lean-maths I guess there will be 6 stupid ways, and 1 clever way...</p>

#### [ Johan Commelin (Aug 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122901):
<p>So maybe the clever way depends on the math that needs to be inserted. But so far I've usually seen that there is a CS-reason for choosing a particular method. And then the maths that needs to be inserted has to be pushed into the right form.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122937):
<p>At the end of the day you have some object defined over Q (e.g. a polynomial or something) and you need to prove that there's some object defined over Z which coerces into it. Now of course _if you know the theorem is true_, then for every q in Q you could let z be floor(q) or ceil(q) or numerator(q) or whatever. But you'll still have to prove that \u z = q, and my guess is that the best choice of z will depend on what your proof that q is actually an integer will be.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131122974):
<p>What is the proof, by the way? I've not looked at the maths in your code yet...</p>

#### [ Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123019):
<p>That is one argument. The other is that you later on want to use <code>z</code>.</p>

#### [ Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123045):
<p>And that might be more important then getting a convenient form for the proof of <code>\u z = q</code>.</p>

#### [ Johan Commelin (Aug 08 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123050):
<p>There is no proof yet.</p>

#### [ Johan Commelin (Aug 08 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123085):
<p>The proof that I've seen (in Serre's "Local fields") is not trivial. It will need quite some extra work to formalise it.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123187):
<p>My gut feeling is that the best strategy is to figure out what the maths strategy is first. I think that's a more important question than asking about the endgame.</p>

#### [ Johan Commelin (Aug 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131123317):
<p>Ok. Then I'll have to do a bit of homework first (-;</p>

#### [ Simon Hudon (Aug 08 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129857):
<p>If I had to try, I would try to not step through the rationals. I would use integer division and prove that 7 divides <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\binom{7}{4}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8951079999999999em;"></span><span class="strut bottom" style="height:1.245118em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8951079999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">4</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">7</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> for later consumption (i.e. if you need to multiply x by 7 and prove that it lands back on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\binom{7}{4}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8951079999999999em;"></span><span class="strut bottom" style="height:1.245118em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8951079999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">4</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">7</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span>).</p>

#### [ Simon Hudon (Aug 08 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129914):
<p>(do you use a <code>\begin{array} ...</code> for the choice operator?)</p>

#### [ Kenny Lau (Aug 08 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131129971):
<p>you mean <code>\binom</code>?</p>

#### [ Simon Hudon (Aug 08 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131130176):
<p>Yes indeed, thanks</p>

#### [ Johan Commelin (Aug 09 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131148931):
<p>Alternative: <code>{7 \choose 4}</code>.</p>

#### [ Johan Commelin (Aug 09 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131148978):
<p>About your suggestion: In the baby case I agree that it is possible to avoid the rationals. But with my polynomial, I don't see how to do this.</p>

#### [ Simon Hudon (Aug 09 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131150412):
<p>Can you show me why that isn't possible? I would have thought that using something like <code>↑(choose p q ÷ 7)</code> wouldn't pose a problem in a context with rational numbers.</p>

#### [ Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151838):
<p>Simon, if you look at <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L215</a> you see that I take some polynomial <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Φ</mi></mrow><annotation encoding="application/x-tex">\Phi</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">Φ</span></span></span></span> with integral coefficients, and I build another (sequence of) polynomial <code>witt_structure_int \Phi</code> with integer coefficients.</p>

#### [ Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151844):
<p>But the construction goes via the rationals.</p>

#### [ Johan Commelin (Aug 09 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151851):
<p>I first define <code>witt_structure_rat</code> in terms of <code>X_in_terms_of_W</code>. And those latter polynomials have honest rational coefficients.</p>

#### [ Johan Commelin (Aug 09 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rationals%20that%20are%20actually%20integers/near/131151897):
<p>There might be an entirely different way of defining <code>witt_structure_int</code>, but I don't know this.</p>


{% endraw %}
