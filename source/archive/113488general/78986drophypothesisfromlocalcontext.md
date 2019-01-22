---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78986drophypothesisfromlocalcontext.html
---

## [general](index.html)
### [drop hypothesis from local context](78986drophypothesisfromlocalcontext.html)

#### [Johan Commelin (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077557):
Please remind me, which tactic removes hypotheses from the local context? Because I have used up some hyptheses, and I won't use them again, but the proof state is filling an entire screen.

#### [Johan Commelin (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077565):
I couldn't find the tactic in TPIL...

#### [Sean Leather (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077568):
`clear`

#### [Johan Commelin (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077608):
aah, thanks

#### [Sean Leather (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077614):
For reference: https://leanprover.github.io/reference/search.html?q=clear&check_keywords=yes&area=default

#### [Johan Commelin (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077620):
I see it is in TPIL, but the words "drop" or "remove" are not in its description

#### [Sean Leather (May 25 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077635):
You could try browsing [this section](https://leanprover.github.io/reference/tactics.html#basic-tactics) if you're looking for something similar in the future.

#### [Mario Carneiro (May 25 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077636):
You can also use `replace` in place of `have` to clear old hyps as well

#### [Sean Leather (May 25 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077717):
I didn't know about [`replace`](https://github.com/leanprover/mathlib/blob/add172ddc03b10734cb34bdcab77861c94235504/tactic/interactive.lean#L160-L174).

