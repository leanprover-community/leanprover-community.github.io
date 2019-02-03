---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/40095finsetsubsetunion.html
---

## Stream: [new members](index.html)
### Topic: [finset.subset_union_*](40095finsetsubsetunion.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Sep 16 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134038959):
<p>Is there a reason why <code>finset.subset_union_left</code> and <code>finset.subset_union_right</code>have implicit arguments <code>{s₁ s₂ : finset α}</code> and the corresponding <code>set.</code> theorems have explicit arguments <code>(s t : set α)</code>?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134045419):
<p>These questions seem a bit subtle to me. The answer might be because this is one of those functions where you sometimes want the arguments to be implicit and sometimes explicit, depending on the exact context. In those cases what is the best choice?</p>

#### [ Chris Hughes (Sep 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134045517):
<p>Given that <code>mem_union_left</code> exists, I think they should be explicit.</p>

#### [ Bryan Gin-ge Chen (Sep 16 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134053191):
<p>That's what I thought too. <a href="https://github.com/leanprover/mathlib/pull/353" target="_blank" title="https://github.com/leanprover/mathlib/pull/353">PR here</a>.</p>


{% endraw %}
