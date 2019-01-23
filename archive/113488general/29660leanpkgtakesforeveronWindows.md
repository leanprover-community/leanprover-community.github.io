---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29660leanpkgtakesforeveronWindows.html
---

## Stream: [general](index.html)
### Topic: [leanpkg takes forever on Windows](29660leanpkgtakesforeveronWindows.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 19 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129937135):
I just typed `leanpkg init` on Windows, and it sat there for around a minute before saying "you meant `leanpkg init name_of_package` so please start again". I just typed `leanpkg init my_package` and in the time it took me to write this the Windows machine still hasn't finished mulling over this command. I've seen this several times before on Windows. What's going on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129937894):
probably lean core files aren't compiled

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 19 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129944576):
They seem to be -- this was from the most recent nightly and there was a bunch of .olean files where there should be..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 19 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129944633):
(I mean in `lib` with the `.lean` files)

