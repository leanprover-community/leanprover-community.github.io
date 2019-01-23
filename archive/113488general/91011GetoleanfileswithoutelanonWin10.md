---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91011GetoleanfileswithoutelanonWin10.html
---

## Stream: [general](index.html)
### Topic: [Get olean files without elan on Win10](91011GetoleanfileswithoutelanonWin10.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 27 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136602966):
I'd like to download updates to mathlib manually from github, then produce the olean files. How can I do this? I saw [these](https://github.com/leanprover/lean/blob/master/doc/make/msvc.md) instructions, but apparently they aren't compatible with VS2018.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 27 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136604656):
I *think* that `elan` is supposed to do all of this for you. But if you choose not to use it for some reason, then you can use `leanpkg` to build the `.olean` files. Maybe this old page https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/ helps you? But I think that users are now encouraged to use `elan`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 27 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605169):
elan still doesn't work with spaces in user names.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605314):
```quote
elan still doesn't work with spaces in user names.
```
Wait, which usernames?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 27 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605377):
your username

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605386):
```quote
your username
```
Yeah, I mean -- the Windows username? For file paths and stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605389):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605391):
Ok, that's not a problem, then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 27 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605739):
Yes, I think the issue is exactly with file paths. What's even more frustrating is that apparently the problem has been fixed, but the PR has not yet been accepted (and might never be, I guess, until Lean 4 comes out next year)

