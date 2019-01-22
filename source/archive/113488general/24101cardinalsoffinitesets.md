---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24101cardinalsoffinitesets.html
---

## [general](index.html)
### [cardinals of finite sets](24101cardinalsoffinitesets.html)

#### [Mario Carneiro (Aug 18 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132344762):
People have mentioned that working with the size of finite sets is a bit complicated right now. We have two methods to talk about the cardinality of a type:

* `fintype.card A`, which requires a `[fintype A]` instance (and hence asserts cardinality separately from finiteness), and
* `cardinal.mk A`, which works on any type but has type `cardinal` instead of `nat` (which makes it useful for different sizes of infinite sets).

In order to use this latter expression to assert a set has a finite number cardinality you have to write `cardinal.mk A = ↑n` where `n : nat`, which is a bit messy, since `cardinal.mk A = 37` is not the same as `cardinal.mk A = ↑37` (you can use `simp` to turn one into the other).

I would like to make it easy to talk about finite sets with natural number cardinalities, without having finiteness as a precondition. Some options:

* `has_card A n` is `{ x : fintype A // card A x = n }`. This has the advantage that it is computable, and a subsingleton, although it is not a proposition stated this way. Since it is a relation rather than a function, you can't rewrite with it, but whether this is a problem depends on how it is used.
* `card_xnat A : with_top nat` is a noncomputable function that takes the value `⊤` on infinite sets and `n` on finite sets of cardinality `n`. Here we can state lemmas like `card_xnat (sum A B) = card_xnat A + card_xnat B` without preconditions, and prove equality with other kinds of cardinality to relate back to the computable versions.
* `card_nat A : nat` is the same as `card_xnat` but with a 0 default value instead of `⊤`. This is really just a totalized partial function, so many theorems will not hold without finiteness assumptions, but it has the advantage that it takes values in `nat` so you get the same experience as `fintype.card A` but without the dependent argument, which can sometimes mess up rewrites.

#### [Johannes Hölzl (Aug 18 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132355335):
I'm currently finishing `ennreal := with_top nnreal`. The setup should work also for `nat`, then `card_xnat` (maybe named `card_enat`, c.f. `ennreal`) would work nice, as it goes into a complete lattice.

#### [Chris Hughes (Aug 18 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356222):
What's the solution used on Coq? Presumably they must have dealt with this a lot to prove Feit Thompson.

#### [Mario Carneiro (Aug 18 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356604):
feit thompson dealt almost exclusively in finite group theory

#### [Mario Carneiro (Aug 18 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356605):
so it wasn't a problem to have finiteness assumptions everywhere

#### [Mario Carneiro (Aug 18 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356614):
plus ssreflect has a lot of slightly different approaches to all this stuff which emphasizes `bool` predicates over propositions

#### [Mario Carneiro (Aug 18 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356665):
Metamath has a `#` function which is essentially `card_enat`; it has a range which is a subset of ennreal (of course they don't deal with subtypes like we do here)

#### [Mario Carneiro (Aug 18 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356675):
but you could say basically `#({A, B, C}) = 3` where that is the usual `3`

#### [Mario Carneiro (Aug 18 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356726):
and this was a distinct function from `card : V -> On` which takes values in the ordinals (and defines the cardinals as the range of this function)

#### [Mario Carneiro (Aug 18 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356791):
I think that in general the classical mathematics approach used in lean makes it resemble Isabelle and Metamath a lot more than Coq

#### [Chris Hughes (Aug 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084180):
May I suggest another option. If we're going down the noncomputable route and the having two different definitions route, I think the best solution is to have a `finite` predicate to use instead of `fintype`. This has the advantage of solving the `rw` issue, which also indirectly helps the type class inference issue, because theorems like `card_empty` wouldn't need `fintype empty` as an input, which makes the type class inference issue easier as well.

All of these options seem wrong to me however, and I'd much rather not confuse people even more by introducing a fourth way of talking about finite cardinals.

#### [Kenny Lau (Aug 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084213):
what is your fourth way?

#### [Chris Hughes (Aug 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084379):
Making a `finite` predicate instead of `fintype` which is `Type`

#### [Johannes Hölzl (Aug 31 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133108434):
We have already `set.finite`. It was defined as inductive over empty and insert, currently it is defined by saying that the set coerced to a type is a `fintype`.

