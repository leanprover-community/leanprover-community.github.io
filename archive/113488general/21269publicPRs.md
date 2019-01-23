---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21269publicPRs.html
---

## Stream: [general](index.html)
### Topic: [public PRs](21269publicPRs.html)

---


{% raw %}
#### [ Mario Carneiro (Aug 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131008853):
I'd like to introduce a slight change in PR management on mathlib. In order to support third party contribution to PRs, I would like to introduce "PR branches" to mathlib. The basic idea is, if there is a PR that is currently in review, for which you are not the author, and you would like to help get it into mathlib, just ask to have it made public on the PR page, and I will add it as a branch on the mathlib repo. This way, if a PR is stalled, you can get it back on track. I think this will make collaboration on WIPs easier, although it will probably confuse GitHub a bit, because of the way PR pages are set up. If you PR to a PR branch, make sure to reference the original PR # so that we can navigate between them through GitHub.

#### [ Simon Hudon (Aug 07 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009168):
Would it be useful to have a separate account for those WIP? That way you can have a stricter separation between the PRs. The added benefit is that you may promote more maintainers for that account

#### [ Mario Carneiro (Aug 07 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009234):
an interesting idea, I hadn't thought about having a public fork

#### [ Mario Carneiro (Aug 07 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009364):
You may or may not recall that mathlib was once https://github.com/leanprover/library_dev . When we first moved from library_dev to mathlib, the idea was that library_dev might contain more experimental stuff or stuff that doesn't quite compile, but that never really happened

#### [ Simon Hudon (Aug 07 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009435):
I vaguely remember. I think a PR account might have to refrain from having a master branch. It would really be only a waiting room for big PRs

#### [ Mario Carneiro (Aug 07 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009497):
well, if it's a fork of mathlib then it will have a master branch, that is just tracking mathlib

#### [ Simon Hudon (Aug 07 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009519):
Yeah exactly. I would just refrain from merging anything into `master` that `leanprover/mathlib` doesn't have

#### [ Mario Carneiro (Aug 07 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009698):
I'm liking the idea so far. @**Jeremy Avigad** What do you think about this? I can create a `lean-sandbox` user account, fork mathlib, and just give write access to anyone who wants it. People can still use the PR system on the sandbox account if they want, or create branches and PR them to mathlib.

#### [ Simon Hudon (Aug 07 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009815):
I recently created `https://github.com/leanprover-community/lean-mode-contrib` to host community contributions to `lean-mode`. It could double as a home for mathlib PRs

#### [ Mario Carneiro (Aug 07 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009834):
sounds good

#### [ Mario Carneiro (Aug 07 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009910):
is `lean-mode-contrib` a fork of something?

#### [ Simon Hudon (Aug 07 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131010064):
Not quite. I thought I'd make it a mode that adds to `lean-mode`. I'm replicating some functionalities from `company-coq`. And now that the repo exists, I think I'll start adding some of my own scripts (like shortcuts for adding common libraries to your leanpkg.toml file).

#### [ Simon Hudon (Aug 07 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131010110):
Now that you ask, it might work if I just make it a fork of `lean-mode` with added features.

#### [ Jeremy Avigad (Aug 07 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131011594):
@**Mario Carneiro** no objection here.

#### [ Mario Carneiro (Aug 07 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131011651):
Great! @**Kevin Buzzard** What do you think about migrating `for_mathlib` to this new repo?

#### [ Simon Hudon (Aug 07 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131012185):
I suggest we choose a couple of maintainers for that repo. I already sent you and Johannes an invitation. I can send others.

#### [ Mario Carneiro (Aug 07 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013207):
I can be a maintainer, but I expect there won't be much maintaining going on

#### [ Mario Carneiro (Aug 07 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013212):
mostly it's just branch organization and such

#### [ Mario Carneiro (Aug 07 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013268):
Since the idea is to have it free for all, it's up to individuals to maintain their own branches as they see fit

#### [ Mario Carneiro (Aug 07 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013282):
I am inspired in part by metamath's "mathbox" infrastructure, although in that case the mathboxes are required to compile at all times but are otherwise organized at the discretion of the user

