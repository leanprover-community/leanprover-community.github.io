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
<p>Do we already have the Galois correspondence for <code>set.map</code> and <code>set.comap</code> (aka, <code>range</code> and <code>preimage</code>)?<br>
Is there machinery to glue Galois correspondences together? E.g. I would like to get a Galois correspondence for <code>opens.map</code> and <code>opens.comap</code> more or less for free.</p>

#### [ Johannes Hölzl (Nov 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870563):
<p>its between <code>set.image</code> and <code>set.preimage</code> (and there is one between <code>preimage</code> and <code>kern_image f s := {y | ∀x, f x = y → x ∈ s}</code>)</p>

#### [ Johannes Hölzl (Nov 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870566):
<p>its in <code>data.set.lattice</code></p>

#### [ Johan Commelin (Nov 17 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20correspondences/near/147870605):
<p>Thanks</p>


{% endraw %}
