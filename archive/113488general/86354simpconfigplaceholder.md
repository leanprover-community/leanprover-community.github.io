---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86354simpconfigplaceholder.html
---

## Stream: [general](index.html)
### Topic: [simp_config placeholder](86354simpconfigplaceholder.html)

---

#### [Sean Leather (Oct 01 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_config%20placeholder/near/134955856):
I just discovered this by accident:

```lean
example : ℕ := by simp _
```

```lean
error: don't know how to synthesize placeholder
context:
⊢ opt_param tactic.simp_config_ext
    {to_simp_config := {max_steps := simp.default_max_steps,
                        contextual := ff,
                        lift_eq := tt,
                        canonize_instances := tt,
                        canonize_proofs := ff,
                        use_axioms := tt,
                        zeta := tt,
                        beta := tt,
                        eta := tt,
                        proj := tt,
                        iota := tt,
                        iota_eqn := ff,
                        constructor_eq := tt,
                        single_pass := ff,
                        fail_if_unchanged := tt,
                        memoize := tt},
     discharger := tactic.failed unit}
```

#### [Reid Barton (Oct 01 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_config%20placeholder/near/134961539):
Nice! `rw [] _` also works to see `rw` options.

