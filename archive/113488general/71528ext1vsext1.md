---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71528ext1vsext1.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [ext1 vs ext : 1](https://leanprover-community.github.io/archive/113488general/71528ext1vsext1.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Sep 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847162):
<p>Is there any difference between <code>ext1</code> and <code>ext : 1</code>?</p>

#### [ Simon Hudon (Sep 28 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847229):
<p>None</p>

#### [ Patrick Massot (Sep 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847278):
<p>Do we want to advertise <code>ext1</code> then? This is different from asking whether it should exist as an internal  part of <code>ext</code></p>

#### [ Patrick Massot (Sep 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847351):
<p>Do we have other tactics taking a natural  number parameter introduced by <code>:</code>?</p>

#### [ Simon Hudon (Sep 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847490):
<blockquote>
<p>Do we have other tactics taking a natural  number parameter introduced by <code>:</code>?</p>
</blockquote>
<p>Not that I know of.</p>

#### [ Simon Hudon (Sep 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847505):
<blockquote>
<p>Do we want to advertise <code>ext1</code> then? This is different from asking whether it should exist as an internal  part of <code>ext</code></p>
</blockquote>
<p>What do you mean by advertise?</p>

#### [ Patrick Massot (Sep 28 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847541):
<p>It's an interactive tactic, and it's mentioned in the docs</p>

#### [ Patrick Massot (Sep 28 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847587):
<p>I'm a bit worried that we have more and more tactics to learn (thanks!) and redundancy may become a small problem</p>

#### [ Simon Hudon (Sep 28 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847624):
<p>So if we were to stop advertising it, we'd take it out of <code>tactic.interactive</code> and remove it from the docs? Or maybe just mention it as part of the doc of <code>ext</code>?</p>

#### [ Simon Hudon (Sep 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847664):
<p>I think you're right about redundancy.</p>

#### [ Mario Carneiro (Sep 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847867):
<p>Is there really no difference? I would have guessed <code>ext1</code> forces an application of extensionality</p>

#### [ Simon Hudon (Sep 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847959):
<p>Initially that was the difference but <span class="user-mention" data-user-id="110524">@Scott Morrison</span> found it more useful if <code>ext</code> would fail if it can't apply at least one extentionality lemma</p>

#### [ Simon Hudon (Sep 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134848009):
<p>With regards to learning tactics, we way want to categorize the ones that we have to make them a bit easier to learn</p>

#### [ Scott Morrison (Sep 29 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858565):
<p>Categorizing them is a good idea. Our approach to documenting new tactics introduced in mathlib so far has been essentially an append-only list of paragraphs describing tactics. :-)</p>

#### [ Simon Hudon (Sep 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858690):
<p>It's still better than before <span class="user-mention" data-user-id="110031">@Patrick Massot</span> started his crusade: most are now documented :D</p>

#### [ Scott Morrison (Sep 29 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858714):
<p>Absolutely! :-)</p>


{% endraw %}
