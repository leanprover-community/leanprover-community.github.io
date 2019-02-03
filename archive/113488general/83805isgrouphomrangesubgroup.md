---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83805isgrouphomrangesubgroup.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [is_group_hom.range_subgroup](https://leanprover-community.github.io/archive/113488general/83805isgrouphomrangesubgroup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.range_subgroup/near/125304068):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">range_subgroup</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">image_univ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="bp">▸</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">image_subgroup</span> <span class="n">f</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span>
</pre></div>


<p>Could you add this to mathlib? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>


{% endraw %}
