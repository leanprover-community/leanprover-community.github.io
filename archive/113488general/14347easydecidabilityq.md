---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14347easydecidabilityq.html
---

## Stream: [general](index.html)
### Topic: [easy decidability q](14347easydecidabilityq.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492071):
Is this provable:

```lean
import data.multiset
example (C : multiset ℕ) : decidable (∃ a : ℕ, a ≥ 4 ∧ a ∈ C) := sorry 
```

and if so, is there a cheap proof? I tried doing it by hand and ended up with a horrible heq goal :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492098):
yes it is provable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492116):
might want to destruct `C`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492249):
Isn't membership in multisets decidable? You combine that fact with decidability of existentials on finite ranges

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492333):
If I use lists I end up with
```
C1 C2 : list ℕ,
Crel : setoid.r C1 C2
⊢ eq.rec
      (list.rec (is_false _)
         (λ (n : ℕ) (L : list ℕ),
            decidable.rec
              (λ (D : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L),
                 dite (3 < n) (λ (h : 3 < n), is_true _) (λ (h : ¬3 < n), is_false _))
              (λ (D : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L), is_true _))
         C1)
      _ =
    list.rec (is_false _)
      (λ (n : ℕ) (L : list ℕ),
         decidable.rec
           (λ (D : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L),
              dite (3 < n) (λ (h : 3 < n), is_true _) (λ (h : ¬3 < n), is_false _))
           (λ (D : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L), is_true _))
      C2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492409):
If I use `multiset.rec` I end up with

```
a a' : ℕ,
m : multiset ℕ,
b : decidable (∃ (a : ℕ), a ≥ 4 ∧ a ∈ m)
⊢ decidable.rec
      (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ a' :: m),
         dite (3 < a) (λ (h : 3 < a), is_true _) (λ (h : ¬3 < a), is_false _))
      (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ a' :: m), is_true _)
      (decidable.rec
         (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ m),
            dite (3 < a') (λ (h : 3 < a'), is_true _) (λ (h : ¬3 < a'), is_false _))
         (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ m), is_true _)
         b) ==
    decidable.rec
      (λ (H : ¬∃ (a_1 : ℕ), a_1 ≥ 4 ∧ a_1 ∈ a :: m),
         dite (3 < a') (λ (h : 3 < a'), is_true _) (λ (h : ¬3 < a'), is_false _))
      (λ (H : ∃ (a_1 : ℕ), a_1 ≥ 4 ∧ a_1 ∈ a :: m), is_true _)
      (decidable.rec
         (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ m),
            dite (3 < a) (λ (h : 3 < a), is_true _) (λ (h : ¬3 < a), is_false _))
         (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ m), is_true _)
         b)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492413):
I assume I'm doing something wrong.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492442):
I think there might be some lemmas that one could use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492448):
bounded existential

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492681):
```quote
Isn't membership in multisets decidable? You combine that fact with decidability of existentials on finite ranges
```
`example (D : multiset ℕ) (d : ℕ) : decidable (d ∈ D) := by apply_instance ` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492691):
@**Kevin Buzzard** shouldn't you be watching the world cup?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492692):
Oh, has it started?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492694):
:o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492696):
it's already 67 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492939):
You can try this:

```lean
instance {α : Sort*} (P : α → Prop) (C : multiset α) : decidable (∃ a ∈ C, P a) :=
sorry

example (C : multiset ℕ) : decidable (∃ a : ℕ, a ≥ 4 ∧ a ∈ C) :=
suffices this : decidable (∃ a ∈ C, a ≥ 4), 
by { resetI, apply @decidable_of_iff _ _ _ this, apply exists_congr, intro, tauto }, 
by { apply_instance }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492951):
well you want P to be decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129493047):
Yes, that's right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129493435):
I don't understand how to use this code. If I comment out the instance then there's an error in the final `apply_instance` but if I look at what needs to be proved at that point it seems to be `decidable (∃ (a : ℕ) (H : a ∈ C), a ≥ 4)` which is exactly my question I think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494162):
Ok, one second I'm filling in that instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494757):
Add this before Simon'd code
```lean
instance decidable_exists_multiset {α : Type*} (s : multiset α) (p : α → Prop) [decidable_pred p] :
  decidable (∃ x ∈ s, p x) := quotient.rec_on s 
list.decidable_exists_mem (λ a b h, subsingleton.elim _ _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494794):
Nice! that's better than what I have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494850):
It would be worth pushing to mathlib I think along with a `finset` counterpart and decidable universals for both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494880):
Will do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494979):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500464):
Thanks to both of you! I cannot believe how much trouble Ellen's dots and boxes project is causing me :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500565):
What's that project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500822):
She's formalizing some of the theory of dots and boxes

