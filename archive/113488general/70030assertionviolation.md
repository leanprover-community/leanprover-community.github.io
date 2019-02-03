---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70030assertionviolation.html
---

## Stream: [general](index.html)
### Topic: [assertion violation](70030assertionviolation.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/124242811):
<p>Kenny found an assertion violation back in Feb or so: <code>instance foo (α : Type) : group α := { mul_assoc := λ x y z, rfl }</code>. I just mention it here because it still seems to be there.</p>

#### [ Kevin Buzzard (Mar 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/124242814):
<p>Should I file an issue?</p>

#### [ Patrick Massot (May 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126993921):
<p>An old friend is back:</p>
<div class="codehilite"><pre><span></span>m_ctx.match(e, *val2)
LEAN ASSERTION VIOLATION
File: /home/travis/build/leanprover/lean/src/frontends/lean/elaborator.cpp
Line: 3167
</pre></div>

#### [ Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994421):
<p>did you catch it?</p>

#### [ Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994467):
<p>It's always line 3167</p>

#### [ Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994468):
<p>they should fix that line</p>

#### [ Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994470):
<p>maybe remove the assertion</p>

#### [ Patrick Massot (May 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994558):
<p>I don't think this qualifies as serious enough for a Lean 3.X fix</p>

#### [ Kevin Buzzard (May 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994564):
<p>Can you reproduce it?</p>

#### [ Patrick Massot (May 23 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994657):
<p>Right now it happens every time I touch anything in my norms.lean</p>


{% endraw %}
