---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59343overridingdecidableinstances.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [overriding decidable instances](https://leanprover-community.github.io/archive/113488general/59343overridingdecidableinstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134423873):
<p>Can someone point me to an example of overriding a <code>decidable</code> instance with a faster algorithm?</p>

#### [ Scott Morrison (Sep 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134423881):
<p>The implementation of <code>nodup_decidable</code> is too slow. :-)</p>

#### [ Simon Hudon (Sep 22 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424056):
<p>You create your own instance and you give it higher priority than <code>nodup_decidable</code>. Is this for lists? Be sure that the culprit <code>nodup_decidable</code> and not the fact that comparing objects (e.g. <code>nat</code>) is slow</p>

#### [ Simon Hudon (Sep 22 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424102):
<p>One more consideration: is this for a proof or for a program? If it's for a proof, you can write a tactic that does the comparison faster.</p>

#### [ Mario Carneiro (Sep 22 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424115):
<p><code>decidable_prime</code> has two implementations</p>

#### [ Mario Carneiro (Sep 22 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424265):
<p>For checking <code>nodup</code> of big things like those lists of numbers, it helps if you've put them in order. <code>list.chain</code> is linear time</p>

#### [ Mario Carneiro (Sep 22 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/overriding%20decidable%20instances/near/134424560):
<p>Oh, wait this doesn't work for cycles, since the order matters. You can still improve on the n^2 performance of the default implementation by utilizing the order. If you sort the list then you can check for duplicates in linear time</p>


{% endraw %}