#### [ Simon Hudon (Aug 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013456):
In principle, the maintainers will have to accept pull requests too. That's why I would err towards more maintainers rather than fewer. 

I've never heard of the mathbox. Do you have a reference for it?

#### [ Mario Carneiro (Aug 07 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131015487):
http://us.metamath.org/mpeuni/mmtheorems.html#19

#### [ Kevin Buzzard (Aug 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030200):
I don't really understand this proposal (that's not some implied criticism -- I just actually mean I don't understand it). I've just looked through the perfectoid `for_mathlib` directory and I see stuff I wrote and then forgot about, stuff which would be trivial to PR into mathlib, stuff which I half-wrote (quotient rings) and then someone else wrote better and which might already have been PR'ed -- after our discussion yesterday I'm wondering whether actually it might introduce some kind of order into the system if some of the really basic stuff like quotient additive groups and quotient rings should get into mathlib ASAP (indeed some of it might be there already). One thing I certainly don't want is for us to end up in the situation where people are relying on me to do things, as I already have far too much to do. As you know Mario I have started making tiny mathlib PRs, just dipping my toe in as it were; the stuff I put in "for_mathlib" myself is just stuff which I feel like it would be too much effort for me to PR into mathlib. On the other hand I'm coming round to the idea that perhaps  working from the bottom up is actually a good idea (rather than what we're currently doing, which is working top down, bottom up and in the middle all at once). 

I think the problem I currently have with the mathlib set-up (which is I think why I started the "for-mathlib" directory) is the following. Let's say I realise I need 50 lines of code about e.g. topological groups, which is not in mathlib, but which would very naturally live in an existing mathlib file, e.g. `analysis/topology/topological_structures.lean`. The thing is, I want them *now*. I could either edit `topological_structure.lean` and make a PR, which would take me a long time because mathlib has conventions I don't know about or don't understand, and then there would be some to-ing and fro-ing whilst people told me that I've proved this lemma in a stupid way, and that lemma is just `by simp`, and that lemma is already there, and that lemma never uses inverses so it should really be in the topological monoid section -- and then I have to find time to edit everything etc etc to try and fix it up -- and this process can easily go on for weeks. During that time I find it really hard to actually access my own work, because it is "in limbo" -- it's not in mathlib and so it's not in my project. It's *much* easier just to write `for_mathlib/topological_structures.lean` and prove the lemmas I want, with their bad names and bad proofs and superfluous hypotheses, because then I can start using them immediately, because I'm not really interested in these lemmas anyway, I'm far more interested in doing the "meat" which is the perfectoid spaces, and in some sense I just want someone else to prove these basic facts about topological groups, someone who knows what they're doing and will do it right the first time. Unfortunately the set of such people is pretty small and they all have their own things that they're doing. I'm not motivated to PR, because of this. 

Will the proposed system offer some sort of alternative approach which gets me out of this hole?

#### [ Mario Carneiro (Aug 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030222):
> One thing I certainly don't want is for us to end up in the situation where people are relying on me to do things, as I already have far too much to do.

The idea here is to allow other people to work on your PRs

#### [ Mario Carneiro (Aug 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030404):
> Let's say I realise I need 50 lines of code about e.g. topological groups, which is not in mathlib, but which would very naturally live in an existing mathlib file, e.g. analysis/topology/topological_structures.lean. The thing is, I want them *now*.

I am fully aware of this situation, I often have to deal with it myself. The solution I came up with for this is to have a `pending` directory or file, which serves basically the same purpose as your `for_mathlib`. The difference is that I PR *first*, and then put something as close as possible to my PR into this pending area during the review period. That way, once the PR is accepted all I have to do is delete the relevant portion from the pending area.

#### [ Mario Carneiro (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030672):
(mathlib used to have a `pending` directory, but I removed it since lean core no longer accepts PRs.)

#### [ Kevin Buzzard (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030721):
I see. So basically you're saying that I'm doing it wrong, and I am beginning to learn from my own experience that the "code now, PR later" approach has its disadvantages (e.g. I think that my partially written quotient ring code might be obsolete -- did Chris PR this? I still struggle with quotients; I have `a ≈ 0↔ ⟦a⟧ = ⟦0⟧ : by sorry` in my code at some point). I think it's far easier (for me at least) to understand other people when they say "do it my way not your way", once I've begun to realise the disadvantages of my way.

#### [ Johan Commelin (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030722):
Which is a pity. It would be awesome if they would accept one final PR that moved all of core into mathlib.

#### [ Mario Carneiro (Aug 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030916):
I'm not saying you have to PR everything as soon as it is written. But once you decide you have something you want to get into mathlib, it moves from where it currently is, probably some random file in your project, to the `for_mathlib` area and also into a PR, possibly [WIP]. Then you get feedback on your stuff, and if you make any updates to the PR you can either copy them to your local version or just leave the pending area out of date and update later (if you think it will affect your project I would recommend you update sooner rather than later).

#### [ Mario Carneiro (Aug 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131031154):
> I think it's far easier (for me at least) to understand other people when they say "do it my way not your way", once I've begun to realise the disadvantages of my way.

I know I have a bad habit of asking people to "do it my way not your way", but I try to explain what the major issues are. The main problem is that making bad design decisions can be very expensive time-wise, without even alerting you to the possibility that the cost is avoidable. So when I hear that you've been struggling with an issue for several months and just working around it, my heart goes out to you and I wish I could have saved you from that.

#### [ Johan Commelin (Aug 08 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088374):
Is this public repo already available?

#### [ Mario Carneiro (Aug 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088548):
it is now https://github.com/leanprover-community/mathlib

#### [ Johan Commelin (Aug 08 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088817):
Ok, cool! And how would one create a new public PR branch on it?

#### [ Johan Commelin (Aug 08 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088838):
Should one ask for push access in this topic?

#### [ Mario Carneiro (Aug 08 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088859):
yeah, that seems fine

#### [ Mario Carneiro (Aug 08 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089133):
okay I think I figured it out. You should now be a "collaborator" on leanprover-community/mathlib

#### [ Mario Carneiro (Aug 08 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089305):
I just sent invites to everybody who has ever been reasonably active on mathlib. If you didn't get one just ask

#### [ Simon Hudon (Aug 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089569):
If you want to use leanprover-community/mathlib to create a PR, I propose you start by creating a branch from leanprover/master. Do not commit to leanprover-community/master directly, that branch is only meant to track leanprover/master.

#### [ Patrick Massot (Aug 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100321):
Let me check I understand correctly what I'm meant to do. I close my current norm PR. Push my norm branch to this new repository, open a new PR from there, right?

#### [ Scott Morrison (Aug 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100390):
Yes, that's about right!

#### [ Sean Leather (Aug 08 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100889):
The [shared mathlib fork](https://github.com/leanprover-community/mathlib) doesn't seem to add much benefit over any other mathlib fork. You could easily use your own. It really is just a bit more convenient is that it has an established “trusted” set of collaborators, so that anyone in that group can contribute to anyone else's work. But if you want to work with only a different set of collaborators, you can also set up your own fork. But it's also a bit more questionable in that there's no clear policy for who does what with what branches, which can cause problems if people have different assumptions or don't communicate changes to each other.

#### [ Patrick Massot (Aug 08 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100915):
Clearly it assumes quite a bit a trust, but let's see how it goes (I'm pretty optimistic here).

#### [ Sean Leather (Aug 08 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101252):
I think I'd do this differently. Instead of a mathlib fork, I'd suggest a sort of mathlib nursery, which is a library that has mathlib as a dependency. The collaborators would be set up as they are now, but the library source would be initially empty and added to by anyone on the `master` branch. Then, everybody moves WIP stuff into the mathlib-nursery. Once somebody's happy with part of their work, they can get feedback from others and somebody can PR that to mathlib. When the PR makes it into mathlib, the mathlib dependency commit is updated and the work is removed from mathlib-nursery.

#### [ Patrick Massot (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101266):
Too late, I opened https://github.com/leanprover/mathlib/pull/241 Let's see how this idea works out

#### [ Sean Leather (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101268):
The main difference is that everybody works on `mathlib-nursery/master` instead of multiple `mathlib` branches.

#### [ Sean Leather (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101274):
Actually, maybe mathlib-nursery and this mathlib fork can coexist and both be useful.

#### [ Patrick Massot (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101316):
The advantage of the current proposal is we don't have to move things into their final position

#### [ Sean Leather (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101318):
So, work starts in the nursery and then moves to the fork.

#### [ Patrick Massot (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101323):
And now Mario has to work on norms in order to prove his new workflow is useful :wink:

#### [ Sean Leather (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101325):
The advantage of the nursery is that things can change and you don't need to worry about final positions. :smile:

#### [ Patrick Massot (Aug 08 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101334):
My experience is that the moving to final position phase is very boring and time consuming

#### [ Sean Leather (Aug 08 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101343):
```quote
And now Mario has to work on norms in order to prove his new workflow is useful :wink:
```
But the leanprover-community/mathlib doesn't add anything to what you're doing. You could always have allowed the mathlib collaborators access to your branch.

#### [ Sean Leather (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101386):
What it does allow is non-mathlib collaborators to work on your branch.

#### [ Patrick Massot (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101399):
Right, so *you* should work on that branch, mess it up and prove Mario was wrong.

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101412):
no, wait

