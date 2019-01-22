---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/64616metadefsyntaxerror.html
---

## [new members](index.html)
### [meta def syntax error](64616metadefsyntaxerror.html)

#### [Ken Roe (Jul 18 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846795):
I was trying out the example from the Lean meta programming paper.  However their example gives a syntax error:

```lean
open tactic
open monad
open expr
open smt_tactic

meta def findd : expr → list expr → tactic expr
| e [] := failed
| e (h::hs) :=
    do t ← infer_type h,
    (unify e t >> return h) <|> find e hs.
```

The "return" statement gives the following error:  (Ignore the line numbers, I've got other stuff in the file)

```lean
traversal.lean:88:18: error
invalid expression
traversal.lean:88:18: error
command expected
```

This is with Lean 3.4.1.  How do I fix the error?

#### [Mario Carneiro (Jul 18 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846865):
the name of the def is `findd`?

#### [Mario Carneiro (Jul 18 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846918):
the `command expected` error is often fixed by scrolling down or setting the lean checking mode (on the status bar) to "check visible files" instead of "check visible lines"

#### [Reid Barton (Jul 18 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129848796):
Or restarting lean.

