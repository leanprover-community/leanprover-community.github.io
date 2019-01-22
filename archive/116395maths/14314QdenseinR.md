---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14314QdenseinR.html
---

## [maths](index.html)
### [Q dense in R](14314QdenseinR.html)

#### [Kevin Buzzard (Dec 28 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152627608):
`theorem rationals_dense (x y : ℝ) (H : x < y) : ∃ q : ℚ, x < q ∧ (q : ℝ) < y :=` Where is this now? I think it was explicitly there before the reals were refactored. Now there is `dense_embedding_of_rat` but then I have to work to get the statement I want.

#### [Reid Barton (Dec 28 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152627809):
`algebra.archimedean` has some similar things

#### [Mario Carneiro (Dec 28 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152634813):
the rationals are archimedean, so `exists_rat_btwn` will work. Also the rationals are dense, so `dense` will work

#### [Mario Carneiro (Dec 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152634858):
oh wait that last one is just rationals between rationals, with no casting

#### [Kevin Buzzard (Dec 28 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152655840):
Aah, thanks to both of you. I'm looking in the wrong places. That was silly of me -- I even lectured this term on the fact that unboundedness of Z in R implied this fact.

#### [Kevin Buzzard (Dec 28 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152666498):
I want the coercion from Q to R to be different somehow. Look at this question the first years will be asked next term: "Let $$S$$ be a non-empty bounded above set of reals. True or false: if $$S\subseteq\mathbb{Q}$$ then $$sup(S)\in\mathbb{Q}$$. How do I make the Lean formalisation of this question less ugly? [added later: this is just one part of a multi-part question about a non-empty bounded-above set of reals $$S$$ so we don't really want to change the definition of $$S$$ itself]

#### [Kevin Buzzard (Dec 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152666549):
```lean
import data.real.basic

-- structure or class?
structure real.rat1 (r : ℝ) :=
(q : ℚ)
(pf : r = ↑q)

definition real.rat2 (r : ℝ) := ∃ q : ℚ, r = q
```
Are these functions in Lean already? What are they / should they be called?

#### [Mario Carneiro (Dec 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152672823):
As usual, this is nonidiomatic lean and so it's less than nice to say. It is equivalent to talk about the supremum of a family `f : I -> Q`

#### [Mario Carneiro (Dec 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152672849):
alternatively, you can let `S : set Q` and have its interpretation in `R` be `(coe '' S)`

#### [Mario Carneiro (Dec 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152672917):
alternatively `S : set R` and `S \sub range coe`

#### [Kevin Buzzard (Dec 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152672923):
Oh that's better

#### [Mario Carneiro (Dec 28 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152672949):
if I wasn't constrained by aiming for a direct translation I would certainly go for the first option

#### [Mario Carneiro (Dec 28 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152673077):
I think we could define `real.rats, real.nats : set R` in the obvious way and use that

#### [Kevin Buzzard (Dec 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152675391):
and now I have to reprove things like `real.rats x -> real.rats y -> real.rats (x + y)`?

#### [Kevin Buzzard (Dec 28 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152675592):
I am not 100% clear on what needs proving actually. There's a lemma which says that + on Q and R coincide, and that's kind of why I need to prove the thing above. But there's another lemma which says that < on Q and R coincide, and that doesn't seem to correspond to something I need to prove here.

#### [Mario Carneiro (Dec 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152696668):
well, it's a set so you would want to write that `x \in rats -> y \in rats -> x + y \in rats`, but yes, and it follows from `rat.cast_add`

#### [Mario Carneiro (Dec 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152696679):
and you are right, there isn't really an analogue for `rat.cast_le`

#### [Mario Carneiro (Dec 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152696719):
it's just the set of rational numbers, as a subset of R

#### [Mario Carneiro (Dec 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152696720):
all the operations are real operations

#### [Mario Carneiro (Dec 29 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152696726):
you can do many things with such a set, the idea is when you need a set and not a type. For example `closure rats = univ` is hard to state otherwise

#### [Chris Hughes (Dec 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q dense in R/near/152699297):
(deleted)

