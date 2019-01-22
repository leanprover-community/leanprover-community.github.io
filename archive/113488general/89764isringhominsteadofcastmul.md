---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89764isringhominsteadofcastmul.html
---

## [general](index.html)
### [is_ring_hom instead of cast_mul](89764isringhominsteadofcastmul.html)

#### [Chris Hughes (Apr 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom instead of cast_mul/near/125591171):
What's the reason not to mark `coe` as a ring_hom instead of using `int.cast_mul` and stuff like that?

#### [Mario Carneiro (Apr 24 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom instead of cast_mul/near/125592816):
Well, for one thing `ring_hom` didn't exist when `cast` was written

#### [Mario Carneiro (Apr 24 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom instead of cast_mul/near/125592828):
but `ring_hom.mul` is not applicable as a simp lemma for reasons that have been discussed before, so we would still want `int.cast_mul` in any case

#### [Mario Carneiro (Apr 24 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_ring_hom instead of cast_mul/near/125592850):
But it's reasonable to prove that `coe` is a ring_hom given the existing theorems

