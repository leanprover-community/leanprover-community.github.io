---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92286dumpexprtocontext.html
---

## Stream: [new members](index.html)
### Topic: [dump expr to context](92286dumpexprtocontext.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 24 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282282):
Is there a way to dump an expr to the context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 24 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282927):
What do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 24 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282942):
`tactic.pose`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 24 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148286561):
@**Rob Lewis** that dumps the evaluated expression to the context; I want the unevaluated expression as an `expr` itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148286627):
You should learn to ask better questions Kenny.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148290574):
You want a tactic that adds a local hypothesis of type `expr`, defined to be some particular `expr` that you have? Could you explain what you're trying to do? I kind of doubt this is the way to do it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148359542):
Can't you just use pose and give it `` `(e) ``, where `e : expr`?

