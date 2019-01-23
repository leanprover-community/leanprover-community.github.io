---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08878fromtacticstoterms.html
---

## Stream: [general](index.html)
### Topic: [from tactics to terms](08878fromtacticstoterms.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132682307):
Even though I'm beginning to understand a bit of the `meta`-world, I still don't fully comprehend the tactic monad. For example: is it possible to extract a concrete term from a `begin ... end`-block?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132696207):
Ok, I found `format_result` in Ed's recent docs on `meta`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132696477):
The problem is that I don't see any output anywhere, when I plug it into some `begin ... end` block.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132697545):
You'll need to `trace` it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132697964):
Hmm. Good idea. But `trace tactic.format_result` gives the error
```lean
failed to synthesize type class instance for
⊢ has_to_tactic_format (tactic format)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 24 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132698024):
sounds ironic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132700521):
`trace_state` usually prints a trace.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 24 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132702583):
@**Johan Commelin** See `tactic.trace_result`

