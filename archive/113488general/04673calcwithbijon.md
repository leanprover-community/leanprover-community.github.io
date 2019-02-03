---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04673calcwithbijon.html
---

## Stream: [general](index.html)
### Topic: [calc with bij_on](04673calcwithbijon.html)

---


{% raw %}
#### [ Reid Barton (Jun 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127674091):
<p>Is there a way I could use <code>calc</code> to chain together <code>bij_on_comp</code>?<br>
<code>bij_on_comp : bij_on g b c → bij_on f a b → bij_on (g ∘ f) a c</code></p>

#### [ Reid Barton (Jun 06 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127674456):
<p>wow, it actually works! <code>local notation a ` ~~ ` b := bij_on _ a b</code>, and define a <code>@[trans]</code> version of <code>bij_on_comp</code> with arguments in the right order</p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676519):
<p>Yeah we took apart calc recently and found out that it was just reading from left to right and attempting to prove a R b S c -&gt; a T c by using results tagged with @trans</p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676710):
<p><a href="https://github.com/kbuzzard/mathlib/blob/master/docs/extras/calc.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/extras/calc.md">https://github.com/kbuzzard/mathlib/blob/master/docs/extras/calc.md</a></p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676713):
<p>Calc is great.</p>

#### [ Reid Barton (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676725):
<p>I wasn't sure whether it would also be able to handle the accumulation going on in the first parameter of <code>bij_on</code></p>

#### [ Reid Barton (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676729):
<p>but apparently it doesn't care</p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676731):
<p>Oh I see</p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676784):
<p>You should add a comment to the docs :-)</p>

#### [ Kevin Buzzard (Jun 06 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676823):
<p>I guess the elaborator just does its best. This software is so cool</p>


{% endraw %}
