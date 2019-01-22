---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66314normnumquestionandcomment.html
---

## [maths](index.html)
### [norm_num question and comment](66314normnumquestionandcomment.html)

#### [Kevin Buzzard (Aug 13 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num question and comment/near/132069983):
```lean
import data.real.basic 

import tactic.norm_num 

definition A : set ℝ := { x | x ^ 2 < 3}

-- hangs
--example : (1 / 2 : ℝ) ∈ A := by norm_num

example : (1 / 2 : ℝ) ^ 2 < 3 ∧ (1 / 2) ^ 2 < 4 :=
begin
  split,
    -- two goals
    norm_num,
  -- where did my second goal go?
end 
```

I don't really know why the first example hangs. I can believe that Lean is reluctant to change `(1/2) \in A` to `A (1/2)` to `(lam x, x^2<3) (1/2)` to `(1/2)^2<3` (note that norm_num can solve the latter no problem) but I don't really know why it hangs. The reason I discovered it choked on this was trying to solve a goal of the form `(1 / 2 : ℝ) ^ 2 < 3 ∧  (1 / 2 : ℝ) ∈ A` by "split,norm_num,..." and `norm_num` hung on me, I thought because of the first goal, but actually because of the second.

Is making `norm_num` just act on the current goal something that can be trivially done? I know about the `{norm_num}` trick but this was an undergraduate that tripped up, not me.

