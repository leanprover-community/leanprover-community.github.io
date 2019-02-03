---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44791Definitionsforbindernotations.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Definitions for binder notations](https://leanprover-community.github.io/archive/113488general/44791Definitionsforbindernotations.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148275473):
<p>If I am a learner and I see <code>X ≃ Y</code> and I want to know what it means, I can type <code>#print notation ≃</code>. If I am a learner and I see <code>{x : ℝ | x &gt; 0}</code> and I type <code>#print {</code> I just get a confusing answer. I guess this also happens for <code>(</code> and <code>[</code>. Of course { and [ are defined in Lean somewhere -- but a beginner is unlikely to be able to find them. Finally, if I try and figure out what <code>Π</code> or <code>λ</code> mean, which to a beginner look as much like notation as <code>≃</code>, <code>#print notation</code> just tells me that actually these aren't notation at all. I was going to write some brief docs about this. What other symbols need to be covered? Oh -- <code>∃!</code> and <code>∃</code>. Hmm -- <code>∀</code> has no notation again, I'm surprised it's not defined to be Pi via a standard notation definition.</p>
<p>I guess a trick which works well with { and [ is to simply switch notation off in your Lean file. But this has an irritating consequence of switching _all_ your notation off, rather than just that for the brackets.</p>

#### [ Reid Barton (Nov 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148278241):
<p><code>[</code> (assuming you're referring to the notation for lists) and the existential quantifiers are defined as notation, the other things you mention are not. I assume they must be built in to the Lean parser.</p>

#### [ Reid Barton (Nov 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148278294):
<p>You can also use jump-to-definition to find out the meaning of notation, sort of. It takes you to the definition of the thing that the notation represents (e.g., the definition of <code>list</code> itself), but often the <code>notation</code> declaration is nearby.</p>


{% endraw %}
