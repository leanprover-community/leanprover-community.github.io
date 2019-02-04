---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57356ACountingArgument.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [A Counting Argument](https://leanprover-community.github.io/archive/113488general/57356ACountingArgument.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Lee (Feb 03 2019 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157461356):
<p>I am trying to prove: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">HG</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">G</span> <span class="bp">=</span> <span class="mi">2</span><span class="bp">*</span><span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="n">G</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span><span class="bp">⁻¹</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>The idea of the proof is to partition the group into sets of elements with their inverses. If there are no non-identity self-inverting elements, then the group would have odd order, giving a contradiction. But I am lost as to how to formalise this into Lean.</p>

#### [ Neil Strickland (Feb 03 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157462511):
<p>I would start with <code>fintype.exists_equiv_fin</code>, which will give you a bijection <code>f</code> from <code>G</code> to <code>fin (2 * k)</code>.  You can then use <code>univ.filter</code> to split <code>G</code> into sets where <code>f(g)</code> is less than, or greater than, or equal to <code>f(g^{-1})</code>.  Then you can show that inversion gives a bijection between the first two of these.</p>

#### [ Mario Carneiro (Feb 03 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157462588):
<p>I would prove that inv is an involution on G, and its orbits have size 2 or 1... then it's just actual counting</p>

#### [ Mario Carneiro (Feb 03 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157462645):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> is pretty good at this stuff, I wonder if he's tried this</p>

#### [ Neil Strickland (Feb 03 2019 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157463021):
<p>That approach seems to need some infrastructure, e.g. a lemma that the cardinality of the union of a finite set of disjoint finite sets is the sum of the cardinalities.  It would certainly be good if that was in mathlib, but I cannot find it there at the moment.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466117):
<p>Perhaps related: <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/xenalib/keji_lemma.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/xenalib/keji_lemma.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/xenalib/keji_lemma.lean</a></p>

#### [ Kevin Buzzard (Feb 03 2019 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466175):
<p>Keji had a map gbar from s to s and a function f on s such that f(x)+f(gbar x) was zero, and wanted to prove that the sum of f over all of s was zero. I muddled through in the above link. I remember it being annoying, but not ever really getting stuck.</p>

#### [ Chris Hughes (Feb 03 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466247):
<p>I don't think it is relevant. What is weirdly relevant is a lemma in <code>sylow</code>, <code>card_modeq_card_fixed_points</code> since inv is an action of C_2 on the group.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466289):
<p>Aah, he also had the hypothesis that f(x) wasn't f(gbar x). Chris -- if you allow Sylow then you can just show that there exists a non-trivial Sylow 2-subgroup and then invoke the lemma that every non-trivial p-group has an element of order p :-)</p>

#### [ Kevin Buzzard (Feb 03 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466296):
<p>The proof Ken mentions (which I've lectured in 2nd year algebra) is a workaround which only works for p=2.</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466660):
<p>isn't the composition of those two facts Cauchy's theorem (there is an element of order p in a group G when p | |G|)</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466665):
<p>it's usually a lemma in Sylow</p>

#### [ Kevin Buzzard (Feb 03 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466734):
<p>Right. But the general proof needs groups acting on sets etc, which we don't teach until Y3, and this p=2 version is useful for 2nd years trying to figure out what all the groups of order 6 are by bare hands.</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466735):
<p>but actually yeah that's definitely easier than the counting argument</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466738):
<p>unless there is some silly restriction on "allowable proofs"</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466791):
<blockquote>
<p>That approach seems to need some infrastructure, e.g. a lemma that the cardinality of the union of a finite set of disjoint finite sets is the sum of the cardinalities. It would certainly be good if that was in mathlib, but I cannot find it there at the moment.</p>
</blockquote>
<p>I think there is a theorem in equiv about splitting a type along the fibers of a function</p>

#### [ Mario Carneiro (Feb 03 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466838):
<p><code>equiv_sigma_subtype</code></p>

#### [ Mario Carneiro (Feb 03 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157466954):
<blockquote>
<p>all the groups of order 6 are by bare hands</p>
</blockquote>
<p>I wonder if we can make a group enumeration function? Like the list of all groups of order 6 up to isomorphism, such that you can check that it has cardinality 2</p>

