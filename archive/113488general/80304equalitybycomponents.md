---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80304equalitybycomponents.html
---

## Stream: [general](index.html)
### Topic: [equality by components](80304equalitybycomponents.html)

---

#### [Reid Barton (Feb 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20by%20components/near/123047697):
If my goal is of the form `⟨x, y⟩ = ⟨x', y'⟩`, is there a tactic that will replace it with two new goals `x = x'` and `y = y'`?

#### [Reid Barton (Feb 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20by%20components/near/123047767):
oh, `congr` did it.

#### [Reid Barton (Feb 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20by%20components/near/123048566):
I'm also wondering how I could do this when the left and/or right hand side is not already a constructor application, and I want to eta expand first. (But in my actual case the right hand side was just a variable, and I could use `induction`.)

#### [Mario Carneiro (Feb 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20by%20components/near/123051739):
Lean doesn't have definitional eta for products fyi

