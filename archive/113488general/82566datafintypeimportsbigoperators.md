---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82566datafintypeimportsbigoperators.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [data.fintype imports big_operators](https://leanprover-community.github.io/archive/113488general/82566datafintypeimportsbigoperators.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 02 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data.fintype%20imports%20big_operators/near/135034142):
<p>Is this good? I would assume that <code>data/fintype.lean</code> is pretty basic. Is it ok that this imports <code>algebra.big_operators</code>?</p>

#### [ Johannes Hölzl (Oct 02 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data.fintype%20imports%20big_operators/near/135036126):
<p>I think we should move the content of <code>big_operators</code> to <code>finset</code> anyway. The big operators on lists are in <code>data/list/...</code> and the one for <code>multiset</code> are in <code>data/multiset.lean</code></p>


{% endraw %}
