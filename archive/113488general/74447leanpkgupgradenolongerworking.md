---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74447leanpkgupgradenolongerworking.html
---

## Stream: [general](index.html)
### Topic: [`leanpkg upgrade` no longer working?](74447leanpkgupgradenolongerworking.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502598):
Since I've switched all my repositories to have `lean_version = "3.4.1"` in the `leanpkg.toml` file, it seems that `leanpkg upgrade` no longer has any effect: that is, commits to downstream repositories aren't pulled.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502600):
Did something change?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502608):
Can anyone guess what I'm doing wrong? I just want my `leanpkg.toml` file to be automatically updated to the latest commit of the downstream repos.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 03 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127510205):
leanpkg is looking for a branch `lean-3.4.1`. You should switch to that from `master` if you only want to support that version. You should not set stable Lean versions on the `master` branch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127519975):
Okay --- I'm a bit confused. The `leanpkg.toml` file in `mathlib` currently says: `lean_version = "3.4.1"`, so I'd copied that over into my little chain of dependencies. What should the `lean_version` in my `leanpkg.toml` files be?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127533855):
mathlib now keeps the `master` and a new `lean-3.4.1` branch in sync, but I'd recommend just moving to the latter altogether https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/lean-3.2E4.2E1.20branch/near/127075441

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535112):
I'm sorry, I still don't understand. What am I meant to do in my repos, so that `leanpkg upgrade` actually upgrades? Should I set all the `lean_version` lines back to `master`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535287):
You should keep `lean_version = "3.4.1"` but push that as a new branch `lean-3.4.1` to your repo(s) and use that branch for development against Lean 3.4.1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535465):
ooooh. That hadn't even occurred to me. For lame git-newbs like me, it's so much easier to just do everything in the master branch. (Okay, I think I could cope, but I'm not sure @**Kevin Buzzard** could. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535529):
You can set the default branch on Github to the new branch, then there shouldn't be all that much difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535555):
In his book "Lean for the working mathematician", I think Kevin will have to spend the first 30 pages on "Git for the working mathematician".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 15 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128114390):
Is there any possibility of changing the tooling so people can continue developing their repositories on `master` branches, and still have `leanpkg upgrade` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 15 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128114399):
(Sorry to restart a two week old thread --- for quick context, apparently the advice was that if you want to be able to use `leanpkg upgrade`, you need to work in a branch called `lean-3.4.1`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128116038):
Well, Lean 3 is frozen. We can add a `branch` config field to leanpkg.toml dependencies in Lean 4 so that users can stay on non-canonical branches.


{% endraw %}
