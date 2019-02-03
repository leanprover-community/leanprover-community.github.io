---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74858warnings.html
---

## Stream: [general](index.html)
### Topic: [warnings](74858warnings.html)

---


{% raw %}
#### [ Reid Barton (Dec 27 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612059):
<p>There isn't any way to suppress all warnings or specific warnings from lean, is there?</p>

#### [ Johan Commelin (Dec 27 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612571):
<p>In the editor? Or in compiler output in the terminal?</p>

#### [ Reid Barton (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612608):
<p>In the terminal</p>

#### [ Reid Barton (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612612):
<p>preferably, from the command line</p>

#### [ Johan Commelin (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612613):
<p>You could just pipe via grep...</p>

#### [ Johan Commelin (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612615):
<p>Completely customisable, but maybe not exactly user friendly</p>

#### [ Johan Commelin (Dec 27 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612626):
<p>What kind of filtering are you looking for?</p>

#### [ Reid Barton (Dec 27 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612765):
<p>Often I want to suppress the many "warning: imported file uses sorry" messages, and sometimes I want to ignore the messages about using sorry as well</p>

#### [ Johan Commelin (Dec 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152613016):
<p>That seems like something that <code>grep</code> could do for you.</p>


{% endraw %}
