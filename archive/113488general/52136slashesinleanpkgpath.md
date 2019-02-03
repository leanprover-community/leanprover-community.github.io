---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52136slashesinleanpkgpath.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [slashes in leanpkg.path](https://leanprover-community.github.io/archive/113488general/52136slashesinleanpkgpath.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 06 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212544):
<p>What does leanpkg.path look like on windows? I have about 20 minutes to get mathlib up and running on a win7 machine with no admin access and hence no git (apparently!). Are they <code>/</code> or <code>\</code>, and one or two?</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212550):
<p>I have lean and mathlib and VS code</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212564):
<p>I have no msys2 and no command line</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212570):
<p>I have notepad :-)</p>

#### [ Andrew Ashworth (Jul 06 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212629):
<div class="codehilite"><pre><span></span>builtin_path
path _target/deps/mathlib/.
path ./src
</pre></div>

#### [ Kevin Buzzard (Jul 06 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212661):
<p>thanks</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212685):
<p>works!</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212689):
<p>hmm</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212690):
<p>now need to make .olean files</p>

#### [ Kevin Buzzard (Jul 06 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212732):
<p>with no command line :-/</p>

#### [ Kenny Lau (Jul 06 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212740):
<p>how about just use the online version</p>

#### [ Chris Hughes (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212976):
<p>download someone elses oleans?</p>

#### [ Kenny Lau (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129212986):
<p>where from?</p>

#### [ Chris Hughes (Jul 06 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213000):
<p>I could upload mine.</p>

#### [ Chris Hughes (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213092):
<p>Or Kevin could upload his.</p>

#### [ Kevin Buzzard (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213106):
<p>I have some here for unix :-)</p>

#### [ Chris Hughes (Jul 06 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/slashes%20in%20leanpkg.path/near/129213107):
<p>I don't know if Windows oleans are any different</p>


{% endraw %}
