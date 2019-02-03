---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38477imageofcomplement.html
---

## Stream: [general](index.html)
### Topic: [image of complement](38477imageofcomplement.html)

---


{% raw %}
#### [ Patrick Massot (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655801):
<p>Do we have <code>{α : Type*} {β : Type*} (f : α ≃ β) (s : set α) : f '' -s = -(f '' s)</code> in mathlib?</p>

#### [ Johannes Hölzl (Mar 13 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655882):
<p>I guess you want <code>f : A -&gt; B</code>, its <code>preimage_compl</code>.</p>

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656012):
<p>No, I'd like what I stated</p>

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656014):
<p>with direct image</p>

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656016):
<p>assuming bijectivity</p>

#### [ Patrick Massot (Mar 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656081):
<p>I admit both the equiv and double apostrophes are hard to read on my screen too</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656089):
<p>you could use <code>preimage_compl</code> on the map in the other direction ;-)</p>

#### [ Patrick Massot (Mar 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656124):
<p>I'm pretty sure I can prove this lemma, I was asking about its current existence</p>

#### [ Johannes Hölzl (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656345):
<p>Ah sorry. Then no: I think its not yet in mathlib.</p>

#### [ Patrick Massot (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656352):
<p>Ok, I hope I'll be able to contribute this</p>


{% endraw %}
