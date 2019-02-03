---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88707subsetorsubtype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subset or subtype?](https://leanprover-community.github.io/archive/113488general/88707subsetorsubtype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268484):
<p>I wrote presheaves of types twice in my life and I see now that my definitions differ.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268485):
<p>First is</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268528):
<p><code>(F : Π U : set α, T.is_open U → Type*) </code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268536):
<p>Second is</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268537):
<p><code>(F : {U // topological_space.is_open T U} → Type*)</code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268539):
<p>Which is "better"?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268544):
<p>I seem to be able to work with either</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268647):
<p>Is the only difference that with the first I have two different names U and HU, and with the second I have V.val and V.property?</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268652):
<p>Yes, it is analogous to the difference between <code>A → B → C</code> and <code>A ∧ B → C</code>.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268694):
<p>But with those two choices, functional program people prefer the first, right?</p>

#### [ Patrick Massot (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268696):
<p>Proof assistant people seem to always prefer <code>A → B → C</code>, so which is better for presheaves?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268697):
<p>which is which ;-)</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268698):
<p>Presumably H.1 and H.2 is V.val and V.property so this is the one I should perhaps avoid</p>

#### [ Reid Barton (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268699):
<p>The second one also gives you the name "V", which for doing abstract sheaf theory things (that don't care about the particular site) seems like it would be more convenient.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268704):
<p>oh but here's a difference: A and B is a type</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268705):
<p>so it can be used more easily as a target</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268797):
<p>This doesn't seem to matter in practice. I am going for set because it seems to be analogous to the "more functional" <code>A -&gt; B -&gt; C</code></p>

#### [ Reid Barton (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123269074):
<p>If you imagine defining a sheaf of sets on a general site, then the first way seems really unnatural (what would be the analogue of <code>is_open</code>?) So from a "math" perspective, the second way looks better.<br>
I don't know what the practical implications are, though.</p>

#### [ Reid Barton (Mar 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123269187):
<p>(I would also set it up so that I can write <code>U : T.open_set</code>, and use <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∩</mo></mrow><annotation encoding="application/x-tex">\cap</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.55556em;"></span><span class="strut bottom" style="height:0.55556em;vertical-align:0em;"></span><span class="base"><span class="mord">∩</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∪</mo></mrow><annotation encoding="application/x-tex">\cup</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.55556em;"></span><span class="strut bottom" style="height:0.55556em;vertical-align:0em;"></span><span class="base"><span class="mord">∪</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>⊂</mo></mrow><annotation encoding="application/x-tex">\subset</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.5391em;"></span><span class="strut bottom" style="height:0.5782em;vertical-align:-0.0391em;"></span><span class="base"><span class="mrel">⊂</span></span></span></span> directly on open sets, etc.)</p>


{% endraw %}
