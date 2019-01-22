---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77961elanonwindows.html
---

## [general](index.html)
### [elan on windows](77961elanonwindows.html)

#### [Scott Morrison (Sep 26 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647268):
@**Sebastian Ullrich**,

#### [Scott Morrison (Sep 26 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647271):
I'm trying to work on installation procedures.

#### [Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647277):
Yesterday two students very successfully used the following technique:

#### [Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647282):
1. Install Git for Windows

#### [Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647284):
2. Install VS Code

#### [Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647289):
3. In a git bash terminal, install Elan

#### [Scott Morrison (Sep 26 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647294):
When I'm trying it again today on a virtualised copy of windows 10, I'm getting the error message:

#### [Scott Morrison (Sep 26 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647342):
```
info: downloading installer
Archive:  elan-init.zip
  inflating: elan-init.exe
elan-init.exe: error while loading shared libraries: api-ms-win-crt-locale-l1-1-0.dll: cannot open shared object file: No such file or directory
```

#### [Scott Morrison (Sep 26 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647349):
Do you (or anyone else) have an idea of why this is a problem for me, but wasn't a problem for them yesterday?

#### [Scott Morrison (Sep 26 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647415):
Presumably it is just that they had already installed something that provided this dll...?

#### [Scott Morrison (Sep 26 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134647421):
Could we perhaps just bundle it in elan-init.zip?

#### [Scott Morrison (Sep 26 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134648684):
It seems this file (and about 8 others) are all available as a separate download at https://www.microsoft.com/en-au/download/details.aspx?id=48145

#### [Scott Morrison (Sep 26 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134648700):
However they are only tiny files, and they are all redistributable, so we could just package them with the elan download.

#### [Scott Morrison (Sep 26 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134649555):
Hmm, I've been looking at the build script for Elan, and can't make head or tail or it, so I think I might be stuck in this direction. I guess for the best available instructions for Elan on windows will have to be to install this extra set of DLLs by hand. :-(

#### [Kevin Buzzard (Sep 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134652368):
[off-topic -- related but not the same -- Scott -- if you have a virtual windows 10 machine around, can you be bothered to try my easy install method ? (1) download and uncompress http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip [lean + mathlib + sample project with path and toml files + all .olean files made] (2) install VS Code and Lean extension, and edit `lean.executablePath` (3) File -> Open Folder -> open "my_project" (4) that's it. I am interested to know how the .olean files perform. Try importing `data.real.basic` or whatever.]

#### [Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653895):
Hi Kevin,

#### [Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653906):
I got stuck at the "edit `lean.executablePath` step, because I don't understand windows.

#### [Scott Morrison (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653915):
That zip file ended up in a "Downloads" directory, but ... where is that? :-)

#### [Scott Morrison (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653951):
The built-in folder viewer in Windows doesn't seem to want to admit that there is some notion of absolute path :-)

#### [Scott Morrison (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653959):
And the VS Code settings editor doesn't want to give me a file picker. :-)

#### [Kevin Buzzard (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134653975):
meh

#### [Kevin Buzzard (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654021):
Try C:/Users/my_userid/Downloads

#### [Scott Morrison (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654040):
Ah, the problem is that the zip file wasn't actually uncompressed!

#### [Scott Morrison (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654056):
In the file viewer I clicked on it and it showed me the contents, but it is just showing me the inside of a zip file without decompressing.

#### [Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654058):
oh yeah, Windows just opens them when you click on them :-/

#### [Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654067):
right click on it to uncompress it maybe

#### [Kevin Buzzard (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654076):
7-zip or winzip or something

#### [Mario Carneiro (Sep 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654118):
there is a "extract all" button in explorer when you open a zip file

#### [Kevin Buzzard (Sep 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654139):
are you good at computers?

#### [Kevin Buzzard (Sep 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654168):
Thanks :-)

#### [Mario Carneiro (Sep 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654173):
was that directed at me?

