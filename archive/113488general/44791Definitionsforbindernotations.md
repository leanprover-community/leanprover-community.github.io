---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44791Definitionsforbindernotations.html
---

## Stream: [general](index.html)
### Topic: [Definitions for binder notations](44791Definitionsforbindernotations.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148275473):
If I am a learner and I see `X ≃ Y` and I want to know what it means, I can type `#print notation ≃`. If I am a learner and I see `{x : ℝ | x > 0}` and I type `#print {` I just get a confusing answer. I guess this also happens for `(` and `[`. Of course { and [ are defined in Lean somewhere -- but a beginner is unlikely to be able to find them. Finally, if I try and figure out what `Π` or `λ` mean, which to a beginner look as much like notation as `≃`, `#print notation` just tells me that actually these aren't notation at all. I was going to write some brief docs about this. What other symbols need to be covered? Oh -- `∃!` and `∃`. Hmm -- `∀` has no notation again, I'm surprised it's not defined to be Pi via a standard notation definition.

I guess a trick which works well with { and [ is to simply switch notation off in your Lean file. But this has an irritating consequence of switching _all_ your notation off, rather than just that for the brackets.

#### [ Reid Barton (Nov 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148278241):
`[` (assuming you're referring to the notation for lists) and the existential quantifiers are defined as notation, the other things you mention are not. I assume they must be built in to the Lean parser.

#### [ Reid Barton (Nov 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitions%20for%20binder%20notations/near/148278294):
You can also use jump-to-definition to find out the meaning of notation, sort of. It takes you to the definition of the thing that the notation represents (e.g., the definition of `list` itself), but often the `notation` declaration is nearby.


{% endraw %}
