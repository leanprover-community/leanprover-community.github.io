---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77961elanonwindows.html
---

## Stream: [general](index.html)
### Topic: [elan on windows](77961elanonwindows.html)

---


{% raw %}
#### [ Scott Morrison (Sep 26 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647268):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>,</p>

#### [ Scott Morrison (Sep 26 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647271):
<p>I'm trying to work on installation procedures.</p>

#### [ Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647277):
<p>Yesterday two students very successfully used the following technique:</p>

#### [ Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647282):
<p>1. Install Git for Windows</p>

#### [ Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647284):
<p>2. Install VS Code</p>

#### [ Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647289):
<p>3. In a git bash terminal, install Elan</p>

#### [ Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647294):
<p>When I'm trying it again today on a virtualised copy of windows 10, I'm getting the error message:</p>

#### [ Scott Morrison (Sep 26 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647342):
<div class="codehilite"><pre><span></span>info: downloading installer
Archive:  elan-init.zip
  inflating: elan-init.exe
elan-init.exe: error while loading shared libraries: api-ms-win-crt-locale-l1-1-0.dll: cannot open shared object file: No such file or directory
</pre></div>

#### [ Scott Morrison (Sep 26 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647349):
<p>Do you (or anyone else) have an idea of why this is a problem for me, but wasn't a problem for them yesterday?</p>

#### [ Scott Morrison (Sep 26 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647415):
<p>Presumably it is just that they had already installed something that provided this dll...?</p>

#### [ Scott Morrison (Sep 26 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134647421):
<p>Could we perhaps just bundle it in elan-init.zip?</p>

#### [ Scott Morrison (Sep 26 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134648684):
<p>It seems this file (and about 8 others) are all available as a separate download at <a href="https://www.microsoft.com/en-au/download/details.aspx?id=48145" target="_blank" title="https://www.microsoft.com/en-au/download/details.aspx?id=48145">https://www.microsoft.com/en-au/download/details.aspx?id=48145</a></p>

#### [ Scott Morrison (Sep 26 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134648700):
<p>However they are only tiny files, and they are all redistributable, so we could just package them with the elan download.</p>

#### [ Scott Morrison (Sep 26 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134649555):
<p>Hmm, I've been looking at the build script for Elan, and can't make head or tail or it, so I think I might be stuck in this direction. I guess for the best available instructions for Elan on windows will have to be to install this extra set of DLLs by hand. :-(</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134652368):
<p>[off-topic -- related but not the same -- Scott -- if you have a virtual windows 10 machine around, can you be bothered to try my easy install method ? (1) download and uncompress <a href="http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip">http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip</a> [lean + mathlib + sample project with path and toml files + all .olean files made] (2) install VS Code and Lean extension, and edit <code>lean.executablePath</code> (3) File -&gt; Open Folder -&gt; open "my_project" (4) that's it. I am interested to know how the .olean files perform. Try importing <code>data.real.basic</code> or whatever.]</p>

#### [ Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653895):
<p>Hi Kevin,</p>

#### [ Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653906):
<p>I got stuck at the "edit <code>lean.executablePath</code> step, because I don't understand windows.</p>

#### [ Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653915):
<p>That zip file ended up in a "Downloads" directory, but ... where is that? :-)</p>

#### [ Scott Morrison (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653951):
<p>The built-in folder viewer in Windows doesn't seem to want to admit that there is some notion of absolute path :-)</p>

#### [ Scott Morrison (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653959):
<p>And the VS Code settings editor doesn't want to give me a file picker. :-)</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134653975):
<p>meh</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654021):
<p>Try C:/Users/my_userid/Downloads</p>

#### [ Scott Morrison (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654040):
<p>Ah, the problem is that the zip file wasn't actually uncompressed!</p>

#### [ Scott Morrison (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654056):
<p>In the file viewer I clicked on it and it showed me the contents, but it is just showing me the inside of a zip file without decompressing.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654058):
<p>oh yeah, Windows just opens them when you click on them :-/</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654067):
<p>right click on it to uncompress it maybe</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654076):
<p>7-zip or winzip or something</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654118):
<p>there is a "extract all" button in explorer when you open a zip file</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654139):
<p>are you good at computers?</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654168):
<p>Thanks :-)</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654173):
<p>was that directed at me?</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654212):
<p>Someone with a mac and someone using linux on the other side of the world trying to figure out how to uncompress a file in Windows :-)</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654216):
<p>We just needed someone who was good at computers to come along</p>

#### [ Sean Leather (Sep 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134654358):
<p>I recently looked at a Windows computer for the first time in a long time. I was surprised things had changed so much, and not in a good way. But, fortunately for my brother-in-law, I could still figure out how to clean up his task bar and make bookmarks in Edge.</p>