#### [Kevin Buzzard (Sep 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654212):
Someone with a mac and someone using linux on the other side of the world trying to figure out how to uncompress a file in Windows :-)

#### [Kevin Buzzard (Sep 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654216):
We just needed someone who was good at computers to come along

#### [Sean Leather (Sep 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134654358):
I recently looked at a Windows computer for the first time in a long time. I was surprised things had changed so much, and not in a good way. But, fortunately for my brother-in-law, I could still figure out how to clean up his task bar and make bookmarks in Edge.

#### [Scott Morrison (Sep 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134656364):
Ok, I unzipped on the terminal, eventually worked out the path to use for `lean.executablePath`, and it works

#### [Scott Morrison (Sep 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134656384):
It was about a 15 second delay watching a yellow bar before your `test.lean` finished.

#### [Scott Morrison (Sep 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134656436):
I'm not sure what that says about the `olean` files, however.

#### [Scott Morrison (Sep 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134656443):
I think this virtual machine is still set to only use one core.

#### [Kevin Buzzard (Sep 26 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134661897):
Doesnt VS code always take some time sorting stuff out when it starts up? What happens if you import analysis.real?

#### [Scott Morrison (Sep 26 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134670622):
I've just updated the mathlib documentation on using elan.

#### [Scott Morrison (Sep 26 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134670633):
Hopefully it is all correct, and works on ubuntu / macOS / windows 10.

#### [Scott Morrison (Sep 26 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134670715):
I probably ought to create brand new virtual machines for each and try them out once more...

#### [Scott Morrison (Sep 26 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134670733):
But I think once that PR gets merged, this may be a better set of starting instructions than Kevin's blog post.

#### [Scott Morrison (Sep 26 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134670755):
https://github.com/leanprover/mathlib/pull/371 if anyone wants to try it out.

#### [Patrick Massot (Sep 26 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134671180):
At the end of scenario 1, I read "If you want to play more, it's better to compile all your dependencies once and for all. You can do this by going into my_playground and running leanpkg build."  But this is already what is written in the previous paragraph. I guess this was meant to explain how to fully compile mathlib. For this I think you need to go to `_target/deps/mathlib` and run `lean --make` (or `leanpkg build`?)

#### [Reid Barton (Sep 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134672299):
Running `leanpkg build` inside the dependencies can cause lean to get confused, I recall. But I think `lean --make` in the dependencies is probably okay and recently I tried `lean --make _target/deps/mathlib` from the project directory and as far as I can tell it worked fine.

#### [Reid Barton (Sep 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134672323):
See https://github.com/leanprover/mathlib/issues/308 where this paragraph is discussed

#### [Reid Barton (Sep 26 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134672441):
I was hoping that some expert would come along and tell me whether my suggestion is OK, but at this point I guess I should just PR it

#### [Scott Morrison (Sep 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134674266):
This sounds good to me. `lean --make _target/deps/mathlib` works for me, and I think should be the canonical advice if you want the entire thing precompiled. I'm not convinced anyone should want that, but okay. :-)

#### [Patrick Massot (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134674305):
I want that. I don't want my workflow to break each time I add a new import in a Lean file

#### [Scott Morrison (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134674326):
okay!

#### [Scott Morrison (Sep 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134674581):
In other installation news, my PR to `vscode-lean` at <https://github.com/leanprover/vscode-lean/pull/91> seems to be working now on all operating systems, and means that the vscode extension will offer to install `elan` for you if it can't find a copy of Lean already.

#### [Scott Morrison (Sep 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134674626):
I think I now have 7 outstanding PRs across 3 repos. :-) Maybe I'll go do some maths for a while.

#### [Scott Morrison (Sep 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134706203):
And then there were 6!

#### [Scott Morrison (Sep 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134706204):
Thanks @**Sebastian Ullrich** for merging that. I think Gabriel is away still, but it would be great if you wanted to have a look at <https://github.com/leanprover/vscode-lean/pull/91>, my PR to vscode-lean which will automatically offer to install elan if it can't find Lean.

