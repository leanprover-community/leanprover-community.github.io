---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04628Inductivepropsyntax.html
---

## [new members](index.html)
### [Inductive prop syntax](04628Inductivepropsyntax.html)

#### [cbailey (Aug 29 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Inductive prop syntax/near/133006097):
Hi, I was wondering if anyone can explain the inductive prop syntax in Lean a little bit; the definition of less_than_or_equal in basic.lean is written in a way that returns a partially applied function for the base case (|refl: less_than_or_equal a), but it doesn't visibly define behavior for that curried return function that would actually say when the prop is true. I noticed that if I #print less_than_or_equal, it comes back as the more familiar Coq style of |refl: forall (a: nat), less_than_or_equal a a, where you explicitly say this prop is true if the two elements are a and a, and the prop has the signature nat -> nat -> Prop without the named (a: nat) parameter. Does Lean default to using reflexivity as the truth condition for an inductively defined prop's base case, or is there something more important about the partially applied function that I'm missing?
Thanks!

#### [Kevin Buzzard (Aug 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Inductive prop syntax/near/133012820):
These aren't partially applied -- there's a trick. The definition is

```lean
inductive less_than_or_equal (a : ℕ) : ℕ → Prop
| refl : less_than_or_equal a
| step : Π {b}, less_than_or_equal b → less_than_or_equal (succ b)
```

but you see the `a` in the first line is left of the colon, so when you see `less_than_or_equal` on the second or third line you should read `less_than_or_equal a`. Now it all makes sense :-)

#### [cbailey (Aug 30 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Inductive prop syntax/near/133062381):
Thank you! That makes sense.

