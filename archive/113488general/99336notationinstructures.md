---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99336notationinstructures.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation in structures](https://leanprover-community.github.io/archive/113488general/99336notationinstructures.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 22 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156598822):
<p>Can someone explain me how notation in structures works? Simon changed the definition of a category to:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">category</span> <span class="o">(</span><span class="n">obj</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="o">(</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">hom</span>      <span class="o">:</span> <span class="n">obj</span> <span class="bp">→</span> <span class="n">obj</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="o">(</span><span class="kn">infixr</span> <span class="bp">`</span> <span class="err">⟶</span> <span class="bp">`</span><span class="o">:</span><span class="mi">10</span> <span class="o">:=</span> <span class="n">hom</span><span class="o">)</span> <span class="c1">-- Interesting!</span>
<span class="o">(</span><span class="n">id</span>       <span class="o">:</span> <span class="bp">Π</span> <span class="n">X</span> <span class="o">:</span> <span class="n">obj</span><span class="o">,</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="kn">notation</span> <span class="bp">`</span><span class="mi">𝟙</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">id</span><span class="o">)</span>
<span class="o">(</span><span class="n">comp</span>     <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">obj</span><span class="o">},</span> <span class="o">(</span><span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">X</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">))</span>
<span class="o">(</span><span class="kn">infixr</span> <span class="bp">`</span> <span class="err">≫</span> <span class="bp">`</span><span class="o">:</span><span class="mi">80</span> <span class="o">:=</span> <span class="n">comp</span><span class="o">)</span>
<span class="o">(</span><span class="n">id_comp&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">obj</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">),</span> <span class="mi">𝟙</span> <span class="n">X</span> <span class="err">≫</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
<span class="o">(</span><span class="n">comp_id&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">obj</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">),</span> <span class="n">f</span> <span class="err">≫</span> <span class="mi">𝟙</span> <span class="n">Y</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
<span class="o">(</span><span class="n">assoc&#39;</span>   <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">W</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">obj</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">W</span> <span class="err">⟶</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">),</span>
  <span class="o">(</span><span class="n">f</span> <span class="err">≫</span> <span class="n">g</span><span class="o">)</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">≫</span> <span class="o">(</span><span class="n">g</span> <span class="err">≫</span> <span class="n">h</span><span class="o">)</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
</pre></div>


<p>But if I <code>#print category</code>, then I don't see this notation being introduced, even though it's still used by the pretty printer.</p>

#### [ Reid Barton (Jan 22 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156598955):
<p>I assumed the notation commands are still logically independent of the structure, they are just interspersed in the file (so that you can use the notation earlier).</p>

#### [ Sebastian Ullrich (Jan 22 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156599043):
<p>Local notations (in sections or structures) are gone completely after parsing. Just like tactic blocks are gone after elaboration.</p>

#### [ Johan Commelin (Jan 22 2019 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156599310):
<p>Ok, so why does the pretty printer use the notation when I ask for <code>#print category</code>? Because the notation was reintroduced afterwards?</p>

#### [ Sebastian Ullrich (Jan 22 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156599501):
<p>Ah, yes</p>

#### [ Johan Commelin (Jan 22 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20structures/near/156599516):
<p>Ok, thanks. Everything's cleared up (-;</p>


{% endraw %}
