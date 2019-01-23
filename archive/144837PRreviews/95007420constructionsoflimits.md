---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/95007420constructionsoflimits.html
---

## Stream: [PR reviews](index.html)
### Topic: [#420 constructions of limits](95007420constructionsoflimits.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135788640):
This extends the first PR on (co)limits. It

Shows that C ⥤ D has limits if D does.
Constructs equalizers and products from limits.
Constucts limits from equalizers and products.
Constructs pullback from equalizers and binary products.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135793797):
Is `simp` slower or is `obviously` slower?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135793798):
And do you care at all? @**Scott Morrison|110087**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794099):
it's `obviously` slower

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794107):
I'm pretty sure that your compile time optimization goals are in direct opposition with Scott's goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794113):
which is why he was so sad to read your `faster` branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794160):
`obviously` calls everything else, including `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794176):
well I'm also sad to read this PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794323):
I think that's fair. @**Scott Morrison** is there a reason you have decided to use `obviously` directly instead of the script that it generates?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796411):
So that I don't have to do any copying and pasting? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796427):
So that the compile time of mathlib grows so large that more effort is put into tactic caching? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796464):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796475):
I've already ripped out a huge number of `obviously` in these two PRs. All the sequences of `rw` are actually generated automatically by `rewrite_search` in my still-private version of `obviously`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796477):
I can rip out more, of course ...

