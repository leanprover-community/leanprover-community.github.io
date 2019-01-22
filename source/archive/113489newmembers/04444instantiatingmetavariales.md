---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04444instantiatingmetavariales.html
---

## [new members](index.html)
### [instantiating meta variales](04444instantiatingmetavariales.html)

#### [Ken Roe (Jul 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230234):
Is there a way to instantiate meta variables.  Consider the theorem below:
```lean
theorem x: ∃ x, x=5 :=
begin existsi _, ..
end
```

What should the ...  be replaced with?  In this theorem, we could just change the existsi _ but in more complex theorems, meta variables seem to appear in many other places and it would be nice to instantiate them.

#### [Kenny Lau (Jul 24 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230270):
what information would you provide in order for the metavariables to be instantiated?

#### [Kenny Lau (Jul 24 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130230286):
replacing `..` with `refl` would prove the theorem, but I don't know if that is what you want

#### [Ken Roe (Jul 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130231216):
refl is not what I want.  In Coq, you can provide a value using instantiate (meta_var := value).  Is there something similar in Lean?

#### [Patrick Massot (Jul 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130231266):
Doesn't this meta variable appear as a new goal?

#### [Kevin Buzzard (Jul 24 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232163):
`existsi 7` will instantiate the metavariable. If you use a hole `_` then you get a new goal `⊢ ℕ` as Patrick says. You can make this the first goal with `show ℕ` or `swap` and then instantiate it with `exact 7`.

#### [Ken Roe (Jul 24 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232676):
I've seen those new goals as holes--that is how to fill in the holes.  Can swap be used beyond the second goal or is there something similar to switch for example the first and third goal?

#### [Patrick Massot (Jul 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232717):
https://github.com/leanprover/mathlib/blob/master/tactic/interactive.lean#L159

#### [Patrick Massot (Jul 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232719):
as explained by Kevin

#### [Patrick Massot (Jul 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/instantiating%20meta%20variales/near/130232781):
You can also use `show` if you have only one goal of that type

