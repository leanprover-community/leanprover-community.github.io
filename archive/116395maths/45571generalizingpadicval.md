---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45571generalizingpadicval.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [generalizing padic_val](https://leanprover-community.github.io/archive/116395maths/45571generalizingpadicval.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Nov 19 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952749):
<p>In my proof of FTA, I need the highest power of a polynomial that divides another polynomial. Should <code>padic_val</code> be generalized to do this. What's the correct generality for this function?</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952773):
<p>You should be able to say this in any comm semiring (where dvd is defined)</p>

#### [ Johan Commelin (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952824):
<p>But maybe UFD's are the right level of generality</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952829):
<p>no, some of this you want to be able to state even without ufd</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952832):
<p>for example you can use it to define a ufd</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952846):
<p>plus that's a hell of a proof obligation for using the notation</p>

#### [ Kevin Buzzard (Nov 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952992):
<p>The theory really takes off in a ring where the notions of prime and irreducible elements coincide; then for r an irreducible element of a comm ring with this property, the "r-adic valuation" is very well-behaved (e.g. it's additive). Even for a ring like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mo>(</mo><mo>−</mo><mn>5</mn><msup><mo>)</mo><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mo>]</mo><mo>:</mo><mo>=</mo><mo>{</mo><mspace width="0.16667em"></mspace><mi>a</mi><mo>+</mo><mi>b</mi><mo>(</mo><mo>−</mo><mn>5</mn><msup><mo>)</mo><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mspace width="0.16667em"></mspace><mo>∣</mo><mspace width="0.16667em"></mspace><mi>a</mi><mo separator="true">,</mo><mi>b</mi><mo>∈</mo><mrow><mi mathvariant="double-struck">Z</mi></mrow><mspace width="0.16667em"></mspace><mo>}</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[(-5)^{1/2}]:=\{\,a+b(-5)^{1/2}\,\mid\,a,b\in\mathbb{Z}\,\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">5</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mclose">]</span><span class="mrel">:</span><span class="mrel">=</span><span class="mopen">{</span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit">a</span></span><span class="mbin">+</span><span class="mord mathit">b</span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">5</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mrel"><span class="mspace thinspace"></span><span class="mrel">∣</span></span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit">a</span></span><span class="mpunct">,</span><span class="mord mathit">b</span><span class="mrel">∈</span><span class="mord"><span class="mord mathbb">Z</span></span><span class="mclose"><span class="mspace thinspace"></span><span class="mclose">}</span></span></span></span></span> the 2-adic valuation of both <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn><mo>±</mo><mo>(</mo><mo>−</mo><mn>5</mn><msup><mo>)</mo><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding="application/x-tex">1\pm (-5)^{1/2}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">1</span><span class="mbin">±</span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">5</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span></span> is 0 but the 2-adic valuation of $(1+(-5)^{1/2})(1-(-5)^{1/2})$ is 1, and 2 is irreducible.</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953038):
<p>I don't think it necessarily has to be a valuation like in the padics</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953047):
<p>you can say 2 is the highest power of 4 that divides 48</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953057):
<p>and you have to worry about infinity being a possible answer regardless, because of 0</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953061):
<p>so at that point it's really valid as long as dvd and power are defined</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953104):
<p>We do rely on the property a^m | b -&gt; a^n | b when m &gt;= n, but that is true in any monoid</p>

#### [ Kevin Buzzard (Nov 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953109):
<p>Right. I don't know the answer to Chris' question of the generality it should be defined in Lean, I was just explaining the boundaries of where it started to be useful in commutative algebra.</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953118):
<p>I wish dvd was defined on monoids instead of semirings</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953170):
<p>although you could argue about whether commutative matters</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953175):
<p>I can't imagine ever needing this function for a non prime element and it won't have any nice properties, but over a UFD this function is used all the time by mathematicians</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953196):
<p>One interesting thing you can do with this function is define the class of rings where it is always finite for nonzeros</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953202):
<p>It's like an archimedean property</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953329):
<p>Here is a silly example using a non-prime: the count of 10 inside a number n is its number of trailing zeros</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953477):
<p>Maybe Noetherian rings with no nilpotents have this property. Nilpotents will always screw you up, and Noetherian is a finiteness hypothesis which typically makes intuitive things like this true</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953504):
<p>Maybe it follows from Krull. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> ?</p>

#### [ Kenny Lau (Nov 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953572):
<p>how should I know</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953639):
<p>Krull needs proper ideals. Aah. So for a unit it's always infinite</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953662):
<p>You didn't do krull yet Kenny? It's in AM. .</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953687):
<p>oh right, ignoring units</p>