#### [ Sean Leather (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101418):
Alternatively, if it was in a nursery, I could already be using it within the nursery. :wink:

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101422):
Say Kenny works on it

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101428):
or Chris, and prove Mario was right

#### [ Kenny Lau (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101432):
work on what

#### [ Johan Commelin (Aug 08 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101480):
You *should* do Patrick's homework :rolling_on_the_floor_laughing:

#### [ Patrick Massot (Aug 08 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101481):
https://github.com/leanprover-community/mathlib/tree/norms

#### [ Patrick Massot (Aug 08 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101489):
That's a new branch is the new mathlib fork where everyone from the community can improve on a PR

#### [ Mario Carneiro (Aug 08 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101944):
The "nursery" idea is closer to the original purpose of `library_dev`

#### [ Mario Carneiro (Aug 08 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102033):
Both options have their uses. I think the main factor is whether you want to work in a project that has a mathlib dependency, or in mathlib itself. For mathlib PRs of course the second option is better

#### [ Mario Carneiro (Aug 08 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102114):
For offshoot projects and experiments, a separate project is maybe nicer to work with, although you lose the ability to modify bits of mathlib to accomodate the work

#### [ Sean Leather (Aug 08 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102193):
```quote
Both options have their uses. I think the main factor is whether you want to work in a project that has a mathlib dependency, or in mathlib itself. For mathlib PRs of course the second option is better
```
Yeah, agreed. I think it would be nice to have a community-based nursery for stuff not ready for PR.

