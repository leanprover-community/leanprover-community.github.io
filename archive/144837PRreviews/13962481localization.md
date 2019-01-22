---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/13962481localization.html
---

## [PR reviews](index.html)
### [#481 localization](13962481localization.html)

#### [Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152240956):
I need a better interface

#### [Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152240961):
@**Johan Commelin** any suggestion?

#### [Johan Commelin (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152240973):
Hmpf, can you explain what problems you are hitting?

#### [Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152240987):
I don't know

#### [Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152240994):
I'm just not sure whether I like `of_comm_ring` and `div`

#### [Johan Commelin (Dec 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241135):
I think they are fine. I would change `of_comm_ring` into `mk`. But that's just a name.

#### [Kenny Lau (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241166):
then why not change `div` to `mk` instead

#### [Johan Commelin (Dec 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241207):
Maybe that would be technically correct.

#### [Chris Hughes (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241468):
Aren't things called `mk` usually supposed to be surjective?

#### [Johan Commelin (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241568):
Ok, so let's not call it `mk`. (I thought of `mk` as the canonical map from the object you start with.)

#### [Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241731):
I don't think they have to be surjective, for objects with some kind of completion in them

#### [Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241735):
like the injection into a free group

#### [Johan Commelin (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241755):
So what about the case at hand?

#### [Mario Carneiro (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241767):
although I guess that's called `of` right now?

#### [Mario Carneiro (Dec 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152241825):
By analogy to `rat`, `div` -> `mk` and `of_comm_ring` -> `of`?

#### [Kenny Lau (Dec 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152318029):
```quote
Hmpf, can you explain what problems you are hitting?
```
 I feel like the lemmas I proved are very ad-hoc and unstructured

#### [Kenny Lau (Dec 21 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152327048):
@**Johan Commelin**

#### [Johan Commelin (Dec 22 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#481 localization/near/152375140):
Hmm... it looks quite fine to me. At least *I* don't see a way to improve this. (Apart from the suggestion Mario made above.)

