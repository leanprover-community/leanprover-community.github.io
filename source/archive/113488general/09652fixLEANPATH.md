---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09652fixLEANPATH.html
---

## [general](index.html)
### [fix LEAN_PATH](09652fixLEANPATH.html)

#### [garySebastian (Apr 01 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124468992):
I've tried to get lean to work on Xubuntu, macOS, and nixos; all three are having the same issue where importing anything (including standard), yields an error: "file standard not found in the LEAN_PATH". I've done a lot of looking around and can't find any relevant information on LEAN_PATH. I have lean in my system PATH. I'm not sure what it wants from me.

#### [Simon Hudon (Apr 01 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469133):
Do you use `leanpkg`?

#### [garySebastian (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469340):
I've tried creating a new project and doing configure/messing with the leankpkg.path, but it doesn't seem to do anything.

#### [Simon Hudon (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469437):
Setting `LEAN_PATH` by hand leads to nothing but trouble so I suggest you unset it (if you set it yourself), create a Lean project with `leanpkg init`and using `leanpkg add` for your dependencies

#### [garySebastian (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124470287):
Thank you for the advice so far, but I'm still getting the same error after trying both leanpkg add https://github.com/leanprover/mathlib and https://github.com/leanprover/stdlib.git. They're both in the _build directory within the project, and they were both added to the leanpkg.path file and leanpkg.toml files.

#### [Simon Hudon (Apr 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124470526):
can you show me your `leanpkg.toml` file and tell me where you put your source file?

#### [Patrick Massot (Apr 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482877):
@**Sebastian Ullrich** and @**Gabriel Ebner**  This is one more motivating example for you. We really need to make it simpler for people to start using Lean

#### [Kenny Lau (Apr 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482878):
I concur

#### [Patrick Massot (Apr 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482884):
I mean: I know you are working hard, I only want to point out further encouragement.

#### [Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493380):
Doesn't this all depend on how you are running Lean?

#### [Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493383):
For example, I _think_ that if you use VS Code and open a folder

#### [Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493384):
and there's e.g. some `leanpkg.path` file in the root of that folder

#### [Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493386):
then I think VS Code will look at that file before it looks at the `LEAN_PATH` environment variable [NB but apparently I am wrong]

#### [Kevin Buzzard (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493392):
What is this `_build` directory you're talking about @**garySebastian** ?

#### [Gabriel Ebner (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493394):
Neither vscode nor emacs touches the LEAN_PATH environment variable.  If it is set, it takes precedence over any `leanpkg.path` file.  Please don't set the `LEAN_PATH` environment variable.

#### [Kevin Buzzard (Apr 01 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493438):
If you just follow the step by step instructions for making a new project and adding mathlib, I think it will add mathlib into a directory called `_target`

#### [Kevin Buzzard (Apr 01 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493440):
(I am talking about using `leanpkg`)

#### [Kevin Buzzard (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493486):
and everything should magically work because `leanpkg` will get your `leanpkg.path` right and you won't need to set `LEAN_PATH` at all by the looks of things

