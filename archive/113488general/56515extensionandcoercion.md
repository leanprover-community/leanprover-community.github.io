---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56515extensionandcoercion.html
---

## Stream: [general](index.html)
### Topic: [extension and coercion](56515extensionandcoercion.html)

---


{% raw %}
#### [ Patrick Massot (Mar 13 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123660814):
<p>A long time ago, I wrote:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">homeo</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fun_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">inv_fun</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span><span class="bp">⟩</span>
</pre></div>


<p>But now it seems I have trouble, probably because a homeo f and f.to_equiv don't have defeq coercion to function. I'm especially interested in direct images of subsets under homeomorphisms. For instance, I'd like to prove <code>(f : homeo X X) (s : set X) : f '' closure s = closure (f '' s)</code>, using <code>image_closure_subset_closure_image</code> from mathlib</p>

#### [ Patrick Massot (Mar 13 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123660819):
<p>How should I setup this?</p>

#### [ Johannes Hölzl (Mar 13 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123661281):
<p>this works for me</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="bp">=</span> <span class="n">h</span><span class="bp">.</span><span class="n">to_equiv</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Patrick Massot (Mar 13 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123661897):
<p>hum. Maybe the problem is something else. Do you manage to prove my closure lemma using this coercion? In principle this a trivial lemma once you have <code>image_closure_subset_closure_image</code> (to be applied to both f and its inverse)</p>

#### [ Johannes Hölzl (Mar 13 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662202):
<p>My solution looks like this now: </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="kn">open</span> <span class="n">set</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
<span class="kn">structure</span> <span class="n">homeo</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fun_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">inv_fun</span><span class="o">)</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span><span class="bp">⟩</span>
<span class="kn">lemma</span> <span class="n">homeo_coe_to_equiv_coe</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="bp">=</span> <span class="n">h</span><span class="bp">.</span><span class="n">to_equiv</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">lemma</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">image_eq_preimage</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">e</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">ext</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">x</span><span class="o">,</span> <span class="n">mem_image_iff_of_inverse</span> <span class="n">e</span><span class="bp">.</span><span class="n">left_inv</span> <span class="n">e</span><span class="bp">.</span><span class="n">right_inv</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">closure</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">closure</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span>
  <span class="o">(</span><span class="n">image_closure_subset_closure_image</span> <span class="n">f</span><span class="bp">.</span><span class="n">fun_con</span><span class="o">)</span>
  <span class="k">begin</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">homeo_coe_to_equiv_coe</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_equiv</span><span class="bp">.</span><span class="n">image_eq_preimage</span> <span class="o">(</span><span class="n">closure</span> <span class="n">s</span><span class="o">),</span> <span class="err">←</span> <span class="n">image_subset_iff</span><span class="o">],</span>
    <span class="n">refine</span> <span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">image_closure_subset_closure_image</span> <span class="n">f</span><span class="bp">.</span><span class="n">inv_con</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[(</span><span class="n">image_comp</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_equiv</span><span class="bp">.</span><span class="n">inverse_apply_apply</span><span class="o">],</span>
    <span class="k">show</span> <span class="n">closure</span> <span class="o">(</span><span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">closure</span> <span class="n">s</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">image_id</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>
  <span class="kn">end</span>
</pre></div>


<p>One problem is that <code>rw</code> and the simplifier can now see through the coercion. So when you want to apply <code>equiv</code> lemmas you need to apply <code>homeo_coe_to_equiv_coe</code> first. Another solution is to make a <code>calc</code> proof, which might be a little bit nicer and one has the opportunity to state the goal in the required form.</p>

#### [ Patrick Massot (Mar 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662495):
<p>Thanks you very much. I feared needing to invoke something like <code> homeo_coe_to_equiv_coe</code> but it doesn't seem so bad in the end, especially if a calc proof works (I'll try).</p>

