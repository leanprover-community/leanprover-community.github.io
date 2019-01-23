---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55897rwfails.html
---

## Stream: [general](index.html)
### Topic: [rw fails](55897rwfails.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 24 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286611):
What have I done wrong here?

```lean
import data.real.basic

class real.nat (r : ℝ) :=
(n : ℕ)
(pf : r = ↑n)

class real.rat (r : ℝ) :=
(q : ℚ)
(pf : r = ↑q)

set_option trace.check true
instance real.rat_of_nat (r : ℝ) [H : real.nat r] : real.rat r :=
⟨(H.n : ℚ),begin
  have H2 := H.pf,
  rw H2, -- fails
/-
  rewrite tactic failed, motive is not type correct
nested exception message:
check failed, application type mismatch (use 'set_option trace.check true' for additional details)
state:
r : ℝ,
H : real.nat r,
H2 : r = ↑(nat.n r)
⊢ r = ↑↑(nat.n r)
-/
  sorry 
end⟩
```

Setting `trace.check` to `true` tells me

```
[check] application type mismatch at
  nat.n _a
argument type
  real.nat r
expected type
  real.nat _a
```

#### [ Kenny Lau (Nov 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286682):
well the second `r` is also being rewrited

#### [ Chris Hughes (Nov 24 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286695):
`H` is an implicit argument in the rhs of `H2`, and it will have the wrong type after the `r` on the rhs is rewritten.

#### [ Kenny Lau (Nov 24 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286760):
```lean
import data.real.basic

class real.nat (r : ℝ) :=
(n : ℕ)
(pf : r = ↑n)

class real.rat (r : ℝ) :=
(q : ℚ)
(pf : r = ↑q)

instance real.rat_of_nat (r : ℝ) [H : real.nat r] : real.rat r :=
⟨H.n, by rw rat.cast_coe_nat H.n; exact H.pf⟩
```

#### [ Johan Commelin (Nov 24 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286776):
Are there simp-lemmas that reduce these double coercions?

#### [ Kenny Lau (Nov 24 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286819):
sure

#### [ Johan Commelin (Nov 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286956):
So, `by simpa using H.pf`?

#### [ Kenny Lau (Nov 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286967):
je kant het proberen... toch


{% endraw %}
