---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50145Missingsomesettheorems.html
---

## Stream: [general](index.html)
### Topic: [Missing some set theorems?](50145Missingsomesettheorems.html)

---


{% raw %}
#### [ Lyle Kopnicky (Jul 25 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252632):
<p>Hi folks, I have been following Logic &amp; Proof (<a href="https://leanprover.github.io/logic_and_proof/logic_and_proof.pdf" target="_blank" title="https://leanprover.github.io/logic_and_proof/logic_and_proof.pdf">https://leanprover.github.io/logic_and_proof/logic_and_proof.pdf</a>) and in Chapter 12, it says to use <code>import data.set</code>, but I get an error that that path doesn't exist. However, I am still able to use set membership operators, etc. On the other hand, the book mentions theorems like <code>mem_inter</code>, but those aren't in scope. Have they moved to another library? How do I import them? Thanks.</p>

#### [ Simon Hudon (Jul 25 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252817):
<p>It got renamed recently to <code>data.set.basic</code></p>

#### [ Simon Hudon (Jul 25 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252860):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> This would be worth updating I believe</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252868):
<p>Ah, thanks, that doesn't seem to work either. Maybe my Lean installation is old.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252871):
<p>I'm using the Lean extension in VS Code, also.</p>

#### [ Simon Hudon (Jul 25 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252916):
<p>Can you bring up your project's leanpkg.toml and check that you have mathlib in your dependencies?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252976):
<p>Yeah, I don't seem to have that. It's in <code>$HOME/lean-3.3.0-darwin/lib/lean/leanpkg/leanpkg.toml</code> and it just has:</p>
<div class="codehilite"><pre><span></span>[package]
name = &quot;leanpkg&quot;
version = &quot;0.1&quot;
</pre></div>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252989):
<p>I guess that's a global <code>leanpkg.toml</code> file? I don't have one for my project. I'm just creating individual <code>.lean</code> files.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253038):
<p>What should I add to the <code>leanpkg.toml</code> file?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253047):
<p>Or maybe I need to run the <code>leanpkg</code> command to add a library?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253109):
<p>I really know nothing about lean package management. Just did the minimal amount to get Lean and the VS Code extension installed.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253850):
<p>Sorry i stepped away</p>

#### [ Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253895):
<p>go in your project's directory with a terminal and call <code>leanpkg init my_project</code> (feel free to pick a better name)</p>

#### [ Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253898):
<p>Then call <code>leanpkg add leanprover/mathlib</code></p>

#### [ Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253899):
<p>then <code>leanpkg build</code></p>

#### [ Simon Hudon (Jul 25 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253905):
<p>By default, leanpkg sets <code>src</code> as the directory where all your sources are located</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254066):
<p>Thanks! The <code>leanpkg init my_project</code> worked, but:</p>
<div class="codehilite"><pre><span></span>$ leanpkg add leanprover/mathlib
mathlib: using local path ./leanprover/mathlib
failed to open file &#39;./leanprover/mathlib/leanpkg.toml&#39;
</pre></div>

#### [ Simon Hudon (Jul 25 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254125):
<p>sometimes you have to be more explicit: <code>leanpkg add https://github.com/leanprover/mathlib</code></p>

#### [ Simon Hudon (Jul 25 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254175):
<p>Btw, this might help: <a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">https://github.com/leanprover/mathlib/blob/master/docs/elan.md</a></p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254181):
<p>That add command seemed to work, thanks. I'm doing the build.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254188):
<p>It's funny, I just recently added a similar feature to the Haskell build tool Stack, to be able to download templates from different github users without having to specify the full path.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254246):
<p>The Elan tool looks helpful, thanks. Sounds a bit like Stack actually, letting you use different versions of the compiler.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254360):
<p>Well, the <code>leanpkg build</code> ran successfully. And I restarted the editor, and now the <code>import data.set.basic</code> shows no error. But <code>univ</code>, <code>mem_inter</code>, and those other theorems are still redlined. Maybe I need to <code>open</code> some namespace?</p>

#### [ Simon Hudon (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254413):
<p>To be fair <code>elan</code> and <code>leanpkg</code> share some the functions of <code>stack</code> but we still don't have curated package collections.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254415):
<p>Wasn't it already possible to link to github in your <code>stack.yaml</code> file, in the <code>packages</code> section?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254416):
<p>Ah, right. Well that's a pretty unique feature to <code>stack</code>.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254457):
<p>I'm hoping to see that happen eventually. I find it pretty useful. But mathlib changes so much that we keep upgrading.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254464):
<p>This is about templates for new projects. There's a set of templates under the <code>commercialstack</code> user on github. This was so you could install templates from a different github user by writing <code>stack new username/template_name</code>. Instead of having to write the whole URL.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254465):
<p>In VS code, there may be a command to let you find definitions.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254508):
<p>Yeah, "no definition found for univ"</p>

#### [ Simon Hudon (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254514):
<p>I might have misled you. Try also importing <code>data.set</code></p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254517):
<p>OK, added that. Still can't find <code>univ</code>.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254518):
<blockquote>
<p>This is about templates for new projects. There's a set of templates under the <code>commercialstack</code> user on github. This was so you could install templates from a different github user by writing <code>stack new username/template_name</code>. Instead of having to write the whole URL.</p>
</blockquote>
<p>Nice!</p>

