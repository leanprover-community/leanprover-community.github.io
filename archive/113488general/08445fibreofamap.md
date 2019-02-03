---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08445fibreofamap.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [fibre of a map](https://leanprover-community.github.io/archive/113488general/08445fibreofamap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 16 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139016):
<p>I wish we have preimage of a point, whatever its use is</p>

#### [ Mario Carneiro (Apr 16 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139300):
<p>Why not use <code>f ⁻¹' {x}</code>?</p>

#### [ Kenny Lau (Apr 16 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139349):
<p>because they don't defintionally expand well</p>

#### [ Mario Carneiro (Apr 16 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139609):
<p>it doesn't expand any worse than <code>{x}</code> itself does. Just make a simp lemma (but actually the existing simp lemmas should compose to get what you want)</p>

#### [ Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139613):
<p>that isn't definitional expansion</p>

#### [ Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139618):
<p>I mean <code>{x}</code> doesn't expand well</p>

#### [ Mario Carneiro (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139619):
<p>so?</p>

#### [ Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139622):
<p>so I don't like it</p>

#### [ Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139624):
<p>nao gosto isso</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139666):
<p>;P</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139671):
<p>It is conceivable that we can change the definition there but it doesn't affect whether to have a definition of fiber</p>

#### [ Kenny Lau (Apr 16 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139724):
<p>ok, let's just change the definition of singleton then</p>


{% endraw %}
