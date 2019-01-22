---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50376Inductivedefinitions.html
---

## [new members](index.html)
### [Inductive definitions](50376Inductivedefinitions.html)

#### [Ken Roe (Aug 28 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926297):
I see a number of comments in my code that a definition of the form:
```lean
inductive allFirsts {t1} {t2} : list t1 → list (t1 × t2) → Prop
 | AFNil : allFirsts list.nil list.nil
 | AFCons : ∀ fx fy r r', allFirsts r r' → allFirsts (fx::r) ((fx,fy)::r')
```
can be rewritten as:
```lean
allFirsts l1 l2 <-> l2.map prod.fst = l1
```

The second form is not a complete definition.  How can I use this form as a definition?

#### [Chris Hughes (Aug 28 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926525):
`def allFirsts {t1 t2} (l1 : list t1) (l2 : list (t1 × t2)) : Prop := l2.map prod.fst = l1`

#### [Kevin Buzzard (Aug 28 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926967):
```lean
import tactic.interactive

inductive allFirsts {t1} {t2} : list t1 → list (t1 × t2) → Prop
 | AFNil : allFirsts list.nil list.nil
 | AFCons : ∀ fx fy r r', allFirsts r r' → allFirsts (fx::r) ((fx,fy)::r')

example {t1 t2} (l1 : list t1) (l2 : list (t1 × t2)) :
allFirsts l1 l2 <-> l2.map prod.fst = l1 :=
begin
  split,
    intro H,
    induction H,
    refl,
    simpa,
  intro H,
  induction H,
  induction l2 with f12 l2,
  exact allFirsts.AFNil,
  cases f12 with f1 f2,
  refine allFirsts.AFCons _ _ _ _ l2_ih,
end
```

