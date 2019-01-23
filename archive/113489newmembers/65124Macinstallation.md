---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65124Macinstallation.html
---

## Stream: [new members](index.html)
### Topic: [Mac installation](65124Macinstallation.html)

---

#### [David Michael Roberts (Oct 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135389084):
I notice @**Scott Morrison|110087** put up a nice short video on getting required dependencies, VS Code and Lean installed on Mac, here: https://www.youtube.com/watch?v=k8U6YOK7c0M

#### [Kevin Buzzard (Oct 08 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135389378):
I also rewrote my cheap Windows installation page: https://xenaproject.wordpress.com/a-cheap-hack-to-get-lean-and-mathlib-running-on-a-windows-10-machine/ . I intend over the next day or two to make a link at the top of my blog pointing to various installation pages / posts, which are now randomly scattered online.

#### [Scott Morrison (Oct 08 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135391640):
I'm still going to make the corresponding video for installation on Windows!

#### [Kevin Buzzard (Oct 08 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135392629):
Be sure to ping me when you do. I am expecting this question to come up a fair bit at Imperial over the next few weeks

#### [Scott Morrison (Oct 09 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135441893):
Okay, the video for installing on Windows 10 is now up! https://www.youtube.com/watch?v=2f_9Zetekd8&feature=youtu.be

#### [Mario Carneiro (Oct 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135445219):
@**Kevin Buzzard** Would it be possible for you to write a page for mathlib that links to the various tutorials and videos for installing lean and/or mathlib?

#### [Kevin Buzzard (Oct 09 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135446958):
I will try to find the time today. On this thread we have Scott's two videos, there are my cheap and less cheap blog posts, there is some elan link somewhere... Is that it?

#### [Kevin Buzzard (Oct 09 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135446966):
There's the official instructions of course!

#### [Mario Carneiro (Oct 09 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135447815):
It would also be good to have follow on instructions for people who followed Scott's instructions and want mathlib

#### [Scott Morrison (Oct 09 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135448769):
Yes, I was thinking that's a separate video, that applies equally on Windows and macos, because it happens entirely within VS Code.

