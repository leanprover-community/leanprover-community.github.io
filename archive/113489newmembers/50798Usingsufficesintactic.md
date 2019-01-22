---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50798Usingsufficesintactic.html
---

## [new members](index.html)
### [Using suffices in tactic](50798Usingsufficesintactic.html)

#### [Ken Roe (Jul 29 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using suffices in tactic/near/130509641):
```lean
theorem testit (f:ℕ) (s:ℕ) :
    (f,s).fst=f :=
begin
   do {
       t ← target,
       trace t.to_raw_fmt,
       suffices xx:(1==2),admit
   },
end
```
Can someone correct the syntax of the above.  I would like to use "suffices" rather than "change" for a tactic.  I get the following error:
```lean
test.lean:13:26: error
invalid expression, 'by', 'begin', '{', or 'from' expected
test.lean:13:26: error
invalid suffices-expression, term
  admit
has type
  tactic unit : Type
but is expected to have type
  1 == 2 : Prop
```

#### [Kenny Lau (Jul 29 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using suffices in tactic/near/130510012):
@**Ken Roe** what are your imports?

#### [Ken Roe (Jul 29 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using suffices in tactic/near/130510199):
```lean

open tactic
open monad
open expr
open smt_tactic.
```

#### [Kenny Lau (Jul 29 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using suffices in tactic/near/130510202):
...

#### [Simon Hudon (Jul 29 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using suffices in tactic/near/130514795):
those are not imports, they are open statements

