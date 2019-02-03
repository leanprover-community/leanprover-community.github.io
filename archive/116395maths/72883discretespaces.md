---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72883discretespaces.html
---

## Stream: [maths](index.html)
### Topic: [discrete spaces](72883discretespaces.html)

---


{% raw %}
#### [ Reid Barton (Oct 19 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete%20spaces/near/136077573):
<blockquote>
<p><strong><a href="https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a" target="_blank" title="https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a">feat(analysis/topology): add type class for discrete topological spaces</a></strong><br>
feat(analysis/topology): add type class for discrete topological spaces<br>
<a href="https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a" target="_blank" title="https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a">https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a</a></p>
</blockquote>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> nice! This is something I was also considering adding, compare <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/for_mathlib/analysis_topology_topological_space.lean" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/for_mathlib/analysis_topology_topological_space.lean">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/for_mathlib/analysis_topology_topological_space.lean</a>. I was thinking of making it an alternative branch in the <code>topological_space &lt;- uniform_space &lt;- metric_space</code> chain; in the link I put it on top of <code>topological_space</code> but it could easily go on top of <code>uniform_space</code> instead.<br>
Thoughts?</p>

#### [ Reid Barton (Oct 19 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete%20spaces/near/136077725):
<p>The advantage is that you wouldn't need all those separate instances for spaces like <code>nat</code>--the disadvantage is you have to be a bit careful to define the instances for things like products and sums correctly, I guess.</p>

#### [ Johannes Hölzl (Oct 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete%20spaces/near/136094635):
<p>I wonder if there exists a case where we have a discrete topology, but one still additional topological structures on it. For example <code>orderable_topology</code> doesn't hold for all discrete spaces. Of course <code>orderable_topology</code> is a mixin in itself so it would fit. But I prefer the flexibility we get from mixins. And I guess <code>discrete_topology</code> isn't used too often so writing two parameters instead of one shouldn't be too hard.<br>
Hence, I would like to keep it as an mixin (i.e. a predicate, not containing the toplogical structure).</p>

#### [ Reid Barton (Oct 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete%20spaces/near/136112844):
<p>Ah, I see. I can imagine a situation where you have a manifold or a topological ring or something, and then also want to assume or prove that the topology is discrete. Makes sense.</p>


{% endraw %}
