---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/85969beginnerproofbyinductionquestion.html
---

## Stream: [new members](index.html)
### Topic: [beginner proof by induction question](85969beginnerproofbyinductionquestion.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 30 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133037403):
<p>I'm trying to prove that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msubsup><msub><mi>F</mi><mi>k</mi></msub><mo>=</mo><msub><mi>F</mi><mrow><mn>2</mn><mi>k</mi><mo>−</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex"> \sum_{k=0}^{n-1}F_k = F_{2k-1} </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.954008em;"></span><span class="strut bottom" style="height:1.253718em;vertical-align:-0.29971000000000003em;"></span><span class="base"><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.954008em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">0</span></span></span></span><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361079999999999em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span>, where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>F</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">F_{k}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is the kth Fibonacci number. Here's my attempt so far:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="n">def</span> <span class="n">fibonacci</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fibonacci</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fib_even_sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">sum_even_fib_eq_fib_double_sub_one</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">fib_even_sum</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">f1</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span> <span class="bp">=</span> <span class="n">fib_even_sum</span> <span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">refl</span><span class="o">,</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">fib_even_sum</span><span class="o">,</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">f1</span><span class="o">,</span> <span class="n">sum_even_fib_eq_fib_double_sub_one</span><span class="o">,</span>
<span class="n">add_comm</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_eq_add_one</span><span class="o">,</span> <span class="n">mul_add</span><span class="o">],</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>As you can see, my goal looks like this:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">*</span> <span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>


<p>But I can't figure out how to simplify <code>2*n + 2*1 -1</code> inside <code>fibonacci</code> to <code>2*n - 1</code>. If I could do that then I would happily finish with <code>refl</code>.</p>
<p>Other style or efficiency suggestions would also be appreciated. Is there a smart way to apply <code>simp</code>? I haven't managed that either.</p>

#### [ Kenny Lau (Aug 30 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040385):
<p>what you wrote at the beginning of this message is false</p>

#### [ Kenny Lau (Aug 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040681):
<p>also what you stated in your lean code is false</p>

#### [ Kenny Lau (Aug 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040726):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="n">def</span> <span class="n">fibonacci</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fibonacci</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fib_even_sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">not_sum_even_fib_eq_fib_double_sub_one</span><span class="o">:</span> <span class="bp">¬∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">fib_even_sum</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">absurd</span> <span class="o">(</span><span class="n">H</span> <span class="mi">1</span><span class="o">)</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kenny Lau (Aug 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133042012):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="n">def</span> <span class="n">fibonacci</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fibonacci</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fib_even_sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">sum_even_fib_eq_fib_double_sub_three</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">fib_even_sum</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span> <span class="o">{</span><span class="n">refl</span><span class="o">},</span>
  <span class="n">change</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_assoc</span><span class="o">],</span>
  <span class="n">change</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">fib_even_sum</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">],</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">refl</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">],</span>
  <span class="n">change</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">3</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_add_comm</span><span class="o">],</span> <span class="n">refl</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">clear</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">refl</span><span class="o">},</span>
    <span class="n">change</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">3</span><span class="o">),</span>
    <span class="n">unfold</span> <span class="n">fibonacci</span><span class="o">,</span>
    <span class="n">transitivity</span><span class="o">,</span> <span class="o">{</span><span class="n">exact</span> <span class="n">ih</span><span class="o">},</span>
    <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_add_right</span> <span class="o">},</span>
  <span class="k">from</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 30 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133053991):
<p>Note that your goal about <code>fibonacci (2 * n - 1) + fibonacci (2 * n) = fibonacci (2 * n + 2* 1 - 1)</code> is false if <code>n = 0</code>, because <code>0 - 1 = 0</code>.</p>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133056271):
<p>Ah, thanks! That was  really silly of me... I got lazy because I had previously proved this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">odd</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span>

<span class="n">def</span> <span class="n">fib_odd_sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">odd</span> <span class="n">m</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">sum_odd_fib_eq_fib_double</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">fib_odd_sum</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">f1</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">odd</span> <span class="n">m</span><span class="o">))</span> <span class="bp">=</span> <span class="n">fib_odd_sum</span> <span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">refl</span><span class="o">,</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">fib_odd_sum</span><span class="o">,</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">f1</span><span class="o">,</span> <span class="n">sum_odd_fib_eq_fib_double</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">],</span>
<span class="n">refl</span>
<span class="kn">end</span>
</pre></div>


<p>and I just wanted to copy and paste stuff. Granted, I should still have checked what I was trying to prove...</p>

#### [ Patrick Massot (Aug 30 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133056881):
<p>We will soon have tools to avoid such kind of mistakes</p>

#### [ Kevin Buzzard (Aug 30 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133057027):
<p>You mean Kenny?</p>

