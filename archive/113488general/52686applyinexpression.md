---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52686applyinexpression.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [apply in expression](https://leanprover-community.github.io/archive/113488general/52686applyinexpression.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Nov 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20in%20expression/near/146851453):
<p>Is there a way to <code>apply</code> in the middle of an expression? Let me explain. Assume that lemma <code>foo</code> tells me that <code>Q</code> can be deduced from <code>P</code>. Now, I have in the middle of a proof a goal of the form <code>∀x, Q x</code>, and I would like to reduce it to <code>∀x, P x</code> without introducing <code>x</code>. Just like <code>simp</code> would do instead of <code>rw</code>, but for implications instead of equivalences. Is this possible?</p>


{% endraw %}
