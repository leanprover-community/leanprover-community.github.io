---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40384computersaresmart.html
---

## Stream: [maths](index.html)
### Topic: [computers are smart??](40384computersaresmart.html)

---


{% raw %}
#### [ Reid Barton (Jun 04 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127549305):
<p>So I was going along constructing coequalizers in Top, like you do. A coequalizer is a kind of quotient, so I needed to prove that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Z</mi></mrow><annotation encoding="application/x-tex">Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span> is the quotient of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi></mrow><annotation encoding="application/x-tex">Y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span></span></span></span> by a relation, then the quotient map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi><mo>→</mo><mi>Z</mi></mrow><annotation encoding="application/x-tex">Y \to Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span> is continuous, so that it's a morphism in Top.<br>
I was all set to add the lemma for that to my <code>continuity</code> tactic, when I noticed the tactic had already succeeded before I did so! What happened?</p>

#### [ Reid Barton (Jun 04 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127549340):
<p>It turns out that continuity of the quotient map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi><mo>→</mo><mi>Z</mi></mrow><annotation encoding="application/x-tex">Y \to Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span> is <em>definitionally equivalent</em> to continuity of the identity map on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Z</mi></mrow><annotation encoding="application/x-tex">Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span>, because a set is defined to be open in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Z</mi></mrow><annotation encoding="application/x-tex">Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span> if and only if its preimage is open in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Y</mi></mrow><annotation encoding="application/x-tex">Y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">Y</span></span></span></span>. So the tactic found that it could just apply <code>continuous_id</code>!</p>

#### [ Johan Commelin (Jun 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127554973):
<p>Wunderbar!</p>

#### [ Johan Commelin (Jun 05 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127587246):
<p>In fact, Reid, how did you define the topology on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>Z</mi></mrow><annotation encoding="application/x-tex">Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">Z</span></span></span></span>? Because there is a bunch of stuff on coinduced topologies in mathlib, and that would also give you continuity of the quotient map by definition.</p>

#### [ Reid Barton (Jun 05 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127595731):
<p>I did use the coinduced topology (see PR at <a href="https://github.com/leanprover/mathlib/pull/155/commits/b60f3687e8692f118c385f958d48d31388593298#diff-1c17754b46d709d0b8e22318f94035cdR903" target="_blank" title="https://github.com/leanprover/mathlib/pull/155/commits/b60f3687e8692f118c385f958d48d31388593298#diff-1c17754b46d709d0b8e22318f94035cdR903">https://github.com/leanprover/mathlib/pull/155/commits/b60f3687e8692f118c385f958d48d31388593298#diff-1c17754b46d709d0b8e22318f94035cdR903</a>)</p>

#### [ Johan Commelin (Jun 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computers%20are%20smart%3F%3F/near/127595747):
<p>I see. So your <code>continuity</code> tactic is not in that PR?</p>


{% endraw %}
