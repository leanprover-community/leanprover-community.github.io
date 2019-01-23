---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78098simplestructuralequality.html
---

## Stream: [new members](index.html)
### Topic: [simple structural equality](78098simplestructuralequality.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 08 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121507):
How would I prove this?
```lean
structure mystr :=
    (A : ℕ)
    (B : bool)
    (p : A > 10)

def mystr_eq (x y : mystr) (A_eq : x.A = y.A) (B_eq : x.B = y.B) : x = y 
:= by sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121866):
```lean
def mystr_eq (x y : mystr) (A_eq : x.A = y.A) (B_eq : x.B = y.B) : x = y
:= by cases x ; cases y ; cc
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121909):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121919):
`congr`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121937):
next question: how to prove it without tactics? Just a proof term.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121944):
`congr ; assumption` instead of `cc` also works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121952):
`congr'` too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121953):
It's longer though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121955):
but is much longer to type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121960):
still longer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121965):
`cc` is longer to run

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121967):
I suppose `congr; cc` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121976):
Can't we have `congra`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121978):
`by congr ; assumption` fails on `congr` for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121980):
`congr'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121985):
is `congra`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122043):
you have to do `cases` first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122165):
term proof:
```
theorem mystr_eq : ∀ (x y : mystr) (A_eq : x.A = y.A) (B_eq : x.B = y.B), x = y
| ⟨xA, xB, xp⟩ ⟨_, _, _⟩ rfl rfl := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 08 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122397):
I was about to post that term proof but Mario just beat me to it. When I was a beginner I found those sorts of proofs miraculous; that's why I thought it was worth mentioning. The equation compiler is so clever.


{% endraw %}
