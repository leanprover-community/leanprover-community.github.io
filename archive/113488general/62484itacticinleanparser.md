---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62484itacticinleanparser.html
---

## Stream: [general](index.html)
### Topic: [itactic in lean.parser](62484itacticinleanparser.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 22 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152572):
Inside a `lean.parser` monad, I can for example read a `name` by
````
n <- ident
````
Is there any way to do the same thing with an `itactic` block? i.e. expecting a `begin ... end` or `{ ... }` block?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152614):
In the end, I'm trying to make a command which _optionally_ accepts an `itactic` block

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148162764):
Unfortunately no. `itactic` is not a parser in Lean 3 for technical reasons and can only be used directly as a parameter type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 22 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148166371):
</3 Heartbreaking but good to know, thanks Sebastian

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 22 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148167149):
And Lean 4?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 22 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148179070):
There *will* be some `itactic` parser in Lean 4 since all parsing will be done in Lean, and you should be able to reuse it to you heart's content

