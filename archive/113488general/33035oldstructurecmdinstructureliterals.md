---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33035oldstructurecmdinstructureliterals.html
---

## Stream: [general](index.html)
### Topic: [old_structure_cmd in structure literals](33035oldstructurecmdinstructureliterals.html)

---

#### [Mario Carneiro (Nov 05 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/old_structure_cmd%20in%20structure%20literals/near/146821394):
Here's a strange discovery:
```lean
import order.complete_lattice

namespace lattice
set_option old_structure_cmd false

def complete_lattice.copy {α} (c : complete_lattice α)
  (le : α → α → Prop) (eq_le : le = @complete_lattice.le α c)
  (top : α) (eq_top : top = @complete_lattice.top α c)
  (bot : α) (eq_bot : bot = @complete_lattice.bot α c)
  (sup : α → α → α) (eq_sup : sup = @complete_lattice.sup α c)
  (inf : α → α → α) (eq_inf : inf = @complete_lattice.inf α c)
  (Sup : set α → α) (eq_Sup : Sup = @complete_lattice.Sup α c)
  (Inf : set α → α) (eq_Inf : Inf = @complete_lattice.Inf α c) :
  complete_lattice α :=
begin
  refine { le := le, top := top, bot := bot, sup := sup, inf := inf, Sup := Sup, Inf := Inf, ..};
    subst_vars,
  exact @complete_lattice.le_refl α c,
  exact @complete_lattice.le_trans α c,
  exact @complete_lattice.le_antisymm α c,
  exact @complete_lattice.le_sup_left α c,
  exact @complete_lattice.le_sup_right α c,
  exact @complete_lattice.sup_le α c,
  exact @complete_lattice.inf_le_left α c,
  exact @complete_lattice.inf_le_right α c,
  exact @complete_lattice.le_inf α c,
  exact @complete_lattice.le_top α c,
  exact @complete_lattice.bot_le α c,
  exact @complete_lattice.le_Sup α c,
  exact @complete_lattice.Sup_le α c,
  exact @complete_lattice.Inf_le α c,
  exact @complete_lattice.le_Inf α c
end
end lattice
```
If you put `set_option old_structure_cmd true` instead, this proof times out

#### [Mario Carneiro (Nov 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/old_structure_cmd%20in%20structure%20literals/near/146821466):
this despite the fact that there are no structures being declared

#### [Johannes Hölzl (Nov 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/old_structure_cmd%20in%20structure%20literals/near/146826135):
uff, luckily I didn't run into this. Does the `{ f := _, .. _}` notation depend on `old_structure_cmd`?

#### [Sebastian Ullrich (Nov 06 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/old_structure_cmd%20in%20structure%20literals/near/146851518):
[It does](https://github.com/leanprover/lean/blob/687745d887ebd89da94ba36d853eff12746af136/src/frontends/lean/elaborator.cpp#L2854). Maybe it shouldn't.

#### [Sebastian Ullrich (Nov 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/old_structure_cmd%20in%20structure%20literals/near/146851533):
The structure instance notation is pretty complex and fragile in Lean 3. I'm really not sure what we should do with it in Lean 4.

