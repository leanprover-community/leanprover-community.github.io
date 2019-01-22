---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29680refinementofpartitions.html
---

## [general](index.html)
### [refinement of partitions](29680refinementofpartitions.html)

#### [Kenny Lau (Apr 18 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224068):
what are the existing lemmas related to refinement of partitions, i.e. the idea that if there are two partitions of a list, then there is a partition that refines both?

#### [Mario Carneiro (Apr 18 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224340):
What do you mean by partition?

#### [Kenny Lau (Apr 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224380):
preimage of `list.join`

#### [Mario Carneiro (Apr 18 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224546):
It seems a bit trivial, since there is a maximal partition

#### [Kenny Lau (Apr 18 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224593):
well there's a minimal refinement

#### [Mario Carneiro (Apr 18 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224606):
I don't think the subpartition relation exists in mathlib, but you could prove it's a lattice

