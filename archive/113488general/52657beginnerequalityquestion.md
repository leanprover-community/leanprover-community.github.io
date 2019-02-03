---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52657beginnerequalityquestion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [beginner equality question](https://leanprover-community.github.io/archive/113488general/52657beginnerequalityquestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ dan pittman (Jun 26 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128673907):
<p>I'm attempting to assert whether two elements of a list are equal, and then act on that assertion in an <code>if-then-else</code> manner, but for my <code>x = y</code> assertion, there is no <code>decidable</code> instance. Perhaps there's a different approach I ought to be taking?</p>

#### [ Chris Hughes (Jun 26 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128674057):
<p>Using the line <code>local attribute [instance] classical.prop_decidable</code> should help, but it will stop your functions being computable. What type do <code>x</code> and <code>y</code> have? You could also make <code>[decidable_eq α]</code> an argument to your function, if it's defined on an arbitrary type.</p>

#### [ dan pittman (Jun 26 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/beginner%20equality%20question/near/128676882):
<p>Thanks! <code>decidable_eq</code> is what I was looking for! I'd written this in Haskell first, and was of course using <code>Eq a =&gt; ...</code>.</p>


{% endraw %}
