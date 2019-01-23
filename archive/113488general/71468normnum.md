---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71468normnum.html
---

## Stream: [general](index.html)
### Topic: [norm_num](71468normnum.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 03 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797276):
I was under the impression that `norm_num` was always successful in its range of expertise. Here is a real-life counterexample:
```lean
lemma crazy (k l : ℕ) (h : l ≤ k): ((2:real)⁻¹)^k ≤ (2⁻¹)^l :=
begin
  apply pow_le_pow_of_le_one _ _ h,
  norm_num,
  -- goal is 2⁻¹ ≤ 1
  norm_num  
end
```
The last `norm_num` call gives rise to a deterministic timeout. Replacing it with `show 2⁻¹ ≤ (1 : real), by norm_num` works fine, so this is not really a problem for me, but still surprising.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 03 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797777):
```lean
import data.real.basic tactic.norm_num

lemma crazy (k l : ℕ) (h : l ≤ k): ((2:real)⁻¹)^k ≤ (2⁻¹)^l :=
begin
  apply pow_le_pow_of_le_one _ _ h,
    norm_num,
  -- goal is 2⁻¹ ≤ 1
  show (2⁻¹ : ℝ) ≤ 1,
  norm_num,
end
```

I've seen this before, but don't remember why it's happening.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797846):
`norm_num` is fighting with `simp`. Compare with `norm_num1, simp, norm_num1, simp,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797854):
which is basically what `norm_num` does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 03 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798112):
Does it mean that it would be more safe for `norm_num` to call `simp [-one_div_eq_inv]`? By the way, I am not convinced that `one_div_eq_inv` is a good simp rule, what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 03 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798174):
It's the same family that turns every `a-b` into `a+-b` that I hate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 03 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798199):
and it's in core lib :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798795):
a better question is why `norm_num1` isn't solving the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798811):
since it does solve the goal if you canonize the instances by restating the goal as you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798908):
I think this one is a result of my relying on the C++ `norm_num` implementation, which lags behind the mathlib implementation quite a bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798941):
I use it for doing `+` `-` `*` `/` on rings and fields, and do everything else in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150799067):
but I have seen it get confused with weird instances before (i.e. `simp` wants to prove that `(0 : int) != (1 : multiplicative int)` even though it's false)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 03 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150799423):
It is definitely confused by the instances. With `pp.all`, the goal it can not solve is
```lean
@has_le.le.{0} real
    (@preorder.to_has_le.{0} real
       (@partial_order.to_preorder.{0} real
          (@ordered_comm_monoid.to_partial_order.{0} real
             (@ordered_cancel_comm_monoid.to_ordered_comm_monoid.{0} real
                (@ordered_semiring.to_ordered_cancel_comm_monoid.{0} real
                   (@linear_ordered_semiring.to_ordered_semiring.{0} real real.linear_ordered_semiring))))))
    (@has_inv.inv.{0} real (@division_ring.to_has_inv.{0} real real.division_ring)
       (@bit0.{0} real
          (@distrib.to_has_add.{0} real
             (@ring.to_distrib.{0} real
                (@normed_ring.to_ring.{0} real (@normed_field.to_normed_ring.{0} real real.normed_field))))
          (@has_one.one.{0} real
             (@zero_ne_one_class.to_has_one.{0} real (@domain.to_zero_ne_one_class.{0} real real.domain)))))
    (@has_one.one.{0} real
       (@monoid.to_has_one.{0} real
          (@semiring.to_monoid.{0} real
             (@ordered_semiring.to_semiring.{0} real
                (@linear_ordered_semiring.to_ordered_semiring.{0} real real.linear_ordered_semiring)))))
```
while the "right" instance is the much nicer 
```lean
@has_le.le.{0} real real.has_le
    (@has_inv.inv.{0} real (@division_ring.to_has_inv.{0} real real.division_ring)
       (@bit0.{0} real
          (@distrib.to_has_add.{0} real
             (@ring.to_distrib.{0} real
                (@normed_ring.to_ring.{0} real (@normed_field.to_normed_ring.{0} real real.normed_field))))
          (@has_one.one.{0} real
             (@zero_ne_one_class.to_has_one.{0} real (@domain.to_zero_ne_one_class.{0} real real.domain)))))
    (@has_one.one.{0} real (@zero_ne_one_class.to_has_one.{0} real (@domain.to_zero_ne_one_class.{0} real real.domain))) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150800863):
Something in `norm_num`, either in C++ or in mathlib, is creating some metavars and leaving them uninstantiated. Adding `e₂ ← instantiate_mvars e₂,` before the `guard` at https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L162 allows `norm_num1` to kill the goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150800903):
I haven't tracked down where the uninstantiated metavar is coming from yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Dec 03 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802454):
[20180814_193304.jpg](/user_uploads/3121/ux1kBLQGexv8qc9xmddMHxrJ/20180814_193304.jpg)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Dec 03 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802460):
I also  bumped into deterministic timeout few times when solving various inequality; the common situation was that I had goals involving some "variable" real number (i.e. not explicit - like the 'k' and 'l' in the example) and norm_num got in a loop (often involving 'one_div_eq_inv')

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802866):
Hmm. I think the C++ `norm_num` instantiates mvars as a side effect, but only sometimes. It doesn't do it when it when the term is already in normal form.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802905):
Simple fix: `e ← instantiate_mvars e,` at `norm_num.lean:468`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804050):
468?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804058):
https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L468

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804070):
you mean before the `ext_simplify_core`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804122):
Booooo! Rob is not running up to date mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804158):
lol, you don't want to know what I'm running

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804210):
Nope, the argument to `derive` should be instantiated before you do anything with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804221):
So make that the first line of the `do` block.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804240):
why not 471/472? that's the first place after calling C `norm_num`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804287):
or is the problem uninstantiated metavars in the user input

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 03 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804363):
Yeah, exactly. At some point you compare the input with something that went through the C++ `norm_num`. The former has mvars, the latter doesn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804500):
we could just check for unify instead of alpha equivalent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804591):
eh, I guess that doesn't make sense here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804644):
yeah okay, ship it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 03 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150805046):
ship who?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150809032):
Not sure if this is a serious question, but this is an international forum, so... [ship it](https://english.stackexchange.com/questions/48443/meaning-of-ship-it)


{% endraw %}
