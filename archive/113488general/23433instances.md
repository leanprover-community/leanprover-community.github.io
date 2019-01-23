---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23433instances.html
---

## Stream: [general](index.html)
### Topic: [instances](23433instances.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Oct 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136163177):
Can someone explain this?
```lean
failed to synthesize type class instance for
TL : Type u,
[...]
_inst_9 : is_contr TL,
[...]
⊢ is_contr TL
```
Even if I set `pp.all true`, it shows that TL is the right thing and there's no hidden difference...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 20 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164270):
Did you try using `letI` to add the instance to the type class inference system? I appreciate that its name indicates that it should be in it already..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Oct 20 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164360):
The environment looks like this:
```lean
@[hott] def pushout_of_embedding {n : ℕ₋₂} [is_embedding g] :
  Π [is_trunc n TL] [is_trunc n TR] [is_trunc n BL],
  is_trunc n (pushout f g) :=
begin
  induction n with n IH,
  { intros, apply base_case,  }
end
```
So it's mentioned after the `:`, maybe that's what prevents it from being a local instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164637):
Yes that's exactly it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164639):
You need to explicitly add it to the instance list with `letI`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164640):
Okay, thanks :+1:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 20 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164675):
Leo changed this behaviour a few months ago. Nothing right of the colon goes in any more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136167263):
you should use `resetI` there instead of `letI`


{% endraw %}
