---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11441equalityofpitypes.html
---

## Stream: [general](index.html)
### Topic: [equality of pi types?](11441equalityofpitypes.html)

---


{% raw %}
#### [ Scott Buckley (Apr 26 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125702762):
Hi guys, I'm stuck trying to prove the following, which seems intuitively true to me:
```
((T1 -> T2) = (T1 -> T2')) ->
T2 = T2' 
```

If it helps, I have instances of T1, (T1 -> T2), and (T1 -> T2'). ```cases``` on the equality hypotheses doesn't get me anywhere. I've tried building proofs various ways, but I always come back to the fundamental problem.

Is this even true?

Cheers,
Scott.
EDIT: fixed parameterisation

#### [ Mario Carneiro (Apr 26 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703075):
Could you post a complete statement of the claim? In particular I want to know what are the types of `T1`, `T2`, and `T2'`

#### [ Mario Carneiro (Apr 26 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703125):
If `T2` and `T2'` are propositions, then this follows purely from the ancillary instances you have; from `T1` and `T1 -> T2` we find that `T2` is true, and similarly `T2'` is true, so they are equal by `propext`

#### [ Mario Carneiro (Apr 26 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703310):
Oh, I just realized that you are misinterpreting the binding power of equality over arrow - I think you wanted to say
```
(T1 -> T2) = (T1 -> T2') -> T2 = T2'
```
This claim is known as injectivity of pi, and it is independent in lean's axiomatization. I am pretty sure it's consistent with DTT but for some reason it's never assumed in any interactive proof assistant I know. (Warning: Also seemingly reasonable is injectivity on the left, i.e. `(T1 -> T2) = (T1' -> T2) -> T1 = T1'`, but this one is false when `T2` is a proposition.)

#### [ Mario Carneiro (Apr 26 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703385):
Oh wait, even injectivity on the right is false when `T1` is empty and `T2` and `T2'` are propositions, i.e. `(false -> false) = (false -> true)` but `false != true`

#### [ Scott Buckley (Apr 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703441):
Thanks Mario. Yeah you're right, I mis-parameterised.
T1, T2, and T2' are Type. All are inhabited.

#### [ Mario Carneiro (Apr 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703491):
I think I will stick with my original answer then - unprovable in Lean but consistent with it

#### [ Mario Carneiro (Apr 26 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703497):
May I ask why you need this?

#### [ Mario Carneiro (Apr 26 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703541):
I know it comes up in attempting to prove
```
f == g -> a == b -> f a == g b
```
which would be nice if it were provable but you have to assume `f = g` for it to work.

#### [ Scott Buckley (Apr 26 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703666):
I'm proving type determinism for my operational semantics. Some expressions contain lean functions. If I have an application, its subexpressions must have function types, so the output of an application must have the same type. That's where this comes in.

#### [ Mario Carneiro (Apr 26 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125704324):
So the types of your functions are calculated dynamically? I think you want to bundle the types as auxiliary data for this kind of thing to work. It's not sufficient to know that they *can be* well typed, you need to keep track of the type itself so that one pi doesn't get swapped with another that is equal but has different parts (assuming pi is noninjective)

#### [ Scott Buckley (Apr 26 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125704716):
yeah that's a good point. thanks for the advice :)

#### [ Kenny Lau (Apr 26 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125732960):
```quote
I think I will stick with my original answer then - unprovable in Lean but consistent with it
```
this is very interesting

#### [ Kenny Lau (Apr 26 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125732962):
@**Kevin Buzzard**

#### [ Kenny Lau (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127208536):
@**Mario Carneiro** is the converse true / provable?

#### [ Kenny Lau (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127208538):
`T2 = T2' -> ((T1 -> T2) = (T1 -> T2'))`

#### [ Chris Hughes (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209021):
Isn't that just `rw`

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209024):
yes

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209029):
what if the right hand side is a pi

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209033):
does pi have an ext theorem?

#### [ Kenny Lau (May 28 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211597):
```lean
∀ {α : Sort u} {β γ : α → Sort v}, (∀ (x : α), β x == γ x) → ((Π (x : α), β x) == Π (x : α), γ x)
```

#### [ Kenny Lau (May 28 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211600):
Is this true/false/independent?

#### [ Johannes Hölzl (May 28 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211882):
You don't need `==` to state this. The type of `β x` and `γ x` are the same. dito on the rhs.

#### [ Johannes Hölzl (May 28 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211934):
```lean
universes u v
example {α : Sort u} {β γ : α → Sort v} (h : ∀ (x : α), β x = γ x) :  
  ((Π (x : α), β x) = Π (x : α), γ x) :=
have β = γ, from funext h,
by subst this
```

#### [ Kenny Lau (May 28 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127212180):
hmm

#### [ Mario Carneiro (May 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127219583):
The converse is false for some choices of T1, and independent for others


{% endraw %}
