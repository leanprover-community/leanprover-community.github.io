---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00220private.html
---

## [general](index.html)
### [private](00220private.html)

#### [Reid Barton (Dec 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150684856):
What's the scope of something defined as `private`? It seems to be larger than just the surrounding section

#### [Reid Barton (Dec 01 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150685049):
And in particular is there any way for a `parameter` to "outlive" a `private` definition which uses it?

#### [Reid Barton (Dec 01 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150685100):
It seems that the answer is no, because
* (apparently?) a `private` definition is in scope in the entire surrounding `namespace` block,
* a `parameter` must be defined inside a `section`,
* a `namespace` cannot go inside a `section`

