---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47161finsetsemilatticesupbot.html
---

## Stream: [new members](index.html)
### Topic: [finset semilattice_sup_bot](47161finsetsemilatticesupbot.html)

---


{% raw %}
#### [ Alistair Tucker (Nov 20 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20semilattice_sup_bot/near/148054444):
<p>Hi! In finset.lean there is</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">semilattice_inf_bot</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">bot</span> <span class="o">:=</span> <span class="err">∅</span><span class="o">,</span> <span class="n">bot_le</span> <span class="o">:=</span> <span class="n">empty_subset</span><span class="o">,</span> <span class="bp">..</span><span class="n">finset</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">}</span>
</pre></div>


<p>but no equivalent instance for semilattice_sup_bot. Is there some good reason for this?</p>

#### [ Johannes Hölzl (Nov 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20semilattice_sup_bot/near/148054870):
<p>I don't see any reason why this is missing.</p>

#### [ Alistair Tucker (Nov 20 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20semilattice_sup_bot/near/148055198):
<p>Thanks</p>


{% endraw %}