#### [ Sean Leather (Aug 08 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102261):
So, there could be a staged process:

1. throw it in the nursery, let other people use it or work on it
2. when matured, create a community mathlib PR for it

#### [ Sean Leather (Aug 08 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102266):
By definition, what's in the nursery is immature.

#### [ Kevin Buzzard (Aug 08 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131107122):
Whilst I have no understanding of the ins and outs of this new proposal, I think that there's a lot to be said for trying a random new thing and seeing how it turns out.

#### [ Kevin Buzzard (Aug 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113284):
OK so I want to try and get some of this `for_mathlib` stuff out of the perfetoid repo and into mathlib. I want to start with https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_submonoid.lean that file, which is Johan Commelin literally translating https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean into additive notation. There is also an `add_subgroup.lean` file which is the corresponding translation of `subgroup.lean`. Do I PR to mathlib? Do I push to mathlib-community?

#### [ Kevin Buzzard (Aug 08 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113483):
This is the other file I would like to get into mathlib: https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_subgroup.lean, a translation of https://github.com/leanprover/mathlib/blob/master/group_theory/subgroup.lean .

#### [ Mario Carneiro (Aug 08 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113511):
literal translation of files to additive notation is what `to_additive` is for

#### [ Kevin Buzzard (Aug 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113570):
OK. So what do we do?

#### [ Kevin Buzzard (Aug 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113588):
Because at the end of the day I want to quotient out an additive group by a subgroup and it's time to make progress.

#### [ Kevin Buzzard (Aug 08 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113616):
because what I really want is to quotient out a ring by an ideal and then borrow some properties from the group quotient.

