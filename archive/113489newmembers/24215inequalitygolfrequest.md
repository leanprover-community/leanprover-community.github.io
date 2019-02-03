---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24215inequalitygolfrequest.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [inequality golf request](https://leanprover-community.github.io/archive/113489newmembers/24215inequalitygolfrequest.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Nov 21 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148130620):
<p>I'm curious to see how simple a lean proof of this can be:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- Thm 1.3 in Hopcroft, Motwani and Ullcroft&#39;s book</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≥</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">x</span> <span class="bp">≥</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>For comparison, here's my ugly rewrite proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">lemma</span> <span class="n">h4</span> <span class="o">:</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
<span class="kn">lemma</span> <span class="n">h5</span> <span class="o">:</span> <span class="o">(</span><span class="mi">5</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="o">(</span><span class="mi">5</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>

<span class="kn">lemma</span> <span class="n">hne</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- simp, ring,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="o">],</span>
  <span class="n">exact</span> <span class="n">pow_pos</span> <span class="o">(</span><span class="n">succ_pos</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">this&#39;&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="mi">5</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">≥</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">):</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="o">(</span><span class="n">div_le_iff</span> <span class="n">hne</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_comm_div</span><span class="o">,</span> <span class="err">←</span><span class="n">mul_div_assoc</span><span class="o">],</span>
  <span class="n">refine</span> <span class="o">(</span><span class="n">le_div_iff</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span><span class="o">,</span>
  <span class="c1">-- simp, ring, simp,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">h4</span><span class="o">,</span> <span class="n">h5</span><span class="o">,</span> <span class="n">cast_pow</span><span class="o">,</span> <span class="n">cast_pow</span><span class="o">,</span> <span class="err">←</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_pow</span><span class="o">,</span> <span class="err">←</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_pow</span><span class="o">,</span> <span class="err">←</span><span class="n">cast_mul</span><span class="o">,</span> <span class="err">←</span><span class="n">cast_mul</span><span class="o">],</span>
  <span class="n">refine</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_le_pow_of_le_left</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_nonneg</span> <span class="bp">_</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span><span class="o">],</span> <span class="n">linarith</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">this&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">≥</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">):</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="mi">2</span> <span class="bp">≥</span> <span class="o">(</span><span class="mi">5</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">norm_num</span>
<span class="bp">...</span> <span class="bp">≥</span> <span class="bp">_</span> <span class="o">:</span> <span class="n">this&#39;&#39;</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≥</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">x</span> <span class="bp">≥</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">x</span><span class="o">,</span> <span class="n">h</span> <span class="k">with</span>
<span class="bp">|</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="bp">|</span> <span class="mi">1</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="bp">|</span> <span class="mi">2</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="bp">|</span> <span class="mi">3</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span> <span class="n">at</span> <span class="n">h</span>
<span class="bp">|</span> <span class="mi">4</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">),</span> <span class="n">hₐ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="mi">2</span> <span class="err">^</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="mi">4</span><span class="o">)</span> <span class="bp">≥</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="mi">4</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">match</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">)</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">thisQ</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">))</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">≥</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">4</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
    <span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span><span class="bp">.</span><span class="mi">2</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">goalQ</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">))</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">≥</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">,</span> <span class="n">cast_mul</span><span class="o">,</span> <span class="n">mul_mul_div</span> <span class="o">(</span><span class="err">↑</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="mi">5</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">hne</span><span class="o">)],</span>
      <span class="n">conv_rhs</span> <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_comm</span><span class="o">,</span> <span class="err">←</span><span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_comm_div</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">]</span> <span class="o">},</span>
      <span class="n">exact</span> <span class="n">mul_le_mul</span> <span class="n">this&#39;</span> <span class="n">thisQ</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">hne</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span>
    <span class="kn">end</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span><span class="bp">.</span><span class="mi">1</span> <span class="n">goalQ</span>
<span class="kn">end</span>
<span class="kn">end</span>
</pre></div>


<p>I tried using <code>linarith</code> at the commented lines but it didn't seem to know how to deal with coercions from <code>nat</code>, even after I put <code>↑a  ≥ 0</code> as a hypothesis. A related question: what's the easiest way to turn a goal like this:</p>
<div class="codehilite"><pre><span></span>(160 + 16 * ↑a) * ↑a ≤ (200 + 25 * ↑a) * ↑a
</pre></div>


<p>into an inequality over <code>nat</code>s (e.g. by getting it into a form where I can use <code>nat.cast_le</code>)?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132450):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">lemma</span> <span class="n">helpful</span> <span class="o">{</span><span class="n">d</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h4</span> <span class="o">:</span> <span class="mi">4</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="n">d</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_le_add_left</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">dec_trivial</span> <span class="n">h4</span><span class="o">)</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">add_mul</span><span class="o">,</span><span class="n">one_mul</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_le_mul_right</span> <span class="bp">_</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">dec_trivial</span> <span class="n">h4</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≥</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">x</span> <span class="bp">≥</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">x</span> <span class="k">with</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">nat</span><span class="bp">.</span><span class="n">eq_or_lt_of_le</span> <span class="n">h</span> <span class="k">with</span> <span class="n">h4</span> <span class="n">h5</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">h4</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h4</span> <span class="o">:</span> <span class="mi">4</span> <span class="bp">≤</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">h5</span><span class="o">,</span>
  <span class="n">exact</span> <span class="k">calc</span> <span class="mi">2</span> <span class="err">^</span> <span class="o">(</span><span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">d</span> <span class="bp">*</span> <span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span>
  <span class="bp">...</span> <span class="bp">≥</span> <span class="n">d</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_le_mul_right</span> <span class="mi">2</span> <span class="o">(</span><span class="n">Hd</span> <span class="n">h4</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_two</span><span class="o">,</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_two</span><span class="o">]</span>
  <span class="bp">...</span> <span class="bp">≥</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span>  <span class="bp">+</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">helpful</span> <span class="n">h4</span><span class="o">)</span> <span class="bp">_</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 21 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132461):
<p>Did I misunderstand the question? I don't understand why you are using rationals.</p>

#### [ Bryan Gin-ge Chen (Nov 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132551):
<p>Yeah, in hindsight that strategy wasn't so smart (I was following the proof from that book which first showed that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>2</mn><mo>≥</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mi mathvariant="normal">/</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">2 \geq (x+1)^2/x^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">2</span><span class="mrel">≥</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mord mathrm">/</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>≥</mo><mn>4</mn></mrow><annotation encoding="application/x-tex">x\geq4</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">≥</span><span class="mord mathrm">4</span></span></span></span>).</p>

#### [ Kevin Buzzard (Nov 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132566):
<p>For <code>(160 + 16 * ↑a) * ↑a ≤ (200 + 25 * ↑a) * ↑a</code> I would try proving the things you want to rewrite with <code>simp</code>. I wrote some stuff about this sort of thing here <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md</a> , maybe that helps.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132622):
<p>I showed that goal too, but I kept everything in nat and showed 2x^2&gt;=(x+1)^2</p>

