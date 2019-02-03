---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81128DeMorgans.html
---

## Stream: [general](index.html)
### Topic: [De Morgan's](81128DeMorgans.html)

---


{% raw %}
#### [ Ken Lee (Oct 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299566):
<p>Just proved <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∨</mo><mi>Q</mi><mo>)</mo><mspace width="0.277778em"></mspace><mo>⟺</mo><mspace width="0.277778em"></mspace><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∧</mo><mi mathvariant="normal">¬</mi><mi>Q</mi></mrow><annotation encoding="application/x-tex">\neg (P \lor Q ) \iff \neg P \land \neg Q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∨</span><span class="mord mathit">Q</span><span class="mclose">)</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟺</span></span><span class="mord mathrm"><span class="mspace thickspace"></span><span class="mord mathrm">¬</span></span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∨</mo><mi mathvariant="normal">¬</mi><mi>Q</mi><mo>→</mo><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∧</mo><mi>Q</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\neg P \lor \neg Q \to \neg (P \land Q)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∨</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span><span class="mrel">→</span><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathit">Q</span><span class="mclose">)</span></span></span></span> in Lean. I don't see why the converse would require classical logic though. Can someone please explain?</p>

#### [ Ken Lee (Oct 23 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299609):
<blockquote>
<p>Just proved <span class="tex-error">$$\not (P \and Q ) \iff \not P \and \not Q$$</span> and <span class="tex-error">$$\not P \or \not Q \to \not (P \and Q)$$</span> in Lean. I don't see why the converse would require classical logic though. Can someone please explain?</p>
</blockquote>
<p>Oh no. It didn't format the inline maths.</p>

#### [ Kenny Lau (Oct 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299662):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∧</mo><mi>Q</mi><mo>)</mo><mspace width="0.277778em"></mspace><mo>⟺</mo><mspace width="0.277778em"></mspace><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∧</mo><mi mathvariant="normal">¬</mi><mi>Q</mi></mrow><annotation encoding="application/x-tex">\neg (P \land Q ) \iff \neg P \land \neg Q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathit">Q</span><span class="mclose">)</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟺</span></span><span class="mord mathrm"><span class="mspace thickspace"></span><span class="mord mathrm">¬</span></span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∨</mo><mi mathvariant="normal">¬</mi><mi>Q</mi><mo>→</mo><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∧</mo><mi>Q</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\neg P \lor \neg Q \to \neg (P \land Q)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∨</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span><span class="mrel">→</span><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathit">Q</span><span class="mclose">)</span></span></span></span></p>

#### [ Kenny Lau (Oct 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299665):
<p><code>\neg (P \land Q ) \iff \neg P \land \neg Q$$ and $$\neg P \lor \neg Q \to \neg (P \land Q)</code></p>

#### [ Ken Lee (Oct 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299713):
<blockquote>
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∧</mo><mi>Q</mi><mo>)</mo><mspace width="0.277778em"></mspace><mo>⟺</mo><mspace width="0.277778em"></mspace><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∧</mo><mi mathvariant="normal">¬</mi><mi>Q</mi></mrow><annotation encoding="application/x-tex">\neg (P \land Q ) \iff \neg P \land \neg Q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathit">Q</span><span class="mclose">)</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟺</span></span><span class="mord mathrm"><span class="mspace thickspace"></span><span class="mord mathrm">¬</span></span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>P</mi><mo>∨</mo><mi mathvariant="normal">¬</mi><mi>Q</mi><mo>→</mo><mi mathvariant="normal">¬</mi><mo>(</mo><mi>P</mi><mo>∧</mo><mi>Q</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\neg P \lor \neg Q \to \neg (P \land Q)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∨</span><span class="mord mathrm">¬</span><span class="mord mathit">Q</span><span class="mrel">→</span><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mbin">∧</span><span class="mord mathit">Q</span><span class="mclose">)</span></span></span></span></p>
</blockquote>
<p>Thanks!</p>

#### [ Jean Lo (Oct 23 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301162):
<p>related question: more generally, how does one go about determining whether a proof can be done constructively?</p>

