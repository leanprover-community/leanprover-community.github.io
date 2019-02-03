---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21269publicPRs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [public PRs](https://leanprover-community.github.io/archive/113488general/21269publicPRs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Aug 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131008853):
<p>I'd like to introduce a slight change in PR management on mathlib. In order to support third party contribution to PRs, I would like to introduce "PR branches" to mathlib. The basic idea is, if there is a PR that is currently in review, for which you are not the author, and you would like to help get it into mathlib, just ask to have it made public on the PR page, and I will add it as a branch on the mathlib repo. This way, if a PR is stalled, you can get it back on track. I think this will make collaboration on WIPs easier, although it will probably confuse GitHub a bit, because of the way PR pages are set up. If you PR to a PR branch, make sure to reference the original PR # so that we can navigate between them through GitHub.</p>

#### [ Simon Hudon (Aug 07 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009168):
<p>Would it be useful to have a separate account for those WIP? That way you can have a stricter separation between the PRs. The added benefit is that you may promote more maintainers for that account</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009234):
<p>an interesting idea, I hadn't thought about having a public fork</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009364):
<p>You may or may not recall that mathlib was once <a href="https://github.com/leanprover/library_dev" target="_blank" title="https://github.com/leanprover/library_dev">https://github.com/leanprover/library_dev</a> . When we first moved from library_dev to mathlib, the idea was that library_dev might contain more experimental stuff or stuff that doesn't quite compile, but that never really happened</p>

#### [ Simon Hudon (Aug 07 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009435):
<p>I vaguely remember. I think a PR account might have to refrain from having a master branch. It would really be only a waiting room for big PRs</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009497):
<p>well, if it's a fork of mathlib then it will have a master branch, that is just tracking mathlib</p>

#### [ Simon Hudon (Aug 07 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009519):
<p>Yeah exactly. I would just refrain from merging anything into <code>master</code> that <code>leanprover/mathlib</code> doesn't have</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009698):
<p>I'm liking the idea so far. <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> What do you think about this? I can create a <code>lean-sandbox</code> user account, fork mathlib, and just give write access to anyone who wants it. People can still use the PR system on the sandbox account if they want, or create branches and PR them to mathlib.</p>

#### [ Simon Hudon (Aug 07 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009815):
<p>I recently created <code>https://github.com/leanprover-community/lean-mode-contrib</code> to host community contributions to <code>lean-mode</code>. It could double as a home for mathlib PRs</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009834):
<p>sounds good</p>

#### [ Mario Carneiro (Aug 07 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131009910):
<p>is <code>lean-mode-contrib</code> a fork of something?</p>

#### [ Simon Hudon (Aug 07 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131010064):
<p>Not quite. I thought I'd make it a mode that adds to <code>lean-mode</code>. I'm replicating some functionalities from <code>company-coq</code>. And now that the repo exists, I think I'll start adding some of my own scripts (like shortcuts for adding common libraries to your leanpkg.toml file).</p>

#### [ Simon Hudon (Aug 07 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131010110):
<p>Now that you ask, it might work if I just make it a fork of <code>lean-mode</code> with added features.</p>

#### [ Jeremy Avigad (Aug 07 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131011594):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> no objection here.</p>

#### [ Mario Carneiro (Aug 07 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131011651):
<p>Great! <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> What do you think about migrating <code>for_mathlib</code> to this new repo?</p>

#### [ Simon Hudon (Aug 07 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131012185):
<p>I suggest we choose a couple of maintainers for that repo. I already sent you and Johannes an invitation. I can send others.</p>

#### [ Mario Carneiro (Aug 07 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013207):
<p>I can be a maintainer, but I expect there won't be much maintaining going on</p>

#### [ Mario Carneiro (Aug 07 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013212):
<p>mostly it's just branch organization and such</p>

#### [ Mario Carneiro (Aug 07 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013268):
<p>Since the idea is to have it free for all, it's up to individuals to maintain their own branches as they see fit</p>

#### [ Mario Carneiro (Aug 07 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013282):
<p>I am inspired in part by metamath's "mathbox" infrastructure, although in that case the mathboxes are required to compile at all times but are otherwise organized at the discretion of the user</p>

#### [ Simon Hudon (Aug 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131013456):
<p>In principle, the maintainers will have to accept pull requests too. That's why I would err towards more maintainers rather than fewer. </p>
<p>I've never heard of the mathbox. Do you have a reference for it?</p>

