---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/15161powerseries.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [power series](https://leanprover-community.github.io/archive/116395maths/15161powerseries.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jan 26 2019 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156894024):
<p>Has anyone built formal power series yet?</p>

#### [ Kenny Lau (Jan 26 2019 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156894121):
<p>just take <span class="tex-error">$$\varprojlim_{n \in \Bbb N} A[X]/(X^n)$$</span> :P</p>

#### [ Kevin Buzzard (Jan 26 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156915982):
<p>This is an interesting question. I believe Patrick has done ring completions so that would be one approach. Alternatively one could just take the stuff on polynomial rings and just delete all the finite support hypotheses! In retrospect power series would have been easier to write than polynomials I guess?</p>

#### [ Kevin Buzzard (Jan 26 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156916113):
<p>These seem like two genuinely different approaches. Which would be best?</p>

#### [ Mario Carneiro (Jan 26 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156916161):
<p>yes, power series are easier than polynomials, although you still need some finiteness for the monomials so that multiplication is well defined</p>

#### [ Mario Carneiro (Jan 26 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156916229):
<p>That said, it's not clear to me which power series ring is the most useful - there are many ways to generalize bits of the polynomial construction, like Laurent series</p>

#### [ Kevin Buzzard (Jan 26 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156917121):
<p>From an algebraic geometry point of view, the power series ring <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mo>[</mo><mi>X</mi><mo>]</mo><mo>]</mo></mrow><annotation encoding="application/x-tex">R[[X]]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span><span class="mclose">]</span></span></span></span> is the most important missing thing, i.e. a ring structure on <code>nat -&gt; R</code>.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156917139):
<p>If you import <code>algebra.pi_instances</code> I think you get a multiplication on these functions, which is pointwise multiplication on the target, but that's the wrong one.</p>

#### [ Patrick Massot (Jan 26 2019 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156917943):
<p>This is clearly a case for type wrapping. Define <code>power_series R = nat -&gt; R</code> and define the correct instance</p>

#### [ Patrick Massot (Jan 26 2019 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156917993):
<p>Unfold and apply_instance for addition</p>

#### [ Kevin Buzzard (Jan 26 2019 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156918007):
<p>If I unfold <code>power_series R</code> will this then actually change what <code>apply_instance</code> finds for multiplication? i.e. can I get some code which changes behaviour if I insert an "unfold"?</p>

#### [ Mario Carneiro (Jan 26 2019 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156918349):
<p>yes, well, the typeclass instance inferred can change</p>

#### [ Mario Carneiro (Jan 26 2019 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156918390):
<p>if you just unfold you will still have the original instance, it will just be a nonstandard typeclass term at that point</p>

#### [ Reid Barton (Jan 26 2019 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156922769):
<p>So there are also some new phenomena which arise for power series, for example:</p>
<ul>
<li>If F(X) and G(X) are power series then we can make sense of F(G(X)) if the constant term of G is zero. I guess the proper generalization is that if F(X) in R[[X]], a in I and R is I-adically complete then we can evaluate F(a). Do we already have these latter notions (maybe in the perfectoid spaces project)?</li>
<li>If F(X) = u X + ... with u a unit in R then we can find an inverse power series G(X) = u^-1 X + ... Is this related to Hensel's lemma?</li>
</ul>

#### [ Kevin Buzzard (Jan 26 2019 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156924334):
<p>The notion of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>I</mi></mrow><annotation encoding="application/x-tex">I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span>-adically complete will be in the perfectoid space project, although I am not sure we have a good API for it. The "correct" way to do this would be to go through some book like Atiyah--Macdonald I guess, whereas we just needed the definition. This stuff will come as I start actually having to use the notion of completeness in lemmas (this is imminent but has not yet happened; I've spent the last two weeks writing references and dealing with other work admin, but my urgent work job list is now very small). Inverse power series -- this is not Hensel. It's the statement that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mo>[</mo><mi>X</mi><mo>]</mo><mo>]</mo><mo>=</mo><mi>R</mi><mo>[</mo><mo>[</mo><mi>F</mi><mo>]</mo><mo>]</mo></mrow><annotation encoding="application/x-tex">R[[X]]=R[[F]]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span><span class="mclose">]</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mclose">]</span><span class="mclose">]</span></span></span></span> which is something else. Hensel (in its full generality -- we only have it for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{Z}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span>) provides roots in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mo>[</mo><mi>X</mi><mo>]</mo><mo>]</mo></mrow><annotation encoding="application/x-tex">R[[X]]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span><span class="mclose">]</span></span></span></span> of polynomials with coefficients in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mo>[</mo><mi>X</mi><mo>]</mo><mo>]</mo></mrow><annotation encoding="application/x-tex">R[[X]]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span><span class="mclose">]</span></span></span></span> in favourable circumstances.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156927185):
<p><a href="https://github.com/leanprover-community/perfectoid-spaces/tree/master/src/for_mathlib" target="_blank" title="https://github.com/leanprover-community/perfectoid-spaces/tree/master/src/for_mathlib">https://github.com/leanprover-community/perfectoid-spaces/tree/master/src/for_mathlib</a> is the topology on a ring generated by an ideal of the ring</p>

#### [ Patrick Massot (Jan 26 2019 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/power%20series/near/156935544):
<p>We do have everything to define I-adically complete in the perfectoid project: the adic-topology and completeness for topological rings</p>


{% endraw %}
