---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54502finsupp.html
---

## Stream: [general](index.html)
### Topic: [finsupp](54502finsupp.html)

---


{% raw %}
#### [ Kenny Lau (Apr 18 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finsupp/near/125235580):
<p>I have a new idea: let's build finsupp using multiset</p>

#### [ Kenny Lau (Apr 18 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finsupp/near/125235584):
<p>heh, ignore me, this won't work at all</p>

#### [ Kenny Lau (Jul 22 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finsupp/near/130083934):
<p>Do we really ever need <code>α →₀ β</code> where <code>β</code> has no addition?</p>

#### [ Mario Carneiro (Jul 22 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finsupp/near/130084298):
<p>I would say yes. There are various places I can think of where you want some kind of finite support but the range doesn't necessarily have a structure so much as a default value. The tape of a turing machine is like this</p>


{% endraw %}
