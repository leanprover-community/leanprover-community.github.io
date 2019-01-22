---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05553Finitemaps.html
---

## [general](index.html)
### [Finite maps](05553Finitemaps.html)

#### [Ben Sherman (Nov 06 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146891105):
Is there a Lean (3) library for finite maps (i.e., key-value maps where finitely many keys are mapped to values)? I don't need performance, just reasoning really. But I'd also be fine if the key type requires decidable ordering (I would assume it would require at least decidable equality). Should I use this https://github.com/spl/lean-finmap?

#### [Reid Barton (Nov 06 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146891398):
There's `data.rbmap` in the Lean standard library, does that meet your needs?

#### [Mario Carneiro (Nov 06 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146891483):
There is also the `finmap` branch of leanprover-community which is porting Sean's work to mathlib

#### [Mario Carneiro (Nov 06 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146891514):
and `hash_map` is also a finite map type

#### [Mario Carneiro (Nov 06 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146891603):
on the non-computational side, `finsupp` is basically the type of finite maps (mapping everything out of domain to 0)

#### [Ben Sherman (Nov 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146892020):
I'm looking for something that has unions and theorems about them. In this regard, both `data.rbmap` and `data.hash_map` are incomplete. And I do want to write programs, so `finsupp` is not what I'm looking for either. So it sounds like `finmap` is the way to go! Thanks for pointing me to the `finmap` branch of mathlib - I guess I'll use that. Thanks for the pointers, everyone!

#### [Mario Carneiro (Nov 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite maps/near/146892405):
Ah, that's good to know. I'll work on adding unions to rbmap and hash_map

