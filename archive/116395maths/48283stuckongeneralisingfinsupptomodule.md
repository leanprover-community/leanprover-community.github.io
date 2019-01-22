---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48283stuckongeneralisingfinsupptomodule.html
---

## [maths](index.html)
### [stuck on generalising finsupp.to_module](48283stuckongeneralisingfinsupptomodule.html)

#### [Johan Commelin (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127201824):
I really don't see why I'm getting stuck here. See the two comment lines just after the first `sorry`.
```lean
/- should this be stronger? [module γ β] → module γ (α →₀ β) -/   -- yes!
def to_module [decidable_eq γ] [ring β] [module β γ] : module β (α →₀ γ) :=
{ smul     := begin
                intros r f,
                apply f.map_range ((•) r) _,
                simp
              end, -- (•)
  smul_add := begin
                intros r f g,
                apply finsupp.ext,
                intro a,
                simp,
                rw smul_add,
                sorry
  end, -- assume a x y, finsupp.ext $ by simp [mul_add], -- original
  -- assume a x y, finsupp.ext $ by simp [map_range,smul_add], -- why doesn't this one work? <=====
  add_smul := sorry, --assume a x y, finsupp.ext $ by simp [add_mul],
  one_smul := assume x, finsupp.ext $ by simp,
  mul_smul := assume r s x, finsupp.ext $ by simp [mul_smul],
  .. finsupp.add_comm_group }
```

#### [Johan Commelin (May 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127202256):
Never mind. I just realised that `is_linear_map` is not a class. Not going down the rabbit hole of modules.

#### [Kenny Lau (May 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127202261):
`linear_map` is

#### [Johan Commelin (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127202328):
And where does that beast live?

#### [Johan Commelin (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127202329):
not in algebra/module

#### [Johan Commelin (May 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck on generalising finsupp.to_module/near/127202473):
Ok, I found it... thanks!

