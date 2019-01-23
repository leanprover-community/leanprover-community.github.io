---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74802VScodeextensiononmacOS.html
---

## Stream: [general](index.html)
### Topic: [VScode extension on macOS](74802VScodeextensiononmacOS.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152447):
Do you need to append your lean/bin directory onto $PATH and then launch vscode from the command line in order for the extension to locate lean on macOS?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152540):
I put my elan path into my .bash_profile and then VS code was able to figure out the rest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152787):
On mac or linux?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152852):
On macOS 10.13 until a few days ago and macOS 10.14 since then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152905):
It's also possible to just put the full path to your lean executable in the lean VS code extension settings and that ought to work as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153376):
Invoking lean from the command line as a sanity check produces:
dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib
  Referenced from: /Users/bixbyr/lean-3.4.1/bin/./lean
  Reason: image not found
Abort trap: 6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153522):
Nvm that looks like a more general brew issue to fix and probably doesn't have anything to do with lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153538):
yeah, you just need to do `brew install gmp`. The fact that this isn't stated anywhere obvious is a well-known issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153606):
https://github.com/leanprover/lean/issues/1971 Supposedly, installing lean itself via homebrew should include gmp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153658):
ah I just installed lean via binary download

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153705):
Yeah, I think the current recommended procedure might be to use elan https://github.com/Kha/elan

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ryan Smith (Oct 04 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153990):
git clone mathlib to include/ or is there a more elegant way to get it and bring it into scope?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135154139):
I've been using `leanpkg` as described [here](https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135154204):
There's a strong possibility that you'll run into [this issue](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/leanpkg/near/134435061) if you're running lean 3.4.1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135162102):
A push was made to document `elan` properly at https://github.com/leanprover-community/mathlib/blob/elan-docs/docs/elan.md . If this document does not answer all your questions then please flag this here or even better submit a PR. It's time this was fixed. Sebastian is very busy with Lean 4, but we as a community can definitely make things like this better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135187195):
I think [the merged version of that file in mathlib](https://github.com/leanprover/mathlib/blob/master/docs/elan.md) is actually more recent. However, as mentioned [here](https://github.com/leanprover/mathlib/issues/365) and in the zulip conversation I linked above, Reid pointed out that those instructions won't get you the most recent version of mathlib since mathlib's `leanpkg.toml` specifies lean 3.4.1 and `leanpkg add` gives you the lean-3.4.1 branch, which is several months out of date.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135194622):
You can ignore that part of the instructions though and still use the instructions for installing elan

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135195074):
Right. To be fully explicit, I think the instructions should be edited to say something like "If you want to include an up-to-date version of mathlib in your project, use `elan install nightly` to install the latest version of lean. Then use `leanpkg new my-project` and `leanpkg add <link to mathlib>`. Make sure that `leanpkg.toml` in  `my-project` has a line saying `lean_version = nightly-something`. Then run `leanpkg upgrade`, etc."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 08 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135405425):
On OSX, do "brew install gmp"