#### [Scott Morrison (Sep 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134706261):
If we can find a mechanism that is reliable, I think this will really soften the installation problem for beginners.

#### [Sebastian Ullrich (Sep 27 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134706807):
@**Scott Morrison|110087** Looks fine to me, but I'm not sure I want to find out how to do a vscode-lean release right now

#### [Sebastian Ullrich (Sep 27 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134706813):
You may want to tidy up the commit history a bit

#### [Scott Morrison (Sep 27 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134707882):
Will do, thanks. I'll wait to see what Gabriel says.

#### [Scott Morrison (Sep 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/134708057):
Okay, commit history fixed!

#### [Neil Strickland (Oct 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135676595):
The new procedure looks promising, but it does not work correctly when the user's home directory has spaces in (which is a common pattern, eg C:\Users\Neil Strickland).  Specifically, when trying to run leanpkg --help in a Git bash terminal embedded in VS Code, I see

```
'Strickland\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Neil:1:0: error: file 'C:\Users\Neil' not found
<unknown>:1:1: error: file 'C:\Users\Neil' not found
```

which indicates that something somewhere is using the path C:\Users\Neil Strickland\.elan\toolchains\stable\bin and not escaping it correctly.

This is a bit mysterious to me.  Running "which leanpkg" reports "/c/Users/Neil Strickland/.elan/bin/leanpkg".  Note that this is not the path that is causing trouble above.   I think that leanpkg is actually starting and producing the above error message.  However, looking at https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/main.lean suggests that "leanpkg --help" should always run correctly without needing to resolve any paths.  On the other hand, it is strange that /c/Users/Neil Strickland/.elan/bin/ contains four executables (lean.exe, elan.exe, leanpkg.exe and leanchecker.exe) which cmp tells me are byte-for-byte identical.  So probably that leanpkg.exe involves some kind of wrapper that is producing the error message.

I have not been able to work out where leanpkg is getting the bad path from.  I looked in various places under /c/Users/Neil Strickland/.elan and /c/Users/Neil Strickland/.vscode and /c/Users/Neil Strickland/AppData/Roaming/Visual Studio Code without success.  Running "env" under Git bash also does not enlighten me.

In general, the problem with spaces in paths in Lean seems to arise as follows.  The only Windows system call anywhere in the Lean code seems to be a CreateProcess() at line 221 of https://github.com/leanprover/lean/blob/master/src/library/process.cpp.  On lines 70,74,77 of https://github.com/leanprover/lean/blob/master/leanpkg/leanpkg/resolve.lean there are calls to exec_cmd which end up using the above system call to start Git.  This is probably appropriate, but the arguments should be escaped properly.  However, in various other places in resolve.lean and main.lean the functions exec_cmd and io.proc.spawn are used to create directories and check for the existence of files and directories.  These could again be fixed by escaping the arguments properly but it would be much more appropriate and robust to refactor the code to  use the system calls CreateDirectory() and PathFileExists() (and their POSIX equivalents) directly.

Probably some of the above commentary should be converted to issues on github.  But I am not yet properly familiar with how everything fits together.

#### [Reid Barton (Oct 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135676727):
The issue is in `leanpkg.bat`: https://github.com/leanprover/lean/pull/1976/files
I'm not sure whether just modifying your local copy will confuse elan, but it's worth a try

#### [Reid Barton (Oct 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135676741):
(There could be other issues, I suppose, but this is one known one.)

#### [Neil Strickland (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135677343):
I don't believe that that is correct.  Other methods of installing Lean give me a file leanpkg.bat which is a wrapper to the executable leanpkg.exe.  However, using elan via VS Code installs the lean executables in C:\Users\Neil Strickland\.elan\bin, and there is a leanpkg.exe there but no leanpkg.bat.  Moreover, leanpkg is invoked from Git bash which would ignore any .bat file anyway.  When starting Git bash inside VS Code in the obvious way, the environment variables LEANDIR, LIBDIR and LEAN_PATH are not set, but the PATH variable includes C:\Users\Neil Strickland\.elan\bin, and "which leanpkg" reports that that is where leanpkg is found.

