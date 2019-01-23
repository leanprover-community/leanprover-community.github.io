---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89822astrangetypeascriptionerror.html
---

## Stream: [general](index.html)
### Topic: [a strange type ascription error](89822astrangetypeascriptionerror.html)

---

#### [Scott Morrison (Jun 22 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464038):
I am getting an error of the form 
````
invalid type ascription, term has type
  @eq X a b
but is expected to have type
  @eq Y a b
````
where here `X` and (especially) `Y` are quite large expressions.

#### [Scott Morrison (Jun 22 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464065):
But `a` and `b` are just names of hypotheses. Any advice on dealing with this sort of thing?

#### [Scott Morrison (Jun 22 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464118):
It seems like merely from the fact that the two terms separately typecheck I should have a proof that `X = Y`...

#### [Scott Morrison (Jun 22 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464203):
Curiously here, even though the goal prints as `a = b`, writing `show a = b` results in `show tactic failed`.

#### [Scott Morrison (Jun 22 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128465208):
... immediate problem solved, (remove a few unnecessary `@[reducible]` attributes), although I don't really understand what was going wrong.

#### [Reid Barton (Jun 22 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128474905):
I have seen a tactic produce a goal which was not well-typed before, and it was very confusing. Sounds like the same sort of issue?

#### [Reid Barton (Jun 22 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128475258):
In my case the offending tactic was `induction using quotient.ind`; from your resolution, it sounds unrelated

#### [Reid Barton (Jun 22 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128475337):
I guess the main point is that "the goal in tactic mode is well-typed" is not a 100% iron-clad guarantee, although it surely indicates a bug somewhere if it is violated.

