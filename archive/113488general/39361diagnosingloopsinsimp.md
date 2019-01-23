---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39361diagnosingloopsinsimp.html
---

## Stream: [general](index.html)
### Topic: [diagnosing loops in `simp`](39361diagnosingloopsinsimp.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 30 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288635):
Can someone remind me what I'm meant to do to diagnose `simp` apparently going into an endless loop, and ending in a timeout? There must be some option to set so I can see which lemmas it is attempting to apply.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 30 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288689):
Ah, okay: `set_option trace.simp_lemmas true`. Curiously in VSCode `set option trace.simp` doesn't include in its autocomplete suggestions `trace.simp_lemmas`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 30 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288696):
Oh, and it's `trace.simplify` that I want anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309134):
Scott -- if this is not mentioned in the simp docs then add one para and make a PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309146):
Or just download

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309147):
https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309188):
and edit it and email it me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309200):
Let's get these answers down in a canonical place.


{% endraw %}
