---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11937preorderlift.html
---

## Stream: [general](index.html)
### Topic: [preorder.lift](11937preorderlift.html)

---


{% raw %}
#### [ Reid Barton (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148741950):
I'm tempted to define `lt` explicitly in `preorder.lift` as `\lam x y, f x < f y`. Does this seem like a terrible idea for any obvious reason?

#### [ Reid Barton (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148741959):
The current definition does not play well with restricting a well ordering to a subtype

#### [ Mario Carneiro (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148741984):
that should be fine

#### [ Kenny Lau (Nov 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148742061):
more things to add to the PR limbo! :P

#### [ Reid Barton (Nov 28 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148742125):
:fencing:

#### [ Reid Barton (Nov 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148743570):
Nice, it didn't break anything, and solved my issue.


{% endraw %}
