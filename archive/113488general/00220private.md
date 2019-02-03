---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00220private.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [private](https://leanprover-community.github.io/archive/113488general/00220private.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Dec 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150684856):
<p>What's the scope of something defined as <code>private</code>? It seems to be larger than just the surrounding section</p>

#### [ Reid Barton (Dec 01 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150685049):
<p>And in particular is there any way for a <code>parameter</code> to "outlive" a <code>private</code> definition which uses it?</p>

#### [ Reid Barton (Dec 01 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/private/near/150685100):
<p>It seems that the answer is no, because</p>
<ul>
<li>(apparently?) a <code>private</code> definition is in scope in the entire surrounding <code>namespace</code> block,</li>
<li>a <code>parameter</code> must be defined inside a <code>section</code>,</li>
<li>a <code>namespace</code> cannot go inside a <code>section</code></li>
</ul>


{% endraw %}
