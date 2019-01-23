---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88290topmulgroups.html
---

## Stream: [maths](index.html)
### Topic: [top mul groups](88290topmulgroups.html)

---


{% raw %}
#### [ Patrick Massot (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135306917):
Am I blind or is the definition of multiplicative topological groups is missing in mathlib?

#### [ Patrick Massot (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135306924):
And nothing about topological groups uses the `to_additive` machine?

#### [ Kevin Buzzard (Oct 06 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307033):
Maybe edit core Lean and redefine the notation for `+` to be `mul`?

#### [ Kevin Buzzard (Oct 06 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307076):
You might well be right though. With groups I went through a phase of confusing `group` and `add_group` but I've never had the same confusion for topological groups.

#### [ Patrick Massot (Oct 06 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307084):
I think I'll stick to additive group, and try to make progress on rings. Then someone will have to do a huge refactor of all this mess

#### [ Patrick Massot (Oct 06 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135312988):
Also, as I suspected, Lean doesn't want to hear that a ring quotiented by an ideal has anything to do with a add_comm_group quotiented by a subgroup. After proving addition is continuous when you quotient a commutative topological group by a subgroup, you cannot get continuity of addition when you quotient a ring by an ideal. This is a bit sad

#### [ Patrick Massot (Oct 06 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135312998):
Even after I wrote:
```lean
variables {α : Type*} [comm_ring α] {M : Type*} [module α M] (N : set α) [is_submodule N]

instance submodule_is_add_subgroup : is_add_subgroup N :=
{ zero_mem :=  is_submodule.zero,
  add_mem :=  λ a b, is_submodule.add,
  neg_mem := λ a,  is_submodule.neg}
```

#### [ Johan Commelin (Oct 06 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313204):
Is that because quotients of modules is not done via quotients of add_groups?

#### [ Patrick Massot (Oct 06 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313213):
yes

#### [ Patrick Massot (Oct 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313269):
https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L22
https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L145
No link

#### [ Johan Commelin (Oct 06 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313316):
I've heard rumors that there are plans to fix this in mathlib 5.2

#### [ Patrick Massot (Oct 06 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313425):
:oh_no: I try to copy-paste proofs but https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L49 and https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L193 are not compatible :sad: :sad: :sad:

#### [ Patrick Massot (Oct 06 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135314044):
@**Johannes Hölzl** I just pushed https://github.com/leanprover-community/mathlib/commit/981ed82f657f49b4f276457de398b9c33af05d54 It's a mess with a lot of duplication and brute force but it should allow me to continue working on completions of topological rings. Of course I'd be grateful if you can refactor it, but I expect it would be quite a bit of work because `topological_structures.lean` does not use at all the `to_additive` machine, and module quotients are unrelated to additive group quotients.

#### [ Patrick Massot (Oct 06 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135314056):
To be clear: currently I need only the ring part of that commit (and the open map things of course) but I let the group and add_comm_group part in order to highlight the refactoring issue

#### [ Patrick Massot (Oct 06 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135318258):
And again it fails because we have multiple instances on the same type, see https://github.com/leanprover-community/mathlib/commit/125efed6aac2f44d8d466b001c655dd04ebd5fb0 I give up for today since I won't be there after dinner. @**Johannes Hölzl** you can have a look if you want. The issue is go back and forth between the separation quotient of a topological ring seen from the purely uniform space point of view and from the quotient ring point of view. It seems Lean doesn't accept they correspond to the same topology, although both are defeq to a quotient topology and I have a lemma stating the two setoid are equals.

#### [ Johannes Hölzl (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135619845):
I added a commit in `lc\completions` s.t. `topological_structures` uses `to_additive` (at least for `topological_add_monoid` and `topological_add_group`)

#### [ Patrick Massot (Oct 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135625411):
Thanks!

#### [ Patrick Massot (Oct 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135625428):
And thanks for working on this branch again


{% endraw %}
