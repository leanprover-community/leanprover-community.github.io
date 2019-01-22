---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64252Splittingtopology.html
---

## [maths](index.html)
### [Splitting topology](64252Splittingtopology.html)

#### [Patrick Massot (Jan 22 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156605219):
@**Mario Carneiro** @**Johannes Hölzl** @**Reid Barton** I continued moving on the topology reorganization project. The next step was to split `topology.basic` and `topology.continuity` while gathering the basics of continuity and the basics of topological spaces. My current result is at https://github.com/leanprover-community/mathlib/tree/top_split I need comments before moving on. My next step would be to reorganize uniform spaces and topological structures, still following the general scheme discussed in Amsterdam

#### [Patrick Massot (Jan 22 2019 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156605761):
Recall that one goal was to have files with less than 1000 lines, and lighters dependencies for stuff needing only the basics of topological spaces and continuous functions. The current lines counts are
```
  1927 basic.lean
   460 bounded_continuous_function.lean
   118 compact_open.lean
  1568 continuity.lean
   271 stone_cech.lean
```
my proposal has:
```
   206 bases.lean
   591 basic.lean
   460 bounded_continuous_function.lean
   118 compact_open.lean
   957 constructions.lean
   359 maps.lean
   132 opens.lean
   573 order.lean
   280 separation.lean
   272 stone_cech.lean
   468 subset_properties.lean
```
you can still see I got tired with `constructions.lean` (which has products, sum, quotients, pi...). That one could probably be split more

#### [Patrick Massot (Jan 22 2019 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606107):
Damn, I  forgot to move homeomorphisms from constructions to map

#### [Patrick Massot (Jan 22 2019 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606162):
That will improve the balance for about 100 lines

#### [Johannes Hölzl (Jan 22 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606359):
Hm the homeomorphisms should be in `basic`. And I should mention that I don't like to goal of keeping the files less than 1000 lines. This is quiet arbitrary and doesn't tell anybody where to find a specific definition/proof

#### [Johannes Hölzl (Jan 22 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606384):
But looking through the changeset it looks very sensible

#### [Patrick Massot (Jan 22 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156607124):
We know you don't like reducing line counts. This was very clear from reading the topology part of mathlib, and also from the Amsterdam discussion. But I think this is still a nice goal, especially when we find out there are sensible cutting points. And of course the 1000 number is totally arbitrary, although there is a certain psychological impact above that threshold.

