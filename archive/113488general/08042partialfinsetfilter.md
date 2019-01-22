---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08042partialfinsetfilter.html
---

## [general](index.html)
### [partial finset.filter?](08042partialfinsetfilter.html)

#### [Kenny Lau (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20finset.filter%3F/near/133493792):
Currently:
```lean
finset.filter : Π {α : Type u_1} (p : α → Prop) [_inst_3 : decidable_pred p], finset α → finset α
```
I wonder if there's a similar function, but instead of defining `p` everywhere, just define it on the input finset?

