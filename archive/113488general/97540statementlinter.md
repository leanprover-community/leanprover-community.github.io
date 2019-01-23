---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97540statementlinter.html
---

## Stream: [general](index.html)
### Topic: [statement linter](97540statementlinter.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 26 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130305793):
I have a new challenge in the same style as the `print_names` command, but harder. We all know how to produce the list of everything defined in the current Lean file. Now we want to filter the result, keeping only lemmas or theorems whose input contains two instances for the same type class. For instance, running this command in https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean must return (among others) `is_closed_diagonal` since:
```lean
import analysis.topology.continuity

#check @is_closed_diagonal
/-
is_closed_diagonal :
  ∀ {α : Type u_1} [_inst_1 : topological_space α] [_inst_4 : topological_space α] [_inst_5 : t2_space α],
    is_closed {p : α × α | p.fst = p.snd}
-/
```
(this is due to instance explicitly asked for in the statement but already present as variables).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 26 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130308512):
oops!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 26 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130312325):
Hint: if `t` is the type of `is_closed_diagonal`, `t.is_pi` will return `tt` (true) because `t` is a pi type (the assumptions are basically function arguments). `t.binding_domain` will gives you the type of the first assumption or variable  (i.e. `Type u_1`) and `t.binding_body` will be the rest (i.e. `∀ [_inst_1 : topological_space α] [_inst_4 : topological_space α] [_inst_5 : t2_space α], is_closed {p : α × α | p.fst = p.snd}`). Look at their definition and write a `arguments : expr → tactic (list expr)` function. This will bring you closer to a solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130328113):
Thank you very much, I'll try to work on this exercise soon (but not right now).

