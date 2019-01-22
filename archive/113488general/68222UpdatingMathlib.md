---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68222UpdatingMathlib.html
---

## [general](index.html)
### [Updating Mathlib](68222UpdatingMathlib.html)

#### [Morenikeji Neri (Aug 10 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131239650):
I typed leanpkg upgrade on msys2 but my mathlib doesn't update. Help!

#### [Kevin Buzzard (Aug 10 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242157):
If you're trying it with the xena-UROP project, it's probably because I set it to track Mathlib 3.4.1, which is fixed. I thought it might make life easier if we were all singing from the same hymn-sheet, as it were.

#### [Chris Hughes (Aug 10 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242193):
Keji wants to use signatures of permutations, which has just been merged.

#### [Kevin Buzzard (Aug 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242302):
To be honest I'm not sure of a slick way of sorting this out. I am guessing Keji is using Lean 3.4.1. If he were to download the latest nightly, and then switch his msys2 so that when he typed `leanpkg` it used the latest nightly, then maybe this would fix it. I don't know if he can just edit `leanpkg.toml` to fix it.

#### [Kevin Buzzard (Aug 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242320):
I'm currently in an airport which is not really the most ideal place to be experimenting with this sort of thing.

#### [Mario Carneiro (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242470):
I think you can just specify your mathlib dependency to point to `"master"`

#### [Mario Carneiro (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242478):
in `leanpkg.toml`

#### [Kevin Buzzard (Aug 10 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131243629):
Keji I just edited `leanpkg.toml` following Mario's suggestion; try pulling the latest version of the repo (with `git pull` perhaps, if you have `git` working in msys2) and then try `leanpkg upgrade` again.

I must be honest -- I hadn't expected this to happen. I was envisaging people on the Xena summer project just playing around with basic stuff and nothing we needed getting PR'ed to mathlib. Really I just wanted to avoid having to spend hours showing people how to upgrade mathlib :-) We now run the risk that some of us will write code which will not run for others, but I guess in the long run most people have got Lean running on their laptops and it's in their interest to learn how to upgrade mathlib.

One could envisage a one-click solution to all of this for Windows users. An "upgrade mathlib" button which just requires someone to type in their github credentials (or perhaps not even that). For mac users it's often easier because they have a terminal pre-installed, and when they install git it might well end up in a directory which is already in their path.

#### [Mario Carneiro (Aug 10 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131243695):
you can't stop progress

#### [Kevin Buzzard (Aug 10 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131244304):
You said this back when I was pleading for mathlib 3.4.1, and as is usually the case I am now coming round to your way of thinking. It's not going to be so easy with CoCalc I suspect, but with my course running on CoCalc I really do think I want a frozen mathlib [famous last words]

#### [Chris Hughes (Aug 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131244397):
Keji tried updating it with `leanpkg upgrade`, but it just unupdated instead, and reverted to some old version.

#### [Kevin Buzzard (Aug 10 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131832343):
Did you pull or otherwise edit leanpkg.toml?

#### [Sebastian Ullrich (Aug 10 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131835840):
I don't think there is a way to tell leanpkg to track a different branch for a dependency yet

#### [Mario Carneiro (Aug 10 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131835920):
isn't the dependency item a git repo and a branch or commit hash?

#### [Sebastian Ullrich (Aug 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836124):
Yes, but `leanpkg upgrade` will still *track* the branch associated with the executed Lean version

#### [Sebastian Ullrich (Aug 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836139):
I.e. if you're running 3.4.1, `leanpkg upgrade` will always update to the head of `lean-3.4.1`

#### [Mario Carneiro (Aug 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836251):
so what does that branch info do?

#### [Sebastian Ullrich (Aug 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836614):
It points to the *currently used* commit, so it doesn't really make sense to store anything other than a commit hash or tag in that field. `leanpkg upgrade` ignores the field.

#### [Scott Morrison (Aug 11 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131852105):
Is it reasonable to be able to change this? I would really like to be able to track arbitrary branches of dependencies.

#### [Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753539):
I'm having trouble with the UROP repo.

#### [Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753573):
```
> leanpkg upgrade
error: override toolchain 'master' is not installed
info: caused by: the toolchain file at '/Users/scott/scratch/xena-UROP-2018/leanpkg.toml' specifies an uninstalled toolchain
```

#### [Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753575):
```
> elan toolchain list
stable (default)
nightly-2018-04-06
nightly-2018-04-20
nightly-2018-06-21
khoek-klean-3.4.2
khoek-klean-3.4.3
3.4.0
3.4.1
```

#### [Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753579):
@**Kevin Buzzard**, do you know what's going on?

#### [Kevin Buzzard (Aug 25 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753588):
I wouldn't trust our `leanpkg.toml` :-)

#### [Kevin Buzzard (Aug 25 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753632):
The last time I pulled the project, it had at least one `<<<<< .. ==== .. >>>>>`in it :-)

