---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/81181BNFforlean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [BNF for lean?](https://leanprover-community.github.io/archive/113489newmembers/81181BNFforlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Francis Nixon (Jan 27 2019 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/BNF%20for%20lean%3F/near/156970536):
<p>I was wondering there was a full BNF for lean somewhere. I noticed this: <a href="https://leanprover.github.io/reference/lexical_structure.html" target="_blank" title="https://leanprover.github.io/reference/lexical_structure.html">https://leanprover.github.io/reference/lexical_structure.html</a>, but I seem to be unable to find a full grammar. Thank.</p>

#### [ Mario Carneiro (Jan 27 2019 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/BNF%20for%20lean%3F/near/156971899):
<p>The lean grammar isn't quite context free, at least in the expression part</p>

#### [ Mario Carneiro (Jan 27 2019 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/BNF%20for%20lean%3F/near/156971948):
<p>or rather, it's context free but the grammar can change depending on the commands that are read, and there are hooks for arbitrary computation in the parser</p>

#### [ Mario Carneiro (Jan 27 2019 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/BNF%20for%20lean%3F/near/156971950):
<p>But if you ignore all that you should be able to get a decent BNF</p>


{% endraw %}
