---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35331leanpkg.html
---

## Stream: [general](index.html)
### Topic: [leanpkg](35331leanpkg.html)

---

#### [Simon Hudon (Feb 27 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123021774):
It is possible to specify git branches in `leanpkg`?

#### [Mario Carneiro (Feb 27 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123022299):
```
[package]
name = "my_awesome_pkg"
version = "0.1"         # no semantic significance currently
lean_version = "3.3.0"  # optional, prints a warning on mismatch with Lean executable
path = "src"            # hard-coded, will be removed in the future
timeout = 100           # optional, passed to `lean` as `-T` parameter

[dependencies]
# local dependency
demopkg = { path = "relative/path/to/demopkg" }
# git dependency
mathlib =
  { git = "https://github.com/leanprover/mathlib",
    rev = "62f7883d937861b618ae8bd645ee16ec137dd0bd" }
```
You should be able to specify a branch using the `rev` field

#### [Simon Hudon (Feb 27 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123022372):
When doing that, I keep getting something saying that that revision is not a part of the tree. It's odd

#### [Simon Hudon (Feb 27 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123028434):
update: I managed to make it work. It might not be a leanpkg issue but I'm not sure. It seemed to be having a hard time cloning repositories for some reason. I wonder if it has anything to do that I wasn't pointing at the usual `mathlib` repo

#### [Sebastian Ullrich (Feb 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033857):
Can you reproduce it if you copy the toml to a fresh directory?

#### [Simon Hudon (Feb 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033928):
Actually, if you clone my repo, the problem should occur again:

```
git clone https://github.com/cipher1024/lean-pipes
```

#### [Simon Hudon (Feb 27 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033977):
Sorry, you asked for a naked toml file. Let's see

#### [Simon Hudon (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123034036):
So, yes the problem occurs even if the toml file is left on its own

#### [Sebastian Ullrich (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123034038):
Okay, I'll try your repo

#### [Sebastian Ullrich (Feb 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123086767):
I don't see your leanpkg.toml referencing a branch

#### [Simon Hudon (Feb 28 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123102397):
Here's the contents of `leanpkg.toml`:

```
[package]
name = "pipes"
version = "0.1"
lean_version = "master"
path = "src"

[dependencies]
mathlib = {git = "https://github.com/cipher1024/mathlib", rev = "ce8da6ab07a68dca1743bd7d8f9768157d644736"}
```

It is on my fork of `mathlib` and that commit is the head of my `coinductive-types` branch

#### [Reid Barton (Sep 22 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435061):
This is a really basic question, but what's the right way to start and maintain a new package that depends on mathlib?
I see mathlib's `leanpkg.toml` specifies `lean_version = "3.4.1"`, so I guess I should use Lean 3.4.1.
So let's say I run `elan run --install 3.4.1 leanpkg new my_project`, as recommended by https://github.com/leanprover/mathlib/blob/master/docs/elan.md. Now I get a new project whose `leanpkg.toml` also specifies `lean_version = "3.4.1"`.
Continuing to follow those directions, I run `leanpkg add leanprover/mathlib`. But now I end up with the `lean-3.4.1` branch of mathlib, which hasn't been updated since June 20. I wanted the latest version. And `leanpkg upgrade` makes no difference.

#### [Reid Barton (Sep 22 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435107):
Is this behavior intentional? At best, it's confusing if following the instructions in that elan.md file doesn't give you the latest version of mathlib, I think.

#### [Reid Barton (Sep 22 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435173):
Even though I should supposedly know how all of this works (e.g., I know there is a `lean-3.4.1` branch of mathlib and leanpkg will select it), I still get caught by surprise since starting a new project is so infrequent--I just made a new project and built mathlib in it and then a half hour later discovered I had the June 20 version which didn't have the new features I wanted to use.

#### [Kevin Buzzard (Sep 22 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435346):
I once thought that editing the toml file and changing 3.4.1 to "master" would fix this, but maybe the issue is that you are using 3.4.1's `leanpkg`?

