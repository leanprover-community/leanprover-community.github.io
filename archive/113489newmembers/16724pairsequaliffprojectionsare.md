---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/16724pairsequaliffprojectionsare.html
---

## Stream: [new members](index.html)
### Topic: [pairs equal iff projections are?](16724pairsequaliffprojectionsare.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722245):
Can anyone give me a pointer on how prove this?
```lean
example {α β} {a c : α} {b d : β} (h: (a, b) = (c, d)) : a = c := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722253):
```lean
example {α β} {a c : α} {b d : β} (h: (a, b) = (c, d)) : a = c :=
begin
  cases h,
  refl,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722349):
The state after `cases` is a bit weird. You can also directly provide the proof term `(prod.mk.inj h).left`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722350):
```lean
example {α β} {a c : α} {b d : β} (h: (a, b) = (c, d)) : a = c :=
(prod.mk.inj h).1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722351):
Thanks so much!!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722360):
```lean
example {α β} : ∀ {a c : α} {b d : β} (h: (a, b) = (c, d)), a = c
| a c b d rfl := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722399):
So that's a tactic mode proof, a term mode proof, and a proof using the equation compiler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722448):
Haha, that's great :D - I'm not quite sure how the equation compiler does it tho ;p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722505):
`(a, b)` has type `prod \alpha \beta`, an inductive type, so you need tools to deal with terms of this type. When the inductive type `prod` is defined, Lean creates with it its recursor `prod.rec`, which is the universal way to define a map from `prod \alpha \beta` to anywhere. Lean then creates a bunch of other useful functions automatically, you can see what they are by typing `#print prefix prod`. There's usually something called `X.mk.inj` in there for an inductive type `X`, so that's what I was looking for. That's how I found the term proof. For the tactic mode proof, `cases` is a great tactic for any inductive type, it takes the type to pieces. 

For the equation compiler proof, we make Lean do the work. I had to move things to the other side of the colon. The point is that I can tell Lean that without loss of generality `h` *must* be `rfl`. I still don't really understand how the equation compiler actually works, but I have sort-of got the hang of how to use it in practice. Your question is a great basic example of how to use its power.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 02 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722564):
it uses `prod.no_confusion` under the hood, which is basically the same as `prod.inj`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722580):
You folks are amazing. Thank you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722619):
Just to be clear -- moving stuff to before or after the colon doesn't change the proposition, it's just a trick for controlling whether or not you have to give the inputs yourself in the "first line" of your proof.

