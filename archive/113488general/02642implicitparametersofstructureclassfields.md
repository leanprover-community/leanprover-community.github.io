---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02642implicitparametersofstructureclassfields.html
---

## [general](index.html)
### [implicit parameters of structure/class fields](02642implicitparametersofstructureclassfields.html)

#### [Reid Barton (Nov 26 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit parameters of structure/class fields/near/148375439):
Are the rules for the types of the field accessors (in particular, whether arguments are explicit or implicit) written out somewhere (not in C++)?

#### [Keeley Hoek (Nov 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit parameters of structure/class fields/near/148408330):
I don't fully know what you mean Reid, so sorry if this stuff you already know, but given `struct : name` and `field : name` you can infer the type of the honest function named `struct` and of the projection `struct ++ field`, then unwind the Pi binders off the projection which just correspond to the type arguments passed to `struct`. That's how I've figured out what all the arguments are and what their `binder_info` is in the past.

