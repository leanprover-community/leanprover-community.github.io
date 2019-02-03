---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89764isringhominsteadofcastmul.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [is_ring_hom instead of cast_mul](https://leanprover-community.github.io/archive/113488general/89764isringhominsteadofcastmul.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Apr 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom%20instead%20of%20cast_mul/near/125591171):
<p>What's the reason not to mark <code>coe</code> as a ring_hom instead of using <code>int.cast_mul</code> and stuff like that?</p>

#### [ Mario Carneiro (Apr 24 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom%20instead%20of%20cast_mul/near/125592816):
<p>Well, for one thing <code>ring_hom</code> didn't exist when <code>cast</code> was written</p>

#### [ Mario Carneiro (Apr 24 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom%20instead%20of%20cast_mul/near/125592828):
<p>but <code>ring_hom.mul</code> is not applicable as a simp lemma for reasons that have been discussed before, so we would still want <code>int.cast_mul</code> in any case</p>

#### [ Mario Carneiro (Apr 24 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom%20instead%20of%20cast_mul/near/125592850):
<p>But it's reasonable to prove that <code>coe</code> is a ring_hom given the existing theorems</p>


{% endraw %}
