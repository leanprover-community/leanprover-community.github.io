---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11415uniformity.html
---

## Stream: [new members](index.html)
### Topic: [uniformity](11415uniformity.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 21 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221947):
Let's say `s` is an open set. Is `{ p | p.1 in s iff p.2 in s }` in the uniformity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 21 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221951):
what would be the set in the uniformity associated to this open set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 21 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136221955):
or is that the wrong thing to ask?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 21 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/uniformity/near/136225299):
Elements of the uniformity are uniform neighborhoods of the diagonal. The set you write is not a neighborhood of the diagonal, so it can not belong to the uniformity. In general, there is no element of the uniformity canonically associated to an open set, as the uniformity is really a global notion. In a topological group, however, if `s` is a neighborhood of the identity, then `{p | p.1 - p.2 \in s}` belongs to the uniformity.

