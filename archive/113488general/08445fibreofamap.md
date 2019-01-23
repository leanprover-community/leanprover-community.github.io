---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08445fibreofamap.html
---

## Stream: [general](index.html)
### Topic: [fibre of a map](08445fibreofamap.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139016):
I wish we have preimage of a point, whatever its use is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139300):
Why not use `f ⁻¹' {x}`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139349):
because they don't defintionally expand well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139609):
it doesn't expand any worse than `{x}` itself does. Just make a simp lemma (but actually the existing simp lemmas should compose to get what you want)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139613):
that isn't definitional expansion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139618):
I mean `{x}` doesn't expand well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139619):
so?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139622):
so I don't like it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139624):
nao gosto isso

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139666):
;P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139671):
It is conceivable that we can change the definition there but it doesn't affect whether to have a definition of fiber

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fibre%20of%20a%20map/near/125139724):
ok, let's just change the definition of singleton then


{% endraw %}
