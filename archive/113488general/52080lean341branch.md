---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52080lean341branch.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean-3.4.1 branch](https://leanprover-community.github.io/archive/113488general/52080lean341branch.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (May 25 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073781):
<p>I added a lean-3.4.1 branch to mathlib, which I think should fix the issues with elan/leanpkg (assuming I spelled everything correctly). <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Will there be any problem with just keeping the branch up to date with master (although I don't think branch symlinks are a thing)? I don't see any reason not to.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073806):
<p>Mario -- many thanks!</p>

#### [ Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073849):
<p>You did not keep the 3.3.0 branch up to date with mathlib master -- why do you want to keep the 3.4.1 branch up to date?</p>

#### [ Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073866):
<p>Why not just have a release version for 3.4.1?</p>

#### [ Mario Carneiro (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074034):
<p>because lean does not have nearly enough versions</p>

#### [ Mario Carneiro (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074040):
<p>mathlib does not develop on lean's schedule</p>

#### [ Mario Carneiro (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074044):
<p>and there is a huge range of commits that are compatible with 3.4.1</p>

#### [ Kevin Buzzard (May 25 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074083):
<p>I understand the argument.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074102):
<p>As I explained to you in email -- I would ideally like to be able to point people to a "3.4.1 release" version of mathlib which is "the canonical version of mathlib to run with the 3.4.1 release version of Lean"</p>

#### [ Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074106):
<p>And your argument is</p>

#### [ Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074110):
<p>that the canonical version is the latest version</p>

#### [ Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074113):
<p>right?</p>

#### [ Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074187):
<p>OTOH I am _forced_ to point certain people (the IT people here, the CoCalc people) to a canonical version of mathlib which goes with Lean 3.4.1 release, because both of these organisations refuse to work with moving targets</p>

#### [ Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074190):
<p>so I am going to tell them both to point to the very first commit in the 3.4.1 branch.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074194):
<p>I cannot envisage any problems with this, and it sounds like the best compromise.</p>

#### [ Mario Carneiro (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074201):
<p>You can point them to the latest version, and they can take that at any point</p>

#### [ Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074206):
<p>The problem with that idea</p>

#### [ Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074207):
<p>is that then it will be hard for people to work out exactly which version they are running</p>

#### [ Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074211):
<p>and it is very much in my interest that code runs on CoCalc if and only if it runs on the machines here</p>

#### [ Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074251):
<p>so I would very much like CoCalc and the machines here to be running exactly the same code</p>

#### [ Mario Carneiro (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074252):
<p>We have a lean-3.3.0 branch as well, which is not a tag but a branch because it incorporates new bugfixes and such which are compatible with 3.3.0</p>

#### [ Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074253):
<p>Oh -- so 3.3.0 moves?</p>

#### [ Patrick Massot (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074254):
<p>There nothing like "the very first commit in the 3.4.1 branch" in git</p>

#### [ Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074255):
<p>Oh!</p>

#### [ Mario Carneiro (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074256):
<p>not much, but yes</p>

#### [ Patrick Massot (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074259):
<p>You can tag a commit</p>

#### [ Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074261):
<p>Aah</p>

#### [ Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074262):
<p>Mario -- last question then</p>

#### [ Kevin Buzzard (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074272):
<p>can I persuade you to tag a commit?</p>

#### [ Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074273):
<p>But a branch is only some moving marker attached to some moving commit</p>

#### [ Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074288):
<p>What you want is Mario creating a release tag</p>

#### [ Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074292):
<p>not a branch</p>

#### [ Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074332):
<p>Thanks for clarifying Patrick.</p>

#### [ Mario Carneiro (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074333):
<p>mathlib doesn't do releases like that</p>

#### [ Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074341):
<p>Sorry that my poor understanding of git is just adding to the noise</p>

#### [ Patrick Massot (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074344):
<p>Kevin kindly asks to change this</p>

#### [ Mario Carneiro (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074347):
<p>if you want a commit, then it will be an artificial stopping point anyway, so just pick a point and write down the hash</p>

#### [ Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074348):
<p>I can do this</p>

#### [ Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074349):
<p>but it will look confusing</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074356):
<p>I am not asking for this for me</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074362):
<p>I am asking for this for other people</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074366):
<p>who want "Lean + Mathlib version 3.4.1"</p>

#### [ Mario Carneiro (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074369):
<p>That's what the branch is for</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074370):
<p>no</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074372):
<p>They want a canonical uniquely defined thing</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074374):
<p>not a moving target</p>

#### [ Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074379):
<p>because both refuse to move</p>

#### [ Kevin Buzzard (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074420):
<p>I will give them a hash</p>

#### [ Kevin Buzzard (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074434):
<p>It is not ideal, but it is the best solution if there is to be no release tag</p>