#### [ Mario Carneiro (Aug 07 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131015487):
<p><a href="http://us.metamath.org/mpeuni/mmtheorems.html#19" target="_blank" title="http://us.metamath.org/mpeuni/mmtheorems.html#19">http://us.metamath.org/mpeuni/mmtheorems.html#19</a></p>

#### [ Kevin Buzzard (Aug 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030200):
<p>I don't really understand this proposal (that's not some implied criticism -- I just actually mean I don't understand it). I've just looked through the perfectoid <code>for_mathlib</code> directory and I see stuff I wrote and then forgot about, stuff which would be trivial to PR into mathlib, stuff which I half-wrote (quotient rings) and then someone else wrote better and which might already have been PR'ed -- after our discussion yesterday I'm wondering whether actually it might introduce some kind of order into the system if some of the really basic stuff like quotient additive groups and quotient rings should get into mathlib ASAP (indeed some of it might be there already). One thing I certainly don't want is for us to end up in the situation where people are relying on me to do things, as I already have far too much to do. As you know Mario I have started making tiny mathlib PRs, just dipping my toe in as it were; the stuff I put in "for_mathlib" myself is just stuff which I feel like it would be too much effort for me to PR into mathlib. On the other hand I'm coming round to the idea that perhaps  working from the bottom up is actually a good idea (rather than what we're currently doing, which is working top down, bottom up and in the middle all at once). </p>
<p>I think the problem I currently have with the mathlib set-up (which is I think why I started the "for-mathlib" directory) is the following. Let's say I realise I need 50 lines of code about e.g. topological groups, which is not in mathlib, but which would very naturally live in an existing mathlib file, e.g. <code>analysis/topology/topological_structures.lean</code>. The thing is, I want them <em>now</em>. I could either edit <code>topological_structure.lean</code> and make a PR, which would take me a long time because mathlib has conventions I don't know about or don't understand, and then there would be some to-ing and fro-ing whilst people told me that I've proved this lemma in a stupid way, and that lemma is just <code>by simp</code>, and that lemma is already there, and that lemma never uses inverses so it should really be in the topological monoid section -- and then I have to find time to edit everything etc etc to try and fix it up -- and this process can easily go on for weeks. During that time I find it really hard to actually access my own work, because it is "in limbo" -- it's not in mathlib and so it's not in my project. It's <em>much</em> easier just to write <code>for_mathlib/topological_structures.lean</code> and prove the lemmas I want, with their bad names and bad proofs and superfluous hypotheses, because then I can start using them immediately, because I'm not really interested in these lemmas anyway, I'm far more interested in doing the "meat" which is the perfectoid spaces, and in some sense I just want someone else to prove these basic facts about topological groups, someone who knows what they're doing and will do it right the first time. Unfortunately the set of such people is pretty small and they all have their own things that they're doing. I'm not motivated to PR, because of this. </p>
<p>Will the proposed system offer some sort of alternative approach which gets me out of this hole?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030222):
<blockquote>
<p>One thing I certainly don't want is for us to end up in the situation where people are relying on me to do things, as I already have far too much to do.</p>
</blockquote>
<p>The idea here is to allow other people to work on your PRs</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030404):
<blockquote>
<p>Let's say I realise I need 50 lines of code about e.g. topological groups, which is not in mathlib, but which would very naturally live in an existing mathlib file, e.g. analysis/topology/topological_structures.lean. The thing is, I want them <em>now</em>.</p>
</blockquote>
<p>I am fully aware of this situation, I often have to deal with it myself. The solution I came up with for this is to have a <code>pending</code> directory or file, which serves basically the same purpose as your <code>for_mathlib</code>. The difference is that I PR <em>first</em>, and then put something as close as possible to my PR into this pending area during the review period. That way, once the PR is accepted all I have to do is delete the relevant portion from the pending area.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030672):
<p>(mathlib used to have a <code>pending</code> directory, but I removed it since lean core no longer accepts PRs.)</p>

