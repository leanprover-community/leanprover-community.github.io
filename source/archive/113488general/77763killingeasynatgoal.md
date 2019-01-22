---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77763killingeasynatgoal.html
---

## [general](index.html)
### [killing easy nat goal](77763killingeasynatgoal.html)

#### [Kevin Buzzard (Mar 20 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969731):
Faced with `∀ n, 2 * nat.succ (n) = nat.succ (2 * n + 1)` I find that simp or ring don't seem to be able to do it. Even `intro n, simp [nat.succ_eq_add_one,mul_add,one_add_one_eq_two]` doesn't work. I can use simp and then ring!

#### [Kevin Buzzard (Mar 20 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969887):
```
  intro n,
  suffices : 2 + 2 * n = 1 + (1 + 2 * n),
    simp [nat.succ_eq_add_one,mul_add,this], 
  ring
```

#### [Kevin Buzzard (Mar 20 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123969888):
meh

#### [Patrick Massot (Mar 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971217):
Isn't there a lemma saying it suffices to prove this in Z, and then ring does it?

#### [Simon Hudon (Mar 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971737):
Interesting! What would that lemma look like?

#### [Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971848):
From a mathematician perspective, the lemma says the inclusion of N into Z is injective

#### [Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971851):
Insert words like coercion or cast

#### [Patrick Massot (Mar 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971854):
and get the CS version

#### [Patrick Massot (Mar 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971878):
I don't have a computer with Lean where I am right now

#### [Kevin Buzzard (Mar 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971881):
Fortunately I think ring seems to work on nat, faced with ring operations like + or *

#### [Simon Hudon (Mar 20 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971936):
ah! So the injectivity of `coe` plus the distributivity over +, * and succ would do it. That is really nice

#### [Kevin Buzzard (Mar 20 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971953):
One issue is that ring would rather see `n + 1` than `nat.succ n`

#### [Kevin Buzzard (Mar 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971978):
to coerce into Z you'll need `nat.cast_add`, `nat.cast_mul`, `nat.cast_one`

#### [Simon Hudon (Mar 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123971979):
I would assume that `↑(succ n) = ↑n + 1` would be a simp rule so `succ` would disappear

#### [Chris Hughes (Mar 20 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972132):
Have you tried rfl? 2*succ n := 2*n + 2 := succ(2*n+1), maybe rw add_comm or mul_comm first?

#### [Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972404):
There should be a tactic doing that for any equality in nat which would immediately follow from ring in int

#### [Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972415):
without any preliminary rw

#### [Patrick Massot (Mar 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972422):
I'm sure Simon is already writing it

#### [Simon Hudon (Mar 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972435):
I sneezed so you wrote the above before I could get started

#### [Kevin Buzzard (Mar 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972553):
```quote
Have you tried rfl? 2*succ n := 2*n + 2 := succ(2*n+1), maybe rw add_comm or mul_comm first?
```
Aah! I tried refl before intro n and it failed, but after intro n it succeeds.

#### [Kevin Buzzard (Mar 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972554):
Thanks.

#### [Kevin Buzzard (Mar 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972561):
Chris, I'm doing the exercises here:

#### [Kevin Buzzard (Mar 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123972570):
https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html

#### [Simon Hudon (Mar 20 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123973436):
I did a bit of scripting and then tried to find what fails and I found that this works: 

```
example (n : ℕ) : 2 * nat.succ (n) = nat.succ (2 * n + 1) :=
begin
  ring,
end
```

Why doesn't it work for you?

#### [Kevin Buzzard (Mar 20 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123976260):
because I had "forall n" in front of it :-/

#### [Simon Hudon (Mar 20 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/killing%20easy%20nat%20goal/near/123976344):
Maybe `ring` should start with `intros`

