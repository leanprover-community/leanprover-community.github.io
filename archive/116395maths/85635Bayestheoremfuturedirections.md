---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85635Bayestheoremfuturedirections.html
---

## Stream: [maths](index.html)
### Topic: [Bayes theorem + future directions](85635Bayestheoremfuturedirections.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Koundinya Vajjha (Dec 21 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Bayes%20theorem%20%2B%20future%20directions/near/152309690):
hello,

I have just completed a formalization of Bayes theorem building on top of the measure theory library. this was my first formalization effort so it is a bit rough around the edges and needs cleaning up.  https://github.com/kodyvajjha/mathlib/commit/54639f16ec9e6a646fe43d870131a6099e8a550c

i had set this target as a first milestone in formalizing the (G)ARCH time series models, and I wanted to ask the community if they had any tips/suggestions on getting there. as i understand it - matrices aren't yet formalized, are there any plans on getting to matrices in the near future?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 21 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Bayes%20theorem%20%2B%20future%20directions/near/152309951):
Matrices are in `ring_theory/matrix`

