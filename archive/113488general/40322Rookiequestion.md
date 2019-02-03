---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40322Rookiequestion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Rookie question](https://leanprover-community.github.io/archive/113488general/40322Rookiequestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Frank Mobler (May 22 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie%20question/near/126907865):
<p>I'm stumped proving <code>example {V : Type}{n : V} : n ∈ ({n} : set V)</code>. Please without tactics first. I want to see how to construct proof terms explicitly for types like this.</p>

#### [ Mario Carneiro (May 22 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie%20question/near/126908079):
<p><code>or.inl rfl</code> is a proof term for that</p>

#### [ Mario Carneiro (May 22 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie%20question/near/126908090):
<p>because the goal is defeq to <code>n = n \/ false</code>:</p>
<div class="codehilite"><pre><span></span>example {V : Type} {n : V} : n ∈ ({n} : set V) :=
show n = n ∨ false, from or.inl rfl
</pre></div>

#### [ Frank Mobler (May 22 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rookie%20question/near/126908144):
<p>Aha. This helps a lot. Light bulbs going on. Thanks.</p>


{% endraw %}
