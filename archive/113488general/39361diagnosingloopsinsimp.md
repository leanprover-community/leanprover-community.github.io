---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39361diagnosingloopsinsimp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [diagnosing loops in `simp`](https://leanprover-community.github.io/archive/113488general/39361diagnosingloopsinsimp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (May 30 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288635):
<p>Can someone remind me what I'm meant to do to diagnose <code>simp</code> apparently going into an endless loop, and ending in a timeout? There must be some option to set so I can see which lemmas it is attempting to apply.</p>

#### [ Scott Morrison (May 30 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288689):
<p>Ah, okay: <code>set_option trace.simp_lemmas true</code>. Curiously in VSCode <code>set option trace.simp</code> doesn't include in its autocomplete suggestions <code>trace.simp_lemmas</code>.</p>

#### [ Scott Morrison (May 30 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127288696):
<p>Oh, and it's <code>trace.simplify</code> that I want anyway.</p>

#### [ Kevin Buzzard (May 30 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309134):
<p>Scott -- if this is not mentioned in the simp docs then add one para and make a PR.</p>

#### [ Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309146):
<p>Or just download</p>

#### [ Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309147):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md</a></p>

#### [ Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309188):
<p>and edit it and email it me.</p>

#### [ Kevin Buzzard (May 30 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diagnosing%20loops%20in%20%60simp%60/near/127309200):
<p>Let's get these answers down in a canonical place.</p>


{% endraw %}
