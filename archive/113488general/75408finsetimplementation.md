---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75408finsetimplementation.html
---

## Stream: [general](index.html)
### Topic: [finset implementation](75408finsetimplementation.html)

---


{% raw %}
#### [ Kenny Lau (Sep 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133565775):
What is the advantage of implementing `finset` as it is now, over implementing it as `multiset` quotient by extensionality?

#### [ Chris Hughes (Sep 08 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133566086):
I'm guessing efficiency of computation, but also perhaps some of the proofs are easier, since the functions are more or less identical to the multiset versions. Something like `finset.sum` is harder to implement with finsets as a quotient.

#### [ Kenny Lau (Sep 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133575013):
But if we implement it as a quotient, then we can have `finset.union`

#### [ Chris Hughes (Sep 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133575019):
Without `decidable_eq` you mean? Hooray. On the downside we'll need `decidable_eq` for `finset.sum` and `finset.card`

#### [ Simon Hudon (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586038):
@**Kenny Lau** I think both implementations can be valuable. Find a different name and then you can provide that new implementation.

#### [ Kenny Lau (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586041):
great

#### [ Kenny Lau (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586043):
could you help me think of a name?

#### [ Simon Hudon (Sep 09 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586089):
One benefit of `finset`'s current implementation is in writing programs that are meant to be executed. Keeping the list minimal is more economical on memory.

#### [ Simon Hudon (Sep 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586181):
The most obvious candidate would be `finset'` but I'm not sure that it's good. We could go with variations on `finset` (like `finite_set`) but I think that's more confusing than anything else. How about `no_eq.finset`?

#### [ Simon Hudon (Sep 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586195):
The other alternative would be to change the name of the current implementation to `compact.finset` or `minimal.finset` or `efficient.finset`

#### [ Simon Hudon (Sep 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586247):
I like your idea. Your kind of implementation makes a set that is easier to use as a monad and as a traversable collection.

#### [ Mario Carneiro (Sep 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586291):
I would suggest something like `qfinset` or `stacked_finset`

#### [ Mario Carneiro (Sep 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586293):
I'm not seeing where the gains are though

#### [ Kevin Buzzard (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586299):
you can have union without decidable equality :-)

#### [ Mario Carneiro (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586300):
gain*s* plural

#### [ Kevin Buzzard (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586301):
:-)

#### [ Kevin Buzzard (Sep 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586340):
Presumably this means that the two definitions can't be proved to be equal without decidable equality?

#### [ Mario Carneiro (Sep 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586342):
For the most part anything you can do with a stacked finset you can also do with a multiset

#### [ Mario Carneiro (Sep 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586354):
There is a computable function `finset -> qfinset` but the reverse is `erase_dup` which requires decidable eq

#### [ Kevin Buzzard (Sep 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586356):
gotcha

#### [ Mario Carneiro (Sep 09 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586398):
But all these functions already exist, between `finset` and `multiset`

#### [ Simon Hudon (Sep 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586470):
I can see three reasons for using stacked sets. 

1. you mean it to form a monad (or a similar kind of functor)
2. you need it to be traversable
3. you want to work with finite sets while using set equality directly without translating back and forth between set and multiset.

#### [ Simon Hudon (Sep 09 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586519):
`qfinset` is then like `set`+ finiteness invariant, similarly to `multiset`


{% endraw %}