#### [ Patrick Massot (Aug 30 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133057171):
<p>I mean the tactic <a href="https://github.com/robertylewis/mathematica_examples/blob/master/src/sanity_check.lean" target="_blank" title="https://github.com/robertylewis/mathematica_examples/blob/master/src/sanity_check.lean">sanity_check</a> that Rob showed in Orsay, Simon's <a href="https://github.com/cipher1024/slim_check" target="_blank" title="https://github.com/cipher1024/slim_check">SlimCheck</a>, and <a href="https://arxiv.org/abs/1606.05945" target="_blank" title="https://arxiv.org/abs/1606.05945">Nunchaku</a> in Lean</p>

#### [ Johannes Hölzl (Aug 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058279):
<p>You find Pablo's Nunchaku-Lean prototype in <a href="https://gitlab.binets.fr/pablo.le-henaff/nunchaku-lean" target="_blank" title="https://gitlab.binets.fr/pablo.le-henaff/nunchaku-lean">https://gitlab.binets.fr/pablo.le-henaff/nunchaku-lean</a></p>

#### [ Johannes Hölzl (Aug 30 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058343):
<p>it doesn't yet implement the dependent type as proposed by the arxiv paper, but hopefully in the future it does</p>

#### [ Patrick Massot (Aug 30 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058502):
<p>is there any documentation explaining how to use it?</p>

#### [ Johannes Hölzl (Aug 30 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133059392):
<p>Not yet. It is only a prototype. Currently, it doesn't even have a <code>leanpkg.toml</code>.<br>
What should work is:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">nunchaku</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">1</span>  <span class="o">:=</span> <span class="k">by</span> <span class="n">nunchaku</span>
</pre></div>


<p>and it should report n = 0 as counterexample.</p>

#### [ Patrick Massot (Aug 30 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133064702):
<p>Thanks. I guess I'll need to see more documentation (including how to install all the dependencies)</p>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133069870):
<p>Returning to my original problem, here's my fixed up proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="n">def</span> <span class="n">fibonacci</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fibonacci</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fib_even_sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span>

<span class="kn">lemma</span> <span class="n">succ_gt_zero</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">):</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">dec_trivial</span>

<span class="kn">theorem</span> <span class="n">sum_even_fib_eq_fib_double_sub_one</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">n</span><span class="bp">&gt;</span><span class="mi">0</span> <span class="bp">→</span> <span class="n">fib_even_sum</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">((</span><span class="n">gt_irrefl</span> <span class="mi">0</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>
<span class="kn">end</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
<span class="n">refl</span>
<span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">f1</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="o">))</span> <span class="bp">=</span> <span class="n">fib_even_sum</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">),</span> <span class="k">by</span> <span class="n">refl</span><span class="o">,</span>
<span class="k">have</span> <span class="n">f2</span> <span class="o">:</span> <span class="n">fib_even_sum</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">),</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">sum_even_fib_eq_fib_double_sub_one</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">succ_gt_zero</span> <span class="n">n</span><span class="o">),</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">fib_even_sum</span><span class="o">,</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">f1</span><span class="o">,</span> <span class="n">add_assoc</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">,</span> <span class="n">f2</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_eq_add_one</span><span class="o">,</span> <span class="n">mul_add</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">],</span>
<span class="n">change</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="n">fibonacci</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">),</span>
<span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133069890):
<p>Thanks to Kenny for his proof as well, which was very instructive.</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333244):
<p>If anyone has a strong stomach, I'd appreciate feedback on this ugly proof of yet another silly Fibonacci fact (this time, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi>F</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mo>−</mo><msub><mi>F</mi><mi>n</mi></msub><msub><mi>F</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mo>(</mo><mo>−</mo><mn>1</mn><msup><mo>)</mo><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">F_{n+1}^2-F_nF_{n+2}=(-1)^n </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999998em;"></span><span class="strut bottom" style="height:1.1205469999999997em;vertical-align:-0.30643899999999996em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999998em;"><span style="top:-2.451892em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.30643899999999996em;"></span></span></span></span></span><span class="mbin">−</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.301108em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">2</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span><span class="mrel">=</span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span>):</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="n">def</span> <span class="n">F</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">F</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">F</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">abcde</span> <span class="o">:</span> <span class="n">a</span><span class="bp">*</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c</span><span class="bp">*</span><span class="n">d</span> <span class="bp">-</span> <span class="o">(</span><span class="n">e</span> <span class="bp">+</span> <span class="n">d</span><span class="bp">*</span><span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">e</span> <span class="bp">-</span> <span class="n">b</span><span class="bp">*</span><span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span> <span class="n">sub_eq_add_neg</span><span class="o">,</span> <span class="n">neg_add</span><span class="o">,</span>
  <span class="err">←</span><span class="n">add_assoc</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">,</span>
  <span class="err">←</span><span class="n">add_assoc</span><span class="o">,</span> <span class="err">←</span><span class="n">add_assoc</span><span class="o">,</span> <span class="n">neg_add_self</span><span class="o">,</span> <span class="n">zero_add</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">mul_comm</span><span class="o">]</span>
