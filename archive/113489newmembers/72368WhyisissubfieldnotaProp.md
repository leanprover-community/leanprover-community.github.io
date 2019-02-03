---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72368WhyisissubfieldnotaProp.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Why is is_subfield not a Prop?](https://leanprover-community.github.io/archive/113489newmembers/72368WhyisissubfieldnotaProp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Jan 12 2019 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987213):
<p>I want to define</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="n">def</span> <span class="n">subfields</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">K&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="n">L</span> <span class="bp">|</span> <span class="n">is_subfield</span> <span class="n">K&#39;</span><span class="o">}</span>
</pre></div>


<p>But I run into a problem because <code>is_subfield</code> is somehow a <code>Type</code>, not a <code>Prop</code>. Why is this/how is this possible, and how can I fix the problem?</p>

#### [ Chris Hughes (Jan 12 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987224):
<p>By mistake. It should be changed.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 12 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987515):
<p>Do you know how I can circumvent the problem?</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987518):
<p>you can use <code>nonempty (is_subfield K')</code></p>

#### [ Chris Hughes (Jan 12 2019 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987531):
<p><a href="https://github.com/leanprover/mathlib/issues/588" target="_blank" title="https://github.com/leanprover/mathlib/issues/588">#588</a></p>

#### [ Kevin Buzzard (Jan 12 2019 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154990392):
<p>You can now also just update mathlib :-)</p>


{% endraw %}
