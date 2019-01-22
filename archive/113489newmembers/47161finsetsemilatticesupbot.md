---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47161finsetsemilatticesupbot.html
---

## [new members](index.html)
### [finset semilattice_sup_bot](47161finsetsemilatticesupbot.html)

#### [Alistair Tucker (Nov 20 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset semilattice_sup_bot/near/148054444):
Hi! In finset.lean there is
```lean
instance : semilattice_inf_bot (finset α) :=
{ bot := ∅, bot_le := empty_subset, ..finset.lattice.lattice }
```
but no equivalent instance for semilattice_sup_bot. Is there some good reason for this?

#### [Johannes Hölzl (Nov 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset semilattice_sup_bot/near/148054870):
I don't see any reason why this is missing.

#### [Alistair Tucker (Nov 20 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset semilattice_sup_bot/near/148055198):
Thanks

