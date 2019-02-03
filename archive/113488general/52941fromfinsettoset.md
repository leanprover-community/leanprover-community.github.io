---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52941fromfinsettoset.html
---

## Stream: [general](index.html)
### Topic: [from finset to set](52941fromfinsettoset.html)

---


{% raw %}
#### [ Johan Commelin (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256617):
<p>I can't find a way to go from <code>finset</code> to <code>set</code> in the <code>finset.lean</code> file. How do I do this?</p>

#### [ Kenny Lau (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256619):
<p><code>{x | x \in s}</code></p>

#### [ Johan Commelin (May 08 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256622):
<p>Ok... there is no <code>lift_to_set S</code> thing or such?</p>

#### [ Kenny Lau (May 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256662):
<p>not that I am aware of</p>

#### [ Johan Commelin (May 08 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126256812):
<p>Ok, then I'll use curly braces {-;</p>

#### [ Chris Hughes (May 08 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20finset%20to%20set/near/126258082):
<p>There's a <code>has_lift</code> instance for finset to set in <code>data.set.finite</code></p>


{% endraw %}
