---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53623metauniverses.html
---

## [general](index.html)
### [meta + universes](53623metauniverses.html)

#### [Reid Barton (Sep 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133974969):
Could/should :four_leaf_clover: allow `meta` to break "universe safety", e.g., stick a field of type `Type` inside a structure declared to have type `Type`?

#### [Reid Barton (Sep 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133975221):
To support things like existential types in Haskell

#### [Sebastian Ullrich (Sep 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133975646):
It's not a bad idea. We have discussed it before, but there are some issues in the details. For example, we would still like to distinguish between values and proofs in the compiler. Anyway, you should be able to define existential types in meta Lean 3 using a generalized version of `unchecked_cast` that can cast between universes

#### [Mario Carneiro (Sep 14 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133980222):
Ah, this is a nice idea, I hadn't thought about using `unchecked_cast` to enable universe casting. I'll add an interface for this in mathlib

#### [Mario Carneiro (Sep 14 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133980318):
I think that the best way to enable this kind of thing in meta land without having a whole different language is to do all universe checks as normal, but drop the check on maximum universe levels for `meta inductive`s

#### [Mario Carneiro (Sep 14 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133980377):
so it would still generate the same recursors as normal, but if the type is supposed to be `Type 3` and you say `Type 1` instead then that's okay

#### [Sebastian Ullrich (Sep 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/133980492):
Right, we discussed that before but never followed up on it https://github.com/leanprover/lean/pull/1580#issuecomment-301203751

#### [Mario Carneiro (Sep 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003123):
@**Sebastian Ullrich** Whoa, this was not expected. Not only does the advertised method not work, but I think I can prove there is no workaround, that is, VM evaluation respects universes! This means that something like universe inconsistent inductives may be the only way to make this work.

#### [Kenny Lau (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003181):
can we define a function that sends `u : nat` to `Type u`?

#### [Mario Carneiro (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003182):
`u : nat` does not typecheck

#### [Kenny Lau (Sep 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003185):
not even in the unsafe level?

#### [Mario Carneiro (Sep 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003190):
they are not the same thing

#### [Mario Carneiro (Sep 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003192):
levels and natural numbers are completely different, syntactically

#### [Kenny Lau (Sep 15 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003257):
where is `max` defined?

#### [Mario Carneiro (Sep 15 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003296):
nowhere, it's primitive

#### [Mario Carneiro (Sep 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta + universes/near/134003307):
Basically, `unchecked_cast` works by casting across a sorried proof of type equality, which is erased by the VM so that the equality recursor just steps directly from one type to another, and hopefully the VM representations match up so this makes sense. But the equality can only go between two elements of the same universe, and similarly with heq. Indeed, if you look at the recursor of any inductive, it has a motive that lands in `Type l` for some fixed `l`, and you can only move from one place to another along this family, meaning you can never escape `Type l` by application of this recursor.

