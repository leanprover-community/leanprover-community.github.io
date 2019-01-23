---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88283funnyerror.html
---

## Stream: [general](index.html)
### Topic: [funny error](88283funnyerror.html)

---


{% raw %}
#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342120):
I could not minimize this error.

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342121):
https://gist.github.com/kckennylau/a62295136d2daf48146f6fcdb8e37a49

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342122):
error:

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342123):
```lean
type mismatch at field 'right_inv'
  ?m_1
has type
  function.right_inverse (λ (φ : alg_hom (polynomial R) A), φ.val (finsupp.single 1 1))
    (λ (r : A),
       ⟨λ (f : polynomial R),
          finsupp.sum f (λ (n : ℕ) (c : R), (λ (r : R) (x : A), algebra.f A r * x) c (monoid.pow r n)),
        _⟩)
but is expected to have type
  function.right_inverse (λ (φ : alg_hom (polynomial R) A), φ.val (finsupp.single 1 1))
    (λ (r : A), ⟨λ (f : polynomial R), finsupp.sum f (λ (n : ℕ) (c : R), c • r ^ n), _⟩)
```

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342164):
where `?m_1` was a literal underscore

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342165):
that's it folks, an underscore has a type error

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342171):
@**Mario Carneiro**

#### [ Kevin Buzzard (May 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344095):
I think we've seen this happen before

#### [ Kevin Buzzard (May 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344099):
were you making a big structure and doing crazy stuff like sorrying out constants?

#### [ Kevin Buzzard (May 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344193):
I find these sorts of things a bit annoying to do for reasons like this


{% endraw %}
