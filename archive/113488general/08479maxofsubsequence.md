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
is there a concise way, if I have `f : nat -> rat`, to obtain the maximum of the sequence as it ranges from 0..N?

#### [ Andrew Ashworth (Feb 27 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019496):
i mean, i can definitely apply max recursively N times starting from 0, but then I have to prove a bunch of theorems about the definition

#### [ Mario Carneiro (Feb 27 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019656):
Not really. There should be a `list.max` for this, it seems to come up often. You can at least `list.foldl max 0` applied to the list `map f (range n)`

#### [ Andrew Ashworth (Feb 27 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019667):
i will investigate this, thanks

#### [ Mario Carneiro (Feb 27 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max%20of%20subsequence/near/123019673):
I'm not sure that's actually better than just the recursive definition though


{% endraw %}
