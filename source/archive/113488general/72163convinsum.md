---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72163convinsum.html
---

## [general](index.html)
### [conv in sum](72163convinsum.html)

#### [Morenikeji Neri (Aug 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130723162):
I would like to show
```lean
finset.sum finset.univ  (λ (μ : S n), e (ρ.to_fun) * e (μ.to_fun) * finset.prod finset.univ (λ (i : fin n), A (μ.to_fun i) i)) = finset.sum finset.univ
      (λ (μ : S n), e (ρ.to_fun) * (e (μ.to_fun) * finset.prod finset.univ (λ (i : fin n), A (μ.to_fun i) i))) 
```
where multiplication is in a comm_ring hence is associative, however I cannot use conv as it cannot synthesis μ.to_fun as it is a function. Any tips?

#### [Morenikeji Neri (Aug 01 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130725250):
all sorted

#### [Simon Hudon (Aug 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130725742):
I recommend you make a minimal working example so that people can have a look inside of a Lean session. 

I think `congr' 1, ext, rw mul_assoc` could help.

