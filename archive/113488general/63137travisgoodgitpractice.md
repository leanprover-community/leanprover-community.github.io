---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63137travisgoodgitpractice.html
---

## Stream: [general](index.html)
### Topic: [travis / good git practice](63137travisgoodgitpractice.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133791639):
I am trying to use all this git/github/community mathlib infrastructure maturely now.

I am in the middle of writing the proof of Hilbert basis, in a branch in my local clone of community mathlib. I've not got very far because I was distracted by (a) not having interface for coefficients of polynomials and (b) the zero ring being a constant special case. In both cases I created new branches (from master, not from my Hilbert basis branch) with small edits to files, and PR'ed directly to mathlib. My Hilbert basis branch is now pushed to community mathlib as a WIP. It depends on both these branches above -- is that a problem? I'm assuming that the system is sufficiently mature to make it not so (I am hoping I can rebase from master if and when these easy PR's are accepted). 

 I also got involved in a different project -- adding matrices over a general ring -- and made yet another branch for these. I PR'ed this to mathlib too and then Sean almost completely rewrote it (which is great, this is exactly what community mathlib is for) and I see that the PR automatically gets updated. I am hoping that I've just about got these things right now. Scott pointed out that using `git merge` can cause chaos with history (as indeed it did with a previous zerology branch I'd created, which I've now deleted) and hopefully I've managed to use rebase correctly to make history look reasonable in all these cases. I occasionally update mathlib from upstream and rebase. If anyone has any comments on anything I'm still doing wrong with this set-up I'd be happy to hear them.

As for travis -- apparently it has failed on the matrix PR :-( I can't see why. Is the fault of travis? There were github problems yesterday apparently.

It's this one: https://github.com/leanprover/mathlib/pull/334

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 12 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133791809):
It looks like the error is due to a timeout: https://travis-ci.org/leanprover/mathlib/jobs/427142459 . This happens occasionally on Travis-CI.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 12 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133791857):
My Travis-CI build passed for that same branch: https://travis-ci.org/spl/mathlib/builds/427091112

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 12 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133792058):
Once the zerology and coefficients PRs have landed in master, you should rebase the Hilbert basis branch on top of master and then PR it (when ready).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 12 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133792143):
The zerology and coefficients patches also exist on your `kmb_hilbert_basis` branch and you probably shouldn't try to rebase them onto master when the time comes, because it's likely that small changes will have been made to them before merging. I can tell you about how to do that now or later (short version: use `git rebase --onto`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 12 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133792292):
Or I guess you can also use `git rebase -i` and then just delete the lines for all the patches you don't want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133793440):
Hmm. Once the PR's land in master, are the traditional edits done in mathlib master? If so I can't merge my local branches with upstream changes -- the community branches never see them. But really what I think I want to happen with the `kmb_hilbert_basis` branch is that I just squash everything down to one commit after I'm finished. I guess I only committed a partially-written proof to back it up in case my laptop dies.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 12 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133794954):
I assume somebody is pulling `leanprover/mathlib` master into `leanprover-community/mathlib` master every now and then? At least, I see they are equal right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 12 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133795047):
Actually it doesn't really matter--I don't know how you have your checkouts set up but you can have both `leanprover/mathlib` and `leanprover-community/mathlib` as remotes in the same local `mathlib` repository. Then you (or anyone) can rebase your `kmb_hilbert_basis` branch on top of `leanprover/mathlib`'s master

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 12 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/133795128):
Yes, I've been pulling leanprover to leanprover-community whenever I notice it out of sync.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 27 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136577522):
which one is safer, `merge` or `rebase`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 27 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136577524):
(whatever "safe" means)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 27 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136579530):
I guess merge is kind of "safer"? It retains more information about the history of commits. Usually that's information you don't actually want though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Oct 27 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589291):
`rebase` rewrites history
`merge` just makes yet another (maybe slightly fancy) commit
People argue about what best practice is, and some people zealously say you shouldn't ever rebase anything
A consequence of rewriting history though is that other people who used to have the same history as you can't cleanly just merge their work back together with yours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Oct 27 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589342):
You can never just delete your own work by merging something, but with rebase you can easily drop commits which you might have to go back and find using `git reflog`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589344):
Keep in mind that lean and mathlib both use a rebase workflow. It doesn't necessarily affect what you do as a third party, but mathlib has a linear commit history as a result. I think this is better organizationally than the big tangle it would be otherwise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589386):
I don't think `rebase` will cause you to lose work, unless you mess up the merge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589435):
also if your branch is based on some commits which have since been rebased (so you are sitting on a separate version of the same commits) then if you rebase your branch on the master these commits will disappear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Oct 27 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589436):
If you `git rebase -i HEAD~10` and then accidentally drop a line from the resulting file, then the commit will be dangling and you will have to find it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589438):
oh yes, interactive rebase is basically just editing history, and you can do whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589443):
I meant just plain `git rebase`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 27 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20/%20good%20git%20practice/near/136589490):
which should have roughly the same merge behavior as `git merge` except that the final commits are arranged linearly


{% endraw %}
