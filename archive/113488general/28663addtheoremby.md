---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28663addtheoremby.html
---

## Stream: [general](index.html)
### Topic: [add_theorem_by](28663addtheoremby.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151486):
<p>Why does this fail?</p>
<div class="codehilite"><pre><span></span>meta  def  foo : tactic unit :=
do tactic.add_theorem_by `bar [] (expr.const `unit []) (do tactic.constructor, return ()),
tactic.add_theorem_by `baz [] (expr.const `unit []) (do
bar ← tactic.get_local `bar,
tactic.exact bar,
return ()),
return ()
</pre></div>

#### [ Simon Hudon (Mar 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151531):
<p>What error do you get?</p>

#### [ Jakob von Raumer (Mar 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151537):
<p>"get_local tactic failed, unknown 'bar'"</p>

#### [ Simon Hudon (Mar 24 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151623):
<p>Ah I see! You need <code>resolve_name</code></p>

#### [ Simon Hudon (Mar 24 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151626):
<p><code>get_local</code> is only for local constants</p>

#### [ Jakob von Raumer (Mar 24 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151804):
<p>Is there a resource for more beautiful fresh local names than <code>mk_fresh_name</code>?</p>

#### [ Mario Carneiro (Mar 24 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151860):
<p>yes, I think it is called <code>get_unused_name</code></p>


{% endraw %}
