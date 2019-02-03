---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30056CubicalHoTTLibrary.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Cubical HoTT Library](https://leanprover-community.github.io/archive/113488general/30056CubicalHoTTLibrary.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Namdak Tonpa (Jan 07 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154560608):
<p>Greetings to everybody! TWIMC, Ground Zero, cubical base library embedded into Lean 3.4.1: <a href="https://github.com/groupoid/lean" target="_blank" title="https://github.com/groupoid/lean">https://github.com/groupoid/lean</a></p>
<p>Ports to other cubical type checkers: <a href="https://cubical.systems" target="_blank" title="https://cubical.systems">https://cubical.systems</a></p>

#### [ Gabriel Ebner (Jan 07 2019 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154601477):
<p>It's exciting to see other variants of HoTT with new implementations in Lean.  You're probably aware of this, but the reason we're using the <code>@[hott]</code> attribute in <a href="https://github.com/gebner/hott3" target="_blank" title="https://github.com/gebner/hott3">https://github.com/gebner/hott3</a> is because otherwise this kind of HoTT in Lean is inconsistent.  Concretely, the <code>@[hott]</code> attribute checks that we're not using large elimination for the built-in equality type, which allows us to prove that all paths between two points are equal:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ground_zero</span><span class="bp">.</span><span class="n">theorems</span><span class="bp">.</span><span class="n">ua</span>
<span class="n">universes</span> <span class="n">u</span>
<span class="n">hott</span> <span class="n">theory</span>
<span class="kn">open</span> <span class="n">ground_zero</span><span class="bp">.</span><span class="n">structures</span> <span class="n">ground_zero</span><span class="bp">.</span><span class="n">ua</span>

<span class="n">def</span> <span class="n">all_hset</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">hset</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">p</span> <span class="n">q</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">p</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">q</span><span class="bp">;</span> <span class="n">refl</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">inconsistent</span> <span class="o">:</span> <span class="n">empty</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">universe_not_a_set</span><span class="bp">;</span> <span class="n">apply</span> <span class="n">all_hset</span>
</pre></div>

#### [ Uranus Testing (Jan 08 2019 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154621668):
<p>Yes you are right. There is another place where we can get an inconsistency—ground_zero.support.inclusion. With it we can get a proof that generalized circle (or one step truncation, <a href="https://homotopytypetheory.org/2015/07/28/constructing-the-propositional-truncation-using-nonrecursive-hits/" target="_blank" title="https://homotopytypetheory.org/2015/07/28/constructing-the-propositional-truncation-using-nonrecursive-hits/">https://homotopytypetheory.org/2015/07/28/constructing-the-propositional-truncation-using-nonrecursive-hits/</a>) is a prop. But without it we can’t get a right recursors for HITs that were constructed directly from quotients because quot.sound uses built-in equality type.</p>

#### [ Uranus Testing (Jan 08 2019 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cubical%20HoTT%20Library/near/154622491):
<p>Quotients require equality type in Prop: <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/kernel/quotient/quotient.cpp#L61" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/kernel/quotient/quotient.cpp#L61">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/kernel/quotient/quotient.cpp#L61</a>, so we cannot do init_quotient with our (ground_zero.types.eq) equality type.</p>


{% endraw %}
