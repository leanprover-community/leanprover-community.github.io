---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75628importrenaming.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [import renaming?](https://leanprover-community.github.io/archive/113488general/75628importrenaming.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161156):
<p>can someone point me to the syntax for import renaming? I can't find it. :-(</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161170):
<p>I don't think there is such a thing</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161216):
<p>I think it was proposed for lean 4, but AFAIK it can't be done in lean 3</p>

#### [ Patrick Massot (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161219):
<p>People often talk about it here, but only to wish it exists</p>

#### [ Scott Morrison (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161224):
<p>oh, wow, maybe I dreamt it. I have a really strong memory of yesterday learning that you could hide and rename individual declarations when you made an import!</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161259):
<p>There is <code>open</code> and <code>hide</code>, which have a syntax for opening individual declarations and renaming</p>

#### [ Johan Commelin (Aug 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161343):
<p>I don't think you learnt that here...</p>

#### [ Sebastian Ullrich (Aug 09 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131184956):
<p>Declarations in a Lean environment aren't grouped by modules, so I don't see how this would be implemented without fundamentally changing the architecture. Which we don't plan to do, afaik.</p>


{% endraw %}
