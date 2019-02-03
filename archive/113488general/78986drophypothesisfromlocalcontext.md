---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78986drophypothesisfromlocalcontext.html
---

## Stream: [general](index.html)
### Topic: [drop hypothesis from local context](78986drophypothesisfromlocalcontext.html)

---


{% raw %}
#### [ Johan Commelin (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077557):
<p>Please remind me, which tactic removes hypotheses from the local context? Because I have used up some hyptheses, and I won't use them again, but the proof state is filling an entire screen.</p>

#### [ Johan Commelin (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077565):
<p>I couldn't find the tactic in TPIL...</p>

#### [ Sean Leather (May 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077568):
<p><code>clear</code></p>

#### [ Johan Commelin (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077608):
<p>aah, thanks</p>

#### [ Sean Leather (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077614):
<p>For reference: <a href="https://leanprover.github.io/reference/search.html?q=clear&amp;check_keywords=yes&amp;area=default" target="_blank" title="https://leanprover.github.io/reference/search.html?q=clear&amp;check_keywords=yes&amp;area=default">https://leanprover.github.io/reference/search.html?q=clear&amp;check_keywords=yes&amp;area=default</a></p>

#### [ Johan Commelin (May 25 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077620):
<p>I see it is in TPIL, but the words "drop" or "remove" are not in its description</p>

#### [ Sean Leather (May 25 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077635):
<p>You could try browsing <a href="https://leanprover.github.io/reference/tactics.html#basic-tactics" target="_blank" title="https://leanprover.github.io/reference/tactics.html#basic-tactics">this section</a> if you're looking for something similar in the future.</p>

#### [ Mario Carneiro (May 25 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077636):
<p>You can also use <code>replace</code> in place of <code>have</code> to clear old hyps as well</p>

#### [ Sean Leather (May 25 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/drop%20hypothesis%20from%20local%20context/near/127077717):
<p>I didn't know about <a href="https://github.com/leanprover/mathlib/blob/add172ddc03b10734cb34bdcab77861c94235504/tactic/interactive.lean#L160-L174" target="_blank" title="https://github.com/leanprover/mathlib/blob/add172ddc03b10734cb34bdcab77861c94235504/tactic/interactive.lean#L160-L174"><code>replace</code></a>.</p>


{% endraw %}