#### [ Scott Morrison (Sep 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134656364):
<p>Ok, I unzipped on the terminal, eventually worked out the path to use for <code>lean.executablePath</code>, and it works</p>

#### [ Scott Morrison (Sep 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134656384):
<p>It was about a 15 second delay watching a yellow bar before your <code>test.lean</code> finished.</p>

#### [ Scott Morrison (Sep 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134656436):
<p>I'm not sure what that says about the <code>olean</code> files, however.</p>

#### [ Scott Morrison (Sep 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134656443):
<p>I think this virtual machine is still set to only use one core.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134661897):
<p>Doesnt VS code always take some time sorting stuff out when it starts up? What happens if you import analysis.real?</p>

#### [ Scott Morrison (Sep 26 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134670622):
<p>I've just updated the mathlib documentation on using elan.</p>

#### [ Scott Morrison (Sep 26 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134670633):
<p>Hopefully it is all correct, and works on ubuntu / macOS / windows 10.</p>

#### [ Scott Morrison (Sep 26 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134670715):
<p>I probably ought to create brand new virtual machines for each and try them out once more...</p>

#### [ Scott Morrison (Sep 26 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134670733):
<p>But I think once that PR gets merged, this may be a better set of starting instructions than Kevin's blog post.</p>

#### [ Scott Morrison (Sep 26 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134670755):
<p><a href="https://github.com/leanprover/mathlib/pull/371" target="_blank" title="https://github.com/leanprover/mathlib/pull/371">https://github.com/leanprover/mathlib/pull/371</a> if anyone wants to try it out.</p>

#### [ Patrick Massot (Sep 26 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134671180):
<p>At the end of scenario 1, I read "If you want to play more, it's better to compile all your dependencies once and for all. You can do this by going into my_playground and running leanpkg build."  But this is already what is written in the previous paragraph. I guess this was meant to explain how to fully compile mathlib. For this I think you need to go to <code>_target/deps/mathlib</code> and run <code>lean --make</code> (or <code>leanpkg build</code>?)</p>

#### [ Reid Barton (Sep 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134672299):
<p>Running <code>leanpkg build</code> inside the dependencies can cause lean to get confused, I recall. But I think <code>lean --make</code> in the dependencies is probably okay and recently I tried <code>lean --make _target/deps/mathlib</code> from the project directory and as far as I can tell it worked fine.</p>

#### [ Reid Barton (Sep 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134672323):
<p>See <a href="https://github.com/leanprover/mathlib/issues/308" target="_blank" title="https://github.com/leanprover/mathlib/issues/308">https://github.com/leanprover/mathlib/issues/308</a> where this paragraph is discussed</p>

#### [ Reid Barton (Sep 26 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134672441):
<p>I was hoping that some expert would come along and tell me whether my suggestion is OK, but at this point I guess I should just PR it</p>

#### [ Scott Morrison (Sep 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134674266):
<p>This sounds good to me. <code>lean --make _target/deps/mathlib</code> works for me, and I think should be the canonical advice if you want the entire thing precompiled. I'm not convinced anyone should want that, but okay. :-)</p>

#### [ Patrick Massot (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134674305):
<p>I want that. I don't want my workflow to break each time I add a new import in a Lean file</p>

#### [ Scott Morrison (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134674326):
<p>okay!</p>

#### [ Scott Morrison (Sep 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134674581):
<p>In other installation news, my PR to <code>vscode-lean</code> at &lt;<a href="https://github.com/leanprover/vscode-lean/pull/91" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/91">https://github.com/leanprover/vscode-lean/pull/91</a>&gt; seems to be working now on all operating systems, and means that the vscode extension will offer to install <code>elan</code> for you if it can't find a copy of Lean already.</p>

#### [ Scott Morrison (Sep 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134674626):
<p>I think I now have 7 outstanding PRs across 3 repos. :-) Maybe I'll go do some maths for a while.</p>

#### [ Scott Morrison (Sep 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134706203):
<p>And then there were 6!</p>

#### [ Scott Morrison (Sep 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134706204):
<p>Thanks <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> for merging that. I think Gabriel is away still, but it would be great if you wanted to have a look at &lt;<a href="https://github.com/leanprover/vscode-lean/pull/91" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/91">https://github.com/leanprover/vscode-lean/pull/91</a>&gt;, my PR to vscode-lean which will automatically offer to install elan if it can't find Lean.</p>

#### [ Scott Morrison (Sep 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134706261):
<p>If we can find a mechanism that is reliable, I think this will really soften the installation problem for beginners.</p>

#### [ Sebastian Ullrich (Sep 27 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134706807):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Looks fine to me, but I'm not sure I want to find out how to do a vscode-lean release right now</p>

