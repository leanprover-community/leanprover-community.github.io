---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95622proofbyinductiononZ.html
---

## Stream: [general](index.html)
### Topic: [proof by induction on Z](95622proofbyinductiononZ.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232278):
Why is a thing like this not possible?
```lean
import algebra.group_power

theorem map_gsmul {A B} [add_group A] [add_group B] (f : A → B) [is_add_group_hom f] (a : A) :
∀ (n : ℤ), f (gsmul n a) = gsmul n (f a)
| (int.of_nat 0) := by simp [gsmul_of_nat, is_add_group_hom.zero f]
| (int.of_nat (n+1)) := by simp [gsmul_of_nat, succ_smul, is_add_group_hom.add f]; exact map_gsmul (int.of_nat n)
| -[1+n] :=
begin
  simp [gsmul_neg, is_add_group_hom.neg f],
  exact map_gsmul (int.of_nat (n+1))
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232459):
That's a funny well founded relation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232508):
I wouldn't say it's funny. I think it's very natural.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232522):
I'm just nesting the inductive property of `int` and `nat`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232523):
But you haven't told lean what it is. I would just prove `map_smul` first for naturals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232531):
I think you need to be more explicit about the well founded relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232532):
or use lemmas like chris says

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232534):
You could do `using_well_founded` but proving `map_smul` first is more sensible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232535):
But why can't I just nest inductive properties?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232537):
because that's not what you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232579):
Hmm, so what did I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232580):
you call `(n+1)` case from `-[1+n]` case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232584):
that's not structurally well founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232587):
Sure, but `n+1` is an `of_nat`, and I had proven those already.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232588):
that's called a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232591):
/me sighs...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232598):
when you write it all in one big induction lean has no choice but to assume everything depends on everything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232655):
But don't you think this is a typical strategy for proving things about Z? Does this deserve special support?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232663):
Or should I prove `map_smul` for add_monoid homs? (Btw, I think there is no instance from `add_group_hom`s to `add_monoid_hom`s).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232711):
```quote
But don't you think this is a typical strategy for proving things about Z? Does this deserve special support?
```
 I think the typical strategy is to use `int.induction_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151233000):
Here's a horrible proof using `using_well_founded`
```lean
theorem map_gsmul {A B} [add_group A] [add_group B] (f : A → B) [is_add_group_hom f] (a : A) :
∀ (n : ℤ), f (gsmul n a) = gsmul n (f a)
| (int.of_nat 0) := by simp [gsmul_of_nat, is_add_group_hom.zero f]
| (int.of_nat (n+1)) := 
  have (n : with_top ℕ) < (n + 1 : ℕ), from with_top.coe_lt_coe.2 (nat.lt_succ_self _),
  by simp [gsmul_of_nat, succ_smul, is_add_group_hom.add f]; 
  exact map_gsmul (int.of_nat n)
| -[1+n] :=
have ((n + 1 : ℕ) : with_top ℕ) < ⊤, from dec_trivial, 
begin
  simp [gsmul_neg, is_add_group_hom.neg f],
  exact map_gsmul (int.of_nat (n+1))
end
using_well_founded 
  {rel_tac := λ _ _, `[exact ⟨_, @inv_image.wf ℤ (with_top ℕ) _
    (λ i : ℤ, int.rec_on i coe (λ _, ⊤) : ℤ → with_top ℕ) 
      (with_top.well_founded_lt nat.lt_wf)⟩],
  dec_tac := tactic.assumption }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151233113):
I understand why you suggest the other strategy...


{% endraw %}
