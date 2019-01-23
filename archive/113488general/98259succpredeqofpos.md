---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98259succpredeqofpos.html
---

## Stream: [general](index.html)
### Topic: [succ_pred_eq_of_pos](98259succpredeqofpos.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/succ_pred_eq_of_pos/near/132638437):
`succ_pred_eq_of_pos` says `n > 0 → succ (pred n) = n` and it's in core Lean. I just applied it and ended up with a goal `card s > 0` with `s` a multiset, and then I tried to rewrite `multiset.card_pos_iff_exists_mem` but the rewrite fails because the hypothesis is `0 < card s`. That's kind of annoying and it's not the first time today that this has happened to me. I feel like `succ_pred_eq_of_pos` should say `0 < n  → succ (pred n) = n` but I guess there's nothing that can be done about this? Or am I missing a trick? Currently I'm just using `show` to rewrite the goal so it uses `<`.


{% endraw %}
