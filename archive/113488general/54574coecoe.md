---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54574coecoe.html
---

## Stream: [general](index.html)
### Topic: [coe_coe](54574coecoe.html)

---

#### [Chris Hughes (May 01 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125958400):
Just noticed the lemma `coe_coe`, which is tagged as `simp`, does this mean I need to be careful about tagging lemmas that make a double coercion into a single coercion with simp?

#### [Kenny Lau (May 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960662):
```quote
Just noticed the lemma `coe_coe`, which is tagged as `simp`, does this mean I need to be careful about tagging lemmas that make a double coercion into a single coercion with simp?
```
yes

#### [Chris Hughes (May 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960853):
What's the difference between `has_coe` and `has_coe_t`?

#### [Kenny Lau (May 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960953):
L37:
```lean
class has_coe (a : Sort u) (b : Sort v) :=
(coe : a → b)

/-- Auxiliary class that contains the transitive closure of has_coe. -/
class has_coe_t (a : Sort u) (b : Sort v) :=
(coe : a → b)
```
-------------
L94:
```lean
instance coe_trans {a : Sort u₁} {b : Sort u₂} {c : Sort u₃} [has_coe a b] [has_coe_t b c] : has_coe_t a c :=
⟨λ x, coe_t (coe_b x : b)⟩
```

#### [Kevin Buzzard (May 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961550):
Maybe the type class coercion system uses this instance?

#### [Kenny Lau (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961600):
curiously, this `has_coe_t` appears literally nowhere

#### [Kevin Buzzard (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961607):
Did you check the C++ bit?

#### [Kenny Lau (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961611):
maybe it's because of this:
```lean
instance coe_to_lift {a : Sort u} {b : Sort v} [has_coe_t a b] : has_lift_t a b :=
⟨coe_t⟩

```

#### [Kenny Lau (May 01 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961620):
so my conjecture is that they use `has_coe_t` to do transitive stuff, and then make `has_lift_t` the interface

#### [Kevin Buzzard (May 01 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961671):
I remember Mario once saying something like he couldn't see the point of has_lift

#### [Kevin Buzzard (May 01 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961673):
There's something about it in TPIL IIRC

#### [Chris Hughes (May 01 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961919):
So I don't need to worry unless it's a `coe_t`. The reason I noticed is because the coercion from pnat to int is a coe_t obviously, so it was being rewritten by coe_coe.

#### [Chris Hughes (May 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962001):
Which means I need double the lemmas

#### [Kevin Buzzard (May 01 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962030):
Has_lift gives you access to the \u uparrow notation but lean won't ever insert them for you if you're not has_coe

#### [Kevin Buzzard (May 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962081):
But each lemma is twice as easy to prove 🙂

#### [Mario Carneiro (May 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984523):
You shouldn't need "double the lemmas", you just need to make sure that any simp lemmas LHS are already split up into multiple coe arrows

#### [Chris Hughes (May 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984671):
But I also want the single arrows for rw's, because if I don't use simp, most of my coercions are single coercions

#### [Mario Carneiro (May 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984685):
why are you using composite coercions to begin with?

#### [Mario Carneiro (May 02 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984693):
I honestly wish the parser inserted multiple coe arrows, but the best I can do to recreate that is `coe_coe`

#### [Mario Carneiro (May 02 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984738):
but you can always write `((a:B):C)` to get multiple coe arrows inserted

#### [Kevin Buzzard (May 02 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987058):
He wants to go from `pnat` to `int`

#### [Mario Carneiro (May 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987205):
I can see that. But why? What is the simp lemma under consideration? Like I said, you can use `((n:nat):int)` to double-coerce

#### [Chris Hughes (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987207):
But that means having to type ((n : nat):int) all the time, instead of just n.

#### [Mario Carneiro (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987218):
all the time meaning only on the LHS of rules marked `[simp]`

#### [Mario Carneiro (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987222):
in proofs you can do whatever

#### [Mario Carneiro (May 02 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987263):
but it is important to state your lemmas correctly

#### [Chris Hughes (May 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987270):
But for any lemma marked simp, I also want it's single coercion corollary if I want to rewrite something.

#### [Mario Carneiro (May 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987271):
like what?

#### [Mario Carneiro (May 02 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987314):
just `rw coe_coe`

#### [Chris Hughes (May 02 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987315):
I could do that too.

#### [Mario Carneiro (May 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987320):
I think you underestimate the number of "single coercion corollaries"

#### [Mario Carneiro (May 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987321):
(hint: it's infinite)

#### [Kenny Lau (May 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987359):
infinity doesn't exist

#### [Mario Carneiro (May 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987364):
and neither do those corollaries, in mathlib

