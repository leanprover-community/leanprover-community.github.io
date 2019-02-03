---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74045unsafecastsinmetaland.html
---

## Stream: [new members](index.html)
### Topic: [unsafe casts in meta land?](74045unsafecastsinmetaland.html)

---


{% raw %}
#### [ Scott Morrison (Jan 04 2019 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389422):
<p>In a meta function, is there some way to do "unsafe casts"?</p>

#### [ Mario Carneiro (Jan 04 2019 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389993):
<p><code>unchecked_cast</code></p>

#### [ Mario Carneiro (Jan 04 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389995):
<p>it's just <code>cast</code> with a fake proof</p>

#### [ Mario Carneiro (Jan 04 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154390017):
<p>But it's not recommended. There are very few safe but type incorrect casts</p>

#### [ Mario Carneiro (Jan 04 2019 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154390060):
<p>and the ones that exist already have names, like <code>unquot</code></p>


{% endraw %}
