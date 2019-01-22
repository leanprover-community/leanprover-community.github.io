---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52657beginnerequalityquestion.html
---

## [general](index.html)
### [beginner equality question](52657beginnerequalityquestion.html)

#### [dan pittman (Jun 26 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128673907):
I'm attempting to assert whether two elements of a list are equal, and then act on that assertion in an `if-then-else` manner, but for my `x = y` assertion, there is no `decidable` instance. Perhaps there's a different approach I ought to be taking?

#### [Chris Hughes (Jun 26 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128674057):
Using the line `local attribute [instance] classical.prop_decidable` should help, but it will stop your functions being computable. What type do `x` and `y` have? You could also make `[decidable_eq α]` an argument to your function, if it's defined on an arbitrary type.

#### [dan pittman (Jun 26 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128676882):
Thanks! `decidable_eq` is what I was looking for! I'd written this in Haskell first, and was of course using `Eq a => ...`.

