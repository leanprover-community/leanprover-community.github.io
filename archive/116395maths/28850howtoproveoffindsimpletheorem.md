---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28850howtoproveoffindsimpletheorem.html
---

## [maths](index.html)
### [how to prove of find simple theorem](28850howtoproveoffindsimpletheorem.html)

#### [Truong Nguyen (Aug 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131837673):
Hi everyone, I am a new user, my question is maybe too simple. Please make it lear for me.
Can you tell me how to find in the library or prove the simple theorem like:

theorem ttt1 (n m: ℕ ) : n <= m → n < m ∨ n = m :=
sorry

#### [Mario Carneiro (Aug 10 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131837777):
the [naming convention](https://github.com/leanprover/mathlib/blob/master/docs/naming.md) would call that `lt_or_eq_of_le`

#### [Truong Nguyen (Aug 11 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849186):
Thank you, but can you tell me how can find the stuffs like this one?

Is there a “search” command to find a theorem in the library?
I am working in some proof, sometime, it looks me quite a lot of time to find simple theorem to use.
For example, I need this one:

theorem tq (a b: ℕ ): ¬ a ≤ b ↔ b < a :=
sorry

Is there a way that I can find or prove it easily? I think it should be easy.
Thank you,
Truong

#### [Kenny Lau (Aug 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849401):
```lean
import tactic.find tactic.ring

run_cmd tactic.skip

#find ¬ _ ≤ _ ↔ _ < _
-- not_le: ∀ {α : Type u} [_inst_1 : linear_order α] {a b : α}, ¬a ≤ b ↔ b < a
```

#### [Kevin Buzzard (Aug 11 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849545):
@**Truong Nguyen** Mario already explained how to find stuff like this -- learn the naming convention :-) Follow the link!

#### [Truong Nguyen (Aug 11 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131932809):
Oh, thank you

#### [Truong Nguyen (Aug 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/133143211):
Dear Kenny Lau,
Can you give some instruction for how to use the "#find" command?

#### [Kevin Buzzard (Aug 31 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/133147051):
```lean
import tactic.find

def x := 0 -- or anything -- for some reason you can't use #find immediately

#find _ + _ ≤ _ + _

```

