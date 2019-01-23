---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03084localnotationinmessagewindow.html
---

## Stream: [general](index.html)
### Topic: [local notation in message window](03084localnotationinmessagewindow.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125571696):
I have a local infix notation for an operation which is a local variable. Is there any hope to see Lean using this notation in the Lean messages window?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574186):
No idea, anyone? That would really help me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574294):
I've struggled with that too. Recently, I had an idea but I haven't tried it yet. What's the type of your variable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574380):
It's a composition law

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574393):
`op : R → R → R`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574400):
``local infix ` ◆ `:70 := op``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574420):
Cool. Let's try this:

```
def my_op := op

local infix ` ◆ `:70 := my_op op
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574479):
breaks everything :disappointed:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574569):
Was that not what you were going for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574605):
```lean
def my_op := op

local infix ` ◆ `:70 := my_op
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574607):
I think that's what he means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574667):
I understood he meant that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574669):
still breaks everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574679):
is `op` a `parameter` or a variable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574684):
variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574689):
Are you inside a section?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574703):
Can you make it a parameter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574704):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574709):
I meant no I'm not inside a section

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574719):
I don't know about parameters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574794):
:laughing: I thought so. They're not great in Lean but sometimes you need them. Before I go there, can you show me the output of `#check @my_op`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574877):
`my_op : Π {R : Type u_3}, (R → R → R) → R → R → R`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574897):
let's just forget that algebraic hierarchy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575047):
With a variable, if you use `my_op` somewhere, you need to provide an argument for each variable. With parameters, inside the section, the parameters are a bit like constant. Inside tactic proofs, they get a bit flaky though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575092):
I don't see the relation between the hierarchy and the problem we discuss here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575103):
Try making `op` a parameter and wrap it and the related definitions in a section


{% endraw %}
