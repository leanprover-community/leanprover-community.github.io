---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99190isthistruewithoutdecidable.html
---

## Stream: [general](index.html)
### Topic: [is this true without decidable](99190isthistruewithoutdecidable.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509753):
```lean
example (R : Type) [ring R] (i j : ℕ) (hnat : i ≠ j)
(hR : ((i : R) + 1) = ((j : R) + 1)) :
((1 : R) = (0 : R)) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509865):
If it is true, what is the one-line proof?
If it is not true, what is the one-line proof assuming `[decidable_eq R]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509993):
Never mind. This is completely false.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510050):
/me needs to relearn modular arithmetic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510142):
I thought this was my goal state. But it's not. `i` and `j` are coerced somewhere else. But I don't know where.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510154):
/me needs to look at the `pp.all true` variant of the goal state.


{% endraw %}
