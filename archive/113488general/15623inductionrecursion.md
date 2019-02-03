---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15623inductionrecursion.html
---

## Stream: [general](index.html)
### Topic: [induction recursion?](15623inductionrecursion.html)

---


{% raw %}
#### [ Max New (Apr 25 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125688817):
<p>Does lean support inductive-recursive definitions?</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125704194):
<p>No. You can simulate a reasonably broad subclass of inductive-recursive definitions, but general induction-recursion proves lean's consistency.</p>

#### [ Sean Leather (Apr 26 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125710616):
<blockquote>
<p>general induction-recursion proves lean's consistency.</p>
</blockquote>
<p>?</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711168):
<p>You can construct the valid contexts and well typed terms in that context by induction-recursion. Then you can prove any lean term has a denotation by induction</p>

#### [ Sean Leather (Apr 26 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711396):
<p>What do you mean by “proving the consistency of Lean”?</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711455):
<p>I mean you can encode lean inside lean and prove of that object-lean that it can't prove false</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711456):
<p>i.e. exactly the thing Godel says is impossible</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711962):
<p>...unless Lean is inconsistent ;-)</p>

#### [ Reid Barton (Apr 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826056):
<p>Is the following a definition by induction-recursion?</p>
<ul>
<li>
<p>An <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">(n+1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span>-dimensional CW complex <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">X_{n+1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.891661em;vertical-align:-0.208331em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.301108em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span> consists of the data of</p>
<ul>
<li>an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>-dimensional CW complex <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">X_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>,</li>
<li>a set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">C_{n+1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.891661em;vertical-align:-0.208331em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.301108em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span> of "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">(n+1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span>-dimensional cells", and</li>
<li>for each <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mo>∈</mo><msub><mi>C</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">i \in C_{n+1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.891661em;vertical-align:-0.208331em;"></span><span class="base"><span class="mord mathit">i</span><span class="mrel">∈</span><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.301108em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span>, an "attaching" map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>e</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">e_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>S</mi><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">S^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> to the underlying topological space of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">X_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>.</li>
</ul>
</li>
<li>
<p>The underlying topological space of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">X_{n+1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.891661em;vertical-align:-0.208331em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.301108em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span> is obtained from that of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">X_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> by attaching a copy of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>D</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow><annotation encoding="application/x-tex">D^{n+1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span></span></span></span> along the attaching map of each cell.</p>
</li>
</ul>

#### [ Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826168):
<p>aha!</p>

#### [ Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826176):
<p>I formalized CW complex a while ago lol</p>

#### [ Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826180):
<p><a href="https://math.stackexchange.com/a/2712786/328173" target="_blank" title="https://math.stackexchange.com/a/2712786/328173">https://math.stackexchange.com/a/2712786/328173</a></p>

#### [ Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826181):
<p>a month ago</p>

#### [ Kenny Lau (Apr 28 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826226):
<p>Isn't it just an inductive type?</p>

#### [ Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826281):
<p>The last field (the attaching maps) involves the function "underlying topological space" which (it seems to me) you need to define simultaneously with the inductive type</p>

#### [ Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826283):
<p>If you could define an infinite alternating list of inductive types and functions, it would be one of those.</p>

#### [ Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826284):
<p>I haven't tried actually writing it out in lean though.</p>

#### [ Kenny Lau (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826288):
<p>you don't need to know that X_n is a topological space, I think?</p>

#### [ Reid Barton (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826296):
<p>Well I omitted the word, but it has to be a continuous map</p>

#### [ Reid Barton (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826297):
<p>The attaching maps</p>

#### [ Kenny Lau (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826298):
<p>oh right</p>

#### [ Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826338):
<p>there might be other approaches, but I have an ugly approach in mind</p>

#### [ Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826339):
<p>define the sigma type inductively</p>

#### [ Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826340):
<p>(not sure if it works, after I say it)</p>

#### [ Reid Barton (Apr 28 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826403):
<p>(I had some idea of how to formalize this in lean, but I'm curious to hear others, and also I didn't write down my idea and I think it was kind of ugly.)</p>

#### [ Reid Barton (Apr 28 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125827025):
<p>I'd also appreciate a type theory expert confirming whether or not this is an example of induction-recursion at all, since induction-recursion is an unfamiliar thing and the typical examples are even more unfamiliar things, while CW complexes are something that all mathematicians learn about.</p>


{% endraw %}
