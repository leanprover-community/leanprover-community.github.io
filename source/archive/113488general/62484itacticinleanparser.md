---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62484itacticinleanparser.html
---

## [general](index.html)
### [itactic in lean.parser](62484itacticinleanparser.html)

#### [Keeley Hoek (Nov 22 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152572):
Inside a `lean.parser` monad, I can for example read a `name` by
````
n <- ident
````
Is there any way to do the same thing with an `itactic` block? i.e. expecting a `begin ... end` or `{ ... }` block?

#### [Keeley Hoek (Nov 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152614):
In the end, I'm trying to make a command which _optionally_ accepts an `itactic` block

#### [Sebastian Ullrich (Nov 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148162764):
Unfortunately no. `itactic` is not a parser in Lean 3 for technical reasons and can only be used directly as a parameter type.

#### [Keeley Hoek (Nov 22 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148166371):
</3 Heartbreaking but good to know, thanks Sebastian

#### [Kevin Buzzard (Nov 22 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148167149):
And Lean 4?

#### [Sebastian Ullrich (Nov 22 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148179070):
There *will* be some `itactic` parser in Lean 4 since all parsing will be done in Lean, and you should be able to reuse it to you heart's content