#### [ Kevin Buzzard (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030721):
<p>I see. So basically you're saying that I'm doing it wrong, and I am beginning to learn from my own experience that the "code now, PR later" approach has its disadvantages (e.g. I think that my partially written quotient ring code might be obsolete -- did Chris PR this? I still struggle with quotients; I have <code>a ≈ 0↔ ⟦a⟧ = ⟦0⟧ : by sorry</code> in my code at some point). I think it's far easier (for me at least) to understand other people when they say "do it my way not your way", once I've begun to realise the disadvantages of my way.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030722):
<p>Which is a pity. It would be awesome if they would accept one final PR that moved all of core into mathlib.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131030916):
<p>I'm not saying you have to PR everything as soon as it is written. But once you decide you have something you want to get into mathlib, it moves from where it currently is, probably some random file in your project, to the <code>for_mathlib</code> area and also into a PR, possibly [WIP]. Then you get feedback on your stuff, and if you make any updates to the PR you can either copy them to your local version or just leave the pending area out of date and update later (if you think it will affect your project I would recommend you update sooner rather than later).</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131031154):
<blockquote>
<p>I think it's far easier (for me at least) to understand other people when they say "do it my way not your way", once I've begun to realise the disadvantages of my way.</p>
</blockquote>
<p>I know I have a bad habit of asking people to "do it my way not your way", but I try to explain what the major issues are. The main problem is that making bad design decisions can be very expensive time-wise, without even alerting you to the possibility that the cost is avoidable. So when I hear that you've been struggling with an issue for several months and just working around it, my heart goes out to you and I wish I could have saved you from that.</p>

#### [ Johan Commelin (Aug 08 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088374):
<p>Is this public repo already available?</p>

#### [ Mario Carneiro (Aug 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088548):
<p>it is now <a href="https://github.com/leanprover-community/mathlib" target="_blank" title="https://github.com/leanprover-community/mathlib">https://github.com/leanprover-community/mathlib</a></p>

#### [ Johan Commelin (Aug 08 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088817):
<p>Ok, cool! And how would one create a new public PR branch on it?</p>

#### [ Johan Commelin (Aug 08 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088838):
<p>Should one ask for push access in this topic?</p>

#### [ Mario Carneiro (Aug 08 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131088859):
<p>yeah, that seems fine</p>

#### [ Mario Carneiro (Aug 08 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089133):
<p>okay I think I figured it out. You should now be a "collaborator" on leanprover-community/mathlib</p>

#### [ Mario Carneiro (Aug 08 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089305):
<p>I just sent invites to everybody who has ever been reasonably active on mathlib. If you didn't get one just ask</p>

#### [ Simon Hudon (Aug 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131089569):
<p>If you want to use leanprover-community/mathlib to create a PR, I propose you start by creating a branch from leanprover/master. Do not commit to leanprover-community/master directly, that branch is only meant to track leanprover/master.</p>

#### [ Patrick Massot (Aug 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100321):
<p>Let me check I understand correctly what I'm meant to do. I close my current norm PR. Push my norm branch to this new repository, open a new PR from there, right?</p>

#### [ Scott Morrison (Aug 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100390):
<p>Yes, that's about right!</p>

#### [ Sean Leather (Aug 08 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100889):
<p>The <a href="https://github.com/leanprover-community/mathlib" target="_blank" title="https://github.com/leanprover-community/mathlib">shared mathlib fork</a> doesn't seem to add much benefit over any other mathlib fork. You could easily use your own. It really is just a bit more convenient is that it has an established “trusted” set of collaborators, so that anyone in that group can contribute to anyone else's work. But if you want to work with only a different set of collaborators, you can also set up your own fork. But it's also a bit more questionable in that there's no clear policy for who does what with what branches, which can cause problems if people have different assumptions or don't communicate changes to each other.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131100915):
<p>Clearly it assumes quite a bit a trust, but let's see how it goes (I'm pretty optimistic here).</p>

#### [ Sean Leather (Aug 08 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101252):
<p>I think I'd do this differently. Instead of a mathlib fork, I'd suggest a sort of mathlib nursery, which is a library that has mathlib as a dependency. The collaborators would be set up as they are now, but the library source would be initially empty and added to by anyone on the <code>master</code> branch. Then, everybody moves WIP stuff into the mathlib-nursery. Once somebody's happy with part of their work, they can get feedback from others and somebody can PR that to mathlib. When the PR makes it into mathlib, the mathlib dependency commit is updated and the work is removed from mathlib-nursery.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101266):
<p>Too late, I opened <a href="https://github.com/leanprover/mathlib/pull/241" target="_blank" title="https://github.com/leanprover/mathlib/pull/241">https://github.com/leanprover/mathlib/pull/241</a> Let's see how this idea works out</p>

#### [ Sean Leather (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101268):
<p>The main difference is that everybody works on <code>mathlib-nursery/master</code> instead of multiple <code>mathlib</code> branches.</p>

