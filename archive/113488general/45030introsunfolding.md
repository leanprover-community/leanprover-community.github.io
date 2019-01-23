---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45030introsunfolding.html
---

## Stream: [general](index.html)
### Topic: [intros unfolding](45030introsunfolding.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128723966):
Is this normal?
```lean
example (P Q : Prop)  : P → Q :=
begin
intros, -- context has a: P, goal is now Q
sorry
end

def f (P Q : Prop) := P → Q

example (P Q : Prop)  : f P Q :=
begin
intros, -- nothing happen :-(
intros a, -- context is a : P, goal is now Q
sorry
end
```
It seems this prevents `finish` to work successfully in some cases without a preliminary `intros a b c d e f`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128724587):
that's kind of interesting. If you make f reducible, or unfold it explicitly, maybe `intros` works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128725099):
Of course explicit unfolding works. But reducible is not enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128725144):
you can also try `intros _`


{% endraw %}
