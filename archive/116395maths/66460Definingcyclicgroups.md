---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66460Definingcyclicgroups.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Defining cyclic groups](https://leanprover-community.github.io/archive/116395maths/66460Definingcyclicgroups.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 29 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522081):
<p>I have quite a bit of group theory waiting to be merged, Sylow's theorems and parity of permutation over a <code>fintype</code>. I cannot merge it because it all depends on some definition of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">C_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. Is it worth having both <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex"> \mathbb{Z}_n </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">C_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>? It would be nice to only have one, but then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{Z}_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is an <code>add_group</code> which obviously causes problems.</p>

#### [ Kevin Buzzard (Jul 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522287):
<p>We surely need a cyclic group with * as the group law. Another issue is that Z/nZ has a canonical generator, namely 1, whereas a cyclic group of order n is a group of order n with the property that a generator exists. A great example of a cyclic group is the units in (Z/pZ), with p prime. The standard proof that it's cyclic is completely nonconstructive.</p>

#### [ Chris Hughes (Jul 29 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522597):
<p>Why would the presence of a canonical generator be a problem? If you don't want it, just ignore it. Any sensible computable version of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">C_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> will have a canonical generator anyway, as it should probably be defeq to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{Z}_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> anyway.</p>

#### [ Kenny Lau (Jul 29 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522607):
<blockquote>
<p>We surely need a cyclic group with * as the group law. Another issue is that Z/nZ has a canonical generator, namely 1, whereas a cyclic group of order n is a group of order n with the property that a generator exists. A great example of a cyclic group is the units in (Z/pZ), with p prime. The standard proof that it's cyclic is completely nonconstructive.</p>
</blockquote>
<p>under which definition of nonconstructive?</p>

#### [ Chris Hughes (Jul 29 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522652):
<p>If you gave me a proof of that I could very easily construct a generator.</p>

#### [ Mario Carneiro (Jul 29 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523620):
<p>I think <code>is_cyclic</code> should be a <em>property</em> of a <code>group</code>, not a particular group</p>

#### [ Mario Carneiro (Jul 29 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523623):
<p>and the Fundamental Theorem of Cyclic groups says that two cyclic groups with the same cardinality are isomorphic</p>

#### [ Kenny Lau (Jul 29 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523672):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">cyclic_group</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">group</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cyclic</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">i</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">a</span><span class="err">^</span><span class="n">i</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523674):
<p><a href="https://github.com/dorhinj/leanstuff/blob/master/gourp1.lean" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/master/gourp1.lean">https://github.com/dorhinj/leanstuff/blob/master/gourp1.lean</a></p>

#### [ Mario Carneiro (Jul 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523681):
<p>yes, except I don't think it should be part of the hierarchy</p>

#### [ Kenny Lau (Jul 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523685):
<p>code not by me</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523724):
<p>I know, chris reads this too</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523733):
<p>It is certainly not true that you can construct a generator given a cyclic group</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523734):
<p>you can at best construct a <code>trunc generator</code> given a <code>fintype</code> or <code>enumerable</code> cyclic group</p>

#### [ Chris Hughes (Jul 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523773):
<blockquote>
<p>I think <code>is_cyclic</code> should be a <em>property</em> of a <code>group</code>, not a particular group</p>
</blockquote>
<p>But we also obviously need the fact that for all n, there exists a cyclic group of order n.</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523778):
<p>maybe, but it depends on how you want to say it</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523783):
<p>How would you need that?</p>

#### [ Chris Hughes (Jul 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523828):
<p>Parity of a permutation is a homomorphism into <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">C_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. In my Sylow proof I needed to use the group action of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">C_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.969438em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> that rotated the elements of a vector <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>G</mi><mi>p</mi></msup></mrow><annotation encoding="application/x-tex">G^p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">G</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Mario Carneiro (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523874):
<p>For the parity example, I'm on board with Kenny's <code>mu2</code>, although I'm not sure what the name stands for</p>

#### [ Kenny Lau (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523876):
<p>mu_n is the set of the n-th roots of unity in a field</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523877):
<p>For the group action, that's obviously a subgroup of the group action of the symmetric group</p>

#### [ Kenny Lau (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523878):
<p>I learnt it from LCFT, but I don't know if it is used elsewhere</p>

#### [ Kenny Lau (Jul 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523883):
<p>and for the record Kevin wrote that part (and the name)</p>

#### [ Chris Hughes (Jul 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523927):
<p>For the Sylow one, I needed to use the map from the naturals to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{Z}_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, so some random subgroup is not that easy to use.</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523976):
<p>I guess you want to know that <code>rotate</code> is a group hom from <code>Z</code> to the symmetric group</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523980):
<p>and its image is cyclic, because the image of any group hom from Z is cyclic</p>

#### [ Chris Hughes (Jul 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523984):
<p>More or less. Maybe I could do it differently.</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524043):
<p>I realize that mathematicians are used to treating <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">C_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> as one thing, but keeping in mind the isomorphism is equality abuse of notation in this area, it's best to allow for cyclic groups to appear in situ</p>

#### [ Mario Carneiro (Jul 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524095):
<p>That said, if you really need a concrete cyclic additive group <code>Zmod n</code> will do the job</p>

#### [ Kenny Lau (Jul 29 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524100):
<p><code>multiplicative (Zmod n)</code></p>

#### [ Chris Hughes (Jul 29 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524105):
<p>That's what I used for Sylow. It wasn't that pretty.</p>


{% endraw %}
