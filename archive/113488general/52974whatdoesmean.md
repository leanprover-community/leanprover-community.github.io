---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52974whatdoesmean.html
---

## [general](index.html)
### [what does . mean?](52974whatdoesmean.html)

#### [Kenny Lau (Apr 16 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129469):
```
type mismatch at application
  Exists.intro property_w property_h
term
  property_h
has type
  (λ (a : G), left_coset a (stab G X x)) property_w = val
but is expected to have type
  . (λ (y : G), (λ (a : G), left_coset a (stab G X x)) y = _x) property_w

#### [Kenny Lau (Apr 16 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129471):
what does the mystic `.` on the start of the last line mean?

#### [Simon Hudon (Apr 16 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129524):
That looks like a typo in the error message. If you ignore it, does the expression make sense?

#### [Kenny Lau (Apr 16 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129525):
a typo in the error message?

#### [Simon Hudon (Apr 16 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129527):
Yeah, someone had to type that error message in the code. They may have made a mistake.

#### [Kenny Lau (Apr 16 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129569):
it still doesn't make much sense

#### [Kenny Lau (Apr 16 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129572):
```
theorem orbit_equiv_stab_cosets (x : X) : nonempty (orbit G X x ≃ left_cosets (stab G X x)) :=
nonempty.intro $
@equiv.of_bijective _ _ (orbit_to_stab_cosets G X x) $
and.intro
  (λ ⟨y1, g1, h1⟩ ⟨y2, g2, h2⟩ H, subtype.eq $ h1.symm.trans $ (((set.set_eq_def _ _).1 $ subtype.mk.inj H) g1).1 h1)
  (λ ⟨gH, g, h⟩, ⟨⟨g ● x, _, rfl⟩, subtype.eq $ h ▸ (set.ext $ λ z, by simp [mem_left_coset_iff]; admit)⟩)

#### [Kenny Lau (Apr 16 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129573):
I don't have `property_h` anywhere

#### [Simon Hudon (Apr 16 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125129674):
Do you have a proof of an existential quantification somewhere in there?

#### [Mario Carneiro (Apr 16 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20does%20.%20mean%3F/near/125130200):
the `.` there is the pp printing of an inaccessible pattern. I'm not exactly sure what you are looking at, but you can safely ignore it

