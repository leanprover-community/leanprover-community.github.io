---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99635customleaninelan.html
---

## Stream: [general](index.html)
### Topic: [custom lean in elan](99635customleaninelan.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 11 2019 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154915008):
Is there some low-tech way to just copy files in `~/.elan` around if I want to try running Lean with a modified core library?
Say by `cd ~/.elan; cp -a lean-3.4.1 lean-3.4.1a`? Probably I need to do something else, as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 11 2019 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154915280):
This should work.  You can also add symlinks to a lean git checkout.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 11 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154919876):
It did just work.

