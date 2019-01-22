---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71470Attributecachingimplementationdetails.html
---

## [general](index.html)
### [Attribute caching implementation details](71470Attributecachingimplementationdetails.html)

#### [Keeley Hoek (Nov 08 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/147281757):
(Warning: I don't know how lean being multithreaded works.)

I've been thinking about how you can store data in an identifier tagged with an attribute. Since a tactic being executed in (for example) the course of a proof can modify this data and change its behaviour based on it, are tactics using this data thread-safe? If for example a piece of attribute data keeps track of a list of things, which might be added to using another attribute or something like that, is it possible that the list contents are read simultaneously, each have a different element appended to them, and then two threads race to write their contents back to the same field with one ultimately winning?

I just can't see how it could possibly be thread-safe. If this is the case, isn't it dangerous (except in trivial situations) for anything to set the data associated to a  attribute?

#### [Mario Carneiro (Nov 08 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/147282069):
It's a functional data structure, so there isn't any possibility for races

#### [Mario Carneiro (Nov 08 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/147282132):
The data associated to an attribute is a pure function of the set of names that have the attribute in the environment

#### [Mario Carneiro (Nov 08 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/147282194):
or maybe more usefully, it is a function of the `environment` object, which is itself a functional data structure

#### [Mario Carneiro (Nov 08 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/147282289):
Each definition adds to the `environment` object in a way similar to `list.cons`. The old environment is still available. In particular, AFAIK the only multithreading lean does (in a single file) is in proof checking, and proofs (`theorem` elaboration) are not allowed to modify the environment (any changes they make are inlined or rolled back when the proof is complete). `def`s are allowed to modify the environment, but they run sequentially in the file processing.

#### [Keeley Hoek (Nov 26 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/148372817):
I'm still a bit confused about this
What happens if two tactics running in proofs of separate `theorem`s set conflicting `options`, for example?

#### [Keeley Hoek (Nov 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Attribute caching implementation details/near/148372975):
Oh sorry, you explained---the changes are forgotten

