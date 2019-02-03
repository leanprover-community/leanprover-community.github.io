---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55645nattostring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [nat to string?](https://leanprover-community.github.io/archive/113488general/55645nattostring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 10 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861127):
<p>How to I get a string from a nat?</p>

#### [ Simon Hudon (Apr 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861272):
<p><code>to_string</code></p>

#### [ Scott Morrison (Apr 10 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861290):
<div class="codehilite"><pre><span></span>invalid field notation, &#39;to_string&#39; is not a valid &quot;field&quot; because environment does not contain &#39;nat.to_string&#39;
  k
which has type
  ℕ
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861356):
<p>try <code>to_string k</code>. It's part of the <code>has_to_string</code> class so it won't support field notation</p>

#### [ Scott Morrison (Apr 10 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861359):
<p>thank you!</p>


{% endraw %}