#### [ Sebastian Ullrich (Sep 27 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134706813):
<p>You may want to tidy up the commit history a bit</p>

#### [ Scott Morrison (Sep 27 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134707882):
<p>Will do, thanks. I'll wait to see what Gabriel says.</p>

#### [ Scott Morrison (Sep 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/134708057):
<p>Okay, commit history fixed!</p>

#### [ Neil Strickland (Oct 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135676595):
<p>The new procedure looks promising, but it does not work correctly when the user's home directory has spaces in (which is a common pattern, eg C:\Users\Neil Strickland).  Specifically, when trying to run leanpkg --help in a Git bash terminal embedded in VS Code, I see</p>
<div class="codehilite"><pre><span></span>&#39;Strickland\.elan\toolchains\stable\bin\..&#39; is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Neil:1:0: error: file &#39;C:\Users\Neil&#39; not found
&lt;unknown&gt;:1:1: error: file &#39;C:\Users\Neil&#39; not found
</pre></div>


<p>which indicates that something somewhere is using the path C:\Users\Neil Strickland\.elan\toolchains\stable\bin and not escaping it correctly.</p>
<p>This is a bit mysterious to me.  Running "which leanpkg" reports "/c/Users/Neil Strickland/.elan/bin/leanpkg".  Note that this is not the path that is causing trouble above.   I think that leanpkg is actually starting and producing the above error message.  However, looking at <a href="https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/main.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/main.lean">https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/main.lean</a> suggests that "leanpkg --help" should always run correctly without needing to resolve any paths.  On the other hand, it is strange that /c/Users/Neil Strickland/.elan/bin/ contains four executables (lean.exe, elan.exe, leanpkg.exe and leanchecker.exe) which cmp tells me are byte-for-byte identical.  So probably that leanpkg.exe involves some kind of wrapper that is producing the error message.</p>
<p>I have not been able to work out where leanpkg is getting the bad path from.  I looked in various places under /c/Users/Neil Strickland/.elan and /c/Users/Neil Strickland/.vscode and /c/Users/Neil Strickland/AppData/Roaming/Visual Studio Code without success.  Running "env" under Git bash also does not enlighten me.</p>
<p>In general, the problem with spaces in paths in Lean seems to arise as follows.  The only Windows system call anywhere in the Lean code seems to be a CreateProcess() at line 221 of <a href="https://github.com/leanprover/lean/blob/master/src/library/process.cpp" target="_blank" title="https://github.com/leanprover/lean/blob/master/src/library/process.cpp">https://github.com/leanprover/lean/blob/master/src/library/process.cpp</a>.  On lines 70,74,77 of <a href="https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/resolve.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/resolve.lean">https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/resolve.lean</a> there are calls to exec_cmd which end up using the above system call to start Git.  This is probably appropriate, but the arguments should be escaped properly.  However, in various other places in resolve.lean and main.lean the functions exec_cmd and io.proc.spawn are used to create directories and check for the existence of files and directories.  These could again be fixed by escaping the arguments properly but it would be much more appropriate and robust to refactor the code to  use the system calls CreateDirectory() and PathFileExists() (and their POSIX equivalents) directly.</p>
<p>Probably some of the above commentary should be converted to issues on github.  But I am not yet properly familiar with how everything fits together.</p>

#### [ Reid Barton (Oct 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135676727):
<p>The issue is in <code>leanpkg.bat</code>: <a href="https://github.com/leanprover/lean/pull/1976/files" target="_blank" title="https://github.com/leanprover/lean/pull/1976/files">https://github.com/leanprover/lean/pull/1976/files</a><br>
I'm not sure whether just modifying your local copy will confuse elan, but it's worth a try</p>

#### [ Reid Barton (Oct 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135676741):
<p>(There could be other issues, I suppose, but this is one known one.)</p>

#### [ Neil Strickland (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135677343):
<p>I don't believe that that is correct.  Other methods of installing Lean give me a file leanpkg.bat which is a wrapper to the executable leanpkg.exe.  However, using elan via VS Code installs the lean executables in C:\Users\Neil Strickland\.elan\bin, and there is a leanpkg.exe there but no leanpkg.bat.  Moreover, leanpkg is invoked from Git bash which would ignore any .bat file anyway.  When starting Git bash inside VS Code in the obvious way, the environment variables LEANDIR, LIBDIR and LEAN_PATH are not set, but the PATH variable includes C:\Users\Neil Strickland\.elan\bin, and "which leanpkg" reports that that is where leanpkg is found.</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135679736):
<p>I'm pinging <span class="user-mention" data-user-id="130491">@Scott Olson</span>, who wrote the patch to <code>leanpkg.bat</code> mentioned by Reid. Since he's already looked into this issue, he may be well-equipped to follow up on Neil's post above.</p>

