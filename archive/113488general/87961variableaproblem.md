---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87961variableaproblem.html
---

## Stream: [general](index.html)
### Topic: [variable a problem](87961variableaproblem.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 08 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463049):
<p>This is presumably well-known but it has just bitten one of my undergraduates. They wrote <code>have Ht2 : (a &lt; nat.succ t) → (nat.succ t &lt; c) → (a &lt; c),</code> in the middle of a tactic proof, with a,t,c nats, and get a type mismatch error: <code>term a has type  nat.succ t &lt; c : Prop</code>. Chris tells me that this is because you can't use <code>have</code> in a tactic proof with an implies sign and a variable <code>a</code>. That sounds like a bug to me. Is it officially not a bug though?</p>

#### [ Sebastian Ullrich (Mar 08 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463243):
<p>Oh, it is <a href="https://github.com/leanprover/lean/issues/1822" target="_blank" title="https://github.com/leanprover/lean/issues/1822">https://github.com/leanprover/lean/issues/1822</a></p>

#### [ Kevin Buzzard (Mar 08 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463326):
<p>So we have to wait for the parser refactoring?</p>

#### [ Sebastian Ullrich (Mar 08 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463636):
<p>Yes</p>


{% endraw %}