#### [ Simon Hudon (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254560):
<p>What version of Lean is written in your <code>leanpkg.toml</code>?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254563):
<p>You can also install templates from gitlab or bitbucket, e.g. <code>stack new gitlab:username/template_name</code></p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254565):
<p>Lean version 3.3.0</p>

#### [ Simon Hudon (Jul 25 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254574):
<p>Ok, that makes sense. Let's set it to <code>3.4.1</code> to have the most recent stuff.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254626):
<p>OK, I changed it and ran <code>leanpkg build</code> but got the error <code>WARNING: Lean version mismatch: installed version is 3.3.0, but package requires 3.4.1
</code>. Maybe I need to install elan.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254672):
<p>Yes, that makes things much easier</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254679):
<p>Thing is, I'm leading a study group tomorrow night where we're supposed to go over the exercises for Chapter 12. And I just got around to working on them tonight, and now I realize probably nobody else is going to be able to work them either. Will have to post instructions for folks.</p>

#### [ Simon Hudon (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254741):
<p>That would be good. I think this might be a good start: <a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">https://github.com/leanprover/mathlib/blob/master/docs/elan.md</a></p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254743):
<p>I wonder how I installed Lean the first time - probably just downloaded the binary package. Looks like it's on homebrew and that has 3.4.1 - might have been another simple way to keep it up to date.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254745):
<p>Got it, thanks!</p>

#### [ Simon Hudon (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254747):
<p>Maybe we should remove it from homebrew and put elan instead</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254809):
<p>Nah. Both ghc and stack are on homebrew. People can choose what they want. But it would be helpful if this page said anything about elan: <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a></p>

#### [ Simon Hudon (Jul 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254915):
<p>Yeah that's true. The thing with ghc though is that there are many options for build systems. Some people use cabal, others nix. But with Lean, I think it's too easy to get started the wrong way and there aren't that many different ways of using the tool.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254972):
<p>OK, good point</p>

#### [ Simon Hudon (Jul 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254978):
<p>Any luck with elan so far?</p>

#### [ Simon Hudon (Jul 25 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130255092):
<p>I should go, my bed is calling to me. I hope it works out for your study session</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130255488):
<p>Sorry, just biked home because the coffee shop closed. Will try elan now. Thanks and take care.</p>

#### [ Mario Carneiro (Jul 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130260428):
<p><span class="user-mention" data-user-id="113073">@Lyle Kopnicky</span>  I think the missing step is <code>open set</code>. Assuming you got <code>import data.set.basic</code> working, the name of the univ set is <code>set.univ</code> or just <code>univ</code> if <code>set</code> is open.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284056):
<p>Thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, but I am even further back now. I installed Elan and did <code>leanpkg install leanprover/mathlib</code> and that seemed to work fine. Then did <code>leanpkg build</code> and it crashed with <code>&lt;unknown&gt;:1:1: error: file 'data/list/basic' not found in the LEAN_PATH</code>. How do I install that? I tried <code>leanpkg install data/list/basic</code> but it says that path is not found.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284080):
<p>Here is my <code>leanpkg.toml</code>:</p>
<div class="codehilite"><pre><span></span>[package]
name = &quot;logic_and_proof&quot;
version = &quot;0.1&quot;
lean_version = &quot;3.4.1&quot;

[dependencies]
</pre></div>


<p>Do I need to manually add something to <code>dependencies</code>?</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284140):
<p>I though running <code>leanpkg install leanprover/mathlib</code> would add something to <code>dependencies</code> but it didn't.</p>

#### [ Reid Barton (Jul 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284155):
<p>You need some version of <code>leanpkg add</code></p>

#### [ Reid Barton (Jul 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284209):
<p>Which will add to that dependencies section for you.</p>

#### [ Reid Barton (Jul 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284312):
<p>(or you can edit that section manually)</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284339):
<p>Ah, that seemed to do the trick. Thanks!</p>

#### [ Reid Barton (Jul 25 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284391):
<p><code>leanpkg install</code> is analogous to <code>cabal install</code> I think. Not sure I have ever used it.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284460):
<p>OK. Up until yesterday I hadn't used <code>leanpkg</code> at all. Have just been using individual <code>.lean</code> files but that didn't work anymore when I needed some of these set theorems.</p>

#### [ Lyle Kopnicky (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130294885):
<p>Yay, finally have it working, following the <code>leanpkg build</code>. In the code, <code>import data.set</code> followed by <code>open set</code> works.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130295045):
<p>How many seconds have you now got to do all the exercises? :-)</p>

#### [ Lyle Kopnicky (Jul 27 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130385489):
<p>Haha... I didn't manage to do the exercise beforehand. But others in the group did, so they presented their solutions. It was awesome. One person had already installed Elan, I guess, and another was using the online Lean, so they were both able to do the exercises.</p>

#### [ Lyle Kopnicky (Jul 27 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130385550):
<p>But during the meeting, I was able to paste their code into my editor and everything checked out fine. I was projecting it on the whiteboard and they could underline things and draw around them.</p>


{% endraw %}
