---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58749iffassoc.html
---

## Stream: [general](index.html)
### Topic: [iff.assoc](58749iffassoc.html)

---

#### [Kevin Buzzard (Jul 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294374):
Chris asked today if `iff` was associative and a room full of mathematicians had no clue between them :-) We proved it by checking all 8 cases in Lean :-) 

```lean
import tactic.finish 
open classical
example (P Q R : Prop) : ((P ↔ Q) ↔ R) ↔ (P ↔ (Q ↔ R)) :=
begin cases (em P);cases (em Q);cases (em R);finish 
end 
```

I was surprised that `finish` didn't do it alone:

```lean
-- example (P Q R : Prop) : ((P ↔ Q) ↔ R) ↔ (P ↔ (Q ↔ R)) := by finish -- fails
```

#### [Kevin Buzzard (Jul 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294462):
I later found a better proof: if we break with convention and define true = 0 and false = 1 then iff is addition mod 2, and addition mod 2 is associative.

Is it true constructively? I struggled, but then again I am certainly no expert.

#### [Kevin Buzzard (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294870):
Here's one place I get stuck:
```
P Q R : Prop,
HQPQ : Q → (P ↔ Q),
HPQQ : (P ↔ Q) → Q,
H : Q → P,
HP : P
⊢ Q
```

I eliminated R (WLOG I believe) and I can't see how to do this. I am now minded to look for a counterexample. @**Kenny Lau** to prove it's not constructively provable it would suffice to find some topological space with three subsets such that some random statement in topology is false, right?

#### [Simon Hudon (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294880):
I think `tauto` should manage to prove it

#### [Kevin Buzzard (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294921):
```
done tactic failed, there are unsolved goals
state:
P Q R : Prop,
a : P ↔ Q ↔ R,
a_1 : P,
a_2 : Q
⊢ R
```

#### [Kevin Buzzard (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294937):
Is `tauto` constructive?

#### [Patrick Massot (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294941):
Kevin, don't you have serious math to formalize?

#### [Kenny Lau (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294942):
I think so

#### [Kevin Buzzard (Jul 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295020):
Blame Chris. He pointed out that when a mathematician writes `A iff B iff C`, they mean `A iff B, and B iff C, so A iff C`, i.e. `iff.trans`. `iff.assoc` is a different question entirely :-) It's like the `1 <= k <= n` thing.

#### [Simon Hudon (Jul 25 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295036):
Yes, I believe it sticks to classical lemmas and if your propositions are decidable, it can prove more

#### [Patrick Massot (Jul 25 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295241):
The original question is perfectly legit, it's the constructivist deviance that I frown upon.

#### [Johan Commelin (Jul 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295283):
```quote
I later found a better proof: if we break with convention and define true = 0 and false = 1 then iff is addition mod 2, and addition mod 2 is associative.
```
That sounds like a proof by transport of structure (-;

#### [Chris Hughes (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298421):
```lean
lemma em_of_iff_assoc : (∀ p q r : Prop, ((p ↔ q) ↔ r) ↔ (p ↔ (q ↔ r))) → ∀ p, p ∨ ¬p :=
λ h p, ((h (p ∨ ¬p) false false).1
⟨λ h, h.1 (or.inr (λ hp, h.1 (or.inl hp))), λ h, h.elim⟩).2 iff.rfl

#print axioms em_of_iff_assoc
```

#### [Kevin Buzzard (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298440):
[no axioms]

#### [Kevin Buzzard (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298446):
Aah yes that's another way of resolving this

#### [Mario Carneiro (Jul 26 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130314672):
I recall having this exact conversation with Kenny a while ago (prove LEM from iff assoc)

#### [Kenny Lau (Jul 26 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323420):
it was xor assoc

#### [Chris Hughes (Jul 26 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323717):
Did you prove XOR assoc -> em?

#### [Kenny Lau (Jul 26 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323718):
```quote
so here is a proof of LEM from xor assoc:
```lean
example (h : ∀ p q r, xor p (xor q r) ↔ xor (xor p q) r) {p} : p ∨ ¬ p :=
have ¬ xor p p, from λ h, h.elim (λ ⟨hp, np⟩, np hp) (λ ⟨hp, np⟩, np hp),
have xor p (xor p true), from (h p p true).2 (or.inr ⟨trivial, this⟩),
this.imp and.left and.right
```
```
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/xor.20is.20not.20associative/near/125266318

#### [Kenny Lau (Jul 26 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323745):
by Mario

#### [Kevin Buzzard (Jul 26 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327664):
`xor` is associative because if you label false as 0 and true as 1 then it's addition mod 2. I thought it was funny that iff could be proved associative with the other labelling. It's almost like this is a proof strat and then you make all labellings and find out what each labelling proves :-)

#### [Kenny Lau (Jul 26 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327717):
can we create a Kripke frame where ((p ↔ q) ↔ r) but not (p ↔ (q ↔ r))?

#### [Kevin Buzzard (Jul 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327883):
`and` is associative because multiplication is associative, and `or` is associative because multiplication is associative. `nand` is not associative (however it is commutative, answering a question which an UG asked me last Oct -- "does commutative imply associative?")

#### [Kevin Buzzard (Jul 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327886):
Is a Kripke frame just a fancy name for a topological space in this context?

#### [Kenny Lau (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327900):
Kripke frame is a semantics for constructive logic

#### [Kenny Lau (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327903):
I think topological space is another semantics

#### [Patrick Massot (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327904):
topos!

