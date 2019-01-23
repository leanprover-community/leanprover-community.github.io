---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75812setintersection.html
---

## Stream: [general](index.html)
### Topic: [set intersection](75812setintersection.html)

---


{% raw %}
#### [ petercommand (Nov 18 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147908613):
I am trying to understand the has_Inf instance of submodule defined at https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L240
How does the carrier definition work?

#### [ petercommand (Nov 18 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147908654):
⋂ s ∈ S, ↑s

#### [ petercommand (Nov 18 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147908656):
I am not sure how it's desugared or how this definition works

#### [ Kenny Lau (Nov 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147910431):
it is `⋂ s, ⋂ H : s ∈ S, ↑s`

#### [ petercommand (Nov 18 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911198):
H?

#### [ petercommand (Nov 18 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911238):
you mean ```⋂ s, ⋂ S : s ∈ S, ↑s```?

#### [ Kenny Lau (Nov 18 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911248):
no, I mean what I typed

#### [ Kenny Lau (Nov 18 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911287):
also `⋂ s : submodule α β, ⋂ H : s ∈ S, ↑s`


{% endraw %}
