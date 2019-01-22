---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71245autoderivehastostring.html
---

## [general](index.html)
### [auto derive has_to_string](71245autoderivehastostring.html)

#### [Zesen Qian (Jul 21 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069413):
RT, something like this in lean?

#### [Mario Carneiro (Jul 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069676):
No, I don't think this one has a derive handler, although you could totally write one

#### [Simon Hudon (Jul 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069770):
If you don't mind going into `meta`-land, you can derive `has_reflect` for your type and use the following to just pretty-print the Lean expression that corresponds to a value of your type:

```lean
meta def to_string' {α : Type*} [has_reflect α] (x : α) : string := 
(to_fmt (reflect x)).to_string
```

#### [Zesen Qian (Jul 21 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070006):
`has_reflect` asks me to provide a `expr` for every value? Not sure how to do it for my type.

#### [Zesen Qian (Jul 21 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070023):
@**Mario Carneiro** yeah, it's just a very long type.

#### [Simon Hudon (Jul 21 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070026):
You write `@[derive has_reflect]` above your type definition

#### [Mario Carneiro (Jul 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070074):
I meant write a derive handler

#### [Zesen Qian (Jul 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070106):
@**Simon Hudon** very cool, thanks.

#### [Simon Hudon (Jul 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070171):
You're welcome

#### [Simon Hudon (Jul 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070237):
@**Mario Carneiro** Such a derive handler seems like a lot of work but I'm wondering if piggy backing on top of `has_reflect` might help us be extra lazy

