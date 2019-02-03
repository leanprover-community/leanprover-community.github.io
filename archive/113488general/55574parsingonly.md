---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55574parsingonly.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [`parsing_only`](https://leanprover-community.github.io/archive/113488general/55574parsingonly.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Nov 10 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60parsing_only%60/near/147438292):
<p>What does the <code>parsing_only</code> attribute, as in</p>
<div class="codehilite"><pre><span></span>notation [parsing_only] `command`:max := tactic unit
</pre></div>


<p>do?</p>

#### [ Sebastian Ullrich (Nov 10 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60parsing_only%60/near/147438358):
<p>It makes the pretty printer ignore that notation</p>


{% endraw %}