#### [ Bryan Gin-ge Chen (Nov 21 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132674):
<p>I was looking at that doc but it didn't say anything about inequalities. But maybe you're saying that I'll have to transform the numbers individually.</p>

#### [ Bryan Gin-ge Chen (Nov 21 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148132748):
<p>Or I guess I can probably get simp to do the LHS / RHS all at once.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136108):
<p>I mean you could try things like <code>rw (show (160 + 16 * ↑a) * ↑a = ((160 + 16 * a) * a : nat), by simp)</code></p>

#### [ Kevin Buzzard (Nov 21 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136373):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">((</span><span class="mi">160</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">16</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">200</span> <span class="bp">+</span> <span class="mi">25</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="mi">160</span> <span class="bp">+</span> <span class="mi">16</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">200</span> <span class="bp">+</span> <span class="mi">25</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">((</span><span class="mi">160</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">16</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">160</span> <span class="bp">+</span> <span class="mi">16</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">((</span><span class="mi">200</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">25</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">a</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">200</span> <span class="bp">+</span> <span class="mi">25</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 21 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148136439):
<p>I had to deal with a gazillion of these sorts of things when I was doing my own undergraduate example sheets, and ended up with what I hope is a robust set of techniques. I still sometimes think about a typeclass solution though.</p>

#### [ Bryan Gin-ge Chen (Nov 22 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148147836):
<p>Thanks, this has been very helpful!</p>

