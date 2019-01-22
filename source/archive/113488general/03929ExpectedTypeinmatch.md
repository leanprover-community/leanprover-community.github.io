---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03929ExpectedTypeinmatch.html
---

## [general](index.html)
### [Expected Type in match](03929ExpectedTypeinmatch.html)

#### [Nima (Apr 21 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483132):
Is there anyway to **explicitly** tell lean the expected type of `match`, so I would not receive the following error:
```quote
invalid match/convoy expression, user did not provide type for the expression, 
lean tried to infer one using expected type information, but result is not type correct
```

#### [Kenny Lau (Apr 21 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483171):
for example?

#### [Mario Carneiro (Apr 21 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483313):
`match a, b : \forall a b, expected_type_of_match with ... end`

#### [Mario Carneiro (Apr 21 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483320):
You can also often use type ascription in some cases, i.e. `(match a, b with ... end : expected type)`

#### [Nima (Apr 21 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483564):
OK, I don't have a good example for this.
Will get back if I found one.

#### [Nima (Apr 21 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483729):
Thank you, this following worked (the other one did not), 
```quote
`match a, b : \forall a b, expected_type_of_match with ... end`
```

