---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55167tacticringfeaturerequests.html
---

## Stream: [general](index.html)
### Topic: [tactic.ring feature requests](55167tacticringfeaturerequests.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 29 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124364059):
```
import tactic.ring
theorem  inductive_step (d : ℕ) : d ^ 2  + (2  * d +  1) = (succ d) ^ 2  :=
begin
-- ring doesn't work
unfold nat.pow,
-- ring doesn't work
rw succ_eq_add_one,
ring, -- works
end
```

#### [ Kevin Buzzard (Mar 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124364100):
I am in two minds about whether I need to tell mathematicians "obviously you need to unfold nat.pow and succ because they are not really to do with rings, which are all about + and *"

#### [ Kevin Buzzard (Mar 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124364102):
or whether I should just expect ring to deal with these

#### [ Kevin Buzzard (Mar 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124364104):
or whether it's even not possible to get ring to deal with these, for technical reasons I'm unaware of

#### [ Kevin Buzzard (Mar 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124364112):
@**Mario Carneiro**

#### [ Kevin Buzzard (Mar 29 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124368836):
```
import tactic.ring
open nat

def  odd : ℕ → ℕ :=  λ i, 2  * i +  1
def  square : ℕ → ℕ :=  λ i, i ^ 2

theorem  odd_square_inductive_step (d : ℕ) : square d + odd d = square (succ d)
:=  by {unfold square odd nat.pow,rw succ_eq_add_one,ring}
```

#### [ Kevin Buzzard (Mar 29 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124368842):
Why can't this just be `by ring`?

#### [ Kevin Buzzard (Mar 29 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.ring%20feature%20requests/near/124368920):
Can't I promise that I'll only ever call ring with an identity that can be formulated using only the axioms of a semiring?


{% endraw %}
