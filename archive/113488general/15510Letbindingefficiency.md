---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15510Letbindingefficiency.html
---

## [general](index.html)
### [Let binding efficiency](15510Letbindingefficiency.html)

#### [Seul Baek (Dec 24 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446520):
If a term `foo` appears multiple times in a definition in such a way that each occurrence of it will have to be normalized,  does the definition become more efficiently computable by using `let x := foo in` in the beginning? The assumption is that `x` will be structured in a way that forces (some) normalization with the let binding (e.g., if `foo : A × B`, then `let (a,b) := foo`).

#### [Mario Carneiro (Dec 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446627):
yes, although lean does that sometimes on its own, during the common subexpression elimination pass

#### [Mario Carneiro (Dec 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446628):
do you mean in the VM or the kernel?

#### [Mario Carneiro (Dec 24 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446634):
Note that `let (a,b) := foo` is not a let binding at all, it is just notation for a recursor

#### [Seul Baek (Dec 24 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446693):
I meant the kernel, although I'd be curious about the VM as well.

#### [Mario Carneiro (Dec 24 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446698):
In the kernel, I am not positive but I would guess that it depends on how shared the expression object is in memory

#### [Mario Carneiro (Dec 24 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446700):
using a let binding like that is a good way to make sure that the same expression object is used in each place

#### [Mario Carneiro (Dec 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446702):
but there will be some overhead with unfolding it

#### [Mario Carneiro (Dec 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446745):
The kernel caches the whnf operation, so it won't need to calculate it many times if it is asked for multiple times

#### [Mario Carneiro (Dec 24 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446751):
but I'm not sure whether the same expression in different contexts can cause a problem (since this might mean renaming vars and unsharing)

#### [Seul Baek (Dec 24 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446851):
The main downside I'm experiencing with `let` is that it doesn't play nice with the simplifier when I have to prove properties about definitions which include it (`_match_1` all over the place) and requires extra definitional lemmas for unfolding. So I was wondering if there are reasons to use it other than its concision.

#### [Seul Baek (Dec 24 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446991):
If `let (a,b) := foo` is not a let binding, is there something else I can do to normalize `foo` and bind it to fresh term(s)?

#### [Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447329):
like I said, it's just a recursor. If you don't like the `_match_1` stuff, you can use tactics instead to construct the term, which don't leave this junk in the term

#### [Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447337):
i.e. `by cases foo with a b; exact`

#### [Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447343):
it's equivalent to writing `prod.rec` explicitly in the term

#### [Seul Baek (Dec 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447817):
I see. Thanks!

