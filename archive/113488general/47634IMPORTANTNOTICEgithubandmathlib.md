---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47634IMPORTANTNOTICEgithubandmathlib.html
---

## Stream: [general](index.html)
### Topic: [IMPORTANT NOTICE: github and mathlib](47634IMPORTANTNOTICEgithubandmathlib.html)

---


{% raw %}
#### [ Simon Hudon (Jan 30 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157229265):
<p>We are in the process of moving <code>mathlib</code> from <code>leanprover</code> to <code>leanprover-community</code>. We will be inviting all the current contributors of <code>mathlib</code> to this new location but only the current maintainers will have write access to the master branch. All other branches will be available to write to. Please look at you inboxes for an invitation (if you currently have access to <code>leanprover-community/mathlib</code>) and update your <code>leanpkg.toml</code> files to point to <code>leanprover-community/mathlib</code> instead of <code>leanprover/mathlib</code>.</p>

#### [ Kenny Lau (Jan 30 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157229437):
<p>What happened?</p>

#### [ Simon Hudon (Jan 30 2019 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157229835):
<p><code>github.com/leanprover</code> and specifically <code>github.com/leanprover/mathlib</code> are owned by Leo and we decided to to move it <code>github.com/leanprover-community</code> so that we can manage the access rights without bothering Leo every time</p>

#### [ Simon Hudon (Jan 30 2019 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157229920):
<p>Edit: you only need to update <code>leanpkg.toml</code> for your packages that import <code>mathlib</code></p>

#### [ Kenny Lau (Jan 30 2019 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230474):
<p>who are "we"?</p>

#### [ Mario Carneiro (Jan 30 2019 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230768):
<p>We've been discussing this in the super secret maintainers club</p>

#### [ Kenny Lau (Jan 30 2019 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230814):
<p>I see</p>

#### [ Mario Carneiro (Jan 30 2019 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230852):
<p>Leo thinks it would be better to move mathlib away from the leanprover organization, and I think it would be better for him and us</p>

#### [ Mario Carneiro (Jan 30 2019 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230891):
<p>Note: the moves have not happened yet, so it's probably a bit early to change your toml files</p>

#### [ Simon Hudon (Jan 30 2019 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230955):
<p>We're in touch with Leo and github trying to make it happen. It should happen any minute now.</p>

#### [ Mario Carneiro (Jan 30 2019 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157230972):
<p>also the important part has to be initiated by leo so it depends on how on the ball he is</p>

#### [ Simon Hudon (Jan 31 2019 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157231111):
<p>Right now we're waiting on the github team actually. Leo responded very quickly.</p>

#### [ Bryan Gin-ge Chen (Jan 31 2019 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157235153):
<p>Might be good to add some instructions to the <code>README</code> on this after it drops.</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157235807):
<p>Actually, we just discovered that github automatically redirects for moved repositories, so I think we should do nothing re: marking the move</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157235818):
<p>My guess is all your remotes will continue to work as normal after the move</p>

#### [ Simon Hudon (Jan 31 2019 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236208):
<p>That's correct.</p>

#### [ Simon Hudon (Jan 31 2019 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236459):
<p>Leo now completed his side of the operation but we faced more obstacles than expected. Here is the current state of affair:</p>
<ul>
<li>what used to be <code>leanprover/mathlib</code> is now <code>leanprover-community/mathlib-2</code></li>
<li>what used to be <code>leanprover-community/mathlib</code> is now <code>leanprover-fork/mathlib-backup</code></li>
</ul>
<p>Their previous URL also work still. In particular, all the branches that used to be at <code>leanprover-community/mathlib</code> are now at <code>leanprover-fork/mathlib-backup</code>. We will keep using them until they are all merged or deleted. All new branches should be created on <code>leanprover-community/mathlib-2</code> which will now be the source of all truth. Only maintainers will be allowed to push to <code>leanprover-community/mathlib-2/master</code> however.</p>

#### [ Simon Hudon (Jan 31 2019 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236487):
<p>If you used to have write access to <code>leanprover-community/mathlib</code>, you should have received an invitation to contribute to <code>leanprover-community/mathlib-2</code>.</p>

#### [ Simon Hudon (Jan 31 2019 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236488):
<p>Any questions?</p>

#### [ Bryan Gin-ge Chen (Jan 31 2019 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236555):
<p>Is <code>mathlib-2</code> the "official" name going forward?</p>

#### [ Simon Hudon (Jan 31 2019 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236647):
<p>I'm hoping that it won't be. I asked Leo to rename it to <code>mathlib-2</code> because github refused the transfer when it was called <code>mathlib</code>. Now that it's called <code>mathlib-2</code>, Leo doesn't have anything else to do to help us with the transfer. I'm getting in touch with the github team to allow us to replace what used to be <code>leanprover-community/mathlib</code>.</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236891):
<p>did the rename to <code>leanprover-community/mathlib-backup</code> not work?</p>