#### [ Kevin Buzzard (Nov 22 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148160788):
<p>So here's a question that came up on my undergraduate example sheets. "Show that the rationals are unbounded above in the reals". In maths we would perhaps say "it's a standard result that for all real x there exists a natural n with n &gt; x, so done". As you can imagine, porting this proof to Lean is a great example of how things are harder than they look here (or how they should be)? <span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> you might want to try proving <code>theorem rationals_unbounded (r : ℝ) : ∃ s : ℚ, r &lt; s</code> from <code>exists_nat_gt : ∀ (x : ℝ), ∃ (n : ℕ), x &lt; ↑n</code>. It's just the same sort of kerfuffle. Some idle coding from earlier in the week:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">archimedean</span>

<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">class</span> <span class="n">is_nat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span>

<span class="n">class</span> <span class="n">is_rat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">q</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">is_rat</span> <span class="n">r</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">nat_is_rat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">is_nat</span> <span class="n">r</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_rat</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">unfreeze_local_instances</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">H</span> <span class="k">with</span> <span class="bp">⟨⟨</span><span class="n">n</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩⟩</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨⟨</span><span class="n">n</span><span class="o">,</span><span class="bp">_⟩⟩</span><span class="o">,</span> <span class="c1">-- some stupid refining happening here out of the way</span>
  <span class="n">rw</span> <span class="n">Hn</span><span class="o">,</span> <span class="n">simp</span>
<span class="kn">end</span>

<span class="c1">-- better than exists_nat_gt</span>
<span class="c1">-- can it be written by a machine?</span>
<span class="kn">theorem</span> <span class="n">real</span><span class="bp">.</span><span class="n">exists_nat_gt&#39;</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
    <span class="bp">∃</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">[</span><span class="n">is_nat</span> <span class="n">n</span><span class="o">],</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">exists_nat_gt</span> <span class="n">x</span> <span class="k">in</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="bp">⟨⟨⟨</span><span class="n">n</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩⟩</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩⟩</span>

<span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="n">Hn</span><span class="o">,</span><span class="n">Hx</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">real</span><span class="bp">.</span><span class="n">exists_nat_gt&#39;</span> <span class="n">r</span> <span class="k">in</span>
<span class="k">begin</span>
  <span class="n">haveI</span> <span class="o">:=</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨⟨</span><span class="n">n</span><span class="o">,</span><span class="k">show</span> <span class="n">is_rat</span> <span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">assumption</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>There's some noise earlier on, but the main proof at the end there is very short, and probably could be shorter (it was one of the things that started me off on the <code>use</code> rant on another thread). I've always wondered whether there is something in these typeclasses I'm setting up here.</p>

#### [ Mario Carneiro (Nov 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162299):
<p>I'm confused. What's the difference between <code>exists_nat_gt</code> and what you want?</p>

#### [ Kevin Buzzard (Nov 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162349):
<p>I want a version of exists_nat_gt which only uses real numbers. The problem which I as a number theorist run into is having to switch between nat, rat and real all the time in a way which is very non-intuitive to a mathematician. I am proposing putting nat and rat (and int) typeclasses on real, meaning that you can reason only with real numbers and avoid having to deal with all the casts.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162417):
<p>The issue is not exists_nat_gt, the issue is proving <code>(r : ℝ) : ∃ s : ℚ, r &lt; s</code> using it, which is more than one line in Lean and only one line in maths.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162507):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">archimedean</span>

<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">definition</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">q</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">r</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">exists_nat_gt</span> <span class="n">r</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨⟨</span><span class="n">n</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">refine</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">simp</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>


<p>That is sort-of horrible.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162510):
<p>perhaps you should use <code>exists_rat_gt</code> then</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162559):
<p>also notice that the proof of that is a one liner</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162574):
<p>These one-liners are hard for beginner mathematicians to write. Of this I am certain.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162577):
<p>That's the problem.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162620):
<p>You can say "well, that's the nature of dependent type theory" or "mathematicians are cheats", but at the end of the day they struggle to see what the issue is.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162701):
<p>My typeclass suggestion, which clearly needs work and may never fly, is just an idea I had for trying to make it easier for mathematicians.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162708):
<p>that's probably true, but you've already written lots of documentation about it. What more are you going for?</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162718):
<p>I want to make it easy for beginners.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162761):
<p>I want the proof of <code>rationals_unbounded (r : ℝ) : ∃ s : rat, r &lt; s</code> to <em>be</em> <code>exists_nat_gt</code> rather than being this plus several lines of faffing around.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162810):
<p><code>:= by standard_typeclass_faff using [exists_nat_gt]</code></p>

