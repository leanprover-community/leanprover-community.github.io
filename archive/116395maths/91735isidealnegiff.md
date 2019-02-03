---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/91735isidealnegiff.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [is_ideal.neg_iff](https://leanprover-community.github.io/archive/116395maths/91735isidealnegiff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Oct 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313777):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">ideals</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">N</span><span class="o">]</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="bp">-</span><span class="n">a</span> <span class="err">∈</span> <span class="n">N</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- rwa is_ideal.neg_iff at h,</span>
  <span class="n">rwa</span> <span class="bp">@</span><span class="n">is_ideal</span><span class="bp">.</span><span class="n">neg_iff</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">N</span> <span class="bp">_</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Why can't I use the first line?</p>

#### [ Patrick Massot (Oct 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313787):
<p>Looks like it makes that lemma unusable</p>

#### [ Patrick Massot (Oct 06 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313830):
<p>Recall <code>lemma neg_iff {S : set α} [is_ideal S] : a ∈ S ↔ -a ∈ S := ⟨is_submodule.neg, λ h, neg_neg a ▸ is_submodule.neg h⟩</code></p>

#### [ Chris Hughes (Oct 06 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313839):
<p>The set should be explicit. I'm not sure why it happens, but it's the same with <code>rw</code>s for <code>is_group_hom</code>, the function that is a <code>group_hom</code> needs to be given explicitly.</p>

#### [ Patrick Massot (Oct 06 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313939):
<p>So you suggest modifying the binder in the statement of the lemma?</p>

#### [ Reid Barton (Oct 06 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314381):
<p>Maybe it's because <code>a ∈ S</code> is really just <code>S a</code>, that is, a variable function applied to a variable argument. Lean is probably unwilling to try to guess both the function and the argument.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314387):
<p>But it shouldn't be unfolding this at all, right?</p>

#### [ Reid Barton (Oct 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314392):
<p>Yeah that part I am not sure about.</p>


{% endraw %}
