---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75475quotind.html
---

## [general](index.html)
### [quot.ind](75475quotind.html)

#### [Kevin Buzzard (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130704193):
Am I right in thinking that `quot.ind` is logically equivalent to `function.surjective (quot.mk r)`? It's simply the universal property of a surjection. I am never 100% sure about these things because of computability or constructability or efficiency or whatever, but, assuming I've not made a slip, why do the CS guys choose `quot.ind` over the surjection statement? If beta were allowed to take values in Type then there would be some constructivity issues I guess, but because it's Prop aren't they exactly the same? Is it simply that `quot.ind` turns out to be more useful than the surjectivity statement in practice or is there something else going on?

#### [Kenny Lau (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130704204):
because `function.surjective` hasn't been defined

#### [Kenny Lau (Aug 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130704255):
the four constants of `quot` are all initiated in core

#### [Mario Carneiro (Aug 01 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130704349):
Yes, `quot.ind` and `quot.exists_rep` are equivalent. Induction principles are preferred for axiomatics since they don't have any prerequisite definitions

#### [Kevin Buzzard (Aug 01 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130705226):
I guess one could have simply spelled out the definition of surjection. I don't quite understand Mario's answer -- what is an "induction principle"? I only ever learnt one and that was about the natural numbers. Aah. Presumably in this context it means "something which constructs a map from the type we're talking about to Prop". OK. I see. Thanks!

#### [Mario Carneiro (Aug 01 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130705358):
"induction principle" is often used synonymously with "recursor" in lean terminology

#### [Mario Carneiro (Aug 01 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind/near/130705365):
Usually an induction principle has a motive that has a target in `Prop` though

