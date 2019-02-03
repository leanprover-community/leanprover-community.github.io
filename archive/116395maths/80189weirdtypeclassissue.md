---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80189weirdtypeclassissue.html
---

## Stream: [maths](index.html)
### Topic: [weird type class issue](80189weirdtypeclassissue.html)

---


{% raw %}
#### [ Johan Commelin (Oct 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026131):
<p>Consider this code:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span>

<span class="kn">open</span> <span class="n">category_theory</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">u₁</span> <span class="n">u₂</span> <span class="n">v</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">w</span> <span class="n">w₁</span> <span class="n">w₂</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="c1">--[@has_limits.{u₁ u₂} C 𝒞]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="c1">-- todo should this be done as a subfunctor?</span>
<span class="kn">structure</span> <span class="n">covering_family</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">)</span>
<span class="o">(</span><span class="n">obj</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span>
<span class="o">(</span><span class="n">hom</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">},</span> <span class="n">obj</span> <span class="n">i</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">covering_family</span>

<span class="kn">structure</span> <span class="n">coverage</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">covers</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">C</span><span class="o">},</span> <span class="n">set</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">))</span> <span class="c1">-- red squiggles under &quot;covering_family&quot;</span>
</pre></div>


<p>I get the following error:</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">C</span>
<span class="err">⊢</span> <span class="n">category</span> <span class="n">C</span>
</pre></div>

#### [ Johan Commelin (Oct 18 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026148):
<p>Why are <code>C</code> and the category structure duplicated there? And why can't it resolve the type class issue?</p>

#### [ Johannes Hölzl (Oct 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026219):
<p>what happens if you remove the <code>include</code> and write the variables directly as parameters for <code>coverage</code>?</p>

#### [ Johan Commelin (Oct 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026236):
<p>These includes are all over the place in Scott's library. If you remove it you get red squiggles under the <code>⟶</code> in <code>obj i ⟶ U</code>.</p>

#### [ Johan Commelin (Oct 18 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026298):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">coverage</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">C</span><span class="o">},</span> <span class="n">set</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span>
</pre></div>


<p>gives the error</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">C</span>
<span class="err">⊢</span> <span class="n">category</span> <span class="n">C</span>
</pre></div>


<p>So now the duplication is gone. But it still can't resolve the type class...</p>

#### [ Johan Commelin (Oct 18 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136026368):
<p>The following works but is very ugly.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">coverage</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">C</span><span class="o">},</span> <span class="n">set</span> <span class="o">(</span><span class="bp">@</span><span class="n">covering_family</span> <span class="bp">_</span> <span class="err">𝒞</span> <span class="n">U</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Oct 18 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136034898):
<p>In general I think the fact that we need <code>include 𝒞</code> all the time is a sign that something is wrong. But I have no clue what is wrong and how to fix it.</p>

#### [ Reid Barton (Oct 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136039835):
<p>I usually include the universe parameters when I run into this kind of issue, like <code>covering_family.{u\1 u\2}</code>. (BTW, usually we use a <code>v</code>-type letter for the morphism universe.)<br>
I have no idea about the duplicate display in the error message though.</p>

#### [ Johan Commelin (Oct 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136040495):
<p>I currently have</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposites</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">yoneda</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">equalizers</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">products</span>

<span class="kn">open</span> <span class="n">category_theory</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">u₁</span> <span class="n">u₂</span> <span class="n">v</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">w</span> <span class="n">w₁</span> <span class="n">w₂</span>

