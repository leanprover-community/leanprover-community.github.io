---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72220systemwideelan.html
---

## Stream: [general](index.html)
### Topic: [system-wide elan](72220systemwideelan.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355328):
@**Sebastian Ullrich** I'd like to try to build a debian package for local deployment for my course. Is it possible to have a system-wide `elan` It seems elan always tries to install in the user directory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355356):
Or should I forget about elan and install Lean directly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 18 2019 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355757):
You can do a system-wide installation of elan manually - here is Arch Linux's package for rustup for comparison: https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/rustup#n30

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355844):
Is there a command line argument for elan saying where it should install?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 18 2019 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156355892):
But if you're using a single Lean version for your course, there's probably not much to benefit from elan

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356012):
That's probably simpler indeed. Maybe releasing Lean 3.4.2 would also make it feel cleaner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 18 2019 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356038):
Yes, I hope I can get to that today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/system-wide%20elan/near/156356048):
Thanks


{% endraw %}
