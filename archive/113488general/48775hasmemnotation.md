---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48775hasmemnotation.html
---

## Stream: [general](index.html)
### Topic: [has_mem notation](48775hasmemnotation.html)

---


{% raw %}
#### [ Johan Commelin (Jan 14 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075639):
<p>Does anyone know how to fix this notation hack?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">covering_family</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">Π</span> <span class="o">{{</span><span class="n">V</span><span class="o">}},</span> <span class="n">set</span> <span class="o">(</span><span class="n">V</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">)</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="n">a</span> <span class="bp">`</span><span class="err">∈</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="n">b</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">b</span> <span class="n">a</span> <span class="c1">-- Aaahrg!</span>

<span class="kn">structure</span> <span class="n">coverage</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">covers</span>   <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">set</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">))</span>
<span class="o">(</span><span class="n">property</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">),</span>
            <span class="bp">∀</span> <span class="n">f</span> <span class="err">∈</span> <span class="n">covers</span> <span class="n">U</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">covers</span> <span class="n">V</span><span class="o">,</span>
            <span class="bp">∀</span> <span class="n">Vj</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">Vj</span> <span class="err">⟶</span> <span class="n">V</span><span class="o">),</span> <span class="n">k</span> <span class="err">∈</span> <span class="n">h</span> <span class="bp">→</span>
            <span class="bp">∃</span> <span class="n">Ui</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">),</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">f</span> <span class="bp">∧</span> <span class="bp">∃</span> <span class="n">m</span> <span class="o">:</span> <span class="n">Vj</span> <span class="err">⟶</span> <span class="n">Ui</span><span class="o">,</span> <span class="n">m</span> <span class="err">≫</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">k</span> <span class="err">≫</span> <span class="n">g</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jan 14 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075643):
<p>Ooh, and here is the relevant top of the file</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaf</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">comma</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">full_subcategory</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">where</span>

<span class="n">universes</span> <span class="n">v</span> <span class="n">u</span>

<span class="kn">namespace</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
</pre></div>

#### [ Chris Hughes (Jan 14 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075774):
<p>Could you do a <code>has_mem</code> instance instead?</p>

#### [ Johan Commelin (Jan 14 2019 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155077701):
<p>No, I don't think <code>has_mem</code> works. I want to say that <code>f : V ⟶ U</code> is a member of <code>c</code>. But the type of <code>f</code> depends on <code>V</code>, which ranges over all of <code>X</code>.</p>


{% endraw %}
