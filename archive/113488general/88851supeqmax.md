---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88851supeqmax.html
---

## Stream: [general](index.html)
### Topic: [sup_eq_max](88851supeqmax.html)

---


{% raw %}
#### [ Chris Hughes (Jul 06 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199027):
Is there a nice way to state the lemma `a ⊔ b = max a b`, in general, for when `sup` is not derived from `max` such as on `with_bot`, or do I just have to prove it for `with_bot`

#### [ Mario Carneiro (Jul 06 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199724):
You can prove `sup a b = max a b` on any type for which `max` makes sense

#### [ Mario Carneiro (Jul 06 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199934):
Oh, I see... There are two `lattice` structures on `with_bot` that don't coincide by defeq

#### [ Mario Carneiro (Jul 06 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199952):
but they are the same since they have the same `le`

#### [ Mario Carneiro (Jul 06 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200322):
unfortunately, despite how I've said that non-defeq diamonds are evil and should be avoided, there is not much I can do about this one since it would require adding a `sup` field to `decidable_linear_order` which is in core

#### [ Chris Hughes (Jul 06 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200405):
It makes sense to add this lemma then?
```lean
lemma sup_eq_max [decidable_linear_order α] (a b : with_bot α) : a ⊔ b = max a b :=
le_antisymm (sup_le (le_max_left _ _) (le_max_right _ _)) (max_le le_sup_left le_sup_right)
```

#### [ Johan Commelin (Jul 06 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200478):
/me thinks that core shouldn't be in core

#### [ Chris Hughes (Jul 06 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200612):
Why did that message appear next to your name instead of beneath?

#### [ Kevin Buzzard (Jul 06 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200630):
because he only thought it, he didn't post it

#### [ Kevin Buzzard (Jul 06 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200681):
There are rumours that core won't be in core in Lean 4

#### [ Johan Commelin (Jul 06 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200728):
```quote
Why did that message appear next to your name instead of beneath?
```
Yeah, I'm old. My IRC habits betray me. (Hint: type `/me` before your message.)


{% endraw %}
