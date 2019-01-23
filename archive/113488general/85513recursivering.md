---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85513recursivering.html
---

## Stream: [general](index.html)
### Topic: [recursive ring](85513recursivering.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127272896):
Is that a bug?
```lean
import tactic.ring

example (a b x y : ℤ) :  -x*y*(a+b)^2 + y*(x+y)*a^2 + x*(x+y)*b^2 - (a*y-b*x)^2 = 0:=
begin
  ring,
  ring,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273575):
so `ring` is not idempotent ^^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273638):
`ring` has a bug in it currently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273640):
I think there's an issue for it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273728):
The example in the issue actually works here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273791):
It's because when `ring` fails, it tries to rewrite the expression into a "nice" SOP form, and this rewriting causes it to circumvent the bug the second time around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273899):
`begin ring, ring, ring, ring, ring, ring, ring, banana_phone end`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127274422):
I really mean: I copy and paste the example in the github issue and it works here


{% endraw %}
