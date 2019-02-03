---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99873falseelim.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [false.elim](https://leanprover-community.github.io/archive/113488general/99873falseelim.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/false.elim/near/133574791):
<p>Why can <code>false</code> elim to anything even though it is only a <code>Prop</code>?</p>

#### [ Chris Hughes (Sep 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/false.elim/near/133574907):
<p>More or less because even if it wasn't a Prop it would still be a subsingleton. Same reason for <code>and</code> <code>eq</code> and <code>acc</code>. I think more precisely any constructors whose type is not a <code>Prop</code> have to be mentioned in the type of the <code>Prop</code>. So <code>acc</code> is okay, because it's non-Prop constructor is mentioned in the type.</p>


{% endraw %}