#### [ Patrick Massot (Mar 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662522):
<p>I see this is also a good opportunity for my poor man tactic (as Kevin would put it):</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">by_double_inclusion</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">do</span>
<span class="bp">`</span><span class="o">[</span><span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm_iff</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="n">split</span><span class="o">]</span>
</pre></div>


<p>Obviously it's a bit ridiculous but the main point is readablity</p>

#### [ Johannes Hölzl (Mar 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662958):
<p>If you add some infrastructure for <code>homeo</code> it gets also nicer:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">structure</span> <span class="n">homeo</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fun_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_con</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">inv_fun</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">homeo</span><span class="bp">.</span><span class="n">id</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">fun_con</span> <span class="o">:=</span> <span class="n">continuous_id</span><span class="o">,</span> <span class="n">inv_con</span> <span class="o">:=</span> <span class="n">continuous_id</span><span class="o">,</span> <span class="bp">..</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">home</span><span class="bp">.</span><span class="n">id_apply</span> <span class="o">:</span> <span class="o">(</span><span class="n">homeo</span><span class="bp">.</span><span class="n">id</span> <span class="n">α</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="n">homeo</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">β</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">fun_con</span> <span class="o">:=</span> <span class="n">h</span><span class="bp">.</span><span class="n">inv_con</span><span class="o">,</span> <span class="n">inv_con</span> <span class="o">:=</span> <span class="n">h</span><span class="bp">.</span><span class="n">fun_con</span><span class="o">,</span> <span class="bp">..</span> <span class="n">h</span><span class="bp">.</span><span class="n">to_equiv</span><span class="bp">.</span><span class="n">symm</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">homeo</span><span class="bp">.</span><span class="n">symm_comp</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">h</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span> <span class="err">∘</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">homeo</span><span class="bp">.</span><span class="n">id</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">funext</span> <span class="n">h</span><span class="bp">.</span><span class="n">left_inv</span>

<span class="kn">lemma</span> <span class="n">homeo_coe_to_equiv_coe</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="bp">=</span> <span class="n">h</span><span class="bp">.</span><span class="n">to_equiv</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">lemma</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">image_eq_preimage</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">e</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">ext</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">x</span><span class="o">,</span> <span class="n">mem_image_iff_of_inverse</span> <span class="n">e</span><span class="bp">.</span><span class="n">left_inv</span> <span class="n">e</span><span class="bp">.</span><span class="n">right_inv</span>

<span class="kn">lemma</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">subset_image</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">e</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="err">&#39;&#39;</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">image_subset_iff</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">image_eq_preimage</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">closure</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">closure</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span>
  <span class="o">(</span><span class="n">image_closure_subset_closure_image</span> <span class="n">f</span><span class="bp">.</span><span class="n">fun_con</span><span class="o">)</span>
  <span class="o">((</span><span class="n">f</span><span class="bp">.</span><span class="n">to_equiv</span><span class="bp">.</span><span class="n">subset_image</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span>
    <span class="k">calc</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="err">&#39;&#39;</span> <span class="n">closure</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">closure</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">))</span> <span class="o">:</span>
        <span class="n">image_closure_subset_closure_image</span> <span class="n">f</span><span class="bp">.</span><span class="n">inv_con</span>
      <span class="bp">...</span> <span class="bp">=</span> <span class="n">closure</span> <span class="n">s</span> <span class="o">:</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">image_comp</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm_comp</span><span class="o">,</span> <span class="n">home</span><span class="bp">.</span><span class="n">id_apply</span><span class="o">,</span> <span class="n">image_id</span><span class="o">])</span>
</pre></div>


<p>I don't see the value in <code>by_double_inclusion</code>. You could just use <code>apply subset.antisymm</code>. I would prefer if people wrote term style proofs.</p>

#### [ Patrick Massot (Mar 14 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123695171):
<p>Thank you very much <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I'm sorry my Lean time is very fragmented those days, so I suddenly stopped answering. I already had some infrastructure but it is only partially compatible with what you wrote. I'll need time to make the whole story consistent, including probably some more lemmas assuming only injectivity or surjectivity.</p>


{% endraw %}