#### [ Sean Leather (Aug 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101274):
<p>Actually, maybe mathlib-nursery and this mathlib fork can coexist and both be useful.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101316):
<p>The advantage of the current proposal is we don't have to move things into their final position</p>

#### [ Sean Leather (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101318):
<p>So, work starts in the nursery and then moves to the fork.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101323):
<p>And now Mario has to work on norms in order to prove his new workflow is useful <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Aug 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101325):
<p>The advantage of the nursery is that things can change and you don't need to worry about final positions. <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Patrick Massot (Aug 08 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101334):
<p>My experience is that the moving to final position phase is very boring and time consuming</p>

#### [ Sean Leather (Aug 08 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101343):
<blockquote>
<p>And now Mario has to work on norms in order to prove his new workflow is useful <span class="emoji emoji-1f609" title="wink">:wink:</span></p>
</blockquote>
<p>But the leanprover-community/mathlib doesn't add anything to what you're doing. You could always have allowed the mathlib collaborators access to your branch.</p>

#### [ Sean Leather (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101386):
<p>What it does allow is non-mathlib collaborators to work on your branch.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101399):
<p>Right, so <em>you</em> should work on that branch, mess it up and prove Mario was wrong.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101412):
<p>no, wait</p>

#### [ Sean Leather (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101418):
<p>Alternatively, if it was in a nursery, I could already be using it within the nursery. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101422):
<p>Say Kenny works on it</p>

#### [ Patrick Massot (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101428):
<p>or Chris, and prove Mario was right</p>

#### [ Kenny Lau (Aug 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101432):
<p>work on what</p>

#### [ Johan Commelin (Aug 08 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101480):
<p>You <em>should</em> do Patrick's homework <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Patrick Massot (Aug 08 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101481):
<p><a href="https://github.com/leanprover-community/mathlib/tree/norms" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/norms">https://github.com/leanprover-community/mathlib/tree/norms</a></p>

#### [ Patrick Massot (Aug 08 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101489):
<p>That's a new branch is the new mathlib fork where everyone from the community can improve on a PR</p>

#### [ Mario Carneiro (Aug 08 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131101944):
<p>The "nursery" idea is closer to the original purpose of <code>library_dev</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102033):
<p>Both options have their uses. I think the main factor is whether you want to work in a project that has a mathlib dependency, or in mathlib itself. For mathlib PRs of course the second option is better</p>

#### [ Mario Carneiro (Aug 08 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102114):
<p>For offshoot projects and experiments, a separate project is maybe nicer to work with, although you lose the ability to modify bits of mathlib to accomodate the work</p>

#### [ Sean Leather (Aug 08 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102193):
<blockquote>
<p>Both options have their uses. I think the main factor is whether you want to work in a project that has a mathlib dependency, or in mathlib itself. For mathlib PRs of course the second option is better</p>
</blockquote>
<p>Yeah, agreed. I think it would be nice to have a community-based nursery for stuff not ready for PR.</p>

#### [ Sean Leather (Aug 08 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102261):
<p>So, there could be a staged process:</p>
<p>1. throw it in the nursery, let other people use it or work on it<br>
2. when matured, create a community mathlib PR for it</p>

#### [ Sean Leather (Aug 08 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131102266):
<p>By definition, what's in the nursery is immature.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131107122):
<p>Whilst I have no understanding of the ins and outs of this new proposal, I think that there's a lot to be said for trying a random new thing and seeing how it turns out.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113284):
<p>OK so I want to try and get some of this <code>for_mathlib</code> stuff out of the perfetoid repo and into mathlib. I want to start with <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_submonoid.lean" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_submonoid.lean">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_submonoid.lean</a> that file, which is Johan Commelin literally translating <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean">https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean</a> into additive notation. There is also an <code>add_subgroup.lean</code> file which is the corresponding translation of <code>subgroup.lean</code>. Do I PR to mathlib? Do I push to mathlib-community?</p>

#### [ Kevin Buzzard (Aug 08 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113483):
<p>This is the other file I would like to get into mathlib: <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_subgroup.lean" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_subgroup.lean">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/add_subgroup.lean</a>, a translation of <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/subgroup.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/subgroup.lean">https://github.com/leanprover/mathlib/blob/master/group_theory/subgroup.lean</a> .</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113511):
<p>literal translation of files to additive notation is what <code>to_additive</code> is for</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113570):
<p>OK. So what do we do?</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113588):
<p>Because at the end of the day I want to quotient out an additive group by a subgroup and it's time to make progress.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113616):
<p>because what I really want is to quotient out a ring by an ideal and then borrow some properties from the group quotient.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113635):
<p>because what I really want is to prove some basic results about valuations, and I need ring quotients.</p>

