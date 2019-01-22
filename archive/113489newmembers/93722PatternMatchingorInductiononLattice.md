---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/93722PatternMatchingorInductiononLattice.html
---

## [new members](index.html)
### [Pattern Matching or Induction on Lattice?](93722PatternMatchingorInductiononLattice.html)

#### [AHan (Nov 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148769128):
If I have a type which is an instance of lattice, how can I pattern match or do induction on it?
For example,
```lean
import data.set.lattice
open lattice
variables {α : Type*} [semilattice_sup_bot α]
lemma x (p : α → β) :  ∀ (a : α), p a
| a :=
```

#### [Johan Commelin (Nov 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148770964):
@**AHan** Why are you trying to do?

#### [Johan Commelin (Nov 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148770966):
Pattern matching doesn't work on any odd type. (This has nothing to do with lattices.) You need `α` to be inductive.

#### [AHan (Nov 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148771305):
I want to prove something like
```lean
lemma lex_acc_of_bot : ∀ (a b : α) (l : list α), (ra a b) → acc (lex ra) (a :: l) := sorry
```

#### [Johan Commelin (Nov 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148771643):
Ok, I don't know enough about this... (I don't know what `ra` and `lex` are). But what had you hoped to pattern match on? Whether `a` was the bottom element, or something like that?

#### [Johan Commelin (Nov 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148771654):
For your lemma, you could do induction on the list; maybe that helps?

#### [AHan (Nov 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148771977):
Oh sorry I should say it clearer
```lean
inductive lex (r : α → α → Prop) : list α → list α → Prop
| nil {} {a l} : lex [] (a :: l)
| rel {a₁ a₂} (l₁ l₂ : list α) (h₁ : r a₁ a₂) (h₂ : l₁.length ≤ l₂.length) : lex (a₁ :: l₁) (a₂ :: l₂)
| cons {a l₁ l₂} (h : lex l₁ l₂) : lex (a :: l₁) (a :: l₂)
```
and `ra` is actually `lt`

#### [Kevin Buzzard (Nov 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148771981):
I found Chris' notes on well founded recursion very useful for this sort of thing.

#### [Kevin Buzzard (Nov 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148772038):
To get the equation compiler to match on a random thing, you need to explicitly trigger it with the `match` command. Hang on I'll get to a PC and send some links

#### [AHan (Nov 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148772043):
I have tried to do induction on list
But the lex order I defined doesn't necessarily decrease on the length of the list... I can't apply the induction hypothesis...

#### [Kevin Buzzard (Nov 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148772103):
https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#match-expressions for pattern matching

https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md for well-founded recursion

#### [AHan (Nov 29 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Pattern Matching or Induction on Lattice?/near/148772752):
@**Kevin Buzzard**  Thanks a lot for the sharing!
So I think the main problem here is, I have to prove that something will decrease....
And I have no idea how to prove this.... lol

