---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/83619directedmap.html
---

## [maths](index.html)
### [directed map](83619directedmap.html)

#### [Mario Carneiro (Nov 06 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146847285):
Does this concept look familiar to anyone?
```lean
variables [preorder α] [preorder β] (m : α → β)
class directed_map : Prop :=
(mono : monotone m)
(dir : ∀ x, directed_on (≥) {a | x ≤ m a})
```

#### [Mario Carneiro (Nov 06 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146847552):
Turns out this is what you need to map a preorder filter. It's a category

#### [Mario Carneiro (Nov 06 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146847622):
By the way, does anyone have any naming suggestions for preorder filters vs set filters?

#### [Mario Carneiro (Nov 06 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146847624):
"prefilter" just occurred to me

#### [Patrick Massot (Nov 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146849018):
What is a preorder filter?

#### [Mario Carneiro (Nov 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146849250):
It is a subset of a preorder which is nonempty, upward closed, and has an element below any two elements in the filter (downward directed)

#### [Mario Carneiro (Nov 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146849262):
basically you generalize the part about filters being sets of sets to sets in a more general ordered structure

#### [Reid Barton (Nov 06 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146872338):
It looks similar to (and implies) the notion of [(co)final functor](https://ncatlab.org/nlab/show/final+functor#definition), but I don't remember seeing this exact notion before.

#### [Reid Barton (Nov 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146872406):
I like the name "directed map", because you have the property: `\a` is directed if and only if the unique map `\a \to unit` is directed

#### [Reid Barton (Nov 06 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146872843):
"prefilter" however strikes me as a word which should mean a filter minus some property, or something like a filter basis. Compare presheaf/sheaf, (historically) prescheme/scheme = (scheme/separated scheme).

#### [Reid Barton (Nov 06 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146873026):
I suppose using `filter` for both cases is infeasible, or you wouldn't be asking the question?

#### [Floris van Doorn (Nov 06 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146874734):
`filter` and `set_filter`? Or is renaming the current one out of the question?

#### [Sebastien Gouezel (Nov 06 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146874798):
`order_filter` and `filter`?

#### [Reid Barton (Nov 06 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed map/near/146874970):
We could also make use of namespacing perhaps