#### [Bryan Gin-ge Chen (Oct 12 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135679736):
I'm pinging @**Scott Olson**, who wrote the patch to `leanpkg.bat` mentioned by Reid. Since he's already looked into this issue, he may be well-equipped to follow up on Neil's post above.

#### [Scott Olson (Oct 12 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135680103):
I made a PR at lean#1976. These errors are from `leanpkg.bat`:

```
'Strickland\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Neil:1:0: error: file 'C:\Users\Neil' not found
<unknown>:1:1: error: file 'C:\Users\Neil' not found
```

Specifically the first line comes from the `IF NOT EXIST` line and the latter two come from the `lean` line since it's getting passed

```
lean --run "C:\Users\Neil" "Strickland\.elan\toolchains\stable\bin\..\lib\lean\leanpkg\leanpkg\main.lean"
```

instead of

```
lean --run "C:\Users\Neil Strickland\.elan\toolchains\stable\bin\..\lib\lean\leanpkg\leanpkg\main.lean"
```

#### [Reid Barton (Oct 12 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135680368):
I think the `leanpkg` in `.elan/bin` (which is really elan itself) invokes `leanpkg` in (for example) `.elan/toolchains/3.4.1/bin/`, which should be `leanpkg.bat` on Windows. I would have to defer to someone who has a Windows machine though.

#### [Scott Olson (Oct 12 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135680439):
Oh yes, I looked into that before and Reid is correct. I forgot the step where elan has its own `leanpkg` wrapper binary.

#### [Scott Olson (Oct 12 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135680475):
I originally spent quite a while thinking elan's code contained the bug until I figured out it was invoking `leanpkg.bat`...

#### [Scott Olson (Oct 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135681462):
Also, for the curious, the elan binaries are not just byte-for-byte identical, but actually hardlinked:

```
C:\Users\Scott>fsutil hardlink list .elan\bin\leanpkg.exe
\Users\Scott\.elan\bin\lean.exe
\Users\Scott\.elan\bin\leanpkg.exe
\Users\Scott\.elan\bin\leanchecker.exe
\Users\Scott\.elan\bin\elan.exe
```

Meaning the filesystem only stores one file which these 4 paths all point to

#### [Neil Strickland (Oct 12 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135681602):
This seems to be correct: C:\Users\Neil Strickland\.elan\bin\leanpkg.exe invokes C:\Users\Neil Strickland\.elan\toolchains\*\leanpkg.bat via cmd.exe even when we start with Git bash, which is all pretty convoluted.  Editing leanpkg.bat by hand at least allows be to run leanpkg --help successfully.  I have not yet tried to do anything more useful.

#### [Scott Olson (Oct 12 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135681792):
`.elan\bin\leanpkg.exe` is just a normal windows program so it can invoke a .bat file regardless of being invoked from git bash or anything else

#### [Neil Strickland (Oct 12 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135682821):
Certainly it can; that doesn't mean that it should.  You probably need to call CreateProcess() to invoke leanpkg and if necessary you can supply the required environment variables as an argument to CreateProcess() as documented at https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa instead of going through leanpkg.bat.

#### [Scott Olson (Oct 12 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135682953):
elan could certainly invoke `lean` itself without going through `leanpkg.bat`, which we should probably do anyway because then it will work regardless of whether we get `leanpkg.bat` fixed, and for older versions

#### [Scott Olson (Oct 12 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135683106):
elan is written in Rust so we probably don't need to think about the exact Windows API calls, but it should be possible to make the wrapper invoke `lean` with the extra `--run <path to leanpkg>` args and the environment variables

#### [Scott Olson (Oct 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan on windows/near/135683846):
I posted an issue to the elan repo: https://github.com/Kha/elan/issues/16

