---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30148typeclassinferencefail.html
---

## Stream: [general](index.html)
### Topic: [type class inference fail](30148typeclassinferencefail.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760290):
```lean
don't know how to synthesize placeholder
context:
R : Type,
_inst_1 : comm_ring.{0} R,
_inst_2 : topological_space.{0} R,
_inst_3 : @topological_ring.{0} R _inst_2 (@comm_ring.to_ring.{0} R _inst_1),
R₀ : set.{0} R,
_inst_4 : @is_subring R (@comm_ring.to_ring.{0} R _inst_1) R₀,
I : set.{0} (@coe_sort.{1 2} (set.{0} R) (@set.has_coe_to_sort.{0} R) R₀),
_inst_5 :
  @is_ideal.{0} (@coe_sort.{1 2} (set.{0} R) (@set.has_coe_to_sort.{0} R) R₀)
    (@subtype.comm_ring R (@comm_ring.to_ring.{0} R _inst_1) _inst_1 R₀ _inst_4)
    I
⊢ topological_space.{0} R
```
Why can this even fail?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760358):
Because type class inference is not looking at your context, maybe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760423):
Right... so how is it ever supposed to figure things out if it doesn't look at my context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760424):
```lean
example (G : Type) : comm_group G → ∀ a b : G, a * b = b * a :=
begin
admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760425):
```
failed to synthesize type class instance for
G : Type,
a : comm_group G,
a b : G
⊢ has_mul G
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760427):
The system doesn't look there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760433):
Shouldn't it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760435):
That's not a question I'm qualified to answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760437):
```lean
example (G : Type) [comm_group G] : ∀ a b : G, a * b = b * a :=
begin
admit
end

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760441):
That works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760445):
the square brackets mean "add me to the type class inference system"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760488):
This feels extremely counterintuitive to me... after all, we go through pains to make sure there is only one instance of a class... so if there is *one* instance in my context there won't be any others. (I promise!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760489):
However there are commands which explicitly add stuff to the type class inference system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760490):
@**Johan Commelin** What does `set_option pp.all true` before that tell you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760491):
Do you know about `letI`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760493):
Maybe search for that in the type class inference thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760497):
Aha, I don't know about `letI`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760498):
I half-understand it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760504):
the main gotcha is that this is defined in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760505):
@**Sean Leather** I already have that set to true. You see it in the output.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760506):
so you have to import _some_ mathlib file before it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760507):
Is this one of our mathematical promises playing up again?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760552):
stream:general topic:more+type+class+inference+issues leti

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760631):
https://leanprover.zulipchat.com/#narrow/search/i.20would.20rather.20just.20make.20type.20class.20inference.20work.2E

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760632):
Kenny teaching me about letI in pretty much the same situation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760634):
Right, so I insert
```lean
by haveI := topological_space R; exact
```
in the middle of my definition, and it works. Ugly!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760659):
I totally agree that it is ugly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760677):
And they have no plans to change it in Lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760686):
Mario wrote all this letI and exactI and haveI when Leo made some non-trivial changes which broke a lot of stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760688):
For some reason, liberal type class inference was making Lean slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760690):
for his application

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760691):
so he made it stricter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760694):
and then a whole bunch of mathlib broke

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760713):
and if this letI hack hadn't worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760737):
then it would not surprise me if mathlib would still be broken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760751):
On the other hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760753):
I'm not sure you can have "mathematician inference"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760757):
I think we're too clever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760799):
If you can formalise some nice MWE of something which you feel would be nice if it worked but doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760800):
then you could ask Sebastian or Mario why it doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760803):
but I fear the answer might be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760804):
something like "if that worked, then this important file would take 100 years to compile"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760811):
But I'm not sure, what happened with the changes to type class inference is beyond my pay grade

