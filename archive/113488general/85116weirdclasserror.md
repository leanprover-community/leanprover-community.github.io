---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85116weirdclasserror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [weird class error](https://leanprover-community.github.io/archive/113488general/85116weirdclasserror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Dec 07 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060003):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">limits</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">types</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">open</span> <span class="n">category_theory</span>

<span class="kn">section</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">[</span><span class="n">limits</span><span class="bp">.</span><span class="n">has_colimits</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>
<span class="n">def</span> <span class="n">is_good</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">is_good_of_has_object</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_good</span> <span class="n">C</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">MyCat</span> <span class="o">:=</span> <span class="kt">Type</span> <span class="n">v</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="n">MyCat</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">dunfold</span> <span class="n">MyCat</span><span class="bp">;</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">limits</span><span class="bp">.</span><span class="n">has_colimits</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span> <span class="n">v</span><span class="o">}</span> <span class="n">MyCat</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">dunfold</span> <span class="n">MyCat</span><span class="bp">;</span> <span class="n">apply_instance</span>
<span class="kn">lemma</span> <span class="n">MyCat_is_good</span> <span class="o">:</span> <span class="n">is_good</span> <span class="n">MyCat</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="o">:=</span> <span class="n">is_good_of_has_object</span> <span class="n">MyCat</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">error: failed to synthesize type class instance for</span>
<span class="cm">⊢ Π (J : Type v) (𝒥 : small_category J) (F : J ⥤ MyCat), limits.has_colimit F</span>
<span class="cm">error: synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized</span>
<span class="cm">  ⁇</span>
<span class="cm">inferred</span>
<span class="cm">  λ (J : Type v) (𝒥 : small_category J) (F : J ⥤ MyCat), MyCat.category_theory.limits.has_colimits F</span>
<span class="cm">-/</span>
</pre></div>

#### [ Reid Barton (Dec 07 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060023):
<p>Is my definition</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">def</span> <span class="n">has_colimits</span> <span class="o">:=</span>
<span class="bp">Π</span> <span class="o">{</span><span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="err">𝒥</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">J</span><span class="o">},</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">has_colimits_of_shape</span> <span class="n">J</span> <span class="n">C</span>
</pre></div>


<p>already asking too much of the class system?</p>

#### [ Reid Barton (Dec 07 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060658):
<p>Also strange: if I change <code>has_colimits</code> to a structure, then I need to add universe annotations to many of its use sites, even if I control for all the variables I'm aware of (same syntactic return universe, both assigned <code>class</code> after the fact, both given <code>elab_simple</code>)</p>

#### [ Johan Commelin (Dec 07 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151120501):
<p>I think I witnessed similar problems when I tried to get the stuff on presheaves in line with the merged limits PR. But I didn't investigate further.</p>


{% endraw %}
