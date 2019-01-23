---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78526decidingifreflwouldwork.html
---

## Stream: [general](index.html)
### Topic: [deciding if `refl` would work](78526decidingifreflwouldwork.html)

---


{% raw %}
#### [ Scott Morrison (Apr 22 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526321):
I have `lhs rhs : expr`, and I would like to know, if the goal were to be `lhs = rhs`,  whether or not `refl` would succeed. I could temporarily make the goal actually `lhs = rhs`, and try `refl`, but I'm wondering if it can be done directly.

#### [ Scott Morrison (Apr 22 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526366):
I'm only hesitant to overwrite the goal because the actual current goal may be something completely unrelated to what my tactic is thinking about that the moment it's wondering about `lhs = rhs`, and it feels kludgy to actually have to use `set_goal`.

#### [ Scott Morrison (Apr 22 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526377):
The problem is that `refl` is basically just shorthand for ``mk_const `eq.refl >>= λ r, apply_core r``, and `apply_core` only unifies with the goal.

#### [ Sebastian Ullrich (Apr 22 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526830):
@**Scott Morrison** Take a look at `tactic.solve_aux`

#### [ Scott Morrison (Apr 22 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125527074):
Thanks @**Sebastian Ullrich**. Implicit in your answer is "get over it, just set_goal to whatever you want, it's how you're meant to do this"! Good to know.

#### [ Sebastian Ullrich (Apr 22 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125527212):
If you want to look at it like that, yes :)

#### [ Simon Hudon (Apr 22 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125530633):
What if you try to unify them directly? `unify lhs rhs`


{% endraw %}