#### [ Chris Hughes (Oct 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301256):
<p>If it implies excluded middle then it can't be done constructively. There's an exercise somewhere proving a whole load of things imply excluded middle.</p>

#### [ Kenny Lau (Oct 23 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301345):
<p>but that is not necessary.</p>

#### [ Kenny Lau (Oct 23 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301420):
<p>you can't check every Kripke model though... is there some finite subset that we can check</p>

#### [ Mario Carneiro (Oct 23 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301599):
<p>there is a completeness result that says any intuitionistically invalid statement is false on a finite kripke model</p>

#### [ Kenny Lau (Oct 23 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301662):
<p>that makes set of intuitionstically valid theorems a Π1 set, thus a Δ1 set?</p>

#### [ Mario Carneiro (Oct 23 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301672):
<p>yes, so it is decidable</p>

#### [ Kevin Buzzard (Oct 23 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301676):
<p><span class="user-mention" data-user-id="132889">@Jean Lo</span>  Here is a basic strategy for checking that various simple things can't be done constructively. First observe that all the rules of constructive logic apply when "truth values" are...something like...open sets in a topological space (I hope I remembered this right). You model "not" as "interior of the complement" and "implies" as "is a subset of". Then some stuff like "P or not P" simply isn't true in this interpretation, because the union of an open set and the interior of its complement might not be the whole space.</p>

#### [ Kenny Lau (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301727):
<p>does this together with the 14-theorem give you a fast(er) way of determining stuff?</p>

#### [ Kenny Lau (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301729):
<p><a href="https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem" target="_blank" title="https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem">https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem</a></p>

#### [ Mario Carneiro (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301731):
<p>It's not complete, unfortunately</p>

#### [ Mario Carneiro (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301735):
<p>at least not unless you consider all topologies</p>

#### [ Kevin Buzzard (Oct 23 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301744):
<p>I don't know, but I don't know what a Kripke model is and yet I've used this way of thinking about things to convince myself that certain propositions can't be proved in classical logic and basically it's the only way I know to do such a thing.</p>

#### [ Kenny Lau (Oct 23 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301745):
<p>just consider the Kuratowski algebra?</p>

#### [ Mario Carneiro (Oct 23 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301848):
<p>A Kripke model is based on a kind of epistemological interpretation of the formulas. There are a bunch of points called "worlds", and at each point there are things that are known to be true at that world, but the things that are not known to be true are just unknowns. There is a "in the future" accessibility relation to other worlds where more things may be known (but previously known things are still known), and things are known to be false only if they are never known in the future</p>

#### [ Kenny Lau (Oct 23 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301894):
<p>I don't think Kevin cares</p>

#### [ Mario Carneiro (Oct 23 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301904):
<p>For example, suppose we have time 0 and time 1, and at time 0 nothing is known and at time 1 <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span> is known. Then at time 0 neither <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span> or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>p</mi></mrow><annotation encoding="application/x-tex">\neg p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit">p</span></span></span></span> is known</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302025):
<p>This semantics generalizes nicely to modal logic as well, where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">□</mi><mi>A</mi></mrow><annotation encoding="application/x-tex">\Box A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord amsrm">□</span><span class="mord mathit">A</span></span></span></span> means A is known now and henceforth in the future</p>

#### [ Kenny Lau (Oct 23 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302083):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">□</mi></mrow><annotation encoding="application/x-tex">\square</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.675em;"></span><span class="strut bottom" style="height:0.675em;vertical-align:0em;"></span><span class="base"><span class="mord amsrm">□</span></span></span></span> <code>\square</code></p>

#### [ Scott Olson (Oct 23 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302094):
<p>My intuition regarding <code>¬(p ∧ q) → ¬p ∨ ¬q</code> is that, as my assumption, I know "<code>p</code> and <code>q</code> aren't <em>both</em> true", but I don't know <em>which one</em> is false, and the conclusion requires me to pick one of the two and prove it's false, which I cannot do</p>

#### [ Kenny Lau (Oct 23 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302122):
<p>ah, is that the program interpretation</p>

