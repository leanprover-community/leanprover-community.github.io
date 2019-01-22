---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36268Triangularparentinstances.html
---

## [general](index.html)
### [Triangular parent instances](36268Triangularparentinstances.html)

#### [Nicholas Scheel (Dec 16 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864665):
Is there any way to work around this error?
```
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  steppable.to_functor t
inferred
  mergeable.to_functor f
```
(I have two classes, `steppable` and `mergeable` that both extend `functor`, and I'm using them both as assumptions for some generic code I am writing)

#### [Chris Hughes (Dec 16 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864720):
I think you more or less have to create a new class `steppable_and_mergeable`. I don't think there's another way.

#### [Nicholas Scheel (Dec 16 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864731):
Okay, that's what I figured ...

#### [Chris Hughes (Dec 16 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864777):
There is actually another way. Change the definition of `mergeable` and `steppable` to take `[functor]` as an argument instead of extending `functor`

#### [Nicholas Scheel (Dec 16 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864894):
I see; that could work, but it seems it doesn't play nicely with `out_param` then

#### [Chris Hughes (Dec 16 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151864940):
I know nothing about `out_param`

#### [Simon Hudon (Dec 16 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151888684):
What's your worry about out_param?

#### [Nicholas Scheel (Dec 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151888986):
Oh hm. I was getting this error, but also marking the instance as `out_param` seemed to fix it:
```
don't know how to synthesize placeholder
context:
t : Type u,
f : Type u → Type u,
_inst_1 : mergeable f,
_inst_2 : steppable t f,
_inst_3 : traversable f,
_inst_4 : is_lawful_functor f,
_inst_5 : is_lawful_traversable f,
a b : t
⊢ Type u → Type u
```
(i.e. it looked like it was failing to figure out what `f` was even though I gave it `t`)
`steppable` now looks like:
```
class steppable (t : Type u) (f : out_param $ Type u → Type u) [out_param $ functor f] :=
(step : t ≃ f t)
```

#### [Sebastian Ullrich (Dec 16 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular parent instances/near/151892913):
There shouldn't be any need for that instance param if it's not used in the class body

