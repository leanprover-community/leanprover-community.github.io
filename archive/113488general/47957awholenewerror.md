---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47957awholenewerror.html
---

## Stream: [general](index.html)
### Topic: [a whole new error](47957awholenewerror.html)

---


{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483415):
```lean
invalid pattern, 'choice (frozen_name multiset.cons) (frozen_name list.cons)' is overloaded, and this kind of overloading is not currently supported in patterns
```

#### [ Mario Carneiro (Apr 21 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483454):
use a local notation

#### [ Mario Carneiro (Apr 21 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483456):
what did you write to get that?

#### [ Kenny Lau (Apr 21 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483501):
```lean
theorem reduce.not : ∀ {L₁ L₂ L₃ : list (α × bool)} (x b), reduce L₁ = L₂ ++ (x, b) :: (x, bnot b) :: L₃ → false
| [] [] L3 _ _ H := by injections
| [] [hd] L3 _ _ H := by injections
| ((x,b)::hd1) L2 L3 _ _ H := by dsimp at H;
  exact match reduce hd1 with
  | [] := by dsimp at H
  | (x2,b2)::hd2 := _
  end
```

#### [ Mario Carneiro (Apr 21 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483556):
does it help to use `((x2,b2)::hd2 : list _)` instead?

#### [ Kenny Lau (Apr 21 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483605):
well, it doesn't, but list.cons worked

#### [ Mario Carneiro (Apr 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484552):
```
theorem reduce.not : ∀ (L₁ L₂ L₃ : list (α × bool)) (x b), reduce L₁ ≠ L₂ ++ (x, b) :: (x, bnot b) :: L₃
| [] L2 L3 _ _ := λ h, by simpa using (list.append_eq_nil.1 h.symm).2
| ((x,b)::L1) L2 L3 x' b' := begin
  dsimp [reduce],
  cases r : reduce L1,
  { dsimp [reduce], intro h,
    have := congr_arg list.length h,
    simp [-add_comm] at this,
    exact absurd this dec_trivial },
  cases hd with y c,
  by_cases x = y ∧ ¬b = c; simp [reduce, h]; intro H,
  { rw H at r,
    exact reduce.not L1 ((y,c)::L2) L3 x' b' r },
  rcases L2 with _|⟨a, L2⟩,
  { injections, substs x' y c b',
    refine h ⟨rfl, _⟩,
    cases b; exact dec_trivial },
  { refine reduce.not L1 L2 L3 x' b' _,
    injection H with _ H,
    rw [r, H], refl }
end
```
ah, I couldn't help myself

#### [ Kenny Lau (Apr 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484554):
thanksssss

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484611):
and I just realized that I only have two interface theorems

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484612):
and I don't have to change the rest

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484613):
which is again a testimony of the theory of interface


{% endraw %}
