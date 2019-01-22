---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/66707subsetswithinducedstructure.html
---

## [new members](index.html)
### [subsets with induced structure](66707subsetswithinducedstructure.html)

#### [Jean Lo (Nov 19 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/subsets with induced structure/near/147981000):
Given a set with some structure, I often would like to think about its subsets that also have a similar structure on it. This seems like a pretty common construction — what would be the idiomatic way to formulate such things in Lean?

Here's a particular example encountered in an attempt to formalise some algebra notes:

```lean
import algebra.group data.set.basic

-- what I had previously. This is unsatisfactory for a number of
-- reasons, including the fact that it doesn't force me to use the
-- operation on `G` when constructing `group H`, which means I'm
-- not proving what I really want to prove.

variable {G: Type*}

def H := { g: G // true }

theorem subgroup_self [group G]: group H := sorry
-- (also, this is incorrect, seemingly because H is of type `Type u_2`?
--  I don't understand what exactly is happening.)


-- I searched mathlib for examples, and the only similar thing I managed
-- to find was `submodule`. Mimicking its definition, I've written down:

structure subgroup (G: Type*) [group G] :=
  (carrier: set G)
  (one: (1:G) ∈ carrier)
  (closed: ∀ g h: G, g ∈ carrier → h ∈ carrier → g * h ∈ carrier)
  (inv: ∀ g: G, g ∈ carrier → g⁻¹ ∈ carrier)

-- now I think I can explicitly construct terms of type `subgroup` by
-- putting together proofs that a certain carrier set has the desired
-- properties — but how do I formulate things like `subgroup_self`,
-- and other assertions that are shaped like 'this given subset of G
-- is a subgroup of G' ?
``` 

In conversations elsewhere, I've heard mentions of `is_subgroup` and `is_submodule`, though I've also been told that `is_submodule` has been replaced, and indeed I could find neither definition in my copy of mathlib.

#### [Bryan Gin-ge Chen (Nov 19 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/subsets with induced structure/near/147981206):
I'm not sure how old your version of mathlib is but `is_subgroup` has been in `group_theory.subgroup` for long time https://github.com/leanprover/mathlib/blob/8ae3fb86f09daab0a48a4b81e19c1eee7552be10/group_theory/subgroup.lean

#### [Jean Lo (Nov 19 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/subsets with induced structure/near/147981678):
oh, in `group_theory/`, of course! I've been having trouble with `helm-lean-definitions` and have been looking in `algebra/group.lean` this whole time. Sorry for that.

So what are the differences between how `is_subgroup` and `submodule`are defined? when should one way of doing it be preferred over the other?

#### [Bryan Gin-ge Chen (Nov 19 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/subsets with induced structure/near/147981908):
Good question! I'm not sure how the new `submodule` stuff works myself.

