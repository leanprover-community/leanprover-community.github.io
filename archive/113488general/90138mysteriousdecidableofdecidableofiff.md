---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90138mysteriousdecidableofdecidableofiff.html
---

## [general](index.html)
### [mysterious decidable_of_decidable_of_iff](90138mysteriousdecidableofdecidableofiff.html)

#### [Sean Leather (Mar 01 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137155):
This is also peculiar. I came upon the following which didn't resolve with `refl` or `simp`:
```lean
⊢ ite (y = x) t₂ (varf y) = ite (y = x) t₂ (varf y)
```
Upon further inspection with `set_option pp.all true`, I found:
```lean
⊢ @eq.{1} (tts.typ V)
    (@ite.{1} (@eq.{1} V y x)
      (_inst_1 y x)
      (tts.typ V)
      t₂
      (@tts.typ.varf V y))
    (@ite.{1} (@eq.{1} V y x)
      (@decidable_of_decidable_of_iff (@eq.{1} V y x) (@eq.{1} V y x) (_inst_1 y x) (iff.refl (@eq.{1} V y x)))
      (tts.typ V)
      t₂
      (@tts.typ.varf V y))
```
Of course, the goal can be reached with:
```lean
by_cases h : y = x; simp [h]
```
But what I'm curious about is (1) why it's there in the first place and (2) why it isn't resolved with `refl` (why is it not defeq?).

My guess for (1) is that it came from one of the [`congr` theorems in `library/init/logic.lean`](https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/library/init/logic.lean#L882-L891).

As for (2), I tried adding:
```lean
@[simp] theorem decidable_of_decidable_of_iff_refl :
  ∀ (d : decidable p), decidable_of_decidable_of_iff d (iff.refl p) = d
| (is_true _)  := rfl
| (is_false _) := rfl
```
and:
```lean
simp [decidable_of_decidable_of_iff_refl _]
```
but nothing changed, and `decidable_of_decidable_of_iff_refl` didn't show up with `set_option trace.simplify true`.

#### [Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137356):
simp only allows you to rewrite at positions that you can "reach" via congruence lemmas.  Since congruence lemmas typically skip subsingletons (such as decidability instances), you can't simp there.

#### [Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137363):
`rw decidable_of_decidable_of_iff_refl` could work

#### [Sean Leather (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137364):
`rw decidable_of_decidable_of_iff_refl _, apply_instance` works

#### [Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137370):
Have you tried `congr` on the original goal?

#### [Sean Leather (Mar 01 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137425):
Ah, that works.

#### [Sebastian Ullrich (Mar 01 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137435):
I suppose this shows that simp should really use refl as a rule instead of just at the very end

#### [Sebastian Ullrich (Mar 01 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137448):
Then it should be able to close that goal together with if_congr

#### [Gabriel Ebner (Mar 01 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137511):
@**Sebastian Ullrich** Can you elaborate on how refl would work here?  Neither side of the equation can be simplified, not even with refl.  AFAICT the only thing that would help is if simp applied the congruence lemmas to the equation (like backchaining).

#### [Sebastian Ullrich (Mar 01 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious decidable_of_decidable_of_iff/near/123137706):
@**Gabriel Ebner** You're right, I was confused about the role of congr lemmas in simp

