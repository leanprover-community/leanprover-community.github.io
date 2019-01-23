---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36244islinearmap.html
---

## Stream: [maths](index.html)
### Topic: [is_linear_map](36244islinearmap.html)

---

#### [Johan Commelin (Nov 22 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148162896):
Is there a reason why `is_linear_map` does not extend `is_add_group_hom`?

#### [Johan Commelin (Nov 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163165):
Here is what I'm trying to do:
```lean
import data.finset data.finsupp algebra.group
import algebra.group_power

universes u v w

namespace finsupp
noncomputable theory
local attribute [instance] classical.prop_decidable

variables {X Y : Type u} {M : Type v}

def linear_extension [add_comm_monoid M] (f : X → M → Y →₀ M) (s : X →₀ M) : Y →₀ M :=
s.sum $ f

namespace linear_extension

instance [add_comm_monoid M] {f : X → M → Y →₀ M} (h₁ : ∀ (x : X), f x 0 = 0) (h₂ : ∀ (x : X) (m₁ m₂ : M), f x (m₁ + m₂) = f x m₁ + f x m₂) :
is_add_monoid_hom $ linear_extension f :=
{ map_zero := rfl,
  map_add  := λ s₁ s₂, finsupp.sum_add_index h₁ h₂ }

instance [add_comm_group M] {f : X → M → Y →₀ M} (h : ∀ (x : X), is_add_group_hom $ f x) :
is_add_group_hom $ linear_extension f :=
{ add := (linear_extension.is_add_monoid_hom (λ x, is_add_group_hom.zero (f x)) (λ x, (h x).add)).map_add }

variables {R : Type w} [ring R] [add_comm_group M] [module R M]
include R

instance is_linear_map {f : X → M → Y →₀ M} (h : ∀ (x : X), @is_linear_map _ _ _ _ _ _ _ (finsupp.to_module _ _) $ f x) :
@is_linear_map _ _ _ _ _ _ (finsupp.to_module _ _) (finsupp.to_module _ _) $ linear_extension f :=
{ add := (linear_extension.is_add_group_hom (λ x, ⟨(h x).add⟩)).add, -- gives stupid error
  smul := _ }

end linear_extension

end finsupp
```

#### [Johan Commelin (Nov 22 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163178):
The error is:
```
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  to_module Y M
```

#### [Johan Commelin (Nov 22 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163749):
@**Mario Carneiro** Somehow the `@is_linear_map _ _ _ _ _ _ _` all over the place give me the feeling that I don't quite understand how to use modules.

#### [Mario Carneiro (Nov 22 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163772):
you shouldn't be using `is_linear_map` at all

#### [Johan Commelin (Nov 22 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163907):
So what should I use?

#### [Mario Carneiro (Nov 22 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163914):
`linear_map`

#### [Johan Commelin (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163971):
Ok, is there value in the other two instances? for add monoids/groups?

#### [Mario Carneiro (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163981):
but I understand that the reason you are getting these errors is because `finsupp.to_module` is not an instance

#### [Mario Carneiro (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163986):
you should try declaring it locally

#### [Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164159):
Ok, that helps.

#### [Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164169):
But I would like to use `linear_extension` in a context with and without modules.

#### [Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164172):
Am I trying to be  too flexible?

#### [Mario Carneiro (Nov 22 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164328):
no that's fine, you should just declare a wrapper for `linear_extension` making it into a linear map

#### [Johan Commelin (Nov 22 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164410):
But that is already there, right. You made `is_linear_map.mk'`. Or do you mean something else?

#### [Mario Carneiro (Nov 22 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164519):
I mean `linear_extension : linear_map A B`

#### [Johan Commelin (Nov 22 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164724):
But then it is no longer a function that can be a group hom if I'm not working with modules...

#### [Mario Carneiro (Nov 22 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164936):
you have another function for that; the function parts will be equal (even defeq)

#### [Johan Commelin (Nov 22 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148166197):
@**Mario Carneiro** Ok, I finally completed the proof. So what is your suggestion? I should have two different names? One for the unbundled, and one for the bundled linear map? Are there naming conventions for this?

#### [Kenny Lau (Nov 22 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148182128):
@**Johan Commelin** add `l` (that's a small `L`) in front of the name for the bundled version

#### [Kenny Lau (Nov 22 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148182132):
so e.g. the map is `mul` and the linear_map is `lmul`

