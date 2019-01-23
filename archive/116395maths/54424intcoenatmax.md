---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54424intcoenatmax.html
---

## Stream: [maths](index.html)
### Topic: [int.coe_nat_max](54424intcoenatmax.html)

---

#### [Kevin Buzzard (Sep 06 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_max/near/133455883):
I don't *think* `int.coe_nat_max : {m n : ℕ} : (↑(max m n) : ℤ) = max m n` is in mathlib, and I needed it today. Kenny produced this proof:

```lean
theorem int.coe_nat_max {m n : ℕ} : (↑(max m n) : ℤ) = max m n :=
begin
  unfold max,simp [int.coe_nat_le],
  split_ifs;refl,
end
```

but I was thinking that the result probably lived near the beginning of `data.int.basic` and I'm not sure that the devs will want `split_ifs` to be used in such a low-level file. Should it go later on or should we think of a more low-level proof? (or is it there already?)

#### [Mario Carneiro (Sep 06 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_max/near/133456744):
I agree this belongs in `data.int.basic`, and there is no problem using `split_ifs`. The mathlib tactics are all very low in the dependency order so that mathlib can use them

