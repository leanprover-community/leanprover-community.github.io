---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93477computablefunctionType2Type1.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [computable function Type 2 -> Type 1](https://leanprover-community.github.io/archive/113488general/93477computablefunctionType2Type1.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 31 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632607):
<p>is there any computable non-constant function Type 2 -&gt; Type 1?</p>

#### [ Chris Hughes (Jul 31 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632741):
<p><code>def f : Type 2 → Type := λ α , plift (nonempty α)</code></p>

#### [ Kenny Lau (Jul 31 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632762):
<p>nice</p>

#### [ Gabriel Ebner (Jul 31 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632821):
<p><code>Type</code> != <code>Type 1</code>.  You need one more <code>plift</code>.</p>


{% endraw %}
