---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/50863transfinitecompositions.html
---

## Stream: [maths](index.html)
### Topic: [transfinite compositions](50863transfinitecompositions.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128023):
Suppose P is a complete lattice. I can define an increasing sequence of finite length in P either as a subtype of a function type or as an inductive type, as shown below.
```lean
import order.complete_lattice
open lattice
variables {P : Type} [complete_lattice P]

def seq1 (n : ℕ) : Type := {f : fin (n+1) → P // ∀ i j, i ≤ j → f i ≤ f j}
inductive seq2 (a : P) : P → ℕ → Type
| nil : seq2 a 0
| cons : Π b b' n, seq2 b n → b ≤ b' → seq2 b' (n+1)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128069):
The first one generalizes easily to any ordinal (or any well-ordered set). Is there a way to generalize the second?
I mention that P is a complete lattice because I'm happy to assume (if it helps) that at each limit stage, the value of the sequence is equal to the sup of all the previous values.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128599):
The only way I can think to handle limit ordinal stages is to ask for an increasing sequence of every smaller ordinal length, such that for any α ≤ β, the sequence of length α is a prefix of the sequence of length β

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128603):
But this seems a bit awkward.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128630):
(What I'm really trying to do is model https://ncatlab.org/nlab/show/transfinite+composition)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128804):
I'm not sure if this is what you're looking for. The following is used in Isabelle to model transfinite recursion:
```isabelle
inductive_set iterates :: "('a ⇒ 'a) ⇒ 'a set" for f :: "'a ⇒ 'a" where
| step: "x ∈ iterates f ⟹ f x ∈ iterates f"
| Sup: "chain (≤) M ⟹ ∀x∈M. x ∈ iterates f ⟹ Sup M ∈ iterates f"
```
Maybe you can use a similar approach?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128831):
Hmm, interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128899):
Indeed we basically always construct such transfinite compositions by iterating some construction at successor stages, and taking a sup/colimit at limit stages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128922):
What kind of thing is M there? a subset of 'a?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129010):
and `chain (≤)` means it's totally ordered?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129169):
Ah, I found the source.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129173):
Yes, `M` is a subset of `'a` and `chain (≤) M` says that `M` is totally ordered

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129410):
the interesting part is that `iterates` is a `chain` in itself, so it contains its supremum, which is the fixed point of `f`.  In this theory `'a` is a chain complete partial order (i.e. all non-empty chains have a supremum)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134133872):
One thing that occurs to me is that my finite sequences are themselves partially ordered by "extends", and the finite prefixes of a countable sequence form a chain

