---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47969MathlibandLEANPATH.html
---

## Stream: [new members](index.html)
### Topic: [Mathlib and LEAN_PATH](47969MathlibandLEANPATH.html)

---


{% raw %}
#### [ Jean Lo (Jan 31 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157302484):
<p>I'm sure I'm missing something really obvious here, but I haven't been able to figure it out:</p>
<p>I recently learnt that mathlib now lives under <code>leanprover-community</code>and was trying to add it as a dependency to a package by doing <code>leanpkg add leanprover-community/mathlib</code>. That downloads the repository but ends with a message </p>
<div class="codehilite"><pre><span></span>cannot find revision lean-3.4.2 in repository _target/deps/mathlib
</pre></div>


<p>Later, attempting to import from mathlib in a file throws a <code>file (filename) not found in LEAN_PATH</code>. <code>LEAN_PATH</code> is unset, as I think it should be; and changing it to <code>/usr/local/lib/lean/library</code> results in the same behaviour.</p>

#### [ Simon Hudon (Jan 31 2019 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157302779):
<p>Do you use <code>elan</code>?</p>

#### [ Jean Lo (Jan 31 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157302863):
<p>Not yet, unfortunately.</p>

#### [ Simon Hudon (Jan 31 2019 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303015):
<p>That will help. Install it, that may very well solve the issue.</p>

#### [ Simon Hudon (Jan 31 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303088):
<p>See: <a href="https://github.com/Kha/elan" target="_blank" title="https://github.com/Kha/elan">https://github.com/Kha/elan</a></p>

#### [ Jean Lo (Jan 31 2019 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303268):
<p>I've only recently built Lean from source and then immediately been told that it's a bad idea. Would it be important that I remove (how?) the current installation of Lean before I start using <code>elan</code> to manage it?</p>

#### [ Simon Hudon (Jan 31 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303421):
<p>Yes, that would be best. Are you on a Unix system? (Linux, Mac OS X, etc)</p>

#### [ Jean Lo (Jan 31 2019 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303470):
<p>Yes, I'm on a Linux machine.</p>

#### [ Simon Hudon (Jan 31 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303599):
<p>Here's how you do it:</p>
<div class="codehilite"><pre><span></span>which lean
</pre></div>


<p>Then you can delete <code>lean</code> as well as <code>leanpkg</code> at that location</p>

#### [ Jean Lo (Jan 31 2019 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303666):
<p>nice. That'd be <code>/usr/local/bin/</code> for me — do I have to worry about <code>/usr/local/lib/lean</code>?</p>

#### [ Simon Hudon (Jan 31 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303744):
<p>I would delete it out of precaution but I think you only really need to delete it if <code>which lean</code> finds it</p>

#### [ Jean Lo (Jan 31 2019 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303884):
<p>will do. Thanks for the help! Will report back about whether <code>elan</code> fixes the issue.</p>

#### [ Simon Hudon (Jan 31 2019 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157303947):
<p><span aria-label="+1" class="emoji emoji-1f44d" role="img" title="+1">:+1:</span></p>

#### [ Reid Barton (Jan 31 2019 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157304099):
<p>I think <code>leanpkg add</code> will always look for the branch corresponding to the version of Lean that you're using, so we just need to make a <code>lean-3.4.2</code> branch on mathlib</p>

#### [ Simon Hudon (Jan 31 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157304194):
<p>Is there a way to keep that branch up-to-date automatically?</p>

#### [ Reid Barton (Jan 31 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157304374):
<p>Not that we have found so far, see <a href="https://github.com/leanprover/mathlib/issues/365" target="_blank" title="https://github.com/leanprover/mathlib/issues/365">#365</a></p>

#### [ Simon Hudon (Jan 31 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157304482):
<p>I was thinking of making <code>lean-3.4.2</code> a tag and getting Travis to push the tag on every successful build</p>

#### [ Reid Barton (Jan 31 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157304754):
<p>If we can make it reasonably secure then it sounds like a good option</p>

