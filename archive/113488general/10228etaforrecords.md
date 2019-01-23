---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10228etaforrecords.html
---

## Stream: [general](index.html)
### Topic: [eta for records](10228etaforrecords.html)

---


{% raw %}
#### [ Johan Commelin (Jan 09 2019 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154705125):
(:warning: I'm a mathematician who is about to use some terminology he doesn't understand.)
What are the pros and cons of eta for records? Why does Lean not have eta for records?

#### [ Gabriel Ebner (Jan 09 2019 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707201):
> Why does Lean not have eta for records?

Because records (`structure`) in Lean are just inductives with a single (non-recursive) constructor.  And we don't have η for inductives either (I'm pretty sure that causes type-checking to be undecidable).

#### [ Gabriel Ebner (Jan 09 2019 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707304):
Pros:
```lean
example (p : ℕ × ℕ) : p = (p.1, p.2) := rfl
example (C) [𝓒 : category C] := opposite (opposite 𝓒) = 𝓒 := rfl
```

#### [ Sebastian Ullrich (Jan 09 2019 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707306):
Agda has (opt-out) eta for inductive, non-recursive records. Which at least terminates, but may still slow down unification.


{% endraw %}
