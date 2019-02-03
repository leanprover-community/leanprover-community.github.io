---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46194implicitarguments.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [implicit arguments](https://leanprover-community.github.io/archive/113488general/46194implicitarguments.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Jan 10 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824603):
<p>Is there any way to tell lean to show all the implicit arguments in an error message?<br>
For example, sometimes when rewrite fails, I would want to know if there are different implicit args that caused the rewrite to fail</p>

#### [ petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824649):
<p>Or in a type mismatch error</p>

#### [ petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824655):
<p>Sometimes it shows all the implicit arguments sometimes it doesn't</p>

#### [ Johan Commelin (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824659):
<p><code>set_option pp.all true</code> will show you everything... that might be too much though...</p>

#### [ Rob Lewis (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824660):
<p><code>set_option pp.implicit true</code> before the declaration.</p>

#### [ Johan Commelin (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824663):
<p>Aah, there you go.</p>

#### [ petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824664):
<p>Thanks</p>

#### [ Rob Lewis (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824669):
<p>There are other <code>pp</code> options that autocomplete should show you. <code>all</code> is difficult to read.</p>


{% endraw %}
