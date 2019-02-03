---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87229unoption.html
---

## Stream: [general](index.html)
### Topic: [unoption](87229unoption.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948591):
<p>What is the function which takes <code>a : option X</code> and a proof that <code>a</code> isn't <code>none</code> and returns the x such that <code>a = some x</code> called? I can write it -- but I suspect someone else already thought of it...</p>

#### [ Kevin Buzzard (Jul 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948631):
<p>I found <code>get</code> but that seems to involve bools...</p>

#### [ Mario Carneiro (Jul 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948720):
<p>it is <code>option.get</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948739):
<p>you can use a bool as a Prop fyi...</p>

#### [ Kevin Buzzard (Jul 19 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129952337):
<p>OK thanks!</p>


{% endraw %}
