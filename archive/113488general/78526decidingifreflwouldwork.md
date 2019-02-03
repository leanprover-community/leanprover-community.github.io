---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78526decidingifreflwouldwork.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [deciding if `refl` would work](https://leanprover-community.github.io/archive/113488general/78526decidingifreflwouldwork.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 22 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526321):
<p>I have <code>lhs rhs : expr</code>, and I would like to know, if the goal were to be <code>lhs = rhs</code>,  whether or not <code>refl</code> would succeed. I could temporarily make the goal actually <code>lhs = rhs</code>, and try <code>refl</code>, but I'm wondering if it can be done directly.</p>

#### [ Scott Morrison (Apr 22 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526366):
<p>I'm only hesitant to overwrite the goal because the actual current goal may be something completely unrelated to what my tactic is thinking about that the moment it's wondering about <code>lhs = rhs</code>, and it feels kludgy to actually have to use <code>set_goal</code>.</p>

#### [ Scott Morrison (Apr 22 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526377):
<p>The problem is that <code>refl</code> is basically just shorthand for <code>mk_const `eq.refl &gt;&gt;= λ r, apply_core r</code>, and <code>apply_core</code> only unifies with the goal.</p>

#### [ Sebastian Ullrich (Apr 22 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125526830):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Take a look at <code>tactic.solve_aux</code></p>

#### [ Scott Morrison (Apr 22 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125527074):
<p>Thanks <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>. Implicit in your answer is "get over it, just set_goal to whatever you want, it's how you're meant to do this"! Good to know.</p>

#### [ Sebastian Ullrich (Apr 22 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125527212):
<p>If you want to look at it like that, yes :)</p>

#### [ Simon Hudon (Apr 22 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deciding%20if%20%60refl%60%20would%20work/near/125530633):
<p>What if you try to unify them directly? <code>unify lhs rhs</code></p>


{% endraw %}
