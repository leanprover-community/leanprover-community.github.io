---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06660metatacticwithunfold.html
---

## Stream: [new members](index.html)
### Topic: [meta tactic with unfold](06660metatacticwithunfold.html)

---


{% raw %}
#### [ Sarah Mameche (Nov 19 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20tactic%20with%20unfold/near/147963936):
Is there an equivalent to 'tactic.apply' with unfold? I have a ```meta```tactic that rewrites with specific lemmas which are given as a ```pexpr``` : 

```lean
meta def rw_pexpr (e : pexpr) : tactic unit := 
do e ← tactic.to_expr e, 
  t ← target, 
  (p,h,_) ← tactic.rewrite e t, 
  replace_target p h 
```
It works for rewriting if the ```pexpr```is a lemma, but not if it is a definition (even though doing rw with the definition interactively works). What can I do if I want to unfold the definition using the meta tactic?

#### [ Mario Carneiro (Nov 19 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20tactic%20with%20unfold/near/147964349):
use `get_equation_lemmas` to get a list of simp lemmas for a definition


{% endraw %}
