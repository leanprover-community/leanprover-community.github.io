---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/88568Unificationhintspaper.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [Unification hints paper](88568Unificationhintspaper.html)

---

#### [William Whistler (Jan 10 2019 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154848944):
https://www.cs.unibo.it/~sacerdot/PAPERS/tphol09.pdf

#### [Karl Palmskog (Jan 10 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154849729):
Paper by Gonthier et al. that takes unification hints to the limit for proof automation: https://software.imdea.org/~aleks/papers/lessadhoc/journal.pdf - see also Coq code with examples https://github.com/coq-community/lemma-overloading

#### [Andrew Ashworth (Jan 10 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154873490):
Interesting paper! I will have to explore the lemma-overloading library on the weekend.

#### [Assia Mahboubi (Jan 10 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154875627):
And here is the [tutorial paper](https://hal.inria.fr/hal-00816703/file/main.pdf), from proceedings of itp 2013, on which this afternoon demos were based.

#### [Johan Commelin (Jan 11 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154903922):
@**Scott Morrison|110087** This was an extremely interested session. Lean has support for unification hints, and nobody knew about it... :grinning: You might be interested, and I guess skimming these papers is one way to get up to speed.

#### [Johan Commelin (Jan 11 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154903964):
Assia, was very surprised to hear that we had unbundled categories. We could at some point try unification hints in the hierarchy of categorical classes.

#### [Karl Palmskog (Jan 12 2019 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154966221):
Aleks Nanevski recently presented the "unification hints to the limit" paper referenced above for a non-academic functional programming audience: https://www.youtube.com/watch?v=yFIaP1YCcxQ

#### [Johan Commelin (Jan 12 2019 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154983884):
That's a very nice talk! Thanks @**Karl Palmskog**
Tl;dr: If you hate rewriting stuff by associativity and commutativity, the speaker shows how to use unification hints to make this completely transparent.

#### [Reid Barton (Jan 15 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155160653):
Very nice indeed.
Here's a Lean analogue of the main example of the talk:
```lean
import order.lattice
open lattice
universe u
variables {α : Type u} [semilattice_sup α]

class le_sup_class (x y : α) : Prop :=
(le : x ≤ y)

instance le_sup_class_self (x : α) : le_sup_class x x :=
{ le := le_refl x }

instance le_sup_class_left (x y z : α) [h : le_sup_class x y] : le_sup_class x (y ⊔ z) :=
{ le := le_trans h.le le_sup_left }

instance le_sup_class_right (x y z : α) [h : le_sup_class x z] : le_sup_class x (y ⊔ z) :=
{ le := le_trans h.le le_sup_right }

def le_sup {x y : α} [h : le_sup_class x y] : x ≤ y := h.le

example {a b c d e : α} : a ≤ b ⊔ ((c ⊔ a) ⊔ d) ⊔ e :=
le_sup
```

#### [Reid Barton (Jan 15 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155161018):
I guess it could just be `le_class`--you could put the fact `x ⊓ y ≤ x` into the same system.

#### [Kevin Buzzard (Jan 15 2019 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155161531):
The point is that type class inference did the dirty work for you.

#### [Johan Commelin (Jan 15 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164104):
And then, in the talk they used "canonical structures" instead of type class inference. I don't know if unification hints would give an additional benefit over type class inference...

#### [Johan Commelin (Jan 15 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164150):
I really like Reid's example. @**Mario Carneiro** What is your opinion on these things? Do you think they are useful? Or just cute hacks?

#### [Kevin Buzzard (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164159):
My very poor understanding of Cyril's point was that canonical structures and unification hints made a different part of the system do the work.

#### [Mario Carneiro (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164160):
I've used them in restricted circumstances

#### [Mario Carneiro (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164208):
this is slightly different from Cyril's unification hints

#### [Mario Carneiro (Jan 15 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164233):
I have an example from `dioph` where I use typeclass inference to prove natural number inequalities so I can write things like `&5 : fin 10` with an appropriate notation

#### [Kevin Buzzard (Jan 15 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164258):
Can one prove `a+b+c+d+e+f+g+h=b+(f+h)+(c+e+(a+g+d))` like this?

#### [Mario Carneiro (Jan 15 2019 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164337):
not easily

#### [Kevin Buzzard (Jan 15 2019 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164358):
I'll stick to `ring` :-)

#### [Gabriel Ebner (Jan 15 2019 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165730):
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

#### [Kevin Buzzard (Jan 15 2019 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165937):
Oh wow! :-) So again if I've understood correctly, this is Lean's type class unification doing the work here, so C++, as opposed to if I used `ring` when it would be an algorithm written in Lean. 

Wait -- did Gabriel just write the `add_comm_group` tactic which sometimes comes up? After Mario's `ring` people noticed that whilst it solved many of the questions that schoolkids would find trivial (like the one in my example), we were missing variants. One was a variant which solved problems in `add_comm_group`s and one was a variant which solved problems in modules. Neither of these things are rings, so the tactic had limited use in these situations.

#### [Kevin Buzzard (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165968):
Or maybe `simp` already does this case? But again this is a different part of the system I guess.

#### [Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165972):
I would say that the algorithm is "written in lean" in this case

#### [Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165974):
it's basically using lean like prolog

#### [Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165981):
remember that "prolog like search" thing?

#### [Kevin Buzzard (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165984):
vividly

#### [Mario Carneiro (Jan 15 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155166033):
this is how you write programs in prolog, as big backtracking searches

#### [Mario Carneiro (Jan 15 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155166043):
you have to be very careful about what instances you put in the classes, as they control the search

#### [Patrick Massot (Jan 15 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155168520):
See also the examples in https://github.com/leanprover/presentations/tree/master/20170116_POPL/backchain

#### [Patrick Massot (Jan 15 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155168644):
In particular https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/back.lean#L87-L88 directly mentions that paper