#### [ Scott Olson (Oct 12 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135680103):
<p>I made a PR at <a href="https://github.com/leanprover/lean/issues/1976" target="_blank" title="https://github.com/leanprover/lean/issues/1976">lean#1976</a>. These errors are from <code>leanpkg.bat</code>:</p>
<div class="codehilite"><pre><span></span>&#39;Strickland\.elan\toolchains\stable\bin\..&#39; is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Neil:1:0: error: file &#39;C:\Users\Neil&#39; not found
&lt;unknown&gt;:1:1: error: file &#39;C:\Users\Neil&#39; not found
</pre></div>


<p>Specifically the first line comes from the <code>IF NOT EXIST</code> line and the latter two come from the <code>lean</code> line since it's getting passed</p>
<div class="codehilite"><pre><span></span>lean --run &quot;C:\Users\Neil&quot; &quot;Strickland\.elan\toolchains\stable\bin\..\lib\lean\leanpkg\leanpkg\main.lean&quot;
</pre></div>


<p>instead of</p>
<div class="codehilite"><pre><span></span>lean --run &quot;C:\Users\Neil Strickland\.elan\toolchains\stable\bin\..\lib\lean\leanpkg\leanpkg\main.lean&quot;
</pre></div>

#### [ Reid Barton (Oct 12 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135680368):
<p>I think the <code>leanpkg</code> in <code>.elan/bin</code> (which is really elan itself) invokes <code>leanpkg</code> in (for example) <code>.elan/toolchains/3.4.1/bin/</code>, which should be <code>leanpkg.bat</code> on Windows. I would have to defer to someone who has a Windows machine though.</p>

#### [ Scott Olson (Oct 12 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135680439):
<p>Oh yes, I looked into that before and Reid is correct. I forgot the step where elan has its own <code>leanpkg</code> wrapper binary.</p>

#### [ Scott Olson (Oct 12 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135680475):
<p>I originally spent quite a while thinking elan's code contained the bug until I figured out it was invoking <code>leanpkg.bat</code>...</p>

#### [ Scott Olson (Oct 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135681462):
<p>Also, for the curious, the elan binaries are not just byte-for-byte identical, but actually hardlinked:</p>
<div class="codehilite"><pre><span></span>C:\Users\Scott&gt;fsutil hardlink list .elan\bin\leanpkg.exe
\Users\Scott\.elan\bin\lean.exe
\Users\Scott\.elan\bin\leanpkg.exe
\Users\Scott\.elan\bin\leanchecker.exe
\Users\Scott\.elan\bin\elan.exe
</pre></div>


<p>Meaning the filesystem only stores one file which these 4 paths all point to</p>

#### [ Neil Strickland (Oct 12 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135681602):
<p>This seems to be correct: C:\Users\Neil Strickland\.elan\bin\leanpkg.exe invokes C:\Users\Neil Strickland\.elan\toolchains\*\leanpkg.bat via cmd.exe even when we start with Git bash, which is all pretty convoluted.  Editing leanpkg.bat by hand at least allows be to run leanpkg --help successfully.  I have not yet tried to do anything more useful.</p>

#### [ Scott Olson (Oct 12 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135681792):
<p><code>.elan\bin\leanpkg.exe</code> is just a normal windows program so it can invoke a .bat file regardless of being invoked from git bash or anything else</p>

#### [ Neil Strickland (Oct 12 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135682821):
<p>Certainly it can; that doesn't mean that it should.  You probably need to call CreateProcess() to invoke leanpkg and if necessary you can supply the required environment variables as an argument to CreateProcess() as documented at <a href="https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa" target="_blank" title="https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa">https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa</a> instead of going through leanpkg.bat.</p>

#### [ Scott Olson (Oct 12 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135682953):
<p>elan could certainly invoke <code>lean</code> itself without going through <code>leanpkg.bat</code>, which we should probably do anyway because then it will work regardless of whether we get <code>leanpkg.bat</code> fixed, and for older versions</p>

#### [ Scott Olson (Oct 12 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135683106):
<p>elan is written in Rust so we probably don't need to think about the exact Windows API calls, but it should be possible to make the wrapper invoke <code>lean</code> with the extra <code>--run &lt;path to leanpkg&gt;</code> args and the environment variables</p>

#### [ Scott Olson (Oct 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20windows/near/135683846):
<p>I posted an issue to the elan repo: <a href="https://github.com/Kha/elan/issues/16" target="_blank" title="https://github.com/Kha/elan/issues/16">https://github.com/Kha/elan/issues/16</a></p>


{% endraw %}
