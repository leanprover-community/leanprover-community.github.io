---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/69142axiomofuniquechoice.html
---

## Stream: [maths](index.html)
### Topic: [axiom of unique choice](69142axiomofuniquechoice.html)

---

#### [Kenny Lau (Apr 17 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125181778):
Is the axiom of unique choice strictly weaker than the axiom of choice? From what I know, ZF has axiom of unique choice

#### [Mario Carneiro (Apr 17 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125181992):
Yes, as you observe

#### [Kevin Buzzard (Apr 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125186342):
There are models of ZF in which choice fails, and I am not entirely sure what the axiom of unique choice is, but the definition of a function in set theory is a collection of ordered pairs (a,b) such that for every a there's at most one b, and I would imagine that for some reasonable interpretation of the axiom of unique choice, you can use the axiom of replacement to build such a set.

#### [Kenny Lau (Apr 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125186348):
unique choice := nonempty X -> subsingleton X -> X

#### [Mario Carneiro (Apr 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125186393):
The axiom of unique choice is true in the standard set theoretic model of type theory without the axiom of choice

#### [Mario Carneiro (Apr 17 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125186406):
although I recall a result that a Tarski universe is well-orderable, so the universes axiom might also imply full choice

#### [Mario Carneiro (Apr 17 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/axiom%20of%20unique%20choice/near/125186508):
relevant: https://cs.nyu.edu/pipermail/fom/2008-March/012783.html

