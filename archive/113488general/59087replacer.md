---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59087replacer.html
---

## [general](index.html)
### [replacer](59087replacer.html)

#### [Mario Carneiro (Sep 11 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700764):
By the suggestion of Simon, I've extended `replacer` to support parameters in its type. That is, you can define a replaceable definition `foo : A -> tactic B` where you have arbitrary input and output, rather than just `tactic unit`. Incidentally, implementing this required my first attempt at meta-metaprogramming, since the defined tactics are written programmatically.

#### [Simon Hudon (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700886):
Does it accept any number of parameters?

#### [Mario Carneiro (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700888):
yes

#### [Mario Carneiro (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700895):
just one output, but we always bundle that anyway

#### [Mario Carneiro (Sep 11 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700963):
It doesn't support monads other than `tactic`, and the prev tactic access does not allow changing parameters

#### [Simon Hudon (Sep 11 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701331):
This supercalifragilisticexpialidocious!

#### [Simon Hudon (Sep 11 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701427):
To let other people in on the idea, I wanted this so that we can write a tactic at the same as we write a proof, even if the tactic is a core tactic, we can put them in the same file and stop recompiling everything every time we change the tactic

#### [Simon Hudon (Sep 11 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701435):
This is a bit similar to hot code loading

#### [Mario Carneiro (Sep 11 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701521):
you don't mean "core" as in "core lean" though. Like time travel, you can't go back before the time machine was invented

#### [Simon Hudon (Sep 11 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701529):
That is correct :)

#### [Simon Hudon (Sep 11 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701549):
You can only replace definitions in files where you can import this replacer tactic.

#### [Simon Hudon (Sep 11 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701974):
What do you use from `tactic.basic`?

#### [Mario Carneiro (Sep 11 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702266):
just the `has_reflect` instance for binder_info

#### [Simon Hudon (Sep 11 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702353):
Cool, I left you a comment on the commit. I think it should be moved to `tactic.replacer` so that `tactic.basic` can import `tactic.replacer` (since it's a tool for writing tactics)

#### [Mario Carneiro (Sep 11 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702529):
I don't think anything in mathlib uses it though

#### [Simon Hudon (Sep 11 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702652):
That's ok. What i intend to do with it when I write tactics for mathlib is to temporarily have `tactic.basic` import `tactic.replacer`, make all the routines I use replaceable, go write an example and, next to it, keep a version of the functions and tactics that I modify. When I'm done, I remove the `def_replacers` and the `import tactic.basic` statement.

#### [Simon Hudon (Sep 11 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703035):
Btw, there is a way we could go back in time passed the creation of our machine: using meta programming, we create a `dynamic` namespace in which we copy all the visible declarations that depend on what we want to replace and and we rewrite their definitions to insert the replacer instead of the original definition.

#### [Mario Carneiro (Sep 11 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703136):
that's more like alternate universe time travel

#### [Simon Hudon (Sep 11 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703163):
I'm happy with multi-universe interpretations

