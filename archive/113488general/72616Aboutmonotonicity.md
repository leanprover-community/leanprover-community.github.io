---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72616Aboutmonotonicity.html
---

## Stream: [general](index.html)
### Topic: [About monotonicity](72616Aboutmonotonicity.html)

---


{% raw %}
#### [ Simon Hudon (Mar 16 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123813072):
I'm currently working on monotonicity related simplification. In some places I consider associativity and commutativity with regards to monotonicity but let's leave that aside for now.

A general monotonicity law for addition looks like:

```
@[monotonic]
lemma add_mono {x₀ y₀ x₁ y₁ : α} [ordered_semiring α]
  (h : x₀ ≤ y₀)
  (h' : x₁ ≤ y₁)
: x₀ + x₁ ≤ y₀ + y₁ := ...
```

Very straightforward, no side conditions. When I turn to multiplication, the lemmas multiply (fun definitely intended). I get one position monotonicity:

```
@[monotonic]
lemma mul_mono_nonneg_left {x y z : α} [ordered_semiring α]
  (h' : 0 ≤ z)
  (h : x ≤ y)
: x * z ≤ y * z := ...

@[monotonic]
lemma mul_mono_nonneg_right {x y z : α} [ordered_semiring α]
  (h' : 0 ≤ z)
  (h : x ≤ y)
: z * x ≤ z * y := ...
```

In total, 4 of them. The other 2 are left as an exercise :wink:. When considering two position-monotonicity for multiplication, their number blows up: 

```
@[monotonic]
lemma mul_mono_nonpos_nonpos_left {x₀ y₀ x₁ y₁ : α} [linear_ordered_ring α]
  [decidable_rel ((≤) : α → α → Prop)]
  (h : 0 ≥ x₀)
  (h : 0 ≥ y₁)
  (h₀ : y₀ ≤ x₀)
  (h₁ : y₁ ≤ x₁)
: x₀ * x₁ ≤ y₀ * y₁ := ...

@[monotonic]
lemma mul_mono_nonpos_nonpos_right {x₀ y₀ x₁ y₁ : α} [linear_ordered_ring α]
  [decidable_rel ((≤) : α → α → Prop)]
  (h : 0 ≥ y₀)
  (h : 0 ≥ x₁)
  (h₀ : y₀ ≤ x₀)
  (h₁ : y₁ ≤ x₁)
: x₀ * x₁ ≤ y₀ * y₁ := ...
```

The difference is in the side condition. They could be unified and make `(h : 0 ≥ x₀) (h : 0 ≥ x₁)` but that is stronger than required. I have additionally six more combinations of `nonpos` / `nonneg`. The goal of `mono` is that you don't have to remember those lemmas, it just applies the right one for you. With the explosion of possible side condition, the error messages might get long if they can't be discharged automatically (because `mono` will look in your assumptions, try `norm_num` and other to discharge side conditions and eliminate candidates).

Does anybody have an opinion on this large number of lemmas just for multiplication?

#### [ Kevin Buzzard (Mar 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816761):
Don't all of these just follow from 0<=x, 0<=y implies 0<=xy, a<=b implies a+t <= b+t and standard ring theory axioms?

#### [ Simon Hudon (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816943):
Do you mean "do all those multiplication lemmas follow from ..."?

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816949):
right

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816951):
but presumably you're asking something else

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816956):
I mean, I am saying that they should do

#### [ Simon Hudon (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816957):
In any case, their truth is rather straightforward. What I'm wondering about is how usable they are.

#### [ Kevin Buzzard (Mar 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817031):
I have no feeling for this sort of thing. Does simp solve any of them? Presumably some cunning tactic would solve them all?

#### [ Simon Hudon (Mar 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817048):
For instance, if I don't split `mul_mono_nonpos_nonpos` into `mul_mono_nonpos_nonpos_left` and `mul_mono_nonpos_nonpos_right`, I get a simpler set of rules. However, some situations won't be addressed by monotonicity because `0 ≤ x0` and `0 ≤ x1` are stronger assumptions than what is strictly necessary

#### [ Simon Hudon (Mar 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817116):
I believe you are talking about proving them. Again, proving them is easy. I'm writing them up so that the monotonicity tactic will be able to decompose proofs of `x * y ≤ z * w` into simpler subgoals.

#### [ Simon Hudon (Mar 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817216):
The tricky part in doing that is remembering to have assumptions about some of your terms being non-negative or non-positive.

#### [ Kevin Buzzard (Mar 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817225):
But there are are lots of ways to deduce `x*y <= z*w`, right?

#### [ Simon Hudon (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817252):
If you forget, `mono` will list all the ways in which `*` is monotonic with the corresponding side conditions

#### [ Kevin Buzzard (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817255):
e.g. `0<=x<=z and 0<=y<=w`, or `0<=x<=w and 0<=y<=z`, or...

#### [ Simon Hudon (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817273):
Exactly. That's why I have 12 monotonicity lemmas for multiplication. It seems like a lot to me but maybe it's justifiable

#### [ Kevin Buzzard (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817275):
`z<=x<=0 and w<=y<=0...`

#### [ Kevin Buzzard (Mar 16 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817323):
Do you care about `0<=x and z<=-x and 0<=y and w<=-y`?

#### [ Kevin Buzzard (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817346):
`0<=x<=3z and 0<=y<=w/3`?

#### [ Simon Hudon (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817350):
I hadn't thought of it. Maybe I should care about that.

#### [ Kevin Buzzard (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817354):
I don't really know what your applications are.

#### [ Kevin Buzzard (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817406):
It's slightly disconcerting that there are so many!

#### [ Simon Hudon (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817409):
```quote
`0<=x<=3z and 0<=y<=w/3`?
```
That, I will leave out.

#### [ Simon Hudon (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817414):
Let me give you an example

#### [ Simon Hudon (Mar 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817589):
Let's say that you have to prove:

```
⊢ x₀ * x₁ * x₂ * y₀ * x₃ * y₁ * x₄ * x₅ ≤ x₀ * x₁ * x₂ * z₀ * x₃ * z₁ * x₄ * x₅
```

I want it to be possible to call 

```
mono*
```

and get the proof reduced to two goals:

```
⊢ y₀ ≤ z₀
⊢ y₁ ≤ z₁
```

provided that you have the right assumptions about `x₀`, `x₁`, `x₂`, `x₃`, `x₄`, `x₅`, namely, them being non-negative or non-positive.

#### [ Kevin Buzzard (Mar 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817661):
If there were a simp lemma that said `0<x -> (a<=b iff x*a <= x*b)` and similar for `0>x` wouldn't simp get you as far as `y0*y1<=z0*z1` or similar?

#### [ Kevin Buzzard (Mar 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817706):
and then you have no reason to believe y0<=z0 and y1<=z1 because maybe y0<=3*z0 and y1<=z1/3

#### [ Simon Hudon (Mar 16 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817789):
Of course, as a user, you're the one deciding to call `mono`. And if you want to keep `y` and `z` in the same goal `ac_mono` will get you the goal that you're mentioning. But `simp` can't get you there automatically because the choice of rewrite is not unique so marking those lemmas as `[simp]` would make your proofs brittle

#### [ Simon Hudon (Mar 16 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817847):
And if you only want a few steps of mono, you can use `mono^3` instead and it will stop after three applications of monotonicity laws

#### [ Simon Hudon (Mar 16 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817872):
The point is, in a monotonic context, you can get rid of all lot of noise in one shot using `mono` or `ac_mono`


{% endraw %}
