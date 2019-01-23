---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51786normnumbug.html
---

## Stream: [general](index.html)
### Topic: [norm_num bug](51786normnumbug.html)

---


{% raw %}
#### [ Calle Sönne (Nov 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147321656):
Here is what I think is a bug in norm_num:
```lean
import tactic.norm_num
import analysis.real

example : ((8 : ℕ) : ℝ) < 9 := by norm_num
```
"tactic failed"

#### [ Simon Hudon (Nov 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147389627):
@**Mario Carneiro** is norm_num supposed to handle coercions?

#### [ Mario Carneiro (Nov 09 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147393172):
no, or at least it has not been extended to coercions

#### [ Simon Hudon (Nov 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147448343):
That could be a nice feature

#### [ Kevin Buzzard (Nov 10 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147448668):
In the mean time, following the tips at https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md, you can always do this:

```lean
import tactic.norm_num
import analysis.real

example : ((8 : ℕ) : ℝ) < 9 := begin
  rw (show ((8 : ℕ) : ℝ) = (8 : ℝ), by simp),
  norm_num
end
```

#### [ Nicholas Scheel (Nov 11 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147475448):
I once made a stupid tactic to do exactly this: https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean

#### [ Nicholas Scheel (Nov 11 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147475536):
you can also do the same with `rat`


{% endraw %}
