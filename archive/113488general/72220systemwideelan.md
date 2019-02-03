---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72220systemwideelan.html
---

## Stream: [general](index.html)
### Topic: [system-wide elan](72220systemwideelan.html)

---


{% raw %}
#### [ Patrick Massot (Jan 18 2019 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355328):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I'd like to try to build a debian package for local deployment for my course. Is it possible to have a system-wide <code>elan</code> It seems elan always tries to install in the user directory</p>

#### [ Patrick Massot (Jan 18 2019 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355356):
<p>Or should I forget about elan and install Lean directly?</p>

#### [ Sebastian Ullrich (Jan 18 2019 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355757):
<p>You can do a system-wide installation of elan manually - here is Arch Linux's package for rustup for comparison: <a href="https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/rustup#n30" target="_blank" title="https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/rustup#n30">https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/rustup#n30</a></p>

#### [ Patrick Massot (Jan 18 2019 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355844):
<p>Is there a command line argument for elan saying where it should install?</p>

#### [ Sebastian Ullrich (Jan 18 2019 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355892):
<p>But if you're using a single Lean version for your course, there's probably not much to benefit from elan</p>

#### [ Patrick Massot (Jan 18 2019 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356012):
<p>That's probably simpler indeed. Maybe releasing Lean 3.4.2 would also make it feel cleaner</p>

#### [ Sebastian Ullrich (Jan 18 2019 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356038):
<p>Yes, I hope I can get to that today</p>

#### [ Patrick Massot (Jan 18 2019 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356048):
<p>Thanks</p>


{% endraw %}
