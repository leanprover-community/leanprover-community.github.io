---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96591proposalforbackwardsreasoning.html
---

## Stream: [general](index.html)
### Topic: [proposal for `backwards_reasoning`](96591proposalforbackwardsreasoning.html)

---


{% raw %}
#### [ Scott Morrison (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383465):
<p>I'd like to propose an interactive partner for <code>solve_by_elim</code>. The idea is that it will be a tool for applying "backwards reasoning" (i.e. applying lemmas against the goal).</p>
<p>The idea is that we'll tag certain lemmas with an attribute, perhaps <code>back</code>, that are "safe" for backwards reasoning. A good example would be <code>min_fac_dvd : ∀ (n : ℕ), min_fac n ∣ n</code>. If you can unify that conclusion with the goal, you can't possibly be unhappy --- the only parameters are determined by unification, so no new goals can appear.</p>
<p><code>backwards_reasoning [x, y, z]</code>, will apply all lemmas marked with <code>@[back]</code> against the goal, as well as applying x, y, z. It will then apply <code>solve_by_elim</code> afterwards (so also applying all hypotheses). The key difference from just using <code>solve_by_elim</code> is that <code>backwards_reasoning</code> will succeed even if it doesn't close the goal, as long as it manages to apply at least one of the specified lemmas.</p>
<p>Here's an example of it in action:</p>

#### [ Scott Morrison (Oct 08 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383576):
<div class="codehilite"><pre><span></span>import data.nat.prime
import tactic.backwards_reasoning

open nat

-- These are all lemmas which it is sufficiently safe to `apply`
-- that they can be automatically applied by backwards_reasoning.
attribute [back] succ_lt_succ
                 fact_pos dvd_fact
                 min_fac_prime min_fac_dvd

theorem infinitude_of_primes (N : ℕ) : ∃ p ≥ N, prime p :=
begin
  let M := fact N + 1,
  let p := min_fac M,
  have pp : prime p, sorry,
  sorry,
</pre></div>


<p>Now we replace that first <code>sorry</code> with <code>backwards_reasoning</code>, and the goal <code>prime p</code> is replaced with <code>M \neq 1</code>.<br>
(If we replace <code>backwards_reasoning</code> with <code>backwards_reasoning#</code>, it prints out what it did: <code>apply min_fac_prime</code>.)</p>
<p>We then realise that a good way to proceed is<code>apply ne_of_gt</code>, so we modify the tactic to <code>backwards_reasoning [ne_of_gt]</code>.<br>
This succeeds, discharging the goal! If we replace the tactic with <code>backwards_reasoning# [ne_of_gt]</code>, it prints what it did:<br>
<code>exact min_fac_prime (ne_of_gt (succ_lt_succ (fact_pos N)))</code>.</p>
<p>If you prefer you can then copy and paste that output, replacing entirely the call to <code>backwards_reasoning</code>.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383595):
<p>(The rest of the proof of <code>infinitude_of_primes</code> can be proved in the same style.)</p>

#### [ Johan Commelin (Oct 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383599):
<p>Looks really good <span class="user-mention" data-user-id="110087">@Scott Morrison</span></p>

#### [ Kenny Lau (Oct 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383652):
<p>looks like <code>inversion</code>™ in Coq</p>

