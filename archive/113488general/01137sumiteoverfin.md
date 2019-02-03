---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01137sumiteoverfin.html
---

## Stream: [general](index.html)
### Topic: [sum ite over fin](01137sumiteoverfin.html)

---


{% raw %}
#### [ Johan Commelin (Sep 07 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512435):
<p>How do I kill off this one?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">MWE</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)),</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">k</span><span class="bp">.</span><span class="n">val</span> <span class="bp">*</span> <span class="n">ite</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">R</span><span class="o">))</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Chris Hughes (Sep 07 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512763):
<p><code>finset.sum_eq_single</code></p>

#### [ Kenny Lau (Sep 07 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512793):
<p>not found</p>

#### [ Kenny Lau (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512872):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">universe</span> <span class="n">v</span>

<span class="kn">lemma</span> <span class="n">MWE</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)),</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">k</span><span class="bp">.</span><span class="n">val</span> <span class="bp">*</span> <span class="n">ite</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">R</span><span class="o">))</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">transitivity</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="mi">0</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)))</span> <span class="bp">_</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">symmetry</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_subset</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">i</span> <span class="n">H</span><span class="o">,</span> <span class="n">simp</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">a</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">ne</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a</span><span class="o">]</span> <span class="o">}</span> <span class="o">},</span>
  <span class="n">simp</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512883):
<p>It's actually <code>sum_eq_single</code> due to a naming error.</p>

#### [ Kenny Lau (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512895):
<p>that's the same thing, and still not found</p>

#### [ Johan Commelin (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512898):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> My Lean still doesn't find it.</p>

#### [ Chris Hughes (Sep 07 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133513251):
<p>I think it might be new.</p>


{% endraw %}
