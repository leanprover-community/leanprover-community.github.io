---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52425noobresusevariablenamequestion.html
---

## Stream: [general](index.html)
### Topic: [noob "resuse variable name" question](52425noobresusevariablenamequestion.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048259):
<p>Dammit I can never remember how to go from <code>H : P</code> and <code>HPQ : P -&gt; Q</code> to <code>H : Q</code> in tactic mode, the point being that I want to throw the original <code>H</code> away and reuse the name. There's a tactic that does this but I can never remember the name and I can't come up with an algorithm to find out for myself, my searches have been futile, so sorry, I have to ask.</p>

#### [ Chris Hughes (Sep 16 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048665):
<p><code>specialize</code> or <code>replace</code></p>

#### [ Kevin Buzzard (Sep 16 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048907):
<p><code>replace</code> -- that was it. I knew it was something like <code>rewrite</code>. Thanks.</p>


{% endraw %}
