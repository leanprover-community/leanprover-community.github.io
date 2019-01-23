---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57079confusionwithsigmatypes.html
---

## Stream: [general](index.html)
### Topic: [confusion with sigma types](57079confusionwithsigmatypes.html)

---


{% raw %}
#### [ Scott Morrison (Sep 22 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419058):
Oops... oversimplified my example.

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419121):
```
def f (n : ℕ) : Type := { l : list ℕ // l.length = n }

def foo : Σ n ≥ 5, f n := sorry
def foo' : Σ n : ℕ, Σ H : n ≥ 5, f n := sorry
```

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419163):
both `foo` and `foo'`error with 
```
type mismatch at application
  Σ (H : n ≥ 5), f n
term
  λ (H : n ≥ 5), f n
has type
  n ≥ 5 → Type : Type 1
but is expected to have type
  ?m_1 → Type : Type (max ? 1)
```

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419164):
what am I doing wrong?

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419170):
Can you just not index sigma types by Props?!

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419171):
ugh.

#### [ Mario Carneiro (Sep 22 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419236):
use `Σ'` or `subtype`

#### [ Scott Morrison (Sep 22 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419775):
Thanks.

#### [ Simon Hudon (Sep 22 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420363):
Does `subtype` do anything that `Σ'` doesn't do?

#### [ Mario Carneiro (Sep 22 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420404):
no, except have easier universe constraints

#### [ Simon Hudon (Sep 22 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420439):
Could it benefit from a `unit` / `punit` approach?

#### [ Mario Carneiro (Sep 22 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134421471):
Huh? It is a `unit`/`punit` approach. I mean it's even called `psigma`

#### [ Simon Hudon (Sep 22 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134421513):
Right but what happened with `unit` is that it became a synonym for `punit.{0}`


{% endraw %}
