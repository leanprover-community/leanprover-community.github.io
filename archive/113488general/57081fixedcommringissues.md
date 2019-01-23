---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57081fixedcommringissues.html
---

## Stream: [general](index.html)
### Topic: [(fixed) comm_ring issues](57081fixedcommringissues.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856041):
I've got the following context/goal:
```lean
R : Type,
_inst_1 : ring.{0} R,
S : set.{0} R,
_inst_2 : @is_subring R _inst_1 S,
_inst_3 : comm_ring.{0} R,
a : R,
a_property : @has_mem.mem.{0 0} R (set.{0} R) (@set.has_mem.{0} R) a S,
b : R,
b_property : @has_mem.mem.{0 0} R (set.{0} R) (@set.has_mem.{0} R) b S
⊢ @eq.{1} R
    (@has_mul.mul.{0} R
       (@mul_zero_class.to_has_mul.{0} R (@semiring.to_mul_zero_class.{0} R (@ring.to_semiring.{0} R _inst_1)))
       a
       b)
    (@has_mul.mul.{0} R
       (@mul_zero_class.to_has_mul.{0} R (@semiring.to_mul_zero_class.{0} R (@ring.to_semiring.{0} R _inst_1)))
       b
       a)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856049):
For the record, here is my silly attempt to prove that subrings of comm rings are comm_ring:
```lean
instance subset.comm_ring [comm_ring R] : comm_ring S :=
{ mul_comm :=
  begin
    rintro ⟨a,_⟩ ⟨b,_⟩,
    apply subtype.eq,
    show a * b = b * a,
    rw mul_comm,
  end,
  .. subset.ring }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856089):
Somehow Lean turns R into a `semiring`, instead of a `comm_semigroup`... And therefore I can't apply `mul_comm`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856104):
For even more record:
```lean
instance subset.ring : ring S :=
{ add_comm      := assume ⟨a,_⟩ ⟨b,_⟩, subtype.eq $ add_comm _ _,
  left_distrib  := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ left_distrib _ _ _,
  right_distrib := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ right_distrib _ _ _,
  .. subtype.add_group,
  .. subtype.monoid }
```
That was nice and easy... (and maybe with Scott's tactics it will become even easier!) but if I substitute `mul` for `add` it borks out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856212):
Fixed. Lean starts crying if I tell it that R is a ring and a comm_ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856214):
And I understand why.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856255):
It just means that I cannot use the `variables {R : Type} [ring R]` from the top of my file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856779):
If you put `{R} [comm_ring R]` in the statement instead of just `[comm_ring R]` it will override the `R` in the enclosing section

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856844):
OTOH, then I still can't use the `variables {S : set R} [is_subring S]` from the top of my file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856857):
What I would need is to somehow tell lean: "Hey, in addition to all the other hypotheses, please extend the ring instance into a comm_ring instance."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 18 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857156):
I don't understand what you are doing. Haven't you already done that in https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857310):
Not the bit on commutative rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857317):
Only plain old rings


{% endraw %}
