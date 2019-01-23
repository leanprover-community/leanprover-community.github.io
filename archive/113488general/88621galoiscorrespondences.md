---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88621galoiscorrespondences.html
---

## Stream: [general](index.html)
### Topic: [galois correspondences](88621galoiscorrespondences.html)

---


{% raw %}
#### [ Johan Commelin (Nov 17 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147866625):
Do we already have the Galois correspondence for `set.map` and `set.comap` (aka, `range` and `preimage`)?
Is there machinery to glue Galois correspondences together? E.g. I would like to get a Galois correspondence for `opens.map` and `opens.comap` more or less for free.

#### [ Johannes Hölzl (Nov 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870563):
its between `set.image` and `set.preimage` (and there is one between `preimage` and `kern_image f s := {y | ∀x, f x = y → x ∈ s}`)

#### [ Johannes Hölzl (Nov 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870566):
its in `data.set.lattice`

#### [ Johan Commelin (Nov 17 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870605):
Thanks


{% endraw %}
