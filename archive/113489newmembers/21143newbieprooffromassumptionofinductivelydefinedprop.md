---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/21143newbieprooffromassumptionofinductivelydefinedprop.html
---

## Stream: [new members](index.html)
### Topic: [newbie: proof from assumption of inductively defined prop](21143newbieprooffromassumptionofinductivelydefinedprop.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135989819):
<p>[moving to <code>new members</code> stream]. You could prove that <code>ev n</code> was decidable, and then use <code>dec_trivial</code> to decide it.</p>

#### [ Rob Lewis (Oct 17 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135991991):
<p>Proving decidability is the right way to do it in general, but for this example:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">ev</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">h</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
