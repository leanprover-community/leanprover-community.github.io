---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46077ordinals.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [ordinals](https://leanprover-community.github.io/archive/116395maths/46077ordinals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Oct 04 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135205944):
<p>If I am interested in sequences indexed by <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mspace width="0.16667em"></mspace><mi>α</mi><mo>∣</mo><mi>α</mi><mo>≤</mo><mi>γ</mi><mspace width="0.16667em"></mspace><mo>}</mo></mrow><annotation encoding="application/x-tex">\{\,\alpha \mid \alpha \le \gamma\,\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit" style="margin-right:0.0037em;">α</span></span><span class="mrel">∣</span><span class="mord mathit" style="margin-right:0.0037em;">α</span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.05556em;">γ</span><span class="mclose"><span class="mspace thinspace"></span><span class="mclose">}</span></span></span></span></span> for varying ordinals <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>γ</mi></mrow><annotation encoding="application/x-tex">\gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05556em;">γ</span></span></span></span>, is it likely to be more convenient to just work with sequences indexed by arbitrary well-ordered sets?<br>
The problem I found is that if you just write down <code>{ \a // \a \le \g }</code>, it lives in the wrong universe.</p>

#### [ Reid Barton (Oct 04 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206295):
<p>I think the alternative is to use <code>quot.out</code> to turn an ordinal into a well-ordered set of that order type, where in math I'd just use the set of smaller ordinals.</p>

#### [ Reid Barton (Oct 04 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206562):
<p>But if I use <code>quot.out</code> then I basically get an arbitrary well-ordered set anyways, so I might as well just work with an arbitrary well-ordered set from the start, I guess.</p>

#### [ Johannes Hölzl (Oct 04 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206599):
<p>Oh yes, I would expect that its far easier assume that <code>γ</code> is a type with well-order. And use the elements of the type as indices.</p>

#### [ Kenny Lau (Oct 04 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206662):
<p>I wrote some code a month ago</p>

#### [ Reid Barton (Oct 04 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206675):
<p>And if I use the variable name <code>γ</code>, then everyone is happy :)</p>

#### [ Kenny Lau (Oct 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206697):
<p>I uploaded them <a href="https://github.com/kckennylau/Lean/blob/master/zfc_ordinals.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/zfc_ordinals.lean">here</a>.</p>

#### [ Reid Barton (Oct 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206710):
<p>Oh interesting, will take a look</p>

#### [ Reid Barton (Oct 04 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135206928):
<p>I'm going to need to take colimits indexed by these partially ordered sets of ordinals less than <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>γ</mi></mrow><annotation encoding="application/x-tex">\gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05556em;">γ</span></span></span></span>--that's why I need the type to live in the correct universe</p>

#### [ Reid Barton (Oct 04 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135207023):
<p>I think the ZFC stuff would also leave me in the wrong universe, though maybe I could prove once and for all that categories which admit small colimits also admit colimits by "categories in ZFC", or something like that...</p>

#### [ Mario Carneiro (Oct 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135209373):
<p>You can measure the cofinality of any preorder, I think. Maybe it's easier to work without even using well orders</p>

#### [ Mario Carneiro (Oct 04 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ordinals/near/135209437):
<p>but yes, you almost certainly want to reason about ordered types rather than ordinals directly</p>


{% endraw %}