#### [ Kevin Buzzard (May 25 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074452):
<p>Thanks both of you for clarifying what I should be doing :-)</p>

#### [ Mario Carneiro (May 25 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074458):
<p>I think 78d28c5cb58f6a22fbb8fc940cc6f97bc0111602 is the last "update to lean" commit</p>

#### [ Mario Carneiro (May 25 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074505):
<p>but I don't know what leanpkg does with tags v branches, so I don't want to carelessly tag it</p>

#### [ Mario Carneiro (May 25 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074507):
<p>because I want leanpkg to find the branch</p>

#### [ Kevin Buzzard (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074512):
<p>If creating a tag causes problems for other people then clearly this is an argument against creating a tag</p>

#### [ Patrick Massot (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074517):
<p>I don't understand the potential problem here</p>

#### [ Patrick Massot (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074519):
<p>with a tagged release</p>

#### [ Johan Commelin (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074566):
<p>Just don't tag it with <code>lean-3.4.1</code></p>

#### [ Mario Carneiro (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074567):
<p>if you ask for elan to give you lean + mathlib 3.4.1, you should get the latest mathlib that is compatible with 3.4.1, which is master</p>

#### [ Johan Commelin (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074575):
<p>Right, Kevin, maybe you can trick them.</p>

#### [ Johan Commelin (May 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074581):
<p>You ask them to install elan, and use elan to install mathlib 3.4.1</p>

#### [ Johan Commelin (May 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074583):
<p>And they won't realise they just installed a moving target...</p>

#### [ Mario Carneiro (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074625):
<p>that's what travis did for a long time, and it worked pretty well</p>

#### [ Patrick Massot (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074628):
<blockquote>
<p>Just don't tag it with <code>lean-3.4.1</code></p>
</blockquote>
<p>Sure, the tag would need to be something like: spring2018</p>

#### [ Johan Commelin (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074631):
<p>Otoh, if users start complaining, you're in trouble anyway...</p>

#### [ Johan Commelin (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074641):
<p>Because they will say: hey, why is this stuff not in your mathlib...</p>

#### [ Mario Carneiro (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074648):
<p>I don't mind having mathlib versions (which would be different from lean versions), but I would like leanpkg to work with them if possible</p>

#### [ Johan Commelin (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074658):
<p>Right, so <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> can you make <code>elan</code> to listen to some tags as well?</p>

#### [ Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074660):
<p>We probably need to wait for <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> then</p>

#### [ Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074661):
<p>oops</p>

#### [ Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074664):
<p>We pinged him at the same time</p>

#### [ Patrick Massot (May 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074706):
<p>sorry about the harassment</p>

#### [ Johan Commelin (May 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074707):
<p>Urgent matters (-;</p>

#### [ Sebastian Ullrich (May 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075441):
<blockquote>
<p>Will there be any problem with just keeping the branch up to date with master (although I don't think branch symlinks are a thing)? I don't see any reason not to.</p>
</blockquote>
<p>Yes, I think it's either that or saying "Nobody should use nightlies right now anyway", setting <code>lean-3.4.1</code> as the default branch, and not updating or outright removing <code>master</code></p>

#### [ Mario Carneiro (May 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075447):
<p>I did set the mathlib dependency to lean-3.4.1 as well</p>

#### [ Sebastian Ullrich (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075502):
<p>Uh, where?</p>

#### [ Mario Carneiro (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075506):
<p>leanpkg.toml</p>

#### [ Mario Carneiro (May 25 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075511):
<p>lean_version = "3.4.1"</p>

#### [ Sebastian Ullrich (May 25 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075627):
<p>Ah, I see. Yeah, it's a bit weird to do that on the <code>master</code> branch since it means Lean nightly people using mathlib will get warnings, which is why I would slightly prefer the latter option I listed. But I guess it's okay either way.</p>

#### [ Mario Carneiro (May 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075662):
<p>I mean, right now there's no difference, and it seems like lean repo is frozen for the foreseeable future so I guess it's fine to officially run 3.4.1</p>

#### [ Patrick Massot (May 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075666):
<p>Is there any Lean nightly though?</p>

#### [ Mario Carneiro (May 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075706):
<p>if and when nightlies start back up again we can switch back</p>

#### [ Sebastian Ullrich (May 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075715):
<p>Yes, both ways should work fine</p>

#### [ Sebastian Ullrich (May 25 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075796):
<p>As Mario said, tag support would have to be added to <code>leanpkg</code>, unless we'd want <code>elan</code> to more or less reimplement and supersede the former. Which is possibly, and <a href="https://github.com/Kha/elan/issues/7" target="_blank" title="https://github.com/Kha/elan/issues/7">https://github.com/Kha/elan/issues/7</a> already points in that direction, but... not something I want to do right now</p>


{% endraw %}
