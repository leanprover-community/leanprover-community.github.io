---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89676Whycanrwrwdifferenthasmulinstancesbutnotfintype.html
---

## Stream: [general](index.html)
### Topic: [Why can rw rw different has_mul instances, but not fintype](89676Whycanrwrwdifferenthasmulinstancesbutnotfintype.html)

---


{% raw %}
#### [ Chris Hughes (Jun 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128082489):
In the following code, `rw` manages to recognize that two different expressions involving different paths of inferring the `has_mul` type class are equal. It can't do this with two definitionally equal `fintype` instances however. What's the difference between `has_mul` and `fintype` that leads to this behaviour?

```lean
def int2 := int

instance : comm_ring int2 := int.comm_ring

set_option pp.implicit true
set_option pp.notation false

lemma one_times_two : (1 : int2) * 2 = 2 :=
begin
/-@eq int2
    (@has_mul.mul int2
       (@mul_zero_class.to_has_mul int2
          (@semiring.to_mul_zero_class int2 (@ring.to_semiring int2 (@comm_ring.to_ring int2 int2.comm_ring))))
       1
       2)
    2-/
  refl,
end

instance : integral_domain int2 := by unfold int2; apply_instance
example : (1 : int2) * 2 = 2 :=
begin
  /-@eq int2
    (@has_mul.mul int2
       (@no_zero_divisors.to_has_mul int2
          (@domain.to_no_zero_divisors int2 (@integral_domain.to_domain int2 int2.integral_domain)))
       1
       2)
    2-/
  rw one_times_two, -- works
end

def bool2 := bool

instance : fintype bool2 := bool.fintype

lemma card_bool1 : fintype.card bool2 = 2 :=
begin
  refl,
end

def bool2_fintype : fintype bool2 := ⟨{tt, ff}, λ x, by cases x; simp⟩

def bool2_fintype3 : fintype bool2 := ⟨{ff, tt}, λ x, by cases x; simp⟩

example : ({ff, tt} : finset bool) = ({tt, ff} : finset bool) := rfl

lemma card_bool2 : @fintype.card bool2 bool2_fintype = 2 :=
card_bool1 -- They are defeq

lemma card_bool3 : @fintype.card bool2 bool2_fintype = 2 :=
begin
  rw card_bool1, --doesn't work
end

lemma card_bool4 : @fintype.card bool2 bool2_fintype3 = 2 := card_bool1
```

#### [ Simon Hudon (Jun 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128082839):
what error do you get?

#### [ Chris Hughes (Jun 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083025):
I accidentally gave an example that did work. I've just edited it.

#### [ Chris Hughes (Jun 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083327):
`card_bool2` works not because they're defeq, but perhaps because it knows fintype is a subsingleton.

#### [ Reid Barton (Jun 14 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083559):
I think it works because it reduced both `card_bool1` and `card_bool2` to `2 = 2`

#### [ Reid Barton (Jun 14 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083570):
it = `card_bool2`

#### [ Reid Barton (Jun 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083640):
I don't know why your `rw one_times_two` works though.

#### [ Kevin Buzzard (Jun 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%20rw%20rw%20different%20has_mul%20instances%2C%20but%20not%20fintype/near/128083660):
Yeah, rw is usually really snotty about things like this


{% endraw %}
