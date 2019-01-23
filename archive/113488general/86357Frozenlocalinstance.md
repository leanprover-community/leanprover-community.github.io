---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86357Frozenlocalinstance.html
---

## Stream: [general](index.html)
### Topic: [Frozen local instance](86357Frozenlocalinstance.html)

---


{% raw %}
#### [ Moses Schönfinkel (Mar 12 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599507):
What is going on in scenarios where Lean tells me `failed to revert 'c', it is a frozen local instance` and then I magically fix everything by calling `tactic.unfreeze_local_instances`?

#### [ Simon Hudon (Mar 12 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599520):
There was recently a change in Lean where Lean is getting more rigid with its instance cache

#### [ Mario Carneiro (Mar 12 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599522):
Since #1920 and the surrounding commits, lean no longer lets you mess with instances in the context that are "frozen", i.e. left of the colon. These are also the only instances which are used in typeclass inference

#### [ Moses Schönfinkel (Mar 12 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599566):
Oh, so "frozen" just means left of the colon. Alrighty, thanks.

#### [ Mario Carneiro (Mar 12 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599568):
By the way in mathlib, there is a name for this tactic: `resetI`. It also is bundled together with several other tactics like `haveI` and `exactI`

#### [ Moses Schönfinkel (Mar 12 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123599712):
`resetI` works like a charm and saves one control space, one down arrow and one enter; win-win

#### [ Moses Schönfinkel (Mar 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908258):
What is the right way to avoid having to `resetI` in a scenario where I have `lemma f {A : Type*} [X : something A]` and I want to do `cases X`? Is doing this actively discouraged for some reason? Or am I misunderstanding the cause of getting the `frozen local instance` error?

#### [ Mario Carneiro (Mar 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908269):
You could put `X` right of the colon

#### [ Moses Schönfinkel (Mar 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908362):
Right, so that's it, thanks.

#### [ Mario Carneiro (Mar 19 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908372):
Also, `resetI` is not a "code smell" or other poor practice you are making it out to be. Lean is doing an optimization that works in most cases, and to make it easy for tactic scripting it is assumed that you usually don't want to be resetting instances ('usually' meaning not after every tactic), but this requires the user to explicitly mark that they are doing this, which is a bit unpleasant to see and explain but would have otherwise been done automatically anyway.

#### [ Moses Schönfinkel (Mar 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908462):
Good enough for me, I'll keep on `resetI`ng relentlessly then.

#### [ Moses Schönfinkel (Mar 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123908463):
Thanks again :).

#### [ Sebastian Ullrich (Mar 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123909880):
@**Moses Schönfinkel**
> Is doing this actively discouraged for some reason?

It actually is, see the issues discussed at https://github.com/leanprover/lean/commit/16f28315eeddf996f85bff96954cd31a94aa4562#diff-b9da5b9cf1417a3f4da2b3adda3eea2fR96

#### [ Mario Carneiro (Mar 19 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123910208):
Ah, that's true. This only is a problem if your typeclass instance is inferred in some function in your goal (in the `decidable` case this is like when you have an `if` in your goal and you try to clean it up by case on the decidable parameter). It falls under the more general heading "don't have non-canonical typeclass proofs in your functions, it's confusing"

#### [ Mario Carneiro (Mar 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Frozen%20local%20instance/near/123910282):
But that's not to say that it is disallowed, because sometimes you just have to do it, if your typeclass is some complicated inductive thing this may be the only option. But try to get rid of those functions as soon as possible after the cases


{% endraw %}
