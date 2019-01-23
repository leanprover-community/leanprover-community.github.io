---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30056CubicalHoTTLibrary.html
---

## Stream: [general](index.html)
### Topic: [Cubical HoTT Library](30056CubicalHoTTLibrary.html)

---

#### [Namdak Tonpa (Jan 07 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154560608):
Greetings to everybody! TWIMC, Ground Zero, cubical base library embedded into Lean 3.4.1: https://github.com/groupoid/lean

Ports to other cubical type checkers: https://cubical.systems

#### [Gabriel Ebner (Jan 07 2019 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154601477):
It's exciting to see other variants of HoTT with new implementations in Lean.  You're probably aware of this, but the reason we're using the `@[hott]` attribute in https://github.com/gebner/hott3 is because otherwise this kind of HoTT in Lean is inconsistent.  Concretely, the `@[hott]` attribute checks that we're not using large elimination for the built-in equality type, which allows us to prove that all paths between two points are equal:
```lean
import ground_zero.theorems.ua
universes u
hott theory
open ground_zero.structures ground_zero.ua

def all_hset (α : Sort u) : hset α :=
by intros a b p q; cases p; cases q; refl

noncomputable def inconsistent : empty :=
by apply universe_not_a_set; apply all_hset
```

#### [Uranus Testing (Jan 08 2019 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154621668):
Yes you are right. There is another place where we can get an inconsistency—ground_zero.support.inclusion. With it we can get a proof that generalized circle (or one step truncation, https://homotopytypetheory.org/2015/07/28/constructing-the-propositional-truncation-using-nonrecursive-hits/) is a prop. But without it we can’t get a right recursors for HITs that were constructed directly from quotients because quot.sound uses built-in equality type.

#### [Uranus Testing (Jan 08 2019 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154622491):
Quotients require equality type in Prop: https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/kernel/quotient/quotient.cpp#L61, so we cannot do init_quotient with our (ground_zero.types.eq) equality type.

