---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70542intcoenatmulisntnatcastmul.html
---

## Stream: [maths](index.html)
### Topic: [int.coe_nat_mul isn't nat.cast_mul](70542intcoenatmulisntnatcastmul.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 01 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130677240):
```lean
#check @int.coe_nat_mul -- int.coe_nat_mul : ∀ (m n : ℕ), ↑(m * n) = ↑m * ↑n -- this is in ℤ
#check @nat.cast_mul -- nat.cast_mul : ∀ {α : Type u_1} [_inst_1 : semiring α] (m n : ℕ), ↑(m * n) = ↑m * ↑n
example : semiring ℤ := by apply_instance -- fine

example (m n : ℕ) : (↑(m * n):ℤ) = ↑m * ↑n := nat.cast_mul m n -- fails

/- full error with pp.all true:
synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  @coe_to_lift.{1 1} nat int (@coe_base.{1 1} nat int int.has_coe)
inferred
  @coe_to_lift.{1 1} nat int
    (@coe_base.{1 1} nat int
       (@nat.cast_coe.{0} int (@mul_zero_class.to_has_zero.{0} int (@semiring.to_mul_zero_class.{0} int int.semiring))
          (@monoid.to_has_one.{0} int (@semiring.to_monoid.{0} int int.semiring))
          (@distrib.to_has_add.{0} int (@semiring.to_distrib.{0} int int.semiring))))
-/
```

It seems that the coercion from nat to int isn't the one from nat to a general semiring. This means that I am having to write a bunch of functions twice, e.g.

```lean
theorem nat.cast_pow {α : Type*} [semiring α] (n : ℕ) : ∀ m : ℕ, (n : α) ^ m = (n ^ m : ℕ)
| 0 := nat.cast_one.symm
| (d+1) := show ↑n * ↑n ^ d = ↑(n ^ d * n), by rw [nat.cast_pow,mul_comm,nat.cast_mul]

theorem nat.cast_pow' (n : ℕ) : ∀ m : ℕ, (n : ℤ) ^ m = (n ^ m : ℕ)
| 0 := nat.cast_one.symm
| (d+1) := show ↑n * ↑n ^ d = ↑(n ^ d * n), by rw [nat.cast_pow',mul_comm,int.coe_nat_mul]
```

Maybe the last one should be `int.coe_nat_pow` or something? Am I missing a trick? I'm trying to move smoothly between the naturals, the integers, and the integers mod p.

#### [ Kevin Buzzard (Aug 01 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130677411):
[I'm threatening to add some of these functions to my brief `nat` PR by the way]

#### [ Mario Carneiro (Aug 01 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130682881):
Yes. There are two coercions from N to Z, with different names. They are proven the same, so given one theorem the other isn't far away, but you have to have both sets of theorems

#### [ Mario Carneiro (Aug 01 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130682992):
There are also two power functions N -> N -> N, with different names, the specialization of `monoid.pow` and `nat.pow`, again they are proven the same and a simp lemma will translate one to the other

#### [ Mario Carneiro (Aug 01 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130683031):
In both cases you can put the blame on the fact that the special case is defined in lean core and mathlib can't undefine it, although I'm not sure I would remove `int.coe_nat` if I could


{% endraw %}
