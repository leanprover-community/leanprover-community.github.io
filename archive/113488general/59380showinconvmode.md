---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59380showinconvmode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [show in conv mode](https://leanprover-community.github.io/archive/113488general/59380showinconvmode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 10 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20in%20conv%20mode/near/123540735):
<p>I have some goal of the form <code>X = Y</code> where <code>Y</code> is one of these annoying terms that I can't cut and paste from pretty printer output (in this case, I believe, because it has replaced a proof with <code>_</code>). I want to use <code>show</code> to rewrite <code>X</code> as <code>X'</code> but I can't write <code>show X'=Y</code> because my problems with Y. I could prove <code>X=X'</code> using rfl and then use a rewrite. But it would be cool to use conv mode, use <code>to_lhs</code> to restrict to <code>X</code> and then use some conv version of show to replace <code>X</code> with <code>X'</code>. Can this be done?</p>


{% endraw %}
