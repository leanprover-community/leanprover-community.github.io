---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91356primeinringtheoryassociatedlean.html
---

## Stream: [general](index.html)
### Topic: [prime in `ring_theory/associated.lean`](91356primeinringtheoryassociatedlean.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 23 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148200980):
`ring_theory/associated.lean` defines 
```
/-- prime element of a semiring -/
def prime [comm_semiring α] (p : α) : Prop :=
p ≠ 0 ∧ ¬ is_unit p ∧ (∀a b, p ∣ a * b → p ∣ a ∨ p ∣ b)
```
in the root namespace, which then causes clashes with `nat.prime` if you have `nat` open.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 23 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148200985):
Could we rename or namespace this? @**Johannes Hölzl**  introduced it [here](https://github.com/leanprover/mathlib/commit/f2beca809321e92b1cb543c2bcac2b031754da43).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201039):
We could just get rid of nat prime as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201079):
wat @_@

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201259):
What do you mean, @**Chris Hughes**?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201315):
Just get rid of `nat.prime` and use prime in its place. I just realized that currently nat.prime is basically `irreducible `, so this would be a non trivial redactor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 23 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201407):
Oh, I see! That sounds both a good idea and ambitious. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 23 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201408):
Is there a good fix in the meantime?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 23 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209287):
I would just call this one `ring.prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209416):
I'm okay with `ring.prime` if the kill nat.prime thing doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209463):
although I've already fixed some bugs caused by this in the library (adding `nat.prime` when `nat` was open), maybe they should be re-ambiguated if it lands?


{% endraw %}
