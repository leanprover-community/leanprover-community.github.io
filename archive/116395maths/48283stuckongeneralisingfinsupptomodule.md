---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48283stuckongeneralisingfinsupptomodule.html
---

## Stream: [maths](index.html)
### Topic: [stuck on generalising finsupp.to_module](48283stuckongeneralisingfinsupptomodule.html)

---


{% raw %}
#### [ Johan Commelin (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127201824):
<p>I really don't see why I'm getting stuck here. See the two comment lines just after the first <code>sorry</code>.</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> should this be stronger? [module γ β] → module γ (α →₀ β) -/</span>   <span class="c1">-- yes!</span>
<span class="n">def</span> <span class="n">to_module</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">β</span> <span class="n">γ</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">β</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">smul</span>     <span class="o">:=</span> <span class="k">begin</span>
                <span class="n">intros</span> <span class="n">r</span> <span class="n">f</span><span class="o">,</span>
                <span class="n">apply</span> <span class="n">f</span><span class="bp">.</span><span class="n">map_range</span> <span class="o">((</span><span class="err">•</span><span class="o">)</span> <span class="n">r</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
                <span class="n">simp</span>
              <span class="kn">end</span><span class="o">,</span> <span class="c1">-- (•)</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="k">begin</span>
                <span class="n">intros</span> <span class="n">r</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
                <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
                <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
                <span class="n">simp</span><span class="o">,</span>
                <span class="n">rw</span> <span class="n">smul_add</span><span class="o">,</span>
                <span class="n">sorry</span>
  <span class="kn">end</span><span class="o">,</span> <span class="c1">-- assume a x y, finsupp.ext $ by simp [mul_add], -- original</span>
  <span class="c1">-- assume a x y, finsupp.ext $ by simp [map_range,smul_add], -- why doesn&#39;t this one work? &lt;=====</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="c1">--assume a x y, finsupp.ext $ by simp [add_mul],</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="k">assume</span> <span class="n">x</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="k">assume</span> <span class="n">r</span> <span class="n">s</span> <span class="n">x</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_smul</span><span class="o">],</span>
  <span class="bp">..</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">add_comm_group</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (May 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127202256):
<p>Never mind. I just realised that <code>is_linear_map</code> is not a class. Not going down the rabbit hole of modules.</p>

#### [ Kenny Lau (May 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127202261):
<p><code>linear_map</code> is</p>

#### [ Johan Commelin (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127202328):
<p>And where does that beast live?</p>

#### [ Johan Commelin (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127202329):
<p>not in algebra/module</p>

#### [ Johan Commelin (May 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/stuck%20on%20generalising%20finsupp.to_module/near/127202473):
<p>Ok, I found it... thanks!</p>


{% endraw %}