#### [ Scott Morrison (Oct 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383661):
<p>Having this be really useful requires some judicious tagging of lemmas with <code>back</code>. My suggestion to start off just by having a smattering of attributes added in the <code>tactics/backwards_reasoning.lean</code> file itself, and to consider later moving them to the point of definition if it seems useful.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383731):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>, can you point me to some examples? The documentation I found for <a href="https://coq.inria.fr/refman/proof-engine/tactics.html" target="_blank" title="https://coq.inria.fr/refman/proof-engine/tactics.html">inversion</a> is not super helpful. :-(</p>

#### [ Kenny Lau (Oct 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383778):
<p><a href="https://coq.inria.fr/refman/proof-engine/tactics.html#coq:tacn.inversion" target="_blank" title="https://coq.inria.fr/refman/proof-engine/tactics.html#coq:tacn.inversion">you're looking at the wrong part</a></p>

#### [ Kenny Lau (Oct 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383783):
<blockquote>
<p><code>inversion ident</code></p>
<p>Let the type of ident in the local context be (I t), where I is a (co)inductive predicate. Then, inversion applied to ident derives for each possible constructor c i of (I t), all the necessary conditions that should hold for the instance (I t) to be proved by c i.</p>
</blockquote>

#### [ Scott Morrison (Oct 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383795):
<p>Glad you like it, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>. :-) I may wait until I hear something from <span class="user-mention" data-user-id="110026">@Simon Hudon</span> or <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> before I bother cleaning it up for a PR.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383796):
<p>But in any case I'll need some version of it before I'm willing to PR my work on limits in category theory. :-)</p>

#### [ Kenny Lau (Oct 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383836):
<p>and in any case one should be noted that I do not know Coq at all.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383850):
<p>Ok. It seems in any case <code>inversion</code> in Coq is quite different; whatever exactly it's doing, it's only doing one step, it's not something that chains together a whole sequence of applications.</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383862):
<p>I don't see what <code>inversion</code> has to do with it - <code>inversion</code> is the equivalent of lean <code>cases</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383938):
<p>How does <code>backwards_reasoning</code> select the lemmas to apply? Does it just go through the whole list every time?</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383944):
<p>also <code>backwards_reasoning</code> has way too many letters in it</p>

#### [ Scott Morrison (Oct 08 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384240):
<p>Yes, it just runs through the whole list every time. I have not tested this at really big scale, but (a version of this) has been in my category theory library for a while, with maybe ~50 lemmas, and it never shows up in profiling. I think <code>apply</code> fails very fast.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384254):
<p>I think that if we used it in mathlib we would want to use it large scale, and then this would become a concern</p>

#### [ Scott Morrison (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384297):
<blockquote>
<p>also <code>backwards_reasoning</code> has way too many letters in it</p>
</blockquote>
<p>I could rename it <code>br</code>, if you prefer. :-). How about just <code>back</code>?</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384308):
<p>indeed I get the sense that it's not very useful unless it is marked everywhere</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384311):
<p>If I understand correctly, you're creating a version of <code>apply_rules</code> on steroids, with additionally a set of default rules to be applied, right?</p>

#### [ Scott Morrison (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384317):
<p>That sounds about right.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384321):
<p>I admit I don't understand <code>apply_rules</code> usage</p>

#### [ Scott Morrison (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384327):
<p>(I have not used apply_rules, but I've seen the implementation.)</p>

#### [ Scott Morrison (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384338):
<p>I guess we could have 'sub-attributes', to mark lemmas as relevant in certain domains.</p>

#### [ Scott Morrison (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384396):
<p>The other solution is just to accept that <code>backwards_reasoning</code> is a slow tactic, and you're meant to switch to <code>backwards_reasoning#</code> once you've discovered the proof, and copy-paste the trace output.</p>

#### [ Scott Morrison (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384409):
<p>(And just not worry about slow tactics, because we all have 30 cores, right?)</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384528):
<p>If you want to go even further in this direction, let me mention the syntax of the Isabelle swiss army knife <code>auto</code>. Some rules in Isabelle are marked <code>[intro]</code>, or <code>[intro!]</code> (the first one would be unsafe rules to be applied in backward reasoning, the second one for safe rules). In the same way there are simp rules. And all of this can be combined with</p>
<div class="codehilite"><pre><span></span>auto (simp: foo_simp, bar_simp, intro:  foo_intro, bar_intro)
</pre></div>


