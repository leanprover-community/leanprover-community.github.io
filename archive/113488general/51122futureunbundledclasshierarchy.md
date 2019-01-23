---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51122futureunbundledclasshierarchy.html
---

## Stream: [general](index.html)
### Topic: [future unbundled class hierarchy](51122futureunbundledclasshierarchy.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698387):
Sebastian Ullrich said (in the multiset thread)

```quote
Just idle speculation, I suppose in a future unbundled class hierarchy we would rather have an instance `is_zero ∅ (multiset a)` instead of `has_zero (multiset a)`?
```

Does this say "in Lean 4, the whole type class system is going to change a lot"? 

I realised over the last two weeks that mathematicians think "G is a group" is a proposition, but that `Hyp : group G` is not. Maybe if a mathematician is pushed they might concede that actually it's "the pair `(G,*)` is a group" which is the proposition, but Lean still wants more (identity and inverse). I guess what I'm saying is that questions from students have made me myself question why things are set up this way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698439):
The last bit has to do with constructivity in type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698457):
Even if a function is uniquely defined in the relational sense, it's not quite the same as a function in type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698464):
I thought it might do. So if someone decided to make the fundamental typeclass `is_group` we'd end up carrying around all three things (mul, inv, identity)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698510):
So while in ZFC it suffices to have (G,*) since 1 is unique, in lean you really want a concrete witness to this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698514):
What about making `G` plus `mul` + `inv` + `1` into a structure, and making `is_group` a propositional typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698516):
In classical lean, you can nevertheless define 1 from * if you wanted, but its definitional reductions won't be great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698524):
I'm just trying to question the way we do it, not because of groups, but because of diamonds in general. Presumably if every typeclass was a Prop the diamond problems would go away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698526):
That option has been discussed (`group_struct` plus `is_group`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698572):
My response is, if `group_struct` isn't useful on its own it's not worth the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698575):
I was wondering whether Sebastian's comments meant that some changes would be implemented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698582):
if every interesting `group_struct` is also a group then it may as well be bundled in the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698584):
Remember there were problems with product of metric / top spaces (which I think were solved) and problems with modules over rings (which I think were not)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698590):
Can this sort of approach be used to solve them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698596):
Sebastian's comments relate to Leo's plans with the new algebraic hierarchy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698597):
If every interesting `group_struct` were a group, but this caused problems later down the line, then this would be an argument for not bundling.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698598):
i.e. the `@[algebra]` classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698601):
that's a rather vague worry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698602):
Where do I read about Leo's plans and the `@[algebra]` classes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698641):
there's a wiki page for it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698644):
https://github.com/leanprover/lean/wiki/Refactoring-structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698654):
I remain skeptical. I will wait for Leo's implementation before considering anything along these lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698667):
So here we are just waiting to see what happens in Lean 4 and then we go with whatever changes get made?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698695):
pretty much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698698):
it's not like there is any other option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698699):
I thought that another vague plan was to get a whole bunch of maths out of core Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698703):
I believe that will happen as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698706):
and then it's up to mathlib to decide whether it's `group` or `is_group`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698713):
It's possible that changes to `simp` will necessitate a certain design

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698767):
And it's not just "leo broke today's system", it could just as easily be "Leo's new system is way better and we would be stupid not to use it"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 15 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698819):
I predict that most of the large scale structural changes in mathlib after lean 4 will be done because we want to take advantage of some new feature, not to fix a breaking change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698841):
I'd seen that wiki page several times before, and my interpretation of it was "it's mostly CS stuff that I don't understand, but it documents an old change to the structure command which was already made"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/future%20unbundled%20class%20hierarchy/near/129698852):
I now think this interpretation might be incorrect -- it might say "even though there is `use_old_structure_command` or whatever it's called, there are still some things here which are not in Lean and might in the future be in Lean"


{% endraw %}