#### [ Kevin Buzzard (Aug 08 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113635):
because what I really want is to prove some basic results about valuations, and I need ring quotients.

#### [ Mario Carneiro (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113682):
PR it

#### [ Kevin Buzzard (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113689):
PR the two files I just linked to? To mathlib or the community one?

#### [ Mario Carneiro (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113697):
do it from the community fork if you think someone else is going to clean it up for you

#### [ Kevin Buzzard (Aug 08 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113736):
What if I don't have a clue if someone else is going to clean it up for me and I don't know how to do it myself either?

#### [ Mario Carneiro (Aug 08 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113748):
then I will clean it up or it will languish

#### [ Kevin Buzzard (Aug 08 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113796):
And should I then make the perfectoid repo depend on community mathlib instead of regular mathlib?

#### [ Mario Carneiro (Aug 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113900):
No, you should keep the stuff in `for_mathlib` and develop the PR independently

#### [ Kevin Buzzard (Aug 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113904):
I see. Thanks!

#### [ Kevin Buzzard (Aug 08 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114525):
So after `git push --set-upstream origin additive-subgroup-theory` github thinks I'm about to submit a PR to mathlib. Is that what I am supposed to be doing?

#### [ Kevin Buzzard (Aug 08 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114617):
My `origin` is `	git@github.com:leanprover-community/mathlib.git `

#### [ Kevin Buzzard (Aug 08 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114640):
i.e. is this just a regular PR to mathlib, but from the community fork rather than my own personal fork?

#### [ Mario Carneiro (Aug 08 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114646):
yes

#### [ Simon Hudon (Aug 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131134390):
@**Sean Leather** I like the idea of a nursery. It makes it easier to get features used faster. The only downside is that you can't adapt any existing features of mathlib. I wonder if it might grow into a huge mess. Maybe we can still try to keep it clean.

#### [ Simon Hudon (Aug 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131134398):
I'm tempted in creating that nursery. Any objections?

#### [ Sean Leather (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155297):
```quote
I'm tempted in creating that nursery. Any objections?
```
Go for it. I'll share the responsibility for keeping it clean. If you don't get around to it, I will create it.

#### [ Mario Carneiro (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155306):
I'm on board

#### [ Simon Hudon (Aug 09 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155535):
Done! You two should have received an invitation. And I think we can include move people still

#### [ Sean Leather (Aug 09 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155610):
Got it. Are you going to initialize it with a `README.md`?

#### [ Mario Carneiro (Aug 09 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155646):
You could initialize it with the content of `library_dev`

#### [ Sean Leather (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155765):
One minimal requirement that I would have and would state on the `README.md` is that the code should build successfully for a given commit of mathlib and Lean version and not have any `sorry`s. I don't think it's an issue if the code changes significantly over time, but it's a pain for others if it doesn't build.

#### [ Mario Carneiro (Aug 09 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155820):
I think that is too strict a requirement. Perhaps it should build but `sorry` is allowed?

#### [ Sean Leather (Aug 09 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155828):
The problem is that `sorry`s infect downstream code and clutter the error and warning messages.

#### [ Mario Carneiro (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155836):
Mathlib already has that requirement, and I know it stops me from publishing stuff early because I think the work is not done yet

#### [ Mario Carneiro (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155840):
but for something that brands itself as a "nursery", it should explicitly accept unfinished work

#### [ Sean Leather (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155845):
Would it resolve your concern if you're allowed to use non-`master` branches for that code?

#### [ Sean Leather (Aug 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155887):
You still have to accept that the library is shared and not private.

#### [ Simon Hudon (Aug 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155890):
Here it is: https://github.com/leanprover-community/mathlib-nursery

#### [ Sean Leather (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155897):
So I think it's appropriate to ask collaborators to minimize the burden.

#### [ Johan Commelin (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155904):
"The features are available a library in the meantime." typo in the README

#### [ Mario Carneiro (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155905):
A `sorry` in the middle of the code doesn't hurt anyone, and it is still being checked for correctness

#### [ Mario Carneiro (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155906):
I would rather just filter out sorry warnings

#### [ Johan Commelin (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155910):
But I don't think it is too much trouble to do *everything* in non-master branches, right?

