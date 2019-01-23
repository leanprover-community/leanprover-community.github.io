---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70963Simplifyingnestedlambdaexpressions.html
---

## Stream: [general](index.html)
### Topic: [Simplifying nested lambda expressions](70963Simplifyingnestedlambdaexpressions.html)

---

#### [Ken Roe (Jan 12 2019 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958159):
It appears that "simp" is not completely robust.  How do I get the following simplification to work?
```lean
theorem beta_r {y:ℕ → ℕ} : (λ (q:ℕ) (z:ℕ), y z)=(λ (r:ℕ), y) :=
begin
    simp
end
```

#### [Bryan Gin-ge Chen (Jan 12 2019 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958482):
The simp seems to work for me. What version of lean are you using / what else do you have in the file?

#### [Bryan Gin-ge Chen (Jan 12 2019 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958593):
The `squeeze_simp` tactic in mathlib's `tactic.squeeze` tells me that `simp only [eq_self_iff_true]` ought to work too.

#### [Ken Roe (Jan 12 2019 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154959050):
I'm using Lean 3.4.1.  Should I update?

#### [Ken Roe (Jan 12 2019 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154959131):
It does work--I realized I need to type a "," after the "simp" to see the reduction show up in the editor.

