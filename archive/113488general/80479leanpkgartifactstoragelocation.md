---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80479leanpkgartifactstoragelocation.html
---

## Stream: [general](index.html)
### Topic: [leanpkg artifact storage location](80479leanpkgartifactstoragelocation.html)

---


{% raw %}
#### [ Keeley Hoek (Aug 01 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130723831):
Hi there! Does anyone know of a particular reason why leanpkg copies dependencies into a "_target" directory in the project folder, as opposed to keeping a directory of artifacts in your home directory (e.g. like maven does)? It'd certainly avoid unnecessarily compiling mathlib multiple times when playing around with little projects.

#### [ Reid Barton (Aug 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724301):
@**Sebastian Ullrich** ^ ?

#### [ Mario Carneiro (Aug 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724346):
one of `leanpkg add` and `leanpkg install` is a global install

#### [ Sebastian Ullrich (Aug 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724449):
`leanpkg install`, but that's intended for use in non-project files

#### [ Kevin Buzzard (Aug 01 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724789):
I currently have two projects which are using different versions of mathlib, but I'm not usually in this situation. I'm running something with UGs where we're all using mathlib 3.4.1 because trying to get 25 people to upgrade their mathlibs is a pain when some of them can't even open a terminal. I'm also doing a project which uses bleeding edge mathlib. But if I could have two flavours of mathlib installed globally I'd be happier than I am now, because I often find myself recompiling. I sometimes cheat and copy and paste instead of recompiling.

#### [ Sebastian Ullrich (Aug 01 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724961):
@**Keeley Hoek** I don't think there is a particular reason other than the current `leanpkg` being the minimum viable product

#### [ Scott Morrison (Aug 02 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748733):
Potentially there's a problem for people who work like me, with two repositories `repoA` and `repoB`, with `repoB` depending on a particular commit from `repoA`, and both repositories change rapidly. In this case in the central `~/.leanpkg` directory I suspect we will end up with lots of copies of `repoA` checked out at different commits.

#### [ Scott Morrison (Aug 02 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748735):
This is probably a small price to pay (people in this situation can just clean out that directory every so often?) in exchange for having multiple projects be able to use the same compile version of mathlib, which would be really really lovely.

#### [ Scott Morrison (Aug 02 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748740):
I'd be very happy to see central storage in any case.

#### [ Sebastian Ullrich (Aug 02 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748981):
What Rust's `cargo` (which is the direct inspiration for `leanpkg`) does is it caches downloaded git repositories in a central cache (because these can be shared even if you're using different versions of them in different projects) and then stores build artifacts per project, probably to avoid flooding the central cache, as @**Scott Morrison** alluded to

#### [ Scott Morrison (Aug 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130751692):
I see, but that wouldn't save on rebuilding mathlib between different projects, which is the real payoff.


{% endraw %}
