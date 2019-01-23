---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25137inductivelydefinedfinsupp.html
---

## Stream: [general](index.html)
### Topic: [inductively-defined finsupp?](25137inductivelydefinedfinsupp.html)

---

#### [Kenny Lau (Mar 29 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124364521):
Can we define finsupp A B inductively as a set of the type (A -> B)?

#### [Johannes Hölzl (Mar 29 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365156):
I'm not sure what you mean?
If you want to define it as an inductive like lists, i.e. the constant zero function, and a constructor to insert an element: this doesn't work, it requires a quotient over the sequence of at which point you add an element, also the constructor requires a proof that the inserted element was zero in the function is not zero. 
We can slightly change the definition to:
```lean
structure finsupp (α : Type u) (β : Type v) [has_zero β] :=
(to_fun : α → β)
(fintype_support : fintype {a | to_fun a ≠ 0})
```
Which would be a good idea...

#### [Kenny Lau (Mar 29 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365223):
@**Johannes Hölzl** I mean an inductively-defined set

#### [Johannes Hölzl (Mar 29 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365286):
You mean the set `{f | finite {a | f a ≠ 0 }}`?
You can:
```lean
inductive is_finsupp [has_zero B] : (A -> B) -> Prop
| zero: is_finsupp (\x, 0)
| insert {a b} : is_finsupp f -> is_finsupp (\x, if x = a then b else f x)
```

#### [Kenny Lau (Mar 29 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365330):
right

#### [Kenny Lau (Mar 29 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365335):
and why isn't this used?

#### [Johannes Hölzl (Mar 29 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365385):
We want to something which is a type and isomorph to the subtype of this set. This allows us to define type class instances. The current version also gives us (mostly) nice computational rules for the function and for the support.

