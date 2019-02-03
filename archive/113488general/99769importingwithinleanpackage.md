---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99769importingwithinleanpackage.html
---

## Stream: [general](index.html)
### Topic: [importing within lean package](99769importingwithinleanpackage.html)

---


{% raw %}
#### [ Chris Hughes (Mar 24 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161392):
<p>So I've tried to download <span class="user-mention" data-user-id="110064">@Kenny Lau</span> and <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>'s stacks project library, but none of the imports are currently working, I get the following message</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="kn">import</span><span class="o">:</span> <span class="n">Kenny_comm_alg</span><span class="bp">.</span><span class="n">avoid_powers</span>
<span class="n">could</span> <span class="n">not</span> <span class="n">resolve</span> <span class="kn">import</span><span class="o">:</span> <span class="n">Kenny_comm_alg</span><span class="bp">.</span><span class="n">avoid_powers</span>
</pre></div>


<p>I tried using both <code>leanpkg install</code> and <code>leanpkg add</code> to download the library, but both have this problem. I'm on windows. Can anyone help?</p>

#### [ Simon Hudon (Mar 24 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161439):
<p>did you do <code>leanpkg init my_project</code> on your directory?</p>

#### [ Chris Hughes (Mar 24 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161491):
<p>Which directory?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161548):
<p>Chris : try the "open folder" option in VS Code. Open the project root as a folder.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161550):
<p>Let me know if it doesn't work. I'll add it to the README if it does.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161592):
<p>That should make the import directories all point to the right places</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161648):
<p>and then I would have suggested "leanpkg upgrade" or "leanpkg build" -- oh -- I see -- this doesn't work because Chris won't have any leanpkg.path file in his clone?</p>

#### [ Chris Hughes (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161656):
<p>I don't have a leanpkg path</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161663):
<p>Chris -- I have a _target directoy that you don't have because my gitignore file tells git not to upload my _target directory to github</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161669):
<p>so you'll need one of those</p>

#### [ Chris Hughes (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161670):
<p>But I should be able to build it, I can build mathlib, and that's the same.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161708):
<p>Mathlib has no dependencies.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161719):
<p>Our project depends on other projects so it's a bit different.</p>

#### [ Chris Hughes (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161721):
<p>It downloaded all the dependecncies automatically. Trouble is they don't compile.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161722):
<p>I'm not sure that's a problem</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161723):
<p>As long as mathlib compiles</p>

#### [ Chris Hughes (Mar 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161730):
<p>And my computer's too slow to make compiling when I import practical.</p>

#### [ Simon Hudon (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161772):
<p>If you want we can start from scratch.</p>

#### [ Chris Hughes (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161774):
<p>It's a problem because it crashes everything</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161775):
<p>You should be able to get it to work. Kenny got it to work</p>

#### [ Chris Hughes (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161776):
<p>And I doubt mathlib compileseither, since it depends on an old version</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161777):
<p>and he was in exactly the same situation as you -- it wasn't his project and he had to clone from github</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161783):
<p>type leanpkg upgrade</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161784):
<p>This should get the correct versions of everything</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161785):
<p>and then leanpkg build and leave it on overnight</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161786):
<p>or however long it takes</p>

#### [ Chris Hughes (Mar 24 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161828):
<p>If there are errors, leaving it overnight doesn't help</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161882):
<p>You're right, it's not working for me.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161884):
<p>I'll try and figure out what's going on.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161894):
<p>Do you have the latest Lean?</p>

#### [ Chris Hughes (Mar 24 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161939):
<p>The latest lean doesn't compile. I have four day old lean.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162170):
<p>OK so I just tried compiling my project using lean from the linux nightly (commit 28f4143be31b) and my project did not compile.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162172):
<p>The first error is this:</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162175):
<div class="codehilite"><pre><span></span>/home/buzzard/temp/lean-stacks-project/_target/deps/mathlib/data/option.lean:24:1: error: failed to synthesize type class instance for
α : Type u
⊢ is_lawful_monad option
</pre></div>

#### [ Kevin Buzzard (Mar 24 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162215):
<p>and there was some talk about lawful monads recently so maybe there was some change</p>

#### [ Chris Hughes (Mar 24 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162284):
<p>If you just find a version it works with, I'll download that.</p>

#### [ Simon Hudon (Mar 24 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162337):
<p>I believe mathlib doesn't build with the latest nightly. I worked with revision <code>07bb7d809b6be49f38ce4e427c54a82708ae281f </code> of Lean</p>

#### [ Simon Hudon (Mar 24 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162345):
<p>And I use <code>4ceb545f7e07431263e1131a9c9524a28de99472</code> for mathlib</p>

#### [ Chris Hughes (Mar 24 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162409):
<p>I have made some progress. It now gets stuck at importing, because nothing's compiled instead of not finding the file it's meant to import.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162420):
<p>I am downloading lean HEAD. It's three days old and it would not surprise me if ever-efficient Mario had made mathlib work with it.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162461):
<p>Chris are you able to compile Lean from source?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162464):
<p><a href="https://github.com/leanprover/lean/blob/master/doc/make/msys2.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/doc/make/msys2.md">https://github.com/leanprover/lean/blob/master/doc/make/msys2.md</a></p>