#### [ Chris Hughes (Nov 19 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967315):
<p>If I define it over a <code>comm_semiring</code> it's going to be noncomputable. Is that the right approach?</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967633):
<p>ah, that's true. How about a <code>decidable_rel dvd</code> assumption?</p>

#### [ Chris Hughes (Nov 19 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967655):
<p>Still not computable. I have to decide whether it's finite or not.</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967755):
<p>right, this puts it in the same class as order-finding</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967784):
<p>how is it being represented in the first place? are you using with_top nat?</p>

#### [ Chris Hughes (Nov 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967826):
<p>I haven't decided. Probably default to zero since zero's not being used for anything else.</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967880):
<p>well, zero has a meaning here (no powers of p in the number)</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967886):
<p>is that a problem?</p>

#### [ Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967893):
<p>Sorry yeah.</p>

#### [ Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967897):
<p>Might be a problem</p>

#### [ Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967910):
<p>It just means <code>p_adic_val_eq_zero_iff</code> has an extra assumption</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967949):
<p>although for general comm semirings that assumption is kind of complicated, right?</p>

#### [ Chris Hughes (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967953):
<p>Currently it defaults to zero.</p>

#### [ Chris Hughes (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967965):
<p>Yes.</p>

#### [ Chris Hughes (Nov 19 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968031):
<p>But maybe in a UFD or something it's simpler, so there'll have to be a UFD version of the lemma.</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968056):
<p>or a proposition asserting finiteness</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968081):
<p>perhaps the <code>roption nat</code> version works best here</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968107):
<p>since that way you get the proposition for free, encoded in the <code>roption</code>, and it's computable</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968192):
<p>but we will want to specialize the function to rings where we can prove finiteness</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968197):
<p>like padics</p>

#### [ Chris Hughes (Nov 19 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968220):
<p>You still have to decide if somethings a unit or not.</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968273):
<p>With the <code>roption</code> version, you can just do the naive search and it's computable</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968281):
<p>because of <code>pfun.fix</code></p>

#### [ Mario Carneiro (Nov 19 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968380):
<p>maybe <code>nat.rfind</code> is easier to use</p>

#### [ Chris Hughes (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968382):
<p>It's "computable" but you still have to give a proof to actually compute it. I'm not a fan of worsening ease of proof for the sake of computability.</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968409):
<p>my point is that here the mathematics and computability aspects coincide</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968415):
<p>we need an extra "infinity" value, and roption gives us that</p>

#### [ Mario Carneiro (Nov 19 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968471):
<p>and as far as giving a proof, that is exactly what we can do in nice rings like <code>int</code></p>

#### [ Mario Carneiro (Nov 19 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968524):
<p>(actually, in the VM you can cheat and evaluate any <code>roption</code>, even if it is an infinite search)</p>

#### [ Chris Hughes (Nov 21 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115154):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> One downside of generalizing padic val, is that now for integers it will return an <code>int</code> rather than a <code>nat</code>, which I know can be very annoying. Is this a good reason to have two definitions?</p>

#### [ Mario Carneiro (Nov 21 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115253):
<p>How so? If it's defined based on monoid.pow then it should give a nat</p>

#### [ Chris Hughes (Nov 21 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115990):
<p>You're right. I'm being stupid.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148127500):
<p>In maths you would have valuations taking on natural values on the "integers" and valuations taking integer values on the "rationals", and both would be used (in some generality).</p>

#### [ Chris Hughes (Nov 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130014):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Is the statement that every non-zero non unit has a finite padic val equivalent to UFD. It seems to be provided there aren't any elements which can be divided by infinitely many distinct primes, and I'm not sure if that's possible or not.</p>

#### [ Johan Commelin (Nov 21 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130128):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> In <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mi mathvariant="normal">√</mi><mrow><mo>−</mo><mn>5</mn></mrow><mo>]</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[\surd{-5}]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8em;"></span><span class="strut bottom" style="height:1.05em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mord mathrm">√</span><span class="mord"><span class="mord">−</span><span class="mord mathrm">5</span></span><span class="mclose">]</span></span></span></span> you have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mn>1</mn><mo>−</mo><mi mathvariant="normal">√</mi><mrow><mo>−</mo><mn>5</mn></mrow><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi mathvariant="normal">√</mi><mrow><mo>−</mo><mn>5</mn></mrow><mo>)</mo><mo>=</mo><mn>6</mn><mo>=</mo><mn>2</mn><mo>⋅</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">(1 - \surd{-5})(1 + \surd{-5}) = 6 = 2 \cdot 3</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8em;"></span><span class="strut bottom" style="height:1.05em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mbin">−</span><span class="mord mathrm">√</span><span class="mord"><span class="mord">−</span><span class="mord mathrm">5</span></span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mbin">+</span><span class="mord mathrm">√</span><span class="mord"><span class="mord">−</span><span class="mord mathrm">5</span></span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">6</span><span class="mrel">=</span><span class="mord mathrm">2</span><span class="mbin">⋅</span><span class="mord mathrm">3</span></span></span></span>. So that is not a UFD.</p>