#### [ Mario Carneiro (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113682):
<p>PR it</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113689):
<p>PR the two files I just linked to? To mathlib or the community one?</p>

#### [ Mario Carneiro (Aug 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113697):
<p>do it from the community fork if you think someone else is going to clean it up for you</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113736):
<p>What if I don't have a clue if someone else is going to clean it up for me and I don't know how to do it myself either?</p>

#### [ Mario Carneiro (Aug 08 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113748):
<p>then I will clean it up or it will languish</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113796):
<p>And should I then make the perfectoid repo depend on community mathlib instead of regular mathlib?</p>

#### [ Mario Carneiro (Aug 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113900):
<p>No, you should keep the stuff in <code>for_mathlib</code> and develop the PR independently</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131113904):
<p>I see. Thanks!</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114525):
<p>So after <code>git push --set-upstream origin additive-subgroup-theory</code> github thinks I'm about to submit a PR to mathlib. Is that what I am supposed to be doing?</p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114617):
<p>My <code>origin</code> is <code>    git@github.com:leanprover-community/mathlib.git </code></p>

#### [ Kevin Buzzard (Aug 08 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114640):
<p>i.e. is this just a regular PR to mathlib, but from the community fork rather than my own personal fork?</p>

#### [ Mario Carneiro (Aug 08 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131114646):
<p>yes</p>

#### [ Simon Hudon (Aug 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131134390):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I like the idea of a nursery. It makes it easier to get features used faster. The only downside is that you can't adapt any existing features of mathlib. I wonder if it might grow into a huge mess. Maybe we can still try to keep it clean.</p>

#### [ Simon Hudon (Aug 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131134398):
<p>I'm tempted in creating that nursery. Any objections?</p>

#### [ Sean Leather (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155297):
<blockquote>
<p>I'm tempted in creating that nursery. Any objections?</p>
</blockquote>
<p>Go for it. I'll share the responsibility for keeping it clean. If you don't get around to it, I will create it.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155306):
<p>I'm on board</p>

#### [ Simon Hudon (Aug 09 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155535):
<p>Done! You two should have received an invitation. And I think we can include move people still</p>

#### [ Sean Leather (Aug 09 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155610):
<p>Got it. Are you going to initialize it with a <code>README.md</code>?</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155646):
<p>You could initialize it with the content of <code>library_dev</code></p>

#### [ Sean Leather (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155765):
<p>One minimal requirement that I would have and would state on the <code>README.md</code> is that the code should build successfully for a given commit of mathlib and Lean version and not have any <code>sorry</code>s. I don't think it's an issue if the code changes significantly over time, but it's a pain for others if it doesn't build.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155820):
<p>I think that is too strict a requirement. Perhaps it should build but <code>sorry</code> is allowed?</p>

#### [ Sean Leather (Aug 09 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155828):
<p>The problem is that <code>sorry</code>s infect downstream code and clutter the error and warning messages.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155836):
<p>Mathlib already has that requirement, and I know it stops me from publishing stuff early because I think the work is not done yet</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155840):
<p>but for something that brands itself as a "nursery", it should explicitly accept unfinished work</p>

#### [ Sean Leather (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155845):
<p>Would it resolve your concern if you're allowed to use non-<code>master</code> branches for that code?</p>

#### [ Sean Leather (Aug 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155887):
<p>You still have to accept that the library is shared and not private.</p>

#### [ Simon Hudon (Aug 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155890):
<p>Here it is: <a href="https://github.com/leanprover-community/mathlib-nursery" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery">https://github.com/leanprover-community/mathlib-nursery</a></p>

#### [ Sean Leather (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155897):
<p>So I think it's appropriate to ask collaborators to minimize the burden.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155904):
<p>"The features are available a library in the meantime." typo in the README</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155905):
<p>A <code>sorry</code> in the middle of the code doesn't hurt anyone, and it is still being checked for correctness</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155906):
<p>I would rather just filter out sorry warnings</p>

#### [ Johan Commelin (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155910):
<p>But I don't think it is too much trouble to do <em>everything</em> in non-master branches, right?</p>

#### [ Simon Hudon (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155952):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> It is work in progress, I'll get it right eventually ;-)</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155960):
<p>Well, the nursery is different since it's not tracking mathlib</p>

