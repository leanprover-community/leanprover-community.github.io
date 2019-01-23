---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99769importingwithinleanpackage.html
---

## Stream: [general](index.html)
### Topic: [importing within lean package](99769importingwithinleanpackage.html)

---

#### [Chris Hughes (Mar 24 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161392):
So I've tried to download @**Kenny Lau** and @**Kevin Buzzard**'s stacks project library, but none of the imports are currently working, I get the following message
```lean
invalid import: Kenny_comm_alg.avoid_powers
could not resolve import: Kenny_comm_alg.avoid_powers
```
I tried using both `leanpkg install` and `leanpkg add` to download the library, but both have this problem. I'm on windows. Can anyone help?

#### [Simon Hudon (Mar 24 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161439):
did you do `leanpkg init my_project` on your directory?

#### [Chris Hughes (Mar 24 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161491):
Which directory?

#### [Kevin Buzzard (Mar 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161548):
Chris : try the "open folder" option in VS Code. Open the project root as a folder.

#### [Kevin Buzzard (Mar 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161550):
Let me know if it doesn't work. I'll add it to the README if it does.

#### [Kevin Buzzard (Mar 24 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161592):
That should make the import directories all point to the right places

#### [Kevin Buzzard (Mar 24 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161648):
and then I would have suggested "leanpkg upgrade" or "leanpkg build" -- oh -- I see -- this doesn't work because Chris won't have any leanpkg.path file in his clone?

#### [Chris Hughes (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161656):
I don't have a leanpkg path

#### [Kevin Buzzard (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161663):
Chris -- I have a _target directoy that you don't have because my gitignore file tells git not to upload my _target directory to github

#### [Kevin Buzzard (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161669):
so you'll need one of those

#### [Chris Hughes (Mar 24 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161670):
But I should be able to build it, I can build mathlib, and that's the same.

#### [Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161708):
Mathlib has no dependencies.

#### [Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161719):
Our project depends on other projects so it's a bit different.

#### [Chris Hughes (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161721):
It downloaded all the dependecncies automatically. Trouble is they don't compile.

#### [Kevin Buzzard (Mar 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161722):
I'm not sure that's a problem

#### [Kevin Buzzard (Mar 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161723):
As long as mathlib compiles

#### [Chris Hughes (Mar 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161730):
And my computer's too slow to make compiling when I import practical.

#### [Simon Hudon (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161772):
If you want we can start from scratch.

#### [Chris Hughes (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161774):
It's a problem because it crashes everything

#### [Kevin Buzzard (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161775):
You should be able to get it to work. Kenny got it to work

#### [Chris Hughes (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161776):
And I doubt mathlib compileseither, since it depends on an old version

#### [Kevin Buzzard (Mar 24 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161777):
and he was in exactly the same situation as you -- it wasn't his project and he had to clone from github

#### [Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161783):
type leanpkg upgrade

#### [Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161784):
This should get the correct versions of everything

#### [Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161785):
and then leanpkg build and leave it on overnight

#### [Kevin Buzzard (Mar 24 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161786):
or however long it takes

#### [Chris Hughes (Mar 24 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161828):
If there are errors, leaving it overnight doesn't help

#### [Kevin Buzzard (Mar 24 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161882):
You're right, it's not working for me.

#### [Kevin Buzzard (Mar 24 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161884):
I'll try and figure out what's going on.

#### [Kevin Buzzard (Mar 24 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161894):
Do you have the latest Lean?

#### [Chris Hughes (Mar 24 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124161939):
The latest lean doesn't compile. I have four day old lean.

#### [Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162170):
OK so I just tried compiling my project using lean from the linux nightly (commit 28f4143be31b) and my project did not compile.

#### [Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162172):
The first error is this:

#### [Kevin Buzzard (Mar 24 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162175):
```
/home/buzzard/temp/lean-stacks-project/_target/deps/mathlib/data/option.lean:24:1: error: failed to synthesize type class instance for
α : Type u
⊢ is_lawful_monad option
```

#### [Kevin Buzzard (Mar 24 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162215):
and there was some talk about lawful monads recently so maybe there was some change

#### [Chris Hughes (Mar 24 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162284):
If you just find a version it works with, I'll download that.

#### [Simon Hudon (Mar 24 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162337):
I believe mathlib doesn't build with the latest nightly. I worked with revision `07bb7d809b6be49f38ce4e427c54a82708ae281f ` of Lean

#### [Simon Hudon (Mar 24 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162345):
And I use `4ceb545f7e07431263e1131a9c9524a28de99472` for mathlib

#### [Chris Hughes (Mar 24 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162409):
I have made some progress. It now gets stuck at importing, because nothing's compiled instead of not finding the file it's meant to import.

