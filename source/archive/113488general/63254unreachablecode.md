---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63254unreachablecode.html
---

## [general](index.html)
### [unreachable code](63254unreachablecode.html)

#### [Kenny Lau (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491054):
sometimes `_` causes "unreachable code" error. it is quite clear that they won't fix it, so I'm not here to "feed the fed horse". Rather, I think I've found a temporary fix by just replacing `_` with `by skip` or any tactic mode thing at all

#### [Mario Carneiro (Dec 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491085):
That's a bit vague. Do you have an example?

#### [Kenny Lau (Dec 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491158):
```lean
instance : group (ℕ × ℕ) :=
{ mul := λ _ _, (_, _) }
```

#### [Mario Carneiro (Dec 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491168):
@**Sebastian Ullrich** known bug?

#### [Sebastian Ullrich (Dec 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151509950):
Probably not. Probably not worth fixing, either?

#### [Sebastian Ullrich (Dec 12 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151510002):
To be honest, the Lean 4 error messages are so bad right now that I don't see any problem at all with this :laughing:

#### [Simon Hudon (Dec 12 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151532124):
Oh dear!