#### [ Johan Commelin (Aug 09 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155962):
<p>If you make me a collaborator, you could delegate that (-;</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155963):
<p>it needs a master branch, and everyone should be not too far away from it</p>

#### [ Johan Commelin (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155968):
<p>Hmmm. I don't understand nurseries.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155973):
<p>(Never went to one as a toddler.)</p>

#### [ Sean Leather (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155976):
<blockquote>
<p>A <code>sorry</code> in the middle of the code doesn't hurt anyone, and it is still being checked for correctness</p>
</blockquote>
<p>I disagree. It adds overhead in terms of messages.</p>
<blockquote>
<p>I would rather just filter out sorry warnings</p>
</blockquote>
<p>How?</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155978):
<p>awk script?</p>

#### [ Sean Leather (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155979):
<p>Also, I'd like to see my own <code>sorry</code> messages and not those of others</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131155983):
<p>then don't compile or depend on others</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156028):
<p>we can have the travis build just ignore sorries</p>

#### [ Sean Leather (Aug 09 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156029):
<blockquote>
<p>Well, the nursery is different since it's not tracking mathlib</p>
</blockquote>
<p>But it is, isn't it? <a href="https://github.com/leanprover-community/mathlib-nursery/blob/master/leanpkg.toml#L8" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery/blob/master/leanpkg.toml#L8">https://github.com/leanprover-community/mathlib-nursery/blob/master/leanpkg.toml#L8</a></p>

#### [ Sean Leather (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156039):
<p>I'd really rather not have <code>sorry</code>s in the first place. I don't think that's too strong a requirement.</p>

#### [ Simon Hudon (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156040):
<p>It depends on mathlib but does not track it</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156041):
<p>I mean in the git sense - it's not a fork</p>

#### [ Sean Leather (Aug 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156049):
<p>Well, forks also don't track in any sense that I can think of. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Mario Carneiro (Aug 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156102):
<p>I can tell you for sure that there are people who work with sorries for long periods, on projects that would be appropriate for this nursery</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156104):
<p>and this was also how <code>library_dev</code> worked</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156160):
<p>Even in mathlib it feels like too strong a requirement sometimes. It's just that lean has a completely stupid reporting mechanism for sorry</p>

#### [ Sean Leather (Aug 09 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156172):
<p>The downstream warnings are definitely too much.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156224):
<p>they make sense in server mode but not in <code>lean --make</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156239):
<p>I recall in one instance I defined a <code>sorry'</code> axiom just to avoid the loud warnings</p>

#### [ Sean Leather (Aug 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156284):
<p>Personally, I'd rather be free of <code>sorry</code> warnings. But I understand that others may have different opinions, so, as a compromise, I propose that we make <code>master</code> free of <code>sorry</code>s and allow them in non-<code>master</code> branches.</p>

#### [ Sean Leather (Aug 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156291):
<blockquote>
<p>I recall in one instance I defined a <code>sorry'</code> axiom just to avoid the loud warnings</p>
</blockquote>
<p>That seems like a reasonable compromise, too.</p>

#### [ Simon Hudon (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156302):
<p>i find <code>sorry'</code> to be a terrifying option</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156303):
<p>Unfortunately it's a bit <em>too</em> quiet</p>

#### [ Sean Leather (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156308):
<p>It's like <code>sorry</code> with a tear. <span class="emoji emoji-1f622" title="cry">:cry:</span></p>

#### [ Simon Hudon (Aug 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156309):
<p>Also, I'd like to minimize the number of branches so that it can be useful as a library</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156350):
<p>what about <code>sorry'</code> being a notation for a tactic that uses an axiom and also prints "using sorry"</p>

#### [ Sean Leather (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156352):
<blockquote>
<p>what about <code>sorry'</code> being a notation for a tactic that uses an axiom and also prints "using sorry"</p>
</blockquote>
<p>Interesting...</p>

#### [ Simon Hudon (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156368):
<p>Isn't that just as loud as <code>sorry</code>?</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156376):
<p>no downstream warnings this way</p>

#### [ Simon Hudon (Aug 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156429):
<p>I see. That's a better option. I think I still prefer having master be sorry-free and the rest be fully sorry</p>

#### [ Simon Hudon (Aug 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156430):
<p>or sorry allowed. Also called Canadian.</p>

#### [ Sean Leather (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156435):
<p>Eh?</p>

#### [ Simon Hudon (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156443):
<p>(there was no moose)</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156444):
<p>I think I would rather have different projects on different folders of the same branch, because it is much easier to browse</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156493):
<p>and each project will have their own style of maintenance, which may or may not include sorry stuff</p>

