---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/15301Scalarmultiplicationnotdefinedforfunctions.html
---

## [maths](index.html)
### [Scalar multiplication not defined for functions](15301Scalarmultiplicationnotdefinedforfunctions.html)

#### [Abhimanyu Pallavi Sudhir (Nov 22 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Scalar multiplication not defined for functions/near/148196578):
It seems that `smul` over `ℝ` isn't defined for functions from `ℝ` to `ℝ` -- or at least, I can't get it to work.

#### [Abhimanyu Pallavi Sudhir (Nov 22 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Scalar multiplication not defined for functions/near/148196620):
It seems to me that functions are a rather natural type to use scalar multiplication on -- or am I missing some trick?

#### [Abhimanyu Pallavi Sudhir (Nov 22 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Scalar multiplication not defined for functions/near/148196682):
(also, should there be a coercion from `α` to `β → α` -- i.e. to constant functions?)

#### [Kevin Buzzard (Nov 22 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Scalar multiplication not defined for functions/near/148196749):
Chris Hughes suggested that importing pi_instances might fix this -- but it didn't seem to.

```lean
import data.real.basic
import algebra.module
import algebra.pi_instances

example : module ℝ ℝ := by apply_instance
example : has_scalar ℝ (ℝ → ℝ) := by apply_instance -- fails
```

`pi_instances` contains the line

```lean
instance module       (α) {r : ring α}           [∀ i, add_comm_group $ f i]  [∀ i, module α $ f i]       : module α (Π i : I, f i)       := {..pi.semimodule α}
```

#### [Kevin Buzzard (Nov 22 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Scalar multiplication not defined for functions/near/148196761):
```lean
import data.real.basic
import algebra.module
import algebra.pi_instances

example : module ℚ ℚ := by apply_instance
example : has_scalar ℚ (ℚ → ℚ) := by apply_instance -- fails

```

That fails too so it's not some decidable equality issue

