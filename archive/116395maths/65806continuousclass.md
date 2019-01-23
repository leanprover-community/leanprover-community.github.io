---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65806continuousclass.html
---

## Stream: [maths](index.html)
### Topic: [continuous class](65806continuousclass.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 30 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130544108):
Should we turn `continuous` into a class `is_continuous` like we did for group homorphisms? I spent quite a lot of time explicitly invoking lemmas that could be handled by type class inference. Same question for uniform continuity.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 30 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130559925):
I think this is a very good idea. It's ~~long~~high (thanks, Kenny) time it is turned in to a class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 30 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130562916):
Should we turn everything which returns a proposition into a class? There will be no diamonds! Why is this not a no-brainer? Johannes wrote `def continuous (f : α → β) := ∀s, is_open s → is_open (f ⁻¹' s)` in `analysis/topology/continuity.lean` so he has chosen to make a definition, and he knows what he's doing. Patrick is proposing instead using a class, but propositions are useful sometimes. But you could make the class a proposition, right? @**Johannes Hölzl** why is this not a class "by default"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130564662):
About what Johannes wrote: I think this was a very long time ago and maybe it wasn't a conscious decision (for me everything written before I started using Lean is ancient).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jul 30 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566344):
`continuous` needs to stay a definition, otherwise a lot of proofs break. I would prefer to use `apply_rules` and maybe `auto_param` instead of type classes. The problem with the type class mechanism is that it doesn't handle composition of functions very well. I'm still not sure if using the type class mechanism to handle morphisms is a good idea.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 30 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566684):
This is interesting -- I don't understand this at all. It certainly sounds like a proof that not everything which is a proposition should be handled by the type class inference system! So the issue is the instance corresponding to "if f and g are continuous then so is f o g" is poorly behaved? Why is this any different to "if G and H are groups then so is G x H"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 30 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566714):
Is it the difference between `f ∘ g` and `λ x, f (g x)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567262):
the type class mechanism needs to be very fast, and it is often very annoying if one wants to force a specific type class instance (i.e. writing it down using `@t A _inst1 ...`). So, yes: many things shouln't be type class instances.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 30 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567582):
Ok, I'll try playing with `apply_rules` (I had no luck with `apply_rules` and `tendsto` so I'm not very optimistic)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jul 30 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567592):
Hm, yes we might have the same problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 30 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130575267):
Yes, I had the same experiences.

* I tried making a type class `is_continuous` but I couldn't get inference to work in even some simple cases, I think involving function composition. But it's possible I didn't set things up quite right. Does the type class work well for group homomorphisms? I haven't had occasion to use that.

* I've been happy with a tactic which just repeatedly tries to apply `continuous.comp` and `continuous_fst` and so on. But it doesn't work to literally use `apply`. Possibly the reason is that `continuous` is a Pi type and this causes `apply` to guess the wrong number of `_`s to insert (I think Mario explained this once). Anyways it works fine to use `refine` and manually specify the correct number of arguments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 30 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130575487):
What I'm currently using: https://gist.github.com/rwbarton/d088776fa881a00c6820a02d14c5c9e0
It's based on (a somewhat old version at this point of) Scott's `tidy` library.


{% endraw %}
