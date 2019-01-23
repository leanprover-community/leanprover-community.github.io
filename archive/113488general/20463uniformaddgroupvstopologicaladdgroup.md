---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20463uniformaddgroupvstopologicaladdgroup.html
---

## Stream: [general](index.html)
### Topic: [uniform_add_group vs topological_add_group](20463uniformaddgroupvstopologicaladdgroup.html)

---

#### [Kenny Lau (Nov 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891308):
We know that a topological additive abelian group is a uniform additive group, and that a uniform additive group is a topological additive group

#### [Kenny Lau (Nov 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891315):
but which one of them should be an instance? @**Kevin Buzzard** @**Mario Carneiro**

#### [Mario Carneiro (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891448):
if they are equivalent, then they should be the same

#### [Mario Carneiro (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891459):
(I have a preference for the topological terminology)

#### [Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891467):
a topological additive group is based on a topological space and an additive group; a uniform additive group is based on a uniform space and an additive group

#### [Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891473):
they can't be the same, right

#### [Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891478):
A topological add group has a uniform structure

#### [Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891487):
so it's both

#### [Kenny Lau (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891488):
but that would cause a loop in the inferrence

#### [Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891490):
how?

#### [Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891493):
I'm saying delete uniform add group and replace it with top add group

#### [Kenny Lau (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891536):
aha

#### [Kenny Lau (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891546):
now?

#### [Mario Carneiro (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891551):
Actually I guess this is already how uniform_add_group is defined

#### [Mario Carneiro (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891553):
so it's just a rename

#### [Kenny Lau (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891571):
well, currently we have:
```lean
class uniform_add_group (α : Type u) [uniform_space α] [add_group α] : Prop :=
(uniform_continuous_sub : uniform_continuous (λp:α×α, p.1 - p.2))

```

#### [Mario Carneiro (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891572):
maybe you don't need uniform continuity

#### [Mario Carneiro (Nov 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891616):
oh, it's a predicate

#### [Mario Carneiro (Nov 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891633):
@**Johannes Hölzl** will object, but I want it to be a class

#### [Kenny Lau (Nov 01 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891713):
indeed it is Hoelzl who introduced uniform add groups, at least according to [this](https://github.com/leanprover/mathlib/commit/ba95269a65a77c8ab5eae075f842fdad0c0a7aaf#diff-da2fc75300f00796d9262c2c7c3bd09aR87)

#### [Mario Carneiro (Nov 01 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891731):
oh, wait we do need uniform continuity

#### [Mario Carneiro (Nov 01 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891750):
Is the uniformity of a uniform add group uniquely defined?

#### [Mario Carneiro (Nov 01 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891808):
Topological groups actually have two induced uniformities, the left and right uniformity

#### [Mario Carneiro (Nov 01 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891834):
so topological add group and uniform add group aren't exactly the same

#### [Mario Carneiro (Nov 01 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891887):
a uniform add group comes with a chosen uniformity, a top add group doesn't

#### [Kenny Lau (Nov 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136892371):
so what should I do?

#### [Kenny Lau (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908449):
@**Kevin Buzzard** what do you think about this?

#### [Kevin Buzzard (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908529):
This is an implementation issue and I have no idea.

#### [Kevin Buzzard (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908576):
I will comment though that with something like the Haar measure on a locally compact Hausdorff topological group, there are two: a left Haar measure and a right Haar measure, but mathematicians often just talk about "the Haar measure" and they have just randomly chosen one of them.

#### [Johan Commelin (Nov 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136909588):
But these are additive groups, which should always be abelian, and then the uniformities coincide.

#### [Kevin Buzzard (Nov 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136909840):
No -- Haar measure doesn't need abelian. It's Pontrjagin duality which needs abelian

#### [Johan Commelin (Nov 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136911163):
Sure, I know that. Infinite Galois groups have Haar measures...
So I think my point is: in the non-commutative case we don't want an instance from `topological_group` to `uniform_group` because in that case we want the user to explicitly say "Use the left uniformity" (or "use the left Haar measure", etc...). But in the commutative case, the left and right uniformity agree (just as with Haar measures), so it would make sense if the system could automatically pick one. But then we get diamond issues, and maybe it is just not worth it.

#### [Kevin Buzzard (Nov 01 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136926698):
Oh I see! Sorry :-) What I'm suggesting is that we always use the left one.

#### [Patrick Massot (Nov 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136940731):
I was also confused by uniform_add_group in the beginning, and wanted to get rid of it and keep topological add groups. But then I had this completion diamond issue, and Johannes fixed it by using more uniform_add_group...

#### [Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942309):
@**Patrick Massot** @**Kevin Buzzard** the problem is that I'm cleaning up the perfectoid project in which you have an instance of topological add comm group -> uniform add group

#### [Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942317):
which messes up everything

#### [Johan Commelin (Nov 01 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942896):
How much breaks if you remove that instance?

#### [Patrick Massot (Nov 01 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136944935):
Everything about topological rings in the perfectoid project has been merged into mathlib, you can get rid of everything

#### [Kenny Lau (Nov 01 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945077):
I don't think it's everything

#### [Kenny Lau (Nov 01 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945126):
here's what is left of `for_mathlib/uniform_space.lean`:
```lean
import analysis.topology.completion
import analysis.topology.uniform_space

namespace uniform_space
variables {α : Type*} [uniform_space α] {β : Type*} [uniform_space β] {γ : Type*} [uniform_space γ]
open Cauchy set

def pure_cauchy₂ : α × β → Cauchy α × Cauchy β := λ x, (pure_cauchy x.1, pure_cauchy x.2)

lemma pure_cauchy_dense₂ : ∀x : Cauchy α × Cauchy β, x ∈ closure (range (@pure_cauchy₂ α _ β _)) :=
begin
  intro x,
  dsimp[pure_cauchy₂],
  rw [←prod_range_range_eq, closure_prod_eq],
  simp[prod.ext_iff, pure_cauchy_dense],
end

namespace pure_cauchy

lemma prod.de : dense_embedding (λ p : α × β, (pure_cauchy p.1, pure_cauchy p.2)) :=
dense_embedding.prod dense_embedding_pure_cauchy dense_embedding_pure_cauchy
end pure_cauchy

end uniform_space
```

#### [Johan Commelin (Nov 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945274):
Are those lemmas used elsewhere in the perfectoid project?

#### [Kenny Lau (Nov 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945292):
I don't know

#### [Patrick Massot (Nov 01 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136948798):
You can remove this.

