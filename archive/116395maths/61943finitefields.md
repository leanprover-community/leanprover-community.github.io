---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61943finitefields.html
---

## Stream: [maths](index.html)
### Topic: [finite fields](61943finitefields.html)

---


{% raw %}
#### [ Joey van Langen (Jan 09 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730425):
<p>I'm going to do some works concerning finite fields. (number of elements, existence and uniqueness)<br>
Can anyone tell me if the following things exist for lean in mathlib or somewhere else and where I can find them?<br>
Integers modulo a prime, prime subfields, ring isomorphisms?</p>

#### [ Rob Lewis (Jan 09 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730801):
<p>Integers mod a prime are at least instantiated as a field: <a href="https://github.com/leanprover/mathlib/blob/master/data/zmod/basic.lean#L313" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/zmod/basic.lean#L313">https://github.com/leanprover/mathlib/blob/master/data/zmod/basic.lean#L313</a></p>

#### [ Rob Lewis (Jan 09 2019 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730956):
<p>Others will probably know more about your other questions. (<span class="user-mention" data-user-id="110064">@Kenny Lau</span> ?)</p>

#### [ Kenny Lau (Jan 09 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731006):
<p>ik ben aan het bezoeken in de stedelijk museum :p</p>

#### [ Joey van Langen (Jan 09 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731019):
<p>Integers modulo p is a nice start</p>

#### [ Rob Lewis (Jan 09 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731107):
<p>I'm glad someone is taking my suggestion to relax this afternoon!</p>

#### [ Joey van Langen (Jan 09 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731112):
<p>Do isomorphisms exist in any context? I can only find them for types</p>

#### [ Kenny Lau (Jan 09 2019 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731465):
<p>use hott!</p>

#### [ Joey van Langen (Jan 09 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731624):
<p>what do you mean by use hott?</p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732681):
<p>he's just trolling. He says "use something other than Lean"</p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732787):
<p>But I guess the answer to your question is that in general most objects don't have isomorphism between those objects already defined in Lean.</p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732821):
<p>You are more likely to find morphisms though, so you can define isomorphisms without too much pain. I guess morphisms of rings will be there somewhere.</p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732935):
<p>Some students at Imperial have done some work on splitting fields, but I don't know if it's public. What is your proposal for defining a finite field? Usually the definition I give is "splitting field of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>X</mi><msup><mi>p</mi><mi>n</mi></msup></msup><mo>−</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">X^{p^n}-X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.87998em;"></span><span class="strut bottom" style="height:0.96331em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.87998em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathit mtight">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7385428571428572em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">F</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{F}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">F</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span>, but I don't think Lean has splitting fields, at least not publically.</p>

#### [ Joey van Langen (Jan 09 2019 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733013):
<p>I'm going to use the definition as a splitting field, by using the splitting field stuff currently in the community repo</p>

#### [ Joey van Langen (Jan 09 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733317):
<p>I will also use the material there concerning algebras as it will give me the tools to realize any finite field as a vector space over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">F</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{F}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">F</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span></p>

#### [ Joey van Langen (Jan 09 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733332):
<p>How do you put latex in these messages?</p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733420):
<p><code>$$\mathbb{F}_p$$</code></p>

#### [ Kevin Buzzard (Jan 09 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733467):
<p>Doesn't always work, for example \sqrt doesn't seem to work</p>

#### [ Joey van Langen (Jan 11 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154923261):
<p>So I have been doing some work on the finite fields with the help of <span class="user-mention" data-user-id="198529">@Casper Putz</span>  for the past couple of days.<br>
We are now close to proving that every finite field has p^n elements with p a prime number.<br>
Most effort was spent proving some simple results which we couldn't find anywhere,<br>
such as the specification of the prime ideals and maximal ideals of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span> and proving that the zero ideal in a field is in fact maximal.<br>
Would people be interested in seeing these results added to mathlib separately? They seem quite useful</p>

#### [ Chris Hughes (Jan 11 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924258):
<p>Yes</p>

#### [ Joey van Langen (Jan 11 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924456):
<p>Any suggestions of where to put that stuff?</p>

#### [ Johan Commelin (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924479):
<p>Do you guys have push access to <a href="https://github.com/leanprover-community/mathlib/" target="_blank" title="https://github.com/leanprover-community/mathlib/">https://github.com/leanprover-community/mathlib/</a> ?</p>

#### [ Joey van Langen (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924488):
<p>For example should the explicit specification of the prime ideals of the integers be put with ideals, with the integers or a separate file entirely</p>

#### [ Johan Commelin (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924492):
<p>If so, put it on a branch <code>finite_fields</code> in that repo.</p>

#### [ Johan Commelin (Jan 11 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924550):
<p>Aaah, I'm always bad at deciding what should go in which file.</p>

#### [ Joey van Langen (Jan 11 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924557):
<blockquote>
<p>Do you guys have push access to <a href="https://github.com/leanprover-community/mathlib/" target="_blank" title="https://github.com/leanprover-community/mathlib/">https://github.com/leanprover-community/mathlib/</a> ?</p>
</blockquote>
<p>We don't have access to the leanprover-community yet. Would be nice to have</p>

#### [ Joey van Langen (Jan 11 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924578):
<p>We're still working on it on my github, but after some cleanup that would probably be the best place to put it</p>

#### [ Chris Hughes (Jan 11 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924590):
<p>It basically depends on imports. Probably ideals imports everything you need, so it should probably go there.</p>

#### [ Johan Commelin (Jan 11 2019 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154926308):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Could you please give <span class="user-mention" data-user-id="143810">@Joey van Langen</span> push access on community mathlib? He's a PhD student of Sander Dahmen.</p>


{% endraw %}
