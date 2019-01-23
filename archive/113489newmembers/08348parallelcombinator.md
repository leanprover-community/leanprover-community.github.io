---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/08348parallelcombinator.html
---

## Stream: [new members](index.html)
### Topic: [parallel combinator](08348parallelcombinator.html)

---

#### [Olli (Sep 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133876440):
is there a way to use the `exact` tactic with the parallel tactic combinator:

works:
```lean
example : p ∧ q ↔ q ∧ p :=
begin
  split,
  exact λ ⟨h1, h2⟩, ⟨h2, h1⟩,
  exact λ ⟨h1, h2⟩, ⟨h2, h1⟩,
end
```

fails:
```lean
example : p ∧ q ↔ q ∧ p :=
begin
  split;
  exact λ ⟨h1, h2⟩, ⟨h2, h1⟩,
end
```

with:
```
equation compiler failed to create auxiliary declaration '_example._match_1'
nested exception message:
invalid object declaration, environment already has an object named '_example._match_1'
```

#### [Kenny Lau (Sep 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133886990):
does `rintro` work?

#### [Ali Sever (Sep 13 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133901349):
This also works,
```lean
example : p ∧ q ↔ q ∧ p :=
begin
  split;
  exact and.symm
end
```

#### [Mario Carneiro (Sep 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133901899):
@**Sebastian Ullrich** This seems to be indicative of a very strange dependency between parsing and creating definitions. Does this still behave the same way in lean 4?

#### [Mario Carneiro (Sep 13 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133903258):
Oh wow, this is stranger than I thought.
```lean
open tactic

meta def mytac : tactic unit :=
do tgt ← target,
   i_to_expr_strict ``(λ ⟨h1, h2⟩, ⟨h2, h1⟩ : %%tgt) >>= exact

meta def twice (tac : tactic unit) : tactic unit := tac >> tac

example {p q : Prop} : p ∧ q ↔ q ∧ p := -- doesn't work
begin
  split,
  twice (do {
    tgt ← target,
    i_to_expr_strict ``(λ ⟨h1, h2⟩, ⟨h2, h1⟩ : %%tgt) >>= exact
  })
end

example {p q : Prop} : p ∧ q ↔ q ∧ p := -- works
begin
  split,
  do {
    tgt ← target,
    i_to_expr_strict ``(λ ⟨h1, h2⟩, ⟨h2, h1⟩ : %%tgt) >>= exact,
    tgt ← target,
    i_to_expr_strict ``(λ ⟨h1, h2⟩, ⟨h2, h1⟩ : %%tgt) >>= exact
  }
end

example {p q : Prop} : p ∧ q ↔ q ∧ p := -- works
begin
  split,
  twice mytac
end
```
My new theory is that it has something to do with the way a tactic is elaborated when it contains a subexpression with side effects like this

#### [Sebastian Ullrich (Sep 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133912590):
Yeah, `to_expr` is creating a new elaborator. This is horrible, haha

#### [Sebastian Ullrich (Sep 13 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133912887):
Well, I guess it could just skip auxiliary names that have already been taken