#### [ Simon Hudon (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155952):
@**Johan Commelin** It is work in progress, I'll get it right eventually ;-)

#### [ Mario Carneiro (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155960):
Well, the nursery is different since it's not tracking mathlib

#### [ Johan Commelin (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155962):
If you make me a collaborator, you could delegate that (-;

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155963):
it needs a master branch, and everyone should be not too far away from it

#### [ Johan Commelin (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155968):
Hmmm. I don't understand nurseries.

#### [ Johan Commelin (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155973):
(Never went to one as a toddler.)

#### [ Sean Leather (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155976):
```quote
A `sorry` in the middle of the code doesn't hurt anyone, and it is still being checked for correctness
```

I disagree. It adds overhead in terms of messages.

```quote
I would rather just filter out sorry warnings
```

How?

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155978):
awk script?

#### [ Sean Leather (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155979):
Also, I'd like to see my own `sorry` messages and not those of others

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155983):
then don't compile or depend on others

#### [ Mario Carneiro (Aug 09 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156028):
we can have the travis build just ignore sorries

#### [ Sean Leather (Aug 09 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156029):
```quote
Well, the nursery is different since it's not tracking mathlib
```
But it is, isn't it? https://github.com/leanprover-community/mathlib-nursery/blob/master/leanpkg.toml#L8

#### [ Sean Leather (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156039):
I'd really rather not have `sorry`s in the first place. I don't think that's too strong a requirement.

#### [ Simon Hudon (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156040):
It depends on mathlib but does not track it

#### [ Mario Carneiro (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156041):
I mean in the git sense - it's not a fork

#### [ Sean Leather (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156049):
Well, forks also don't track in any sense that I can think of. :wink:

#### [ Mario Carneiro (Aug 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156102):
I can tell you for sure that there are people who work with sorries for long periods, on projects that would be appropriate for this nursery

#### [ Mario Carneiro (Aug 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156104):
and this was also how `library_dev` worked

#### [ Mario Carneiro (Aug 09 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156160):
Even in mathlib it feels like too strong a requirement sometimes. It's just that lean has a completely stupid reporting mechanism for sorry

#### [ Sean Leather (Aug 09 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156172):
The downstream warnings are definitely too much.

#### [ Mario Carneiro (Aug 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156224):
they make sense in server mode but not in `lean --make`

#### [ Mario Carneiro (Aug 09 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156239):
I recall in one instance I defined a `sorry'` axiom just to avoid the loud warnings

#### [ Sean Leather (Aug 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156284):
Personally, I'd rather be free of `sorry` warnings. But I understand that others may have different opinions, so, as a compromise, I propose that we make `master` free of `sorry`s and allow them in non-`master` branches.

#### [ Sean Leather (Aug 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156291):
```quote
I recall in one instance I defined a `sorry'` axiom just to avoid the loud warnings
```
That seems like a reasonable compromise, too.

#### [ Simon Hudon (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156302):
i find `sorry'` to be a terrifying option

#### [ Mario Carneiro (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156303):
Unfortunately it's a bit *too* quiet

#### [ Sean Leather (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156308):
It's like `sorry` with a tear. :cry:

#### [ Simon Hudon (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156309):
Also, I'd like to minimize the number of branches so that it can be useful as a library

#### [ Mario Carneiro (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156350):
what about `sorry'` being a notation for a tactic that uses an axiom and also prints "using sorry"

