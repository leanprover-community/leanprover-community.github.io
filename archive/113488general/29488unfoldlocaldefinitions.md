---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29488unfoldlocaldefinitions.html
---

## [general](index.html)
### [unfold local definitions](29488unfoldlocaldefinitions.html)

#### [Reid Barton (May 10 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126372867):
Is there a way in tactic mode to unfold something bound by a surrounding `let`?

#### [Reid Barton (May 10 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373312):
I guess I also want to do a beta reduction, since the thing I want to unfold is a function whose definition is `assume x, ...`

#### [Gabriel Ebner (May 10 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373507):
You can do `dsimp [x]` if `x` is the let-binding in the local context.

#### [Gabriel Ebner (May 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373529):
```lean
example : let x := 5 in x + x > 0 :=
begin
intro x,
dsimp [x],
-- 5 + 5 > 0
end
```

#### [Reid Barton (May 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126375254):
Oh. Thanks!
I guess I never tried precisely this, but only `unfold` and `rw`.

