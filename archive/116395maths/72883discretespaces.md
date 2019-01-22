---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72883discretespaces.html
---

## [maths](index.html)
### [discrete spaces](72883discretespaces.html)

#### [Reid Barton (Oct 19 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete spaces/near/136077573):
```quote
**[feat(analysis/topology): add type class for discrete topological spaces](https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a)**
feat(analysis/topology): add type class for discrete topological spaces
https://github.com/leanprover/mathlib/commit/f6812d5a881b1bca826808e6bd40eb3e75979d2a
```
@**Johannes Hölzl** nice! This is something I was also considering adding, compare https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/for_mathlib/analysis_topology_topological_space.lean. I was thinking of making it an alternative branch in the `topological_space <- uniform_space <- metric_space` chain; in the link I put it on top of `topological_space` but it could easily go on top of `uniform_space` instead.
Thoughts?

#### [Reid Barton (Oct 19 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete spaces/near/136077725):
The advantage is that you wouldn't need all those separate instances for spaces like `nat`--the disadvantage is you have to be a bit careful to define the instances for things like products and sums correctly, I guess.

#### [Johannes Hölzl (Oct 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete spaces/near/136094635):
I wonder if there exists a case where we have a discrete topology, but one still additional topological structures on it. For example `orderable_topology` doesn't hold for all discrete spaces. Of course `orderable_topology` is a mixin in itself so it would fit. But I prefer the flexibility we get from mixins. And I guess `discrete_topology` isn't used too often so writing two parameters instead of one shouldn't be too hard.
Hence, I would like to keep it as an mixin (i.e. a predicate, not containing the toplogical structure).

#### [Reid Barton (Oct 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/discrete spaces/near/136112844):
Ah, I see. I can imagine a situation where you have a manifold or a topological ring or something, and then also want to assume or prove that the topology is discrete. Makes sense.

