---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91640derivehasreflect.html
---

## Stream: [general](index.html)
### Topic: [@[derive has_reflect]](91640derivehasreflect.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090195):
<p>For long-enough structure definitions, e.g.</p>
<div class="codehilite"><pre><span></span>@[derive has_reflect]
structure config :=
(max_iterations  : ℕ := 500)
(max_discovers   : ℕ := 0)
(optimal         : bool := tt)
(exhaustive      : bool := ff)
(trace           : bool := ff)
(trace_summary   : bool := ff)
(trace_rules     : bool := ff)
(trace_discovery : bool := tt)
(explain         : bool := ff)
(explain_using_conv : bool := tt)
</pre></div>


<p>the <code>@[derive has_reflect]</code> takes multiple seconds to execute. Does anyone know why this is?</p>

#### [ Keeley Hoek (Nov 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090203):
<p>Actually, without at least some of those fields deleted, I haven't even seen it finish</p>

#### [ Keeley Hoek (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090210):
<p>ok it does, eventually!</p>

#### [ Keeley Hoek (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090213):
<p>(but why?)</p>

#### [ Scott Morrison (Nov 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090351):
<p>Turn on profiling and see if it tells you something useful?</p>

#### [ Keeley Hoek (Nov 21 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090946):
<p>turns out its the fault of <code>tactic.add_decl</code> :(</p>


{% endraw %}