#### [ Jean Lo (Jan 31 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305069):
<p>have now followed instructions and installed <code>elan</code>. (I'm also using <code>lean-mode</code> — had to set <code>lean-rootdir</code> by hand on the last install, and the path is no longer accurate. Is setting it now to <code>$HOME/.elan</code> the correct thing to do?)</p>
<p>Also, the <code>cannot find revision</code>issue persists. (I'm supposing it's because this 'leanpkg-add looks for the corresponding branch' thing?)</p>

#### [ Reid Barton (Jan 31 2019 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305131):
<p>I think you should unset <code>lean-rootdir</code></p>

#### [ Reid Barton (Jan 31 2019 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305208):
<p>If <code>elan</code> is on your path, then you should not need any configuration, and setting variables might break the way that <code>elan</code> automatically selects the correct version of lean to use for each project</p>

#### [ Jean Lo (Jan 31 2019 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305323):
<p>That was the first thing I attempted, but that just made <code>lean-mode</code> throw an error about</p>
<div class="codehilite"><pre><span></span>Lean was not found in the ’exec-path’ and ’lean-rootdir’ is not defined. Please set it via M-x customize-variable RET lean-rootdir RET.
</pre></div>

#### [ Reid Barton (Jan 31 2019 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305448):
<p>Put the elan bin directory on your path instead (I think the elan installation should have printed instructions on how to do this?)</p>

#### [ Reid Barton (Jan 31 2019 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305468):
<p>then make sure your emacs has the new path, that is, it was started from a new shell</p>

#### [ Reid Barton (Jan 31 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305527):
<p>You want this anyways so that <code>leanpkg</code> will work on the command line</p>

#### [ Reid Barton (Jan 31 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305631):
<p>It looks like setting <code>lean-rootdir</code> to the elan directory would also make emacs work</p>

#### [ Reid Barton (Jan 31 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305648):
<p>(as in <code>~/.elan</code>)</p>

#### [ Jean Lo (Jan 31 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305708):
<p>I thiiink I followed the instructions given by the elan installation, and leanpkg does work on the command line. Setting <code>lean-rootdir</code> to the elan directory makes the <code>lean-rootdir</code> error go away but it still can't seem to figure out how to import stuff from mathlib</p>

#### [ Reid Barton (Jan 31 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157305906):
<p>is this the <code>cannot find revision lean-3.4.2</code> error, or something else?</p>

#### [ Reid Barton (Jan 31 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157306036):
<p>you may need to restart emacs or something</p>

#### [ Reid Barton (Jan 31 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157306039):
<p>if it's a different error</p>

#### [ Jean Lo (Jan 31 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157306087):
<p>Yeah, it's that. <code>cannot find revision lean-3.4.2</code> is printed by <code>leanpkg add leanprover-community/mathlib</code>; and attempting anything like <code>import data.real.basic</code> gives me the <code>not found in the LEAN_PATH</code> error.</p>

#### [ Reid Barton (Jan 31 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157306289):
<p>Right, so that's because the branch doesn't exist</p>

#### [ Reid Barton (Jan 31 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157306384):
<p>Maybe you can use <code>leanpkg add leanprover-community/mathlib master</code>, or the low-tech solution is just to copy the line from somewhere like <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.2/leanpkg.toml" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.2/leanpkg.toml">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.2/leanpkg.toml</a> and put whatever commit you want to use there</p>

#### [ Simon Hudon (Jan 31 2019 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157307919):
<p>I just created the branch. Can you try again?</p>

#### [ Jean Lo (Jan 31 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157308054):
<p>hnh. <code>leanpkg add leanprover-community/mathlib master</code> just ... prints the usage page and does nothing, even though the usage page suggests that <code>add &lt;url&gt; [branch]</code>is the way to write it so I don't really know what's happening.</p>
<p>the low-tech solution seems to have gotten it working though.</p>

#### [ Reid Barton (Jan 31 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157308317):
<p>Weird</p>

#### [ Jean Lo (Jan 31 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157310824):
<p>just tried to add mathlib as a dependency again, everything seems to work fine now that the branch exists. Thanks so much for the help.</p>

#### [ Simon Hudon (Jan 31 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157310834):
<p><span aria-label="+1" class="emoji emoji-1f44d" role="img" title="+1">:+1:</span></p>

#### [ Kevin Buzzard (Jan 31 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157313509):
<p>One of my students ran into a serious issue today and I am wondering whether the installation procedure is now broken. She was doing a fresh Lean install on a mac. She got VS Code working fine. In <span class="user-mention" data-user-id="110087">@Scott Morrison</span> 's description of what to do next it says "you could install elan by hand with <code>curl ...</code> but actually let's use VS Code; open up a file called <code>test.lean</code> and watch the magic happen". She opened <code>test.lean</code> and the magic did not happen (the "Oh! You have no lean! Let's install elan!" box never appeared). That was problem 1. And problem 2 was that once we had got elan installed, she got this <code>cannot find revision lean-3.4.2</code> error. Like Jean, we muddled through, because I knew what the end result was supposed to look like (e.g. I had to edit her <code>leanpkg.path</code> at some point) but we are currently at another low point for installation ease, and I suspect that some docs might now need to be changed.</p>

#### [ Simon Hudon (Jan 31 2019 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157313971):
<p>Did it eventually work?</p>

#### [ Simon Hudon (Jan 31 2019 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157314086):
<p>I'm wondering if the difficulties are temporary because of the transfer of ownership of mathlib. Can you try once again and see if it's fixed?</p>

#### [ Kevin Buzzard (Jan 31 2019 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157314143):
<p>Yes, it took me about 15 minutes but she now has a working Lean and mathlib. I thought I'd seen all the errors but I am fairly new to <code>elan</code> myself and I did not understand the <code>cannot find revision lean-3.4.2</code> error, I don't think I'd seen it before. I am also now unclear which of the three of so versions of mathlib on github is the one we're supposed to be adding as a dependency for a generic user who just wants things working so they can do elementary stuff.</p>

#### [ Kevin Buzzard (Jan 31 2019 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157314301):
<p>I can't try it now because our meeting finished several hours ago and I'm not going to see her again until next week; I'm also reluctant to fiddle with her installation because we got it working now. I guess if she runs into problems I'll hear from her. She's going to make a start on group cohomology but I don't know how far we'll get.</p>

#### [ Simon Hudon (Jan 31 2019 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157314436):
<p>With regards to the right version, <code>leanprover/mathlib</code> and <code>leanprover-community/mathlib</code> now refer to the same library and that's the one we use. The actual location is <code>leanprover-community/mathlib</code> but doing things as before (i.e. using <code>leanprover/mathlib</code>) should still work.</p>

#### [ Simon Hudon (Jan 31 2019 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157314447):
<p>A few hours ago, I added a <code>lean-3.4.2</code> branch which might resolve part or all the issues.</p>

#### [ Andrew Ashworth (Feb 01 2019 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157319557):
<blockquote>
<p>but actually let's use VS Code; open up a file called test.lean and watch the magic happen". She opened test.lean and the magic did not happen (the "Oh! You have no lean! Let's install elan!" box never appeared). That was problem 1.</p>
</blockquote>
<p>if this is supposed to happen, then I'll also confirm its not working on most recent version of windows and vscode as of yesterday</p>

#### [ Simon Hudon (Feb 01 2019 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157320445):
<p>Have you tried today?</p>

#### [ Scott Morrison (Feb 01 2019 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157320698):
<p>I just tried today, on a mac, and indeed the magic "let's install elan" box is not working. at the moment.</p>

#### [ Simon Hudon (Feb 01 2019 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157320883):
<p>Ok, that's useful to know. Beside installing <code>elan</code>, what is it supposed to do?</p>

#### [ Simon Hudon (Feb 01 2019 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157320945):
<p>What I mean to ask is, beside executing <code>curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh</code> does it do anything? And what happens if you write that line in a terminal?</p>

#### [ Scott Morrison (Feb 01 2019 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321103):
<p>Sorry, <span class="user-mention" data-user-id="110026">@Simon Hudon</span> , what is _what_ supposed to do? I didn't follow. The vscode-lean extension is no longer offering to install <code>elan</code> if no usable copy of <code>lean</code> is found. I think I understand why, and am testing a fix.</p>

#### [ Scott Morrison (Feb 01 2019 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321269):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span>, you added the line: <a href="https://github.com/leanprover/vscode-lean/blob/master/src/server.ts#L71" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/src/server.ts#L71">https://github.com/leanprover/vscode-lean/blob/master/src/server.ts#L71</a> a while back. Could you explain why? I think it is incorrect, and it broke the "offer to install elan if lean is not available" functionality.</p>

#### [ Scott Morrison (Feb 01 2019 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321273):
<p>I can PR removing it again if no one objects.</p>

#### [ Kevin Buzzard (Feb 01 2019 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321385):
<p>The curl thing installs elan just fine, it's vs code that doesn't</p>

#### [ Simon Hudon (Feb 01 2019 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321485):
<p>Ok <span class="user-mention" data-user-id="110087">@Scott Morrison</span> it looks like you're on top of it. Let me know you need something.</p>

#### [ Scott Morrison (Feb 01 2019 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321760):
<p>Okay, I tested that removing that line causes vscode to offer to install elan, and then not offer again after it succeeds. I didn't attempt to test other situations carefully (where people have lean installed elsewhere, perhaps they'll still get the offer if something goes wrong?).</p>

