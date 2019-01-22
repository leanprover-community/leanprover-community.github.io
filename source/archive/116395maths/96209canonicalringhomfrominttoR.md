---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96209canonicalringhomfrominttoR.html
---

## [maths](index.html)
### [canonical ring hom from int to R](96209canonicalringhomfrominttoR.html)

#### [Johan Commelin (Jul 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132971):
Does the canonical ring homomorphism from `int` to a ring `R` already have a name in Lean?

#### [Kenny Lau (Jul 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132977):
something something `int.coe`

#### [Mario Carneiro (Jul 23 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132982):
`int.cast`

#### [Johan Commelin (Jul 23 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133232):
Aah, of course. And do we already know that this is a ring hom?

#### [Kenny Lau (Jul 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133599):
```lean
import data.int.basic

universe u

instance int.cast.is_ring_hom (α : Type u) [ring α] : is_ring_hom (int.cast : ℤ → α) :=
{ map_add := int.cast_add,
  map_mul := int.cast_mul,
  map_one := int.cast_one }
```

#### [Kenny Lau (Jul 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133600):
now you know

#### [Johan Commelin (Jul 23 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135077):
(Sorry, I got distracted by other stuff.) Anyway, I'm not surprised that it is a 4-liner. It is just that I don't know how to figure out if this is somewhere in mathlib or not...

#### [Mario Carneiro (Jul 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135209):
it is not, but kenny is pointing out that all the theorems are already there

#### [Kevin Buzzard (Jul 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135926):
```quote
(Sorry, I got distracted by other stuff.) Anyway, I'm not surprised that it is a 4-liner. It is just that I don't know how to figure out if this is somewhere in mathlib or not...
```
You can check to see if Lean's type class inference system already knows a fact by seeing if you can prove it with `by apply_instance`. Of course this does not tell you whether the proof is in mathlib in a file you didn't import yet...

#### [Johan Commelin (Jul 23 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130136073):
True, I keep forgetting that trick.

#### [Kevin Buzzard (Jul 23 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130137120):
I used it extensively over the weekend in the middle of code just to make sure that type class inference was keeping up with what I was trying to do

#### [Kevin Buzzard (Jul 23 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130137155):
Just debugging lines which I'd delete after, checking my quotient group instances were working

