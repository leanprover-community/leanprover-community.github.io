---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27371meminbinder.html
---

## [general](index.html)
### [mem in binder](27371meminbinder.html)

#### [Patrick Massot (Jun 16 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145487):
I wrote the code `⨅ U ∈ nhd_zero R, principal {p : R×R | p.2 - p.1 ∈ U}` but now I realize I don't quite understand what's going on under the hood. The inf notation is defined by:
```lean
def infi [complete_lattice α] (s : ι → α) : α := Inf {a : α | ∃i : ι, a = s i}
notation `⨅` binders `, ` r:(scoped f, infi f) := r
```
What is `ι` in my case? `{U : set R // U ∈ nhd_zero R}`?

#### [Patrick Massot (Jun 16 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145505):
or is it some kind of Pi type?

#### [Reid Barton (Jun 16 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145510):
It magically becomes `⨅ U, ⨅ (H : U ∈ nhd_zero R), principal {p : R×R | p.2 - p.1 ∈ U}`

#### [Patrick Massot (Jun 16 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145564):
ok, this is consistent with stuff I saw

#### [Reid Barton (Jun 16 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145649):
You can even refer to `H` after the comma, though this seems like a bad idea to me

#### [Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145811):
Thank you

#### [Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145812):
I'm writing really strange looking code

#### [Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128145817):
I hope Johannes will help me clean it up

#### [Patrick Massot (Jun 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem in binder/near/128146158):
It's getting really late here. I'll give up for today. If someone else wants to play with filters while I sleep, I think the lemma I need next is:
```lean
lemma filter.mem_sets_of_mem_infi {α : Type*} {ι : Sort*} {f : ι → filter α} {A : set α} :
A ∈ (⨅ i,f i).sets → ∃ i, A ∈ (f i).sets
```

