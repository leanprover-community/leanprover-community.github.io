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
<p>I'm tempted to define <code>lt</code> explicitly in <code>preorder.lift</code> as <code>\lam x y, f x &lt; f y</code>. Does this seem like a terrible idea for any obvious reason?</p>

#### [ Reid Barton (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148741959):
<p>The current definition does not play well with restricting a well ordering to a subtype</p>

#### [ Mario Carneiro (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148741984):
<p>that should be fine</p>

#### [ Kenny Lau (Nov 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148742061):
<p>more things to add to the PR limbo! :P</p>

#### [ Reid Barton (Nov 28 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148742125):
<p><span class="emoji emoji-1f93a" title="fencing">:fencing:</span></p>

#### [ Reid Barton (Nov 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder.lift/near/148743570):
<p>Nice, it didn't break anything, and solved my issue.</p>


{% endraw %}
