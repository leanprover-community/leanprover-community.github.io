---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21143newbieprooffromassumptionofinductivelydefinedprop.html
---

## [general](index.html)
### [newbie: proof from assumption of inductively defined prop](21143newbieprooffromassumptionofinductivelydefinedprop.html)

#### [Kevin Sullivan (Oct 17 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135988274):
Given a typical definition of an evenness property ...

```lean
inductive ev: ℕ → Prop 
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)
```

Here's a script that proves that 7 isn't even:

```lean
example : ¬ ev 7 :=
begin
assume ev7,
cases ev7 with ev5,
cases ev7_a,
cases ev7_a_a,
cases ev7_a_a_a,
end
```

To prove that 8 is even, I can use repeat { apply ev_SS }.

What is a stylistically nicer way to prove that 7 isn't even.

#### [Kevin Buzzard (Oct 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135989820):
You could move this thread into the `new members` stream. And if you're posting code you can triple quote it: write ` ```lean ` at the beginning and ` ``` ` at the end. For your question: you could prove `ev n` was decidable, and then `dec_trivial` would decide it.

#### [Andrew Ashworth (Oct 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135990543):
I think this is something that can be improved in Lean 4, when reflection runs a bit faster. https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-camera-ready.pdf

#### [Andrew Ashworth (Oct 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135990685):
the paper's first few sections go through several ways of implementing an evenness checker

#### [Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992402):
got it:

```lean
instance decidable_ev : ∀ n, decidable (ev n)
| 0 := is_true ev_0
| 1 := is_false (λ ev1, by cases ev1)
| (n + 2) := decidable_of_decidable_of_iff (decidable_ev n) $ (ev_SS_iff n).symm

example : ¬ ev 7 := dec_trivial
```

#### [Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992403):
dammit I failed:

```lean
inductive ev : ℕ → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

open ev

lemma ev_SS_iff (n : ℕ) : ev (n + 2) ↔ ev n :=
begin
  split,
  { -- cases way
    intro evSS,
    cases evSS,
    assumption
  },
  { -- easy way
    exact ev_SS n
  }
end

open ev

instance decidable_ev : ∀ n, decidable (ev n)
| 0 := is_true ev_0
| 1 := is_false (λ ev1, by cases ev1)
| (n + 2) := begin rw ev_SS_iff n, exact decidable_ev n end

example : decidable (ev 2) := by apply_instance

example : ev 2 := dec_trivial -- fails
/-
exact tactic failed, type mismatch, given expression has type
  true
but is expected to have type
  as_true (ev 2)
state:
⊢ as_true (ev 2)
-/
```

#### [Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992404):
```lean
example : ¬ (ev 7) :=
begin
  repeat {rw ev_SS_iff},
  intro ev1,cases ev1
end
```
is an answer (using the lemma I proved in the previous post).

#### [Kevin Buzzard (Oct 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992525):
Sorry, had dodgy internet and posts have appeared in random order

#### [Chris Hughes (Oct 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992534):
I'm guessing `dec_trivial` failed because you didn't make decidable an instance.

#### [Kevin Buzzard (Oct 17 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992607):
My rw proof doesn't work for some reason

#### [Scott Olson (Oct 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992638):
I think the problem is rewriting with an `iff` invokes propext which then cannot reduce?

#### [Scott Olson (Oct 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992659):
```lean
#eval (ev 2 : bool) -- tt
#reduce (ev 2 : bool) -- decidable.rec (λ (h : ev 2 → false), ff) (λ (h : ev 2), tt) (eq.rec (is_true ev_0) _)
```

#### [Scott Olson (Oct 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992755):
If you `set_option pp.proofs true` the innocent little `_` there is `(propext <large iff structure expression>)`

#### [Kevin Buzzard (Oct 17 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992771):
Nice!

#### [Kenny Lau (Oct 17 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992968):
```lean
inductive ev : ℕ → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

instance : decidable_pred ev
| 0 := is_true ev.ev_0
| 1 := is_false $ λ H, by cases H
| (n+2) := match ev.decidable_pred n with
    | is_true H := is_true (ev.ev_SS n H)
    | is_false H := is_false (λ h, by cases h with h h; exact H h)
    end
```

#### [Chris Hughes (Oct 17 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993101):
@**Kenny Lau** now that we've established that "computable" functions aren't really computable unless you avoid `propext` and `quot.sound`, are you going to start avoiding those axioms as well?

#### [Kenny Lau (Oct 17 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993158):
```lean
inductive ev : ℕ → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

theorem ev_iff (n : ℕ) : ev n ↔ ev (n + 2) :=
⟨ev.ev_SS n, λ H, by cases H with h h; exact h⟩

instance decidable_ev : ∀ n, decidable (ev n)
| 0 := is_true ev.ev_0
| 1 := is_false (λ ev1, by cases ev1)
| (n + 2) := decidable_of_decidable_of_iff (decidable_ev n) (ev_iff n)
```

#### [Kenny Lau (Oct 17 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993447):
```lean
inductive ev : ℕ → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

def ev_b : ℕ → bool
| 0 := tt
| 1 := ff
| (n+2) := ev_b n

theorem ev_iff : ∀ n, ev_b n ↔ ev n
| 0 := ⟨λ _, ev.ev_0, λ _, rfl⟩
| 1 := ⟨λ ev1, by cases ev1, λ ev1, by cases ev1⟩
| (n+2) := ⟨λ evss, ev.ev_SS n ((ev_iff n).1 evss),
    λ evss, by cases evss with _ evss; exact (ev_iff n).2 evss⟩

instance : decidable_pred ev :=
λ n, decidable_of_decidable_of_iff infer_instance (ev_iff n)
```

#### [Mario Carneiro (Oct 17 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135998146):
You should use `bodd` instead, it has an efficient implementation in VM and a not stupid implementation in kernel