<span class="kn">namespace</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">has_coequalizers</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">{</span><span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">)</span>

<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="o">:=</span> <span class="n">has_coequalizers</span><span class="bp">.</span><span class="n">coequalizer</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">f</span> <span class="n">g</span>
<span class="n">def</span> <span class="n">coequalizer</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">X</span>
<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="o">:</span> <span class="n">Z</span> <span class="err">⟶</span> <span class="o">(</span><span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">π</span>
<span class="bp">@</span><span class="o">[</span><span class="n">search</span><span class="o">]</span> <span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">w</span> <span class="o">:</span> <span class="n">f</span> <span class="err">≫</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">≫</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">w</span>
<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="o">:</span> <span class="n">is_coequalizer</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">has_coequalizers</span><span class="bp">.</span><span class="n">is_coequalizer</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span> <span class="n">f</span> <span class="n">g</span>

<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">desc</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">Z</span> <span class="err">⟶</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">f</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span> <span class="err">⟶</span> <span class="n">P</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">desc</span> <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">P</span><span class="o">,</span> <span class="n">π</span> <span class="o">:=</span> <span class="n">h</span><span class="o">,</span> <span class="n">w</span> <span class="o">:=</span> <span class="n">w</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">hom_ext</span> <span class="o">{</span><span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">}</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="n">k</span> <span class="o">:</span> <span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span> <span class="err">⟶</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">k</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">s</span> <span class="o">:</span> <span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span> <span class="o">:=</span> <span class="bp">⟨</span> <span class="bp">⟨</span> <span class="n">X</span> <span class="bp">⟩</span><span class="o">,</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">⟩</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">q</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">uniq</span> <span class="n">s</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">p</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">uniq</span> <span class="n">s</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">q</span><span class="o">,</span> <span class="err">←</span><span class="n">p</span><span class="o">],</span>
  <span class="n">solve_by_elim</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">section</span> <span class="n">presheaf</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₂</span> <span class="n">v₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒳</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">presheaf</span> <span class="o">:=</span> <span class="n">X</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="n">C</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">presheaf</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="n">omit</span> <span class="err">𝒞</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coproducts</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₂</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span>

<span class="kn">end</span> <span class="n">presheaf</span>

<span class="c1">-- todo should this be done as a subfunctor?</span>
<span class="kn">structure</span> <span class="n">covering_family</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">index</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span>
<span class="o">(</span><span class="n">obj</span> <span class="o">:</span> <span class="n">index</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">hom</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">index</span><span class="o">),</span> <span class="n">obj</span> <span class="n">i</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">covering_family</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒳</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span>

<span class="n">def</span> <span class="n">sieve</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">coequalizer</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">sorry</span><span class="o">)</span>
<span class="o">(</span><span class="bp">@</span><span class="n">Sigma</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="bp">×</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="bp">_</span><span class="o">))</span>
<span class="o">(</span><span class="bp">@</span><span class="n">Sigma</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="o">(((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="err">∘</span> <span class="n">f</span><span class="bp">.</span><span class="n">obj</span><span class="o">))</span>
<span class="bp">_</span> <span class="bp">_</span>

<span class="n">def</span> <span class="n">sheaf_condition</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">))</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₂</span> <span class="n">v₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">covering_family</span>

<span class="kn">structure</span> <span class="n">coverage</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">covers</span>   <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">set</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">))</span>
<span class="o">(</span><span class="n">property</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">)),</span>
            <span class="bp">∃</span> <span class="n">h</span> <span class="o">:</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">V</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">j</span> <span class="o">:</span> <span class="n">h</span><span class="bp">.</span><span class="n">index</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">{</span><span class="n">i</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span><span class="o">}</span> <span class="o">{</span><span class="n">k</span> <span class="o">:</span> <span class="n">h</span><span class="bp">.</span><span class="n">obj</span> <span class="n">j</span> <span class="err">⟶</span> <span class="n">f</span><span class="bp">.</span><span class="n">obj</span> <span class="n">i</span><span class="o">},</span>
            <span class="n">h</span><span class="bp">.</span><span class="n">hom</span> <span class="n">j</span> <span class="err">≫</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">k</span> <span class="err">≫</span> <span class="n">f</span><span class="bp">.</span><span class="n">hom</span> <span class="n">i</span><span class="o">)</span>

<span class="n">class</span> <span class="n">site</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">coverage</span> <span class="o">:</span> <span class="bp">@</span><span class="n">coverage</span> <span class="n">X</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">))</span>

<span class="kn">section</span> <span class="n">sheaf</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">site</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₂</span> <span class="n">v₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒳</span> <span class="err">𝒞</span>

<span class="kn">structure</span> <span class="n">sheaf</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">presheaf</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span>
<span class="o">(</span><span class="n">sheaf_condition</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">@</span><span class="n">covering_family</span> <span class="bp">_</span> <span class="err">𝒳</span><span class="bp">.</span><span class="n">to_category</span> <span class="n">U</span><span class="o">)),</span> <span class="n">f</span><span class="bp">.</span><span class="n">sheaf_condition</span> <span class="n">presheaf</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">sheaf</span>



<span class="kn">namespace</span> <span class="n">topological_space</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">site</span> <span class="o">(</span><span class="n">opens</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">coverage</span> <span class="o">:=</span>
  <span class="o">{</span> <span class="n">covers</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">Us</span><span class="o">,</span> <span class="k">begin</span> <span class="n">sorry</span> <span class="c1">-- the union of the Ui should be U</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="n">property</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">topological_space</span>
</pre></div>


<p>Lean is especially unhappy about the part where I try to define the <code>sieve</code>.</p>

#### [ Johan Commelin (Oct 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136040514):
<p>Currently I'm just going to wait till some PR's get merged.</p>

#### [ Reid Barton (Oct 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136041150):
<p>Lots of those <code>_</code>s in sieve still need to be filled in, right?</p>

#### [ Reid Barton (Oct 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136041176):
<p>Or at least... 3 I guess?</p>

#### [ Johan Commelin (Oct 18 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136041777):
<p>Yes, that is right. But I need fibre products for the for the <code>_</code> in the first <code>Sigma</code>. <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Reid Barton (Oct 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136043495):
<blockquote>
<p>In general I think the fact that we need <code>include 𝒞</code> all the time is a sign that something is wrong. But I have no clue what is wrong and how to fix it.</p>
</blockquote>
<p>So there are two issues which come up a lot due to the way category theory uses universe variables.<br>
1. The <code>include 𝒞</code> thing is a workaround for a specific elaborator bug where it doesn't correctly account for universe parameters of variables that have been included by the "square bracket rule". If you hit this bug then you will see an error about something like "bad tactic or buggy elaborator".<br>
2. It also often happens that you have to help Lean out with some explicit universe parameters. I think what is going on is that one of the parameters is not constrained by anything (usually the <code>v</code>), and so Lean is looking for a <code>category.{u ?u_1} C</code> instance. Apparently it's unwilling to take an instance <code>category.{u v} C</code> for some specific <code>v</code> and specialize <code>?u_1</code> to <code>v</code>. I'm not sure whether this is a bug or just something where the system doesn't work in the way we would usually prefer.</p>

#### [ Johan Commelin (Oct 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136043564):
<p>I see. I wouldn't mind if universe unification was slightly more greedy in this case.</p>

#### [ Reid Barton (Oct 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136043615):
<p>Your <code>covering_family</code> thing is the second issue.</p>

#### [ Reid Barton (Oct 18 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136043903):
<p>Maybe we would like to have something like <code>out_param</code> on the universe parameter <code>v</code>, but that's not currently possible</p>

#### [ Reid Barton (Oct 18 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136043980):
<p>Also I don't really understand how <code>out_param</code> works, so I could be way off-base.</p>

#### [ Reid Barton (Oct 18 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136044517):
<p>Maybe the clearest example of this is something like <code>terminal_object (C : Type u) [category.{u v} C] [has_terminal_object.{u v} C] : C</code> where you could have a type <code>C : Type u</code> equipped with two totally different <code>category.{u v}</code> and <code>category.{u w}</code> structures with different terminal objects. The type of <code>terminal_object C</code> is just <code>C</code> which has <code>Type u</code> so there is no way you could ever constrain the <code>v</code> parameter.</p>

#### [ Johan Commelin (Oct 19 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136107468):
<p>The issues aren't gone, but my definition of <code>sieve</code> is converging onto something far more readable then I had before:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposites</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">yoneda</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">open</span> <span class="n">category_theory</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">u₁</span> <span class="n">u₂</span> <span class="n">v</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">w</span> <span class="n">w₁</span> <span class="n">w₂</span>

<span class="kn">namespace</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">has_coequalizers</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">{</span><span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">)</span>

<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="o">:=</span> <span class="n">has_coequalizers</span><span class="bp">.</span><span class="n">coequalizer</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">f</span> <span class="n">g</span>
<span class="n">def</span> <span class="n">coequalizer</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">X</span>
<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="o">:</span> <span class="n">Z</span> <span class="err">⟶</span> <span class="o">(</span><span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">π</span>
<span class="bp">@</span><span class="o">[</span><span class="n">search</span><span class="o">]</span> <span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">w</span> <span class="o">:</span> <span class="n">f</span> <span class="err">≫</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">≫</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">w</span>
<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="o">:</span> <span class="n">is_coequalizer</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">has_coequalizers</span><span class="bp">.</span><span class="n">is_coequalizer</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">C</span> <span class="n">f</span> <span class="n">g</span>

<span class="n">def</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">desc</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">Z</span> <span class="err">⟶</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">f</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span> <span class="err">⟶</span> <span class="n">P</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">desc</span> <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">P</span><span class="o">,</span> <span class="n">π</span> <span class="o">:=</span> <span class="n">h</span><span class="o">,</span> <span class="n">w</span> <span class="o">:=</span> <span class="n">w</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">hom_ext</span> <span class="o">{</span><span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Z</span><span class="o">}</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="n">k</span> <span class="o">:</span> <span class="n">coequalizer</span> <span class="n">f</span> <span class="n">g</span> <span class="err">⟶</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">k</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">s</span> <span class="o">:</span> <span class="n">cofork</span> <span class="n">f</span> <span class="n">g</span> <span class="o">:=</span> <span class="bp">⟨</span> <span class="bp">⟨</span> <span class="n">X</span> <span class="bp">⟩</span><span class="o">,</span> <span class="n">coequalizer</span><span class="bp">.</span><span class="n">π</span> <span class="n">f</span> <span class="n">g</span> <span class="err">≫</span> <span class="n">h</span> <span class="bp">⟩</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">q</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">uniq</span> <span class="n">s</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">p</span> <span class="o">:=</span> <span class="o">(</span><span class="n">coequalizer</span><span class="bp">.</span><span class="n">universal_property</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">uniq</span> <span class="n">s</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">q</span><span class="o">,</span> <span class="err">←</span><span class="n">p</span><span class="o">],</span>
  <span class="n">solve_by_elim</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">section</span> <span class="n">presheaf</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₂</span> <span class="n">v₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒳</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">presheaf</span> <span class="o">:=</span> <span class="n">X</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="n">C</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">presheaf</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="n">omit</span> <span class="err">𝒞</span>
<span class="kn">instance</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">has_coequalizers</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_coequalizers</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">instance</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">has_coproducts</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_coproducts</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">instance</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">has_pullbacks</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_pullbacks</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">presheaf</span>

<span class="c1">-- todo should this be done as a subfunctor?</span>
<span class="kn">structure</span> <span class="n">covering_family</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">index</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span>
<span class="o">(</span><span class="n">obj</span> <span class="o">:</span> <span class="n">index</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">map</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">index</span><span class="o">),</span> <span class="n">obj</span> <span class="n">i</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">covering_family</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒳</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span>

<span class="n">def</span> <span class="n">sieve</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">CP</span> <span class="o">:=</span> <span class="o">(((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="err">∘</span> <span class="n">f</span><span class="bp">.</span><span class="n">obj</span><span class="o">)</span> <span class="k">in</span>
<span class="n">coequalizer</span>
  <span class="o">(</span><span class="n">Sigma</span><span class="bp">.</span><span class="n">desc</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="bp">×</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span><span class="o">),</span> <span class="o">(</span><span class="n">Sigma</span><span class="bp">.</span><span class="n">ι</span> <span class="n">CP</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="err">∘</span> <span class="o">(</span><span class="n">pullback</span><span class="bp">.</span><span class="n">π₁</span> <span class="o">((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span> <span class="o">((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)))))</span>
  <span class="o">(</span><span class="n">Sigma</span><span class="bp">.</span><span class="n">desc</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="bp">×</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span><span class="o">),</span> <span class="o">(</span><span class="n">Sigma</span><span class="bp">.</span><span class="n">ι</span> <span class="n">CP</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="err">∘</span> <span class="o">(</span><span class="n">pullback</span><span class="bp">.</span><span class="n">π₂</span> <span class="o">((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span> <span class="o">((</span><span class="n">yoneda</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)))))</span>

<span class="n">def</span> <span class="n">sheaf_condition</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="n">covering_family</span> <span class="n">U</span><span class="o">))</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₂</span> <span class="n">v₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">covering_family</span>
</pre></div>

#### [ Johan Commelin (Oct 19 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20type%20class%20issue/near/136107519):
<p>But there are still a lot of typeclass issues.</p>


{% endraw %}
