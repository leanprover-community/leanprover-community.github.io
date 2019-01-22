---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31377Traceofsimpsteps.html
---

## [new members](index.html)
### [Trace of "simp" steps](31377Traceofsimpsteps.html)

#### [Ken Roe (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Trace of "simp" steps/near/130300149):
I applied "simp" to a complex hypothesis and got an unexpected result.  Is there a way to get a trace of the steps taken by simp?

#### [Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Trace of "simp" steps/near/130300168):
```lean
set_option trace.simp_lemmas true
set_option trace.simplify true
```

#### [Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Trace of "simp" steps/near/130300170):
I think it's the second one

#### [Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Trace of "simp" steps/near/130300172):
but why not both

#### [Reid Barton (Jul 25 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Trace of "simp" steps/near/130300213):
trace.simplify.rewrite will show just the successful steps

