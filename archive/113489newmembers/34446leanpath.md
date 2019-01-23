---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/34446leanpath.html
---

## Stream: [new members](index.html)
### Topic: [lean path](34446leanpath.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Hendrik (Sep 22 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134421026):
I have the following problem: After installing the lean vs code extension and downloading the math library, adding the math library to a workspace results in unresolved imports because the math library is not inside the LEAN_PATH.

Does this mean that the math library needs to be saved inside the lean folder or is there a way to add the path to the math library to LEAN_PATH?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134421303):
Are you using `leanpkg add` to set up mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134421304):
There are some detailed instructions [here](https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/) which worked for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Hendrik (Sep 22 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134421464):
Oh, I didn't, I simply forked the math library from github. Thank you for the link!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Hendrik (Sep 22 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134421708):
I got to the point where lean --version works well but trying to create a project fails to the "failed to start child process" error also documented here: https://groups.google.com/forum/#!topic/lean-user/a3nphm5h2p4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Geoffrey Yeung (Sep 22 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134424116):
just my 2 cents, in my case it was because git was not in PATH

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Hendrik (Sep 22 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134425890):
I'm pretty sure the path variables are set correctly. Maybe I will try the linux installation some time in the future. I think the developers should actually put a lot more attention on making lean accessible to new users. I am comfortable with command line use but doing a project with students would be a nightmare.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134437284):
I have a working setup on windows 10 and I don't recall ever having to deal with this error. I'm using the bash shell that comes with git for windows "`C:\Program Files\Git\bin\sh.ext`", though I'm using it from the program [`cmder`](http://cmder.net). The only lean-related thing I have in the path (which I placed in my `.bashrc`) is the path to my lean-nightly directory which is inside something like `users\user\Downloads`.

When exactly does the failed to start child process error occur, and does it say anything else? Is it when running `leanpkg new`? We should at least be able to figure out where it's being triggered...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20path/near/134487011):
@**Hendrik** It looks like this issue has been figured out [here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/leanpkg/near/134482297). One quick solution is simply to try the git-bash shell if you have that installed.

