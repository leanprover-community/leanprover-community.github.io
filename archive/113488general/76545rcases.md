---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76545rcases.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rcases?](https://leanprover-community.github.io/archive/113488general/76545rcases.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Sep 07 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%3F/near/133502924):
<p>Is there a way to use <code>rcases</code> with <code>?</code> to get hints, or just <code>rintros</code>?</p>

#### [ Reid Barton (Sep 07 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%3F/near/133503552):
<p>Wait, how do I use <code>rintros?</code> again? It's telling me "unexpected token".</p>

#### [ Kevin Buzzard (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%3F/near/133505329):
<p><code>rintros</code> works for me. Is it in <code>tactic.interactive</code>? Looks like it. Note also <code>meta def rintros := rintro</code> ;-)</p>

#### [ Kenny Lau (Sep 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%3F/near/133508220):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> note the question mark in <code>rintros?</code></p>

#### [ Johan Commelin (Sep 07 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%3F/near/133508629):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> You missed a chance to formulate that as a question.</p>


{% endraw %}
