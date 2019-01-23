---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47722unfoldpartialapplication.html
---

## Stream: [general](index.html)
### Topic: [unfold partial application](47722unfoldpartialapplication.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766659):
Hey.
I'm trying to unfold my own definition which is only applied partially, e.g.
in a goal
```lean
finset.sum (S : finset α) (my_function b) = something_else
```
where
```lean
my_function : some_type -> α -> some_comm_monoid_type
```

In that case, dunfold/unfold doesn't work and I need to specify
```lean
finset.sum (S : finset α) (λa, my_function b a) = something_else
```
for the tactic to work. Is there a workaround for this to be done automatically ? Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766782):
You can define `my_function` with the second argument right of the colon

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766787):
i.e. write `my_function (s : some_type) : α -> some_comm_monoid_type := λa, ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766794):
assuming you always want to unfold this function in such a partially applied environment