#### [Scott Morrison (Oct 09 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135448783):
(That's part of the reason for setting up a usable terminal on Windows, so afterwards everything can be done from VS Code.)

#### [Scott Morrison (Oct 09 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135448790):
(Although it occurs to me the Windows video should have included that one extra step, to hook up git bash as the default terminal instead of powershell.)

#### [Johan Commelin (Oct 09 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135451532):
@**Neil Strickland** This thread contains two videos with installation instructions. Kevin is also updating his instructions. Would you mind adding links to these videos etc on your MO post? I think you pointed out a very good issue (that installation was horribly difficult). I also hope that we are addressing them now. What do you think?

#### [David Michael Roberts (Oct 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135459174):
Maybe the windows video should go in its own topic, for ease of finding?

#### [Scott Morrison (Oct 09 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135460140):
Hopefully there will be permanent links to these soon from more prominent places...

#### [Kevin Buzzard (Oct 09 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135464799):
I am just going to have an "installing lean" link at the top of my blog with multiple options

#### [David Michael Roberts (Oct 10 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518661):
OK, so I have actually installed Lean and VS code as per @**Scott Morrison|110087** 's video, and now want to do some mathlibbing. But I am told by @**Kevin Buzzard** 's post https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/ that I probably am better off with the nightly build of lean, so that mathlib will have the latest and greatest stuff.  After following the instructions at that post:
```
leanpkg new my_project
cd my_project
leanpkg add https://github.com/leanprover/mathlib
leanpkg build
```
I get
```
davidroberts$ leanpkg build
configuring my_project 0.1
mathlib: trying to update _target/deps/mathlib to revision 905345a2ceaa5d0c7bc2f6310026961416b2cae4
> git checkout --detach 905345a2ceaa5d0c7bc2f6310026961416b2cae4    # in directory _target/deps/mathlib
HEAD is now at 905345a fix(data/array/lemmas,...): fix build
> lean --make src
```
and this was much much quicker than I thought it would be. Is it working or no?

#### [Scott Morrison (Oct 10 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518670):
It could well be.

#### [Scott Morrison (Oct 10 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518672):
leanpkg build, and lean --make src don't compile all of mathlib

#### [Scott Morrison (Oct 10 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518674):
They only compile those parts of it which are imported by some file in `src/`.

#### [Scott Morrison (Oct 10 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518675):
This might mean nothing at all at the moment.

#### [Scott Morrison (Oct 10 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518716):
Add a file under `src/` that imports, e.g. `data.nat.prime`.

#### [Scott Morrison (Oct 10 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518742):
*However*, what you did _still_ doesn't get you the latest and greatest version of mathlib.

#### [Scott Morrison (Oct 10 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518743):
:-(

#### [Scott Morrison (Oct 10 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518785):
If you look up that git commit hash you'll see it's from June 21.

#### [Scott Morrison (Oct 10 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518791):
This is because `leanpkg` is taking you to the latest commit on the `lean-3.4.1` branch, which for some reason (@**Mario Carneiro** ?) never gets updated?

#### [Scott Morrison (Oct 10 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518799):
(We _really_ need to fix this issue.)

#### [Mario Carneiro (Oct 10 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518803):
Don't blame me, Kevin wanted it to stay still

#### [Scott Morrison (Oct 10 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518805):
To get the actual latest version, you should edit your `leanpkg.toml` file.

#### [Mario Carneiro (Oct 10 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518808):
I guess it points to something like the earliest commit compatible with 3.4.1?

#### [Scott Morrison (Oct 10 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518868):
And replace the line `lean_version = ...` with `lean_version = "nightly-2018-08-23"`.

#### [Scott Morrison (Oct 10 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518879):
(I better make another video. :-)

#### [David Michael Roberts (Oct 10 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518883):
Aha, doing `leanpkg build` after adding a file to `src/`containing `import data.nat.prime` (plus an `#eval 2+2`) makes it do a lot more

#### [David Michael Roberts (Oct 10 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518898):
```quote
And replace the line `lean_version = ...` with `lean_version = "nightly-2018-08-23"`.
```
ah, ok! I'll do that once the current build has finished

#### [Scott Morrison (Oct 10 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518938):
I wonder if @**Kevin Buzzard** cares about where `lean-3.4.1` points, anymore.

#### [Scott Morrison (Oct 10 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518943):
If he doesn't, do you think we can keep it closer to master, @**Mario Carneiro** ?

#### [Mario Carneiro (Oct 10 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518945):
I guess, but how close?

#### [Scott Morrison (Oct 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518952):
As often as you can be bothered pushing it?

#### [Scott Morrison (Oct 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135518957):
Have a script that keeps it right up to master??

#### [David Michael Roberts (Oct 10 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519039):
Well, that's doing something.

#### [David Michael Roberts (Oct 10 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519041):
Question: why the nightly from the 21st of June?

#### [Scott Morrison (Oct 10 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519082):
Oh ...

#### [David Michael Roberts (Oct 10 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519097):
Is that the 'latest and greatest' version of mathlib?

#### [Scott Morrison (Oct 10 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519100):
No.

#### [Scott Morrison (Oct 10 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519113):
These nightlies are versions of *Lean*, not of mathlib.

#### [Scott Morrison (Oct 10 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519119):
mathlib changes most days!

#### [Scott Morrison (Oct 10 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519125):
I've just edited my instruction above. You should use `nightly-2018-08-23`.

#### [Scott Morrison (Oct 10 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519133):
(And maybe even edit your message above where you quoted me, so we can completely rewrite history. :-)

#### [David Michael Roberts (Oct 10 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519181):
Done!

#### [David Michael Roberts (Oct 10 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135519295):
I now have `nightly-2018-08-23`, thanks!

#### [Kevin Buzzard (Oct 10 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521818):
The "you're better off with the nightly build" comment was from when Lean 3.4 was changing a lot, and mathlib would change to keep up with Lean. This is all much less of an issue nowadays.

#### [Kevin Buzzard (Oct 10 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521864):
```quote
Don't blame me, Kevin wanted it to stay still
```
I wanted it to stay still between June and September. Thank you *very* much Mario for making it stay still over my summer project. I now really really don't want it to stay still any more for the simple reason that it is causing constant confusion amongst users.

#### [Kevin Buzzard (Oct 10 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521928):
Can we just delete the branch @**Mario Carneiro** or will this cause a new kind of confusion amongst users?

#### [Mario Carneiro (Oct 10 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521931):
No, it ties in to the way leanpkg works

#### [Mario Carneiro (Oct 10 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521933):
I think leanpkg gets even more confused if it's not there at all

#### [Kevin Buzzard (Oct 10 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521975):
I was fearing this. Can we get it to track master somehow?

#### [Mario Carneiro (Oct 10 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mac%20installation/near/135521976):
Does someone want to write a git hook so that when I commit to master lean-3.4.1 moves too?

