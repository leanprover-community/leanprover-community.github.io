---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02347namingpartofthegoal.html
---

## [general](index.html)
### [naming part of the goal](02347namingpartofthegoal.html)

#### [Reid Barton (Jan 01 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154143914):
I discovered a trick for referring to parts of the goal without having to write them out. For example, suppose your goal is to prove that some really complicated expression equals 0. You can give that expression a name `lhs` by writing
```lean
  let lhs := _,
  change lhs = 0,
```

#### [Patrick Massot (Jan 01 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154143960):
Oh, that's sneaky

#### [Patrick Massot (Jan 01 2019 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154143970):
It could be nice to wrap this trick in a small tactic

#### [Sebastian Ullrich (Jan 01 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154144846):
omg

#### [Patrick Massot (Jan 01 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154145021):
I can feel this trick won't be allowed in Lean 4...

#### [Kevin Buzzard (Jan 01 2019 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154146061):
(deleted)

#### [Sebastian Ullrich (Jan 02 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154146598):
@**Patrick Massot** I don't see anything wrong with any specific part here, it's more like a surprising combination of features

#### [Mario Carneiro (Jan 02 2019 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159623):
you can also use `let lhs, swap,` which is what I usually use for this trick

#### [Mario Carneiro (Jan 02 2019 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159626):
since there is no `let_suffices` tactic

#### [Mario Carneiro (Jan 02 2019 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159654):
I think having a tactic for this wouldn't be a bad idea though. Possibly using conv patterns to find the expression to name

#### [Mario Carneiro (Jan 02 2019 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159836):
How about this: `name foo + 1 + bar` will treat any undefined names in the expression like `foo` and `bar` as holes to be filled. It searches for the first unifying subterm of the goal (or hyps) and let binds them and replaces them in the target (not just in the pattern, in the whole goal). So if the goal is `(x - 3) + 1 + (y - 3) = x - 3` then the resulting goal is `foo := x - 3, bar := y - 3 |- foo + 1 + bar = foo`

#### [Mario Carneiro (Jan 02 2019 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159916):
It doesn't work in the presence of binders; or more specifically it won't match any open terms. I don't see what other option is available

#### [Mario Carneiro (Jan 02 2019 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154159984):
so if the goal was `\exists y, (x - 3) + 1 + y = x - 3` then the inner match `(x - 3) + 1 + #0` would be ignored

#### [Johan Commelin (Jan 02 2019 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming part of the goal/near/154163289):
@**Reid Barton** That's brilliant!

