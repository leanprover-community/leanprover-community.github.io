---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68209customrecursor.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [custom recursor](https://leanprover-community.github.io/archive/113488general/68209customrecursor.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Mar 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198503):
<p>I'm creating a recursor for a type that I defined and I'd like <code>match</code> and <code>cases</code> to pick it instead of what Lean generated. Is there a way to do that?</p>

#### [ Andrew Ashworth (Mar 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198843):
<p>instead of cases, why not use <code>induction</code>where you can specify the recursor?</p>

#### [ Mario Carneiro (Mar 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198918):
<p>No, that's not really possible. You can use the <code>using</code>clause of <code>induction</code>, but it's not particularly reliable in my experience. I don't really consider it supported</p>

#### [ Simon Hudon (Mar 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123199074):
<p>For <code>cases</code> on coinductive types, I can make my own tactics but it would be great if the same tactic could cover both inductive and coinductive types</p>

#### [ Simon Hudon (Mar 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123199079):
<p>Maybe I should just add that to my wish list</p>


{% endraw %}
