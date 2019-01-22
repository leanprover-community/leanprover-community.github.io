---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24698autoderivinginstances.html
---

## [general](index.html)
### [auto deriving instances](24698autoderivinginstances.html)

#### [Zesen Qian (Jun 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688095):
Is there a quick way to derive instances for type definitions like `def boolean : Type := bool`?

#### [Kenny Lau (Jun 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688100):
don't use them :)

#### [Zesen Qian (Jun 07 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688156):
I feel type synonym is useful in development.

#### [Kenny Lau (Jun 07 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688161):
pretty sure you can't find it anywhere in mathlib

#### [Simon Hudon (Jun 07 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688204):
If you mark your definition as reducible, I think, the instances will simply be inherited

#### [Simon Hudon (Jun 07 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688215):
Otherwise, you can do 

```lean
instance : my_class some_synonym :=
by dsimp [some_synonym] ; apply_instance
```

#### [Zesen Qian (Jun 07 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688285):
@**Simon Hudon** very nice, sir.

