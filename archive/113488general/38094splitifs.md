---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38094splitifs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [split_ifs](https://leanprover-community.github.io/archive/113488general/38094splitifs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Jun 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536409):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>, could we have <code>split_ifs</code> fail if there are no ifs to split? It's a trivial change, as in <a href="https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1">https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1</a>.</p>

#### [ Gabriel Ebner (Jun 04 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536623):
<p>In general I don't have a preference, as long as it is consistent.  So if we're changing all tactics to fail if they would do nothing, then that's ok.<br>
But this change will make <code>split_ifs</code> always fail, since it recursively calls itself.</p>

#### [ Scott Morrison (Jun 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536647):
<p>ugh, sorry. :-) I will actually test my next fix!</p>

#### [ Scott Morrison (Jun 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536703):
<p>At the moment it is really inconsistent. Last year sometime we convinced Leo that <code>simp</code> and <code>dsimp</code> should fail if they made no progress, and I would love to have everything else gradually switch to this convention.</p>

#### [ Scott Morrison (Jun 04 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536958):
<p>Okay, this one should actually work: <a href="https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1">https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1</a></p>

#### [ Scott Morrison (Jun 04 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127537017):
<p>So far I am just sending PRs for tactics where I run into an inconvenience because they fail silently, and I have to test myself whether they worked. If it would be helpful, I could try to check that all the tactics in mathlib behave this way.</p>

#### [ Gabriel Ebner (Jun 04 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127537138):
<p>Looks good to me if mathlib still builds.</p>


{% endraw %}
