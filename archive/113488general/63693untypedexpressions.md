---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63693untypedexpressions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [untyped expressions](https://leanprover-community.github.io/archive/113488general/63693untypedexpressions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Apr 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308427):
<p>When referring to local constants it's pretty annoying that I have to give the type every time. Can't I used leave the type unelaborated until the local constant is abstracted away anyway?</p>

#### [ Kenny Lau (Apr 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308443):
<p>for example?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308537):
<p><span class="user-mention" data-user-id="110789">@Jakob von Raumer</span> Sure, you can use any dummy type as long as you don't need type inference</p>

#### [ Jakob von Raumer (Apr 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308550):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> When I use them in expressions that I later on treat with <code>expr.pis</code> for example</p>

#### [ Jakob von Raumer (Apr 19 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308601):
<p>Well, so I just use `(Type)?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308733):
<p>yeah</p>


{% endraw %}
