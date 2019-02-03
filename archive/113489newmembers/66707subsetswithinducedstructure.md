---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/66707subsetswithinducedstructure.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [subsets with induced structure](https://leanprover-community.github.io/archive/113489newmembers/66707subsetswithinducedstructure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jean Lo (Nov 19 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subsets%20with%20induced%20structure/near/147981000):
<p>Given a set with some structure, I often would like to think about its subsets that also have a similar structure on it. This seems like a pretty common construction — what would be the idiomatic way to formulate such things in Lean?</p>
<p>Here's a particular example encountered in an attempt to formalise some algebra notes:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="c1">-- what I had previously. This is unsatisfactory for a number of</span>
<span class="c1">-- reasons, including the fact that it doesn&#39;t force me to use the</span>
<span class="c1">-- operation on `G` when constructing `group H`, which means I&#39;m</span>
<span class="c1">-- not proving what I really want to prove.</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">G</span><span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="n">def</span> <span class="n">H</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">g</span><span class="o">:</span> <span class="n">G</span> <span class="bp">//</span> <span class="n">true</span> <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">subgroup_self</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]:</span> <span class="n">group</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="c1">-- (also, this is incorrect, seemingly because H is of type `Type u_2`?</span>
<span class="c1">--  I don&#39;t understand what exactly is happening.)</span>


<span class="c1">-- I searched mathlib for examples, and the only similar thing I managed</span>
<span class="c1">-- to find was `submodule`. Mimicking its definition, I&#39;ve written down:</span>

<span class="kn">structure</span> <span class="n">subgroup</span> <span class="o">(</span><span class="n">G</span><span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">:=</span>
  <span class="o">(</span><span class="n">carrier</span><span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span>
  <span class="o">(</span><span class="n">one</span><span class="o">:</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">G</span><span class="o">)</span> <span class="err">∈</span> <span class="n">carrier</span><span class="o">)</span>
  <span class="o">(</span><span class="n">closed</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">g</span> <span class="n">h</span><span class="o">:</span> <span class="n">G</span><span class="o">,</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">carrier</span> <span class="bp">→</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">carrier</span> <span class="bp">→</span> <span class="n">g</span> <span class="bp">*</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">carrier</span><span class="o">)</span>
  <span class="o">(</span><span class="n">inv</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">g</span><span class="o">:</span> <span class="n">G</span><span class="o">,</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">carrier</span> <span class="bp">→</span> <span class="n">g</span><span class="bp">⁻¹</span> <span class="err">∈</span> <span class="n">carrier</span><span class="o">)</span>

<span class="c1">-- now I think I can explicitly construct terms of type `subgroup` by</span>
<span class="c1">-- putting together proofs that a certain carrier set has the desired</span>
<span class="c1">-- properties — but how do I formulate things like `subgroup_self`,</span>
<span class="c1">-- and other assertions that are shaped like &#39;this given subset of G</span>
<span class="c1">-- is a subgroup of G&#39; ?</span>
</pre></div>


<p>In conversations elsewhere, I've heard mentions of <code>is_subgroup</code> and <code>is_submodule</code>, though I've also been told that <code>is_submodule</code> has been replaced, and indeed I could find neither definition in my copy of mathlib.</p>

#### [ Bryan Gin-ge Chen (Nov 19 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subsets%20with%20induced%20structure/near/147981206):
<p>I'm not sure how old your version of mathlib is but <code>is_subgroup</code> has been in <code>group_theory.subgroup</code> for long time <a href="https://github.com/leanprover/mathlib/blob/8ae3fb86f09daab0a48a4b81e19c1eee7552be10/group_theory/subgroup.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/8ae3fb86f09daab0a48a4b81e19c1eee7552be10/group_theory/subgroup.lean">https://github.com/leanprover/mathlib/blob/8ae3fb86f09daab0a48a4b81e19c1eee7552be10/group_theory/subgroup.lean</a></p>

#### [ Jean Lo (Nov 19 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subsets%20with%20induced%20structure/near/147981678):
<p>oh, in <code>group_theory/</code>, of course! I've been having trouble with <code>helm-lean-definitions</code> and have been looking in <code>algebra/group.lean</code> this whole time. Sorry for that.</p>
<p>So what are the differences between how <code>is_subgroup</code> and <code>submodule</code>are defined? when should one way of doing it be preferred over the other?</p>

#### [ Bryan Gin-ge Chen (Nov 19 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subsets%20with%20induced%20structure/near/147981908):
<p>Good question! I'm not sure how the new <code>submodule</code> stuff works myself.</p>


{% endraw %}
