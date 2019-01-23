---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22859fcircghorforallxfgxhx.html
---

## Stream: [general](index.html)
### Topic: [f circ g = h or forall x, f (g x) = h x?](22859fcircghorforallxfgxhx.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544509):
I am constantly proving that various functions are equal because they are both the unique function with some property. A lot of my proofs naturally prove `f circ g = h`. However Kenny often writes such goals as `forall x, f (g x) = h x`. Normally in Lean I would prove `f circ g = h`  by applying funext and then `intro x`. However in the kind of mathematics I'm currently doing this is not the way to prove things -- in fact I hardly ever get my hands dirty with explicit terms, I'm just chasing around universal properties.

#### [ Kevin Buzzard (Apr 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544552):
Kenny set up a structure with things like `function.left_inverse g f` and `function.right_inverse g f` and I had assumed these would unravel to `g circ f = id` etc but even these core functions evaluate to `forall x, g (f x) = x`

#### [ Mario Carneiro (Apr 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544560):
The left inverse thing is convenient because that way you can write `function.left_inverse g f x`

#### [ Kevin Buzzard (Apr 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544561):
What's a nice convenient way to deduce "forall x, g (f x) = h x" from "g circ f = h" ? I keep having to enter tactic mode and then rewriting the goal with rw, and usually rw \l.

#### [ Kevin Buzzard (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544600):
Is there a proof of `g circ f = h -> forall x, g (f x) = h x`?

#### [ Kevin Buzzard (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544601):
I am using it all the time

#### [ Mario Carneiro (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544603):
then make it a lemma

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544606):
fair do's

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544612):
what's it called?

#### [ Mario Carneiro (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544615):
it's a bit too specific for my taste, but if you fold it in with one of your definitions I'm sure it will work well

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544618):
I think what I'd rather do is to rewrite all the definitions which we have which involve the x

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544672):
however I am concerned that end users might need the "explicit" versions

#### [ Mario Carneiro (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544675):
then have a special constructor for your more user-facing theorems that accepts the explicit version

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544677):
I don't understand this

#### [ Mario Carneiro (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544678):
I would make that lemma a biconditional BTW, you will want both directions

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544679):
I know that 9 times out of 10 when i'm trying to prove f = g the first thing I do is apply funext

#### [ Kevin Buzzard (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544682):
but here it's never true

#### [ Mario Carneiro (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544687):
My initial thought on this is to use functions, you are basically doing category theory lite

#### [ Kevin Buzzard (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544689):
right

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544691):
I don't care about my actual definition of a localised ring

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544730):
all I ever use is the universal property

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544731):
which is a real relief

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544733):
because the localised ring is a quotient type

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544735):
and they are awkward to use

#### [ Mario Carneiro (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544740):
So when do you actually need the `x`?

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544741):
no idea

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544749):
I am not sure I do

#### [ Mario Carneiro (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544750):
At the very least you have some notion of a "user" that will use one of the theorems and prove a hypothesis by funext

#### [ Mario Carneiro (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544753):
which theorems are most likely candidates for this?

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544755):
I am not sure I have a clear notion of a user

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544756):
I think I am the only user at the minute

#### [ Mario Carneiro (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544794):
hence the quotes

#### [ Kevin Buzzard (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544799):
Maybe if Kenny does more exercises in Atiyah-Macdonald he'll become another user

#### [ Kevin Buzzard (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544801):
Maybe I'll just rip out all the x's.

#### [ Mario Carneiro (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544802):
or maybe your theorem has a conclusion that is a function equality, and the mythical user wants to congr_fun that equality

#### [ Mario Carneiro (Apr 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544810):
you should identify the most outward-facing of your theorems and make them as pleasant to use as you can

#### [ Kevin Buzzard (Apr 23 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125545016):
This exercise (wanting a theory of localization because I have a use for it, but asking Kenny to prove the theorems) has really clarified for me how this whole process of writing a library works.

#### [ Patrick Massot (Apr 23 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125558389):
```quote
 by applying funext and then `intro x`
```
Side remark: you can write `funext x` instead of `funext, intro x`. Soon you'll even be able to write `ext x` without thinking about whether you deal with an actual function or any other object for which extensionality makes sense


{% endraw %}
