---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/61216396squeezesimp.html
---

## Stream: [PR reviews](index.html)
### Topic: [#396 squeeze_simp](61216396squeezesimp.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353930):
#396

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353970):
I'm afraid some of the changes to the tactic files in the `faster` branch hasn't been transferred to the `squeeze_simp` PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353972):
@**Mario Carneiro** what should I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354026):
make another follow-on PR...  what was it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354029):
I don't really know what happened, now that the history has been erased

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354036):
I just see that some changes to the tactic files have not been incorporated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354083):
if you rebase the `faster` branch on master, it should remove any parts that are already merged, leaving only the stuff that is missing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354089):
I've rebased the `faster` branch on master

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354090):
maybe I should rebase the `squeeze-simp` branch on master and see what happens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354091):
is this a good idea?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354137):
squeeze-simp is already merged, so if you rebase it on master it will disappear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354144):
just look at [this](https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-a5e03974850487ddd92200ffaf57f9b2L18)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354152):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354153):
I see that the `squeeze-simp` branch has been changed after its separation from `faster`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354154):
at this point I don't know what to do anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354156):
just delete/revert any changes in those files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354201):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354261):
how about [this](https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-47cbe97193e277c9a413e62bc8afadffR15)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354266):
@**Simon Hudon** could you clarify which one is the intended version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360028):
Hi! I made some changes to in `squeeze-simp` to add documentation and make the tactic usable for @**Scott Morrison|110087** to use in `tidy`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360029):
This is a great idea to have this stream btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360133):
@**Simon Hudon** did you see my link?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360194):
I have. It seems to confirm what I thought the diff would be. Is there something in particular that you're trying to highlight?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360241):
if you wait for a while after opening the link, it will show you one line I highlighted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360247):
so in particular I'm talking about the file `meta/rb_map.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360248):
could you clarify which side is the version you want mathlib to have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360943):
I think either one can work. I ended up not needing those functions I think but they are generally useful functions so we can keep them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362776):
@**Simon Hudon** then which one of us should make a new PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362782):
Why do we need a new PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362786):
the same reason this one is a PR separate from `faster`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362891):
I don't think it's worth making a separate PR for it. If you want to take it out of yours, let's just bring it back when we need it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362894):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362895):
how do I do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362900):
is there some `git` magic that will let me do this or do I have to do it manually?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135363076):
With `git log meta/rb_map.lean`, you can check what is the latest commit that changed the file, that's probably where I introduced those functions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135363086):
Actually, let me look into it, I'll create the PR while I'm at it

