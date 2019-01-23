---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46429normnumandfact.html
---

## Stream: [maths](index.html)
### Topic: [norm_num and fact](46429normnumandfact.html)

---

#### [Kevin Buzzard (Nov 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147921330):
```lean
import data.nat.basic
import tactic.norm_num

open nat

example : fact 7 ≥ 3 ^ 7 := 
begin
--  unfold fact, norm_num, -- fails, perhaps because of succ's
  show 7 * (6 * (5 * (4 * (3 * (2 * (1 * 1)))))) ≥ 3 ^ 7,
  norm_num,
end

```

@**Mario Carneiro**  Can you get `norm_num` to know enough about `fact` to make this work? After unfolding `fact` I get a goal with a lot of `nat.succ`'s in. Or is this harder than it looks?

#### [Mario Carneiro (Nov 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147921503):
I think you can rewrite `nat.succ` to `+1` and then apply `norm_num`

#### [Mario Carneiro (Nov 18 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147922308):
```lean
example : fact 7 ≥ 3 ^ 7 :=
by dsimp only [fact, succ_eq_add_one]; norm_num
```

