---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54381inducedcoinduced.html
---

## Stream: [maths](index.html)
### Topic: [induced, coinduced, ...](54381inducedcoinduced.html)

---


{% raw %}
#### [ Kenny Lau (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116033):
<p>If I have a function f:A-&gt;B with a topology on B, are the following two topologies on A x A the same?<br>
1. equip A with the induced topology, and then do the product topology<br>
2. build fxf:AxA-&gt;BxB and then use the induced topology, where BxB has the product topology</p>

#### [ Kenny Lau (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116036):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Jun 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116082):
<p>They are equal but not defeq</p>

#### [ Kenny Lau (Jun 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116170):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how do you suggest I prove it?</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116227):
<p>you should be able to use some nonsense in the lattice of top spaces to prove it relatively easily</p>

#### [ Kenny Lau (Jun 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116242):
<p>we have <code>induced_le</code> but not <code>le_induced</code>, so...</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116294):
<p>isn't <code>induced</code> defined as some kind of supremum? That gives you a proof approach</p>

#### [ Kenny Lau (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116297):
<p>i'll try</p>

#### [ Kenny Lau (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116302):
<p>(no, prod is supremum, induced isn't)</p>

#### [ Kenny Lau (Jun 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116321):
<p>oh and is there an idiom to obtain the categorical product of two functions?</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116410):
<p>not particularly, <code>embedding_prod_mk</code> just uses <code>(λx:α×γ, (f x.1, g x.2))</code></p>

#### [ Kenny Lau (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116416):
<p>is that an idiom?</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116420):
<p>I suppose</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116471):
<p>I think <code>induced_sup</code> will help</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116474):
<p>and <code>induced_compose</code></p>

#### [ Kenny Lau (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116482):
<p>why are they in <code>continuity</code> @_@</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116486):
<p>because <code>induced</code> is really talking about continuous functions</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116491):
<p>consider <code>continuous_iff_induced_le</code></p>

#### [ Mario Carneiro (Jun 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116539):
<p>also the proofs use continuity arguments</p>

#### [ Kenny Lau (Jun 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116668):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> oh my god I just realized I have been asking the wrong question</p>

#### [ Kenny Lau (Jun 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116683):
<p>f:A-&gt;B be a set-theoretic function, and a topology on A. Are the following two topologies on BxB the same?<br>
1. equip B with coinduced, and then product<br>
2. coinduced from fxf:AxA-&gt;BxB, where AxA has the product topology</p>

#### [ Kenny Lau (Jun 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116684):
<p>let's say f is surjective</p>

#### [ Mario Carneiro (Jun 15 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128117009):
<p>I expect so, try to prove it and find out</p>

#### [ Reid Barton (Jun 15 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118668):
<p>I'm almost certain they are not the same in general.</p>

#### [ Reid Barton (Jun 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118746):
<p>If A-&gt;B is a quotient map, then XxA-&gt;XxB need not be a quotient map. But I don't know the counterexample off-hand.</p>

#### [ Kenny Lau (Jun 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118753):
<p>I just proved it with one extra assumption</p>

#### [ Reid Barton (Jun 15 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118770):
<p>It's true if X is locally compact, or in your original question if A and B are</p>

#### [ Reid Barton (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118814):
<p>what was your extra assumption?</p>

#### [ Kenny Lau (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118818):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hf1</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hf2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">S</span><span class="o">)))</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">prod</span><span class="bp">.</span><span class="n">topological_space</span> <span class="n">β</span> <span class="n">β</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">topological_space</span><span class="bp">.</span><span class="n">coinduced</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span> <span class="n">t</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">topological_space</span><span class="bp">.</span><span class="n">coinduced</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span> <span class="n">t</span><span class="o">)</span>
    <span class="bp">=</span> <span class="bp">@</span><span class="n">topological_space</span><span class="bp">.</span><span class="n">coinduced</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="n">prod</span><span class="bp">.</span><span class="n">topological_space</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="err">∘</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">rfl</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="err">∘</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">prod</span><span class="bp">.</span><span class="n">snd</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">rfl</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="n">f</span> <span class="o">(</span><span class="n">topological_space</span><span class="bp">.</span><span class="n">coinduced</span> <span class="n">f</span> <span class="n">t</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">induced_le_iff_le_coinduced</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">coinduced</span> <span class="n">f</span> <span class="n">t</span><span class="bp">;</span>
<span class="k">from</span> <span class="n">le_antisymm</span>
  <span class="o">(</span><span class="n">lattice</span><span class="bp">.</span><span class="n">sup_le</span>
    <span class="o">(</span><span class="n">induced_le_iff_le_coinduced</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">induced_compose</span><span class="o">,</span> <span class="n">H1</span><span class="o">,</span> <span class="err">←</span> <span class="n">induced_compose</span><span class="o">]</span><span class="bp">;</span>
      <span class="k">from</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">induced_mono</span> <span class="n">H3</span><span class="o">)</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">le_sup_left</span><span class="o">))</span>
    <span class="o">(</span><span class="n">induced_le_iff_le_coinduced</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">induced_compose</span><span class="o">,</span> <span class="n">H2</span><span class="o">,</span> <span class="err">←</span> <span class="n">induced_compose</span><span class="o">]</span><span class="bp">;</span>
      <span class="k">from</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">induced_mono</span> <span class="n">H3</span><span class="o">)</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">le_sup_right</span><span class="o">)))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">S</span> <span class="n">hs</span><span class="o">,</span> <span class="n">is_open_prod_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">hm</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">hf1</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">hf1</span> <span class="n">y</span> <span class="k">in</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">u</span><span class="o">,</span> <span class="n">v</span><span class="o">,</span> <span class="n">hu</span><span class="o">,</span> <span class="n">hv</span><span class="o">,</span> <span class="n">hmu</span><span class="o">,</span> <span class="n">hnv</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">is_open_prod_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hs</span> <span class="n">m</span> <span class="n">n</span> <span class="o">(</span><span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">hm</span><span class="o">,</span> <span class="n">hn</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hxy</span><span class="o">)</span> <span class="k">in</span>
  <span class="bp">⟨</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">u</span><span class="o">,</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">v</span><span class="o">,</span> <span class="n">hf2</span> <span class="n">u</span> <span class="n">hu</span><span class="o">,</span> <span class="n">hf2</span> <span class="n">v</span> <span class="n">hv</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">hmu</span><span class="o">,</span> <span class="n">hm</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">hnv</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">p</span><span class="o">,</span> <span class="n">q</span><span class="bp">⟩</span> <span class="bp">⟨⟨</span><span class="n">P</span><span class="o">,</span> <span class="n">hp1</span><span class="o">,</span> <span class="n">hp2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">Q</span><span class="o">,</span> <span class="n">hq1</span><span class="o">,</span> <span class="n">hq2</span><span class="bp">⟩⟩</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">hp2</span> <span class="n">hq2</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hp2</span><span class="o">,</span> <span class="err">←</span> <span class="n">hq2</span><span class="o">]</span><span class="bp">;</span> <span class="k">from</span> <span class="bp">@</span><span class="n">H</span> <span class="o">(</span><span class="n">P</span><span class="o">,</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">⟨</span><span class="n">hp1</span><span class="o">,</span> <span class="n">hq1</span><span class="bp">⟩⟩</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118820):
<p>that the map be open</p>


{% endraw %}
