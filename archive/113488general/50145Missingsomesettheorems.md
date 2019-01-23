---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50145Missingsomesettheorems.html
---

## Stream: [general](index.html)
### Topic: [Missing some set theorems?](50145Missingsomesettheorems.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252632):
Hi folks, I have been following Logic & Proof (https://leanprover.github.io/logic_and_proof/logic_and_proof.pdf) and in Chapter 12, it says to use `import data.set`, but I get an error that that path doesn't exist. However, I am still able to use set membership operators, etc. On the other hand, the book mentions theorems like `mem_inter`, but those aren't in scope. Have they moved to another library? How do I import them? Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252817):
It got renamed recently to `data.set.basic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252860):
@**Mario Carneiro** @**Jeremy Avigad** This would be worth updating I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252868):
Ah, thanks, that doesn't seem to work either. Maybe my Lean installation is old.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252871):
I'm using the Lean extension in VS Code, also.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252916):
Can you bring up your project's leanpkg.toml and check that you have mathlib in your dependencies?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252976):
Yeah, I don't seem to have that. It's in `$HOME/lean-3.3.0-darwin/lib/lean/leanpkg/leanpkg.toml` and it just has:

```
[package]
name = "leanpkg"
version = "0.1"
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130252989):
I guess that's a global `leanpkg.toml` file? I don't have one for my project. I'm just creating individual `.lean` files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253038):
What should I add to the `leanpkg.toml` file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253047):
Or maybe I need to run the `leanpkg` command to add a library?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253109):
I really know nothing about lean package management. Just did the minimal amount to get Lean and the VS Code extension installed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253850):
Sorry i stepped away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253895):
go in your project's directory with a terminal and call `leanpkg init my_project` (feel free to pick a better name)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253898):
Then call `leanpkg add leanprover/mathlib`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253899):
then `leanpkg build`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130253905):
By default, leanpkg sets `src` as the directory where all your sources are located

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254066):
Thanks! The `leanpkg init my_project` worked, but:

```
$ leanpkg add leanprover/mathlib
mathlib: using local path ./leanprover/mathlib
failed to open file './leanprover/mathlib/leanpkg.toml'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254125):
sometimes you have to be more explicit: `leanpkg add https://github.com/leanprover/mathlib`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254175):
Btw, this might help: https://github.com/leanprover/mathlib/blob/master/docs/elan.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254181):
That add command seemed to work, thanks. I'm doing the build.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254188):
It's funny, I just recently added a similar feature to the Haskell build tool Stack, to be able to download templates from different github users without having to specify the full path.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254246):
The Elan tool looks helpful, thanks. Sounds a bit like Stack actually, letting you use different versions of the compiler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254360):
Well, the `leanpkg build` ran successfully. And I restarted the editor, and now the `import data.set.basic` shows no error. But `univ`, `mem_inter`, and those other theorems are still redlined. Maybe I need to `open` some namespace?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254413):
To be fair `elan` and `leanpkg` share some the functions of `stack` but we still don't have curated package collections.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254415):
Wasn't it already possible to link to github in your `stack.yaml` file, in the `packages` section?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254416):
Ah, right. Well that's a pretty unique feature to `stack`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254457):
I'm hoping to see that happen eventually. I find it pretty useful. But mathlib changes so much that we keep upgrading.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254464):
This is about templates for new projects. There's a set of templates under the `commercialstack` user on github. This was so you could install templates from a different github user by writing `stack new username/template_name`. Instead of having to write the whole URL.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254465):
In VS code, there may be a command to let you find definitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254508):
Yeah, "no definition found for univ"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254514):
I might have misled you. Try also importing `data.set`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254517):
OK, added that. Still can't find `univ`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254518):
```quote
This is about templates for new projects. There's a set of templates under the `commercialstack` user on github. This was so you could install templates from a different github user by writing `stack new username/template_name`. Instead of having to write the whole URL.
```
Nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254560):
What version of Lean is written in your `leanpkg.toml`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254563):
You can also install templates from gitlab or bitbucket, e.g. `stack new gitlab:username/template_name`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254565):
Lean version 3.3.0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254574):
Ok, that makes sense. Let's set it to `3.4.1` to have the most recent stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254626):
OK, I changed it and ran `leanpkg build` but got the error `WARNING: Lean version mismatch: installed version is 3.3.0, but package requires 3.4.1
`. Maybe I need to install elan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254672):
Yes, that makes things much easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254679):
Thing is, I'm leading a study group tomorrow night where we're supposed to go over the exercises for Chapter 12. And I just got around to working on them tonight, and now I realize probably nobody else is going to be able to work them either. Will have to post instructions for folks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254741):
That would be good. I think this might be a good start: https://github.com/leanprover/mathlib/blob/master/docs/elan.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254743):
I wonder how I installed Lean the first time - probably just downloaded the binary package. Looks like it's on homebrew and that has 3.4.1 - might have been another simple way to keep it up to date.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254745):
Got it, thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254747):
Maybe we should remove it from homebrew and put elan instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254809):
Nah. Both ghc and stack are on homebrew. People can choose what they want. But it would be helpful if this page said anything about elan: https://leanprover.github.io/download/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254915):
Yeah that's true. The thing with ghc though is that there are many options for build systems. Some people use cabal, others nix. But with Lean, I think it's too easy to get started the wrong way and there aren't that many different ways of using the tool.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254972):
OK, good point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130254978):
Any luck with elan so far?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130255092):
I should go, my bed is calling to me. I hope it works out for your study session

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130255488):
Sorry, just biked home because the coffee shop closed. Will try elan now. Thanks and take care.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130260428):
@**Lyle Kopnicky**  I think the missing step is `open set`. Assuming you got `import data.set.basic` working, the name of the univ set is `set.univ` or just `univ` if `set` is open.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284056):
Thanks @**Mario Carneiro**, but I am even further back now. I installed Elan and did `leanpkg install leanprover/mathlib` and that seemed to work fine. Then did `leanpkg build` and it crashed with `<unknown>:1:1: error: file 'data/list/basic' not found in the LEAN_PATH`. How do I install that? I tried `leanpkg install data/list/basic` but it says that path is not found.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284080):
Here is my `leanpkg.toml`:

```
[package]
name = "logic_and_proof"
version = "0.1"
lean_version = "3.4.1"

[dependencies]
```

Do I need to manually add something to `dependencies`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284140):
I though running `leanpkg install leanprover/mathlib` would add something to `dependencies` but it didn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284155):
You need some version of `leanpkg add`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284209):
Which will add to that dependencies section for you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284312):
(or you can edit that section manually)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284339):
Ah, that seemed to do the trick. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284391):
`leanpkg install` is analogous to `cabal install` I think. Not sure I have ever used it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130284460):
OK. Up until yesterday I hadn't used `leanpkg` at all. Have just been using individual `.lean` files but that didn't work anymore when I needed some of these set theorems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130294885):
Yay, finally have it working, following the `leanpkg build`. In the code, `import data.set` followed by `open set` works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130295045):
How many seconds have you now got to do all the exercises? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 27 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130385489):
Haha... I didn't manage to do the exercise beforehand. But others in the group did, so they presented their solutions. It was awesome. One person had already installed Elan, I guess, and another was using the online Lean, so they were both able to do the exercises.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Jul 27 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Missing%20some%20set%20theorems%3F/near/130385550):
But during the meeting, I was able to paste their code into my editor and everything checked out fine. I was projecting it on the whiteboard and they could underline things and draw around them.

