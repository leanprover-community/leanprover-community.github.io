---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02379extractimpfromiff.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [extract `imp` from `iff`](https://leanprover-community.github.io/archive/113488general/02379extractimpfromiff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 07 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135330842):
<p>I'd like a function <code>meta imp_of_iff : expr -&gt; tactic expr</code>, that takes a lemma that says, <code>\Pi (...), P \iff Q</code>, and gives me instead the lemma <code>\Pi (...), P \to Q</code>. Has anyone seen this lying around somewhere in mathlib? It's probably not too hard, I'm just hoping it's already done!</p>

#### [ Scott Morrison (Oct 07 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331375):
<p>Ugh, okay, I revise that, I'm finding it hard. :-)</p>

#### [ Scott Morrison (Oct 07 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331435):
<p>Ah, maybw <code>tactic/alias.lean</code> has <code>mk_iff_mp_app</code>, which seems promising.</p>

#### [ Scott Morrison (Oct 07 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331537):
<p>Hmm, not clear that helps, it seems tied to actual declarations.</p>

#### [ Scott Morrison (Oct 07 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331975):
<p>Sorted it out. <code>tactic/alias.lean</code> has everything I need.</p>


{% endraw %}
