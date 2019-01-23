---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01043isthereanybetterway.html
---

## Stream: [maths](index.html)
### Topic: [is there any better way?](01043isthereanybetterway.html)

---

#### [Truong Nguyen (Sep 03 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271618):
Hi Everybody,
I this this way of proving 1 < 4 is not a smart way. Do you have any better way for doing this. Thanks

theorem oiooo : 1 < 4 :=
begin
have thh: 1 < nat.succ 1, from nat.lt_succ_self 1,
have hht6: nat.succ 1 < 3, from nat.lt_succ_self 2,
have ht5: 3 < 4, from nat.lt_succ_self 3,
have tg: 1 < 3, from nat.lt_trans thh hht6,
show 1 < 4, from nat.lt_trans tg ht5
end

#### [Johan Commelin (Sep 03 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271642):
You can format code by putting three backticks before and after it:
````
```lean
Your code goes here
```
````

#### [Kenny Lau (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271717):
```lean
theorem oiooo : 1 < 4 := dec_trivial
```

#### [Kenny Lau (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271728):
```lean
theorem oiooo : 1 < 4 :=
by repeat {constructor}
```

#### [Kevin Buzzard (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271729):
rofl

#### [Kevin Buzzard (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271731):
that's some obscure proof

#### [Kevin Buzzard (Sep 03 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271750):
@**Truong Nguyen** the correct proof is `dec_trivial` -- inequalities are decidable on the naturals

#### [Kevin Buzzard (Sep 03 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271800):
Unfortunately the reals do not have decidable equality, so for them you have to prove stuff like 1 < 4 using `norm_num`

#### [Johan Commelin (Sep 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271865):
```lean
import tactic.tidy

theorem oiooo : 1 < 4 := {! _ !}
```

#### [Kenny Lau (Sep 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271869):
```lean
theorem oiooo : 1 < 4 :=
nat.one_lt_bit0 $ ne.symm $ nat.zero_ne_bit0 $ nat.one_ne_zero
```

#### [Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271880):
The `{! _ !}` is called a goal. You can fill it in in two ways: (1) Click the light bulb. (2) Put your cursor in the goal and hit `Ctrl-.`

#### [Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271887):
Choose the option "Use `tidy` to fill in the goal."

#### [Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271898):
```lean
theorem oiooo : 1 < 4 := by tidy
```
will also work.

#### [Truong Nguyen (Sep 03 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133273683):
Oh, Thank you.
How about this one: 
``` lean
theorem tyyy (a b: ℕ ):
(a + b) % 4 = (a % 4 + b % 4) % 4 :=
sorry
```

#### [Bryan Gin-ge Chen (Sep 03 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274209):
This is part of the way there:
```lean
import data.zmod, tactic.ring

theorem tyyy0 (a b: ℕ ):
((a + b) : zmod 4) = (a : zmod 4) + (b : zmod 4) := by ring
```
There should be some way to use `zmod.cast_mod_nat` but I'm stuck.

#### [Truong Nguyen (Sep 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274358):
I am stuck too.

#### [Reid Barton (Sep 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274407):
I think the original tyyy is a lemma somewhere in mathlib

#### [Reid Barton (Sep 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274562):
There's `int.add_mod_mod` and `int.mod_add_mod`

#### [Reid Barton (Sep 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274692):
Which you can combine to get what you want

#### [Chris Hughes (Sep 03 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274701):
I think this should work
```lean
theorem tyyy (a b: ℕ ):
(a + b) % 4 = (a % 4 + b % 4) % 4 := 
nat.modeq.modeq_add (eq.symm (nat.mod_mod _ _)) (eq.symm (nat.mod_mod _ _))
```