#### [ Simon Hudon (Jan 31 2019 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157236936):
<p>It worked but left behind a redirect which I couldn’t overwrite</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237005):
<p>I mean where did the <code>lp-fork</code> user come from?</p>

#### [ Simon Hudon (Jan 31 2019 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237122):
<p>I created it just for this occasion. I’ll delete it when we’re done with this repo</p>

#### [ Simon Hudon (Jan 31 2019 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237210):
<p>Update: I just renamed <code>leanprover-community/mathlib-2</code> to <code>leanprover-community/mathlib</code>. I think the name was only blocked to transfers.</p>

#### [ Simon Hudon (Jan 31 2019 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237294):
<p>Now, <code>leanprover/mathlib</code> and <code>leanprover-community/mathlib</code> both point to the same repo.</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237309):
<p>I see the branch protection for master has CI status checks enabled. I think this is not a good idea, since it takes 45 minutes to run the CI, it's going to really throttle our ability to push stuff</p>

#### [ Mario Carneiro (Jan 31 2019 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157237346):
<p>at least, I think we need to see if this is going to cause a problem</p>

#### [ Simon Hudon (Jan 31 2019 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157238452):
<p>I see. We could have a branch “stable” which we make sure always builds this way. How about that?</p>

#### [ Reid Barton (Jan 31 2019 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157238987):
<p>Or we could call it "lean-3.4.2“</p>

#### [ Simon Hudon (Jan 31 2019 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157239050):
<p>I like it</p>

#### [ Simon Hudon (Jan 31 2019 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157239283):
<p>We could also make <code>lean-3.4.2</code> into a tag which travis pushes when a build on master succeeds</p>

#### [ Bryan Gin-ge Chen (Jan 31 2019 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157239410):
<p>that will fix the leanpkg issues, right?</p>

#### [ Simon Hudon (Jan 31 2019 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157239526):
<p>which one do you mean?</p>

#### [ Bryan Gin-ge Chen (Jan 31 2019 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157240355):
<p>I seem to recall that <code>leanpkg upgrade</code> wouldn't update mathlib if I had <code>lean_version = "3.4.2"</code> in <code>leanpkg.toml</code>. I can try to check after another commit gets pushed to master. I've been using <code>"nightly"</code> in that option so it gives a warning, but then running <code>leanpkg upgrade</code> does keep mathlib up to date.</p>
<p>I thought there was also an issue with <code>leanpkg new</code> and <code>leanpkg add</code> but I can't seem to reproduce it now.</p>

#### [ Simon Hudon (Jan 31 2019 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157240578):
<p>I think it would fix the first one but I'm not sure about the second one</p>

#### [ Mario Carneiro (Jan 31 2019 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157242566):
<p>so the move is complete now?</p>

#### [ Simon Hudon (Jan 31 2019 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157242728):
<p>Mostly. We can already start working only with <code>leanprover-community/mathlib</code> and the only exception is the existing PRs that refer to <code>leanprover-fork/mathlib-backup</code>. Once we're done with those, I think the transfer will be complete.</p>

#### [ Simon Hudon (Jan 31 2019 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157242782):
<p>People can, at their leisure, move the branches that aren't part of PRs from <code>mathlib-backup</code> to <code>mathlib</code></p>

#### [ Mario Carneiro (Jan 31 2019 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157242956):
<p>does this help? <a href="https://help.github.com/articles/changing-the-base-branch-of-a-pull-request/" target="_blank" title="https://help.github.com/articles/changing-the-base-branch-of-a-pull-request/">https://help.github.com/articles/changing-the-base-branch-of-a-pull-request/</a></p>

#### [ Simon Hudon (Jan 31 2019 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157243134):
<p>No, the base is the branch located in <code>lp-community</code></p>

#### [ Kenny Lau (Jan 31 2019 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257052):
<p>why is <a href="https://travis-ci.org/leanprover-community/mathlib/jobs/486825650" target="_blank" title="https://travis-ci.org/leanprover-community/mathlib/jobs/486825650">my build</a> &gt; 15 mins? Is there some issue with the caching?</p>

#### [ Kenny Lau (Jan 31 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257124):
<p>Also is <a href="https://github.com/leanprover/mathlib/issues/658" target="_blank" title="https://github.com/leanprover/mathlib/issues/658">#658</a> working?</p>

#### [ Kenny Lau (Jan 31 2019 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257380):
<p>I think this is very confusing. Can someone loop me in as to the current status of affairs?</p>

#### [ Kenny Lau (Jan 31 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257436):
<p>before your moves I had a branch leanprover-community/mathlib/submodule-mul</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257467):
<p>AFAICT it's building</p>

#### [ Kenny Lau (Jan 31 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257485):
<p>and after your moves I tried pushing to that branch again from git</p>

#### [ Kenny Lau (Jan 31 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257501):
<p>and it automatically created a new branch instead of redirecting it to the fork branch</p>

