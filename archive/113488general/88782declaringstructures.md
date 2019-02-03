---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88782declaringstructures.html
---

## Stream: [general](index.html)
### Topic: [declaring structures](88782declaringstructures.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 10 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537345):
<p>Can I declare structures in the meta lang?</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537873):
<p><code>meta structure</code>? :)</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537878):
<p>I guess you want to create one from a tactic. There's no such API yet.</p>

#### [ Jakob von Raumer (Mar 11 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566179):
<p>How about for <code>inductive</code>?</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566327):
<p>See <a href="https://groups.google.com/d/msg/lean-user/nmNlRiqogys/DKj97GkxAwAJ" target="_blank" title="https://groups.google.com/d/msg/lean-user/nmNlRiqogys/DKj97GkxAwAJ">https://groups.google.com/d/msg/lean-user/nmNlRiqogys/DKj97GkxAwAJ</a></p>

#### [ Jakob von Raumer (Mar 11 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566887):
<p>But that doesn't mean that using <code>environment.add_inductive</code> will render the type completely useless, right?</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123568493):
<p>It's useless to end users, but not useless to other meta programs like the coinductive predicates</p>


{% endraw %}
