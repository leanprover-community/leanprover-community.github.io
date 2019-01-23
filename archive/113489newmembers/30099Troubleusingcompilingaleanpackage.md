---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30099Troubleusingcompilingaleanpackage.html
---

## Stream: [new members](index.html)
### Topic: [Trouble using compiling a lean package](30099Troubleusingcompilingaleanpackage.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Calle Sönne (Nov 17 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147882741):
Im trying compile a leanpackage. I assume the way you do is by running leanpkg build in the folder where leanpkg.toml is located. However doing that gives me the following error:

error: override toolchain 'master' is not installed
info: caused by: the toolchain file at '/home/calle/herstein/leanpkg.toml' specifies an uninstalled toolchain

I have tried running leanpkg build, leanpkg init, leanpkg .configure. All of them give the same error (even just running "lean" within the folder gives same error). Other than this lean is working fine and I can use/work on other packages.

Here is the leanpkg.toml file if that explains anything:

[package]                                                                                                                                                                                
name = "herstein"
version = "0.1"
lean_version = "master"
path = "src"

[dependencies]
mathlib = {git = "https://github.com/leanprover/mathlib", rev = "c7c0d2a1bb2f0ba353bbcb0510352a25c80fc186"}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147882884):
Hi @**Calle Sönne** Are you using `elan`? Which OS are you on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885359):
He is using `elan`, it's on Windows, he showed me this on Thursday and I had no idea. Just running `leanpkg` by itself with no parameters gave this error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885375):
and lean is funded by microsoft lmao

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885432):
I'm funded by Imperial College but that doesn't mean that the "official" website they insist on generating for me bears any relation to what I have been doing over the last 10 years. Big organizations are complex things Kenny.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885448):
what, [this one](https://www.imperial.ac.uk/people/k.buzzard)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Calle Sönne (Nov 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885540):
Im using linux (Manjaro)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885596):
Is `lean_version = "master"` supposed to work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885621):
```quote
what, [this one](https://www.imperial.ac.uk/people/k.buzzard)?
```
 Yes. It's auto-generated you know! The script was written in about 2004.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Calle Sönne (Nov 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885626):
Im using elan version 0.7.1 and lean version 3.4.2 nightly-2018-11-13

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885670):
I would put one of those version numbers in the `lean_version` field then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885673):
elan uses that field to decide which lean to invoke and I don't think it understands "master"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885676):
Try `lean_version = "nightly-2018-11-13"`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885683):
(in leanpkg.toml)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885737):
I see, so this is the issue. I've never used elan and I didn't understand the error. The job of elan is to ensure that the version of Lean coincides with the version used by the package. This will be an issue in future when Lean 4 hits. But it never bites me now because every package I know of uses Lean 3.4.1 or some nightly after 3.4.1 which is basically the same as 3.4.1 but with some minor irrelevant bugfix

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Calle Sönne (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885738):
That did it :) Thank you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885740):
:-)


{% endraw %}