#### [ Scott Morrison (Feb 01 2019 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157321766):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> if I missed something, please let me know.</p>

#### [ Bryan Gin-ge Chen (Feb 01 2019 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157323485):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Hmm, I was trying to address this: <a href="https://github.com/leanprover/vscode-lean/issues/95" target="_blank" title="https://github.com/leanprover/vscode-lean/issues/95">https://github.com/leanprover/vscode-lean/issues/95</a> I think you might be right that I did something wrong.</p>

#### [ Bryan Gin-ge Chen (Feb 01 2019 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157324318):
<p>I added a comment at the PR <a href="https://github.com/leanprover/vscode-lean/pull/111" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/111">https://github.com/leanprover/vscode-lean/pull/111</a></p>

#### [ Scott Morrison (Feb 01 2019 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157378321):
<p>Okay, I've just PR'd a better fix. Hopefully VSCode will prompt to install elan if it can't find a copy of Lean, exactly once, and will not do so if the server crashes and needs to be restarted.</p>
<p><a href="https://github.com/leanprover/vscode-lean/pull/112/files" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/112/files">https://github.com/leanprover/vscode-lean/pull/112/files</a></p>

#### [ Johan Commelin (Feb 02 2019 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157412373):
<p>I have a laptop without Lean. Once this is merged, I'll test it on that laptop.</p>

#### [ Johan Commelin (Feb 02 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mathlib%20and%20LEAN_PATH/near/157428006):
<p><span class="user-mention" data-user-id="199347">@Raymond</span> This also explains why VScode didn't do anything when you tried to install Lean.</p>


{% endraw %}