#### [ Simon Hudon (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156494):
<p>I agree. I would just put temporary versions in branches until the sorries are substituted</p>

#### [ Sean Leather (Aug 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156499):
<p>So, let's see the desires here:</p>
<ul>
<li>Minimize <code>sorry</code>s</li>
<li>Minimize number of branches</li>
<li>Prefer directories over branches</li>
</ul>

#### [ Mario Carneiro (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156506):
<p>That may never happen though - I'm thinking of projects with <em>really</em> long term undefined assumptions</p>

#### [ Sean Leather (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156507):
<p>I agree with all of those, but the <code>sorry</code> is the one that can affect others the most.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156514):
<p>like Kevin's top-down formalization projects</p>

#### [ Sean Leather (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156562):
<blockquote>
<p>I would just put temporary versions in branches until the sorries are substituted</p>
</blockquote>
<p>Yes, that's what I'm thinking.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156565):
<p>it is utterly unreasonable to just say "no getting in here until you're done"</p>

#### [ Sean Leather (Aug 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156578):
<p>But “unfinished” is not the same as “no <code>sorry</code>s.”</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156587):
<p>In a top-down formalization, it is often impossible to have one without the other</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156589):
<p>unless you use a hack that is equivalent to <code>sorry</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156592):
<p>and I don't want to encourage that</p>

#### [ Simon Hudon (Aug 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156648):
<p>I must say I'm on the fence</p>

#### [ Sean Leather (Aug 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156657):
<p>Not everything should go into mathlib-nursery.</p>

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156668):
<p>It's easy enough to create another repository for other projects.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156671):
<p>Right</p>

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156677):
<p>I think mathlib-nursery should be for things that are intended for mathlib and shareable with others.</p>

#### [ Simon Hudon (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156680):
<p>What would you put in the nursery, <span class="user-mention" data-user-id="110045">@Sean Leather</span> ?</p>

#### [ Sean Leather (Aug 09 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156681):
<p>Things with <code>sorry</code> are not ready to be shared with others.</p>

#### [ Sean Leather (Aug 09 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156721):
<p>Kevin's <code>for_mathlib</code> stuff, for example.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156722):
<p>I think <code>xena</code> would disagree with you on that point</p>

#### [ Sean Leather (Aug 09 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156736):
<blockquote>
<p>I think <code>xena</code> would disagree with you on that point</p>
</blockquote>
<p>I don't understand you.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156744):
<p>I think the whole <code>lean-perfectoid-spaces</code> project is conceivably within scope for the nursery</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156795):
<p>it is a multiple person project with aspirations to be in mathlib someday, which depends on mathlib but is not properly a part of it right now</p>

#### [ Johan Commelin (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156800):
<blockquote>
<blockquote>
<p>I think <code>xena</code> would disagree with you on that point</p>
</blockquote>
<p>I don't understand you.</p>
</blockquote>
<p>Xena is one big repo where a dozen people are all working on different projects and using each others stuff. And half of the time it doesn't even build. People really don't care about a few sorries in there.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156801):
<p>exactly</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156806):
<p>that's what I want to see in the nursery</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156815):
<p>except maybe for the "not building" part</p>

#### [ Simon Hudon (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156819):
<p>But we do want it to build at least most of the time, no?</p>

#### [ Johan Commelin (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156822):
<p>It is a nursery: toddlers beat each other up, steal each others toys, say <code>sorry</code>, and continue playing together.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156826):
<p>Says the guy who never went there, but has a house with 3 toddlers running around.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156880):
<p>Right, I suggest that mathlib-toddlers at least make sure that their stuff builds. After all, we're grown-ups.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156889):
<p>But even grown-ups should say <code>sorry</code> sometimes.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156911):
<p>Ok, so now comes the fun part!</p>

#### [ Johan Commelin (Aug 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156913):
<p>What is the punishment for pushing a commit that doesn't build?</p>

#### [ Sean Leather (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156914):
<p>Okay, other than Johan taking an analogy too far (<span class="emoji emoji-1f609" title="wink">:wink:</span>), my idea of a mathlib-nursery is a place where projects that are working can be nursed into shape for mathlib.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156962):
<p>You broke it, you fix it</p>

#### [ Sean Leather (Aug 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156963):
<p>So, first you start with your own repository, then you move bits and pieces into the nursery, then you PR to mathlib.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156979):
<p>But that is what the community fork is already doing...</p>

