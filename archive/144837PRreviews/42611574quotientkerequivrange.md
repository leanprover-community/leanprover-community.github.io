---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/42611574quotientkerequivrange.html
---

## Stream: [PR reviews](index.html)
### Topic: [#574 quotient_ker_equiv_range](42611574quotientkerequivrange.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154473405):
@**Chris Hughes** Nice job. Should you also prove that the equiv is an iso?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474606):
Yes, but I'm not sure of the best way to state it. We already have that fact, since `lift` is a group hom but not with the best statement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474663):
Should it just be an instance, or do we want bundled group isomorphisms. I guess we do want bundled group isomorphisms at some point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474671):
Right, and then define the category `Grp` while you are at it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474777):
Should group isomorphisms be represented exclusively in terms of category theory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474788):
We have `linear_equiv` which doesn't mention categories.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474789):
I don't know anything about categories so I can't really comment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474887):
Hmm, I don't know if we should have a separate version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474888):
All I meant was that once you have bundled group homs, defining the category is also trivial. (Using the bundled category machinery.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474899):
What is a group iso for you? A group hom that is bijective, or an equiv where `to_fun` is a group hom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 05 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474901):
Category theory will give you the latter (and also require `to_inv` to be a group hom)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 05 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154475012):
Definitely an equiv

