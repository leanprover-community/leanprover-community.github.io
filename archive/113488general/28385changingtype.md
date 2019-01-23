---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28385changingtype.html
---

## Stream: [general](index.html)
### Topic: [`@` changing type?](28385changingtype.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193790):
What's going on here?

```lean
definition Nat := Π {X : Type}, (X → X) → X → X

definition Zero : Nat :=
λ (X : Type) (F : X → X) (i : X), i

#check (Zero : Nat) -- fails

#check (@Zero : Nat) -- works 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193835):
change λ (X : Type) to λ {X : Type}?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193846):
What does that change mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193849):
It doesn't fix the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193852):
never mind then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193853):
```lean
definition Nat := Π {X : Type}, (X → X) → X → X

definition Zero : Nat :=
λ {X : Type} (F : X → X) (i : X), i

#check (Zero : Nat) -- fails

#check (@Zero : Nat) -- works 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193856):
```
invalid type ascription, term has type
  (?m_1 → ?m_1) → ?m_1 → ?m_1 : Type
but is expected to have type
  Nat : Type 1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193858):
It's a universe issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193861):
change the pi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193864):
brackets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193918):
Zero has type `(? -> ?) -> ? -> ?` or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193934):
or use `⦃`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193940):
for weakly implicit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194314):
```quote
change λ (X : Type) to λ {X : Type}?
```
This is syntactically valid but does it change anything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194378):
my guess is that if you don't state the type the inferred type will be `Pi {X}, ...` for one of them and `Pi (X), ...` for the other one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194534):
In this case the binder on the lambda doesn't matter, since it is explicitly given the type `Nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194551):
All that matters for elaboration purposes is whether `Nat` is defined as `Pi {X : Type}, ...` or `Pi (X : Type), ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194690):
Do I correctly infer from Kevin's example that Lean does not remember that `Zero` has type `Nat`, even if it is explicitly told so during the `definition`? So it uses that fact while type checking the definition, but afterwards throws it away and only stores the term (or something)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194746):
I think the problem is that when Lean sees `Zero` with `{}` it immediately tries to fill in the `{}` variable, so `Zero` is the same as `@Zero _` which is not the same as `@Zero`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194750):
If you use `{{}}` then Lean decides to wait until later before guessing what goes in the brackets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194801):
The easiest fix is just to use `(X : Type)` I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194807):
When defining a type as a pi like this, you almost never want to use `Pi {X}` because of "surprises" like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194818):
This is one of the main use cases for `Pi {{X}}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194820):
like in the definition of `set.subset`


{% endraw %}
