---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39393annoyance.html
---

## [general](index.html)
### [$ annoyance](39393annoyance.html)

#### [Kevin Buzzard (May 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710552):
```lean
import data.set 
variables (α : Type) (p : set α → Prop)

definition subtype_is_partial_order :
partial_order {U : set α // p U} := 
{ le := λ Us Vs,Us.1 ⊆ Vs.1,
  le_refl := λ Us, set.subset.refl Us.1,
  le_trans := λ Us Vs Ws, set.subset.trans,
  le_antisymm := λ Us Vs HUV HVU, subtype.eq $ set.subset.antisymm HUV HVU
--  le_antisymm := λ Us Vs, subtype.eq $ set.subset.antisymm -- doesn't work, annoyingly
}
```

#### [Kevin Buzzard (May 17 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710573):
I wanted to write a beautiful partial order on some subsets of a type.

#### [Kevin Buzzard (May 17 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710640):
`le_refl` is a bit meh because I had to write `Us.1`, but I do understand that `set.subset.refl` needs to be told what it's refling in general

#### [Kevin Buzzard (May 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710677):
`le_trans` is perfect and I could probably even have written `\lam _ _ _`

#### [Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710770):
`le_antisymm` is a bit annoying though because in functional programming if you write `\lam x y, blah y` then you can normally remove the `y`s. But I can't remove `HUV` and `HVU` here because of my `$` trickery. Is this just some annoyance in functional programming that I have to put up with or is there some other idiom which means I can get rid of `HUV` and `HVU` somehow?

#### [Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710780):
`le_antisymm := λ Us Vs, subtype.eq ∘ set.subset.antisymm` doesn't work either

#### [Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710801):
I can see why these things don't work, I just want something which looks a bit cooler if possible. Not for any particularly good reason, I'm just trying to write tidy code

#### [Kevin Buzzard (May 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710885):
Here's a succinct way of asking my question:

#### [Kevin Buzzard (May 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710887):
```lean
  le_refl := λ _, set.subset.refl _,
  le_trans := λ _ _ _, set.subset.trans,
  le_antisymm := λ _ _ HUV HVU, subtype.eq $ set.subset.antisymm HUV HVU
```

#### [Kevin Buzzard (May 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126710927):
Can I get rid of those last two variables?

#### [Chris Hughes (May 17 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126711207):
`le_antisymm := λ Us Vs, subtype.eq ∘ set.subset.antisymm` doesn't work because there are two arguments, and `f ∘ g` is `λ x, f (g x)`not `λ x y, f (g x y)`The eta reduction doesn't work because the arguments are inside brackets.

#### [Chris Hughes (May 17 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126711306):
I think you just have to put up with it, but it doesn't look that annoying.

#### [Chris Hughes (May 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126711333):
This works `le_antisymm := λ Us Vs HUV, subtype.eq ∘ set.subset.antisymm HUV`

#### [Chris Hughes (May 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126711384):
If you want to be extra confusing.

#### [Chris Hughes (May 17 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126716170):
```quote
I can see why these things don't work, I just want something which looks a bit cooler if possible. Not for any particularly good reason, I'm just trying to write tidy code
```
I should have read the question

#### [Sebastian Ullrich (May 17 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718633):
`λ Us Vs, ((∘) ∘ (∘)) subtype.eq set.subset.antisymm`

#### [Reid Barton (May 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718805):
At least you can't write the awful `(f .) . g` in lean.

#### [Reid Barton (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718821):
I had to work out on paper whether that does what I remember it doing.

#### [Patrick Massot (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718822):
what would that mean?

#### [Sebastian Ullrich (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718828):
Yes, I'll definitely fix that for Lean 4

#### [Reid Barton (May 17 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718896):
Haskell `.` is Lean's `∘`, and `(f .)` means `λ h, f ∘ h`

#### [Patrick Massot (May 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718929):
Aaaarg, I did that rookie mistake again! I called some variable `a`

#### [Patrick Massot (May 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126718983):
Sebastian, will this mistake be forgiven in Lean 4?

#### [Sebastian Ullrich (May 17 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126719304):
absolutely

#### [Kevin Buzzard (May 17 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126720531):
`#eval (+) 2 2 -- 4`

#### [Kevin Buzzard (May 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126720580):
I remember reading that one could do this in Haskell but I didn't know it was a Lean thing

#### [Kevin Buzzard (May 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126720690):
`#check ((∘) ∘ (∘)) -- (?M_1 → ?M_2) → (?M_4 → ?M_3 → ?M_1) → ?M_4 → ?M_3 → ?M_2`

#### [Kevin Buzzard (May 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126720691):
I love Lean

#### [Kevin Buzzard (May 18 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126720732):
who needs pencil and paper

#### [Kevin Buzzard (May 18 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126722090):
Ok so I used pencil and paper

#### [Kevin Buzzard (May 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126722151):
Recall that `(∘) f g x = (f ∘ g) x = f (g x)`. So

```
   ((∘) ∘ (∘)) a b c d 
=  (∘) ((∘) a) b c d 
=  ((∘) a) (b c) d 
=  (∘) a (b c) d 
=  a (b c d)
```

#### [Kevin Buzzard (May 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126722157):
which is indeed what we wanted to do

#### [Kevin Buzzard (May 18 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126722175):
At the back of my mind I always feel like computer scientists learn this sort of stuff in their first year of undergrad whereas this is never taught to mathematicians at all

#### [Brendan Zabarauskas (May 18 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126729532):
Depends on the computer science course :weary:

#### [Mario Carneiro (May 18 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126729645):
I don't think this is actually accurate, but I admit it as Kevin's warped view of what computer science is. I think it is accurate to say that you become comfortable with this when learning Haskell and not before

#### [Mario Carneiro (May 18 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126729702):
I think that the demographics of this chat are disproportionately skewed towards functional programmers (for good reason), so it's easy to get that impression

#### [Brendan Zabarauskas (May 18 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/$ annoyance/near/126729800):
Correct. I'm one who had to learn FP and type theory/programming language stuff in my own time. But might be getting off topic here.

