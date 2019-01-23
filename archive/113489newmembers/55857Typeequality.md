---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/55857Typeequality.html
---

## Stream: [new members](index.html)
### Topic: [Type equality](55857Typeequality.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 11 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478097):
Is it possible to decide whether two types are equal?

#### [ Kenny Lau (Nov 11 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478161):
no

#### [ Keeley Hoek (Nov 11 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478266):
That makes me sad

#### [ Kenny Lau (Nov 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478309):
`local attribute [instance] classical.dec`

#### [ Keeley Hoek (Nov 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478315):
Cheers, but I wanted to use it in a program

#### [ Keeley Hoek (Nov 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478323):
Instead I think I'm going to have to concoct some `user_notation` trickery to get the same syntax

#### [ Kevin Buzzard (Nov 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147479490):
I've heard it said here that even `nat = int` is undecidable

#### [ Kenny Lau (Nov 11 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147479581):
independent, even

#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147482478):
```quote
I've heard it said here that even `nat = int` is undecidable
```
How exactly are we defining equality of types?

#### [ Chris Hughes (Nov 11 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147482996):
As defined in Lean. If you separately define two inductive types of the same size, their equality will be independent.

#### [ Keeley Hoek (Nov 12 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147511856):
I guess the lesson is to stay in `expr`-land if you're trying to do something programmatically like this (e.g. either its a ```expr.const `bool []``` or its not)

#### [ Mario Carneiro (Nov 12 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147511939):
Well, it depends on what you mean. That will not get `id bool = bool`

#### [ Keeley Hoek (Nov 12 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147513299):
sure yep


{% endraw %}
