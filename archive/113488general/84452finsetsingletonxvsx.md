---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84452finsetsingletonxvsx.html
---

## Stream: [general](index.html)
### Topic: ["finset.singleton x" vs "{x}"](84452finsetsingletonxvsx.html)

---


{% raw %}
#### [ Kenny Lau (Sep 28 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134833971):
<p>there are two ways to write the same finset. there's a simp lemma converting the latter to the former. however there are also many lemmas written using the latter instead of the former. so what is the standard?</p>

#### [ Kenny Lau (Sep 28 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134834042):
<p>I don't even know if it's a good idea to inherit the multiset singleton as <code>finset.singleton</code> to begin with. That means I don't see why there needs to be two traditions at all and we should just stick to {x}</p>

#### [ Kenny Lau (Sep 28 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134834160):
<p>also when there are two things that represent the same thing, don't we usually write two lemmas each time?</p>

#### [ Mario Carneiro (Sep 28 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134838973):
<p>finset.singleton doesn't require decidable_eq</p>

#### [ Chris Hughes (Sep 28 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134839003):
<p>Is that the only reason?</p>

#### [ Mario Carneiro (Sep 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134839093):
<p>I think so... unfortunately root.singleton is a definition rather than a typeclass</p>

#### [ Mario Carneiro (Sep 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22finset.singleton%20x%22%20vs%20%22%7Bx%7D%22/near/134839212):
<p>it is also marginally faster to execute</p>


{% endraw %}
