---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19144intorder.html
---

## Stream: [general](index.html)
### Topic: [int order](19144intorder.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888086):
Why is most of https://github.com/leanprover/mathlib/blob/master/data/int/order.lean commented out? Do we have these theorems elsewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888105):
Do we usually keep commented code in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888255):
Oh, it seems we have them in core :open_mouth:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888272):
@**Mario Carneiro** what's this mess?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889045):
that is a *very* old file, ported from lean 2 I guess, and the theorems in it were either never updated or never needed, or appeared in other places (e.g. core) so they just stayed as is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889074):
I'm pretty sure the whole file can be deleted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889152):
on the plus side, it's good to see that the VSCode highlighting now understands that it is a comment; it used to try highlighting it since the nested comment at the start confused it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889165):
github highlighting doesn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889226):
```
theorem coe_nat_pos {n : ℕ} (Hpos : #nat n > 0) : ↑n > 0 :=
```
we haven't had that notation since lean 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889367):
I wanted to make sure that all the theorems in the file have equivalents before deleting it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889457):
Yeah, let's do that before Lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889497):
is that an exercise I can outsource?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889539):
It depends whether you're currently working on maths or the theory of computability of ordinal stuff :-p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889914):
does linear algebra count as maths?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889927):
Is it over a semiring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889947):
lattice of submodules

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889956):
no semirings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889970):
I'm sure there is a trick, but let's say yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889984):
Since I agree that semimodules have dubious worth, I plan to only generalize theorems from modules as needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890168):
Chris asked me if semifields existed yesterday. I asked him if every semiring could be embedded into a ring and he said he didn't think so, so I told him I had no clue what a semifield was. He suggested that you take the field axioms and then remove all the ones mentioning `-`. I suppose that's one way of making new structures! I wasn't even sure if this gave a well-defined definition (in the sense that there might be more than one way of axiomatising fields)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890191):
```quote
github highlighting doesn't
```
There's [an open PR](https://github.com/leanprover/Lean.tmbundle/pull/7) to fix the github highlighting; it probably needs to be updated for the most recent fixes to the VS code extension though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890291):
Wow, this thread is degenerating quickly :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 13 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892163):
PRed https://github.com/leanprover/mathlib/pull/348

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892911):
me and Kenny are playing multiplayer lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892928):
lots of things are there that weren't there last week. I should take this to the cocalc thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895614):
Do we already have `{α : Type*} [linear_ordered_ring α] {a : α} (h : a ≠ 0) : a * a > 0`. I can prove it but it should be there already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895853):
I guess it should have a name like `mul_self_pos`, and I don't see it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895951):
I don't think it's there, and it's good to have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895952):
There's `mul_pos` and `mul_self_nonneg` but maybe you found a hole :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896064):
Indeed I called it `mul_self_pos`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896078):
approve

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896082):
Mario, do you want a PR or would it be quicker for you to add it yourself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896851):
A PR would contains something like:
```lean
section linear_ordered_ring
variables {α : Type*} [linear_ordered_ring α]

lemma mul_self_eq_zero_iff (a : α) : a*a = 0 ↔ a = 0 :=
begin
  split; intro h,
  { cases linear_ordered_ring.eq_zero_or_eq_zero_of_mul_eq_zero h with H H ; exact H },
  { rw [h, mul_zero] }
end

lemma mul_self_pos {a : α} (h : a ≠ 0) : a * a > 0 :=
lt_of_le_of_ne (mul_self_nonneg a) (λ H, h $ (mul_self_eq_zero_iff a).1 $ eq.symm H)
end linear_ordered_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896882):
Or even one more $

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896885):
I didn't include that other lemma, but it's true in any domain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896957):
do we have that `linear_ordered_ring` implies domain?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896964):
I mean, as an instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896965):
except for that pesky 0 != 1 thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896981):
OF course I see (and use) the lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896985):
oh wait, 0 < 1 in a linorder ring so it's okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897078):
https://github.com/leanprover/mathlib/commit/46502df9a61b131ee5e9265ec2593ab87b654b94 Sometimes diff tries to be too clever...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897207):
I mean, both lemmas have a hypothesis `ha` about something named `a`, so they're basically the same lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897219):
I can hear my students saying that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133898099):
you permuted two lemmas!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 13 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133900919):
(deleted)


{% endraw %}
