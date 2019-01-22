---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20962whydoesoronlyeliminatetoProp.html
---

## [general](index.html)
### [why does or only eliminate to Prop?](20962whydoesoronlyeliminatetoProp.html)

#### [Kevin Buzzard (Mar 22 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063589):
I just noticed this. Chris Hughes wrote a proof for me, but in my application of his proof I have a function from `fin n` to `nat`, and he has implemented his proof using a function from `nat` to `nat` which he only ever evaluates at numbers less than `n`. Given my function from `fin n` to `nat` I hence need to come up with a function from `nat` to `nat` which extends it and I thought I'd just define it using `or.elim (decidable.em (i<n))` but this won't work because the target can't be `nat`.

#### [Chris Hughes (Mar 22 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063639):
You can using choice, but ite is probably more natural

#### [Chris Hughes (Mar 22 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063654):
`p or ¬p` is not as strong as `decidable p`

#### [Kevin Buzzard (Mar 22 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063729):
I had trouble eliminating `dite` a couple of weeks ago because I couldn't remember `dif_pos`. Why isn't it called `dite.elim_true` or something?

#### [Mario Carneiro (Mar 22 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064130):
If you want to eliminate on a decidable proposition, `dite` is the standard way. You can't eliminate from an `or` to a type because the or doesn't contain information about which disjunct is true (it's been forgotten in proof irrelevance), and you can't recover the data once you drop it.

#### [Mario Carneiro (Mar 22 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064215):
Also, `simp` will simplify with `dif_pos` and its friends, I usually prefer that to using the names explicitly

#### [Kevin Buzzard (Mar 22 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064628):
I was preparing myself for the fact that `dite` will be removed from Lean 4 ;-)

#### [Chris Hughes (Mar 24 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124151668):
The other reason, which only just occurred to me, is that if both sides of your `or` are true, then your function is defined to be two different things.

#### [Chris Hughes (Mar 24 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152040):
I'm just trying to work out in general which inductive predicates can eliminate into Sort, and which only eliminate into Prop. It's not that obvious why something like acc doesn't have this problem, and can eliminate into Sort.

#### [Mario Carneiro (Mar 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152052):
the basic idea is that there should only be one way to construct an element of an inductive prop if you want large elimination

#### [Mario Carneiro (Mar 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152093):
that's why it is called subsingleton elimination

#### [Mario Carneiro (Mar 24 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152142):
There are two proofs of `p \/ q`, which are equal by proof irrelevance, so inversion would be inconsistent

#### [Mario Carneiro (Mar 24 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152150):
similarly there are multiple ways to prove `\ex x. p x` by giving different witnesses, so you can't extract the witness

#### [Mario Carneiro (Mar 24 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152201):
The general rule is described in my paper, in the section "large elimination"

#### [Simon Hudon (Mar 24 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152304):
Do you know the reason behind the choice of making universes non-cumulative?

#### [Mario Carneiro (Mar 24 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152533):
It simplifies a lot of things

#### [Mario Carneiro (Mar 24 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152574):
cumulativity would break unique typing, for one

#### [Mario Carneiro (Mar 24 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152580):
you have to have a subtyping relation, which interacts with everything in the type theory in nontrivial ways

#### [Simon Hudon (Mar 24 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152622):
Oh? I didn't think you'd need a subtype relation just because of the universes

#### [Mario Carneiro (Mar 24 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152623):
I was thinking about extending my analysis to Coq, but it would not be a small modification

#### [Mario Carneiro (Mar 24 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152668):
you have to also have stuff like `A -> Sort 1 <= A -> Sort 2`

#### [Simon Hudon (Mar 24 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152723):
... and now that I think of it, might get tricky for generic monadic code, if you want to allow`m α` `m β` even when `α`, `β` are in different universes. You might need covariance / contravariance hints in the type of `m`