<p>which will apply eagerly the rules <code>foo_intro</code> or <code>bar_intro</code> and the rules marked <code>[intro!]</code> in the library (and also the <code>[intro]</code> ones if their assumptions can be checked right away), simplify everything using the simplifier with the additional rules <code>foo_simp</code> and <code>bar_simp</code>, and go over again. All this with some amount of backtracking that can be controlled. 90% of Isabelle proofs are <code>auto</code>proofs...</p>

#### [ Scott Morrison (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384636):
<p>Thanks for this description, <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span>!</p>

#### [ Scott Morrison (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384708):
<p>My version of <code>tidy</code> in the category theory library has been using <code>backwards_reasoning</code> all along, and the main loop of <code>tidy</code> causes it to bounce back and forth between <code>backwards_reasoning</code> and <code>simp</code>. :-) Good to know I was re-inventing <code>auto</code>.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384713):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> And do those proofs remain <code>auto</code>, or do they get replaced by some unreadable proof that <code>auto</code> found? In other words: is this fast, and how does Isabelle solve the speed issues that we are hitting now in Lean?</p>

#### [ Scott Morrison (Oct 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384719):
<p>(Of course, <code>tidy</code> does many other things in the loop, for better or worse.)</p>

#### [ Scott Morrison (Oct 08 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384780):
<p>My private <code>backwards_reasoning</code> also makes the distinction analogous to <code>[intro]</code> vs <code>[intro!]</code>, but I haven't reimplemented that completely in the new backwards_reasoning I've just been describing.</p>

#### [ Sebastien Gouezel (Oct 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384964):
<blockquote>
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> And do those proofs remain <code>auto</code>, or do they get replaced by some unreadable proof that <code>auto</code> found? In other words: is this fast, and how does Isabelle solve the speed issues that we are hitting now in Lean?</p>
</blockquote>
<p>There are no speed issues in Isabelle. <code>auto</code> is extremely fast, but this is certainly related to the lack of dependent types and unification, which makes everything much simpler.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135385652):
<p>Anyone who watched <span class="user-mention" data-user-id="110087">@Scott Morrison</span> 's video of his Adelaide talk will have seen a pretty stunning application of <code>backwards_reasoning</code>. It was very well-delivered too. He was formalising proof of infinitely many primes and getting his hands dirty. "Oh we'll just skip this", "oh we'll come back to this later", "Oh Ok so now we've proved there are infinitely many primes modulo 5 sorries which clearly are going to be the hard work", "oh look, globally replacing <code>sorry</code> with <code>backwards_reasoning</code> closes the goal!"</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135385811):
<p>what do you mean lack of unification?</p>

#### [ Scott Morrison (Oct 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386143):
<p>Okay, that demo in Adelaide was a bit misleading. Way too many things were marked <code>@[back]</code>, that in practice we couldn't avoid.</p>

#### [ Scott Morrison (Oct 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386148):
<p>It's going to be a little while before <code>backwards_reasoning</code> or friends really does what it appeared to do there...</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386584):
<p>That doesn't matter. The point was made.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386607):
<p>I will be doing the same thing in Sheffield; showing the audience how proving <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mn>3</mn></msup><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">(x+y)^3=x^3+3x^2y+...</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">3</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mbin">+</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span></span></span></span> is really hard from the axioms and then solving it using automation</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386652):
<p>Mathematicians need to understand that doing simple maths might be simple in Lean.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386668):
<p>The more we say it's true and the more we work on cases where it is not true (like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>≅</mo><mi>B</mi><mo>→</mo><mi>S</mi><mi>p</mi><mi>e</mi><mi>c</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>≅</mo><mi>S</mi><mi>p</mi><mi>e</mi><mi>c</mi><mo>(</mo><mi>B</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">A\cong B\to Spec(A)\cong Spec(B)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">A</span><span class="mrel">≅</span><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mord mathit">p</span><span class="mord mathit">e</span><span class="mord mathit">c</span><span class="mopen">(</span><span class="mord mathit">A</span><span class="mclose">)</span><span class="mrel">≅</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mord mathit">p</span><span class="mord mathit">e</span><span class="mord mathit">c</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mclose">)</span></span></span></span>) the more it will become true</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386691):
<p>If it's easy in maths, we need to try and make it easy in Lean.</p>

