---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32676heqhellagain.html
---

## [general](index.html)
### [heq hell again](32676heqhellagain.html)

#### [Patrick Massot (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135479776):
My current goal looks like `eq.mpr comm_ring._proof_2 (quotient_ring.comm_ring (closure (is_ideal.trivial α))) == quotient_ring.comm_ring (closure (is_ideal.trivial α))` I'm ready to believe this is a rightful punishment for an earlier sin, but I'd like to know whether there is any hope to escape, or I should go back and think about what I'm doing

#### [Chris Hughes (Oct 09 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480240):
Does this lemma help?
```lean
universe u
lemma for_patrick {α β : Sort u} (h : β = α) (x : α) : eq.mpr h x == x :=
by subst h; refl
```

#### [Patrick Massot (Oct 09 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480267):
YES!

#### [Patrick Massot (Oct 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480471):
Can you explain what's going on here?

#### [Patrick Massot (Oct 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480493):
@**Mario Carneiro** should this be added as a simp lemma in mathlib?

#### [Patrick Massot (Oct 09 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480728):
Let's see how bad things are. What I wanted to write was:
```lean
instance [comm_ring α] [uniform_space α] [uniform_add_group α] [topological_ring α] :
  topological_ring (quotient (separation_setoid α)) :=
by  rw ring_sep_rel ; apply_instance
```
What I actually wrote (after adding Chris's simp lemma):
```lean
instance [comm_ring α] [uniform_space α] [uniform_add_group α] [topological_ring α] :
  topological_ring (quotient (separation_setoid α)) :=
begin
  convert topological_ring_quotient (closure (is_ideal.trivial α)),
  { apply ring_sep_rel },
  { dsimp [topological_ring_quotient_topology, quotient.topological_space, to_topological_space],
    congr,
    apply ring_sep_rel,
    apply ring_sep_rel },
  { apply ring_sep_rel },
  { simp [uniform_space.comm_ring] },
end
```
Like: *come one Lean: apply ring_sep_rel!*

#### [Patrick Massot (Oct 09 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480782):
where `lemma ring_sep_rel (α) [comm_ring α] [uniform_space α] [uniform_add_group α] [topological_ring α] :
  separation_setoid α = quotient_ring.quotient_rel (closure $ is_ideal.trivial α)`

#### [Chris Hughes (Oct 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135480982):
`subst` is a better version of `rw`, that can `rw` the types of proofs as well. before `subst h` the goal is `@eq.mpr β α h x == x`, after `subst h`the goal is `@eq.mpr β β (@eq.refl (Sort u) β) x == x`, and now the types are the same on each sude of the equality, and `eq.mpr` can iota-reduce, since `eq.refl` is a constructor, so it's just `refl`. 

The trouble with `subst` is it only works with local constants, so these proofs often require you to turn your goal into a lemma where you can use `subst` on local constants. A good version of `subst` that handles things other than local constants is something that needs to be written I think.

#### [Chris Hughes (Oct 09 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135481256):
`eq_rec_heq` is exactly the same as the lemma I wrote by the way.

#### [Patrick Massot (Oct 09 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135481343):
not quite

#### [Patrick Massot (Oct 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135482297):
Chris, do you know if there is some more documentation about this magic `subst`? It sounds like it could be very useful. Lately I've been fighting that kind of `rw` issues a lot

#### [Chris Hughes (Oct 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135487819):
I don't think there's any documentation. The strategy to use it is to make sure that the expression you're substituting is a local constant, and if it isn't, then make an intermediate lemma. In the example I gave, only `α` had to be a local constant.

#### [Reid Barton (Oct 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135488280):
I always assumed `subst` was just induction on `eq`, is it actually something different?

#### [Simon Hudon (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135488614):
@**Reid Barton** That's a useful way to see it. The thing is that by doing induction on eq, you're substitution everywhere at once so when your variable is used as a parameter for a function with a dependent type, it can help do the substitution in every term and type at once so that the goal remains type correct

#### [Chris Hughes (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135488646):
Looking at the definition it appears to not be based on the induction tactic. `cases` also works in this example, but basically `subst` is for when the motive is hard to compute due to dependent arguments. The proof terms use `eq.drec` instead of `eq.rec`

#### [Patrick Massot (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135488654):
It sounds exactly like what I've needed for one week

#### [Patrick Massot (Oct 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135488934):
What is a local constant?

#### [Simon Hudon (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489147):
It's a free variable in your goal, not a definition and not a bound variable.

#### [Chris Hughes (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489169):
I think it's basically a variable in your local context, so `α` is, but not `ℕ` or `f α`

#### [Reid Barton (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489182):
"something you could substitute something else for"

#### [Patrick Massot (Oct 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489247):
It's hard to see how such a restrictive condition can be satisfied

#### [Mario Carneiro (Oct 09 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489445):
Only one side has to be a variable. e.g. `x = 1 |- P x` reduces to `P 1`

#### [Chris Hughes (Oct 09 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489455):
You turn your goal into a lemma about local constants, and then substitute your expression into that lemma, like I did with `for_patrick` A bit messy, but reliable.

#### [Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489480):
Also, `rcases e with rfl` will do subst on terms

#### [Patrick Massot (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489504):
What?!

#### [Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489507):
and `rcases e with <>` will do cases instead, which has slightly different effects wrt unfolding

#### [Patrick Massot (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489516):
All this becomes more and more obscure to me

#### [Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489532):
it's super useful to use `rfl` in rcases patterns

#### [Mario Carneiro (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489628):
If your assumption is `f x = g y` then it's difficult to eliminate the equality once and for all, it could make lots of things equal to other things in an unpredictable way (see: word problem)

#### [Mario Carneiro (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489659):
but when one side is a fresh variable, like `x = g y`, then we can just replace `x` with `g y` everywhere in the context to eliminate `x`

#### [Mario Carneiro (Oct 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489743):
The nice thing is that this works *regardless of any dependencies*, which is a big plus compared to `rw` with this equality everywhere

#### [Mario Carneiro (Oct 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489786):
Basically all facts about `eq` and `heq` are proved using this trick

#### [Patrick Massot (Oct 09 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135489943):
I think I need to see examples to understand this

#### [Patrick Massot (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135491213):
I have no idea where to start

#### [Kevin Buzzard (Oct 09 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135491595):
Patrick I have heard Chris moaning about this `heq` stuff. But I have never once had to use it? Why is that? Am I avoiding a certain kind of mathematics? Why do you need it?

#### [Reid Barton (Oct 09 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135491658):
When you didn't use the identity map as a map from `F (id '' U)` to `F U`, this is the kind of thing you avoided.

#### [Kevin Buzzard (Oct 09 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135492132):
Yes I just went back to that thread.

#### [Andrew Ashworth (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135492200):
I found a pretty good summary of all the different types of equality here: https://jozefg.bitbucket.io/posts/2014-08-06-equality.html

#### [Patrick Massot (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq hell again/near/135492206):
I have no idea what heq is. I can only tell you that when arguments of a term depend on other arguments then `rw` and `simp` often don't work. `convert` works but spawns `heq` goals. I understand nothing about Mario's explanations unfortunately

