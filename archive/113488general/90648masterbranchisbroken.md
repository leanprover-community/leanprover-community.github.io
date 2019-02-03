---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90648masterbranchisbroken.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [master branch is broken](https://leanprover-community.github.io/archive/113488general/90648masterbranchisbroken.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340328):
<p>Ugh, <code>master</code> is broken in mathlib.</p>

#### [ Scott Morrison (Oct 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340329):
<div class="codehilite"><pre><span></span>arguta:mathlib scott$ git status
On branch master
Your branch is up-to-date with &#39;origin/master&#39;.

nothing to commit, working tree clean
arguta:mathlib scott$ lean --make tests/tactics.lean
/Users/scott/projects/lean/mathlib/tests/tactics.lean:641:2: error: is_def_eq tactic failed, the following expressions are not definitionally equal (remark: is_def_eq tactic does modify the metavariable assignment)
  p : Prop
and
  s : Prop
state:
p q r s : Prop,
h₀ : p ↔ q,
h₁ : q ↔ r,
h₂ : r ↔ s
⊢ p ↔ s
</pre></div>

#### [ Scott Morrison (Oct 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340330):
<p>(I spent 20 minutes trying to work out how my branch had broken something, before realising it wasn't my fault.)</p>

#### [ Simon Hudon (Oct 07 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340368):
<p>My bad. we should comment out those tests while I'm fixing that tactic</p>

#### [ Simon Hudon (Oct 07 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340518):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can you comment out these test cases please?</p>

#### [ Mario Carneiro (Oct 07 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340525):
<p>eh, can you PR it? It takes me an hour to move to and from <code>module</code> branch</p>

#### [ Simon Hudon (Oct 07 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/master%20branch%20is%20broken/near/135340729):
<p>Here you go: <a href="https://github.com/leanprover/mathlib/pull/398" target="_blank" title="https://github.com/leanprover/mathlib/pull/398">https://github.com/leanprover/mathlib/pull/398</a></p>


{% endraw %}
