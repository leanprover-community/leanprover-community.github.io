---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55555canwemakeacorelemmaintoasimplemma.html
---

## [general](index.html)
### [can we make a core lemma into a simp lemma](55555canwemakeacorelemmaintoasimplemma.html)

#### [Johan Commelin (Aug 07 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041229):
`nat.sub_self` is in core. I think it should be a simp lemma. Can we add such an attribute post-hoc in a mathlib file?

#### [Sean Leather (Aug 07 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041281):
```lean
attribute [simp] nat.sub_self
```

#### [Kevin Buzzard (Aug 07 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041567):
or `local attribute [simp] nat.sub_self` if you're scared that making it a simp lemma more globally will cause other problems. I see that the additive group version `sub_self` isn't a simp lemma either. This might be something to do with subtraction being involved. I think `a - b = a + (-b)` is a `simp` lemma and because of this `simp` might change your `a - a` to `a + (-a)` before it notices your attribute.

We were talking about a related thing a day or two ago, where `simp` just failed to simplify quite a complicated thing because it couldn't manage `a + (b + -a) = b`.

#### [Johan Commelin (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041932):
Right. But I think whenever `n : nat` and you encounter `(n - n)` somewhere in your goal, there should be no harm at all if you replace it with `0 : nat`...

#### [Johan Commelin (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041935):
Maybe I just don't understand `simp`.

#### [Mario Carneiro (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041937):
`nat.sub_self` should be a simp lemma. We can add it to `data.nat.basic`. As I've mentioned, `sub_self` will never trigger as a simp lemma

#### [Johan Commelin (Aug 07 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042034):
Right... because "group vs semigroup" ?

#### [Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042055):
`nat.sub` is not the same as the one defined for additive groups

#### [Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042090):
the sub-unfolding simp lemma only applies to the additive group sub

#### [Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042093):
of course `n + -n` doesn't even make sense over nat

#### [Kevin Buzzard (Aug 07 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042688):
Aah very nice :-) Is there any way of telling `simp` to try `sub_self` before trying the dreaded `sub_eq_add_neg`?