#### [Reid Barton (Sep 22 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435466):
It probably would fix it, especially since I am using elan (although I'm not sure whether it is the version of leanpkg that matters, or what you write in the `lean_version` field of the toml file).
The elan.md instructions (I'm talking about "Scenario 1: Start a new package") suggest that you might see `nightly-2018-04-06` as the Lean version, and I found that `elan run --install nightly-2018-04-06 leanpkg new my_playground` does give you master mathlib, maybe because there is no branch corresponding to `nightly-2018-04-06`.
But it seems strange that the way to get mathlib master is to tell elan/leanpkg to use any other Lean version than the one actually used by mathlib...

#### [Reid Barton (Sep 22 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435506):
Presumably when those instructions were written, mathlib really did specify a version other than 3.4.1 and so the instructions worked

#### [Reid Barton (Sep 22 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435557):
By the way I should say explicitly that I'm assuming the current behavior is incorrect and I'm not supposed to get what appears to me to be this random version from June 20, but maybe others (like perhaps you Kevin) think it's working as intended because you want a fixed version for all your students.

#### [Kevin Buzzard (Sep 22 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436089):
That is all over now. I wanted a fixed version for my summer students just so I could see the advantages and the disadvantages. One of the advantages is that they don't ever have to update mathlib. What happened in practice was that people generally wanted more recent mathlib stuff and they learnt how to upgrade anyway, because sufficiently many of them knew how to use git because they were on a joint maths/computer science degree, so it worked out fine in the end and everyone was using different mathlibs anyway, and there didn't seem to be a problem.

#### [Reid Barton (Sep 22 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436346):
Okay, great. In that case I'm going to push for making it impossible to get this random old version of mathlib without asking for it, since I think that results in a potentially confusing experience for new users (e.g., one hears "mathlib has X" but then makes a project to try it out and X is missing).

#### [Reid Barton (Sep 22 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436566):
Moved discussion to github: #365

#### [Reid Barton (Sep 22 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436567):
Dang that's not a link to a mathlib issue.

#### [Reid Barton (Sep 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436607):
https://github.com/leanprover/mathlib/issues/365

#### [Scott Morrison (Sep 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134456778):
I think this is a really good idea. I've been confused by this, too.

#### [Mario Carneiro (Sep 23 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457081):
I guess leanpkg and elan have been designed for reproducible builds, which is the popular option these days. Unfortunately the usual thing new lean/mathlib users want is master + master, which goes against this idea, and so the tools fight them on this.

#### [Mario Carneiro (Sep 23 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457122):
I guess you could say they are being "too smart for their own good"

#### [Simon Hudon (Sep 23 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457124):
Is this something a switch could fix?

#### [Mario Carneiro (Sep 23 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457132):
`elan` in particular should strive for setting up users with the latest everything unless the user specifically asks for an old version

#### [Reid Barton (Sep 23 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457135):
Well you still get reproducible builds because the mathlib commit hash is in the leanpkg.toml file. It's just a matter of where you want to start a new project.

#### [Mario Carneiro (Sep 23 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457182):
Does `elan` know that mathlib exists? Or does the default thing just get you lean on its own

#### [Reid Barton (Sep 23 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457187):
I'm definitely happy that I can still build my lean-homotopy-theory project against the version of mathlib specified in the file, otherwise I would have no idea how any of the proofs that broke when building against master were supposed to work :)

#### [Simon Hudon (Sep 23 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457228):
I think elan only gets you Lean and the lean version in your toml file selects the tag of mathlib

#### [Reid Barton (Sep 23 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457230):
elan doesn't know about mathlib. The process is `elan run --install 3.4.1 leanpkg new myproject`, `cd myproject`, `leanpkg add leanprover/mathlib`.

#### [Reid Barton (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457237):
Then `leanpkg` picks the 3.4.1 branch of mathlib because that is what is specified in the `leanpkg.toml` file that elan wrote. I think

#### [Reid Barton (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457238):
Sorry--that leanpkg wrote

#### [Mario Carneiro (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457240):
Right, and this is backwards since it says "get me the version of mathlib compatible with 3.4.1" rather than "get me the version of lean compatible with mathlib master"

#### [Reid Barton (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457298):
Yes, that is definitely a bit weird.

#### [Mario Carneiro (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457304):
I think you should be able to ask elan to target a particular version/branch of any lean project, not just lean itself

#### [Mario Carneiro (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457305):
and then it derives the lean version from the toml file of that project

#### [Reid Barton (Sep 23 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457403):
I think the current situation is a consequence of the fact that the "package manager" leanpkg is shipped/versioned with lean itself

#### [Reid Barton (Sep 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457445):
that is, only leanpkg (not elan) knows about packages at all, but in order to get (any) leanpkg, you first must choose a lean version

#### [Reid Barton (Sep 23 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457902):
I wonder how crazy it would be to just replace leanpkg with crate or some other language's tool

#### [Mario Carneiro (Sep 23 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458086):
Note that `elan` *is* some other language's tool (it is forked from Rust's `cargo`)

#### [Sebastian Ullrich (Sep 23 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458484):
> I think you should be able to ask elan to target a particular version/branch of any lean project, not just lean itself
> and then it derives the lean version from the toml file of that project

But that's exactly what it's doing :) . Check out a Lean project at some commit and elan sets up the right Lean version for you.
What you're asking for is for elan not to set up some existing project, but a _new_ project based on its intended _dependencies_, no? What I could imagine is a command `elan new` that works like `leanpkg new`, but also takes a list of initial dependencies and selects the new package's Lean version based on that

