---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86899constructingaclassforih.html
---

## Stream: [general](index.html)
### Topic: [constructing a class for ih](86899constructingaclassforih.html)

---


{% raw %}
#### [ Gavid Liebnich (Nov 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147882679):
<p>Could anyone point me in a right direction in this proof?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">vector</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>

<span class="n">def</span> <span class="n">between</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">}</span>

<span class="n">class</span> <span class="n">c_mapper</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span>
  <span class="o">(</span><span class="n">n</span>       <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span>       <span class="o">:</span> <span class="bp">Π</span><span class="n">m</span><span class="o">,</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
  <span class="o">(</span><span class="n">data</span>    <span class="o">:</span> <span class="bp">Π</span><span class="n">m</span><span class="o">,</span> <span class="n">between</span> <span class="mi">0</span> <span class="o">(</span><span class="n">n</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">structure</span> <span class="n">mapper</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">data</span> <span class="o">:</span> <span class="n">vector</span> <span class="bp">ℕ</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">indexed_mapper_is_c_mapper</span> <span class="o">:</span>
  <span class="n">c_mapper</span> <span class="n">mapper</span> <span class="o">:=</span> <span class="o">{</span>
    <span class="n">n</span>       <span class="o">:=</span> <span class="bp">λ</span><span class="n">m</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">n</span><span class="o">,</span>
    <span class="n">h</span>       <span class="o">:=</span> <span class="bp">λ</span><span class="n">m</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">h</span><span class="o">,</span>
    <span class="n">data</span>    <span class="o">:=</span> <span class="bp">λ</span><span class="n">m</span> <span class="n">x</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">data</span><span class="bp">.</span><span class="n">nth</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span>
  <span class="o">}</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">c_mapper</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">yield</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span>
      <span class="n">c_mapper</span><span class="bp">.</span><span class="n">data</span> <span class="n">m</span> <span class="err">∘</span> <span class="bp">λ</span><span class="n">n</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">c_mapper</span><span class="bp">.</span><span class="n">n</span> <span class="n">m</span><span class="o">)},</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">sorry</span><span class="bp">⟩</span>
    <span class="o">)</span>
    <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">attach</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="err">$</span> <span class="n">c_mapper</span><span class="bp">.</span><span class="n">n</span> <span class="n">m</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">yield_len</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span> <span class="o">(</span><span class="n">yield</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">c_mapper</span><span class="bp">.</span><span class="n">n</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize</span> <span class="n">h</span> <span class="o">:</span> <span class="n">yield</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">l</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">l</span> <span class="k">with</span> <span class="n">x</span> <span class="n">xs</span> <span class="n">ih</span> <span class="n">generalizing</span> <span class="n">m</span><span class="o">,</span>
    <span class="o">{</span>
      <span class="c1">-- yield m = [] is contradictory</span>
      <span class="n">admit</span>
    <span class="o">},</span>
    <span class="o">{</span>
      <span class="c1">-- How to construct α for ih?</span>
    <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>I don't suppose there is at all a way to construct a new <code>α</code> here for the <code>ih</code> in <code>yield_len</code>  - it's a <code>class</code>. Do I need to reformulate the entire statement? Or do I need to do induction over something different there?</p>

#### [ Kenny Lau (Nov 17 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147883055):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">vector</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>

<span class="n">def</span> <span class="n">between</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">}</span>

<span class="n">class</span> <span class="n">c_mapper</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">m</span><span class="o">,</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
<span class="o">(</span><span class="n">data</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">m</span><span class="o">,</span> <span class="n">between</span> <span class="mi">0</span> <span class="o">(</span><span class="n">n</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">structure</span> <span class="n">mapper</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span>
<span class="o">(</span><span class="n">data</span> <span class="o">:</span> <span class="n">vector</span> <span class="bp">ℕ</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">indexed_mapper_is_c_mapper</span> <span class="o">:</span> <span class="n">c_mapper</span> <span class="n">mapper</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">n</span>    <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">n</span><span class="o">,</span>
  <span class="n">h</span>    <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">h</span><span class="o">,</span>
  <span class="n">data</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">x</span><span class="o">,</span> <span class="n">m</span><span class="bp">.</span><span class="n">data</span><span class="bp">.</span><span class="n">nth</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">c_mapper</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">yield</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="err">$</span> <span class="n">c_mapper</span><span class="bp">.</span><span class="n">n</span> <span class="n">m</span><span class="o">)</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span>
<span class="n">c_mapper</span><span class="bp">.</span><span class="n">data</span> <span class="n">m</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="bp">_</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span>

<span class="kn">lemma</span> <span class="n">yield_len</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span> <span class="o">(</span><span class="n">yield</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">c_mapper</span><span class="bp">.</span><span class="n">n</span> <span class="n">m</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">length_map</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">length_attach</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_range</span> <span class="bp">_</span>
</pre></div>

#### [ Gavid Liebnich (Nov 17 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884558):
<p>Alright this works in this particular case, however, what if I actually need to do induction on something that will require a value of some class type - such as occurs in this case if I do happen to do induction and I get to a state with ih <code>∀ (m : α), yield m = xs → list.length xs = c_mapper.n m</code>. Providing this <code>m</code> doesn't seem possible to me, because it's just some <code>α</code> that's known to be <code>[c_mapper α]</code>.</p>

#### [ Kenny Lau (Nov 17 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884574):
<p>I don't think induction on <code>yield m</code> is a good idea in this case anyway</p>

#### [ Gavid Liebnich (Nov 17 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20a%20class%20for%20ih/near/147884616):
<p>What would one do induction on then?</p>


{% endraw %}
