---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63146testingtactics.html
---

## Stream: [general](index.html)
### Topic: [testing tactics](63146testingtactics.html)

---


{% raw %}
#### [ Scott Morrison (Mar 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790056):
<p>I have a <code>meta def T : expr → tactic expr := ...</code> that I've written that isn't behaving properly, and I want to do some debugging. Inside the definition there are some <code>trace</code> statements that explain to me what's going on --- I just need a convenient way to invoke my tactic. Suppose I have some other <code>def f := ...</code>, and I want to invoke <code>T</code> on <code>f</code>. What do I do?</p>

#### [ Scott Morrison (Mar 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790062):
<p>I'm hoping there's just something easy involving quotations that I don't know.</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790083):
<p>Something like <code>to_expr `(f) &gt;&gt;= T</code> should work</p>

#### [ Scott Morrison (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790135):
<p><code>term `(f) has type reflected f but is expected to have type pexpr</code></p>

#### [ Mario Carneiro (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790137):
<p>Actually, <code> `(f)</code> is already an <code>expr</code>, so <code>T `(f)</code> should work</p>

#### [ Scott Morrison (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790146):
<p><code> to_expr ``(f)</code> works, however</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790148):
<p>You would use <code>to_expr</code> if you need to parse the expression at run time rather than parse time</p>

#### [ Scott Morrison (Mar 16 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790199):
<p>thanks!</p>


{% endraw %}
