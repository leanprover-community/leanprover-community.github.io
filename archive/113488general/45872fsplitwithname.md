---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45872fsplitwithname.html
---

## Stream: [general](index.html)
### Topic: [fsplit with name](45872fsplitwithname.html)

---


{% raw %}
#### [ Reid Barton (Nov 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fsplit%20with%20name/near/148645058):
<p>I want to construct an <code>Exists</code> value where both parts are Props in tactic mode. Is there a convenient way to use something like <code>fsplit</code> to produce two subgoals but also to have the result of the first subgoal available as a hypothesis in the second subgoal?</p>

#### [ Reid Barton (Nov 27 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fsplit%20with%20name/near/148645203):
<p>Currently I have <code>have : P, { ... }, refine &lt;this, _&gt;, ...</code> but it's a little clunky and it means I have to write out <code>P</code></p>

#### [ Reid Barton (Nov 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fsplit%20with%20name/near/148646115):
<p>actually I turned out not to need <code>this</code>, but I'm still curious</p>


{% endraw %}
