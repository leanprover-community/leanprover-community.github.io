---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18749finsetwithtwoelements.html
---

## Stream: [maths](index.html)
### Topic: [finset with two elements](18749finsetwithtwoelements.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 08 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097823):
@**Morenikeji Neri** has proved `det(AB)=det(A)det(B)` modulo some lemma about switching two rows of a matrix making the sign change, which became a lemma about summing over a set of size 2, which has now been reduced to this:

```lean
import data.fintype

open finset

example (α : Type*) [fintype α] [decidable_eq α] (s t : α) (Hdiff : s ≠ t) :
filter (λ a, a = s ∨ a = t) univ = insert s (finset.singleton t) := sorry
```

This says (if I got it right) that if `s` and `t` are two distinct terms, then filtering over the predicate which says "I am `s` or `t`" gives me precisely the finset containing `s `and `t` (I built it using insert and singleton because there are lemmas like `sum_insert` and `sum_singleton).

I used to rant a lot about "easy in maths, hard in lean" stuff when I found it very frustrating that there was stuff which was easy in maths but which *I* found hard in Lean. As I get better at Lean I realise that I'm ranting less and just solving my own problems. But this one looks scary, because a finset is quite a complicated object for me -- I'm not sure I can steer `nodup` and I'm still quite an amateur when it comes to quotients. 

This is about the third post I've written about this problem; the first two I've written, thought "actually I can make progress", and then deleted. But this one still looks scary. Can anyone suggest a way to progress on this?

#### [ Kenny Lau (Aug 08 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097900):
```lean
import data.fintype

open finset

example (α : Type*) [fintype α] [decidable_eq α] (s t : α) (Hdiff : s ≠ t) :
  filter (λ a, a = s ∨ a = t) univ = insert s (finset.singleton t) :=
ext.2 $ by simp
```

#### [ Kenny Lau (Aug 08 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097931):
```lean
import data.fintype

open finset

example (α : Type*) [fintype α] [decidable_eq α] (s t : α) (Hdiff : s ≠ t) :
  filter (λ a, a = s ∨ a = t) univ = insert s (finset.singleton t) :=
by ext; simp
```

#### [ Kevin Buzzard (Aug 08 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098109):
:o

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098117):
I didn't even think to try simp, because "this was obviously much too complicated for a stupid thing like simp"

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098122):
Thanks Kenny!

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098128):
My simp-fu is still very weak.

#### [ Rob Lewis (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098132):
I think you don't even need the `Hdiff` argument!

#### [ Kevin Buzzard (Aug 08 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098177):
You might be right -- I didn't check to see what insert did when it was already in.

#### [ Kevin Buzzard (Aug 08 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098193):
multiset insert adds another one, I guess that was what scared me off.

#### [ Mario Carneiro (Aug 08 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098908):
I would say the moral of the story here is the power of finset extensionality. Finsets are complicatedly defined, but it is not hard to show equalities between finsets because you can just reason about the set that they define

#### [ Kevin Buzzard (Aug 08 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131099150):
Yes -- it wasn't the `simp` that was the insight, it was the `ext`. The proof (of det AB = det A det B) is apparently complete now. Of course it's not remotely mathlib-ready...

#### [ Kevin Buzzard (Aug 08 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131099565):
By the way, the proof featured:

```lean
lemma sum_equiv_classes {α β : Type*} [add_comm_monoid α] [fintype β] (f : β → α)
  (h : setoid β) [decidable_rel h.r] [decidable_eq β] : 
finset.sum (@finset.univ β _) f = finset.sum finset.univ 
  (λ (x : quotient h), finset.sum (filter (λ b : β, ⟦b⟧ = x) finset.univ) f) := 
```

which I thought at the time was a good idea, but actually was a pain to apply because I didn't have an equivalence relation on a fintype, I had an equivalence relation on a finset, so there was a certain amount of inelegant scuffling around with `↥↑s` at some point. Wouldn't surprise me if I was missing a trick.


{% endraw %}
