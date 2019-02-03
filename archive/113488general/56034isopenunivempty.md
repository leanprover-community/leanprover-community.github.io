---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56034isopenunivempty.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [is_open_{univ,empty}](https://leanprover-community.github.io/archive/113488general/56034isopenunivempty.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 04 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866118):
<p>Is there a reason for the following discrepancy?</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">is_open_univ</span>
<span class="c">/-</span><span class="cm"> @[reducible]</span>
<span class="cm">def topological_space.is_open_univ : ∀ {α : Type u} (c : topological_space α), is_open c univ :=</span>
<span class="cm">λ (α : Type u) (c : topological_space α), [topological_space.is_open_univ c] -/</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">is_open_empty</span>
<span class="c">/-</span><span class="cm"> @[simp]</span>
<span class="cm">theorem is_open_empty : ∀ {α : Type u} [_inst_1 : topological_space α], is_open ∅ :=</span>
<span class="cm">λ {α : Type u} [_inst_1 : topological_space α],</span>
<span class="cm">  eq.mpr (id (eq.rec (eq.refl (is_open ∅)) (eq.symm sUnion_empty))) (is_open_sUnion (λ (a : set α), false.elim)) -/</span>
</pre></div>

#### [ Reid Barton (Dec 04 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866186):
<p>You have the wrong <code>is_open_univ</code> I think</p>

#### [ Reid Barton (Dec 04 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866213):
<p>You probably want the root namespace one</p>

#### [ Johan Commelin (Dec 04 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866296):
<p>Aahrg, I see.</p>

#### [ Johan Commelin (Dec 04 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866331):
<p>Otoh, because of proof irrelevance it doesn't really matter which one I'm using, I guess.</p>

#### [ Reid Barton (Dec 04 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866363):
<p>I assumed you were concerned about the type: <code>()</code> vs <code>[]</code></p>

#### [ Johan Commelin (Dec 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866808):
<p>Yes, I was.</p>

#### [ Johan Commelin (Dec 04 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_%7Buniv%2Cempty%7D/near/150866893):
<p>There is all sorts of asymmetry. But using the <code>_root_</code> version solves all my headaches (-;</p>


{% endraw %}
