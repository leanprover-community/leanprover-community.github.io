---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74045unsafecastsinmetaland.html
---

## Stream: [new members](index.html)
### Topic: [unsafe casts in meta land?](74045unsafecastsinmetaland.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 04 2019 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389422):
In a meta function, is there some way to do "unsafe casts"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389993):
`unchecked_cast`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154389995):
it's just `cast` with a fake proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154390017):
But it's not recommended. There are very few safe but type incorrect casts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unsafe%20casts%20in%20meta%20land%3F/near/154390060):
and the ones that exist already have names, like `unquot`


{% endraw %}
