---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14331simpequalityandinstances.html
---

## [new members](index.html)
### [simp, equality, and instances](14331simpequalityandinstances.html)

#### [Simon Winwood (Sep 25 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561065):
Hi, I am trying to prove that list intersection with a singleton list is essentially a filter, and get this sub-goal:
```
lemma filter_mem_singleton_is_filter_eq {a} [decidable_eq a] {x : a} {xs : list a}:
  filter (λy, y ∈ [x]) xs = filter (λy, y = x) xs := 
```
this is more or less trivial, but for the implicite `decidable` term in the filter.  When I rewrite the mem term to be eq, the terms look like:
```
a : Type u_1,
_inst_1 : decidable_eq a,
x : a,
xs : list a
⊢ @filter a (λ (y : a), y = x)
      (@eq.rec (a → Prop) (λ (y : a), y ∈ [x]) (@decidable_pred a)
         (λ (a_1 : a), @list.decidable_mem a _inst_1 a_1 [x])
         (λ (y : a), y = x)
         _)
      xs =
    @filter a (λ (y : a), y = x) (λ (a : a), _inst_1 a x) xs
```
where the terms are equal but for the instance terms (after `simp, dsimp`).  I have run into this before, but managed to find a workaround.  My questions is: is this common, and what is the solution, or am I doing something that is very un-lean?

#### [Mario Carneiro (Sep 25 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561362):
When you get to that goal, use `congr` to simplify it

#### [Mario Carneiro (Sep 25 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561367):
before the rw

#### [Simon Winwood (Sep 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561425):
oh, nice, that works.

#### [Mario Carneiro (Sep 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561432):
`congr` knows about subsingleton arguments and will automatically prove they are equal. In this case `decidable p` is a subsingleton

#### [Simon Winwood (Sep 25 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561678):
and a follow-on - is there somewhere I should be sending the lemmas I prove?  They look like they should be in the standard library, but I don't know the protocol for submitting them.  These are lemmas like the interaction between list.inter and const etc..

#### [Mario Carneiro (Sep 25 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134561916):
This should probably be going into [mathlib](https://github.com/leanprover/mathlib). The core library is frozen and does not accept PRs

#### [Mario Carneiro (Sep 25 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134562029):
Although I'm not sure I want this particular theorem, it seems a bit specialized... Both sides are equivalent to `list.repeat x (xs.count x)`

#### [Simon Winwood (Sep 25 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simp, equality, and instances/near/134562143):
This is a helper lemma, so maybe not.  It looks like mathlib has a bunch of lemmas which may do what I want, anyway.  Thanks!

