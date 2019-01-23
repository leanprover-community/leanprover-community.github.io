---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/03603Whydoesntexistsintrogiveerrforwitnessofwrongtype.html
---

## Stream: [new members](index.html)
### Topic: [Why doesn't exists.intro give err for witness of wrong type](03603Whydoesntexistsintrogiveerrforwitnessofwrongtype.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115096):
Here's a proof that 7 is even. Why does exists.intro accept 3.5 as an argument, given that m is declared to be of type nat?

```lean 
def isEven (n: ℕ) : Prop :=
  ∃ m : ℕ, n / m = 2

theorem sevenIsEven : (isEven 7) :=
begin
unfold isEven,
apply exists.intro 3.5,
apply rfl,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115173):
Try it with `3` instead. Should work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115181):
Probably `3.5` is coerced into `3 : nat` or something like that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115244):
Note that your definition of `isEven` is not what we usually mean with being even, because `n / m` is not what we usually mean with `n / m`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 19 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115369):
If you use `set_option pp.numerals false` you see that `3.5` gets encoded as `bit1 (bit1 (has_one.one ℕ)) / bit0 (has_one.one ℕ)`, which, as Johan points out, is a natural number because of rounded division.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 19 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115404):
(`(bit1 (bit1 (has_one.one ℕ)) / bit0 (has_one.one ℕ))` is `7 / 2`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115693):
I must say that I would rather get a syntax error at this point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115958):
One way to make this happen is to look at one of @**Kevin Buzzard** suggestions and distinguish between proper division (`/`) and integer division (`÷`) (and the same can be said for subtraction vs pointed subtraction) and make sure that integers and natural numbers are only equipped with integer division. This way, expressing fractional numbers as division wouldn't work when fractional numbers aren't available.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 19 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136117906):
```quote
Here's a proof that 7 is even. 
```
Just to be clear, what's happening here is that division is maybe not what you think it is. `7 / 3 = 2`, because `7 / 3` is declared to be of type nat.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 19 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136118086):
Right. And somehow, integer division doesn't seem to mesh with fractional numbers. If we were to express integer division as `÷` and a separate type class, `3.5` would not be a valid natural number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 19 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136120649):
```quote
Right. And somehow, integer division doesn't seem to mesh with fractional numbers. If we were to express integer division as `÷` and a separate type class, `3.5` would not be a valid natural number
```
Ok. Yes. This is slightly disturbing, but I understand.

```lean
def x : nat := 3.5
```

x is now 3.


{% endraw %}
