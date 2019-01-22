---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72538LongStoneCech.html
---

## [maths](index.html)
### [Long Stone-Cech](72538LongStoneCech.html)

#### [Patrick Massot (Jan 22 2019 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598228):
@**Reid Barton** https://github.com/leanprover/mathlib/blob/master/src/topology/stone_cech.lean#L253 takes forever to elaborate. Do you care if I change it to:
```lean
instance stone_cech.t2_space : t2_space (stone_cech α) :=
begin
  rw t2_iff_ultrafilter,
  rintros g ⟨x⟩ ⟨y⟩ u gx gy,
  apply quotient.sound,
  intros γ tγ h₁ h₂ f hf,
  resetI,
  let ff := stone_cech_extend hf,
  change ff ⟦x⟧ = ff ⟦y⟧,
  have lim : ∀ z : ultrafilter α, g ≤ nhds ⟦z⟧ → tendsto ff g (nhds (ff ⟦z⟧)) :=
  assume z gz,
    calc map ff g ≤ map ff (nhds ⟦z⟧) : map_mono gz
              ... ≤ nhds (ff ⟦z⟧) : (continuous_stone_cech_extend hf).tendsto _,
  exact tendsto_nhds_unique u.1 (lim x gx) (lim y gy)
end
```

#### [Patrick Massot (Jan 22 2019 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598235):
which I think is also easier to read by the way

#### [Reid Barton (Jan 22 2019 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598456):
If it's faster go for it

#### [Patrick Massot (Jan 22 2019 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598640):
Thanks. I'm asking because this change will be hidden in a large reorganization PR (the second phase of the topology reorganization decided in Amsterdam).

#### [Reid Barton (Jan 22 2019 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598653):
Oh great, are you already working on that?

#### [Patrick Massot (Jan 22 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156598677):
Yes. I'm splitting `topology.basic` and `topology.continuity`

#### [Patrick Massot (Jan 22 2019 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long Stone-Cech/near/156599697):
And guess what I learned? Non-finishing calls to `simp` are evil

