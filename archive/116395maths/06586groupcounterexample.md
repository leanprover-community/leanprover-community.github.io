---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/06586groupcounterexample.html
---

## Stream: [maths](index.html)
### Topic: [group counterexample](06586groupcounterexample.html)

---

#### [Kevin Buzzard (Nov 23 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148214352):
Q1 part (i) on the 2nd year group theory sheet at Imperial (where $$G$$ is a group throughout) is "True or false : If we can find elements $$g$$, $$h$$ in $$G$$ such that $$gh = hg$$ then $$G$$ is abelian."

So this is false, and @**Amelia Livingston** and I were thinking about this question at Xena today. I wanted to formalise the question as closely as possible to the example sheet, so I wanted to write something like

```lean
theorem q1p1 : ¬ (∀ (G : Type*) [group G], (∃ g h : G, g * h = h * g) → is_abelian G) := sorry
```

You have to put the negation at the front of everything, so `group J` is after the colon and Lean doesn't know what `*` is. So version 2, which typechecks, is

```lean
theorem q1p1 : ¬ (∀ (G : Type*) [group G], by exactI (∃ g h : G, g * h = h * g) → is_abelian G) :=
```

But then we run into universe issues in the proof:

```lean
theorem q1p1 : ¬ (∀ (G : Type*) [group G], by exactI (∃ g h : G, g * h = h * g) → is_abelian G) :=
begin
  intro H
  replace H := H (perm (fin 3)), -- fails
```

The error is

```
type mismatch at application
  H (perm (fin 3))
term
  perm (fin 3)
has type
  Type : Type 1
but is expected to have type
  Type u_1 : Type (u_1+1)
```

I guess I understand that we can't do much about the `by exactI` stuff, but why can't Lean resolve my universe metavariable? Am I accidentally claiming that there are counterexamples in every universe?

#### [Johan Commelin (Nov 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148214469):
Yes you are

#### [Johan Commelin (Nov 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148214477):
Take `G : Type` instead of `Type*`. I think that will help

#### [Kevin Buzzard (Nov 23 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148216373):
But isn't that cheating?

#### [Kevin Buzzard (Nov 23 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148216392):
How do I formalise the statement that it is not true that for all groups in all universes, some stupid thing holds

#### [Kevin Buzzard (Nov 23 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148216435):
I want the quantifier in the not

#### [Kevin Buzzard (Nov 23 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148216437):
The universe quantifier

#### [Mario Carneiro (Nov 23 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148217061):
impossible

#### [Mario Carneiro (Nov 23 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148217069):
that's existential quantification over universes

#### [Mario Carneiro (Nov 23 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148217081):
What you can do instead is show a counterexample in a particular universe, which of course implies the existential that you can't write

#### [Kevin Buzzard (Nov 23 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20counterexample/near/148217369):
So do I have to use `ulift` to get `replace H := H (perm (fin 3))` working? I've never used `ulift` before.

