---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/75284subringvssubmodule.html
---

## [maths](index.html)
### [subring vs submodule](75284subringvssubmodule.html)

#### [Patrick Massot (Oct 09 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/135464064):
Let me bring up old news since it looks like the module refactor is almost done. The following works nicely:
```lean
import ring_theory.subring

variables {R : Type} [comm_ring R] (S : set R) [is_subring S]

example : comm_ring S := by apply_instance
example : has_add S := by apply_instance
```
Now add `import linear_algebra.quotient_module` at top, and the second example no-longer works. In particular this breaks the cast from nat to S. Is this fixed in the module refactor?

#### [Patrick Massot (Nov 03 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/137121150):
Let me bring up that thread. Kenny or Mario, do you think this problem is now fixed by the module refactor?

#### [Kenny Lau (Nov 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/137122003):
`linear_algebra.quotient_module` is deleted (and its content is migrated to `linear_algebra.basic`), so I imported that instead, and it worked

