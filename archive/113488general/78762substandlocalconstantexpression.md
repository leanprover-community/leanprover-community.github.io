---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78762substandlocalconstantexpression.html
---

## [general](index.html)
### [subst and local constant expression](78762substandlocalconstantexpression.html)

#### [Sean Leather (Feb 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034490):
Why does `subst` need its expression argument to be a local constant? I would like to be able to do something like `subst <expr>` with an arbitrary `<expr>`, but this results in:
```
error: subst tactic failed, given expression is not a local constant
```
Instead, I have to do:
```lean
have : a = b := <expr>, subst this
```
Is it because `subst` always `clear`s the argument? Should there be a version of `subst` that doesn't `clear`?

#### [Mario Carneiro (Feb 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034493):
yeah I petitioned for this but leo said no

#### [Mario Carneiro (Feb 27 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034533):
it's an expr so you can use the french quotes to select a variable from the context by type

#### [Mario Carneiro (Feb 27 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034544):
You can do mostly the same thing with `cases e` where `e : a = b`

#### [Simon Hudon (Feb 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034636):
Otherwise, you may need to do `generalize` first and then `subst`.

