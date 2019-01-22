---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61616euclideandivision.html
---

## [general](index.html)
### [euclidean division](61616euclideandivision.html)

#### [Nicholas Scheel (Mar 26 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124205800):
Is there a proof of Euclidean division (divmod) in the libraries somewhere? I've been looking around for theorems with `mod` in the core library and mathlib but couldn't find anything ...

#### [Simon Hudon (Mar 26 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124206823):
Have you looked in `init.data.nat.lemmas` in the core library?

https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L660-L740

#### [Nicholas Scheel (Mar 26 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124207213):
ahh that makes sense now, thanks! I must have glossed over it earlier

#### [Simon Hudon (Mar 26 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124207315):
No problems! The naming scheme is fairly regular so if you search for `_mod_` in the core library or mathlib, it should give you a good list of available lemmas. If you miss any, they're usually close to the ones you do find

