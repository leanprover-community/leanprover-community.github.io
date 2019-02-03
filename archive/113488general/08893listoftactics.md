---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08893listoftactics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [list of tactics](https://leanprover-community.github.io/archive/113488general/08893listoftactics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Mar 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967762):
<p>Is there a tactic that allows me to give a list of tactics where each one solves one goal?</p>

#### [ Simon Hudon (Mar 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967842):
<p>Yes try this: <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L845-L847" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L845-L847">https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L845-L847</a></p>

#### [ Mario Carneiro (Mar 20 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967976):
<p>The interactive way to write this is <code>tac; [tac1, tac2, tac3]</code></p>

#### [ Simon Hudon (Mar 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123968190):
<p>I should really stop assuming people are scripting when answering <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>


{% endraw %}
