---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73800HowshouldIPR.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [How should I PR?](https://leanprover-community.github.io/archive/113488general/73800HowshouldIPR.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133189632):
<p>I think I have been using the wrong method, so maybe I should unlearn what I have learnt. The main problem is that one never PR's a single independent file, i.e. often there are files in mathlib that need to be changed. How should I make sure that the changes will compile fine? Should I have another branch of mathlib locally?</p>

#### [ Kenny Lau (Sep 01 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133189753):
<p>I think the reason I haven't PR'd a long time is that I find that I need to modify other files and it's really inconvenient</p>

#### [ Simon Hudon (Sep 01 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133189853):
<p>I suggest you create a branch for your PR and you can even host it on <code>leanprover-community</code> if you like.</p>

#### [ Kenny Lau (Sep 01 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133189902):
<p>how would I do it on git?</p>

#### [ Simon Hudon (Sep 01 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133189970):
<p>First you checkout mathlib, then you create a branch for your changes, then you make your changes and commit them to that branch, then you add <code>leanprover-community/mathlib</code> as a remote and finally you push your changes to that remote.</p>

#### [ Kenny Lau (Sep 01 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190019):
<p>sounds complicated</p>

#### [ Simon Hudon (Sep 01 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190524):
<p>How do you currently do it?</p>

#### [ Kenny Lau (Sep 01 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190568):
<p>write an individual file, do a pull request on github breaking the file into several pieces, hope for the best</p>

#### [ Simon Hudon (Sep 01 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190768):
<p>Do you mean that you don't use git on your own computer?</p>

#### [ Kenny Lau (Sep 01 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190794):
<p>I do, just not with mathlib</p>

#### [ Simon Hudon (Sep 01 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133190900):
<p>So the first step is to work on mathlib with git. You checkout the library and then you can compile it on your own computer and check if your changes break anything.</p>

#### [ Kenny Lau (Sep 01 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133191169):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> what if I want to have two PR's at the same time?</p>

#### [ Simon Hudon (Sep 01 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133191212):
<p>If they are independent, on your own machine, you can create two separate branches and push them. VS code should provide a way to switch between branches. I only know that emacs does.</p>

#### [ Simon Hudon (Sep 01 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133191275):
<p>If they are not independent, again, you create two branches and then you have to be careful when updating the first one</p>

#### [ Kenny Lau (Sep 02 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133202814):
<p>nice, I added 3 lines to one file and now my local file takes forever to compile</p>

#### [ Simon Hudon (Sep 02 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133202874):
<p>Yeah, mathlib is pretty big</p>

#### [ Simon Hudon (Sep 02 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133202926):
<p>I recommend you don't compile all of it after each change and when you do compile, quit the compilation after the first error.</p>

#### [ Kenny Lau (Sep 02 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133202972):
<p>I mean, I can't even use my local file anymore</p>

#### [ Kenny Lau (Sep 02 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133202975):
<p>because it has to recompile the file I changed and its descendents</p>

#### [ Scott Morrison (Sep 02 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133203940):
<p>Are you using <code>leanpkg build</code> and/or <code>lean --make</code>? These will rebuild the olean files for you.</p>

#### [ Kenny Lau (Sep 02 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133204074):
<p>yes but this takes like half an hour</p>

#### [ Scott Morrison (Sep 02 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133206657):
<p>the alternative is to not do it, and have it take half an hour every time, rather than just once</p>

#### [ Kenny Lau (Sep 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133207134):
<p>yeah I figured</p>

#### [ Chris Hughes (Sep 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133208455):
<p>I tend to write my mathlib PR all in one file, and then only when it's finished do I move stuff into the right places.</p>

#### [ Kenny Lau (Sep 02 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133208693):
<p>that's what I used to do</p>

#### [ Patrick Massot (Sep 02 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210341):
<p>This is also an extremely painful workflow</p>

#### [ Patrick Massot (Sep 02 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210385):
<p>We really need to figure out a trick. I'm also editing mathlib at the moment and this issue builds a powerful psychological barrier</p>

#### [ Patrick Massot (Sep 02 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210392):
<p>Maybe we can have a lib duplicating only the part of mathlib we want to edit, but then it's hard to make sure we use the correct dependencies (without recreating the original issue of course)</p>

#### [ Kevin Buzzard (Sep 02 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210475):
<p>Some dumb questions from someone with no experience of managing code and with very few mathlib PR's under his belt: (1) Editing which kind of file causes this problem? A file which many other files depend on, or a file which few other files depend on? (2) If it's a file which many other files depend on, why not just not import them somehow, and work with a subset of mathlib which only contains dependencies for the file you're editing? Is this hard to do in practice? (3) If it's a file which few other files depend on, then why are there problems editing it? What is being re-compiled a lot?</p>

#### [ Patrick Massot (Sep 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210574):
<p>What we did for the perfectoid project (duplicate part of the directory and file hierarchy, then each file imports the corresponding mathlib files and adds things) almost works, but it's still difficult to put things in the correct location inside the file at the end. And, more importantly, when PRing things file by file, it's hard to stay synchronized. That last issue is probably much worse that it should have been, because we waited for so long before starting PRs.</p>

#### [ Patrick Massot (Sep 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210588):
<p>I actually don't know the answers to Kevin's question, that's part of the headache. I only see that suddenly everything takes forever</p>

#### [ Kevin Buzzard (Sep 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210594):
<p>Are you talking about the "for_mathlib" strategy?</p>

#### [ Patrick Massot (Sep 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210595):
<p>yes</p>

#### [ Patrick Massot (Sep 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210596):
<p>And then the string of PRs I opened on Tuesday and Wednesday</p>

#### [ Kevin Buzzard (Sep 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210597):
<p>I could see that Mario had some reservations about this, in the form "I see you have a bunch of stuff marked <code>for_mathlib</code> -- I hope it actually does end up in mathlib..."</p>

#### [ Patrick Massot (Sep 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210640):
<p>That directory lost many files in <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/pull/15" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/pull/15">https://github.com/kbuzzard/lean-perfectoid-spaces/pull/15</a></p>

#### [ Patrick Massot (Sep 02 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133210650):
<p>Actually only three files, but other got significantly reduced</p>

#### [ Kenny Lau (Sep 02 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133217834):
<p>Great, now Johannes made some edit suggestions and it would take <a href="https://travis-ci.org/leanprover/mathlib/builds/423595890?utm_source=github_status&amp;utm_medium=notification" target="_blank" title="https://travis-ci.org/leanprover/mathlib/builds/423595890?utm_source=github_status&amp;utm_medium=notification">an extra hour</a> to compile</p>

#### [ Mario Carneiro (Sep 02 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218002):
<p>travis is very slow, slower than anyone's machines. Last time I tried it took around 15 minutes to compile all of mathlib on my computer</p>

#### [ Mario Carneiro (Sep 02 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218013):
<p>but you don't really have to wait for travis, I don't even look at it until I'm about to merge, and you should only react when travis sends you an email saying something broke</p>

#### [ Johannes Hölzl (Sep 02 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218083):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  if you want I can also merge it and incorporate the changes myself.</p>

#### [ Kenny Lau (Sep 02 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218136):
<p>Please go ahead.</p>

#### [ Kenny Lau (Sep 02 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218206):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Oh and maybe make <code>⊗</code> and <code>⊗ₛ</code> into global infix</p>

#### [ Johannes Hölzl (Sep 02 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218366):
<p>I'm working on it. I  will also rebase the <code>tensor-product</code> branch.</p>

#### [ Kenny Lau (Sep 02 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218420):
<p>whatever that means</p>

#### [ Johannes Hölzl (Sep 02 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218436):
<p>It means that you shouldn't push to <code>tensor-product</code> as I might overwrite it when I rebase it...</p>

#### [ Kenny Lau (Sep 02 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218536):
<p>oh ok</p>

#### [ Johannes Hölzl (Sep 02 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218609):
<p>I pushed the rebased version and squashed them. So Github does remember that it was your original commit and PR. But the commit messages are in the style expected for mathlib.</p>

#### [ Johannes Hölzl (Sep 02 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218614):
<p>Now I can do my changes on top of it before merging it into mathlib.</p>

#### [ Kenny Lau (Sep 02 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133218786):
<p>that's very interesting... (pretending to understand)</p>

#### [ Kevin Buzzard (Sep 02 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133220077):
<p>How about we get Travis to compile .olean files for every OS and host a fully compiled mathlib with .olean files on GitHub?</p>

#### [ Mario Carneiro (Sep 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133220132):
<p>I don't know if we can get travis to compile .oleans for any system other than the one it's running</p>

#### [ Kevin Buzzard (Sep 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133220134):
<p>Would the potential problems with timestamps be solvable?</p>

#### [ Mario Carneiro (Sep 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133220135):
<p>you can always set timestamps</p>

#### [ Kevin Buzzard (Sep 02 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20should%20I%20PR%3F/near/133220186):
<p>Could it be a community project somehow? Mathlib gets updated, someone on Ubuntu 18.04 compiles it and shares the .olean files, then Ubuntu users can have that as a dependence instead of mathlib. Is it as easy as that? Or did Sebastian U say you couldn't even share .olean files between two different computers running the same OS?</p>


{% endraw %}
