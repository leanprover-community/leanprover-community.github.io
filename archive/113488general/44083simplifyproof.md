---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44083simplifyproof.html
---

## Stream: [general](index.html)
### Topic: [simplify_proof](44083simplifyproof.html)

---

#### [Scott Morrison (Jun 06 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify_proof/near/127646386):
At some point Mario told me how to write a "simplify_proof" tactic, but in my fiddling with it I seem to have lost the essential magic step where the new, simplified proof is actually installed in place of the original proof:
````
open tactic
meta def simplify_proof {α} (tac : tactic α) : tactic α :=
λ s,
  let tac1 : tactic (α × expr) := do
    a ← tac,
    r ← result,
    lems ← simp_lemmas.mk_default,
    dr ← (lems.dsimplify [] r <|> pure r),
    pure (a, dr) in
match tac1 s with
| result.success (a, r) s' := (result >>= unify r >> pure a) s'
| result.exception msg e s' := result.exception msg e s'
end
````

#### [Scott Morrison (Jun 06 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify_proof/near/127646390):
Or am I misunderstanding what this should do?

#### [Scott Morrison (Jun 06 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify_proof/near/127646595):
Ah, got it! Somewhere along the way I put a spurious ' at the end of the `result.success` line, preventing the tactic from doing its time travel trick.

#### [Kevin Buzzard (Jun 06 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify_proof/near/127646896):
I sometimes wonder what `simp` is doing, and I know that I can look, but I can never be bothered. I vaguely suspect there might be times where replacing a call to `simp` with a call to what it actually does might be better -- am I just living in a dream world do you think? (in the sense that it's unlikely to make any noticeable difference other than obfusctating my code?)

