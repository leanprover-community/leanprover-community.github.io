---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/42069inductionoverconstrainedstructure.html
---

## Stream: [new members](index.html)
### Topic: [induction over constrained structure](42069inductionoverconstrainedstructure.html)

---


{% raw %}
#### [ Gavid Liebnich (Nov 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147588184):
<p>I am slightly stuck on a proof, could anyone point me in the right direction? The tl;dr is that I have a structure <code>X</code> holding <code>n</code> and a proof that <code>h : 0 &lt; n</code>. However, <code>h</code> makes it impossible to do induction on <code>n</code>, because my inductive hypotheses requires me to construct a new <code>X</code> such that <code>h</code> holds, which is untrue for an arbitrary <code>n</code>.</p>
<p>Here's a hopefully small example:</p>
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

<span class="kn">lemma</span> <span class="n">yield_eq_data</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">mapper</span><span class="o">}</span> <span class="o">:</span> <span class="n">yield</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span><span class="bp">.</span><span class="n">data</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">m</span> <span class="k">with</span> <span class="n">n</span> <span class="n">h</span> <span class="n">data</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span> <span class="n">generalizing</span> <span class="n">data</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">cases</span> <span class="n">h</span> <span class="o">},</span>
    <span class="o">{</span>
      <span class="c1">-- ih : ∀ (h : 0 &lt; n)..., which I will never show</span>
    <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>The resulting state has the inductive hypothesis: <code>∀ (h : 0 &lt; n) (data : vector ℕ n), yield {n := n, h := h, data := data} = vector.to_list ({n := n, h := h, data := data}.data)</code>, which is not usable, because I can't show <code>h</code>.</p>

#### [ Mario Carneiro (Nov 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589062):
<p>You can case on whether <code>0 &lt; n</code> or not</p>

#### [ Mario Carneiro (Nov 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589079):
<p>if not, then <code>n = 0</code>, and this is your "actual" base case</p>

#### [ Moses Schönfinkel (Nov 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20over%20constrained%20structure/near/147589595):
<p>(deleted)</p>


{% endraw %}
