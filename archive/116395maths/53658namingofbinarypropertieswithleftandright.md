---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53658namingofbinarypropertieswithleftandright.html
---

## [maths](index.html)
### [naming of binary properties with left and right](53658namingofbinarypropertieswithleftandright.html)

#### [Sean Leather (Apr 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming of binary properties with left and right/near/125715828):
@**Chris Hughes** updated his `finset.disjoint` PR with a [change](https://github.com/leanprover/mathlib/commit/009ff9b) to rename the following:

* `empty_disjoint` → `disjoint_empty_left`
* `disjoint_empty` → `disjoint_empty_right`

Personally, I prefer the new names: they are more descriptive and don't rely on positional naming, which can be confusing. But I wanted to open up a discussion on this in general to determine the mathlib style guidelines. I don't think these types of things have been consistently named.

#### [Sean Leather (Apr 26 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming of binary properties with left and right/near/125715961):
We probably want feedback from @**Johannes Hölzl** and @**Mario Carneiro** in particular.

#### [Chris Hughes (Apr 26 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming of binary properties with left and right/near/125730500):
There's also the question of which one's `right` and which one's `left`. I would have named `dvd_mul_right : a ∣ a * b` `dvd_mul_left`

#### [Kenny Lau (Apr 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming of binary properties with left and right/near/125732771):
@**Chris Hughes** confer or.inl and or.inr

#### [Sean Leather (Apr 30 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming of binary properties with left and right/near/125881780):
I created a [GitHub issue](https://github.com/leanprover/mathlib/issues/129) for this discussion. Please leave any thoughts there.