#### [ Kenny Lau (Jan 31 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257535):
<p>and that is a problem because <a href="https://github.com/leanprover/mathlib/issues/658" target="_blank" title="https://github.com/leanprover/mathlib/issues/658">#658</a> listens on the fork branch</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257538):
<p>the new thing is to push your stuff to a branch on mathlib itself, which has the same name as the old community mathlib</p>

#### [ Kenny Lau (Jan 31 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257542):
<p>so I need to set up the new upstream manually</p>

#### [ Kenny Lau (Jan 31 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257568):
<p>but the pull requests listen on the fork branches...</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257651):
<p>I guess that's a grandfather thing... push to the fork for your old open PRs, create lc/mathlib branches in the future</p>

#### [ Kenny Lau (Jan 31 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257657):
<blockquote>
<p>AFAICT it's building</p>
</blockquote>
<p>yes, but I don't see any evidence of caching</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257683):
<p>who knows, I wouldn't worry about it unless it happens every time</p>

#### [ Kenny Lau (Jan 31 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257742):
<p>I think the caches on the old leanprover-community/mathlib haven't been moved to leanprover-fork/mathlib-backup</p>

#### [ Kenny Lau (Jan 31 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257747):
<p>that's why there are no caches there</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257753):
<p>it looks like it did download a cache, but we don't have a lot of diagnostic info on what cache data travis is using</p>

#### [ Kenny Lau (Jan 31 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257759):
<p>this is a bad sign as we have 25 open PR's, if each of them needs to be built once then we would lose a lot of time</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257782):
<p>only if they push new commits</p>

#### [ Kenny Lau (Jan 31 2019 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257806):
<p>also I get a strange "view <a href="https://github.com/leanprover/mathlib/issues/658" target="_blank" title="https://github.com/leanprover/mathlib/issues/658">#658</a>" button when I visit leanprover-community/mathlib/submodule-mul</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257843):
<p>it's not like we can do anything about it... the caches are very brittle. If they don't work, regenerate them. If <em>those</em> don't work we have a problem</p>

#### [ Kenny Lau (Jan 31 2019 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257852):
<p>does this suggest that somehow it is connected to the other branch?</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257863):
<p>it is the same commit</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257950):
<p>oh, <a href="https://travis-ci.org/leanprover/mathlib" target="_blank" title="https://travis-ci.org/leanprover/mathlib">https://travis-ci.org/leanprover/mathlib</a> is a 404</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257952):
<p>I guess travis can't handle the move as smoothly as github</p>

#### [ Mario Carneiro (Jan 31 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257960):
<p>could be related to the loss of cache</p>

#### [ Kenny Lau (Jan 31 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257965):
<p>yep</p>

#### [ Kenny Lau (Jan 31 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157257971):
<p>anyway can you review <a href="https://github.com/leanprover/mathlib/issues/658" target="_blank" title="https://github.com/leanprover/mathlib/issues/658">#658</a>? :P</p>

#### [ Johan Commelin (Jan 31 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157295186):
<p>I just learned that the "maintainers elected in Amsterdam now have commit rights". I'm very sorry for not having been able to attend this discussion in Amsterdam. Out of curiosity, is this list of maintainers documented somewhere?</p>

#### [ Patrick Massot (Jan 31 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157295242):
<p>mathlib readme</p>

#### [ Patrick Massot (Jan 31 2019 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157295324):
<p>I'm also sorry I missed that. I would have volunteered for documentation maintainership</p>

#### [ Patrick Massot (Jan 31 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157295777):
<p>Inspired by this successful change of ownership, we decided to redo properly the move of perfectoid spaces from Kevin's account to leanprover-community. So I pulled back all commits to the old repository and deleted the new one. Now I need someone with correct rights (<span class="user-mention" data-user-id="110026">@Simon Hudon</span> ?) to grant Kevin the right to create a repository in leanprover-community, so that he can transfer properly (with redirections, without loosing watchers and stars etc.)</p>

#### [ Johan Commelin (Jan 31 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157295976):
<blockquote>
<p>mathlib readme</p>
</blockquote>
<p>Aah, thanks. Hadn't seen that yet. So <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> isn't mentioned in that list, but he's the person doing almost all merges right now? <span aria-label="grinning" class="emoji emoji-1f600" role="img" title="grinning">:grinning:</span></p>

#### [ Simon Hudon (Jan 31 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157296913):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> is moving to the dark side of computer science: he's leaving academia to go work in a place called real world (never heard of it before). He still has rights but we won't be assigning him any work</p>

#### [ Simon Hudon (Jan 31 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157297139):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> : I just extended Kevin an invitation so that he can move his repo</p>

#### [ Johannes Hölzl (Jan 31 2019 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/IMPORTANT%20NOTICE%3A%20github%20and%20mathlib/near/157299175):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  is right, I don't think I will have time to work on mathlib in the future. I added the list of maintainers and deliberately put not myself on it.</p>


{% endraw %}
