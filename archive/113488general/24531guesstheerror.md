---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24531guesstheerror.html
---

## [general](index.html)
### [guess the error](24531guesstheerror.html)

#### [Kevin Buzzard (Mar 29 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124371146):
```
theorem  easy : let H : 0  <  2  := dec_trivial in
(⟨0,H⟩ : fin 2) = ⟨0,H⟩ := rfl
```

#### [Gabriel Ebner (Mar 29 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124372404):
Ah, I guess there are two ways in which a lemma can fail to be rfl: either the proof is not rfl, or the proposition is not an equation.

#### [Gabriel Ebner (Mar 29 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124372463):
Note that `easy` would not work as a simp lemma, since it matches on the `let` instead of the `fin.mk` (and the exact decidability proof):
```lean
#eval simp_lemmas.mk.add_simp ``easy >>= simp_lemmas.pp >>= tactic.trace
-- simplification rules for iff
-- [easy] #0, let H : 0 < 2 := _ in ⟨0, H⟩ = ⟨0, H⟩ ↦ true
```

#### [Gabriel Ebner (Mar 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124372537):
To explain: `lemma foo : ... = ... := rfl` is only intended to be used for simp-lemmas.  And then it *literally* needs to be `rfl` on the right-hand side.  Not `eq.refl _`, not `by refl`, but `rfl`.

#### [Gabriel Ebner (Mar 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124372551):
So in your case you can just use `by refl` or `eq.refl _` and `easy` will work.

#### [Kevin Buzzard (Mar 29 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124376162):
So this let isn't just syntactic sugar?

#### [Sebastian Ullrich (Mar 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess the error/near/124417030):
No, let is a primitive term kind supported by the kernel