#### [ Scott Olson (Oct 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302208):
<p>yeah, interpreting <code>∧</code> as a pair type and <code>∨</code> as a sum type</p>

#### [ Kenny Lau (Oct 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302213):
<p>I think the corresponding model is where at time 0 nothing is known, at time 1a we know q, and at time 1b we know p.</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302267):
<p>The kripke model for this one has three points, with time 0 where nothing is known and a branching future. In world 1, p is known, and in world 2 q is known. Then since <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi><mo>∧</mo><mi>q</mi></mrow><annotation encoding="application/x-tex">p\land q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.55556em;"></span><span class="strut bottom" style="height:0.75em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span><span class="mbin">∧</span><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> is true in no world, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mo>(</mo><mi>p</mi><mo>∧</mo><mi>q</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\neg(p\land q)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mopen">(</span><span class="mord mathit">p</span><span class="mbin">∧</span><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="mclose">)</span></span></span></span> is true in every world, but neither <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>p</mi></mrow><annotation encoding="application/x-tex">\neg p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit">p</span></span></span></span> nor <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">¬</mi><mi>q</mi></mrow><annotation encoding="application/x-tex">\neg q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathrm">¬</span><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> is true in world 0</p>

#### [ Kenny Lau (Oct 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302274):
<p>:)</p>

#### [ Scott Olson (Oct 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302330):
<p>Interesting, I've never heard of that stuff but it lines up really well with what I did in my head</p>

#### [ Kenny Lau (Oct 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302335):
<p>I think you can consider the more general <code>((p ∧ q) → r) → (p → r) ∨ (q → r)</code> and use the same model</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302374):
<p>yes</p>

#### [ Kenny Lau (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302405):
<p>cool</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302409):
<p>There is no single finite model complete for intuitionistic logic though, or equivalently there is an infinite family of truth values over one proposition</p>

#### [ Kenny Lau (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302427):
<p>or maybe "truth values" just don't make sense</p>

#### [ Scott Olson (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302429):
<div class="codehilite"><pre><span></span>h : (p ∧ q) → false
⊢ (p → false) ∨ (q → false)
</pre></div>


<p>(expanding the \not to the function to false)</p>
<p>I can either assume <code>p</code> or assume <code>q</code> (the two worlds) and then prove <code>false</code>, but I can't apply the function <code>h</code> with just one of them</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302449):
<p><a href="https://upload.wikimedia.org/wikipedia/commons/5/5c/Rieger-Nishimura.svg" target="_blank" title="https://upload.wikimedia.org/wikipedia/commons/5/5c/Rieger-Nishimura.svg">https://upload.wikimedia.org/wikipedia/commons/5/5c/Rieger-Nishimura.svg</a></p>

#### [ Kenny Lau (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302461):
<p>what is thsi</p>

#### [ Reid Barton (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302472):
<p>I saw this image for the first time like three days ago and I was very confused about how I had never seen it before</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302478):
<p>it is the lattice of propositions over one variable</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302485):
<p>up to equivalence</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302539):
<p>in classical logic it is much less interesting, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">⊥</mi><mo>&lt;</mo><mi>p</mi><mo separator="true">,</mo><mi mathvariant="normal">¬</mi><mi>p</mi><mo>&lt;</mo><mi mathvariant="normal">⊤</mi></mrow><annotation encoding="application/x-tex">\bot &lt; p,\neg p &lt; \top</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathrm">⊥</span><span class="mrel">&lt;</span><span class="mord mathit">p</span><span class="mpunct">,</span><span class="mord mathrm">¬</span><span class="mord mathit">p</span><span class="mrel">&lt;</span><span class="mord mathrm">⊤</span></span></span></span></p>

#### [ Kenny Lau (Oct 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302543):
<p>interesting</p>

#### [ Kenny Lau (Oct 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302586):
<p>the program interpretation is to let <code>p</code> to mean <code>X contains 1</code> and <code>q</code> to mean <code>X contains no 1</code> where <code>X</code> is an arbitrary (computable) binary sequence, right?</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302662):
<p>that's one way to do it</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302766):
<p>But if you like the program (aka BHK) formulation of intuitionistic semantics, then you might like the computational interpretation of peirce's law as call with continuation</p>

