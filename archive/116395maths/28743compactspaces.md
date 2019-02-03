---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28743compactspaces.html
---

## Stream: [maths](index.html)
### Topic: [compact spaces](28743compactspaces.html)

---


{% raw %}
#### [ Reid Barton (Sep 22 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134451428):
<p>I'm inclined to add the following class, following the naming scheme of <code>t2_space</code>, <code>separable_space</code>, etc.</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">compact_space</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">compact_univ</span> <span class="o">:</span> <span class="n">compact</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span>
</pre></div>


<p>Advantages: we can write a lot of instances, and various theorems have "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> compact" as a hypothesis, and it's not always possible or useful to generalize to "Let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> be a compact subset of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span>".</p>

#### [ Reid Barton (Sep 22 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134451430):
<p>Any thoughts?</p>

#### [ Kevin Buzzard (Sep 22 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134452154):
<p>My only comment was that ever since I saw the definition of compact I was surprised it applied to a subspace rather than the space. What is the advantage of the subset approach? It's not how mathematicians traditionally do it.</p>

#### [ Mario Carneiro (Sep 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134455015):
<p>I agree. I don't think there is much advantage to working with subsets here, since you get exactly the right behavior with <code>compact_space s</code> with the subtype coercion</p>


{% endraw %}