#### [Mario Carneiro (Sep 23 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458530):
That sounds good to me. Is it currently possible to write stuff in a file to get the equivalent of `elan new` using `elan`?

#### [Sebastian Ullrich (Sep 23 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458543):
Though that seems like much more work than documenting "active mathlib development is happening for Lean version $VERSION, so use `elan +$VERSION leanpkg new` if you want to use it"

#### [Mario Carneiro (Sep 23 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458597):
It also sounds like it might be possible for me to set up a "template" project that depends on mathlib but otherwise contains very little, as a target for users to download and make elan understand

#### [Mario Carneiro (Sep 23 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458609):
Is it possible for a project like this to target the master branch of mathlib?

#### [Mario Carneiro (Sep 23 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458660):
What does `elan +$VERSION leanpkg new` mean here? Do you mean `$VERSION = 3.4.1`?

#### [Mario Carneiro (Sep 23 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458663):
the really important part is being able to tell elan "get mathlib master" without having to specify a commit

#### [Mario Carneiro (Sep 23 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458711):
I'm fine with telling people to get 3.4.1, since it's basically going to stay that way until lean 4 and then everything will be different anyway, but mathlib won't stay still and elan has to be able to adapt to that

#### [Sebastian Ullrich (Sep 23 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458754):
Okay, that `leanpkg upgrade` doesn't allow you to customize which branch it uses is a related but separate issue (and specific to leanpkg, not elan)

#### [Mario Carneiro (Sep 23 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458814):
So what is the current recommendation? Do users need to go into `_target/deps/mathlib` and checkout master?

#### [Sebastian Ullrich (Sep 23 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458817):
I guess we can agree that leanpkg using a separate branch per Lean version was a good idea but didn't work out in practice, since nobody wants to maintain code for multiple Lean versions. We could definitely change that in Lean 4, ie. when development on leanpkg continues

#### [Mario Carneiro (Sep 23 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458860):
The problem isn't maintaining multiple lean versions, it's not allowing other kinds of branches

#### [Mario Carneiro (Sep 23 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458870):
in particular master branches, which are going to be, ehm, rather common

#### [Sebastian Ullrich (Sep 23 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458974):
If you use the master branch for development against a Lean version that is not master, it does look like you don't agree with leanpkg at all how branches should be handled

#### [Sebastian Ullrich (Sep 23 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458994):
Given the current leanpkg, the only real solution would be to rename the master branch to `lean-3.4.1`. If we don't want that, we'll have to change leanpkg... at some point

#### [Reid Barton (Sep 23 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459118):
Is deleting the `lean-3.4.1` branch not a solution, or merely not a "real solution"?

#### [Sebastian Ullrich (Sep 23 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459128):
Then `leanpkg upgrade` will simply do nothing except complain, afaik

#### [Reid Barton (Sep 23 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459129):
When Lean 4 arrives we will be able to modify leanpkg at the same time, so is it reasonable to assume for now that there is only one version of Lean in existence?

