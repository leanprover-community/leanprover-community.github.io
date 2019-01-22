---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67736errorfailedtounify.html
---

## [general](index.html)
### [error: failed to unify](67736errorfailedtounify.html)

#### [Johan Commelin (May 25 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error: failed to unify/near/127084634):
I am at a stage where I am currently hitting errors of the following type
```lean
invalid apply tactic, failed to unify
  p.fst = q.fst
with
  ?m_2 = ?m_3
```
I have no clue why Lean can't unify those... probably there are some hidden metavariables somewhere... how do I get more info?

#### [Johannes Hölzl (May 25 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error: failed to unify/near/127084763):
can you try to use `set_option pp.all true` and inspect the term again

#### [Johan Commelin (May 25 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error: failed to unify/near/127085460):
Thanks, the response by Lean was a little bit overwhelming. But it solved my problem!

