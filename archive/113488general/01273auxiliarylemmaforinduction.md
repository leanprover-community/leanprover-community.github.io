---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01273auxiliarylemmaforinduction.html
---

## Stream: [general](index.html)
### Topic: [auxiliary lemma for induction](01273auxiliarylemmaforinduction.html)

---

#### [Kevin Buzzard (Aug 23 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132633649):
```lean
structure foo :=
(size : ℕ)

definition auxiliary_thing (p : foo → Sort*) (m : ℕ)
(H0 : ∀ x : foo, x.size = 0 → p x)
(Hsucc : ∀ n : ℕ, 
  (∀ x : foo, x.size = n → p x) → (∀ x : foo, x.size = n+1 → p x)) :
∀ x : foo, x.size = m → p x :=
begin
  induction m with n Hn,
    exact H0,
  exact Hsucc n Hn,
end

/- What I actually want -/
definition foo.recurse_on_size (p : foo → Sort*)
(H0 : ∀ x : foo, x.size = 0 → p x)
(Hsucc : ∀ n : ℕ, 
  (∀ x : foo, x.size = n → p x) → (∀ x : foo, x.size = n+1 → p x)) :
∀ x : foo, p x :=
begin
  intro x,
  apply auxiliary_thing p (x.size) H0 Hsucc,
  refl,
end
```

Is this introduction of an auxiliary lemma a sensible way to go about things, or am I better off trying to prove what I want directly using some fancy equation compiler trickery?

#### [Simon Hudon (Aug 23 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132637724):
Are you using the auxiliary lemma in order to have `m` to do your induction on? Have you tried `generalize h : x.size = m, induction m with n Hn`?

#### [Kevin Buzzard (Aug 23 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132638452):
Aah that's the trick. Thanks Simon!

#### [Simon Hudon (Aug 23 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132639057):
Any time :)

#### [Simon Hudon (Aug 23 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132639260):
I wonder if it would be worth combining the two tactics so that `induction e` (with `e` an arbitrary expression) would produce the equality assumption.

