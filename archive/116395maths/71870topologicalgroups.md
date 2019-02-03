---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71870topologicalgroups.html
---

## Stream: [maths](index.html)
### Topic: [topological groups](71870topologicalgroups.html)

---


{% raw %}
#### [ Patrick Massot (Sep 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20groups/near/133277465):
<p>I pushed to <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean</a> the current state of my work on completions of uniform groups. I would really appreciate help (from Mario, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> or anyone else) with understanding how one should setup the instance maze (or use definitions instead of instances) to be able to finish <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161</a> (assume I can prove <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124</a>). I'd be ready to have the uniform space structure on a topological group to be outside the type class system, especially since we would ideally also like to handle non-commutative groups at some point, and those have two natural uniform structures. But I don't know how to use them if there are not instances (everything else uses instance implicit arguments).</p>


{% endraw %}
