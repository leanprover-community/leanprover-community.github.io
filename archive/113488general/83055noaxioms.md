---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83055noaxioms.html
---

## Stream: [general](index.html)
### Topic: [no axioms](83055noaxioms.html)

---

#### [Kenny Lau (Apr 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125814400):
```lean
inductive tower : set (set (set α))
| empty : tower ∅
| succ  : ∀ {t}, tower t → tower (succ S t)
| chain : ∀ {C}, C ⊆ chains S → is_chain C → (∀ A ∈ C, tower A) → tower { A | ∃ t ∈ C, A ∈ t }
#print axioms succ -- classical.choice quot.sound propext
#print axioms tower -- no axioms
```
Why does `tower` use no axioms even though I clearly see `succ`?

#### [Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821103):
Kenny you are posting code which doesn't run

#### [Kenny Lau (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821104):
oops

#### [Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821105):
so I can only conjecture

#### [Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821106):
but not verify

#### [Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821108):
that if you instead try `#print axioms tower.mk`

#### [Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821109):
you will see the axioms you used

#### [Kevin Buzzard (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821116):
let me know if I answered your question

#### [Kenny Lau (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821118):
it's a prop so it has no k

#### [Kenny Lau (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821119):
mk

#### [Kevin Buzzard (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821170):
If it's a prop then maybe it really does use no axioms

#### [Kevin Buzzard (Apr 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821217):
because all those `cases H` which you had to change to `classical.some H` when you were working with data

#### [Simon Hudon (Apr 28 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821481):
An inductive type definition is not a definition in the kernel. It's built by postulating that `tower` is a type of the proper universe, that `empty`, `succ` and `chain` are functions that return a tower and that a recursor exists

#### [Kevin Buzzard (Apr 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822337):
sorry, someone came round

#### [Kevin Buzzard (Apr 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822338):
was going to finish "...can be changed back somehow"

#### [Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822343):
Actually I really do not understand what is going on here.

#### [Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822346):
Am I right in thinking that in general it is possible to construct Props which don't use axioms but whose construction essentially uses types which are not props and whose construction involves axioms?

#### [Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822347):
How much will Prop let us forget?

#### [Kevin Buzzard (Apr 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822386):
I do not know if I can make my question rigorous

#### [Simon Hudon (Apr 28 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125825885):
I don't get your question. Do you mean constructing pops that only uses inductive definitions?

#### [Gabriel Ebner (Apr 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125846688):
The technical answer is that the code for `#print axioms` does not traverse inductive declarations.  It only looks at the contents and types of definitions, and types of axioms.  This is probably not a problem since you presumably don't require choice if you never use `tower.succ`.