#### [ Simon Hudon (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162465):
<p>If you check travis, you'll see that it doesn't work with HEAD</p>

#### [ Chris Hughes (Mar 24 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162471):
<p>Probably not with the current version, since it says build failing. Maybe with a previous version.</p>

#### [ Chris Hughes (Mar 24 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162474):
<p>But I haven't worked out how to build an old commit with git yet.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162528):
<p>Just google "git change to commit" or something</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162565):
<p>google is really good for git commands</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162577):
<p>git checkout commit</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162579):
<p>is probably how to do it</p>

#### [ Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162580):
<p>Oh wooah lean HEAD just failed to build.</p>

#### [ Chris Hughes (Mar 24 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162703):
<p>Yeah. If we just find a version of lean and mathlib to use it should be fine. But I don't know which version.</p>

#### [ Simon Hudon (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162747):
<blockquote>
<p>Simon Hudon: I believe mathlib doesn't build with the latest nightly. I work with revision <code>07bb7d809b6be49f38ce4e427c54a82708ae281f</code>  of Lean</p>
<p>Simon Hudon: And I use <code>4ceb545f7e07431263e1131a9c9524a28de99472</code> for mathlib </p>
</blockquote>

#### [ Kevin Buzzard (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162752):
<p>I just checked out c4cc8c88c08d86cd902c577de09ef69528c2da36 of Lean on the basis that it was the most recent version that compiled (as far as I coudl see)</p>

#### [ Mario Carneiro (Mar 24 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162805):
<p>I built a version slightly in advance of the nightly, but it should be out now</p>

#### [ Chris Hughes (Mar 24 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162881):
<p>Where are the instructions on building lean? I did it before, but I don't remember how</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162927):
<p>Do you know which commit it works with? I am having trouble getting Lean to compile from source and mathlib doesn't compile if I download the latest linux nightly and then use "leanpkg upgrade"</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162939):
<blockquote>
<p>Where are the instructions on building lean? I did it before, but I don't remember how</p>
</blockquote>
<p><a href="https://github.com/leanprover/lean/blob/master/doc/make/msys2.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/doc/make/msys2.md">https://github.com/leanprover/lean/blob/master/doc/make/msys2.md</a></p>

#### [ Chris Hughes (Mar 24 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162993):
<p>I''ve been using the f7977ff5a6bcf7e5c54eec908364ceb40dafc795 version of mathlib. The latest version only works with the version of lean that doesn't work</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163050):
<p>How do I get travis to tell me the last Lean commit which compiled for linux?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163051):
<p>And how do I get mathlib to tell me the version of Lean which it compiled against?</p>

#### [ Simon Hudon (Mar 24 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163101):
<p>You can get the result of all the builds here:</p>
<p><a href="https://travis-ci.org/leanprover/mathlib/builds" target="_blank" title="https://travis-ci.org/leanprover/mathlib/builds">https://travis-ci.org/leanprover/mathlib/builds</a></p>

#### [ Simon Hudon (Mar 24 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163158):
<p>I'm not sure how to use that to infer the corresponding version of Lean other than see that the last successful build was 10 days ago. We can go and see what version Lean was on 10 days ago</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163201):
<p>I don't understand travis.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163202):
<p>According to this link:</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163203):
<p><a href="https://ci.appveyor.com/project/leodemoura/lean/history" target="_blank" title="https://ci.appveyor.com/project/leodemoura/lean/history">https://ci.appveyor.com/project/leodemoura/lean/history</a></p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163206):
<p>the last successful build was c17e5b913b2db687ab38f53285326b9dbb2b1b6e</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163215):
<p>but according to <a href="https://travis-ci.org/leanprover/lean/builds" target="_blank" title="https://travis-ci.org/leanprover/lean/builds">https://travis-ci.org/leanprover/lean/builds</a></p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163255):
<p>it was d6d44a19947e2575b3fceed6d61167d258c661fb</p>

#### [ Simon Hudon (Mar 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163278):
<p>I guess you can try either</p>

#### [ Simon Hudon (Mar 24 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163321):
<p>You might be interested in recording the version of Lean that you use in your repository. You can facilitate the testing and importing this way</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163678):
<p>That's a good idea.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163729):
<p>If I decide to use leanpkg upgrade with a specific version of lean, which version of mathlib will it upgrade to?</p>

#### [ Simon Hudon (Mar 24 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163735):
<p>If you need a reference, I have some scripts for that. Some of them blocks you from committing on git if your lean version is inaccurate</p>

#### [ Simon Hudon (Mar 24 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163756):
<p>I think there are two possibilities: if you're on an official release (say 3.3.0) it will get the version of mathlib that works with it. Otherwise, it will get HEAD</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124164063):
<p>(deleted)</p>


{% endraw %}
