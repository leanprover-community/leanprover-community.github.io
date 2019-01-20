---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: LeanTogether2019/Unificationhintspaper.html
---

## [Lean Together 2019](index.html)
### [Unification hints paper](Unificationhintspaper.html)

#### Johan Commelin (Jan 15 2019 at 13:06):
And then, in the talk they used "canonical structures" instead of type class inference. I don't know if unification hints would give an additional benefit over type class inference...

#### Johan Commelin (Jan 15 2019 at 13:07):
I really like Reid's example. @**Mario Carneiro** What is your opinion on these things? Do you think they are useful? Or just cute hacks?

#### Kevin Buzzard (Jan 15 2019 at 13:08):
My very poor understanding of Cyril's point was that canonical structures and unification hints made a different part of the system do the work.

#### Mario Carneiro (Jan 15 2019 at 13:08):
I've used them in restricted circumstances

#### Mario Carneiro (Jan 15 2019 at 13:08):
this is slightly different from Cyril's unification hints

#### Mario Carneiro (Jan 15 2019 at 13:09):
I have an example from `dioph` where I use typeclass inference to prove natural number inequalities so I can write things like `&5 : fin 10` with an appropriate notation

#### Kevin Buzzard (Jan 15 2019 at 13:09):
Can one prove `a+b+c+d+e+f+g+h=b+(f+h)+(c+e+(a+g+d))` like this?

#### Mario Carneiro (Jan 15 2019 at 13:10):
not easily

#### Kevin Buzzard (Jan 15 2019 at 13:11):
I'll stick to `ring` :-)

#### Gabriel Ebner (Jan 15 2019 at 13:38):
@**Kevin Buzzard** Of course you can, thanks for asking!  (But seriously, please use `simp` or `ring` instead.)
```lean
universes u

class ac_cancel_core {α : Type u} [add_comm_monoid α] (a : α) (b : α) (c : out_param α) :=
(is_eq : b = a + c)

namespace ac_cancel_core

variables {α : Type u} [add_comm_monoid α] (a b c d : α)

instance left [h : ac_cancel_core a b d] : ac_cancel_core a (b+c) (d+c) := ⟨by simp [h.is_eq]⟩
instance right [h : ac_cancel_core a c d] : ac_cancel_core a (b+c) (b+d) := ⟨by simp [h.is_eq]⟩
instance refl : ac_cancel_core a a 0 := ⟨by simp⟩

end ac_cancel_core

class ac_cancel {α : Type u} [add_comm_monoid α] (a : α) (b : α) (c : out_param α) :=
(is_eq : b = a + c)

namespace ac_cancel

variables {α : Type u} [add_comm_monoid α] (a b c d e : α)

instance core [h : ac_cancel_core a b c] : ac_cancel a b c := ⟨by simp [h.is_eq]⟩
instance zero : ac_cancel 0 b b := ⟨by simp⟩
instance plus [h1 : ac_cancel a c d] [h2 : ac_cancel b d e] : ac_cancel (a+b) c e :=
⟨by simp [h1.is_eq, h2.is_eq]⟩

end ac_cancel

lemma ac_refl {α : Type u} [add_comm_monoid α] {a b : α} [h : ac_cancel a b 0] : a = b :=
by simp [h.is_eq]

example (a b c : ℕ) : a+(c+b) = (c+a)+b := ac_refl
example (a b c : ℕ) : a+b = b+a := ac_refl

-- fails due to maximum class instance depth
example (a b c d e f g h : ℕ) : a+b+c+d+e+f+g+h=b+(f+h)+(c+e+(a+g+d)) :=
ac_refl
```

#### Kevin Buzzard (Jan 15 2019 at 13:42):
Oh wow! :-) So again if I've understood correctly, this is Lean's type class unification doing the work here, so C++, as opposed to if I used `ring` when it would be an algorithm written in Lean. 

Wait -- did Gabriel just write the `add_comm_group` tactic which sometimes comes up? After Mario's `ring` people noticed that whilst it solved many of the questions that schoolkids would find trivial (like the one in my example), we were missing variants. One was a variant which solved problems in `add_comm_group`s and one was a variant which solved problems in modules. Neither of these things are rings, so the tactic had limited use in these situations.

#### Kevin Buzzard (Jan 15 2019 at 13:43):
Or maybe `simp` already does this case? But again this is a different part of the system I guess.

#### Mario Carneiro (Jan 15 2019 at 13:43):
I would say that the algorithm is "written in lean" in this case

#### Mario Carneiro (Jan 15 2019 at 13:43):
it's basically using lean like prolog

#### Mario Carneiro (Jan 15 2019 at 13:43):
remember that "prolog like search" thing?

#### Kevin Buzzard (Jan 15 2019 at 13:43):
vividly

#### Mario Carneiro (Jan 15 2019 at 13:44):
this is how you write programs in prolog, as big backtracking searches

#### Mario Carneiro (Jan 15 2019 at 13:44):
you have to be very careful about what instances you put in the classes, as they control the search

#### Patrick Massot (Jan 15 2019 at 14:24):
See also the examples in https://github.com/leanprover/presentations/tree/master/20170116_POPL/backchain

#### Patrick Massot (Jan 15 2019 at 14:26):
In particular https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/back.lean#L87-L88 directly mentions that paper

