---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62254atactictoforgetthedefinition.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [a tactic to forget the definition](https://leanprover-community.github.io/archive/113488general/62254atactictoforgetthedefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 07 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147254137):
<p>Can we make a tactic to forget the definition of something in the local context while keeping everything else unchanged?</p>

#### [ Kenny Lau (Nov 07 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147254192):
<p>so it would make <code>h : R := 1+1</code> into <code>h : R</code></p>

#### [ Chris Hughes (Nov 07 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147259811):
<p>Use <code>generalize</code> instead of let to define h in the first place. Is this something to do with trying to get <code>subst </code> to work?</p>

#### [ Kenny Lau (Nov 07 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147260386):
<p>it isn't</p>

#### [ Mario Carneiro (Nov 08 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147266720):
<p>you could <code>replace h := h</code> I think</p>


{% endraw %}
