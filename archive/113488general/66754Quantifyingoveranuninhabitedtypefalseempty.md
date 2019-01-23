---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66754Quantifyingoveranuninhabitedtypefalseempty.html
---

## Stream: [general](index.html)
### Topic: [Quantifying over an uninhabited type (false/ empty)](66754Quantifyingoveranuninhabitedtypefalseempty.html)

---

#### [Adam Kurkiewicz (Mar 22 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124058931):
I'm wondering whether this is something I should be able to prove (I think I should). It came up when I was trying to show that two definitions of primality are equivalent.

Let's say that we have a property, which quantifies over an empty, uninhabited type:

```
def  impossible_property : Prop  :=
∀ (Pfalse : false), 1  =  1
```

Is it true that `¬ impossible_property`, i.e. how, if at all, can I finish this proof:

```
def  cant_happen : ¬ impossible_property :=
λ Pimp : impossible_property,
sorry
```

#### [Johannes Hölzl (Mar 22 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059054):
Its the opposite: `impossible_property` is always inhabited, it can be easily proved using `false.elim`.

#### [Adam Kurkiewicz (Mar 22 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059575):
Cheers, indeed:

```
def  impossible_property : Prop  :=
∀ (Pfalse : false), 1  =  1
def  can_happen_ : impossible_property :=
λ (Pfalse: false),
false.elim Pfalse
```

#### [Moses Schönfinkel (Mar 22 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059651):
This is better shown with a "ridiculous" example. 
```lean
lemma exfalso_quod_libet (h : false) : 4 = 2 := false.elim h
```

#### [Adam Kurkiewicz (Mar 22 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124060858):
Thanks Moses,

this is indeed a better example. I'm afraid though that my confusion goes deeper than the initial question.

I've been trying to show that two definitions of primality are equivalent:

```
def  is_divisible: nat → nat →  Prop  :=
λ n m : nat, ∃ k : nat, m * k = n

def  is_prime1: nat →  Prop  :=
λ p, ∀ (m : nat) (Pmdp : is_divisible p m), ((m =  1) ∨ (m = p)) ∧ (p ≠  1)

def  is_prime2: nat →  Prop  :=
λ p, ∀ (k : nat) (b1 : k < p) (b2 : 1  < k), (¬ is_divisible p k)
```

Using your example I was able to show that 1 is prime according to the second definition `is_prime2`:

```
def  one_is_prime2 : is_prime2 1  :=
λ (k : nat) (x : k <  1) (y : 1  < k),
have a : 1  <  1, from lt.trans y x,
have one_ne_one : 1  ≠  1, from (ne_of_lt a),
false.elim (one_ne_one (eq.refl 1))
```
 
This clearly makes `is_prime_2` a bad definition of primality, but I really can't see what went wrong.

#### [Mario Carneiro (Mar 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061502):
You should look at the definition of `prime` and equivalent variations in mathlib `data.nat.prime`

#### [Mario Carneiro (Mar 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061507):
Most definitions of `prime` have to explicitly exclude 1

#### [Mario Carneiro (Mar 22 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061570):
It is true that there are no 1<k<1 such that 1 | k, meaning that 1 is spuriously identified as prime using `is_prime2`.

#### [Mario Carneiro (Mar 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061651):
By the way you probably want `p \ne 1` in`is_prime1` to come before the forall, otherwise it only applies when there exists an m such that p|m (which is true, but still it's a bit subtle)

#### [Mario Carneiro (Mar 22 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061716):
forall has low binding power, meaning that it extends until it hits a close parenthesis

#### [Adam Kurkiewicz (Mar 22 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124063178):
Thanks, this makes sense. 

The problem extends to `is_prime2 0`, since `k < 0 → false` and we end up with the same problems. Definition of primality in mathlib excludes  these cases, just as you pointed out, before the quantifier:  `def  prime (p : ℕ) := p ≥  2  ∧  ∀ m ∣ p, m =  1  ∨ m = p`

