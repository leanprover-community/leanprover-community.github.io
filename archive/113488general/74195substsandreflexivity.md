---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74195substsandreflexivity.html
---

## Stream: [general](index.html)
### Topic: [substs and reflexivity](74195substsandreflexivity.html)

---


{% raw %}
#### [ Sean Leather (Aug 20 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substs%20and%20reflexivity/near/132442829):
It seems like `subst` solves a reflexive goal but `substs` does not. If I replace `subst p, subst q`with `substs p q`, I have to add `refl` to solve the goal.

Looking at the definition of the interactive `subst`, I can see why:

```lean
meta def subst (q : parse texpr) : tactic unit :=
i_to_expr q >>= tactic.subst >> try (tactic.reflexivity reducible)
```

So the documentation on `substs` is not quite correct:

```lean
/-- Multiple subst. `substs x y z` is the same as `subst x, subst y, subst z`. -/
meta def substs (l : parse ident*) : tactic unit :=
l.mmap' (λ h, get_local h >>= tactic.subst)
```

Is it enough to add ` >> try (tactic.reflexivity reducible)` to the end of the `substs` definition to recoup this feature? Is there any reason why we shouldn't do this?


{% endraw %}