#### [Reid Barton (Sep 23 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459132):
Hmm, let me try.

#### [Sebastian Ullrich (Sep 23 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459171):
https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/leanpkg/leanpkg/git.lean#L10-L14

#### [Reid Barton (Sep 23 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459228):
I have a toy project here using `nightly-2018-04-06` and I changed the mathlib commit to an older version and ran leanpkg configure and verified that it checked out the old version. Then I ran `leanpkg upgrade` and it successfully upgraded to mathlib master:
```
rwbarton@bridge:~/lean/my_playground2$ leanpkg upgrade
mathlib: trying to update _target/deps/mathlib to revision f53c776c2e09eff5358c5de6902e402c641a1673
> git checkout --detach f53c776c2e09eff5358c5de6902e402c641a1673    # in directory _target/deps/mathlib
HEAD is now at f53c776... feat(analysis/topology): pi-spaces: topolopgy generation, prove second countability
configuring my_playground2 0.1
mathlib: trying to update _target/deps/mathlib to revision ca7f118058342a2f077e836e643d26e0ad1f3ca6
> git checkout --detach ca7f118058342a2f077e836e643d26e0ad1f3ca6    # in directory _target/deps/mathlib
Previous HEAD position was f53c776... feat(analysis/topology): pi-spaces: topolopgy generation, prove second countability
HEAD is now at ca7f118... fix(docs/tactics.md): missing backquote, formatting
rwbarton@bridge:~/lean/my_playground2$ echo $?
0
rwbarton@bridge:~/lean/my_playground2$ cat leanpkg.toml
[package]
name = "my_playground2"
version = "0.1"
lean_version = "nightly-2018-04-06"
path = "src"

[dependencies]
mathlib = {git = "https://github.com/leanprover/mathlib", rev = "ca7f118058342a2f077e836e643d26e0ad1f3ca6"}
```

#### [Reid Barton (Sep 23 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459230):
Is that something special about using nightly lean vs a stable version number?

#### [Sebastian Ullrich (Sep 23 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459253):
Yes, see the link above

#### [Reid Barton (Sep 23 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459273):
Ah...

#### [Sebastian Ullrich (Sep 23 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459287):
```quote
When Lean 4 arrives we will be able to modify leanpkg at the same time, so is it reasonable to assume for now that there is only one version of Lean in existence?
```

I suppose that is a reasonable assumption right now. Even if we don't change the leanpkg semantics, it will just work if Lean 4 porting efforts happen on the mathlib master branch and development for Lean 3 on the `lean-3.4.1` branch

#### [Mario Carneiro (Sep 23 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459337):
> If you use the master branch for development against a Lean version that is not master, it does look like you don't agree with leanpkg at all how branches should be handled

I think the master branch of lean is basically 3.4.1, so if this is what is needed then I'm okay with it. How do I sign up?

