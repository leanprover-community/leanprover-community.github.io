---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72538LongStoneCech.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Long Stone-Cech](https://leanprover-community.github.io/archive/116395maths/72538LongStoneCech.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jan 22 2019 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598228):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> <a href="https://github.com/leanprover/mathlib/blob/master/src/topology/stone_cech.lean#L253" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/src/topology/stone_cech.lean#L253">https://github.com/leanprover/mathlib/blob/master/src/topology/stone_cech.lean#L253</a> takes forever to elaborate. Do you care if I change it to:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">stone_cech</span><span class="bp">.</span><span class="n">t2_space</span> <span class="o">:</span> <span class="n">t2_space</span> <span class="o">(</span><span class="n">stone_cech</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">t2_iff_ultrafilter</span><span class="o">,</span>
  <span class="n">rintros</span> <span class="n">g</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">⟩</span> <span class="n">u</span> <span class="n">gx</span> <span class="n">gy</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">γ</span> <span class="n">tγ</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">f</span> <span class="n">hf</span><span class="o">,</span>
  <span class="n">resetI</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">stone_cech_extend</span> <span class="n">hf</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">ff</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">ff</span> <span class="err">⟦</span><span class="n">y</span><span class="err">⟧</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">lim</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ultrafilter</span> <span class="n">α</span><span class="o">,</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="err">⟦</span><span class="n">z</span><span class="err">⟧</span> <span class="bp">→</span> <span class="n">tendsto</span> <span class="n">ff</span> <span class="n">g</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">ff</span> <span class="err">⟦</span><span class="n">z</span><span class="err">⟧</span><span class="o">))</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="n">z</span> <span class="n">gz</span><span class="o">,</span>
    <span class="k">calc</span> <span class="n">map</span> <span class="n">ff</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">map</span> <span class="n">ff</span> <span class="o">(</span><span class="n">nhds</span> <span class="err">⟦</span><span class="n">z</span><span class="err">⟧</span><span class="o">)</span> <span class="o">:</span> <span class="n">map_mono</span> <span class="n">gz</span>
              <span class="bp">...</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="o">(</span><span class="n">ff</span> <span class="err">⟦</span><span class="n">z</span><span class="err">⟧</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">continuous_stone_cech_extend</span> <span class="n">hf</span><span class="o">)</span><span class="bp">.</span><span class="n">tendsto</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">tendsto_nhds_unique</span> <span class="n">u</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">lim</span> <span class="n">x</span> <span class="n">gx</span><span class="o">)</span> <span class="o">(</span><span class="n">lim</span> <span class="n">y</span> <span class="n">gy</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Jan 22 2019 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598235):
<p>which I think is also easier to read by the way</p>

#### [ Reid Barton (Jan 22 2019 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598456):
<p>If it's faster go for it</p>

#### [ Patrick Massot (Jan 22 2019 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598640):
<p>Thanks. I'm asking because this change will be hidden in a large reorganization PR (the second phase of the topology reorganization decided in Amsterdam).</p>

#### [ Reid Barton (Jan 22 2019 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598653):
<p>Oh great, are you already working on that?</p>

#### [ Patrick Massot (Jan 22 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156598677):
<p>Yes. I'm splitting <code>topology.basic</code> and <code>topology.continuity</code></p>

#### [ Patrick Massot (Jan 22 2019 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Long%20Stone-Cech/near/156599697):
<p>And guess what I learned? Non-finishing calls to <code>simp</code> are evil</p>


{% endraw %}