#### [ Patrick Massot (Oct 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135388213):
<p>I also liked the backward reasoning demo in Adelaide, but I struggled with the name. Of course I'm not a native English speaker but, to me, <code>backward_reasoning</code> sounds like we are doing something wrong (like using <code>P -&gt; Q</code> to prove <code>P</code> from <code>Q</code>).</p>

#### [ Johan Commelin (Oct 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394086):
<p>How far are we from this turning into a PR?</p>

#### [ Scott Morrison (Oct 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394249):
<p>Close.</p>

#### [ Scott Morrison (Oct 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394254):
<p>But I have grumpy coauthors back in the real world. :-)</p>

#### [ Simon Hudon (Oct 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135406314):
<p>Hi <span class="user-mention" data-user-id="110087">@Scott Morrison</span>! Sorry I got distracted by this sleeping thing. This looks really cool! I think we can do things much faster than going through the whole list of lemmas and we may not hit the performance wall that we did with simp. </p>
<p>A bit like <code>simp</code>, we can index <code>back</code> lemmas using the head symbol of the rhs of its pi type. Then, the number of candidate at each step should be much smaller. I'd have to think some more about further optimizations but I think Isabelle suggests it must be possible to do things really fast</p>

#### [ Scott Morrison (Oct 09 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135436974):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, indexing sounds great. How hard do you think this would be? I'm not confident I could implement it efficiently, but especially if you can give me a pointer to something similar I can give it a try. If I pushed a branch, I'd be very happy if you wanted to look at doing this.</p>

#### [ Scott Morrison (Oct 09 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135436986):
<p>I also want to implement two attributes, analogous to [intro] and [intro!] in Isabelle, for lemmas that it's always safe to apply, vs lemmas that should only be applied if their hypotheses can immediately be solved. I already had this in my original implementation of <code>back</code>, but it's not in the current one. Perhaps I should do this first, and then we can think about indexing?</p>

#### [ Simon Hudon (Oct 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437029):
<p>Sure, no problems. You can also have a look at the user attribute for extensionality if you want to try it before I get into it</p>

#### [ Simon Hudon (Oct 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437035):
<p>Sure</p>

#### [ Simon Hudon (Oct 09 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437056):
<p>You can do one <code>intro</code> attribute and use <code>!</code> as a parameter</p>

#### [ Scott Morrison (Oct 10 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519236):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> , can you point me to examples of using a token like <code>!</code> as a parameter to an attribute?</p>

#### [ Mario Carneiro (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519868):
<p><code>intro!</code> is an attribute</p>

#### [ Mario Carneiro (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519872):
<p>but I think the parsing for that is in core</p>

#### [ Mario Carneiro (Oct 10 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519888):
<p>The parsing for an attribute is just a regular <code>lean.parser</code> monad thing, so you can use <code>tk "!"?</code> to get a possible <code>!</code> token</p>

#### [ Mario Carneiro (Oct 10 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519943):
<p>If you want an example of an attribute with arguments, look at <code>to_additive_attr</code> in <code>algebra.group</code>. You specify the type of the parsed result in one of the optional arguments to <code>user_attribute</code>, and you give the parser itself in the <code>parser := </code> field</p>

#### [ Scott Morrison (Oct 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135520477):
<p>Thanks. I've just made a PR at <a href="#narrow/stream/144837-PR-reviews/subject/.23410.20backwards.20reasoning" title="#narrow/stream/144837-PR-reviews/subject/.23410.20backwards.20reasoning">https://leanprover.zulipchat.com/#narrow/stream/144837-PR-reviews/subject/.23410.20backwards.20reasoning</a>, so perhaps anything further on this thread can go there.</p>


{% endraw %}