#### [ Kenny Lau (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302777):
<p>I never understood what call/cc means</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302993):
<p>The type is <code>callcc : ((p -&gt; q) -&gt; p) -&gt; p</code>. Suppose we are building something of type N, say, and in the course of it we want to do double negation elimination on some proposition <code>p</code>, like say "this TM halts". Then that means we are going to do something with this value of type <code>p</code>, so that's a function <code>p -&gt; N</code>, and so callcc steals this "continuation" and passes it to the enclosed function of type <code>(p -&gt; N) -&gt; p</code></p>

#### [ Mario Carneiro (Oct 23 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136303945):
<p>For example, consider the following implementation of <code>em</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">callcc</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span> <span class="o">((</span><span class="n">p</span> <span class="bp">-&gt;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="n">p</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="n">p</span>

<span class="n">def</span> <span class="n">em</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="err">⊕</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span> <span class="n">empty</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">callcc</span> <span class="bp">_</span> <span class="n">empty</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span>
<span class="k">show</span> <span class="n">p</span> <span class="err">⊕</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span> <span class="n">empty</span><span class="o">),</span> <span class="k">from</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hp</span><span class="o">,</span> <span class="n">H</span> <span class="err">$</span>
<span class="k">show</span> <span class="n">p</span> <span class="err">⊕</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span> <span class="n">empty</span><span class="o">),</span> <span class="k">from</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span>
</pre></div>


<p>This function looks like magic when you see it for the first time. It's a computational interpretation of EM! So we can just put in our favorite nondecidable proposition to this oracle, like the Riemann hypothesis, and find out the answer. It calls <code>callcc</code> at this point, which remembers our position in the code, and then calls the <code>sum.inr</code> constructor. So the oracle says: RH is false! We are happy until we find out maybe that RH is actually true, and in justified anger return to our function to prove a contradiction. When we call the function though, it calls <code>H</code> with <code>sum.inl hp</code>. What happened? The function <code>H</code> remembers when we called callcc the first time, and "rewinds time" with our proof of RH in hand. So the oracle says: RH is true! and it stole our proof.</p>

#### [ Kenny Lau (Oct 23 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304147):
<blockquote>
<p>our favorite nondecidable proposition to this oracle, like the Riemann hypothesis</p>
</blockquote>
<p>hmm...</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304242):
<p>I guess this is like "innocent until proven guilty", we have "false until proven true"</p>

#### [ Kenny Lau (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304249):
<p>I still don't understand what it does... thanks for your lengthy explanation though</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304262):
<p>The semantics is a bit tricky to explain without a notion of "continuation"</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304322):
<p>the idea is that every expression exists in a context, where you are evaluating an expression <em>in order to pass it to something else</em></p>

#### [ Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304335):
<p>and this something else can be thought of as a function from the type of the expr to the "final output"</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304340):
<p>which can be whatever, it doesn't really matter</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304349):
<p>it's like an expression with a hole in it where our expr goes</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304376):
<p>and <code>callcc</code> saves this expr-with-hole that surrounds the <code>callcc f</code> expression itself, and calls <code>f</code> on it</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304463):
<p>This enables bizarre behavior like returning twice from a function or functions that call each other as coroutines, or exception handling</p>

#### [ Mario Carneiro (Oct 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304470):
<p>lots of control flow can be expressed using continuations</p>

#### [ Kenny Lau (Oct 23 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304536):
<p>what kind of thing is call/cc?</p>

#### [ Kenny Lau (Oct 23 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304544):
<p>is it a function that we can implement? is it a function that only exists in some alternate programming language?</p>

#### [ Mario Carneiro (Oct 23 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136306080):
<p>it isn't a function you can implement in lean, but it is a function that could conceivably be supported in the VM as a primitive</p>

#### [ Kenny Lau (Oct 23 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318157):
<p>Could you write your RH thing in say <code>Scheme</code>?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318356):
<p>yes</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318362):
<p>I think they are the pioneers of callcc</p>

