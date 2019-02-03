---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37173newbehaviourofext.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [new behaviour of ext?](https://leanprover-community.github.io/archive/113488general/37173newbehaviourofext.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 12 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133776231):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, did the behaviour of ext just change? I'm finding the hypotheses of my ext lemmas being added as goals in a different order than previously.</p>

#### [ Mario Carneiro (Sep 12 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133776645):
<p><code>ext</code> did change. could you be more specific about the difference?</p>

#### [ Scott Morrison (Sep 12 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133794672):
<p>Sorry, I think actually nothing changed, but I would like to propose a change!</p>

#### [ Scott Morrison (Sep 12 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133794678):
<p>When you <code>apply</code>, there is an option to control the order of the introduced goals.</p>

#### [ Scott Morrison (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133794729):
<p>The default is "dependent first", with the idea that fulfilling these may magically clear the later ones.</p>

#### [ Scott Morrison (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133794757):
<p>I find that instead it's more likely to give me confusing goals with metavariables, and I would prefer to explain the non-dependent goals first!</p>

#### [ Simon Hudon (Sep 12 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20behaviour%20of%20ext%3F/near/133801826):
<p>The order of assumptions should not have changed. What might have changed is the exact extensionality rule that gets applied. For instance, we're trying to avoid funext if set.ext is more relevent. I'm hoping this should make your proofs more stable even as the set of extensionality lemmas changes with time.</p>


{% endraw %}
