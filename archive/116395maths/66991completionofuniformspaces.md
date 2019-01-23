---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66991completionofuniformspaces.html
---

## Stream: [maths](index.html)
### Topic: [completion of uniform spaces](66991completionofuniformspaces.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 25 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/completion%20of%20uniform%20spaces/near/128617201):
The perfectoid projects crucially needs completions of topological rings. I can see mathlib already has a lot about [completion of uniform spaces](https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102) but I also remember the definition of real numbers was changed by @**Mario Carneiro**. Is there anything we should know before doing completions of topological rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 26 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/completion%20of%20uniform%20spaces/near/128630553):
All the material for completion of topological rings via uniform completion is still there. It simply isn't being used to construct the reals anymore, since the direct construction is better in a number of other ways. If you have need for a generic completion operator in a more abstract context, feel free to use it


{% endraw %}
