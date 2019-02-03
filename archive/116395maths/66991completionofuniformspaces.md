---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66991completionofuniformspaces.html
---

## Stream: [maths](index.html)
### Topic: [completion of uniform spaces](66991completionofuniformspaces.html)

---


{% raw %}
#### [ Patrick Massot (Jun 25 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/completion%20of%20uniform%20spaces/near/128617201):
<p>The perfectoid projects crucially needs completions of topological rings. I can see mathlib already has a lot about <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102">completion of uniform spaces</a> but I also remember the definition of real numbers was changed by <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>. Is there anything we should know before doing completions of topological rings?</p>

#### [ Mario Carneiro (Jun 26 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/completion%20of%20uniform%20spaces/near/128630553):
<p>All the material for completion of topological rings via uniform completion is still there. It simply isn't being used to construct the reals anymore, since the direct construction is better in a number of other ways. If you have need for a generic completion operator in a more abstract context, feel free to use it</p>


{% endraw %}
