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
<p>I am trying to understand the has_Inf instance of submodule defined at <a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L240" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L240">https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L240</a><br>
How does the carrier definition work?</p>

#### [ petercommand (Nov 18 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147908654):
<p>⋂ s ∈ S, ↑s</p>

#### [ petercommand (Nov 18 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147908656):
<p>I am not sure how it's desugared or how this definition works</p>

#### [ Kenny Lau (Nov 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147910431):
<p>it is <code>⋂ s, ⋂ H : s ∈ S, ↑s</code></p>

#### [ petercommand (Nov 18 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911198):
<p>H?</p>

#### [ petercommand (Nov 18 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911238):
<p>you mean <code>⋂ s, ⋂ S : s ∈ S, ↑s</code>?</p>

#### [ Kenny Lau (Nov 18 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911248):
<p>no, I mean what I typed</p>

#### [ Kenny Lau (Nov 18 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20intersection/near/147911287):
<p>also <code>⋂ s : submodule α β, ⋂ H : s ∈ S, ↑s</code></p>


{% endraw %}