#### [Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162420):
I am downloading lean HEAD. It's three days old and it would not surprise me if ever-efficient Mario had made mathlib work with it.

#### [Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162461):
Chris are you able to compile Lean from source?

#### [Kevin Buzzard (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162464):
https://github.com/leanprover/lean/blob/master/doc/make/msys2.md

#### [Simon Hudon (Mar 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162465):
If you check travis, you'll see that it doesn't work with HEAD

#### [Chris Hughes (Mar 24 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162471):
Probably not with the current version, since it says build failing. Maybe with a previous version.

#### [Chris Hughes (Mar 24 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162474):
But I haven't worked out how to build an old commit with git yet.

#### [Kevin Buzzard (Mar 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162528):
Just google "git change to commit" or something

#### [Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162565):
google is really good for git commands

#### [Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162577):
git checkout commit

#### [Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162579):
is probably how to do it

#### [Kevin Buzzard (Mar 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162580):
Oh wooah lean HEAD just failed to build.

#### [Chris Hughes (Mar 24 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162703):
Yeah. If we just find a version of lean and mathlib to use it should be fine. But I don't know which version.

#### [Simon Hudon (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162747):
```quote
Simon Hudon: I believe mathlib doesn't build with the latest nightly. I work with revision `07bb7d809b6be49f38ce4e427c54a82708ae281f`  of Lean

Simon Hudon: And I use `4ceb545f7e07431263e1131a9c9524a28de99472` for mathlib 
```

#### [Kevin Buzzard (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162752):
I just checked out c4cc8c88c08d86cd902c577de09ef69528c2da36 of Lean on the basis that it was the most recent version that compiled (as far as I coudl see)

#### [Mario Carneiro (Mar 24 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162805):
I built a version slightly in advance of the nightly, but it should be out now

#### [Chris Hughes (Mar 24 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162881):
Where are the instructions on building lean? I did it before, but I don't remember how

#### [Kevin Buzzard (Mar 24 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162927):
Do you know which commit it works with? I am having trouble getting Lean to compile from source and mathlib doesn't compile if I download the latest linux nightly and then use "leanpkg upgrade"

#### [Kevin Buzzard (Mar 24 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162939):
```quote
Where are the instructions on building lean? I did it before, but I don't remember how
```
https://github.com/leanprover/lean/blob/master/doc/make/msys2.md

#### [Chris Hughes (Mar 24 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124162993):
I''ve been using the f7977ff5a6bcf7e5c54eec908364ceb40dafc795 version of mathlib. The latest version only works with the version of lean that doesn't work

#### [Kevin Buzzard (Mar 24 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163050):
How do I get travis to tell me the last Lean commit which compiled for linux?

#### [Kevin Buzzard (Mar 24 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163051):
And how do I get mathlib to tell me the version of Lean which it compiled against?

#### [Simon Hudon (Mar 24 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163101):
You can get the result of all the builds here:

https://travis-ci.org/leanprover/mathlib/builds

#### [Simon Hudon (Mar 24 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163158):
I'm not sure how to use that to infer the corresponding version of Lean other than see that the last successful build was 10 days ago. We can go and see what version Lean was on 10 days ago

#### [Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163201):
I don't understand travis.

#### [Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163202):
According to this link:

#### [Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163203):
https://ci.appveyor.com/project/leodemoura/lean/history

#### [Kevin Buzzard (Mar 24 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163206):
the last successful build was c17e5b913b2db687ab38f53285326b9dbb2b1b6e

#### [Kevin Buzzard (Mar 24 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163215):
but according to https://travis-ci.org/leanprover/lean/builds

#### [Kevin Buzzard (Mar 24 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163255):
it was d6d44a19947e2575b3fceed6d61167d258c661fb

#### [Simon Hudon (Mar 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163278):
I guess you can try either

#### [Simon Hudon (Mar 24 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163321):
You might be interested in recording the version of Lean that you use in your repository. You can facilitate the testing and importing this way

#### [Kevin Buzzard (Mar 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163678):
That's a good idea.

#### [Kevin Buzzard (Mar 24 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163729):
If I decide to use leanpkg upgrade with a specific version of lean, which version of mathlib will it upgrade to?

#### [Simon Hudon (Mar 24 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163735):
If you need a reference, I have some scripts for that. Some of them blocks you from committing on git if your lean version is inaccurate

#### [Simon Hudon (Mar 24 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124163756):
I think there are two possibilities: if you're on an official release (say 3.3.0) it will get the version of mathlib that works with it. Otherwise, it will get HEAD

#### [Kevin Buzzard (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/importing%20within%20lean%20package/near/124164063):
(deleted)

