---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88782declaringstructures.html
---

## Stream: [general](index.html)
### Topic: [declaring structures](88782declaringstructures.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 10 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537345):
Can I declare structures in the meta lang?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 10 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537873):
`meta structure`? :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 10 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123537878):
I guess you want to create one from a tactic. There's no such API yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 11 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566179):
How about for `inductive`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 11 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566327):
See https://groups.google.com/d/msg/lean-user/nmNlRiqogys/DKj97GkxAwAJ

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 11 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123566887):
But that doesn't mean that using `environment.add_inductive` will render the type completely useless, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 11 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaring%20structures/near/123568493):
It's useless to end users, but not useless to other meta programs like the coinductive predicates


{% endraw %}