#### [ Sean Leather (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156352):
```quote
what about `sorry'` being a notation for a tactic that uses an axiom and also prints "using sorry"
```
Interesting...

#### [ Simon Hudon (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156368):
Isn't that just as loud as `sorry`?

#### [ Mario Carneiro (Aug 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156376):
no downstream warnings this way

#### [ Simon Hudon (Aug 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156429):
I see. That's a better option. I think I still prefer having master be sorry-free and the rest be fully sorry

#### [ Simon Hudon (Aug 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156430):
or sorry allowed. Also called Canadian.

#### [ Sean Leather (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156435):
Eh?

#### [ Simon Hudon (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156443):
(there was no moose)

#### [ Mario Carneiro (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156444):
I think I would rather have different projects on different folders of the same branch, because it is much easier to browse

#### [ Mario Carneiro (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156493):
and each project will have their own style of maintenance, which may or may not include sorry stuff

#### [ Simon Hudon (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156494):
I agree. I would just put temporary versions in branches until the sorries are substituted

#### [ Sean Leather (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156499):
So, let's see the desires here:

* Minimize `sorry`s
* Minimize number of branches
* Prefer directories over branches

#### [ Mario Carneiro (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156506):
That may never happen though - I'm thinking of projects with *really* long term undefined assumptions

#### [ Sean Leather (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156507):
I agree with all of those, but the `sorry` is the one that can affect others the most.

#### [ Mario Carneiro (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156514):
like Kevin's top-down formalization projects

#### [ Sean Leather (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156562):
```quote
I would just put temporary versions in branches until the sorries are substituted
```

Yes, that's what I'm thinking.

#### [ Mario Carneiro (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156565):
it is utterly unreasonable to just say "no getting in here until you're done"

#### [ Sean Leather (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156578):
But “unfinished” is not the same as “no `sorry`s.”

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156587):
In a top-down formalization, it is often impossible to have one without the other

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156589):
unless you use a hack that is equivalent to `sorry`

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156592):
and I don't want to encourage that

#### [ Simon Hudon (Aug 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156648):
I must say I'm on the fence

#### [ Sean Leather (Aug 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156657):
Not everything should go into mathlib-nursery.

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156668):
It's easy enough to create another repository for other projects.

#### [ Mario Carneiro (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156671):
Right

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156677):
I think mathlib-nursery should be for things that are intended for mathlib and shareable with others.

#### [ Simon Hudon (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156680):
What would you put in the nursery, @**Sean Leather** ?

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156681):
Things with `sorry` are not ready to be shared with others.

#### [ Sean Leather (Aug 09 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156721):
Kevin's `for_mathlib` stuff, for example.

#### [ Mario Carneiro (Aug 09 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156722):
I think `xena` would disagree with you on that point

#### [ Sean Leather (Aug 09 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156736):
```quote
I think `xena` would disagree with you on that point
```
I don't understand you.

#### [ Mario Carneiro (Aug 09 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156744):
I think the whole `lean-perfectoid-spaces` project is conceivably within scope for the nursery

#### [ Mario Carneiro (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156795):
it is a multiple person project with aspirations to be in mathlib someday, which depends on mathlib but is not properly a part of it right now

#### [ Johan Commelin (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156800):
```quote
```quote
I think `xena` would disagree with you on that point
```
I don't understand you.
```
Xena is one big repo where a dozen people are all working on different projects and using each others stuff. And half of the time it doesn't even build. People really don't care about a few sorries in there.

#### [ Mario Carneiro (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156801):
exactly

#### [ Mario Carneiro (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156806):
that's what I want to see in the nursery

#### [ Mario Carneiro (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156815):
except maybe for the "not building" part

#### [ Simon Hudon (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156819):
But we do want it to build at least most of the time, no?

#### [ Johan Commelin (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156822):
It is a nursery: toddlers beat each other up, steal each others toys, say `sorry`, and continue playing together.

#### [ Johan Commelin (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156826):
Says the guy who never went there, but has a house with 3 toddlers running around.

#### [ Johan Commelin (Aug 09 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156880):
Right, I suggest that mathlib-toddlers at least make sure that their stuff builds. After all, we're grown-ups.

#### [ Johan Commelin (Aug 09 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156889):
But even grown-ups should say `sorry` sometimes.

#### [ Johan Commelin (Aug 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156911):
Ok, so now comes the fun part!

#### [ Johan Commelin (Aug 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156913):
What is the punishment for pushing a commit that doesn't build?

#### [ Sean Leather (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156914):
Okay, other than Johan taking an analogy too far (:wink:), my idea of a mathlib-nursery is a place where projects that are working can be nursed into shape for mathlib.

#### [ Mario Carneiro (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156962):
You broke it, you fix it

#### [ Sean Leather (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156963):
So, first you start with your own repository, then you move bits and pieces into the nursery, then you PR to mathlib.

#### [ Johan Commelin (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156979):
But that is what the community fork is already doing...

#### [ Sean Leather (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156983):
Yes, that's for the PR part.

#### [ Mario Carneiro (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156988):
if a fix doesn't appear forthcoming, some annoyed third party may comment out your file

#### [ Johan Commelin (Aug 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157049):
Right. And if my witt vectors compile, but they take 15 seconds?

#### [ Johan Commelin (Aug 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157055):
Same treatment, I guess...

#### [ Kenny Lau (Aug 09 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157085):
```quote
if a fix doesn't appear *forth*coming, some annoyed *third* party may comment out your file
```
since it would take *seconds* to even compile the *first* line of their code

#### [ Simon Hudon (Aug 09 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157245):
I'm off to bed. I trust you guy will find a vision you agree on for the nursery

#### [ Sean Leather (Aug 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157327):
Optimism. :wink: Good night!

#### [ Simon Hudon (Aug 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157349):
What can I say? I'm monotonically increasing!

#### [ Simon Hudon (Aug 09 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157386):
Good day to you, sir!

#### [ Johan Commelin (Aug 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131161276):
Wait! What do you mean with `_` in "There should be no `sorry`s or  `_`."?
We debated the `sorry`s (and I still think they should be allowed). But what is this `_` being forbidden? That's used all over the place in mathlib. I think you mean a specific use of `_`, but I'm not sure which...

#### [ Mario Carneiro (Aug 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131161370):
I assume the kind of `_` that causes "could not synth placeholder" errors

#### [ Sean Leather (Aug 09 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131165577):
I just put that in the readme as a starting point. We can continue to debate everything. Nothing is set in stone.

#### [ Sean Leather (Aug 09 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131165604):
Yes, I meant unsolved goals. I'll change it, or someone else could rephrase it.

#### [ Sean Leather (Aug 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131167166):
I've hopefully improved on the wording.

#### [ Johan Commelin (Aug 18 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357821):
Does it make sense that if a PR from the community fork is merged that the person who merges (i.e. Mario or Johannes) also deletes the branch on the community fork?

#### [ Johan Commelin (Aug 18 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357836):
That keeps the list of branches clean, and it also helps to keep an overview of which branches you can/should work on.

#### [ Johan Commelin (Aug 18 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357838):
Or can we have incremental merges from branches on the community fork?

#### [ Johan Commelin (Aug 18 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357888):
For example, can/may I work on the `docs-theories` branched, after it is merged? Or should I start a `docs2` branch?

#### [ Mario Carneiro (Aug 18 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357924):
Once a branch has been merged, you should at least rebase / remove merged commits from the branch if you want to keep working on it, but there is no harm in retaining the branch name unless it is confusing to you

#### [ Mario Carneiro (Aug 18 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357972):
Or you could just add a merge commit to the new master and keep working

#### [ Johan Commelin (Aug 18 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357989):
Right, so if I missed the fact that the branch was merged into the official mathlib, then I mess up the repo...

#### [ Mario Carneiro (Aug 18 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358036):
well, the merge commit will probably clobber all the work on the branch anyway

#### [ Mario Carneiro (Aug 18 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358043):
and as long as I am squash merging it doesn't really matter how messy the branch gets

#### [ Mario Carneiro (Aug 18 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358064):
I would be fine with deleting branches after a merge (and github gives me a big button to do exactly that), but it is conceivable that I merge before they are really done

#### [ Mario Carneiro (Aug 18 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358113):
For example, I have seen Chris make a PR and then a few more commits come in the next day or two - if I merge those early, then Chris will be in a weird position, even moreso if I delete his branch

#### [ Mario Carneiro (Aug 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358177):
If I don't delete the branch (or even if I do, I guess), he can recreate the branch from his local copy, add some more commits, and PR again to post the new material

#### [ Johan Commelin (Aug 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358182):
Right. So in the end... it doesn't really matter, and I can happily push some commits?

#### [ Mario Carneiro (Aug 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358189):
yeah, basically

#### [ Johan Commelin (Aug 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358209):
Ok. That's good to know. I'll be offline again for a couple of days, and I still need to read up on the recent additions to the docs. But I hope to add some stuff later on.

#### [ Mario Carneiro (Aug 18 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358263):
and I will be traveling this weekend and in germany next week, not sure how much free time there will be


{% endraw %}
