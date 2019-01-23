---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18934instance.html
---

## Stream: [general](index.html)
### Topic: [instance](18934instance.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 13 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132041055):
`algebra/module.lean`:
```lean
instance range {f : β → γ} (hf : is_linear_map f) : is_submodule (set.range f) :=
by rw [← set.image_univ]; exact is_submodule.image hf
```
should this be an instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132041241):
no good, unless `is_linear_map` is a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132043377):
what to do about it then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132043635):
fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Guy Leroy (Aug 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121087):
I'm struggling with instances, I have the error:
failed to synthesize type class instance for
```lean 
a n : ℕ,
_inst_1 : pos_nat n,
em : coprime a n
⊢ decidable_eq (coprime a n → Π [_inst_1 : pos_nat n], units (zmod n))
```
How should I state the instance that would solve this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121699):
You should give us more context, this goal is probably not what you actually want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121881):
While I agree with patrick, I doubt that this is the right goal to solve, it is incidentally provable. Probably the missing piece is `decidable (pos_nat n)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Guy Leroy (Aug 14 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121916):
Thanks Patrick, you're right, I made a mistake when writing my goal and it's all fixed now.
I would still be curious as to what this instance actually means.
As for the context I wrote 
```lean
have : (units_zmod_mk a n) ^ order_of (units_zmod_mk a n), from pow_order_of_eq_one (units_zmod_mk a n),
```
instead of 
```lean
have  : (units_zmod_mk a n em) ^ order_of (units_zmod_mk a n em) = 1, from pow_order_of_eq_one (units_zmod_mk a n em),
```
and I have defined above 
```lean
def units_zmod_mk (a n : ℕ ) (h : nat.coprime a n) [pos_nat n] : units (zmod n) := 
{
    val := a,
    inv := a⁻¹,
    val_inv := by rw [mul_inv_eq_gcd n a, coprime.gcd_eq_one h];dsimp;rw zero_add,
    inv_val := by rw [mul_comm, mul_inv_eq_gcd n a, coprime.gcd_eq_one h];dsimp;rw zero_add,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Guy Leroy (Aug 14 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121924):
Okay thanks Mario

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132122004):
I assume the `decidable_eq` goal is coming from `order_of`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Guy Leroy (Aug 14 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132122352):
Very well thanks, I'm slowly trying to get a grasp of instances


{% endraw %}
