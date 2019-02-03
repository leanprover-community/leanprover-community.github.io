---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58233Shouldmeasurablespacebeaclass.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Should measurable_space be a class?](https://leanprover-community.github.io/archive/113488general/58233Shouldmeasurablespacebeaclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 29 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Should%20measurable_space%20be%20a%20class%3F/near/148754678):
<p>I believe there are often situations where you have two measures on the same set, and two measurable spaces. An example would be Borel-measurable vs Lebesgue-measurable.</p>

#### [ Johannes Hölzl (Nov 29 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Should%20measurable_space%20be%20a%20class%3F/near/148772400):
<p>There are always cases where one measurable space is not fitting. Especially when we talk about filtrations in probability theory.  But in most applications in measure theory there is only one measurable space per type. Borel- vs. Lebesgue-measurable is a special case, and I think the best way to handle it is a special way to talk about completions.</p>
<p>In Isabelle I developed measure theory without using the type class mechanism. And it is very annoying. In 90% of all cases you only have one measurable space. But in Isabelle it was not possible to use a theorem which uses a type class instance to instantiate with something different (this is now possible, but very ugly). In Lean we can use different measurable spaces, even when it is a little bit of a hassle to use the <code>@</code>-syntax and hope that the simplifier accepts our instances.</p>


{% endraw %}
