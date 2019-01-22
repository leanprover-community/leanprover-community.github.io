---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55735categorytheorydirectories.html
---

## [general](index.html)
### [category theory directories](55735categorytheorydirectories.html)

#### [Reid Barton (Aug 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605394):
@**Scott Morrison**, would you accept PRs to `lean-category-theory` and `lean-category-theory-pr` which move everything from `categories/` to `category_theory/`?

#### [Reid Barton (Aug 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605484):
I'm trying to update my project to use the new mathlib with categories, and I'd rather only go through the Great Renaming of modules once

#### [Reid Barton (Aug 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605487):
And, I also use your `-pr` library.

#### [Reid Barton (Aug 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132609260):
Actually, I may just add some "forwarding" modules to my project for now, since I think I only use a few modules from `-pr` at this point.

#### [Scott Morrison (Aug 25 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751901):
Okay, the `lean-category-theory-pr`library has finally been laid to rest, and there's just mathlib and `lean-category-theory`.  Sorry about that. :-)

#### [Scott Morrison (Aug 25 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751912):
In related news, `lean-category-theory` now contains my updated version of limits (not all the colimit stuff is filled in yet, hoping someone wants to write me a nice tactic. :-)

#### [Scott Morrison (Aug 25 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751960):
It's missing some things that used to be in `lean-category-theory`, in particular constructing limits from products and equalizers, and showing that if D has limits, the functor category `C \lea D` has limits too. Hopefully these should be easier to reimplement with the new design, anyway.

#### [Reid Barton (Aug 25 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132752036):
It turned out `.isomorphisms` was the only module I was using, so it was easy to work around.