#### [ Sean Leather (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156983):
<p>Yes, that's for the PR part.</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131156988):
<p>if a fix doesn't appear forthcoming, some annoyed third party may comment out your file</p>

#### [ Johan Commelin (Aug 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157049):
<p>Right. And if my witt vectors compile, but they take 15 seconds?</p>

#### [ Johan Commelin (Aug 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157055):
<p>Same treatment, I guess...</p>

#### [ Kenny Lau (Aug 09 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157085):
<blockquote>
<p>if a fix doesn't appear <em>forth</em>coming, some annoyed <em>third</em> party may comment out your file</p>
</blockquote>
<p>since it would take <em>seconds</em> to even compile the <em>first</em> line of their code</p>

#### [ Simon Hudon (Aug 09 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157245):
<p>I'm off to bed. I trust you guy will find a vision you agree on for the nursery</p>

#### [ Sean Leather (Aug 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157327):
<p>Optimism. <span class="emoji emoji-1f609" title="wink">:wink:</span> Good night!</p>

#### [ Simon Hudon (Aug 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157349):
<p>What can I say? I'm monotonically increasing!</p>

#### [ Simon Hudon (Aug 09 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131157386):
<p>Good day to you, sir!</p>

#### [ Johan Commelin (Aug 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131161276):
<p>Wait! What do you mean with <code>_</code> in "There should be no <code>sorry</code>s or  <code>_</code>."?<br>
We debated the <code>sorry</code>s (and I still think they should be allowed). But what is this <code>_</code> being forbidden? That's used all over the place in mathlib. I think you mean a specific use of <code>_</code>, but I'm not sure which...</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131161370):
<p>I assume the kind of <code>_</code> that causes "could not synth placeholder" errors</p>

#### [ Sean Leather (Aug 09 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131165577):
<p>I just put that in the readme as a starting point. We can continue to debate everything. Nothing is set in stone.</p>

#### [ Sean Leather (Aug 09 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131165604):
<p>Yes, I meant unsolved goals. I'll change it, or someone else could rephrase it.</p>

#### [ Sean Leather (Aug 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/131167166):
<p>I've hopefully improved on the wording.</p>

#### [ Johan Commelin (Aug 18 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357821):
<p>Does it make sense that if a PR from the community fork is merged that the person who merges (i.e. Mario or Johannes) also deletes the branch on the community fork?</p>

#### [ Johan Commelin (Aug 18 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357836):
<p>That keeps the list of branches clean, and it also helps to keep an overview of which branches you can/should work on.</p>

#### [ Johan Commelin (Aug 18 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357838):
<p>Or can we have incremental merges from branches on the community fork?</p>

#### [ Johan Commelin (Aug 18 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357888):
<p>For example, can/may I work on the <code>docs-theories</code> branched, after it is merged? Or should I start a <code>docs2</code> branch?</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357924):
<p>Once a branch has been merged, you should at least rebase / remove merged commits from the branch if you want to keep working on it, but there is no harm in retaining the branch name unless it is confusing to you</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357972):
<p>Or you could just add a merge commit to the new master and keep working</p>

#### [ Johan Commelin (Aug 18 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132357989):
<p>Right, so if I missed the fact that the branch was merged into the official mathlib, then I mess up the repo...</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358036):
<p>well, the merge commit will probably clobber all the work on the branch anyway</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358043):
<p>and as long as I am squash merging it doesn't really matter how messy the branch gets</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358064):
<p>I would be fine with deleting branches after a merge (and github gives me a big button to do exactly that), but it is conceivable that I merge before they are really done</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358113):
<p>For example, I have seen Chris make a PR and then a few more commits come in the next day or two - if I merge those early, then Chris will be in a weird position, even moreso if I delete his branch</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358177):
<p>If I don't delete the branch (or even if I do, I guess), he can recreate the branch from his local copy, add some more commits, and PR again to post the new material</p>

#### [ Johan Commelin (Aug 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358182):
<p>Right. So in the end... it doesn't really matter, and I can happily push some commits?</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358189):
<p>yeah, basically</p>

#### [ Johan Commelin (Aug 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358209):
<p>Ok. That's good to know. I'll be offline again for a couple of days, and I still need to read up on the recent additions to the docs. But I hope to add some stuff later on.</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/public%20PRs/near/132358263):
<p>and I will be traveling this weekend and in germany next week, not sure how much free time there will be</p>


{% endraw %}