#### [Reid Barton (Sep 23 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459715):
So before I incorrectly "realized" that we could just delete the lean-3.4.1 branch, options I was considering were:
* Development happens on the lean-3.4.1 branch, not master. (You can set lean-3.4.1 as the "default" branch in the github UI to help with this--I did it for https://github.com/rwbarton/lean-homotopy-theory. But I don't know whether changing this for an existing project like mathlib with many forks would have some ramifications.)
* There are some obscure git features like `git symbolic-ref` which might allow us to make lean-3.4.1 an alias to master, but it's not clear whether they would really work for us or whether they can be configured through github.
* We could try to keep lean-3.4.1 up to date with master by some technical or semi-technical means (like a pre-push hook for mathlib committers--there are few enough of them that it should be feasible).

#### [Kevin Buzzard (Sep 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469763):
Why don't people use the latest lean nightly? It's 3.4.1 with some broken stuff fixed.

#### [Kevin Buzzard (Sep 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469804):
6th April, 20th April -- why? I use the June version

#### [Bryan Gin-ge Chen (Sep 23 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469964):
Actually, there's an August version out now...

#### [Mario Carneiro (Sep 23 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134470067):
The fixes aren't so important to me. More important is whether switching back to nightlies will improve or exacerbate the `leanpkg` situation

#### [Mario Carneiro (Sep 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134470078):
Is Kevin's blog post still the best option for installing lean + mathlib on windows?

#### [Scott Morrison (Sep 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472306):
As far as I can tell. We really need something like elan for windows.

#### [Olli (Sep 23 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472811):
elan works fine on Windows

#### [Olli (Sep 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472866):
the Windows specific issue I and a few others seem to run into is leanpkg failing with "failed to start child process", for which I have found no solution for

#### [Bryan Gin-ge Chen (Sep 23 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134473291):
For which subcommands and under what precise circumstances does leanpkg fail on your machine? Does it output anything else?

#### [Olli (Sep 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474398):
any command that has to do with creating a project, adding dependencies etc. here is an example, where I have modified the leanpkg script (i.e. leanpkg.bat on Windows) to ignore the `@ECHO OFF` directive so that the commands getting ran are printed:

```
PS C:\Users\Olli\Dev\Lean> leanpkg new playground

C:\Users\Olli\Dev\Lean>SET LEANDIR=C:\Users\Olli\.elan\toolchains\stable\bin\../

C:\Users\Olli\Dev\Lean>SET LIBDIR=C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean

C:\Users\Olli\Dev\Lean>IF NOT EXIST C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean SET LIBDIR=C:\Users\Olli\.ela
n\toolchains\stable\bin\../

C:\Users\Olli\Dev\Lean>SET LEAN_PATH=C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\library;C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg

C:\Users\Olli\Dev\Lean>SET PATH=C:\Users\Olli\.elan\toolchains\stable\bin\../\bin;C:\Users\Olli\.elan\bin;C:\Users\Olli\.elan\toolchains\stable\bin;C:\Users\Olli\lean-3.4.1-windows\bin;;C:\Users\Olli\AppData\Local\Programs\Microsoft VS Code\bin

C:\Users\Olli\Dev\Lean>lean --run C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg\leanpkg\main.lean new playground
failed to start child process
PS C:\Users\Olli\Dev\Lean>
```

I also tried modifying the script to get rid of the funny looking `\../` part of the path, but I get the same result

#### [Olli (Sep 23 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474483):
This is what I have installed:
```
PS C:\Users\Olli\Dev\Lean> lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
PS C:\Users\Olli\Dev\Lean> elan --version
elan 0.7.0 (0dd8c5ce4 2018-09-16)
```

#### [Keeley Hoek (Sep 23 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474485):
At your terminal what happens if you type `test -f foo`

#### [Olli (Sep 23 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474491):
this is PowerShell, so there is no such command

#### [Olli (Sep 23 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474530):
what are we trying to find out?

#### [Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474536):
this is precisely the problem!

#### [Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474537):
(and maybe other things)

#### [Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474539):
`leanpkg` attempts to spawn `test` when it runs, and it fails, so you see that message

#### [Olli (Sep 23 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474605):
ah I see, so if I installed a version of that utility compiled for Windows, then that might be a workaround?

#### [Keeley Hoek (Sep 23 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474648):
If you'd be willing to help diagnose, try opening `C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg\leanpkg\main.lean` in a text editor, and navigate to line `199`. You should see a line:
````
  ex ← exists_file user_toml_fn,
````
Try replacing that line with
````
 let ex := tt,
````
Does your command before work then?

#### [Keeley Hoek (Sep 23 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474660):
Yes I suppose having a unix-like environment with coreutils would work, but it really shouldn't be necessary. `leanpkg` should be better
If this works for you I can get you a less dodgy solution cooked up in a second, since you're using elan

#### [Keeley Hoek (Sep 23 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474704):
Actually my line number is wrong.... But I still mean that line I quoted

#### [Keeley Hoek (Sep 23 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474705):
Should be line `196`

#### [Olli (Sep 23 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474757):
Like this?
```lean
  let user_toml_fn := dot_lean_dir ++ "/" ++ leanpkg_toml_fn,
  ex := tt,
  when (¬ ex) $ write_manifest {
      name := "_user_local_packages",
      version := "1"
    } user_toml_fn,
```
I get:
```
C:\Users\Olli\.elan\toolchains\stable\lib\lean\leanpkg\leanpkg\main.lean:182:4: error: non-exhaustive match, the followi
ng cases are missing:
main "configure" list.nil ({data := _} :: _)
main "configure" ({data := _} :: _) _
main "new" list.nil _
main "new" [_] ({data := _} :: _)
main "new" (_ :: {data := _} :: _) _
main "init" list.nil _
main "init" [_] ({data := _} :: _)
main "init" (_ :: {data := _} :: _) _
main "add" list.nil _
main "add" [_] ({data := _} :: _)
main "add" (_ :: {data := _} :: _) _
main "upgrade" list.nil ({data := _} :: _)
main "upgrade" ({data := _} :: _) _
main "install" list.nil _
main "install" [_] ({data := _} :: _)
main "install" (_ :: {data := _} :: _) _
main _ _ _
C:\Users\Olli\.elan\toolchains\stable\lib\lean\leanpkg\leanpkg\main.lean:196:5: error: command expected
failed to start child process
```

#### [Keeley Hoek (Sep 23 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474819):
you need a `let` in front of the `ex`, but I'm reading more now and this won't solve your problem :(( (it will still be the same)
`leanpkg` wants `test` and (unix) `mkdir`

#### [Keeley Hoek (Sep 23 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474837):
I should be able to cook something up which does help you, though! Let me dig in a for a sec

#### [Olli (Sep 23 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475008):
thanks, yeah I now see what the issue is, I have been meaning to install Lean in WSL but so far haven't had any need to use libraries yet so I didn't get around to it

#### [Keeley Hoek (Sep 23 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475208):
Yeah there are very many pieces which assume a unix-y environment, even just down to the directory separator character
Setting something like WSL up sounds like your best bet :)

#### [Keeley Hoek (Sep 23 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475210):
(at the moment)

#### [Olli (Sep 23 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475526):
if making leanpkg natively support Windows is too tall of a task, I would say the next best thing would be improving the error messages for this particular situation

#### [Keeley Hoek (Sep 23 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475862):
I didn't write it, but the comments in there make sure to say the intention was to add windows support later
I didn't realise that it was just broken on windows

I might try to make a version that runs natively later this week

#### [Andrew Ashworth (Sep 23 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477434):
don't all the lean installation instructions assume a mingw installation?

#### [Olli (Sep 23 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477522):
I do have MinGW installed, but that does not include `test` which is not an executable but rather a shell built-in as far as I can tell

#### [Andrew Ashworth (Sep 23 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477633):
ahh. I never noticed this issue, because a bash shell is required to compile lean

#### [Keeley Hoek (Sep 23 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477915):
So I have no idea about MinGW anything, but for what its worth I've built coreutils before and it has a `test` binary
Idk if it's in MinGW though

#### [Reid Barton (Sep 23 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477924):
Yeah, on a normal unix system, `test` is both a shell built-in (for speed) and an executable

#### [Reid Barton (Sep 23 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477978):
I don't know how POSIX-like the MinGW shell is, but you can try `which test` or `command test` (if nothing happens, it worked)

#### [Olli (Sep 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478025):
it's not included with the installation of MinGW that I have, and I've tried googling if I can download it separately from somewhere but unfortunately `test` is a rather tricky name when it comes to search engines

#### [Reid Barton (Sep 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478027):
Yes, I found that as well...

#### [Keeley Hoek (Sep 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478030):
does MinGW ship with a shell?

#### [Reid Barton (Sep 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478035):
Are you using MSYS?

#### [Olli (Sep 23 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478074):
yes

#### [Keeley Hoek (Sep 23 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478075):
doesn't msys have bash?

#### [Olli (Sep 23 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478088):
yes it does, I will try that next

#### [Reid Barton (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478095):
The question is whether it has `/usr/bin/test` though, right?

#### [Keeley Hoek (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478136):
I'd be blown away if it didn't!

#### [Reid Barton (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478138):
Well, yeah...

#### [Olli (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478194):
```
PS C:\MSYS\1.0\bin> ./bash.exe
bash.exe"-3.1$ which test
which: test: unknown command
bash.exe"-3.1$ exit
```

#### [Keeley Hoek (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478200):
classic!

#### [Olli (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478206):
Git bash for windows has it

#### [Olli (Sep 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478228):
and there it does work as expected

#### [Reid Barton (Sep 23 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478294):
I have no idea whether this is useful, but I did find through Google some log https://gist.github.com/choco-bot/eec2966667c148959f417ca93995222e#file-install-txt-L523 where it installs something called `msys2-base-x86_64-20180531.tar` and on line 1054 it installs a certain `test.exe`

#### [Keeley Hoek (Sep 23 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478303):
a few windows people here seem to use MSYS2, maybe its less insane! (I dare say that's why they have been oblivious to these issues on windows)

#### [Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478459):
you can't just run bash exe

#### [Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478460):
the mingw bash script sets a bunch of environment variables

#### [Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478461):
also, I use MSYS2 with no issues

#### [Olli (Sep 23 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478505):
I see, yeah I will try installing MSYS2, and I just confirmed that I was able to add mathlib to a new project and it appears to work fine from VSCode which is good

#### [Reid Barton (Sep 23 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134482297):
@**Olli**, so is your conclusion that leanpkg is not compatible with MSYS, but is compatible with MSYS2?

#### [Olli (Sep 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134482841):
@**Reid Barton** yes that appears to be correct

#### [Olli (Sep 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134483308):
MSYS2 contains `test.exe`

#### [Bryan Gin-ge Chen (Sep 23 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134485601):
Is it also true that using the git-for-windows bash shell also works for you? I don't think I have msys2 on my windows 10 machine and I got leanpkg working there.

#### [Olli (Sep 23 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134486944):
yes, I should probably have tried that first, but had totally forgot I even had it installed

#### [Bryan Gin-ge Chen (Sep 23 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487071):
That's great, thanks for being so patient and looking into it. Now we should look into editing these solutions into the various docs that are floating around out there...

#### [Mario Carneiro (Sep 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487567):
I don't think git bash is fully usable for lean, although I forget why. I made some attempts to do this when I started and some necessary packages were missing with no clear way to get them

#### [Mario Carneiro (Sep 23 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487588):
Certainly CMD and powershell won't work

#### [Mario Carneiro (Sep 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487622):
I haven't tested Cygwin extensively, but it has its own issues to deal with and I found MSYS2 much easier

#### [Mario Carneiro (Sep 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487642):
I'd be curious to see if anyone makes lean work with WSL

#### [Bryan Gin-ge Chen (Sep 23 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487844):
I've been using git bash up to now and haven't noticed anything wrong, but all I'm doing with regards to lean is just running `leanpkg upgrade` and `leanpkg build` occasionally. I did have to mess around with my console program to get unicode characters to print properly though.

#### [Scott Morrison (Oct 25 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440118):
Hi @**Reid Barton**, did you ever sort this out? Can we just delete the `lean-3.4.1` branch of `mathlib`? I see that Mario has been occasionally updating, but it still requires manual intervention.

#### [Reid Barton (Oct 25 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440150):
No, we can't just delete it unfortunately--leanpkg requires a branch matching the lean version to exist, when that version is a stable version

#### [Reid Barton (Oct 25 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440338):
I think the best "solution" we have for now is for somebody to figure out how to write a git hook that Mario can use to update the branch head automatically

#### [Neil Strickland (Jan 18 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156376118):
I am also using git bash without obvious problems.  I have msys2 installed but it is not in the path so that should not make a difference.
@**Bryan Gin-ge Chen** , what did you do to fix the unicode?

#### [Bryan Gin-ge Chen (Jan 18 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156376424):
For me it was an issue with a setting in my console program, [`cmder`](http://cmder.net/) which seems to be a reskin or repackaging of [`conemu`](https://conemu.github.io/). I had to add the setting `chcp utf8` to the environment per [this page](https://conemu.github.io/en/UnicodeSupport.html).

#### [Neil Strickland (Jan 18 2019 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156378147):
Thanks.  That suggestion doesn't seem immediately applicable to me as I am just using git bash in vscode (and git bash outside vscode seems to handle unicode correctly).  I poked around a bit more and found this page https://github.com/Microsoft/vscode/issues/60330, but the suggestions there seemed to have no effect.  I'll probably just leave it now as it is not really causing me any trouble, it's just untidy.

