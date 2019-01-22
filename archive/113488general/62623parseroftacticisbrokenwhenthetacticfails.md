---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62623parseroftacticisbrokenwhenthetacticfails.html
---

## [general](index.html)
### [parser.of_tactic is broken when the tactic fails](62623parseroftacticisbrokenwhenthetacticfails.html)

#### [Mario Carneiro (Aug 31 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser.of_tactic%20is%20broken%20when%20the%20tactic%20fails/near/133093024):
I just stumbled on the following issue:
```
open tactic
meta def test : tactic unit := failed
meta def tac (_ : interactive.parse test) := skip
run_cmd add_interactive [`tac]
example : true := by tac.
-- vm check failed: is_closure(o) (possibly due to incorrect axioms, or sorry)
```
The problem appears to be that nothing catches an error thrown in a tactic when it is passed through the `of_tactic` builtin function

