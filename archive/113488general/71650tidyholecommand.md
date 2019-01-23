---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71650tidyholecommand.html
---

## Stream: [general](index.html)
### Topic: [tidy hole command](71650tidyholecommand.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133272160):
@**Scott Morrison** The tidy hole command is really marvellous. Here are some trivialities that might give epsilon improvement:
(1) If `tidy` generates the proof `begin refl end`, generate `rfl` instead.
(2) If `tidy` generates the proof `begin exact foo end`, generate `foo` instead.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276810):
@**Johan Commelin**, the first is impossible, or rather useless: Lean actually decides _in the parser_ whether you not you proved by `rfl`, rather than inspecting the proof term!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276820):
But (2) will go on my todo list. (i.e. I'll leave your message starred :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276825):
No, I mean that you inspect the string you are about to return.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276866):
The hole command returns some string, and VScode substitutes that for the hole. Is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276869):
Ah, okay. Absolutely, I can do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276870):
If that string is exactly `begin refl end`, then you might as well output `rfl` instead.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276875):
by induction convert tactic proofs to term proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276879):
I can also have "begin just_one_tactic end" into "by just_one_tactic".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276880):
I think `refl` tries slightly harder than `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276882):
That's somewhere on the VScode extension wishlist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276940):
```quote
I think `refl` tries slightly harder than `rfl`
```
Hmmm... that might be true. So maybe we need to slightly patch tidy, to first try `exact rfl`. Then (1) will be a special case of (2).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276948):
Anyway, this is not high priority stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 03 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277149):
`refl` works for any reflexive relation I think. `rfl` is just equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277163):
I think it also does more definitional reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 03 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277646):
Can you give an example? If I prove something with `by refl`, the proof term is just `eq.refl _` which is `rfl`


{% endraw %}
