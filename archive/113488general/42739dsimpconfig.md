---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42739dsimpconfig.html
---

## [general](index.html)
### [dsimp_config](42739dsimpconfig.html)

#### [Edward Ayers (Oct 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/135537467):
Please could someone help me fill in these holes in the docstring for `dsimp_config`?
```lean
structure dsimp_config :=
(md                        := reducible) -- reduction mode: how aggressively constants are replaced with their definitions.
(max_steps : nat           := simp.default_max_steps) -- The maximum number of steps allowed before failing.
(canonize_instances : bool := tt) -- [TODO] ??? 
(single_pass : bool        := ff) -- [TODO] Does this mean that _each_ simp-lemma can only be used once?
(fail_if_unchanged         := tt) -- Don't throw if simp didn't do anything.
(eta                       := tt) -- allow eta-equivalence: `(λ x, F $ x) ↝ F`
(zeta : bool               := tt) -- do zeta-reductions: `let x : a := b in c ↝ c[x/b]`.
(beta : bool               := tt) -- do beta-reductions: `(λ x, E) $ (y) ↝ E[x/y]`.
(proj : bool               := tt) -- reduce projections: `⟨a,b⟩.1 ↝ a` [TODO] I think?
(iota : bool               := tt) -- reduce recursors for inductive datatypes: eg `nat.rec_on (succ n) Z R ↝ R n $ nat.rec_on n Z R`
(unfold_reducible          := ff) -- if tt, definitions with `reducible` transparency will be unfolded (delta-reduced)
(memoize                   := tt) -- [TODO] what is being memoised?
```

#### [Edward Ayers (Oct 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/135537599):
(I'm working through `init/meta` in the Lean source and adding all the missing docstrings)

#### [Chris Hughes (Nov 15 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147772589):
@**Edward Ayers** Is a copy of your Lean with docstring available online anywhere? It would be really useful.

#### [Edward Ayers (Nov 16 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809879):
https://github.com/EdAyers/lean

#### [Edward Ayers (Nov 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809934):
Checkout the `doc` branch

#### [Edward Ayers (Nov 16 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809977):
I use the build from that branch as my main lean executable

#### [Patrick Massot (Nov 16 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810027):
Do you mean you added stuff besides docstrings?

#### [Edward Ayers (Nov 16 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810032):
No I haven't added anything except docstrings on that branch

#### [Edward Ayers (Nov 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810043):
(hopefully, no guarantees)

#### [Edward Ayers (Nov 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810057):
It builds mathlib though so its probably fine. I didn't sneak in `false` as an axiom anywhere.

#### [Edward Ayers (Nov 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810108):
I also can't guarantee that the docstrings I added aren't misleading, they are more a side-effect of me trying to understand the sourcecode

#### [Chris Hughes (Nov 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810263):
Thanks @**Edward Ayers**

