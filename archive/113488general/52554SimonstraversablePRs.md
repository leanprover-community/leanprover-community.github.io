---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52554SimonstraversablePRs.html
---

## Stream: [general](index.html)
### Topic: [Simon's "traversable" PR's.](52554SimonstraversablePRs.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130402086):
What do these do? I can't understand anything :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130402632):
You can have a look at https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type.20class.20traversable but I fear this really CS and software engineering.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130402640):
I was also planning to ask after Simon will be done with his series of PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130402721):
Oh so it's nothing to do with the "transportable" proving that if X is a perfectoid space and X equiv Y then Y is a perfectoid space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130402760):
I think Simon mentioned a link at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 27 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130403363):
It's very much CS, though I wouldn't call it software engineering. If you're interested in references, see:
https://hackage.haskell.org/package/base/docs/Data-Traversable.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 27 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130403385):
I believe Simon is setting up infrastructure to simplify expression manipulation and, therefore, tactic writing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130403955):
Aah thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 27 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130405496):
@**Sean Leather** that's pretty much it. Plus, I think Lean should be like Haskell as a programming language and traversable should help with that.

@**Kevin Buzzard** Don't despair, `transportable` is still under development.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 27 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simon%27s%20%22traversable%22%20PR%27s./near/130406943):
... and so is `mono`, if people still remember it


{% endraw %}
