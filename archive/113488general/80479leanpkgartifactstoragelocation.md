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
<p>Hi there! Does anyone know of a particular reason why leanpkg copies dependencies into a "_target" directory in the project folder, as opposed to keeping a directory of artifacts in your home directory (e.g. like maven does)? It'd certainly avoid unnecessarily compiling mathlib multiple times when playing around with little projects.</p>

#### [ Reid Barton (Aug 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724301):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ^ ?</p>

#### [ Mario Carneiro (Aug 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724346):
<p>one of <code>leanpkg add</code> and <code>leanpkg install</code> is a global install</p>

#### [ Sebastian Ullrich (Aug 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724449):
<p><code>leanpkg install</code>, but that's intended for use in non-project files</p>

#### [ Kevin Buzzard (Aug 01 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724789):
<p>I currently have two projects which are using different versions of mathlib, but I'm not usually in this situation. I'm running something with UGs where we're all using mathlib 3.4.1 because trying to get 25 people to upgrade their mathlibs is a pain when some of them can't even open a terminal. I'm also doing a project which uses bleeding edge mathlib. But if I could have two flavours of mathlib installed globally I'd be happier than I am now, because I often find myself recompiling. I sometimes cheat and copy and paste instead of recompiling.</p>

#### [ Sebastian Ullrich (Aug 01 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130724961):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> I don't think there is a particular reason other than the current <code>leanpkg</code> being the minimum viable product</p>

#### [ Scott Morrison (Aug 02 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748733):
<p>Potentially there's a problem for people who work like me, with two repositories <code>repoA</code> and <code>repoB</code>, with <code>repoB</code> depending on a particular commit from <code>repoA</code>, and both repositories change rapidly. In this case in the central <code>~/.leanpkg</code> directory I suspect we will end up with lots of copies of <code>repoA</code> checked out at different commits.</p>

#### [ Scott Morrison (Aug 02 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748735):
<p>This is probably a small price to pay (people in this situation can just clean out that directory every so often?) in exchange for having multiple projects be able to use the same compile version of mathlib, which would be really really lovely.</p>

#### [ Scott Morrison (Aug 02 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748740):
<p>I'd be very happy to see central storage in any case.</p>

#### [ Sebastian Ullrich (Aug 02 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130748981):
<p>What Rust's <code>cargo</code> (which is the direct inspiration for <code>leanpkg</code>) does is it caches downloaded git repositories in a central cache (because these can be shared even if you're using different versions of them in different projects) and then stores build artifacts per project, probably to avoid flooding the central cache, as <span class="user-mention" data-user-id="110087">@Scott Morrison</span> alluded to</p>

#### [ Scott Morrison (Aug 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20artifact%20storage%20location/near/130751692):
<p>I see, but that wouldn't save on rebuilding mathlib between different projects, which is the real payoff.</p>


{% endraw %}
