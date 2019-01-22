---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35057dictionarymaptypeordset.html
---

## [general](index.html)
### [dictionary / map type: ordset](35057dictionarymaptypeordset.html)

#### [Mario Carneiro (Dec 11 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151471035):
I've been playing around with conventional programming in lean lately (thank you Advent of Code), and it has made me realize that our capabilities with finite maps is quite limited. Currently, we have:

* `native.rb_map`: meta interface to a C++ implementation of red black trees
* `rbmap`: lean implementation of red black trees in core
* `finmap`: maps via association lists (in mathlib)
* `finsupp`: finitely supported functions (non computational)

The only one which is really suitable for computation is `rbmap` (`finmap` is too slow, since it is implemented with lists, although it is useful for specifications and verified computation), and it is implemented in core with basically only two operations: `insert` and `find`. And because the well-formedness condition is incorrect, you can't even implement more operations, like `erase`.

So I decided to start anew with weight balanced trees, as a direct port from Haskell's `Data.Set`. The result is the [`ordnode A`](https://github.com/leanprover-community/mathlib/blob/ordmap/data/ordmap/ordnode.lean) type, which has a very complete set of operations for working with sets and maps. The library for `ordset A` is still under development but will incorporate the correct invariants on top of `ordnode A` so that the usual properties are provable.

PS: The names `ordnode`, `ordset`, `ordmap` are a bit inelegant, I'm open to suggestions.

#### [Gabriel Ebner (Dec 11 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472291):
`ordset α` does not seem to be isomorphic to `finset α`---is this intentional?

#### [Mario Carneiro (Dec 11 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472428):
I added the equivalence relatively recently (`ordnode.equiv`). I will change `ordset` to be a quotient of the current subtype

#### [Mario Carneiro (Dec 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472565):
Also it's not going to be isomorphic to `finset A` anyway, because of preorder stuff

#### [Mario Carneiro (Dec 11 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472607):
I think the `ordset`s over a linear order should be isomorphic to `finset A`

#### [Mario Carneiro (Dec 11 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472787):
(more precisely, over a total preorder, a `ordset A` can only represent a comparability antichain, i.e. `x, y \in s` and `x <= y` and `y <= x` implies `x = y`)

#### [Gabriel Ebner (Dec 11 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472863):
Yeah, with the quotient they should be isomorphic for total orders.

#### [Joe Hendrix (Dec 11 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151473732):
I had my own version of rb trees  while back (https://github.com/joehendrix/lean-containers/).  It uses quotients so we can get a decidable equivalence relation.
I had to put it on hold for other projects, and only got around to insert (so it's close to the existing rbmap capabilities).  I think it also probably doesn't work with the latest lean 3.  Maps are implemented on top of sets.

#### [Edward Ayers (Dec 11 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151480189):
I ported Coq's implementation of RB trees (sans proofs).  I also didn't test it much so has bugs.
https://github.com/EdAyers/edlib/blob/master/rb.lean

#### [Edward Ayers (Dec 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151481780):
For naming, I vote `table`

