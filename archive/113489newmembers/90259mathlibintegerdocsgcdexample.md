---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/90259mathlibintegerdocsgcdexample.html
---

## Stream: [new members](index.html)
### Topic: [mathlib integer docs gcd example](90259mathlibintegerdocsgcdexample.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 09 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131176076):
The final `example` in [this file from the mathlib docs](https://github.com/leanprover/mathlib/blob/master/docs/theories/integers.md) (I guess it originally comes from [this page on the xena blog](https://xenaproject.wordpress.com/maths-in-lean-integers/)) doesn't seem to typecheck for me:
```lean
import data.nat.gcd
open nat 
example (m n : ℕ) : int.gcd m n = m * (gcd_a m n) + n * (gcd_b m n) := gcd_eq_gcd_ab
```
I get this:
```lean
type mismatch at application
  m * gcd_a m n
term
  gcd_a m n
has type
  ℤ
but is expected to have type
  ℕ
```
and something similar for the other summand.

#### [ Mario Carneiro (Aug 09 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131177735):
that should be
```
example (m n : ℕ) : (nat.gcd m n : ℤ) = m * (gcd_a m n) + n * (gcd_b m n) := gcd_eq_gcd_ab m n
```

#### [ Kevin Buzzard (Aug 09 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131177872):
[what Mario said]

#### [ Bryan Gin-ge Chen (Aug 09 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131178041):
Thanks! I was having trouble figuring out the fix by myself...

#### [ Patrick Massot (Aug 09 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131181859):
https://github.com/leanprover/mathlib/pull/244

#### [ Patrick Massot (Aug 09 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131181958):
It would be really nice to find a workflow making sure examples in the docs are correct. The manual way would be to copy them to a `tests/docs/` directory, and hope things will stay synced.

#### [ Patrick Massot (Aug 09 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131182072):
Thanks Mario! I wonder if this is my new merge time record. I already hit some similar score a long time ago.


{% endraw %}
