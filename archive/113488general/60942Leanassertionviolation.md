---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60942Leanassertionviolation.html
---

## Stream: [general](index.html)
### Topic: [Lean assertion violation](60942Leanassertionviolation.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293256):
```
universes u v 

theorem set.subset.trans {α : Type*} {a b c : set α} (ab : a ⊆ b) (bc : b ⊆ c) : a ⊆ c :=
assume x h, bc (ab h)

def set.preimage {α : Type u} {β : Type v} (f : α → β) (s : set β) : set α := {x | f x ∈ s}
infix ` ⁻¹' `:80 := set.preimage

structure presheaf_of_types (α : Type*) := 
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) (H : V ⊆ U), 
  (F U) → (F V))
(Hcomp : ∀ (U V W : set α) 
  (HUV : V ⊆ U) (HVW : W ⊆ V),
  (res U W (set.subset.trans HVW HUV)) = (res V W HVW) ∘ (res U V HUV) )

definition presheaf_of_types_pushforward
  {α : Type*}
  {β : Type*}
  (f : α → β)
  (FPT : presheaf_of_types α)
  : presheaf_of_types β :=
  { F := λ V : set β, FPT.F (set.preimage f V),
    res := λ V₁ V₂ H, 
    FPT.res (set.preimage f V₁) (set.preimage f V₂)(λ x Hx,H Hx),
    Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293261):
```
LEAN ASSERTION VIOLATION
File: /home/travis/build/leanprover/lean/src/frontends/lean/elaborator.cpp
Line: 3167
Task: /home/buzzard/Encfs/Computer_languages/Lean/lean/bug.lean: presheaf_of_types_pushforward
m_ctx.match(e, *val2)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293307):
Here's a (mathlib-free) assertion violation. Is this a known issue? If not, is my MWE minimal enough? If so, shall I file a bug report? I'd be happy to hear advice before working on this any more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293311):
I'm looking into it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293312):
`Lean (version 3.3.1, commit d6d44a19947e, Release)` Ubuntu 16.04

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293315):
Can reproduce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293322):
Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293326):
I get the feeling structure notation is too sophisticated for our (the implementers') own good :sweat_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293365):
ha ha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293368):
so it's my fault? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293370):
I wasn't expecting rfl to work, it's just sometimes worth a try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293376):
It's obviously our fault for enabling you to do weird things :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293379):
I would be interested to know what the first thing you do in this situation is. If it's to fire up some C++ debugger then fair enough, you've lost me already, but if it's to just set some options and watch more carefully then I would be interested to follow along for a while

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293419):
What do I do that is weird?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293548):
actually I wonder whether I am now grown up enough to fire up a C++ debugger myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293628):
It's a unification error, so I'm now looking at the `is_def_eq_detail` trace. The terms are still quite big - if you find a way to minimize them, that would be great.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293638):
OK I will try and minimise more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294055):
```
definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { F := sorry,
    res := sorry,
    Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294056):
No idea if that helps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294100):
I just replaced some stuff with sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294184):
```
definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294251):
oh I have made it smaller

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294257):
```
universes u v

structure presheaf_of_types (α : Type*) := 
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) ,
  (F U) → (F V))
(Hcomp : ∀ (U V W : set α),
  (res U W  = (res V W) ∘ (res U V) ))

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hcomp := λ Uβ Vβ Wβ,rfl -- assertion violation
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294683):
```
structure presheaf_of_types (α : Type*) := 
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) ,
  (F U) → (F V))
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295041):
```
structure presheaf_of_types (α : Type) := 
(res : ∀ (U V : set α) ,
  {x : α // U x} → {x : α // V x})
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295092):
I'm going to stop there because all I am doing now is taking things like my general F from set alpha to Type and replacing it with an arbitrary explicit F (in this case the map sending U to the subtype corresponding to U)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295103):
oh here's an even better one, I can just use some random map unit to unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295104):
```
structure presheaf_of_types (α : Type) := 
(res : ∀ (U V : set α) ,
  unit → unit)
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295160):
Still simpler:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295163):
```
structure presheaf_of_types (α : Type) := 
(res : ∀ (U : set α) ,
  unit → unit)
(Hidem : ∀ U : set α, res U = (res U) ∘ (res U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295210):
```
structure presheaf_of_types (α : Type) := 
(res : unit → unit)
(Hidem : ∀ U : set α, res = (res) ∘ (res))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295231):
Thanks! That should do hopefully.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295270):
```
structure presheaf_of_types := 
(res : unit → unit)
(Hidem : ∀ U : unit, res = res ∘ res)

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  : presheaf_of_types :=
  { Hidem := λ U, rfl,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295286):
Thanks for asking for more minimisation -- in some sense that was quite instructive. Initially I just removed everything not directly related to the violation in the form I had it, but after you asked more I realised there was nothing stopping me trying to find simpler violations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295366):
Adding the field `res := id` makes the problem go away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295482):
Hey, is it doing a prolog-like search?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295495):
Poor Kevin was deprived of a prolog-like search yesterday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295496):
Please be nice this time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295504):
I should never have equated this phrase with "random thing I don't understand"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295549):
but looking at the debugging output it looks like it might be backtracking...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295576):
I'm picturing you asking to Scholze: "are you doing a a prolog-like search" at the end of a really tough talk.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295702):
Maybe I don't even know what backtracking means. I guess I look at these debugging outputs and think "oh look it's trying lots of things in what looks like a systematic manner"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295706):
It's not enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295709):
but I probably need to look more closely to distinguish the difference between "if this fails, discard it and try something else"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295710):
and "let's actually backtrack here"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295711):
You want to start following a path and then come back to an earlier branch point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295714):
yes this is just dawning on me now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298542):
@**Kevin Buzzard** Congrats, I think you found a bug where definitional equality is not idempotent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298548):
Is that a good thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298549):
Do I get an achievement?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298550):
I'm jalous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298585):
My conv bug seems much less cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 05 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298715):
@**Sebastian Ullrich** "Idempotent"??  Do you mean `is_def_eq(t, t)` returns false?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298717):
On the first run it returns true for two terms, then false on any subsequent runs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298811):
ooh can I prove false??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298814):
I would definitely get an achievement for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298816):
Nah, it's just the elaborator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298818):
aah well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298831):
Apparently `elim_delayed_abstractions` accidentally supports backtracking assignments to a metavar... not the correct place for a Prolog-like search

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298834):
you lost me at the prolog-like search bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298883):
That was mostly a joke :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 05 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298896):
Wow, this is unexpected.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298946):
Kenny posted this about a week ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298947):
`instance error (α : Type) : group α := { mul_assoc := λ x y z, rfl }
`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298948):
without any further comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298954):
and it might be the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 05 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123299000):
Yep, same assertion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 05 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123299285):
[users.png](/user_uploads/3121/JbuLIJprxGe-IqMGOyrrJlyK/users.png)
One little bug and everybody flies out, except devs. So sad...


{% endraw %}
