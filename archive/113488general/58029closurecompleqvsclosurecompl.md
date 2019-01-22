---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58029closurecompleqvsclosurecompl.html
---

## [general](index.html)
### [closure_compl_eq vs closure_compl](58029closurecompleqvsclosurecompl.html)

#### [Kenny Lau (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058320):
[closure_compl_eq vs closure_compl](/user_uploads/3121/799w6_d5y5HxDNH8PGRRdgyJ/2018-10-02-6.png)

https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L261-L271

#### [Kenny Lau (Oct 02 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058346):
lemme `blame` this...

#### [Kenny Lau (Oct 02 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058452):
it's [this change](https://github.com/leanprover/mathlib/commit/afefdcbb46f85e471ca258373d33e92a9d2dd61c#diff-6e52fa1a2004f6ddfddb7023e1ec2709R243) that moved the latter theorem from `topology/topological_space.lean` to `analysis/topology/topological_space.lean`

#### [Patrick Massot (Oct 02 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058454):
oh wow, there are actually adjacent!

#### [Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058529):
actually, below and above these theorems:

#### [Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058578):
```lean
@[simp] lemma interior_compl_eq {s : set α} : interior (- s) = - closure s :=
by simp [closure_eq_compl_interior_compl]

@[simp] lemma closure_compl_eq {s : set α} : closure (- s) = - interior s :=
by simp [closure_eq_compl_interior_compl]

lemma closure_compl {s : set α} : closure (-s) = - interior s :=
subset.antisymm
  (by simp [closure_subset_iff_subset_of_is_closed, compl_subset_compl, subset.refl])
  begin
    rw [compl_subset_comm, subset_interior_iff_subset_of_open, compl_subset_comm],
    exact subset_closure,
    exact is_open_compl_iff.mpr is_closed_closure
  end

lemma interior_compl {s : set α} : interior (-s) = - closure s :=
calc interior (- s) = - - interior (- s) : by simp
  ... = - closure (- (- s)) : by rw [closure_compl]
  ... = - closure s : by simp
```

#### [Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135058582):
just like a sandwich

#### [Johannes Hölzl (Oct 02 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135061762):
gone https://github.com/leanprover/mathlib/commit/fff12f5889c7cd5a9169b42433eb14f3b53e7614

#### [Kenny Lau (Oct 02 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135061814):
I'm quite surprised they have no dependencies...

#### [Kevin Buzzard (Oct 03 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135085888):
I guess one could try and use meta magic to search for theorems with two distinct names?

#### [Patrick Massot (Oct 03 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq vs closure_compl/near/135086020):
In principle this is very easy

