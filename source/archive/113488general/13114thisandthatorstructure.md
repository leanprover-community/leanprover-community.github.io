---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13114thisandthatorstructure.html
---

## [general](index.html)
### [this and that, or structure?](13114thisandthatorstructure.html)

#### [Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377318):
I notice that in our schemes work, Kenny and I independently defined the concept of an open immersion between topological spaces.

#### [Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377327):
I wrote

#### [Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377411):
```lean
structure open_immersion
  {α : Type*} [Tα : topological_space α]
  {β : Type*} [Tβ : topological_space β]
  (f : α → β) : Prop :=
(fcont : continuous f)
(finj : function.injective f)
(fopens : ∀ U : set α, is_open U ↔ is_open (f '' U))
```

#### [Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377452):
Kenny wrote

#### [Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377475):
```lean
def topological_space.open_immersion {X Y : Type} [tX : topological_space X] [tY : topological_space Y] (φ : X → Y) := 
  continuous φ ∧ 
  function.injective φ ∧ 
  ∀ U : set X, tX.is_open U → tY.is_open (set.image φ U)
```

#### [Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377929):
I don't think it would be too taxing to check that these two props were equivalent.

#### [Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378082):
But I think there's an argument for putting this basic notion into mathlib

#### [Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378100):
and before I wrote the PR

#### [Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378262):
I realised I was going to have to understand better

#### [Kevin Buzzard (Apr 20 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378523):
about the relative advantages / disadvantages between chaining "and" vs making a structure

#### [Kenny Lau (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379302):
https://github.com/kbuzzard/lean-stacks-project/commit/a3e4acc5b443f02c1decf3db32260ff28e4dd855#diff-ad019596efa140984bbb88e365b57df7

#### [Kevin Buzzard (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379303):
They're both props, the structure version has the feature that it demands that you spell out which term is doing which of the three jobs that need doing, which may or may not be a good thing, and the "and" approach lets you write more compact code, constructing instances with pointy brackets, which may or may not be a good thing

#### [Kenny Lau (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379310):
you wrote both definitions

#### [Mario Carneiro (Apr 20 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379590):
You can use pointy brackets with either definition

#### [Kevin Buzzard (Apr 20 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379698):
You're right Kenny, thanks.

#### [Mario Carneiro (Apr 20 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379812):
All structure instances, in fact, can be written with pointy brackets instead of structure notation

#### [Mario Carneiro (Apr 20 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380086):
it's just that this is harder to read when there are many properties since order matters

#### [Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380341):
Were you to be getting a mathlib PR with a definition of an open immersion

#### [Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380367):
which would you prefer?

#### [Mario Carneiro (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380414):
the structure, I think

#### [Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380548):
OK thanks

#### [Kevin Buzzard (Apr 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125381058):
Sorry Kenny, I could see that you had done the hard work in that tag (supplying the proof of the result below) so just assumed you'd written the definition.

#### [Patrick Massot (Apr 20 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382019):
```quote
you wrote both definitions
```
Ooohh, I never realized Kenny is only one schizophrenic identity of Kevin. That explains soo much...

#### [Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382178):
Our secret is out Kenny! Or should I say, Mr Hyde...

#### [Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382277):
In fact the far more mundane truth is that I write code, forget, and then write code again.

#### [Kenny Lau (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382278):
right, I'm the constructivist version of Kevin

#### [Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382304):
ha ha

#### [Patrick Massot (Apr 20 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125383630):
Yeah, the story of a first year working in scheme theory was sort of believable, but the constructivism stuff I should have realize this was completely impossible

#### [Gabriel Ebner (Apr 20 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125384461):
```quote
You can use pointy brackets with either definition
```
OTOH, curly braces work much more nicely with the structure.  That is, you can write `{fcont := _, finj := _, fopens := _}`.  While with `∧`, you'd need `{left := _, right := {left := _, right := _}}`.

#### [Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125391137):
so `\and` is redundant in Lean ;-)

