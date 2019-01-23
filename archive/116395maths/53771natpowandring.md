---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53771natpowandring.html
---

## Stream: [maths](index.html)
### Topic: [nat.pow and ring](53771natpowandring.html)

---

#### [Kevin Buzzard (Jun 09 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802027):
```lean
import tactic.ring 

example (d : ℕ) : d ^ 2 + (2 * d + 1) = (d + 1) ^ 2 := 
begin 
  unfold has_pow.pow monoid.pow nat.pow,
  ring
end
```

#### [Kevin Buzzard (Jun 09 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802028):
Could I have done that in one line with `ring`? [using some options or something]

#### [Andrew Ashworth (Jun 09 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802751):
[deleted - incorrect information]

#### [Kevin Buzzard (Jun 09 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802943):
So I could make an even cooler ring tactic by writing a tactic which tries to do those unfolds and then applies ring?

#### [Kevin Buzzard (Jun 09 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802946):
Is life that easy?

#### [Andrew Ashworth (Jun 09 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127803089):
[deleted - incorrect information]

#### [Andrew Ashworth (Jun 09 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127803099):
[deleted - incorrect information]

#### [Mario Carneiro (Jun 09 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127808199):
ring should handle powers... it automatically handles ring like operations that make sense as polynomial expressions, although it can't handle x^n for nonconstant n

#### [Mario Carneiro (Jun 09 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127808250):
in particular it has optimizations for sparse polynomials like x^100 + x, which requires interpreting ^

#### [Andrew Ashworth (Jun 09 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127809868):
that's pretty sweet! I didn't expect that you'd put that much effort into the tactic. thanks for writing it!

#### [Kevin Buzzard (Jun 09 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816599):
Yes thanks very much indeed for writing it. It is an essential part of the "mathematician's interface" to Lean. Writing it was I'm sure nontrivial but at the end of the day, as I know I've said before, if a mathematician can't prove things like the example above with one or two lines then they will never take to Lean.

#### [Kevin Buzzard (Jun 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816655):
Just to be clear -- in the example above `ring` falls without the initial unfolding

#### [Patrick Massot (Jun 09 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816664):
The `ring` tactic is already very useful but it has bugs

#### [Johan Commelin (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127822932):
How hard would it be to state a theorem about the `ring` tactic, and prove that the implementation is compliant? Then we are sure we won't have bugs. But I guess that the `meta` stuff makes this complicated.