#### [ Kevin Buzzard (Feb 03 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157470782):
<p>The naive algorithm for listing all the groups of order 6 up to isomorphism will take forever even in a non-proof-checker computer algebra package. What you want to do is to assume all Chris' Sylow stuff and then make a formally verified database of groups of small order containing each one up to isomorphism exactly once.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157470935):
<p>A completely low-level approach, which is pretty horrible, goes like this: all elements have order 1,2,3 or 6. If there's an element of order 6 then it's cyclic. If not then all non-identity elements have orders 2 or 3. By Ken's lemma there's an element of order 2. If all non-identity elements have order 2 then the group is abelian (this is on the problem sheet; <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mi>y</mi><mi>x</mi><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">xyxy=1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.8388800000000001em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">x</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span> so <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mi>y</mi><mo>=</mo><msup><mi>y</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>y</mi><mi>x</mi></mrow><annotation encoding="application/x-tex">xy=y^{-1}x^{-1}=yx</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.008548em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">x</span></span></span></span>) and choosing two elements of order 2 gives a subgroup of order 4, contradiction. So there's an element of order 3 as well, Now we have names for every element -- if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">s</span></span></span></span> has order 2 and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi></mrow><annotation encoding="application/x-tex">t</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">t</span></span></span></span> has order 3 then the group is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mn>1</mn><mo separator="true">,</mo><mi>t</mi><mo separator="true">,</mo><msup><mi>t</mi><mn>2</mn></msup><mo separator="true">,</mo><mi>s</mi><mo separator="true">,</mo><mi>s</mi><mi>t</mi><mo separator="true">,</mo><mi>s</mi><msup><mi>t</mi><mn>2</mn></msup><mo>}</mo></mrow><annotation encoding="application/x-tex">\{1,t,t^2,s,st,st^2\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord mathrm">1</span><span class="mpunct">,</span><span class="mord mathit">t</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mord mathit">s</span><span class="mpunct">,</span><span class="mord mathit">s</span><span class="mord mathit">t</span><span class="mpunct">,</span><span class="mord mathit">s</span><span class="mord"><span class="mord mathit">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mclose">}</span></span></span></span> and it's just a case of working out <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>t</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">ts</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.61508em;"></span><span class="strut bottom" style="height:0.61508em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">t</span><span class="mord mathit">s</span></span></span></span>; you go through the possibilities and figure out what's going on It's pretty tedious.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157470951):
<p>Sylow tells you immediately that there's a normal subgroup of order 3 and hence it's a semidirect product of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mn>3</mn></msub></mrow><annotation encoding="application/x-tex">C_3</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">C_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>; the two actions of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">C_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mn>3</mn></msub></mrow><annotation encoding="application/x-tex">C_3</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> give the two groups.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157471002):
<p>I think that before we classify finite groups of small order it would be wise to classify finite abelian groups of small order, which follows from the structure theorem of finitely-generated modules over a PID.</p>

#### [ Kevin Buzzard (Feb 03 2019 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157471017):
<p>We have all the tools for this latter result, but it's a pretty messy proof (at least the ones I've seen are). It's easier to do classification of f.g. modules over a Euclidean domain (which has the same answer), but my impression is that there's no point doing this really because ultimately we'll want PID's.</p>

#### [ Mario Carneiro (Feb 03 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157484127):
<p>The problem with this kind of argumentation is it's really tailored to the particular order (6 in this case). If you want to do the same thing with 1024 it's hopeless. I want to know if there is some in between algorithm, which uses group theory tricks but may still produce duplicates which have to be eliminated the hard way</p>

#### [ Kenny Lau (Feb 03 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157484131):
<p>We don't even know how many groups of order 2048 there are</p>

#### [ Kevin Buzzard (Feb 03 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157485619):
<p>This sort of problem is notoriously difficult</p>

#### [ Kevin Buzzard (Feb 03 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157485692):
<p>After a while we don't even have good notion. You have to start saying "well here's the multiplication table...". The problem is with p-groups (groups of prime power order). There are 20 groups of order 16 and by order 32 I think there are groups without names -- they're called "the 23rd one on the GAP database of groups of order 32" and things like that</p>

#### [ Mario Carneiro (Feb 04 2019 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157489478):
<p>Is there an upper bound on the number of groups up to isomorphism asymptotically better than the naive one?</p>

#### [ Mario Carneiro (Feb 04 2019 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157489613):
<p>If you view it as n permutations you get (n!)^n, which you can probably improve if you use the fact that it's a permutation in columns too, although that seems complicated</p>

#### [ Reid Barton (Feb 04 2019 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20Counting%20Argument/near/157492745):
<p><a href="https://groupprops.subwiki.org/wiki/Higman-Sims_asymptotic_formula_on_number_of_groups_of_prime_power_order" target="_blank" title="https://groupprops.subwiki.org/wiki/Higman-Sims_asymptotic_formula_on_number_of_groups_of_prime_power_order">https://groupprops.subwiki.org/wiki/Higman-Sims_asymptotic_formula_on_number_of_groups_of_prime_power_order</a></p>


{% endraw %}
