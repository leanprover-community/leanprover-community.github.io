---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71627Ringcompletion.html
---

## [maths](index.html)
### [Ring completion](71627Ringcompletion.html)

#### [Patrick Massot (Dec 18 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110493):
@**Johannes Hölzl**  I think I just completed the topological ring completion project. Remember where we got stuck last time: we could define a ring structure on `completion a` assuming that `a` was a *separated* topological ring, see https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L1168. We could also construct a ring structure on `quotient (separatation_setoid a)`, see https://github.com/leanprover/mathlib/blob/master/analysis/topology/quotient_topological_structures.lean#L204. I did that by leveraging the algebraic quotient construction, using that the separation relation for uniform groups is the same as the left coset relation for the closure of zero. This meant fighting the system to use an equivalence relation equality to relate the quotients. Then I constructed https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L710-L711 `completion (quotient $ separatation_setoid a) ≃ completion α` which I hoped to use to glue the preceding two constructions and get a ring structure on `completion α`. But this meant fighting Lean again, for lack of transport of structure along this equiv.

#### [Johannes Hölzl (Dec 18 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110596):
Yes, I remember. How did you solve it. Or did you copy the structure and wrote down the transport for each rule?

#### [Patrick Massot (Dec 18 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110617):
So I backtracked completely. I defined a ring structure on `sep_quot α := quotient (separatation_setoid a)` directly, using the link between the separation relation and the closure of zero only in the lemma proving that multiplication descends to the quotient. And then I defined `hcompletion α := completion (sep_quot α)`. This looks really weird because remember `completion α := quotient (separation_setoid $ Cauchy α)`, so we use the separation relation twice. But it works very smoothly

#### [Patrick Massot (Dec 18 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110717):
Remember how Bourbaki does it: they replace `Cauchy α` with the space of *minimal* Cauchy filters on α. And they define the completion as `min_cauchy (quotient $ separatation_setoid a)`. That's how they avoid the double quotient

#### [Patrick Massot (Dec 18 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110728):
while still first getting rid of the separation issue

#### [Patrick Massot (Dec 18 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110785):
I didn't start that road because I saw you did everything with non-minimal Cauchy filters. And of course all three constructions solve the same universal problem, so there are uniquely isomorphic

#### [Johan Commelin (Dec 18 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110831):
Cool! Congrats on completing this! :tada:

#### [Patrick Massot (Dec 18 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152110892):
The messy thing with my construction is that `completion α` becomes a purely intermediate thing, still with a rather large theory, which needs to be restated for `hcompletion`

#### [Kevin Buzzard (Dec 18 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111034):
Is "Bourbaki did it this way" an argument for or against "Lean should do it this way", or are they just independent things?

#### [Patrick Massot (Dec 18 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111074):
It's part of my excuse for creating this mess

#### [Patrick Massot (Dec 18 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111173):
I mean this mess: `instance : has_coe α (hcompletion α) := ⟨quotient.mk ∘ Cauchy.pure_cauchy ∘ quotient.mk⟩`

#### [Kevin Buzzard (Dec 18 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111181):
If it works, it works :-)

#### [Kenny Lau (Dec 18 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111293):
you can't maintain a library by bodging...

#### [Patrick Massot (Dec 18 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111369):
It has a very clean interface since it solves a very clearly specified universal problem

#### [Kevin Buzzard (Dec 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111438):
Is one of the the issues that we need to transport theorems along isomorphisms and this is still not yet possible, so we fudge our way around it?

#### [Patrick Massot (Dec 18 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152111474):
The transport idea was already a work-around actually

#### [Patrick Massot (Dec 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113098):
The big thing is at https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8

#### [Patrick Massot (Dec 18 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113142):
That's 500 more lines to `completion.lean`

#### [Patrick Massot (Dec 18 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113277):
But some of them should move elsewhere, independently of the reorganization discussion

#### [Patrick Massot (Dec 18 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113409):
It includes using `def function.comp₂ (f : α → β → γ) (g : γ → δ) : α → β → δ := λ  x y, g (f x y)` and its companions `def continuous₂ (f : α → β → γ) := continuous (function.uncurry f)` etc to nicely handle functions of two variables (like addition and multiplication), as was mentioned in another thread

#### [Patrick Massot (Dec 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113626):
I'd like to get @**Johannes Hölzl** input before finishing restating stuff for `hcompletion`

#### [Johannes Hölzl (Dec 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113645):
I think ` continuous₂` and `uniform_continuous₂` should be fully transparent, without any rules about them. So only use them when writing down concrete instances

#### [Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113690):
I need them as assumption for many statements

#### [Johannes Hölzl (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113703):
Yes, there its okay

#### [Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113719):
and the most important piece is the composition lemma

#### [Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113731):
https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8#diff-f7d0385aaa9b17579cee0f2af9cc9135R120

#### [Patrick Massot (Dec 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152113791):
This is what make this so convenient

#### [Patrick Massot (Dec 18 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152124223):
```quote
Remember how Bourbaki does it: they replace `Cauchy α` with the space of *minimal* Cauchy filters on α. And they define the completion as `min_cauchy (quotient $ separatation_setoid a)`. That's how they avoid the double quotient
```
I just checked, and actually the above is not quite correct. It seems that minimal Cauchy filters are already separated.

#### [Patrick Massot (Dec 18 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring completion/near/152124381):
So this is a really more economical way of building the Hausdorff completion. But they don't solve problem of factorizing morphisms into complete spaces (not hausdorff complete spaces), whereas we do it.

