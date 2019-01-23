---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58376549overcategories.html
---

## Stream: [PR reviews](index.html)
### Topic: [#549 over categories](58376549overcategories.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321838):
Hi @**Johan Commelin**, is it a good idea to define over and under categories in terms of comma categories?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321844):
It is certainly less ergonomic that just defining them from scratch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321858):
So the question is if things are actually defeq enough that you can use theorems about comma categories directly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321868):
If they aren't, I'd suggest biting the bullet and making them separate, and explicitly showing at equivalence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321912):
But I'm not sure, and can't tell just from looking at the PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 21 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152322555):
Well, so far I haven't had much problems with using this definition. So I like it (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 03 2019 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154225310):
@**Scott Morrison|110087** You say that it is less ergonomic than defining from scratch. Otoh I think almost every line that I wrote would need an equivalent line in the "from scratch" definition (all the simp-lemmas). And lines such as
```lean
def forget {X : T} : (over X) ⥤ T := comma.fst _ _
```
can hardly be shorter when defining things from scratch. So far I haven't really felt like I was battling generality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 03 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154262094):
Oh, I agree that it's exactly as much effort for this PR. The question is how it differs to users. In particular the "from scratch" approach means users might not need to worry about filling in 'unit.star' in a few places.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 03 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154262108):
But I'm not at all confident about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154487442):
@**Reid Barton** What do you think?


{% endraw %}