#### [ Mario Carneiro (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162816):
<p>they aren't literally the same thing, so you can't completely eliminate the faffing, but you can get it down to one line</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162822):
<p>well, you can if you use the library lemma :)</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162824):
<p>They are literally the same thing to a mathematician, and whilst I completely understand that they are not the same thing at all, I want to make this transparent.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162836):
<p>no they are not the same to a mathematician either... one is talking about nats and the other is talking about rats</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162839):
<p>clearly not the same</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162842):
<p>And my conclusions were that when it suits them, mathematicians <em>redefine</em> the rationals to be the subset of the reals which are rational</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162884):
<p>and similarly they redefine the naturals. Mathematicians only work with objects up to canonical isomorphism so they don't even notice that this is happening.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162893):
<p>In that case you have to make an analogous observation that <code>nat</code> is a subset of <code>rat</code> ... it's not zero step no matter how you do it</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162907):
<p>I know it's not zero step, but it's perhaps one tactic.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148162988):
<p>Ultimately I'll just say the same thing one more time -- if in a maths lecture you prove that for all reals x there exists a natural n with n &gt; x, and then you want to deduce that for all reals x there exists a rational q with q &gt; x, the proof in a maths lecture is "what are you talking about? We just did this!" It's 0 lines.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163003):
<p>Because conveniently at this point in the lecturer's brain, a natural <em>is</em> a rational.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163009):
<p>I am hoping that one day we'll have an interface which will enable mathematicians to keep this pretence up.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163015):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">q</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">exists_rat_gt</span> <span class="n">r</span> <span class="k">in</span> <span class="bp">⟨⟨_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩⟩</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Nov 22 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163062):
<p>you cheated, you used <code>exists_rat_gt</code>. And already that line is hard for beginners, who work in tactic mode, to write.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163072):
<div class="codehilite"><pre><span></span>theorem rationals_unbounded (r : ℝ) : ∃ s : S, r &lt; s :=
let ⟨n, h⟩ := exists_nat_gt r in ⟨⟨_, n, rfl⟩, by simpa⟩
</pre></div>

#### [ Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163085):
<p>Can we get rid of all pointy brackets?</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163094):
<p>With my type class idea, I wanted to get pointy bracket usage down to 0</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163102):
<p>you have to inhabit an exists</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163104):
<p>I wanted the output to be a <em>real</em> with a typeclass proving it's a nat.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163150):
<p>Right. So I want to use <code>use</code> to inhabit the exists.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163230):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">exists_nat_gt</span> <span class="n">r</span> <span class="k">with</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span> <span class="n">swap</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">split</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">n</span> <span class="o">}</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">simpa</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163232):
<p>This basically is the culmination of my thoughts so far on this silly issue. That's why I wanted <code>use</code> and that's why I'm thinking about <code>[is_rat r]</code>. But we've moved on from least upper bounds now, so next week I'll be fussing about something else :-) It was just some thoughts on how this part of my course was more difficult than I wanted it to be in Lean, and Bryan's post is another indication of this -- his original post in this thread is a clear indication that mathematicians find it difficult to work with this extra layer of difficulty when nat, rat and real all become different objects, because we are not used to thinking of them like this.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163242):
<p>arguably that is more like a newbie proof</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163245):
<p>just lots of splitting and bashing</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163260):
<p>This simpa proof is my favourite so far. I still don't know what simpa does. Whenever I read the description I still get confused. First we simplify the hypotheses, then the conclusion using some hypotheses, then we look for the conclusion in the hypotheses, or something. Maybe I should work on my <code>simpa</code> understanding.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163313):
<p>Thanks for the <code>simpa</code> proof. I will look at it.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163393):
<p><code>simpa using h</code> simplifies <code>h</code> with the lemmas, then simplifies the goal using the lemmas, then applies <code>assumption</code> to match <code>h</code> with the goal</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163411):
<p>here I never said to use <code>h</code>, so it actually just simplified the goal and then applied assumption</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148163423):
<p>so it is identical to <code>simp; assumption</code> in this case</p>

