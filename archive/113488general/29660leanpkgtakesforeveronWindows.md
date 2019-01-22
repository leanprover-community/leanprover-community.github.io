---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29660leanpkgtakesforeveronWindows.html
---

## [general](index.html)
### [leanpkg takes forever on Windows](29660leanpkgtakesforeveronWindows.html)

#### [Kevin Buzzard (Jul 19 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg takes forever on Windows/near/129937135):
I just typed `leanpkg init` on Windows, and it sat there for around a minute before saying "you meant `leanpkg init name_of_package` so please start again". I just typed `leanpkg init my_package` and in the time it took me to write this the Windows machine still hasn't finished mulling over this command. I've seen this several times before on Windows. What's going on?

#### [Mario Carneiro (Jul 19 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg takes forever on Windows/near/129937894):
probably lean core files aren't compiled

#### [Kevin Buzzard (Jul 19 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg takes forever on Windows/near/129944576):
They seem to be -- this was from the most recent nightly and there was a bunch of .olean files where there should be..

#### [Kevin Buzzard (Jul 19 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg takes forever on Windows/near/129944633):
(I mean in `lib` with the `.lean` files)

