---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/29865typeofnot.html
---

## Stream: [new members](index.html)
### Topic: [type of `not`](29865typeofnot.html)

---

#### [Scott Olson (Oct 09 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135432721):
Is there a reason we have `def not : Prop → Prop` rather than `def not : Sort u → Prop`?

I had some proofs of `¬foo` which I had to change to `foo → false` when I changed `foo` from a simple `∃` Prop to a `structure` sigma Type, but it seems like it would make sense to still say `¬foo`.

#### [Simon Hudon (Oct 09 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135433027):
It's probably a matter of convention. `¬p`, you usually assume that `p` is a proposition . An operation such as you describe might more usefully be called `is_empty`

#### [Mario Carneiro (Oct 09 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135434043):
there used to be a `~A` notation for this, but it didn't get used enough to be worth it.

