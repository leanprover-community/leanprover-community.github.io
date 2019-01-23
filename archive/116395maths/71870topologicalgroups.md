---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71870topologicalgroups.html
---

## Stream: [maths](index.html)
### Topic: [topological groups](71870topologicalgroups.html)

---

#### [Patrick Massot (Sep 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20groups/near/133277465):
I pushed to https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean the current state of my work on completions of uniform groups. I would really appreciate help (from Mario, @**Johannes Hölzl** or anyone else) with understanding how one should setup the instance maze (or use definitions instead of instances) to be able to finish https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161 (assume I can prove https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124). I'd be ready to have the uniform space structure on a topological group to be outside the type class system, especially since we would ideally also like to handle non-commutative groups at some point, and those have two natural uniform structures. But I don't know how to use them if there are not instances (everything else uses instance implicit arguments).