<span class="kn">end</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">variable</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="o">[</span><span class="n">parsing_only</span><span class="o">]</span> <span class="bp">`</span><span class="n">F_n</span><span class="bp">`</span> <span class="o">:=</span> <span class="err">↑</span><span class="o">(</span><span class="n">F</span> <span class="n">n</span><span class="o">)</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="o">[</span><span class="n">parsing_only</span><span class="o">]</span> <span class="bp">`</span><span class="n">F_n1</span><span class="bp">`</span> <span class="o">:=</span> <span class="err">↑</span><span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">))</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="o">[</span><span class="n">parsing_only</span><span class="o">]</span> <span class="bp">`</span><span class="n">F_n2</span><span class="bp">`</span> <span class="o">:=</span> <span class="err">↑</span><span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">ex10</span> <span class="o">:</span> <span class="o">((</span><span class="n">F</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span><span class="o">):</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">F</span> <span class="n">n</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">refl</span><span class="o">},</span>
  <span class="n">unfold</span> <span class="n">pow</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">pow</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">pow</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">pow</span> <span class="n">at</span> <span class="n">ih</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">ih</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">],</span>
  <span class="n">change</span> <span class="err">↑</span><span class="o">((</span><span class="n">F</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">F</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)))</span>
    <span class="bp">-</span> <span class="o">(</span><span class="n">F_n1</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F_n1</span> <span class="bp">+</span> <span class="n">F_n2</span><span class="o">))</span>
    <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F_n1</span> <span class="bp">*</span> <span class="n">F_n1</span> <span class="bp">-</span> <span class="n">F_n</span> <span class="bp">*</span> <span class="n">F_n2</span><span class="o">),</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="n">mul_add</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_add</span><span class="o">],</span>
  <span class="n">change</span> <span class="n">F_n2</span> <span class="bp">*</span> <span class="n">F_n</span> <span class="bp">+</span> <span class="n">F_n2</span> <span class="bp">*</span> <span class="n">F_n1</span>
    <span class="bp">-</span><span class="o">(</span><span class="n">F_n1</span> <span class="bp">*</span> <span class="n">F_n1</span> <span class="bp">+</span> <span class="n">F_n1</span> <span class="bp">*</span> <span class="n">F_n2</span><span class="o">)</span>
    <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F_n1</span> <span class="bp">*</span> <span class="n">F_n1</span> <span class="bp">-</span> <span class="n">F_n</span> <span class="bp">*</span> <span class="n">F_n2</span><span class="o">),</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">abcde</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>Is there a better tactic to use for proving <code>abcde</code> (or better, getting around it entirely)? Constructing these long sequences of <code>rw</code>s is very tiresome but I don't have a good idea of when I can throw in <code>simp</code>.</p>

#### [ Patrick Massot (Sep 04 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333346):
<p>abcde is <code>by ring</code></p>

#### [ Patrick Massot (Sep 04 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333369):
<p>don't forget <code>import tactic.ring</code> at top</p>

#### [ Chris Hughes (Sep 04 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333488):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">ex10</span> <span class="o">:</span> <span class="o">((</span><span class="n">F</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span><span class="o">):</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">F</span> <span class="n">n</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">F</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">ih</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span>
    <span class="n">ring</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333501):
<p>Ah, right. I could have sworn I tried that..</p>
<p>Indeed, I can just delete <code>abcde</code> entirely and finish with <code>ring</code>.</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333626):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> that's not working for me, unfortunately...</p>

#### [ Patrick Massot (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333634):
<p>works here</p>

#### [ Chris Hughes (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333646):
<p>Did you import <code>tactic.ring</code>?</p>

#### [ Patrick Massot (Sep 04 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333708):
<p>Chris, can you also golf my limit computation?</p>

#### [ Chris Hughes (Sep 04 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333726):
<p>Probably not. I know nothing about analysis in lean.</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333816):
<p>OK, it works now. I had some other notation in my main file that was interfering somehow.</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334372):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> If you don't mind, could you explain your thought process when you came up with that? For instance, did you peek at my ugly proof first, or did those lemmas immediately jump into your head.</p>
<p>Is the take-away that <code>simp</code>, then <code>ring</code>should be my go-to for this sort of thing?</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334439):
<p><code>ring</code> does equalities between ring expressions, i.e. addition, subtraction, multiplication and powers by constants</p>

#### [ Chris Hughes (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334506):
<p>I used your proof a little bit, to see that I needed induction. Other than that, it's just unfold everything, find some way of substituting in the induction hypothesis, and then hope <code>ring</code> works.</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334537):
<p>Thanks, that's very helpful!</p>


{% endraw %}
