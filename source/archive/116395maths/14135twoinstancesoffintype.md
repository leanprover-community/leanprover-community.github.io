---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14135twoinstancesoffintype.html
---

## [maths](index.html)
### [two instances of fintype](14135twoinstancesoffintype.html)

#### [Casper Putz (Jan 18 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156362890):
Hi, I have the following code where I explicitely constructed an equivalence between two types ``α`` and ``β → γ``, and all types are fintypes. I want to conclude that ``α.card = γ.card ^ β.card`` but I have a problem with instances. I would like to something like this:

```lean
import data.fintype
open fintype

variables {α : Type*} {β : Type*} {γ : Type*}
variables [fintype α] [fintype β] [fintype γ]
variables [decidable_eq α]
variables (f : α ≃ (β → γ))

example : card α = card γ ^ card β :=
calc card α = @card (β → γ) (of_equiv α f) : eq.symm $ of_equiv_card f
        ... = card γ ^ card β : card_fun
```

The problem is I have two different instances of ``fintype (β → γ) ``. The one coming from ``fintype.of_equiv`` (which ``of_equiv_card`` uses) and one coming from ``pi.fintype`` (which ``card_fun`` uses).  How could I solve this? Or should I try a completely different route?

#### [Chris Hughes (Jan 18 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156363177):
Something like this?
```lean
example : card α = card β ^ card γ :=
calc card α = @card (β → γ) (of_equiv α f) : eq.symm $ of_equiv_card f
        ... = card (β → γ) : by congr
        ... = card γ ^ card β : card_fun
```

#### [Casper Putz (Jan 18 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156363562):
Yes! I also needed ``[decidable_eq β]``, but then it worked :). Thanks!