#### [ Kenny Lau (Oct 23 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318441):
<p>then what would it return?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318449):
<p>like I said, "false" until you prove it wrong</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318453):
<p>and then it goes back in time with your proof and says "true"</p>

#### [ Kenny Lau (Oct 23 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318501):
<p>do you have actual Scheme code?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318508):
<p>no, but you should just be able to use <code>callcc</code> in a term like I've shown</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318521):
<p>the lean code should translate without issue to scheme</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318583):
<p>there is also the matter of scheme not being a typed language</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318709):
<p>if the time travel is the part that is surprising, a more pedestrian explanation is that it just saves the current state of the VM - the call stack and values of the variables, then we can later "reset" to this execution state</p>

#### [ Kenny Lau (Oct 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318715):
<p>how does the program "take" our proof?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318717):
<p>you pass it to the function in an attempt to derive false</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318761):
<p>and rather than producing a proof of false, it abandons the entire execution of the rest of the program and resets with this proof in hand</p>

#### [ Kenny Lau (Oct 23 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318779):
<p>does <code>callcc</code> have any equational lemmas?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318784):
<p>yes, but they are a bit weird because they depend on the execution context</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318985):
<p>You have to set up the idea of a dynamic semantics. Let's say we want to evaluate <code>e1 + e2</code>, we can write this as <code>e1 + e2 &lt; K</code>where <code>K</code> is the call stack. It is expecting a value of type <code>nat</code> say, here. So we first evaluate <code>e1</code>, that is, <code>e1 &lt; _ + e2, K</code> where we have pushed <code>_ + e2</code> on the stack. We get to a value <code>v &gt; _ + e2, K</code> (the arrow is reversed to indicate that the value is done computing) which steps to <code>e2 &lt; v + _, K</code>. That is we are evaluating <code>e2</code> now. This finishes to <code>v2 &gt; v + _, K</code> which steps to <code>v' &gt; K</code> where <code>v'</code> is the actual result of adding numbers <code>v</code> and <code>v2</code></p>

#### [ Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319003):
<p>I don't understand how you can pass the proof to the function</p>

#### [ Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319008):
<p>the function doesn't accept things of type <code>p</code> right</p>

#### [ Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319009):
<p>it wants a thing of type <code>(p -&gt; q) -&gt; p</code></p>

#### [ Mario Carneiro (Oct 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319021):
<p>In the <code>em</code> example I define a particular function of type <code>(p -&gt; false) -&gt; p</code></p>

#### [ Mario Carneiro (Oct 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319037):
<p>or rather <code>(p + not p -&gt; false) -&gt; p + not p</code></p>

#### [ Mario Carneiro (Oct 23 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319085):
<p>so when the callcc is called it evaluates this function giving it a kind of magic function which has type <code>p + not p -&gt; false</code></p>

#### [ Mario Carneiro (Oct 23 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319152):
<p>this function should not ever be called, because it "destroys the universe" rather than producing a proof of false</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319316):
<p>Here's another example. If <code>f : (N -&gt; false) -&gt; N</code> is the constant function 42, then <code>callcc f</code> just returns 42. Nothing special happens as long as <code>f</code> never uses its argument</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319330):
<p>But if <code>f = \lam g, false.elim (g 12)</code>, then <code>callcc f</code> returns 12</p>

#### [ Kenny Lau (Oct 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319335):
<p>how?</p>

#### [ Kenny Lau (Oct 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319377):
<p>and if <code>f = \lam g, false.elim (g 12) + false.elim (g 13)</code>?</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319379):
<p>returns 12</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319386):
<p>the rest of the computation is abandoned once <code>g</code> is called</p>

#### [ Kenny Lau (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319394):
<p>hmm...</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319395):
<p>The function <code>g</code> given to <code>f</code> is actually the expr-with-hole that <code>callcc f</code> is situated in</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319465):
<p>it might make more sense if <code>g</code> is called <code>throw</code> instead</p>

#### [ Mario Carneiro (Oct 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319468):
<p>and <code>callcc</code> is <code>catch</code></p>


{% endraw %}
