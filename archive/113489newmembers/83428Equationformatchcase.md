---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/83428Equationformatchcase.html
---

## Stream: [new members](index.html)
### Topic: [Equation for match-case](83428Equationformatchcase.html)

---

#### [Erika (Nov 09 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147352744):
Is there way to fill this hole (similar to coq's match-return)
```lean
match f x with
| case1 y := g x y (_: f x = case1 y)
| ...
end
```

#### [Mario Carneiro (Nov 09 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353395):
It's not built in to the `match` syntax, but there is a tactic for this, `cases`

#### [Mario Carneiro (Nov 09 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353401):
```
cases h : f x with y,
{ -- case1 y
  exact g x y h, }
```

#### [Erika (Nov 09 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353467):
ooh, that's good to know, I also noticed that `refine` will not make goals for `_` within a match arm

#### [Mario Carneiro (Nov 09 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353504):
Lean does have match-return as well, but you have to handhold it a bit to get this goal
```lean
match f x, rfl : ∀ a, f x = a → P with
| case1 y, h := g x y (h: f x = case1 y)
| ...
end
```

#### [Erika (Nov 09 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353510):
ah, I see, this is acceptable too

#### [Mario Carneiro (Nov 09 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353526):
I'm not sure I know what you mean by not making goals for `_`

#### [Mario Carneiro (Nov 09 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353529):
refine will make goals for anything it can't infer

#### [Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353575):
oh, maybe you mean `match` blocks refine because it uses the equation compiler (so it is typechecking in a different context, for a standalone definition)

#### [Erika (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353590):
```lean
def test (b: bool) : bool :=
begin
  refine (match b with | tt := tt | ff := _ end), -- error for _, instead of new goal
end
```

#### [Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353592):
right

#### [Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353593):
same happens when you use `let <...> = e1 in e2`

#### [Erika (Nov 09 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353604):
thanks for the help

#### [Mario Carneiro (Nov 09 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353611):
you can still use tactics in there, but you have to make a separate begin-end block

#### [Mario Carneiro (Nov 09 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353653):
```lean
def test (b: bool) : bool :=
begin
  exact (match b with | tt := tt | ff := begin
    ...
  end end),
end
```

