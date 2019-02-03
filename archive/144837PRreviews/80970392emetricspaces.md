---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/80970392emetricspaces.html
---

## Stream: [PR reviews](index.html)
### Topic: [#392 emetric spaces](80970392emetricspaces.html)

---


{% raw %}
#### [ Johan Commelin (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384309):
<p>I am wondering: <code>dist</code> of a metric space takes values in <code>ℝ</code>, while the <code>edist</code> of an emetric space takes values in <code>ennreal</code>. Should the latter maybe take values in <code>with_top ℝ</code>?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384322):
<p>I haven't thought this through carefully. I just noted it while reading through the code.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384347):
<p><code>ennreal</code> has nicer properties than <code>with_top R</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384408):
<p>I think we had a conversation about going the other way, i.e. using <code>nnreal</code> for the codomain of <code>dist</code></p>

#### [ Kenny Lau (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384413):
<p>If X is a metric space, is P(X) an emetric space?</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384434):
<p>I think there is a Hausdorff something or other about this</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384439):
<p><a href="https://en.wikipedia.org/wiki/Hausdorff_distance" target="_blank" title="https://en.wikipedia.org/wiki/Hausdorff_distance">https://en.wikipedia.org/wiki/Hausdorff_distance</a></p>

#### [ Mario Carneiro (Oct 08 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384480):
<p>it's not all sets, just compact sets</p>

#### [ Johan Commelin (Oct 08 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384489):
<p>And the axiom <code>(dist_nonneg : ∀ x y, dist x y ≥ 0)</code> in the definition of metric space. This is redundant, because it follows from <code>edist_dist</code>.</p>

#### [ Kenny Lau (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384518):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> compactness just ensures that it is finite</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384520):
<p>oh wait, the Hausdorff distance is defined on all sets but it is only an extended pseudometric</p>

#### [ Kenny Lau (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384526):
<p>and in any case I'm just talking about d(X,Y) := inf d(x,y)</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384538):
<p>that's not even zero on the same sets</p>

#### [ Kenny Lau (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384589):
<p>it is</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384604):
<p>it is</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384611):
<p>but it's not an iff</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384619):
<p>The Hausdorff distance is an edistance on closed subets.</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384627):
<p>This is one of the motivations to introduce this notion of emetric spaces.</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384634):
<p>It restricts to a genuine distance on compact nonempty subsets.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384641):
<p>Another motivation is the infinite product space</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384692):
<p>with supremum metric</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384732):
<p>The axiom <code>dist_nonneg</code> is not redundant. When I write <code>edist x y = ↑(nnreal.of_real (dist x y))</code>, it would be true if <code>dist x x = -1</code>, say, as <code>nnreal.of_eal</code> sends <code>-1</code>to <code>0</code>.</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384881):
<p><code>ennreal</code> is very much better behaved than <code>ereal</code> from the algebraic point of view. So, if you know that something is nonnegative, you should really favor <code>ennreal</code> over <code>ereal</code> from a usability point of view. On the opposite, <code>real</code> is better behaved than <code>nnreal</code> (subtraction is nice on <code>real</code>), so if you have the choice between the two better use reals. The main difference is that you will often subtract distances, but you should never subtract edistances as they can be infinite.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135384893):
<p>why the finiteness assumption in <code>emetric_space_pi</code></p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135385019):
<p>If you take an infinite product of emetric spaces, with the sup distance, then the topology you get is typically not the product topology. So, this is not a good notion.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135387840):
<blockquote>
<p>it is</p>
</blockquote>
<p>not on the empty set...</p>

#### [ Johan Commelin (Oct 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135387951):
<p>We need an Ofer Gabber emoji</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135387962):
<p>we'll make you a CS guy yet... you get an honorary degree in zeroology</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135388367):
<p>I am proud to be a zerologist. In fact one of the nicest comments a speaker ever said to me was in a talk when I noted that an assertion made by the speaker did not make sense when <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">n=0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.64444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">=</span><span class="mord mathrm">0</span></span></span></span> and I pointed this out, and they said "I did not know Gabber was in the audience!".</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/135388431):
<p>I nearly responded "well he's certainly not giving the talk"</p>

#### [ Johan Commelin (Nov 09 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23392%20emetric%20spaces/near/147372294):
<p>This PR is now merged! Hurray! <span class="emoji emoji-1f389" title="tada">:tada:</span> <span class="emoji emoji-1f419" title="octopus">:octopus:</span></p>


{% endraw %}
