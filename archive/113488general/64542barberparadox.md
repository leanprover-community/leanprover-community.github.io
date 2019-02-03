---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64542barberparadox.html
---

## Stream: [general](index.html)
### Topic: [barber paradox](64542barberparadox.html)

---


{% raw %}
#### [ Cameron Crossman (Dec 11 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151478623):
<p>Can someone please help me with the barber paradox proof in lean?</p>

#### [ Cameron Crossman (Dec 11 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151478627):
<p>theorem barber_paradox : ¬ (∀ x : men, shaves barber x ↔ ¬ shaves x x)</p>

#### [ Andrew Ashworth (Dec 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151478769):
<p>Do you have a specific question?</p>

#### [ Chris Hughes (Dec 11 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151479142):
<p><a href="#narrow/stream/113488-general/topic/Logic.20.26.20Proof" title="#narrow/stream/113488-general/topic/Logic.20.26.20Proof">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic.20.26.20Proof</a></p>

#### [ Abhimanyu Pallavi Sudhir (Dec 16 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151882895):
<blockquote>
<p>theorem barber_paradox : ¬ (∀ x : men, shaves barber x ↔ ¬ shaves x x)</p>
</blockquote>
<p>See <code>barber_is_dead</code> (and a tactic mode proof above it) here: <a href="https://github.com/abhimanyupallavisudhir/lean/blob/master/logic_theorems.lean" target="_blank" title="https://github.com/abhimanyupallavisudhir/lean/blob/master/logic_theorems.lean">https://github.com/abhimanyupallavisudhir/lean/blob/master/logic_theorems.lean</a></p>

#### [ Kevin Buzzard (Dec 16 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151883459):
<p>Ha ha are you revising Cantor's theorem :-)</p>

#### [ Kevin Buzzard (Dec 16 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151883587):
<p>I don't think you need to be classical for pants on fire. I had to prove this in cantor at the end</p>

#### [ Kevin Buzzard (Dec 16 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/barber%20paradox/near/151887219):
<p><code>example (P : Prop) (Q : Prop) : ¬ P → (P → Q) := by intros;contradiction</code> etc. Your instinct as a mathematician is to case split, but it's often not necessary. Not that this matters (at least not that it matters to us mathematicians...)</p>


{% endraw %}
