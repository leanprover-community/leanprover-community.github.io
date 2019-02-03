---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64324buginleanimports.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [bug in lean imports](https://leanprover-community.github.io/archive/113488general/64324buginleanimports.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Dec 24 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20in%20lean%20imports/near/152471531):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I guess no one has ever tried to use 7 dots in a row in relative imports, but it doesn't work. The <code>=</code> should be a <code>+=</code> <a href="https://github.com/leanprover/lean/blob/master/src/frontends/lean/parser.cpp#L2422" target="_blank" title="https://github.com/leanprover/lean/blob/master/src/frontends/lean/parser.cpp#L2422">here</a>, and I tested that if you put <code>import .......test</code> it counts as only one level up (and in general <code>k</code> dots means <code>k mod 3</code> levels up)</p>


{% endraw %}
