---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53580calctactic.html
---

## Stream: [general](index.html)
### Topic: [calc tactic](53580calctactic.html)

---

#### [Mario Carneiro (Jan 02 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178076):
I just noticed that `calc` is an interactive tactic which somehow unfolds to `exact calc` by magic
```lean
example (x : ℕ) : x + 0 = x :=
begin
  calc x + 0 = 0 + x : add_comm _ _
         ... = x : zero_add _
end
```

#### [Mario Carneiro (Jan 02 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178117):
I'm not sure exactly how this works, since `tactic.interactive.calc` doesn't exist

#### [Mario Carneiro (Jan 02 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178355):
yep, it's hardcoded - `calc` turns into `exact calc` (https://github.com/leanprover/lean/blob/master/src/frontends/lean/tactic_notation.cpp#L273-L276)

