---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08479maxofsubsequence.html
---

## Stream: [general](index.html)
### Topic: [max of subsequence](08479maxofsubsequence.html)

---


{% raw %}
#### [ Andrew Ashworth (Feb 27 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019419):
<p>is there a concise way, if I have <code>f : nat -&gt; rat</code>, to obtain the maximum of the sequence as it ranges from 0..N?</p>

#### [ Andrew Ashworth (Feb 27 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019496):
<p>i mean, i can definitely apply max recursively N times starting from 0, but then I have to prove a bunch of theorems about the definition</p>

#### [ Mario Carneiro (Feb 27 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019656):
<p>Not really. There should be a <code>list.max</code> for this, it seems to come up often. You can at least <code>list.foldl max 0</code> applied to the list <code>map f (range n)</code></p>

#### [ Andrew Ashworth (Feb 27 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019667):
<p>i will investigate this, thanks</p>

#### [ Mario Carneiro (Feb 27 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019673):
<p>I'm not sure that's actually better than just the recursive definition though</p>


{% endraw %}
