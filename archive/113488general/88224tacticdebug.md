---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88224tacticdebug.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic debug](https://leanprover-community.github.io/archive/113488general/88224tacticdebug.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 31 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20debug/near/127382538):
<p>Is there anything like a Lean debugger which would allow me to execute tactics line by line and inspect the values of variables? Or should I add trace commands after every lines in Simon's tactics to hope to understand how they work?</p>

#### [ Gabriel Ebner (Jun 01 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20debug/near/127402959):
<p>There is a debugger, but I don't think anybody here uses it (or even knows how to use it).  You need to run it from the command-line.  Example: <a href="https://github.com/leanprover/presentations/blob/master/20170116_POPL/debug/has_to_string_break.lean" target="_blank" title="https://github.com/leanprover/presentations/blob/master/20170116_POPL/debug/has_to_string_break.lean">https://github.com/leanprover/presentations/blob/master/20170116_POPL/debug/has_to_string_break.lean</a>  I'd stick to trace messages.</p>

#### [ Patrick Massot (Jun 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20debug/near/127403142):
<p>Thanks!</p>


{% endraw %}
