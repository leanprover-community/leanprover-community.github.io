---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/91939algebraicclosureconstruction.html
---

## Stream: [maths](index.html)
### Topic: [algebraic closure construction](91939algebraicclosureconstruction.html)

---


{% raw %}
#### [ Chris Hughes (Jan 23 2019 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156722066):
<p>So I'm trying out Tom Hales' construction of algebraic closure. The argument is to use zorn on this type ordered by subset, such that the inclusion map is a field hom.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extensions</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="err">Σ</span> <span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">big_type</span> <span class="n">K</span><span class="o">),</span> <span class="n">discrete_field</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">s</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">h</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">embedding</span> <span class="n">K</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_field_hom</span> <span class="o">(</span><span class="n">inclusion</span> <span class="n">h</span><span class="o">)</span> <span class="bp">∧</span>
    <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">in_algebraic_closure</span> <span class="bp">_</span> <span class="o">(</span><span class="n">inclusion</span> <span class="n">h</span><span class="o">)</span> <span class="n">x</span><span class="o">}</span>
</pre></div>


<p>This involves putting a field structure on the Union of a chain within this type. This is very messy. All the operations are noncomputable, and to prove <code>add_assoc</code>, I end up with four different definitions of addition, with a tactic state like this.</p>
<div class="codehilite"><pre><span></span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">set</span> <span class="err">↥</span><span class="o">(</span><span class="n">extensions</span> <span class="n">K</span><span class="o">),</span>
<span class="n">hc</span> <span class="o">:</span> <span class="n">chain</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="o">:</span> <span class="err">↥</span><span class="o">(</span><span class="n">extensions</span> <span class="n">K</span><span class="o">)),</span> <span class="n">m</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="n">c</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="err">↥⋃</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="err">↥</span><span class="n">c</span><span class="o">),</span> <span class="o">((</span><span class="n">s</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span>
<span class="err">⊢</span> <span class="o">(</span><span class="bp">⟨</span><span class="err">↑</span><span class="n">z</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">+</span> <span class="bp">⟨</span><span class="o">(</span><span class="bp">⟨</span><span class="err">↑</span><span class="n">x</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">+</span> <span class="bp">⟨</span><span class="err">↑</span><span class="n">y</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span>
    <span class="o">(</span><span class="bp">⟨</span><span class="err">↑</span><span class="n">x</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">+</span> <span class="bp">⟨</span><span class="o">(</span><span class="bp">⟨</span><span class="err">↑</span><span class="n">y</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">+</span> <span class="bp">⟨</span><span class="err">↑</span><span class="n">z</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span>
</pre></div>


<p>Is there a nicer approach?</p>

#### [ Johannes Hölzl (Jan 23 2019 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726657):
<p>Just to understand how you need to continue: since <code>hc</code> tells you that <code>c</code> forms a chain it is enough to select a maximal element and know that <code>x</code>, <code>y</code>, or <code>z</code> are all in this maximal field.</p>

#### [ Chris Hughes (Jan 23 2019 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726730):
<p>Yes, but that's quite a messy argument.</p>

#### [ Johannes Hölzl (Jan 23 2019 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726737):
<p>it is</p>

#### [ Kenny Lau (Jan 23 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726839):
<p>I just realized today that Artin's construction does not require splitting fields.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726862):
<p>Wasn't I telling you this last Thursday?</p>

#### [ Kenny Lau (Jan 23 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726869):
<p>maybe I wasn't listening :P</p>

#### [ Kevin Buzzard (Jan 23 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156726892):
<p>I think you convinced me it did, and then I tried to convince Neil in Amsterdam and he convinced me it didn't :-)</p>

#### [ Johannes Hölzl (Jan 23 2019 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156727502):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I don't know how these proofs work in general. But maybe you need to write more infrastructure around <code>extensions</code>. First, instead of defining it as a <code>set</code> a <code>Type</code> may be more helpful. You need to add a <code>partial_order</code> type class on it, then use <code>zorn_partial_order</code>. Also provide a local <code>discrete_field (field_of_extension ...)</code> instance. Then at least the type class instances shouldn't be a problem. In the end the work is the same, but it might be clearer to see what is required</p>

#### [ Chris Hughes (Jan 24 2019 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156793586):
<p>I thought about this, and I've realised it would be easy if we had direct limit.</p>

#### [ Kenny Lau (Jan 24 2019 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156793603):
<p>no, direct limit is the easiest part</p>

#### [ Kenny Lau (Jan 24 2019 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebraic%20closure%20construction/near/156793622):
<p>but I might work on direct limit today</p>


{% endraw %}
