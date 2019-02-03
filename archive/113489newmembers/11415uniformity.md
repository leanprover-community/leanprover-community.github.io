---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11415uniformity.html
---

## Stream: [new members](index.html)
### Topic: [uniformity](11415uniformity.html)

---


{% raw %}
#### [ Kenny Lau (Oct 21 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221947):
<p>Let's say <code>s</code> is an open set. Is <code>{ p | p.1 in s iff p.2 in s }</code> in the uniformity?</p>

#### [ Kenny Lau (Oct 21 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221951):
<p>what would be the set in the uniformity associated to this open set?</p>

#### [ Kenny Lau (Oct 21 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221955):
<p>or is that the wrong thing to ask?</p>

#### [ Sebastien Gouezel (Oct 21 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136225299):
<p>Elements of the uniformity are uniform neighborhoods of the diagonal. The set you write is not a neighborhood of the diagonal, so it can not belong to the uniformity. In general, there is no element of the uniformity canonically associated to an open set, as the uniformity is really a global notion. In a topological group, however, if <code>s</code> is a neighborhood of the identity, then <code>{p | p.1 - p.2 \in s}</code> belongs to the uniformity.</p>


{% endraw %}
