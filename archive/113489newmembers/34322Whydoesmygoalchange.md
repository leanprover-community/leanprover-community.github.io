---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/34322Whydoesmygoalchange.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Why does my goal change?](https://leanprover-community.github.io/archive/113489newmembers/34322Whydoesmygoalchange.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ali Sever (Aug 04 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130885232):
<p>After using <code>constructor</code> my goal was <code>?m_1 ∉ A</code>. Then I used <code>cases h with p hp</code>, and my goal became <code>?m_1[_] ∉ A</code>. What does that mean, and why does it even happen?</p>

#### [ Kenny Lau (Aug 04 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130885281):
<p>MWE</p>

#### [ Mario Carneiro (Aug 04 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130886032):
<p>That is a representation of a delayed abstraction. It means that the metavariable <code>?m_1</code> has been partially instantiated, although it still hasn't figured out what it should be yet</p>

#### [ Kevin Buzzard (Aug 04 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130888106):
<p>Ali I think it's an unwise idea in general to have metavariables in your goals. Presumably you have more than one goal at this point, and another goal is probably asking you what the metavariable is. You might want to fill in some earlier hole.</p>


{% endraw %}
