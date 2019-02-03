---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30267morelimitstuff.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [more limit stuff](https://leanprover-community.github.io/archive/116395maths/30267morelimitstuff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 17 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151910753):
<p>I've got the following lemmas</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_map</span> <span class="o">{</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">K</span><span class="o">]</span> <span class="o">[</span><span class="n">has_colimits_of_shape</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">K</span> <span class="n">C</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">{</span><span class="n">E₁</span> <span class="n">E₂</span> <span class="o">:</span> <span class="n">K</span> <span class="err">⥤</span> <span class="n">J</span><span class="o">}</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">E₁</span> <span class="err">⟹</span> <span class="n">E₂</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">F</span> <span class="n">E₁</span> <span class="bp">=</span> <span class="n">colim</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">whisker_right</span> <span class="n">α</span> <span class="n">F</span><span class="o">)</span> <span class="err">≫</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">F</span> <span class="n">E₂</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext1</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
  <span class="n">conv</span> <span class="o">{</span><span class="n">to_rhs</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span><span class="n">category</span><span class="bp">.</span><span class="n">assoc</span><span class="o">},</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_id</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span>
<span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">F</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">=</span> <span class="n">colim</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">left_unitor</span> <span class="n">F</span><span class="o">)</span><span class="bp">.</span><span class="n">hom</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span>

<span class="kn">lemma</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_comp</span>
<span class="o">{</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">K</span><span class="o">]</span> <span class="o">[</span><span class="n">has_colimits_of_shape</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">K</span> <span class="n">C</span><span class="o">]</span>
<span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">L</span><span class="o">]</span> <span class="o">[</span><span class="n">has_colimits_of_shape</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">L</span> <span class="n">C</span><span class="o">]</span>
<span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="n">K</span> <span class="err">⥤</span> <span class="n">J</span><span class="o">)</span> <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">L</span> <span class="err">⥤</span> <span class="n">K</span><span class="o">)</span> <span class="o">:</span>
<span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">F</span> <span class="o">(</span><span class="n">D</span> <span class="err">⋙</span> <span class="n">E</span><span class="o">)</span> <span class="bp">=</span> <span class="n">colim</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">associator</span> <span class="n">D</span> <span class="n">E</span> <span class="n">F</span><span class="o">)</span><span class="bp">.</span><span class="n">hom</span>
<span class="err">≫</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="bp">_</span> <span class="n">D</span> <span class="err">≫</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">F</span> <span class="n">E</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tidy</span> <span class="o">{</span><span class="n">trace_result</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
  <span class="n">erw</span> <span class="err">←</span> <span class="n">category</span><span class="bp">.</span><span class="n">assoc</span><span class="o">,</span>
  <span class="n">erw</span> <span class="n">colim_ι_map</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">associator</span> <span class="n">D</span> <span class="n">E</span> <span class="n">F</span><span class="o">)</span><span class="bp">.</span><span class="n">hom</span> <span class="n">j</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">functor</span><span class="bp">.</span><span class="n">associator</span><span class="o">],</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">erw</span> <span class="n">is_colimit</span><span class="bp">.</span><span class="n">fac</span><span class="o">,</span>
  <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>


<p>Should I put these (and their duals) into a new PR? Or should this be cast into some other form first?</p>

#### [ Reid Barton (Dec 17 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911327):
<p>Isn't the third one <code>colimit.pre_pre</code>?</p>

#### [ Reid Barton (Dec 17 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911330):
<p>Oh I missed the actual second one.</p>

#### [ Reid Barton (Dec 17 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911339):
<p>The associator is a definitional equality, so you don't really need it.</p>

#### [ Reid Barton (Dec 17 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911403):
<p>Though sometimes Lean tries to be too smart, and gets confused by the reassociation unless you spell things out for it.</p>

#### [ Johan Commelin (Dec 17 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/152007178):
<p>Aah, I see. So the third one can go. That leaves the other 2.</p>


{% endraw %}
