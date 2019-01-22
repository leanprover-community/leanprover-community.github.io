---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/99807subtractiononnaturalnumbers.html
---

## [maths](index.html)
### [subtraction on natural numbers](99807subtractiononnaturalnumbers.html)

#### [Simon Hudon (Apr 11 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124913490):
Is there a name and notation to distinguish between subtraction on natural numbers and subtraction on integers? This is for my dissertation rather than a Lean proof

#### [Mario Carneiro (Apr 11 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914007):
Subtraction on natural numbers is sometimes called "monus" and denoted with a subtraction sign with a dot over it, like the top half of an american division sign

#### [Mario Carneiro (Apr 11 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914047):
like so: ∸

#### [Simon Hudon (Apr 11 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914053):
Thanks! Is there a LaTeX command for that?

#### [Mario Carneiro (Apr 11 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914058):
wiki says `\dot -`

#### [Mario Carneiro (Apr 11 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914101):
you will probably have to play with spacing to get it to look nice

#### [Simon Hudon (Apr 11 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914108):
Alright then

#### [Patrick Massot (Apr 11 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920713):
Short answer: use `unicode-math` and type ∸
Long answer: if for some reason, you don't want to use `unicode-math`, use its documentation: http://mirrors.ctan.org/macros/latex/contrib/unicode-math/unimath-symbols.pdf search for "dot above" and get to page 17 where you see that ∸ is translated to `\dotminus`.  The problem is that you need to find which package defines this (an information which is irrelevant if you go with unicode-math). Very quick google latex dotminus brings: https://tex.stackexchange.com/questions/360069/what-symbol-for-primitive-recursive-cutoff-minus

#### [Patrick Massot (Apr 11 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920758):
Actually maybe using this symbol in Lean could make sense

#### [Patrick Massot (Apr 11 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920760):
It would help mathematicians notice this is not the right operation

#### [Kevin Buzzard (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920768):
I think there's an argument for using some sort of modification on all the total extensions of the usual functions as well ;-)

#### [Mario Carneiro (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920771):
It's a thought, but I'd hate to have to explain to newcomers why `3 - 2 = 1` doesn't work

#### [Patrick Massot (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920777):
Yeah, this is not great either

#### [Patrick Massot (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920779):
Can we have both?

#### [Kevin Buzzard (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920780):
Yes but I have to explain why 2 - 3 gets evaluated as something wrong, which is worse

#### [Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920822):
Like, the lib uses the funny symbol but users can still use -

#### [Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920824):
And when they complain about 2 - 3 we tell them about ∸

#### [Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920825):
I don't know

#### [Kevin Buzzard (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920826):
I am not seriously advocating changes to `-` and `/`, however it was the realisation that I could think about them in this way which made me realise that the "make it total" system would not lead to contradictions.

#### [Mario Carneiro (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920827):
It's in core, so this isn't changing anyway

#### [Mario Carneiro (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920832):
this would break too much of the "programming" part of lean I think

#### [Kevin Buzzard (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920835):
Maybe obscure unicode characters which look the same and can be redefined by users is the best option :-)

#### [Mario Carneiro (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920837):
it would be hard to support a separate notation without a separate constant, and that would then mess up simp lemmas and such

#### [Mario Carneiro (Apr 11 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920885):
It's plausible that you could make a local notation (for `@has_sub.sub nat _`) work

#### [Mario Carneiro (Apr 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920948):
My favorite way to reason about `2 - 3` is to consider that `2 - 3 : nat` (since `-` is a binary op on `nat`) so it can't possibly be the "right" answer. Now just consider, what's the next best option?

#### [Mario Carneiro (Apr 11 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920993):
I think it suffices to just remind people that this isn't a partial function

