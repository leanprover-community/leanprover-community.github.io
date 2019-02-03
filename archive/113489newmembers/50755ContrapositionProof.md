---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50755ContrapositionProof.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Contraposition Proof](https://leanprover-community.github.io/archive/113489newmembers/50755ContrapositionProof.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Cameron Crossman (Dec 04 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150809932):
<p>I am a new user and I am just getting my bearings with the platform.  Would someone be able to walk me through a proof of Contraposition written in Lean? (p → q) → (¬q → ¬p). Much appreciated!  I know the general steps but am getting confused about how to translate that into Lean.<br>
(p → q)<br>
¬(p ^ ¬q)<br>
¬( ¬q ^ p)<br>
r = ¬q, s = ¬p substitution<br>
¬(r ^ ¬s )<br>
(r → s)<br>
substitute back in<br>
¬q → ¬p</p>

#### [ Kevin Buzzard (Dec 04 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150810178):
<p>In tactic mode? If you keep using the <code>intro</code> tactic you will find yourself with hypotheses <code>p-&gt;q</code>, <code>not q</code> and <code>p</code> and with a goal of <code>false</code>. Now apply your hypotheses until you're done. Sorry, on phone and just off to bed, hope this helps</p>

#### [ Mario Carneiro (Dec 04 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150813490):
<p>Lean's logic is similar to natural deduction, where <code>¬p</code> means <code>p -&gt; false</code> so the proof is actually a lot easier than the one you sketched</p>

#### [ Bryan Gin-ge Chen (Dec 04 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150816360):
<p><a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/logic.lean#L34" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/logic.lean#L34">Here's the proof in lean core</a>, called "mt" for "modus tollens".</p>

#### [ Cameron Crossman (Dec 04 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150816560):
<p>Thank you!</p>


{% endraw %}
