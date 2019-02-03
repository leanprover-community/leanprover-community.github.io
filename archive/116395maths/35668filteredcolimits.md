---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35668filteredcolimits.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [filtered colimits](https://leanprover-community.github.io/archive/116395maths/35668filteredcolimits.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Dec 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152355333):
<p>Has anyone been working with filtered colimits? Perhaps <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>?</p>

#### [ Reid Barton (Dec 21 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152355438):
<p>In particular, I need the formula for a filtered colimit of sets shown at <a href="https://stacks.math.columbia.edu/tag/04AX" target="_blank" title="https://stacks.math.columbia.edu/tag/04AX">https://stacks.math.columbia.edu/tag/04AX</a> before Lemma 4.19.2 and perhaps someone has already done this</p>

#### [ Kevin Buzzard (Dec 21 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152361288):
<p>We (and <span class="user-mention" data-user-id="110064">@Kenny Lau</span> ) recently did arbitrary colimits via some tensor product construction. I think Kenny took filtered colimits of commutative rings at some point because even though I tried my hardest to avoid it, I think I ultimately needed them when defining the structure sheaf on Spec(A) (the issue is extending the sheaf from basic opens to an arbitrary open).</p>

#### [ Kevin Buzzard (Dec 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152361924):
<p><a href="https://github.com/leanprover/mathlib/pull/118" target="_blank" title="https://github.com/leanprover/mathlib/pull/118">https://github.com/leanprover/mathlib/pull/118</a></p>

#### [ Kevin Buzzard (Dec 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152362009):
<p>Minor discussion on 17th May about directed systems around line 25. Note that this PR got closed.</p>

#### [ Kevin Buzzard (Dec 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152362014):
<p>Kenny -- will this PR be resurrected one day? I need it for schemes.</p>


{% endraw %}
