---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03027wellfoundedrecursion.html
---

## [general](index.html)
### [well_founded recursion](03027wellfoundedrecursion.html)

#### [petercommand (Dec 16 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151874709):
Given that a relation ```R : a -> a -> Prop``` satisfies ```{ f : stream a // forall n, R (f (n + 1)) (f n)} -> false```, is it possible to get ```well_founded R```?

#### [petercommand (Dec 16 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151874716):
i.e. translate the traditional no infinite chain condition to well_founded in lean

#### [Chris Hughes (Dec 16 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151876319):
```lean
example {α : Type*} (r : α → α → Prop)
  (h : Π f : ℕ → α, ∃ n, ¬r (f (n + 1)) (f n)) : 
  well_founded r :=
let f : Π a : α, ¬ acc r a → {b : α // ¬ acc r b ∧ r b a} :=
  λ a ha, classical.indefinite_description _ 
    (classical.by_contradiction 
      (λ hc, ha $ acc.intro _ (λ y hy, 
        classical.by_contradiction (λ hy1, hc ⟨y, hy1, hy⟩)))) in
well_founded.intro 
  (λ a, classical.by_contradiction 
    (λ ha, let g : Π n : ℕ, {b : α // ¬ acc r b} := λ n, nat.rec_on n ⟨a, ha⟩ 
        (λ n b, ⟨f b.1 b.2, (f b.1 b.2).2.1⟩ ) in 
      have hg : ∀ n, r (g (n + 1)) (g n), 
        from λ n, nat.rec_on n (f _ _).2.2 
          (λ n hn, (f _ _).2.2), 
      exists.elim (h (subtype.val ∘ g)) (λ n hn, hn (hg _))))
```

#### [petercommand (Dec 16 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151876769):
Thanks!

#### [Chris Hughes (Dec 16 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151878820):
PRed #519

#### [Kenny Lau (Dec 16 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151879289):
maybe we should prove the axiom of dependent choice

#### [Chris Hughes (Dec 16 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151879296):
What is that?

#### [Reid Barton (Dec 16 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151887313):
There's also `well_founded_iff_no_descending_seq` already although the formulation is slightly different.

#### [Kevin Buzzard (Dec 16 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151887541):
```quote
What is that?
```
 In ZFC, countable dependent choice (DC) is the form of the axiom of choice which is used most often by mathematicians, usually without them even noticing. At the n'th step, n a natural, you have a non-empty set of things to choose from, and you choose one and call it $$x_n$$. Then the $$n+1$$ st non-empty set appears (and this set could depend on the choice you made, hence "dependent", but it's certainly non-empty) and you can choose something from that, and so on. Mathematicians would use it to do the following sort of thing: if $$S$$ is a set of reals with the property that $$\forall\epsilon>0, \exists s\in S$$ with $$|s|<\epsilon$$, then to get a sequence $$s_1,s_2,s_3,\ldots$$ of elements of $$S$$ that tend to zero you apply countable choice to create a sequence with the property that $$|s_n|<1/n$$.

#### [Kevin Buzzard (Dec 16 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151887609):
Aah. To get a non-increasing sequence you could use countable dependent choice.

#### [Reid Barton (Dec 16 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded%20recursion/near/151888044):
https://gist.github.com/rwbarton/7bd5b3b19d930f577355a596a5ed8b4d is basically dependent choice, without the choice part (but you could use choice in the inductive step)

