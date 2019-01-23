---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45346equivanduniverses.html
---

## Stream: [maths](index.html)
### Topic: [equiv and universes](45346equivanduniverses.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837442):
I am interested in beefing up equiv but I am only now coming to terms with how universes work and do not yet really understand how they affect the picture if at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837448):
```lean
import data.equiv
universes u v y z
def αu (X Y : Type u) := X → Y 
def αuv (X : Type u) (Y : Type v) := X → Y
def αv (X Y : Type v) := X → Y 
 
definition u_v {X : Type z} {Y : Type z} : equiv (αu X Y) (αv X Y) := 
{ to_fun := λ f,f,
  inv_fun := λ f,f,
  left_inv := λ x,rfl,
  right_inv := λ x,rfl,
}

definition u_uv {X : Type z} {Y : Type z} : equiv (αu X Y) (αuv X Y) := 
{ to_fun := λ f,f,
  inv_fun := λ f,f,
  left_inv := λ x,rfl,
  right_inv := λ x,rfl,
}

definition u_uv {X : Type u} {Y : Type v} : equiv (αu X Y) (\auv X Y) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837452):
the last one isn't a puzzle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837455):
it unfortunately doesn't typecheck because of universe issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837460):
Is there any way of somehow forcing it to typecheck with universe coercion or something? And then would equiv still fail?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 29 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125838746):
I guess the zeroth thing to know about universes is that `universe u` doesn't mean "Fix a universe $U$"; it just makes `u` a legal thing to put somewhere that a universe is expected.
In other words, the `u` and `v`s in `\au`, `\auv`, `\av` are unrelated, and definitions `\au` and `\av` are exactly the same.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 29 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125838886):
You can think of Lean universes as corresponding to Grothendieck universes except that Lean universes are not cumulative, so that a type belongs to `Type u` for just one `u`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 29 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125839130):
To "move" a type from one universe to a bigger one, use `ulift`. The new type is `equiv` to the old one (`equiv.ulift`).

