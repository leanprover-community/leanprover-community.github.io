---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57903inductionontwomultisets.html
---

## Stream: [general](index.html)
### Topic: [induction on two multisets](57903inductionontwomultisets.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456296):
I am trying to define a function `multiset nat -> multiset nat -> nat`, by induction. If I have two multisets `C` and `L` and if I know the value of the function on all the pairs `(C-{x},L)`(with `x` in `C`)  and `(C,L-{y})` (with `y` in `L`) then I have a formula which will give me the value at `(C,L)`. The formula is not symmetric in `C` and `L`. The tool which the API gives me is

```
multiset.strong_induction_on :
  Π {α : Type u_1} {p : multiset α → Sort u_2} (s : multiset α),
    (Π (s : multiset α), (Π (t : multiset α), t < s → p t) → p s) → p s
```

but I can't figure out how to use this directly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456360):
You can do this by a nested induction using that function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456361):
So I tried this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456408):
but my interpretation of what you're saying is "define `f(C,L)` for `L` constant and `C` varying, by induction on `C`" and the problem is that the definition needs both `C` and `L` to move. What am I missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456416):
Define `f C L` for all `L` and fixed `C`, by induction on `C`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456461):
In the IH we know `f (C-{x}) L'` for all `L'` and need to define `f C L`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456465):
To define `f C L` I need more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456466):
I need `f C L'` for all `L'` smaller than `L`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456475):
we do so by induction on `L`. Now the induction hypothesis gives us `f C (L-{y})` and we must define `f C L`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456479):
OK I'll take it from here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456481):
The reason I asked was that I was not 100% sure that the tools I had were enough. If you're confident that they are then I just need to work harder. Thanks for the tips.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456486):
it is two inductions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456488):
one inside the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456489):
Right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456529):
I'm a mathematician. I don't understand induction properly :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456530):
We only do induction on nat in maths.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456532):
This can also be viewed as a well founded induction in lex order, first by `C` then `L`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456533):
This I know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456535):
But the only way I know to do a well-founded induction is on an inductive type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456542):
and since `(C-{x},L)` and `(C,L-{y})` are both less in this order, this method should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456589):
I guess an alternative to the `multiset.strong_induction_on` API is just to provide a proof that multiset `<` is well founded and let you use the tools from the `well_founded` namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456591):
I didn't even know that namespace existed!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456606):
That's what powers the `using_well_founded` equation compiler stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456609):
The only time I've used well-founded stuff is when trying to persuade the equation compiler that my definition is sound.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456611):
i.e. indirectly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456615):
Back in the old days we used `well_founded.fix` when we wanted to write a wf definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456660):
and it requires a proof that the relation du jour is well founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129473610):
I didn't get the memo that this method was passe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129473764):
Probably I need to get with the times :)

