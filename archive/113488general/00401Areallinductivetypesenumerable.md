---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00401Areallinductivetypesenumerable.html
---

## Stream: [general](index.html)
### Topic: [Are all inductive types enumerable?](00401Areallinductivetypesenumerable.html)

---


{% raw %}
#### [ Kenny Lau (Aug 01 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696713):
<p>Are all inductive types enumerable?</p>

#### [ Mario Carneiro (Aug 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696827):
<p>inductive types whose parts are enumerable are enumerable</p>

#### [ Mario Carneiro (Aug 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696857):
<p>indeed it's not unreasonable to have a <code>derive_handler</code> for that</p>

#### [ Kenny Lau (Aug 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696864):
<p>it would solve Q4 of my questions lol</p>

#### [ Kenny Lau (Aug 01 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696907):
<p><a href="#narrow/stream/113488-general/subject/Lean.20assignment.20from.20Kenny/near/130567187" title="#narrow/stream/113488-general/subject/Lean.20assignment.20from.20Kenny/near/130567187">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Lean.20assignment.20from.20Kenny/near/130567187</a></p>

#### [ Mario Carneiro (Aug 01 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20all%20inductive%20types%20enumerable%3F/near/130696921):
<p>You can prove finite trees are enumerable by using <code>denumerable (list A)</code> recursively</p>


{% endraw %}
