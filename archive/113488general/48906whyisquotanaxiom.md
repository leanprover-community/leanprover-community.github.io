---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48906whyisquotanaxiom.html
---

## Stream: [general](index.html)
### Topic: [why is quot an axiom?](48906whyisquotanaxiom.html)

---

#### [Kevin Buzzard (Dec 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363029):
Can't we just do it like this?

```lean
import tactic.interactive

-- Lean has the "quotient" function to make equivalence classes.
-- Here I try to figure out why it is needed.

universes u v

namespace xena

-- this doesn't work with Prop but do I care?

variable {β : Type u}
variable (r : β → β → Prop)

-- equiv reln closure of r
inductive requiv {β : Type u} (r : β → β → Prop) : β → β → Prop
| of_r (a b : β) : r a b → requiv a b
| refl (a : β) : requiv a a
| symm ⦃a b : β⦄ : requiv a b → requiv b a
| trans ⦃a b c : β⦄ : requiv a b → requiv b c → requiv a c

definition equiv_class (r : β → β → Prop) (b : β) : set β := {c : β | requiv r b c}

definition quot {β : Type u} (r : β → β → Prop) : Type u :=
{eq_cl : set β // ∃ a : β, equiv_class r a = eq_cl}

namespace quot

definition mk : Π {α : Type u} (r : α → α → Prop), α → quot r :=
λ α r a, ⟨equiv_class r a,a,rfl⟩

theorem ind : ∀ {α : Type u} {r : α → α → Prop} {β : quot r → Prop},
    (∀ (a : α), β (mk r a)) → ∀ (q : quot r), β q :=
λ α r β h q,
begin
  rcases q with ⟨C,a,Ha⟩,
  convert h a,
  rw Ha,
end

noncomputable definition lift :
  Π {α : Type u} {r : α → α → Prop} {β : Sort v} (f : α → β),
    (∀ (a b : α), r a b → f a = f b) → quot r → β :=
λ α r β f h q,begin
  apply f,
  rcases q with ⟨C,HC⟩,
  -- cases HC with a Ha, MEH
  let a := classical.some HC,
  have Ha : equiv_class r a = C := classical.some_spec HC,
  -- ask about better way
  exact a,
end

definition sound : ∀ {α : Type u} {r : α → α → Prop} {a b : α}, r a b → quot.mk r a = quot.mk r b :=
λ α r a b h,begin
  unfold mk,
  suffices : equiv_class r a = equiv_class r b,
    simp [this],
  ext,
  split,
  { intro Hx,
    show requiv r b x,
    apply requiv.trans _ Hx,
    apply requiv.symm,
    apply requiv.of_r,
    assumption,
  },
  { intro Hx,
    show requiv r a x,
    apply requiv.trans _ Hx,
    apply requiv.of_r,
    assumption,
  }
end

end quot

end xena
```

I think I do all the basic theory of `quot`. I've been teaching quotients (in ZFC) in my class and I was trying to figure out how to explain to mathematicians why all this `quot.sound` stuff all had to be dealt with via extra axioms, but I've just done it all myself. The two sacrifices I had to make were: (1) it doesn't work for props (but who takes a quotient on proofs of a prop?) and (2) `lift` (the map which mathematicians think of as a "descent", quite the other direction to the computer science word) is noncomputable. What does `quot.sound` offer that my set-up doesn't but which I want or need?

#### [Kevin Buzzard (Dec 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363044):
I just make the quotient type as a bunch of equivalence classes.

#### [Kevin Buzzard (Dec 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363092):
A subtype of `set β` consisting of the equiv classes.

#### [Reid Barton (Dec 21 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363322):
The differences are that `lift` is computable, and `lift f _ (mk r x) = f x`(which it looks like you haven't proved, but I'm sure you can) hold definitionally (this is `quot.lift_beta`).

#### [Kevin Buzzard (Dec 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152364358):
Actually I'm struggling with the theorem about lift:

```lean
-- the computation principle
variables (β : Type v) (f : α → β) (a : α)
variable (h : ∀ a b , r a b → f a = f b)
theorem thm : lift f h (mk r a) = f a := begin
  rcases (mk r a) with ⟨C,HC⟩, -- HC has nothing to do with a now.
  let b := classical.some HC,
  have Hb : equiv_class r b = C := classical.some_spec HC,
/-
α : Type u,
r : α → α → Prop,
β : Type v,
f : α → β,
a : α,
h : ∀ (a b : α), r a b → f a = f b,
C : set α,
HC : ∃ (a : α), equiv_class r a = C,
b : α := classical.some HC,
Hb : equiv_class r b = C
⊢ lift f h ⟨C, HC⟩ = f a
-/
  show f b = f a,
  apply h b a,
  -- but I don't know a ∈ C
  sorry
end
```

#### [Chris Hughes (Dec 22 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152367268):
Also, your proof of `sound` uses `quot.sound`

#### [Kevin Buzzard (Dec 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152386750):
Oh does it? I suppose that's cheating :-)

#### [Mario Carneiro (Dec 22 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152387461):
You use set extensionality in the proof, which is an axiom in ZFC and is derived from `propext` and `quot.sound` in lean

#### [Kevin Buzzard (Dec 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152462524):
OK so I proved `xena.quot.thm`. I think definitional equality is overrated, and if I have my maths hat on I'd say the same about computability. I am concerned about Chris' comment though. I am doing this to try and figure out how to explain to mathematicians why Lean wants quotients to be an extra axiom. But set extensionality is implied by function extensionality, right? Would another approach have been to make funext and/or propext axioms and then get quotients using my method? At least if we decide not to care about computability and definitional equality and be 100% mathematician.

#### [Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463063):
yes, that's called zfc

#### [Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463066):
you make set.ext an axiom

#### [Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463070):
and derive funext and the others by constructing everything from sets

#### [Mario Carneiro (Dec 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463123):
if you want to convince yourself, make a copy of `set.ext` as an actual axiom, and then derive all that and check that you didn't use propext or quot.sound in `#print axioms`

