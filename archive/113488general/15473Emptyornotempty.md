---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15473Emptyornotempty.html
---

## Stream: [general](index.html)
### Topic: [Empty or not empty](15473Emptyornotempty.html)

---


{% raw %}
#### [ Patrick Massot (Dec 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty%20or%20not%20empty/near/152017713):
<p>How can I prove something by case splitting depending on whether or not a type is inhabited? I know about the <code>inhabited</code> and <code>nonempty</code> classes, but it looks like I can't do anything when I assume <code>not (nonempty a)</code> or <code>not (inhabited a)</code>. So what I do is <code>by_cases H : ∃ x : α, true,</code>. Is that right?</p>

#### [ Chris Hughes (Dec 17 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty%20or%20not%20empty/near/152018000):
<p>You can prove <code>a -&gt; false</code> from <code>h : not (nonempty a)</code>, it's just <code>assume x, h ⟨x⟩</code>. Not sure what else you'd need apart from this.</p>

#### [ Patrick Massot (Dec 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty%20or%20not%20empty/near/152018113):
<p>Strange, I thought I tried that. Thanks! I does look slightly less stupid that way</p>


{% endraw %}
