---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15623inductionrecursion.html
---

## Stream: [general](index.html)
### Topic: [induction recursion?](15623inductionrecursion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Max New (Apr 25 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125688817):
Does lean support inductive-recursive definitions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125704194):
No. You can simulate a reasonably broad subclass of inductive-recursive definitions, but general induction-recursion proves lean's consistency.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 26 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125710616):
```quote
general induction-recursion proves lean's consistency.
```
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711168):
You can construct the valid contexts and well typed terms in that context by induction-recursion. Then you can prove any lean term has a denotation by induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 26 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711396):
What do you mean by “proving the consistency of Lean”?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711455):
I mean you can encode lean inside lean and prove of that object-lean that it can't prove false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711456):
i.e. exactly the thing Godel says is impossible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125711962):
...unless Lean is inconsistent ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826056):
Is the following a definition by induction-recursion?

* An $$(n+1)$$-dimensional CW complex $$X_{n+1}$$ consists of the data of
  - an $$n$$-dimensional CW complex $$X_n$$,
  - a set $$C_{n+1}$$ of "$$(n+1)$$-dimensional cells", and
  - for each $$i \in C_{n+1}$$, an "attaching" map $$e_i$$ from $$S^n$$ to the underlying topological space of $$X_n$$.

* The underlying topological space of $$X_{n+1}$$ is obtained from that of $$X_n$$ by attaching a copy of $$D^{n+1}$$ along the attaching map of each cell.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826168):
aha!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826176):
I formalized CW complex a while ago lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826180):
https://math.stackexchange.com/a/2712786/328173

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826181):
a month ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826226):
Isn't it just an inductive type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826281):
The last field (the attaching maps) involves the function "underlying topological space" which (it seems to me) you need to define simultaneously with the inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826283):
If you could define an infinite alternating list of inductive types and functions, it would be one of those.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826284):
I haven't tried actually writing it out in lean though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826288):
you don't need to know that X_n is a topological space, I think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826296):
Well I omitted the word, but it has to be a continuous map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826297):
The attaching maps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826298):
oh right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826338):
there might be other approaches, but I have an ugly approach in mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826339):
define the sigma type inductively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826340):
(not sure if it works, after I say it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125826403):
(I had some idea of how to formalize this in lean, but I'm curious to hear others, and also I didn't write down my idea and I think it was kind of ugly.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20recursion%3F/near/125827025):
I'd also appreciate a type theory expert confirming whether or not this is an example of induction-recursion at all, since induction-recursion is an unfamiliar thing and the typical examples are even more unfamiliar things, while CW complexes are something that all mathematicians learn about.

