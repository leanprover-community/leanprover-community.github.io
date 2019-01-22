---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53958metareduceanexpr.html
---

## [general](index.html)
### [[meta] reduce an expr](53958metareduceanexpr.html)

#### [Zesen Qian (Aug 11 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968299):
So I have an `expr` of the form `not a`, can I evaluate this expr further? because `not` is defined as `\lam a, (a -> false)`.

#### [Zesen Qian (Aug 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968352):
`a` is of type `Prop`, BTW.

#### [Simon Hudon (Aug 11 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968459):
When you say evaluate, do you mean simplify? if so, you can find rules about `not` in `logic.basic` (mathlib) and `init.logic` (core), then you can call `simp [...]` with those rules your expression.

#### [Zesen Qian (Aug 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968478):
hmm, is it possible to do it without explicitly refering to the def of `not`?

#### [Simon Hudon (Aug 11 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968606):
I'm not following you. My `simp` expression only lists lemmas to use with your reduction.

#### [Zesen Qian (Aug 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/131968653):
I see what you are saying, thank you.

#### [Zesen Qian (Aug 17 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[meta] reduce an expr/near/132324576):
(deleted)

