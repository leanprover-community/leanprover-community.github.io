---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06120tactictoexpr.html
---

## Stream: [general](index.html)
### Topic: [tactic.to_expr](06120tactictoexpr.html)

---

#### [Edward Ayers (Dec 11 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151462345):
How can I get `tactic.to_expr` to not apply metavariables to implicit arguments? That is;
``` lean
constant α : Type
axiom P : ∀ {a:α}, a = a
run_cmd do
    p ← tactic.resolve_name `P,
    e ← tactic.to_expr p,
    t ← tactic.infer_type e,
    trace t,  -- gives "?m_1 = ?m_1"
    pure ()
```
I really want to find a way of getting `trace t` to say `∀ {a:α}, a = a` given only the declaration name `P`

#### [Reid Barton (Dec 11 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468593):
Do you need to go through `to_expr`?

#### [Rob Lewis (Dec 11 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468620):
`e ← tactic.to_expr p.mk_explicit` should work for this case.

#### [Reid Barton (Dec 11 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468935):
I was going to suggest
```lean
run_cmd do
    d ← get_decl `P,
    trace d.type,
    pure ()
```

#### [Rob Lewis (Dec 11 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151470588):
Yeah, that's better here, although I guess it depends on the real context.

