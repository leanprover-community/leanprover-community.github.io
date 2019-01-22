---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10725startupspeed.html
---

## [new members](index.html)
### [startup speed](10725startupspeed.html)

#### [Scott Olson (Sep 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895169):
Is it normal for Lean to take several minutes to catch up when I freshly open my project in VSCode, even if I've completely precompiled the mathlib dependency to .olean files?

#### [Scott Olson (Sep 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895228):
Maybe not several minutes, but at least around 1 minute

#### [Scott Olson (Sep 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895274):
And once it's caught up it seems to spend a significant amount of time after that "checking import for sorry" every time

#### [Reid Barton (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895497):
I use emacs but it doesn't sound normal. How did you build the mathlib dependency?

#### [Reid Barton (Sep 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895503):
`leanpkg build` in your project should help. `leanpkg build` inside `_target/deps/mathlib` will confuse lean and lead to this kind of behavior

#### [Scott Olson (Sep 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895598):
Oh, interesting. I ended up doing the latter because the former wouldn't actually build mathlib at all

#### [Scott Olson (Sep 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895605):
So I probably need to go back and debug what caused the original problem instead

#### [Patrick Massot (Sep 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895650):
If you really want to make sure all of mathlib is built, even the pieces not currently needed in your project, you need do do `lean --make` inside `_targets/deps/mathlib`, not `leanpkg build`

#### [Reid Barton (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895692):
The original problem is just that lean is "smart" and only compiles the parts of the dependencies that are actually needed--which is annoying if that subset might increase in the future and you'd rather just build it once and be done with it.

#### [Scott Olson (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895694):
I thought it might be something like that but I wasn't sure how to get around it, thanks!

#### [Scott Olson (Sep 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895704):
Do I need to "undo" the `leanpkg build` I did inside `_target/deps/mathlib` somehow, or just run the correct command now?

#### [Patrick Massot (Sep 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895755):
running the correct command should be enough

#### [Scott Olson (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895905):
How exactly does Lean get confused here - do the .olean files mark themselves in some way, so that my project would not recognize the .olean files I previously built as its own? I'm scanning for hidden files or some other way it would possibly distinguish and finding nothing so far

#### [Kevin Buzzard (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895906):
What OS are you using?

#### [Scott Olson (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895907):
Windows 10

#### [Scott Olson (Sep 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895909):
I run linux as well but haven't checked if I get the same behavior there yet

#### [Kevin Buzzard (Sep 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895949):
Sebastian was saying the other day that sometimes Windows, or maybe some standard anti-virus, goes through the files and maybe randomly touches them messing up "last updated" times. I think Lean tries to recompile an olean file if it thinks that the lean file was modified after the olean file was built, and maybe it gets confused on Windows? I don't use this OS though and this is all second hand.

#### [Reid Barton (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895956):
I think it has something to do with the `leanpkg.path` file, but I don't know exactly what

#### [Scott Olson (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895957):
I'll keep an eye on the last updated times

#### [Kevin Buzzard (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895958):
Sebastian was saying this in an attempt to explain why `leanpkg` regularly takes 10 seconds to start running on windows

#### [Kevin Buzzard (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895959):
despite core lean shipping with the olean files

#### [Kevin Buzzard (Sep 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896009):
(leanpkg is written in lean)

#### [Scott Olson (Sep 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896015):
I haven't had that trouble with `leanpkg` startup times. I installed it via `elan` if it makes a difference

#### [Scott Olson (Sep 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896024):
but perhaps I just don't have an AV that causes that specific problem

#### [Scott Olson (Sep 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896067):
I can confirm `leanpkg build` in the correct directory solved the problem for me, thanks all

#### [Scott Olson (Sep 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896070):
My problem before was misinterpreting the docs I was reading and assuming it would build all of mathlib, but I was running it before adding any imports so it actually built none of it

#### [Scott Olson (Sep 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896197):
Incidentally this solved another problem I had where VSCode's lean.exe would rise to over 2GiB of RAM during the initial build and never drop back down. Apparently it doesn't get as high when the precompiled stuff is available

#### [Reid Barton (Sep 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896408):
Oh--does your `mathlib` dependency specify a different version of lean than your top-level project, by any chance?

#### [Scott Olson (Sep 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896991):
Oh yeah, that would probably cause the .olean incompatibility by itself. `mathlib`'s toml says `3.4.1` but I'm using a recently nightly in my project, because if I used `3.4.1` it checks out the `lean-3.4.1` branch of `mathlib` and I wanted `master`

#### [Scott Olson (Sep 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897030):
This is probably a problem for even running `lean --make` inside the mathlib dir, right?

#### [Scott Olson (Sep 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897132):
I did just run `lean --make` earlier and we can see the olean version difference:

```
$ head -c 60 src/regular.olean | xxd
00000000: 6f6c 6561 6e66 696c 6500 332e 342e 322c  oleanfile.3.4.2,
00000010: 206e 6967 6874 6c79 2d32 3031 382d 3038   nightly-2018-08
00000020: 2d32 332c 2063 6f6d 6d69 7420 6231 3361  -23, commit b13a
00000030: 6331 3237 6664 3833 00ff d828            c127fd83...(

$ head -c 60 _target/deps/mathlib/data/nat/basic.olean | xxd
00000000: 6f6c 6561 6e66 696c 6500 332e 342e 312c  oleanfile.3.4.1,
00000010: 2063 6f6d 6d69 7420 3137 6665 3364 6563   commit 17fe3dec
00000020: 6166 3861 00ff f2e4 59f1 0004 0002 696e  af8a....Y.....in
00000030: 6974 0000 0402 6c6f 6769 6300            it....logic.
```

#### [Reid Barton (Sep 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897190):
```quote
This is probably a problem for even running `lean --make` inside the mathlib dir, right?
```
Yes if you already ran `leanpkg build` which created the `leanpkg.path` file there.

#### [Reid Barton (Sep 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897191):
Or wait.

#### [Reid Barton (Sep 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897226):
Actually I guess it is a question of elan.

#### [Scott Olson (Sep 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897231):
Yeah, `elan` will automatically download and build with whatever version the toml specifies

#### [Scott Olson (Sep 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897241):
I can probably do the mathlib dir manual `lean --make` by telling elan which specific version to build with, which seems fair to me for an optional manual step

#### [Reid Barton (Sep 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897242):
I guess the `lean --make _target/deps/mathlib` instructions are safer in this particular situation then, assuming that elan uses the current working directory to start its search for the toml file

#### [Scott Olson (Sep 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897282):
Ah yeah I should double check what it does in that case

#### [Scott Olson (Sep 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897291):
I gotta say it's rather convenient for me coming from Rust that `elan` is based on `rustup` because I have a pretty good grasp on exactly how it works already =)

#### [Scott Olson (Sep 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897501):
@**Reid Barton** You're right, using `lean --make _target/deps/mathlib` is the simplest/safest way to make sure it builds the whole thing with your current project's Lean version

