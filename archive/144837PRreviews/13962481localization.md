---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/13962481localization.html
---

## Stream: [PR reviews](index.html)
### Topic: [#481 localization](13962481localization.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240956):
I need a better interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240961):
@**Johan Commelin** any suggestion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240973):
Hmpf, can you explain what problems you are hitting?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240987):
I don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240994):
I'm just not sure whether I like `of_comm_ring` and `div`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241135):
I think they are fine. I would change `of_comm_ring` into `mk`. But that's just a name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241166):
then why not change `div` to `mk` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241207):
Maybe that would be technically correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241468):
Aren't things called `mk` usually supposed to be surjective?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241568):
Ok, so let's not call it `mk`. (I thought of `mk` as the canonical map from the object you start with.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241731):
I don't think they have to be surjective, for objects with some kind of completion in them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241735):
like the injection into a free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241755):
So what about the case at hand?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241767):
although I guess that's called `of` right now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241825):
By analogy to `rat`, `div` -> `mk` and `of_comm_ring` -> `of`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152318029):
```quote
Hmpf, can you explain what problems you are hitting?
```
 I feel like the lemmas I proved are very ad-hoc and unstructured

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 21 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152327048):
@**Johan Commelin**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 22 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152375140):
Hmm... it looks quite fine to me. At least *I* don't see a way to improve this. (Apart from the suggestion Mario made above.)

