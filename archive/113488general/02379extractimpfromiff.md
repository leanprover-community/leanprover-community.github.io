---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02379extractimpfromiff.html
---

## Stream: [general](index.html)
### Topic: [extract `imp` from `iff`](02379extractimpfromiff.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135330842):
I'd like a function `meta imp_of_iff : expr -> tactic expr`, that takes a lemma that says, `\Pi (...), P \iff Q`, and gives me instead the lemma `\Pi (...), P \to Q`. Has anyone seen this lying around somewhere in mathlib? It's probably not too hard, I'm just hoping it's already done!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331375):
Ugh, okay, I revise that, I'm finding it hard. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331435):
Ah, maybw `tactic/alias.lean` has `mk_iff_mp_app`, which seems promising.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331537):
Hmm, not clear that helps, it seems tied to actual declarations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extract%20%60imp%60%20from%20%60iff%60/near/135331975):
Sorted it out. `tactic/alias.lean` has everything I need.