#### [ Johan Commelin (Nov 21 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130239):
<p>But I think it satisfies your other requirement.</p>

#### [ Chris Hughes (Nov 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148141439):
<p>Situation like that happening didn't occur to me.</p>

#### [ Chris Hughes (Nov 22 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148154102):
<p>Some of the statements become a bit ugly with <code>roption</code>. Is there a good way around this?</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">mul</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">ha0</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hb0</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">get</span> <span class="o">(</span><span class="n">padic_val</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">finite_of_prime</span> <span class="n">hp</span> <span class="n">ha0</span><span class="o">)</span> <span class="bp">+</span>
  <span class="n">get</span> <span class="o">(</span><span class="n">padic_val</span> <span class="n">p</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">finite_of_prime</span> <span class="n">hp</span> <span class="n">hb0</span><span class="o">)</span> <span class="bp">=</span>
  <span class="n">get</span> <span class="o">(</span><span class="n">padic_val</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">))</span> <span class="o">(</span><span class="n">finite_of_prime</span> <span class="n">hp</span> <span class="o">(</span><span class="n">mul_ne_zero</span> <span class="n">ha0</span> <span class="n">hb0</span><span class="o">))</span>
</pre></div>

#### [ Johan Commelin (Nov 22 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148158928):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> What is your current definition of <code>padic_val</code>? Is there someplace we can read your latest code?<br>
I think the idea was that you don't even assume that <code>p</code> is prime... (I didn't even know that we had prime elements in arbitrary rings already). If you want to make an assumption on the element, it is probably most natural to assume that it is irreducible. Also, maybe the name should now also be generalised to <code>adic_val</code>?</p>

#### [ Mario Carneiro (Nov 22 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159267):
<p>I called it "prime count" in metamath, although it wasn't defined only on primes</p>

#### [ Mario Carneiro (Nov 22 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159273):
<p>it's not really the padic valuation since usually that involves a reciprocal</p>

#### [ Mario Carneiro (Nov 22 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159287):
<p>how about <code>divisibility</code>?</p>

#### [ Kevin Buzzard (Nov 22 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148161166):
<p>Re the <code>get</code>s -- can you just define addition on <code>roption</code>? I don't quite know what I'm talking about here. Re</p>
<blockquote>
<p>it's not really the padic valuation since usually that involves a reciprocal</p>
</blockquote>
<p>even though the term is used for both the multiplicative and additive versions of this idea, I think "the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span>-adic  valuation" usually refers to the map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">v_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.716668em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>p</mi><mo>)</mo><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">v_p(p)=1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">p</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span>, where as "the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span>-adic norm" is the one with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∣</mi><mi>p</mi><msub><mi mathvariant="normal">∣</mi><mi>p</mi></msub><mo>=</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>p</mi></mrow><annotation encoding="application/x-tex">|p|_{p}=1/p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord mathrm">∣</span><span class="mord mathit">p</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">p</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit">p</span></span></span></span>. Sadly, in perfectoid land, the norm is referred to as a "valuation" :-(</p>

#### [ Chris Hughes (Nov 22 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148171739):
<p>The current definition is </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">padic_val</span> <span class="o">[</span><span class="n">comm_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_rel</span> <span class="o">((</span><span class="err">∣</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">roption</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="bp">⟨∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="bp">¬</span><span class="n">a</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="err">∣</span> <span class="n">b</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="n">h</span><span class="bp">⟩</span>
</pre></div>

#### [ Chris Hughes (Nov 22 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148172800):
<p>I'll probably change the name at some point.</p>

#### [ Chris Hughes (Nov 23 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225756):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Are you in favour of making a version of <code>with_top</code> with <code>roption</code> instead of <code>option</code>, with all the order and algebra on it? It would make sense for <code>padic_val</code>, but also order of elements of infinite groups.</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225784):
<p>maybe specialized to <code>enat</code>?</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225838):
<p>that particular structure seems useful, not so sure about generally with-topping a set</p>

#### [ Chris Hughes (Nov 23 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225854):
<p>Okay sure.</p>

#### [ Chris Hughes (Nov 23 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148231085):
<p>I can't do <code>inf</code> computably for the lattice on enat. Should I leave it out?</p>


{% endraw %}
