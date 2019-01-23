---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35032Whathappenednext.html
---

## Stream: [general](index.html)
### Topic: [What happened next?](35032Whathappenednext.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124638598):
```
example (d : ℕ) (H : 1  =  2  * nat.succ d) : 1  =  2  * d +  2  :=
begin
rw H,
-- goal now?
admit,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124638609):
Took me slightly by surprise at the time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124639398):
heh, I assume `2` got rewritten?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640156):
That was part of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640252):
The other phenomenon shows itself here:
```lean
example (x y : ℕ) (H : 1 = x) : 2 = y :=
begin
rw H,
-- goal now?
admit,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640326):
Oh I have just realised what is going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640331):
So the goal becomes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640335):
` bit0 x = y `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640345):
but that's because `2` isn't defined to be `succ 1` here, it's defined to be `bit0 1`

