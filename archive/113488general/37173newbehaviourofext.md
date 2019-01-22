---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37173newbehaviourofext.html
---

## [general](index.html)
### [new behaviour of ext?](37173newbehaviourofext.html)

#### [Scott Morrison (Sep 12 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133776231):
Hi @**Simon Hudon**, did the behaviour of ext just change? I'm finding the hypotheses of my ext lemmas being added as goals in a different order than previously.

#### [Mario Carneiro (Sep 12 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133776645):
`ext` did change. could you be more specific about the difference?

#### [Scott Morrison (Sep 12 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133794672):
Sorry, I think actually nothing changed, but I would like to propose a change!

#### [Scott Morrison (Sep 12 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133794678):
When you `apply`, there is an option to control the order of the introduced goals.

#### [Scott Morrison (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133794729):
The default is "dependent first", with the idea that fulfilling these may magically clear the later ones.

#### [Scott Morrison (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133794757):
I find that instead it's more likely to give me confusing goals with metavariables, and I would prefer to explain the non-dependent goals first!

#### [Simon Hudon (Sep 12 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new behaviour of ext?/near/133801826):
The order of assumptions should not have changed. What might have changed is the exact extensionality rule that gets applied. For instance, we're trying to avoid funext if set.ext is more relevent. I'm hoping this should make your proofs more stable even as the set of extensionality lemmas changes with time.

