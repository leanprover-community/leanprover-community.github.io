---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/12456decidability.html
---

## Stream: [new members](index.html)
### Topic: [decidability](12456decidability.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 12 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521031):
<p>How can you ask lean to decide something which is decidable? e.g. <code>prime n</code></p>

#### [ Kevin Buzzard (Nov 12 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521350):
<p><code>dec_trivial</code> will do it in theory, but for primes it might well time out in practice and you're better off using <code>norm_num</code></p>

#### [ Keeley Hoek (Nov 12 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521438):
<p>ok thanks Kevin</p>


{% endraw %}
