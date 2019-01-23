---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48256normnumweirdness.html
---

## Stream: [maths](index.html)
### Topic: [norm_num weirdness](48256normnumweirdness.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156327693):
What's going on here?

```lean
import tactic.norm_num
import data.real.basic

lemma floor_iff_bounds (r : ℝ) (z : ℤ) :
↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [←le_floor, ←int.cast_one, ←int.cast_add, ←floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]

-- set_option pp.all true
theorem floor_example : floor (71/10 : ℝ) = 7 :=
begin 
  rw ←floor_iff_bounds,
  split,
  { norm_num},
  -- ⊢ 71 / 10 < ↑7 + 1
  -- norm_num, -- seems to hang 
suffices : (71 : ℝ) / 10 < 7 + 1,
  simpa using this,
  -- ⊢ 71 / 10 < 7 + 1
  -- norm_num -- deterministic timeout
  sorry
end

example : (71 : ℝ) / 10 < 7 + 1 :=
begin
  -- ⊢ 71 / 10 < 7 + 1
  -- exactly the same term as the sorry above
  -- even with pp.all true
  norm_num -- works fine?!
end
```

Inside the bigger proof, I can't get norm_num to work, even though with pp.all on the goal seems to be exactly the same as the simpler example, where `norm_num` works fine. I checked the types with diff and there was no difference (unless I did something stupid)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156328876):
And lean is happy with this:
```lean
import tactic.norm_num
import data.real.basic

lemma floor_iff_bounds (r : ℝ) (z : ℤ) :
↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [←le_floor, ←int.cast_one, ←int.cast_add, ←floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]

set_option pp.all true
lemma aux : (71 : ℝ) / 10 < 7 + 1 :=
begin
  -- ⊢ 71 / 10 < 7 + 1
  -- exactly the same term as the sorry above
  -- even with pp.all true
  norm_num -- works fine?!
end

theorem floor_example : floor (71/10 : ℝ) = 7 :=
begin
  rw ←floor_iff_bounds,
  split,
  { norm_num},
  -- ⊢ 71 / 10 < ↑7 + 1
  -- norm_num, -- seems to hang
suffices : (71 : ℝ) / 10 < 7 + 1,
  simpa using this,
  exact aux, 
  -- ⊢ 71 / 10 < 7 + 1
  -- norm_num -- deterministic timeout
  -- sorry
end
```
Weird.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329084):
And this works too:
```lean
import tactic.norm_num
import data.real.basic

lemma floor_iff_bounds (r : ℝ) (z : ℤ) :
↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [←le_floor, ←int.cast_one, ←int.cast_add, ←floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]

set_option pp.all true
theorem floor_example : floor (71/10 : ℝ) = 7 :=
begin
  rw ←floor_iff_bounds,
  split,
  { norm_num},
  -- ⊢ 71 / 10 < ↑7 + 1
  -- norm_num, -- seems to hang
suffices : (71 : ℝ) / 10 < 7 + 1,
  simpa using this,
  have  : (71 : ℝ) / 10 < 7 + 1 := by norm_num,
  exact this,
  -- ⊢ 71 / 10 < 7 + 1
  -- norm_num -- deterministic timeout
  -- sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329174):
This is really weird. The second norm_num works if you sorry the first. But then, bizarrely, if you change the first one to `{suffices : (7 : ℝ) ≤ 71/10, simpa, sorry}` the second norm_num fails.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329293):
Last one, I promise! This works too (probably should have tried this first):
```lean
import tactic.norm_num
import data.real.basic

lemma floor_iff_bounds (r : ℝ) (z : ℤ) :
↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [←le_floor, ←int.cast_one, ←int.cast_add, ←floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]

--set_option pp.all true

theorem floor_example : floor (71/10 : ℝ) = 7 :=
begin
  rw ←floor_iff_bounds,
  split,
  { norm_num},
  -- ⊢ 71 / 10 < ↑7 + 1
  -- norm_num, -- seems to hang
suffices : (71 : ℝ) / 10 < 7 + 1,
  simpa using this,
  -- have  : (71 : ℝ) / 10 < 7 + 1 := by norm_num1,
  exact by norm_num,
  -- ⊢ 71 / 10 < 7 + 1
  -- norm_num -- deterministic timeout
  -- sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329529):
My best guess is that it has something to do with the type class instance cache. But it's bedtime now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357776):
This localizes to the same place as https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num . If you add some tracing around `norm_num.lean:162` you see what's going on: the `guard` is failing because `e2` and `e2'` have different `has_one` instances. I'm still not 100% sure why `norm_num` creates different instances in different circumstances, but I guess it's some kind of a cache issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357872):
One solution: guarding for structural equality is maybe too strong there, but checking that they unify is too weak. We really want to check that the numeral structures match exactly, and the type class instances unify.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357929):
@**Mario Carneiro** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358300):
I see that `norm_num` is replacing one instance with another, but I don't see how that makes the later stage fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358319):
even if the bottom up simp decides to replace the instance, normalizing the lt should still work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358810):
`norm_num1` should kill the second goal. But it fails at that `guard` call, because the output of C++ `norm_num` uses a different `has_one` instance than the one that (I think) came from the elaborator. It made some progress though, which `simp` then reverts, so it loops.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358900):
doesn't the guard just make sure that something has changed before changing it? It should be harmless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358938):
oh, different guard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358946):
that guard is just an assert, it can be removed if it's causing trouble

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358948):
The guard makes sure that the output of C++ `norm_num` is what Lean `norm_num` was expecting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359001):
I guess it could be defeq instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359035):
defeq doesn't really make sense here. The point of the guard is to catch mistakes, I guess. If you check for defeq and there is a mistake, you could force the kernel to normalize numerals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359038):
Removing the guard completely seems better than that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359050):
is there an option in `is_def_eq` for don't try too hard?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359126):
But then "bugs" like this one are harder to notice. I could imagine this slowing down `norm_num` noticeably in some cases, instead of failing, but that's harder for Kevin to notice/point out here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359127):
I'm not sure what `approx` does, but `md := reducible` should help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359157):
By the way -- thanks @**Bryan Gin-ge Chen** for the `exact by` workaround! I've heard of `by exact` but never this way round. This works great in my use case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359228):
`approx` has something to do with the higher order unification strategy, I think? Not sure. Are the relevant type class defs reducible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359234):
eh, I guess not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359279):
I think `is_def_eq` should be okay as long as they are actually defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359282):
if they aren't it will start unfolding numerals but that's still impossible to my knowledge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359283):
Heh. If they're actually defeq we don't need the check at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359333):
maybe you are right - failing would be great if it made norm_num fail, but this is deep in an inner function and failure has a particular meaning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359347):
it just causes these funny loops instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359648):
Yeah. A "structurally equal numeral, up to type classes" test would work here, and could maybe be useful elsewhere. The instances will be unified somewhere regardless (if we want this example to succeed).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359738):
Again, the alternative is just removing the guard, which also doesn't seem so bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359755):
I think `n1.to_nat = n2.to_nat` should work for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359764):
The two "bugs" that it's identified are only kind of bugs.

