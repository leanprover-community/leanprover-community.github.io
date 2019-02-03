---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44794isopenxxuinU.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [is_open {x | x + u \in U}](https://leanprover-community.github.io/archive/113488general/44794isopenxxuinU.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 10 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133679397):
<p>Given a topological additive monoid, I expected theorems that say that you can translate opens along addition by a given element. But I could not find those... is this in mathlib, or do I need to roll my own?</p>

#### [ Kenny Lau (Sep 10 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133679963):
<p>continuous_add or something</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680126):
<p>Are you sure Kenny? That seems to prove only that the pre-image of an open under the map lam x, x+c (c constant) is open. But you can't cancel in a monoid and Johan seems to want to show that the image, not the pre-image, of an open is open. <span class="user-mention" data-user-id="112680">@Johan Commelin</span> are you sure that what you want to prove is true? What exactly do you want to prove?</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680147):
<p>and what exactly are you thinking about topological monoids for??</p>

#### [ Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680161):
<p>Hmmm, I probably over-generalised.</p>

#### [ Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680168):
<p>Let's assume it's a group.</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680174):
<p>then what Kenny said</p>

#### [ Johannes Hölzl (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680177):
<p>Huh, the title looks like a preimage</p>

#### [ Johan Commelin (Sep 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680182):
<p>That's good enough for applications, since I'm a mathematician.</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680237):
<p>oh yes, Kenny's comment answers the question in the title but not in the body.</p>

#### [ Johan Commelin (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680244):
<p>Ok, somehow <code>continuous_add</code> didn't work straightaway. I'll try harder.</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680273):
<p>I'm assuming continuous_add is continuity of addition, so now you need to compose with the map from G to G x G sending g to g,c</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680277):
<p>which is continuous for any topological space</p>

#### [ Kenny Lau (Sep 10 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133680978):
<blockquote>
<p>Given a topological additive monoid, I expected theorems that say that you can translate opens along addition by a given element. But I could not find those... is this in mathlib, or do I need to roll my own?</p>
</blockquote>
<p>I think this is not true. Consider the topological multiplicative monoid <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="double-struck">R</mi></mrow><annotation encoding="application/x-tex">\Bbb R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord mathbb">R</span></span></span></span> and translation by 0</p>

#### [ Kevin Buzzard (Sep 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681061):
<p>bingo</p>

#### [ Reid Barton (Sep 10 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681162):
<p>Hmn, I could PR the <code>continuity</code> tactic now that tidy is in mathlib</p>

#### [ Patrick Massot (Sep 10 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681868):
<p>Related: <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289</a></p>

#### [ Patrick Massot (Sep 10 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open%20%7Bx%20%7C%20x%20%2B%20u%20%5Cin%20U%7D/near/133681885):
<p>Reid: yes, please!</p>


{% endraw %}
