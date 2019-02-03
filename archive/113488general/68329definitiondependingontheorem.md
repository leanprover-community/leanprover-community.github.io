---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68329definitiondependingontheorem.html
---

## Stream: [general](index.html)
### Topic: [definition depending on theorem](68329definitiondependingontheorem.html)

---


{% raw %}
#### [ Johan Commelin (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135382946):
<p>For my Lean-talk I would like a good example of a definition that depends on a (non-trivial) theorem. I don't want to use perfectoid spaces because that is way too advanced. I want to use this thread to collect a list of cute examples.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135383090):
<p>How about: the dimension of a vector space depending on the fact that all bases have the same cardinality</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135383347):
<p>technically, the definition doesn't need this assumption, because it is defined as the <em>minimum</em> of such cardinalities. Instead, a proof is required to show that a minimum of cardinalities is well defined</p>

#### [ Chris Hughes (Oct 08 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135384058):
<p>convergence of exponential series. Also proof that the polynomial division algorithm is well founded took me a while. All of these can be done without any proofs technically, with some <code>dite</code> statement.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135384131):
<p>at the expense of computability of course</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387000):
<p>The definition of an affine scheme needs the fact that the structure sheaf on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mi>p</mi><mi>e</mi><mi>c</mi><mo>(</mo><mi>A</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">Spec(A)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mord mathit">p</span><span class="mord mathit">e</span><span class="mord mathit">c</span><span class="mopen">(</span><span class="mord mathit">A</span><span class="mclose">)</span></span></span></span> is actually a sheaf, which took us quite some time to prove.</p>

#### [ Johan Commelin (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387024):
<p>Yes, but I will be talking to an audience that partly doesn't know what a sheaf is...</p>

#### [ Patrick Massot (Oct 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387944):
<p>What about the definition of addition of real numbers? Or even addition or integers</p>


{% endraw %}
