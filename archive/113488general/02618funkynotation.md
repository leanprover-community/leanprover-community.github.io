---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02618funkynotation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [funky notation](https://leanprover-community.github.io/archive/113488general/02618funkynotation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135168245):
<p>Is this doomed to fail?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_ideal_adic</span> <span class="o">(</span><span class="n">J</span> <span class="o">:</span> <span class="n">set</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">J</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">pow_ideal</span> <span class="n">J</span> <span class="n">n</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">K</span> <span class="o">:</span> <span class="n">set</span> <span class="n">A</span><span class="o">,</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="err">∈</span> <span class="n">K</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">K</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">n</span><span class="o">,</span> <span class="n">pow_ideal</span> <span class="n">J</span> <span class="n">n</span> <span class="err">⊆</span> <span class="n">K</span><span class="o">)</span>

<span class="kn">notation</span> <span class="o">:</span> <span class="bp">`</span><span class="n">is_</span><span class="bp">`</span><span class="n">J</span><span class="bp">`_</span><span class="n">adic</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">is_ideal_adic</span> <span class="n">J</span>
</pre></div>

#### [ Johannes Hölzl (Oct 04 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135168274):
<p>its doomed</p>

#### [ Johan Commelin (Oct 04 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135168386):
<p>That's too bad</p>

#### [ Mario Carneiro (Oct 04 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135193028):
<p>they are just funny looking brackets...</p>

#### [ Johan Commelin (Oct 04 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135193856):
<p>Still it doesn't work )-;</p>

#### [ Reid Barton (Oct 04 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135194568):
<p>Shouldn't have the colon after <code>notation</code></p>

#### [ Johan Commelin (Oct 04 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funky%20notation/near/135194768):
<p>Thanks <span class="user-mention" data-user-id="110032">@Reid Barton</span> it works!</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span><span class="n">is</span><span class="bp">-`</span><span class="n">J</span><span class="bp">`-</span><span class="n">adic</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">is_ideal_adic</span> <span class="n">J</span>

<span class="n">def</span> <span class="n">is_adic</span> <span class="o">(</span><span class="n">A₀</span> <span class="o">:</span> <span class="n">set</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subring</span> <span class="n">A₀</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">J</span> <span class="o">:</span> <span class="n">set</span> <span class="n">A₀</span><span class="o">)</span> <span class="o">[</span><span class="n">hJ</span> <span class="o">:</span> <span class="n">is_ideal</span> <span class="n">J</span><span class="o">],</span>
<span class="o">(</span><span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">topological_subring</span> <span class="n">A₀</span><span class="bp">;</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">hJ</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is</span><span class="bp">-</span><span class="n">J</span><span class="bp">-</span><span class="n">adic</span><span class="o">)</span>
</pre></div>


<p>You can't use underscores, or you'll need to leave spaces...</p>


{% endraw %}
