---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57755galoisinsertion.html
---

## Stream: [general](index.html)
### Topic: [galois insertion](57755galoisinsertion.html)

---

#### [Kenny Lau (Sep 25 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575752):
```lean
import algebra.archimedean

example (α : Type*) [floor_ring α] : galois_insertion (ceil : α → ℤ) coe :=
{ choice := λ x _, ⌈x⌉,
  gc := λ x n, ceil_le,
  le_l_u := λ _, le_of_eq (ceil_coe _).symm,
  choice_eq := λ _ _, rfl }
```

#### [Kenny Lau (Sep 25 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575753):
let's come up with more examples

#### [Mario Carneiro (Sep 25 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575821):
nice observation. Of course `floor` is also in an adjoint pair, this time on the right side

#### [Mario Carneiro (Sep 25 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575944):
also natural number subtraction is best understood in terms of the galois connection it forms with addition

#### [Mario Carneiro (Sep 25 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575949):
same with natural/integer division

#### [Kenny Lau (Sep 25 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576084):
```quote
also natural number subtraction is best understood in terms of the galois connection it forms with addition
```
previously unsaid sentence in human history @**Kevin Buzzard**

#### [Simon Hudon (Sep 25 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576195):
Sorry, I have to contradict you. I wrote those Galois connection and PRed them to the core library while I was interning at Galois. And I thought that was a beautiful coincidence and wouldn't shut up about it :P

#### [Mario Carneiro (Sep 25 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576211):
did you make any galois connections while you were there? :)

#### [Simon Hudon (Sep 25 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576214):
I certainly did :D

#### [Kevin Buzzard (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134578923):
Kenny can you remind me what a Galois connection and Galois insertion is?

#### [Reid Barton (Sep 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134591243):
If it helps, Galois connection ~ adjunction and Galois insertion ~ reflective subcategory, i.e. one of the adjoints is the inclusion of a full subcategory (or possibly coreflective, probably the other one is called a Galois coinsertion)

#### [Reid Barton (Sep 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134591256):
where ~ means "is what you get by specializing to preorders = categories with at most one morphism in each hom set"

#### [Kevin Buzzard (Sep 25 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592595):
so a pair of adjoint functors and one is inclusion of a full subcategory. Aren't there lots of examples then? e.g. metric spaces <-> complete metric spaces and lots of other examples of when you drop a property of X and then find some adjoint?

#### [Reid Barton (Sep 25 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592862):
Yes except metric spaces don't form a preorder

#### [Reid Barton (Sep 25 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592982):
So the flavor of the examples tends to be a bit different, e.g., sub-R-modules inside all subsets or these floor/ceiling examples. But the theorems are largely the same--the left half of the connection preserves sups and so on

#### [Kevin Buzzard (Sep 25 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134593292):
Aah! At most one morphism between two objects, and a pair of adjoint functors, and inclusion of a full subcategory. That's the question.

#### [Kenny Lau (Sep 29 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134878359):
Is `nat.pred` and `nat.succ` a galois insertion?

#### [Kenny Lau (Sep 29 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134878360):
I can't seem to prove it

#### [Kevin Buzzard (Sep 29 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879239):
a<= succ b iff pred a <= b looks true to me

#### [Kevin Buzzard (Sep 29 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879241):
succ is inclusion of a full subcategory

#### [Kevin Buzzard (Sep 29 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879290):
succ a <= b iff a <= pred b is false though

#### [Kevin Buzzard (Sep 29 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879307):
And pred is not an inclusion of a full subcategory

#### [Kevin Buzzard (Sep 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879423):
So it's 50-50 from where I'm sitting as to whether it's an insertion or a coinsertion

#### [Kevin Buzzard (Sep 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879424):
But it's not both

#### [Mario Carneiro (Sep 29 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879960):
I was surprised to find that this wasn't already proven... more accurately there were some silly assumptions

#### [Mario Carneiro (Sep 29 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879976):
`a - b <= c <-> a <= b + c` is the galois connection, which is an insertion since `(a + b) - b = a`. Take `b = 1` and you have succ/pred

