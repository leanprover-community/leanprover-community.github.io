---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89951circumflexnotation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [circumflex notation](https://leanprover-community.github.io/archive/113488general/89951circumflexnotation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Miko de Amsterdamo (Apr 12 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/circumflex%20notation/near/124981819):
<p>What does this notation do? (hat/circumflex) I'm looking at an example in <a href="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html" target="_blank" title="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html">https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html</a> and I found it in "(assume ha, h^.left ha)"</p>

#### [ Simon Hudon (Apr 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/circumflex%20notation/near/124982270):
<p>That's old notation. It was for field projection. Now it's only <code>.</code></p>

#### [ Miko de Amsterdamo (Apr 12 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/circumflex%20notation/near/124982310):
<p>So the token <code>^.</code> has been replaced by just <code>.</code> ?</p>

#### [ Simon Hudon (Apr 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/circumflex%20notation/near/124983725):
<p>That's correct. So <code>.</code> has the double duty of qualifying names with name spaces and resolving projections.</p>

#### [ Miko de Amsterdamo (Apr 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/circumflex%20notation/near/124983730):
<p>Thanks!</p>


{% endraw %}
