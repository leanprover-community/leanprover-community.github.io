---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77891ratmkeq.html
---

## [general](index.html)
### [rat.mk_eq](77891ratmkeq.html)

#### [Kenny Lau (Apr 25 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125675114):
```lean
theorem mk_eq : ∀ {a b c d : ℤ} (hb : b ≠ 0) (hd : d ≠ 0),
  a /. b = c /. d ↔ a * d = c * b :=
suffices ∀ a b c d hb hd, mk_pnat a ⟨b, hb⟩ = mk_pnat c ⟨d, hd⟩ ↔ a * d = c * b,
[...]
```

#### [Kenny Lau (Apr 25 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125675152):
the one in `suffices` is what I need T_T

#### [Mario Carneiro (Apr 25 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680601):
Just rewrite `mk_pnat` into `/.`, they are equal

#### [Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680649):
this is what I did at the end:
```lean
theorem rat.mk_pnat_eq_iff (a b c d) : rat.mk_pnat a b = rat.mk_pnat c d ↔ a * d = c * b :=
begin
  cases b with b hb, cases d with d hd,
  simp [rat.mk_pnat_eq],
  rw [rat.mk_eq],
  exact ne_of_gt (int.coe_nat_pos.2 hb),
  exact ne_of_gt (int.coe_nat_pos.2 hd),
end
```

#### [Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680667):
this part of the code is not going to be PR'd so the neatness of the proof doesn't really matter ot me

#### [Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680671):
but I did write a whole bunch of lemmas in the meantime

#### [Mario Carneiro (Apr 25 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680795):
The real question is why are you dealing with `mk_pnat`? The interface should let you just use field operations and avoid `mk` entirely

#### [Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680800):
oh, `mk_pnat` is not intended to be used?

#### [Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680838):
I used it because I am using `pnat`

#### [Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680843):
or are you going to tell me that `pnat` is not to be used either

#### [Mario Carneiro (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680914):
Just use `n / d` where `d : N+`

#### [Mario Carneiro (Apr 25 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680991):
The only reason you might want `mk_pnat` is if you care about the efficiency of computing this value (this will translate `d` to rat by adding ones)

