---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/13525512discretecategories.html
---

## Stream: [PR reviews](index.html)
### Topic: [#512 discrete categories](13525512discretecategories.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904838):
Really this is "everything that I thought worth saving from the old limits PR, not including anything about special shapes".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904883):
In particular it includes discrete categories, and some minor tidying in several files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904974):
I've also rebased what remains of my "special shape limits" work onto this. (This is not intended as any endorsement of the contents. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 05 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905483):
@**Scott Morrison|110087** Looks good to me. Isn't the `of_obj` in your PR superseded by my `of`-PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905494):
Ah, yes, I'd forgotten that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905496):
Is yours already merged?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 05 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905546):
Nope, not yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 05 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905778):
ok, I removed `of_obj` again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 07 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151128542):
@**Scott Morrison|110087**, I think it's better to make "assorted changes" into separate PRs or at least separate commits.
That makes it easier for the maintainers to commit parts as soon as they are happy with them, and not have to think about those parts again for every round of review of the other, more substantial changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 16 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151891968):
@**Scott Morrison|110087** Do you think you have time somewhere this week to look at this PR? There's a couple of comments. Would it make sense to split of the discrete categories as a separate PR? (I think smaller chunks get merged faster...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151902875):
is discrete category the free functor Set -> Cat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 17 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151907735):
Yes, although we don't have Cat as a category yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 20 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/152244018):
I've updated this PR now. (Sorry it was a grab-bag PR. I'll avoid these in future.)


{% endraw %}