#### [ Patrick Massot (Nov 22 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148171478):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm not sure I understand what you want. It seems to me that</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rcases</span> <span class="n">exists_nat_gt</span> <span class="n">r</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">use</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">simpa</span>
<span class="kn">end</span>
</pre></div>


<p>is not too bad</p>

#### [ Patrick Massot (Nov 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148173479):
<p>I played a bit with your ideas and, of course, I don't have a really nice answer. Something not too bad that may be worth thinking about:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">def</span> <span class="n">is_rat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">q</span>

<span class="kn">instance</span> <span class="n">nat_is_rat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_rat</span> <span class="n">n</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">come_on</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">repeat</span> <span class="o">{</span> <span class="n">assumption</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply_instance</span> <span class="bp">&lt;|&gt;</span> <span class="n">split</span><span class="o">}]</span>

<span class="kn">theorem</span> <span class="n">rationals_unbounded</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">is_rat</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">exists_nat_gt</span> <span class="n">r</span> <span class="k">with</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">use</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">come_on</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Nov 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148173532):
<p>I'm a bit disappointed that none of our general purpose automation tactic seem to be able to replace my ad hoc one.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175435):
<p>Because none of them ask type class inference for any help? Surely the type class system is supposed to fix these problems before the user sees them?</p>

#### [ Kevin Buzzard (Nov 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175495):
<p>I guess the challenge now is to prove Bryan's lemma using his proof strategy!</p>

#### [ Kevin Buzzard (Nov 22 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175677):
<p>Of course it's a theorem about a rational number x with [is_nat x] or [is_int x] (changing the choice should not change the proof at all) and the hypothesis x ge 4. Ideally no actual nats should show up in the proof at all other than those buried in the typeclass system</p>

#### [ Kevin Buzzard (Nov 22 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175704):
<p>That's the question. I shouldn't be telling Bryan "don't use rat" -- we should be making rat easier to use in this context.</p>

#### [ Kevin Buzzard (Nov 22 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148175713):
<p>Because that's what mathematicians do instinctively</p>

#### [ Scott Morrison (Nov 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268407):
<p>Blech, dealing with inequalities is so awful. :-) I have been avoiding it for a long time!</p>

#### [ Scott Morrison (Nov 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268408):
<p><code>lemma le_pred_of_lt {n m : ℕ} (h : n &lt; m) : n ≤ m - 1 := sorry</code></p>

#### [ Scott Morrison (Nov 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148268500):
<p>ok...</p>
<div class="codehilite"><pre><span></span>lemma le_pred_of_lt {n m : ℕ} (h : n &lt; m) : n ≤ m - 1 :=
pred_le_pred (succ_le_of_lt h)
</pre></div>

#### [ Kevin Buzzard (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269623):
<p>One reason this is annoying is that it's the CS minus there, which doesn't behave as nicely as our minus</p>

#### [ Kenny Lau (Nov 24 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269675):
<p>I think the horse is long dead...</p>

#### [ Scott Morrison (Nov 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148269715):
<p>Yeah, I'm happy enough about this other minus, just miserable that this stuff is still hard.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270331):
<p>I'm just saying that one reason it's hard is that nat minus is poorly behaved, you're in a situation where (a-b)+b isn't a and this will surely make automation harder to write.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270337):
<p>All the lemmas you need should be there somewhere -- the library does a really good job of being complete. Don't forget to import data.nat.basic .</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270503):
<p>in a lot of ways, automation for nat subtraction is similar to automating stuff involving division - you have well definedness conditions that are generated by your statement and they have to be maintained when you rewrite the expression</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/inequality%20golf%20request/near/148270608):
<p>Yes, that's an insightful comment. Mathematicians know that dividing by zero is something one "never does" so we're always prepared to supply that proof that the denominator is non-zero. But it's easy for us to forget the corresponding precondition for nat subtraction, because nat subtraction just doesn't exist in maths. You define division to be random where we don't define it, but you define nat subtraction to be the wrong thing when we have a perfectly good answer which just happens to be a number which is not a nat.</p>


{% endraw %}
