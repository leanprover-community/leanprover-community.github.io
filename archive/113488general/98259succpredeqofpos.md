---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98259succpredeqofpos.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [succ_pred_eq_of_pos](https://leanprover-community.github.io/archive/113488general/98259succpredeqofpos.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/succ_pred_eq_of_pos/near/132638437):
<p><code>succ_pred_eq_of_pos</code> says <code>n &gt; 0 → succ (pred n) = n</code> and it's in core Lean. I just applied it and ended up with a goal <code>card s &gt; 0</code> with <code>s</code> a multiset, and then I tried to rewrite <code>multiset.card_pos_iff_exists_mem</code> but the rewrite fails because the hypothesis is <code>0 &lt; card s</code>. That's kind of annoying and it's not the first time today that this has happened to me. I feel like <code>succ_pred_eq_of_pos</code> should say <code>0 &lt; n  → succ (pred n) = n</code> but I guess there's nothing that can be done about this? Or am I missing a trick? Currently I'm just using <code>show</code> to rewrite the goal so it uses <code>&lt;</code>.</p>


{% endraw %}
