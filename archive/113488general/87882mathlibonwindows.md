---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87882mathlibonwindows.html
---

## Stream: [general](index.html)
### Topic: [mathlib on windows](87882mathlibonwindows.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 16 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134031931):
I am trying to install mathlib on a windows laptop. In mingw I set all the paths, but I get this:
```
$ leanpkg install https://github.com/leanprover/mathlib
> mkdir -p C:\msys64\home\aviga/.lean
> cd C:\msys64\home\aviga/.lean
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
mathlib: trying to update _target/deps/mathlib to revision lean-3.4.1
cannot find revision lean-3.4.1 in repository _target/deps/mathlib
```
What am I doing wrong?  And -- out of curiosity -- why does it take so long for `leanpkg` to start up?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134032148):
Hi Jeremy! If leanpkg takes a while to start up, it's most likely not running from its .olean files. I don't know about the git error unfortunately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 16 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134032556):
I suspected that, but I can't imagine why not. I installed the binary from `leanprover.github.io`, and the files are all there.
Maybe I'll ask Mario to help me on Monday.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 16 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134032624):
Hmm, I use Lean on Windows.  I've never installed mathlib user-wide. I know it works if you do `leanpkg add` per project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 16 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134033297):
Thanks for the suggestion. Indeed, using `leanpkg add` worked (modulo the problem with not using the `.olean` files).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134034346):
Heh, well, we do have the following source comment :) : https://github.com/leanprover/lean/blob/master/src/util/lean_path.cpp#L45

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 16 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134034502):
Thanks. Things seem to be ok now. Using `lean --make` in the `library` directory seems to have fixed the `.olean` problem. And deleting the `.lean` directory and running `leanpkg install` again seems to be working. It is building `mathlib` now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134041464):
@**Jeremy Avigad** Now that I think about it, I'm surprised the .olean files haven't been a bigger issue before. We check the modification time of the .olean file against that of the corresponding .lean file. Extracting files from a zip file resets the modification time, so the result depends on the extraction order (at least in the zip file itself, .olean files are listed after their .lean files). And even then, Windows touches each downloaded file again to mark them as "potentially dangerous"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134044339):
Just to remark that I am nowadays completely resigned to the fact that every invocation of `leanpkg` on a Windows machine begins with a 15 second wait during which nothing seems to happen other than me moaning about Windows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134045713):
A little test shows that on linux the `tar` command seems to preserve file timestamps. Is this just a problem with zip on Windows? And am I right in thinking I can fix on a user's Windows machine by somehow re-compiling leanpkg just once?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134060613):
elan seems to reset the modifications times even on Linux, though that's probably its own fault. Anyway, I've never had an issue with it on Linux, whereas I could reproduce the issue on Windows on the first try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134060655):
As Jeremy said, you should go into the `library` folder and call `lean --make`. You could do the same in `leanpkg`, but that's probably not the expensive part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 16 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065460):
An old post from Kevin (https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/) suggests he has been struggling with this issue for a while. 
Actually, for me, the situation is even more mysterious. When I do `lean --make` in the `library` folder, it compiles a bunch of files, say list `A`. If I type `lean --make` again, it compiles another bunch, say, list `B`. Then if I do it again, it then recompiles list `A`! If I keep doing it,  it continues to cycle through those two. It is almost as though `lean` thinks there is a cyclic dependency, or there is some kind of funny race condition with timestamps. (I think the wait to start `leanpkg` became less painful only because I landed on the shorter side of the cycle.)
I'll be out all afternoon and the laptop is at home, but I'll experiment more later tonight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065730):
Oof, that doesn't sound good at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 16 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065734):
One good news, Lean 4 will have a trace option to debug why an .olean file wasn't imported...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 16 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065838):
This might be only tangentially related, but I experienced [something like this](https://github.com/leanprover/mathlib/issues/308) when I ran `leanpkg build` inside `_target/deps/mathlib` in a package and then ran it from the base folder afterwards. I had also expected that once the .olean files were generated once, they didn't have to be rebuilt if nothing changed, but I guess that's not true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065939):
You should not run `leanpkg` inside the `target` folder, I think it gets confused

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134065945):
you can just run `lean --make` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 17 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134074893):
Update: deleting all the`. olean` files (`del /s *.olean` in `library`) and rebuilding (`lean --make`) seems to work fine. After that, `lean --make` does nothing. I had to go into the `leanpkg` directory and run `lean --make` there too. Now `leanpkg` runs instantaneously.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 17 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20on%20windows/near/134075802):
I just released a new version of elan that seems to fix the issue

