---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56647xXPxvsxxXPx.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [∃ x ∈ X, P x vs. ∃ x, x ∈  X ∧ P x](https://leanprover-community.github.io/archive/113489newmembers/56647xXPxvsxxXPx.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Sep 22 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134438550):
<p>Up to now I've been using <code>∃ x ∈ X, P x</code> in theorem statements (or also e.g. <code>∃ X ⊆  Y, Q X</code>) (where X : finset a and a has decidable_eq) without really thinking about it. First of all, they look like what I'm used to, and second of all, I've been able to get things to work with them up to now. In lean, they translate to <code>∃ x, ∃ (h : x ∈ X), P x</code> and <code>∃ X, ∃ (H : X ⊆ Y), Q X</code>, and I've just been mindlessly using extra layers of <code>exists.elim</code> / <code>exists.intro</code> to deal with the <code>h</code>'s and <code>H</code>'s in proofs.</p>
<p>Recently I've been defining new functions from these existence theorems using <code>encodable.choose</code> and then defining other functions using <code>encodable.choose_spec</code>to prove things about them. While contemplating the prospect of unwrapping these extra "exists" again, I've come to the realization that maybe it's just much cleaner to use <code>∃ x, x ∈ X ∧ P x</code> everywhere instead. This turns out to break decidability, but I think I've managed to get that sorted by adding an extra instance.</p>
<p>Anyways, I just wanted to see whether my conclusion (avoid <code>∃ x ∈ X, P x</code> in favor of <code>∃ x, x ∈ X ∧ P x</code>) makes sense and whether there are other related pitfalls I should be wary of.</p>

#### [ Kevin Buzzard (Sep 22 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134439149):
<p>(deleted)</p>

#### [ Reid Barton (Sep 22 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134439203):
<p><code>∃ x ∈ X, P x</code> is a pretty well-established idiom. I'm not that familiar with <code>encodable</code> but I think I would be more inclined to make whatever worked with <code>x ∈ X ∧ P x</code> also work with the nested exists. After all, <code>∃ h : P, Q</code> (with <code>Q</code> not mentioning <code>h</code>) is isomorphic to <code>P ∧ Q</code> anyways.</p>

#### [ Bryan Gin-ge Chen (Sep 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134440789):
<p>It is indeed possible to make things work both ways, but I'm still thinking the second way is will be easier in the long run. Here's a toy example showing the flavor of how I've been using <code>encodable.choose_spec</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">encodable</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">E</span> <span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">encodable</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">open</span> <span class="n">finset</span> <span class="n">encodable</span>

<span class="c1">-- implicit nested exists</span>
<span class="kn">theorem</span> <span class="n">foo</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">G</span> <span class="o">:=</span>
<span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">exists_mem_of_ne_empty</span> <span class="n">h</span><span class="o">)</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_inter</span><span class="bp">.</span><span class="n">mp</span> <span class="n">ha</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_inter</span><span class="bp">.</span><span class="n">mp</span> <span class="n">ha</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">foo_e</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">choose</span> <span class="err">$</span> <span class="n">foo</span> <span class="n">h</span>

<span class="c1">-- have to unwrap the extra exists in foo here and elsewhere</span>
<span class="n">def</span> <span class="n">foo_e_spec</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">foo_e</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">F</span> <span class="bp">∧</span> <span class="n">foo_e</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">G</span> <span class="o">:=</span>
<span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">choose_spec</span> <span class="err">$</span> <span class="n">foo</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">ha</span><span class="bp">⟩</span><span class="o">)</span>

<span class="c1">-- only one exists</span>
<span class="kn">theorem</span> <span class="n">bar</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">e</span><span class="o">,</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">F</span> <span class="bp">∧</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">G</span> <span class="o">:=</span>
<span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">exists_mem_of_ne_empty</span> <span class="n">h</span><span class="o">)</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">mem_inter</span><span class="bp">.</span><span class="n">mp</span> <span class="n">ha</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">bar_e</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">choose</span> <span class="err">$</span> <span class="n">bar</span> <span class="n">h</span>

<span class="n">def</span> <span class="n">bar_e_spec</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">F</span> <span class="err">∩</span> <span class="n">G</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">bar_e</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">F</span> <span class="bp">∧</span> <span class="n">bar_e</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">G</span> <span class="o">:=</span>
<span class="n">choose_spec</span> <span class="err">$</span> <span class="n">bar</span> <span class="n">h</span>
</pre></div>

#### [ Patrick Massot (Sep 22 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134442413):
<p>Be sure to read the discussion in <a href="#narrow/stream/113488-general/topic/undead" title="#narrow/stream/113488-general/topic/undead">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead</a> about nested exist</p>

#### [ Bryan Gin-ge Chen (Sep 22 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134442546):
<p>Yeah, I think I tried to use <code>∃! x∈ X</code> once and immediately ran into the issue described there.</p>


{% endraw %}