#### [Kevin Buzzard (Aug 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753645):
`leanpkg upgrade` just worked for me

#### [Kevin Buzzard (Aug 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753650):
```
WARNING: Lean version mismatch: installed version is nightly-2018-06-21, but package requires master
```

#### [Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753694):
I really wouldn't put `leanpkg upgrade` as part of your install instructions: https://github.com/ImperialCollegeLondon/xena-UROP-2018

#### [Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753696):
`leanpkg configure` is what you want

#### [Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753704):
(that doesn't touch your leanpkg.toml file, making it more likely it will survive multiple users)

#### [Kevin Buzzard (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753706):
Oh thanks. This was an attempt to get users to install mathlib in `_target`

#### [Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753708):
btw --- we need to make sure you update/replace your blog post on installing on Windows, to tell people to use `elan`.

#### [Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753719):
At Dagstuhl, Neil Strickland made a valiant effort to have someone show him how to install and prove the infinitude of primes in as many theorem provers as he could.

#### [Kevin Buzzard (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753724):
Neil just asked me to give a colloquium in Sheffield

#### [Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753725):
I really struggled helping him install Lean on his (windows) laptop.

#### [Kevin Buzzard (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753788):
You need a terminal and git, and you need to understand how your chosen terminal's path can be configured to globally remember where git and lean are installed

#### [Keeley Hoek (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753798):
I don't think 'master' could ever work with the latest version of elan
it has to be 'stable', 'nightly-xxx', or something on this list https://github.com/leanprover/lean/releases with the prefix "v" removed

#### [Kevin Buzzard (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753800):
Aah there's the problem then. I don't use `elan`

#### [Kevin Buzzard (Aug 25 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753842):
Thanks.

#### [Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753915):
Yeah --- we were definitely having problems with paths, and it wasn't helping that Neil had already tried and failed, so had left things affecting the paths.

#### [Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753920):
It also didn't help that his system had 3 different notions of "path", between windows, cygwin, and msys2.

#### [Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753924):
(He wanted to use cygwin, because that was the windows shell he was familiar with)

#### [Scott Morrison (Aug 25 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753969):
`elan` has a really big advantage here: it tries to take care of the paths for you, and I trust @**Sebastian Ullrich** to play with paths better than I trust users. :-)

#### [Johan Commelin (Aug 25 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753982):
Would Docker be an option for such showcasing purposes?

#### [Johan Commelin (Aug 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754022):
I hear that Docker also runs on Windows.

#### [Kevin Buzzard (Aug 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754025):
Here's a proposal for Windows users only: we make a "one size fits all" download. One zip file, that you put in `C:/Users/Neil` and then unpack, giving you a directory `C:/Users/Neil/leanstuff/`.

#### [Kevin Buzzard (Aug 25 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754042):
You then tell users to install VS Code, and then "open folder" the folder `C:/Users/Neil/leanstuff/sample_project/`, and to tell VS Code where the Lean binary is, which is `C:/Users/Neil/leanstuff/lean-3.4.2/bin/lean.exe`

#### [Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754045):
and then everything just works.

#### [Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754083):
No git, no command line, no nothing

#### [Johan Commelin (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754090):
Couldn't you even package VS code, with the right path setting, into that zipfile?

#### [Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754092):
and that's because the sample project directory has got a correct leanpkg.toml, and `_target/deps/mathlib` exists and has all the `.olean` files and everything

#### [Kevin Buzzard (Aug 25 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754100):
I have no idea about how Windows works and whether you can package a complicated thing like VS Code in a zip file

#### [Reid Barton (Aug 25 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755190):
I also don't know how Windows works or how Docker on Windows works but it sounds like something worth looking into.
The examples I've managed to find involve VS Code running inside Docker on a Linux virtual system, and connecting to an X window server running under Windows. That sounds ... workable, but a little awkward (you still have at least two pieces to download).

#### [Reid Barton (Aug 25 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755208):
Some links:
https://hub.docker.com/r/joengenduvel/docker-vscode/
http://blog.ctaggart.com/2016/05/visual-studio-code-served-from-docker.html
https://www.aaron-powell.com/posts/2017-09-21-vscode-linux-docker-windows/

#### [Reid Barton (Aug 25 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755429):
There's probably no advantage to putting VS Code in the Docker container, and requiring the end user to download an X server and the Lean/mathlib/VS Code container, over just using the native VS Code, and requiring the end user to download VS Code and the Lean/mathlib container. And there are almost certainly advantages to native VS Code over one running over X11.

#### [Reid Barton (Aug 25 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755441):
I do sort of like the idea of Windows users having Lean/mathlib/git/etc. running inside a Docker container, though, since it reduces the support surface area

#### [Reid Barton (Aug 25 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755483):
It might become a very large download though, not sure.

