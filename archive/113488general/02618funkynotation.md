---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02618funkynotation.html
---

## [general](index.html)
### [funky notation](02618funkynotation.html)

#### [Johan Commelin (Oct 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135168245):
Is this doomed to fail?
```lean
def is_ideal_adic (J : set A) [is_ideal J] : Prop :=
∀ n, is_open (pow_ideal J n) ∧ (∀ K : set A, (0 : A) ∈ K → is_open K → ∃ n, pow_ideal J n ⊆ K)

notation : `is_`J`_adic` := is_ideal_adic J
```

#### [Johannes Hölzl (Oct 04 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135168274):
its doomed

#### [Johan Commelin (Oct 04 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135168386):
That's too bad

#### [Mario Carneiro (Oct 04 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135193028):
they are just funny looking brackets...

#### [Johan Commelin (Oct 04 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135193856):
Still it doesn't work )-;

#### [Reid Barton (Oct 04 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135194568):
Shouldn't have the colon after `notation`

#### [Johan Commelin (Oct 04 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky notation/near/135194768):
Thanks @**Reid Barton** it works!
```lean
notation `is-`J`-adic` := is_ideal_adic J

def is_adic (A₀ : set A) [is_subring A₀] : Prop := ∃ (J : set A₀) [hJ : is_ideal J],
(by haveI := topological_subring A₀; haveI := hJ; exact is-J-adic)
```
You can't use underscores, or you'll need to leave spaces...

