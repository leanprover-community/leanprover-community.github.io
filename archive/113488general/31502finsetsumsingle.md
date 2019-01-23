---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31502finsetsumsingle.html
---

## Stream: [general](index.html)
### Topic: [finset.sum_single](31502finsetsumsingle.html)

---

#### [Morenikeji Neri (Jul 26 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum_single/near/130363587):
I'm wondering if there is a proof for
theorem finset.sum_single {α : Type}[fintype α ] {β : Type} [add_comm_monoid β] (f: α → β) {i: α} (h: ∀ (j:α), i ≠ j → f(j)=0 ): 
f i = finset.sum finset.univ (λ (K: α),f K) := sorry
on mathlib?

#### [Kevin Buzzard (Jul 26 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum_single/near/130363659):
rofl -- Keji did you just get internet? :-) Kenny proved this for you about 5 hours ago :-) The proof is in your email inbox :-)

#### [Patrick Massot (Jul 26 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum_single/near/130363721):
You could also try to take up my dormant project https://github.com/PatrickMassot/bigop

#### [Morenikeji Neri (Jul 26 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum_single/near/130363726):
Haha, yeah I did. I guess it waited to be sent when I wasn't connected . Thanks Kenny!

