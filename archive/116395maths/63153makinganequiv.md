---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/63153makinganequiv.html
---

## Stream: [maths](index.html)
### Topic: [making an equiv](63153makinganequiv.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 07 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133531588):
I have `f : α → α → α → α → α → α → Prop` that says `a ≠ b ∧ c ≠ b ∧ d ≠ e ∧ f ≠ e ∧ blah`. I have shown `f`is reflexive, symmetric and transitive (i.e. an equiv on α × α × α), but only when `a ≠ b ∧ c ≠ b`. Now I want to make the equiv classes, I'm having trouble with deciding what to do.
 If I set `f` to take a random value for `a = b`, then working with `f`is going to be annoying. If I make the equiv on `α × α × α` such that `a ≠ b ∧ c ≠ b`, then any time I talk about the class `a b c` I have to give proofs of `a ≠ b`and `c ≠ b`. Is there different method? 

In GeoCoq they cheat, instead of making an equiv, they make a new function (which is what the book does too),
```coq
Definition Q_CongA a :=
  ∃ A B C,
    A ≠ B ∧ C ≠ B ∧ ∀ X Y Z, CongA A B C X Y Z ↔ a X Y Z.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 07 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133532250):
You could define the equivalence relation on the subtype. It sounds like you just have to give proofs that `a \ne b` and stuff. Lean is all about edge cases. Why do you consider the GeoCoq solution cheating? You can define quotients on non-equivalence relations in lean, but it's not recommended.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133559910):
I want to define a function from an equivalence class, but to give the value I first need an element from the class (but every element gives the same result), how would I do this? i.e. I want to make a function which I know is well-defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133560004):
Assuming you're using `quot`/`quotient`, then `quot.lift`/`quotient.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 08 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133563238):
Ali I don't know if this helps, but when Luca was learning about equivalence classes (because he wanted to define a group structure on pi_1(X,x), which is a quotient) I wrote https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean to show him some basic tricks. For basic questions like how to define a function on a set of equivalence classes I could recommend the relevant docs https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients from TPIL, however mathlib adds extra functions which one can use with quotients, and these are not documented here. The mathlib file is here https://github.com/leanprover/mathlib/blob/master/data/quot.lean and it defines things such as `quotient.eq` which are very useful in practice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133570338):
Thanks, I was reading up on these this morning. I don't think there's a way to use the "cheat" method Coq uses (above), because I can't use exists to eliminate into something that isn't Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 09 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608290):
is there a way to do quot.lift on a set with a function that is constant over the set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 09 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608428):
You mean a computable function from `set \a` that's based on some arbitrary element of a set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 09 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608436):
The answer is probably no, because a set contains no computational content about it's elements.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 09 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608502):
Why does it work for quotient sets, but not just normal sets?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608553):
Why don't you formalise exactly what you're asking in Lean and post it? It's good practice, and also good practice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608945):
Something like this, 
`def F {α β : Type} (A : set α) (f : α → β) : (∀ a b, a ∈ A → b ∈ A → f a = f b) → β := x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 09 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609193):
This is not enough. You need to assume that `A` is not empty.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 09 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609197):
Then you can use some form of choice. (or you know that `β` is not empty and chose a default element.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609247):
Or if you express the nonempty condition as `trunc A`, which is the quotient of `A` by the relation which identifies everything, then you can define `F` (computably) using `quotient.lift`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609264):
If you use `choice`, then you don't even need the condition `(∀ a b, a ∈ A → b ∈ A → f a = f b)` to define `F`, which is mildly alarming, but you do need it to prove that `F` equals `f a` for any `a ∈ A`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 09 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609451):
If I use `trunc`, will it be annoying to switch between `A` and `trunc A`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609872):
Well `trunc A` is an alternative to `nonempty A`, which you would need instead.
The main annoyance of `trunc A` is that it isn't a proposition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610024):
```quote
Something like this, 
`def F {α β : Type} (A : set α) (f : α → β) : (∀ a b, a ∈ A → b ∈ A → f a = f b) → β := x`
```
You mean `:= sorry`? As others have pointed out this can't yet be done (alpha and beta could both be empty at this point). So in some sense you still haven't asked the question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 09 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610381):
I guess I'll have to try a different approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610654):
I'm not saying that any approach doesn't work, but I am saying that I've learnt from experience that actually formalising my question precisely as `definition : blah := sorry` or `theorem : blah := sorry` really helps me to understand what I am asking before I ask it.

