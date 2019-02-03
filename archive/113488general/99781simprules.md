---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99781simprules.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp rules](https://leanprover-community.github.io/archive/113488general/99781simprules.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Dec 04 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877417):
<p>I see there are many things that I would like to add as simp rules. For instance <code>le_refl</code>. And all de Morgan's rules that take a <code>not</code> and push it inside logical connectives, to get to some kind of a normal form, like <code>theorem not_or_distrib : ¬ (a ∨ b) ↔ ¬ a ∧ ¬ b</code>. Are there good reasons not to do it?</p>

#### [ Mario Carneiro (Dec 04 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877616):
<p>I think a normal form for propositions is not a good idea unless it is a component in a full proof a la <code>tauto</code></p>

#### [ Mario Carneiro (Dec 04 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877625):
<p>most of the time this just mucks things up for manual proof</p>

#### [ Mario Carneiro (Dec 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877720):
<p>I don't see a problem with <code>le_refl</code> as a simp rule; what other things are in scope here?</p>

#### [ Sebastien Gouezel (Dec 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877737):
<p>What do you mean?</p>

#### [ Scott Morrison (Dec 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877881):
<p>I definitely wouldn't want <code>not_or_distrib</code> as a simp lemma. The right hand side is only obviously simpler after you've made a particular choice about what your normal form is.</p>

#### [ Sebastien Gouezel (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877902):
<p>My question about normal forms is because I ended up in a proof with several expressions of the form <code>¬(¬ a ∨ b)</code>, or things like that. I can definitely add the right rule to expand stuff, but I am under the impression that most of the time it is the right thing to do.</p>

#### [ Scott Morrison (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877933):
<p>simp lemmas should have right hand sides that are "unambiguously" simpler.</p>

#### [ Mario Carneiro (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877935):
<p>if I'm trying to prove <code>A -&gt; B</code> and <code>simp</code> decides to "helpfully" replace it with <code>not A or B</code> I will be annoyed</p>

#### [ Scott Morrison (Dec 04 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877979):
<p>If a normal form exists for some class of objects, we want a tactic that rewrites into that normal form, but if not everyone wants to use that normal form all the time, that tactic shouldn't be <code>simp</code>.</p>

#### [ Sebastien Gouezel (Dec 04 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878008):
<p>Of course, <code>A -&gt; B</code> should not be simplified like you say. I only want to add in the ones that push <code>¬</code> as far inside as possible, which looks simpler to me as <code>¬</code> is more basic than and or or. But if you all agree that it is a bad idea, let's forget about it.</p>

#### [ Mario Carneiro (Dec 04 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878142):
<p>I think that propositional structure in lean quite often reflects a certain structure of proof, according to its intuitionistic reading</p>

#### [ Mario Carneiro (Dec 04 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878221):
<p>even if we are being classical, lean is still easier to use when you "go with the flow" of the logic, and other stuff requires applying theorems explicitly</p>


{% endraw %}
