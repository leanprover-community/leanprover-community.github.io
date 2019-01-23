---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52136slashesinleanpkgpath.html
---

## Stream: [general](index.html)
### Topic: [slashes in leanpkg.path](52136slashesinleanpkgpath.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212544):
What does leanpkg.path look like on windows? I have about 20 minutes to get mathlib up and running on a win7 machine with no admin access and hence no git (apparently!). Are they `/` or `\`, and one or two?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212550):
I have lean and mathlib and VS code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212564):
I have no msys2 and no command line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212570):
I have notepad :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 06 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212629):
```
builtin_path
path _target/deps/mathlib/.
path ./src
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212661):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212685):
works!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212689):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212690):
now need to make .olean files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212732):
with no command line :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212740):
how about just use the online version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212976):
download someone elses oleans?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212986):
where from?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213000):
I could upload mine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213092):
Or Kevin could upload his.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213106):
I have some here for unix :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213107):
I don't know if Windows oleans are any different


{% endraw %}
