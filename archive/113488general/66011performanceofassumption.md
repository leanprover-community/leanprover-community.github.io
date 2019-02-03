---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66011performanceofassumption.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [performance of `assumption`](https://leanprover-community.github.io/archive/113488general/66011performanceofassumption.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Oct 31 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136852607):
<p>I just encountered a weird performance issue. In the middle of a rather long proof, I have just proved a fact that I want to use next. If I use <code>exact this</code>, this takes less than 3ms. But <code>assumption</code> takes 7 seconds... Of course, in this specific case this is not a problem, but first I was using a tactic that calls <code>assumption</code>, several times in the proof, and the whole proof then took more than 30s. Is there a way to understand what is going on?</p>
<p>My goal looks like <code>dist (⇑f x') (⇑g x') ≤ ε / 4</code>. The output of the profiler on <code>assumption</code> is</p>
<div class="codehilite"><pre><span></span><span class="n">elaboration</span><span class="o">:</span> <span class="n">tactic</span> <span class="n">compilation</span> <span class="n">took</span> <span class="mi">3</span><span class="bp">.</span><span class="mi">03</span><span class="n">ms</span>
<span class="n">essai</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">520</span><span class="o">:</span><span class="mi">29</span><span class="o">:</span> <span class="n">information</span> <span class="n">tactic</span> <span class="n">profile</span> <span class="n">data</span>

<span class="n">elaboration</span><span class="o">:</span> <span class="n">tactic</span> <span class="n">execution</span> <span class="n">took</span> <span class="mi">7</span><span class="bp">.</span><span class="mi">06</span><span class="n">s</span>
<span class="n">num</span><span class="bp">.</span> <span class="n">allocated</span> <span class="n">objects</span><span class="o">:</span>  <span class="mi">153</span>
<span class="n">num</span><span class="bp">.</span> <span class="n">allocated</span> <span class="n">closures</span><span class="o">:</span> <span class="mi">126</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">find_same_type</span><span class="bp">._</span><span class="n">main</span><span class="bp">._</span><span class="n">lambda_1</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">find_same_type</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="bp">._</span><span class="n">lambda_1</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">unify</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">istep</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="bp">_</span><span class="n">interaction</span><span class="bp">._</span><span class="n">lambda_2</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">scope_trace</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">interaction_monad_orelse</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">istep</span><span class="bp">._</span><span class="n">lambda_1</span>
 <span class="mi">7060</span><span class="n">ms</span>   <span class="mi">100</span><span class="bp">.</span><span class="mi">0</span><span class="err">%</span>   <span class="n">tactic</span><span class="bp">.</span><span class="n">step</span>
</pre></div>


<p>For the record, here is the list of the local facts I have. The issue is probably coming from one of them...</p>
<div class="codehilite"><pre><span></span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">β</span><span class="o">,</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_4</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_5</span> <span class="o">:</span> <span class="n">compact_space</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_6</span> <span class="o">:</span> <span class="n">compact_space</span> <span class="n">β</span><span class="o">,</span>
<span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">,</span>
<span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span>
<span class="n">εpos</span> <span class="o">:</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">εpos8</span> <span class="o">:</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">b_lim</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">δ</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">δ</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">},</span> <span class="n">dist</span> <span class="n">x</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">b</span> <span class="n">x</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">),</span>
<span class="n">δ</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span>
<span class="n">δpos</span> <span class="o">:</span> <span class="n">δ</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">hδ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">},</span> <span class="n">dist</span> <span class="n">x</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">b</span> <span class="n">x</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">,</span>
<span class="n">tα</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span>
<span class="n">this_h_w</span> <span class="o">:</span> <span class="n">tα</span> <span class="err">⊆</span> <span class="n">univ</span><span class="o">,</span>
<span class="n">finite_tα</span> <span class="o">:</span> <span class="n">finite</span> <span class="n">tα</span><span class="o">,</span>
<span class="n">htα</span> <span class="o">:</span> <span class="n">univ</span> <span class="err">⊆</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">tα</span><span class="o">),</span> <span class="n">ball</span> <span class="n">x</span> <span class="n">δ</span><span class="o">,</span>
<span class="n">tβ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">,</span>
<span class="n">this_h_w_1</span> <span class="o">:</span> <span class="n">tβ</span> <span class="err">⊆</span> <span class="n">univ</span><span class="o">,</span>
<span class="n">finite_tβ</span> <span class="o">:</span> <span class="n">finite</span> <span class="n">tβ</span><span class="o">,</span>
<span class="n">htβ</span> <span class="o">:</span> <span class="n">univ</span> <span class="err">⊆</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">tβ</span><span class="o">),</span> <span class="n">ball</span> <span class="n">y</span> <span class="o">(</span><span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">),</span>
<span class="n">fin_univ</span> <span class="o">:</span> <span class="n">finite</span> <span class="n">univ</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">,</span>
<span class="n">hF</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">F</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">tβ</span> <span class="bp">∧</span> <span class="n">dist</span> <span class="n">y</span> <span class="o">(</span><span class="n">F</span> <span class="n">y</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">,</span>
<span class="n">approx</span> <span class="o">:</span> <span class="n">bounded_continuous_map</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">→</span> <span class="err">↥</span><span class="n">tα</span> <span class="bp">→</span> <span class="err">↥</span><span class="n">tβ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">bounded_continuous_map</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="err">↥</span><span class="n">tα</span><span class="o">),</span> <span class="bp">⟨</span><span class="n">F</span> <span class="o">(</span><span class="err">⇑</span><span class="n">f</span> <span class="err">↑</span><span class="n">a</span><span class="o">),</span> <span class="bp">_⟩</span><span class="o">,</span>
<span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">bounded_continuous_map</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span>
<span class="n">f_eq_g</span> <span class="o">:</span> <span class="n">approx</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">approx</span> <span class="n">g</span><span class="o">,</span>
<span class="n">hg</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">dist</span> <span class="o">(</span><span class="err">⇑</span><span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="err">⇑</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span> <span class="n">y</span><span class="o">),</span>
<span class="n">hf</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">dist</span> <span class="o">(</span><span class="err">⇑</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="err">⇑</span><span class="n">f</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span> <span class="n">y</span><span class="o">),</span>
<span class="n">x</span> <span class="n">x&#39;</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">x&#39;tα</span> <span class="o">:</span> <span class="n">x&#39;</span> <span class="err">∈</span> <span class="n">tα</span><span class="o">,</span>
<span class="n">hx&#39;</span> <span class="o">:</span> <span class="n">dist</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="bp">&lt;</span> <span class="n">δ</span><span class="o">,</span>
<span class="n">F_f_g</span> <span class="o">:</span> <span class="n">F</span> <span class="o">(</span><span class="err">⇑</span><span class="n">f</span> <span class="n">x&#39;</span><span class="o">)</span> <span class="bp">=</span> <span class="n">F</span> <span class="o">(</span><span class="err">⇑</span><span class="n">g</span> <span class="n">x&#39;</span><span class="o">),</span>
<span class="n">this</span> <span class="o">:</span> <span class="n">b</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span> <span class="n">x&#39;</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span> <span class="n">b</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x&#39;</span> <span class="n">x</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span> <span class="n">dist</span> <span class="o">(</span><span class="err">⇑</span><span class="n">f</span> <span class="n">x&#39;</span><span class="o">)</span> <span class="o">(</span><span class="err">⇑</span><span class="n">g</span> <span class="n">x&#39;</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">4</span>
</pre></div>


<p>(one bonus point for you if you can guess which theorem I am proving from this output :)</p>

#### [ Rob Lewis (Oct 31 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136854109):
<p>You could try <code>clear</code>ing hypotheses one by one until <code>assumption</code> succeeds quickly. This would at least point out which hypothesis is causing the problem.</p>

#### [ Rob Lewis (Oct 31 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136854136):
<p>Just to check -- if you remove the hypothesis that you want it to find, it takes 7 seconds and then fails, right?</p>

#### [ Sebastien Gouezel (Oct 31 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136855236):
<p>Excellent idea. Here is the minimized outcome, which really looks like a bug somewhere.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foo</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">8</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">8</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">4</span><span class="o">)</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">4</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">assumption</span>
</pre></div>


<p>takes 8 seconds. Remove <code>a</code> or <code>b</code>, it goes down by 4 seconds. Without any of them, 3ms...</p>

#### [ Sebastien Gouezel (Oct 31 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136855749):
<p>The problem is that 4 and 8 are big numbers for reals. You can trigger the same problem with rationals if you increase slightly the numbers:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foo</span> <span class="o">{</span><span class="n">x</span> <span class="n">z</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">100</span><span class="o">)</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">100</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">assumption</span>
</pre></div>


<p>triggers a timeout on my machine...</p>

#### [ Floris van Doorn (Oct 31 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136856013):
<p>If I make the definition of inequality irreducible in <code>real.basic</code>:</p>
<div class="codehilite"><pre><span></span>protected def le (x y : ℝ) : Prop := x &lt; y ∨ x = y
instance : has_le ℝ := ⟨real.le⟩
[...]
attribute [irreducible] real.le
</pre></div>


<p>then <code>assumption</code> is instant again. Apparently <code>assumption</code> had to do an awful lot of unfolding. <br>
Probably <code>lt</code> and <code>le</code> in <code>real</code> should be irreducible, after some basic facts have been proven about it.</p>

#### [ Chris Hughes (Oct 31 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136856465):
<p>I think I remember Mario saying something about <code>assumption</code> trying to reduce all the hypotheses. I guess <code>le</code> and division are hard to reduce on reals. This example takes 11s to fail on my machine.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">x</span> <span class="n">z</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
</pre></div>


<p>Maybe <code>le</code> and division should be irreducible.</p>

#### [ Sebastien Gouezel (Oct 31 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136856827):
<p>Your example is not specific to reals:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">x</span> <span class="n">z</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">100</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
</pre></div>


<p>also fails.</p>

#### [ Rob Lewis (Oct 31 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136858710):
<p>Making the orders on <code>rat</code> and <code>real</code> irreducible only breaks things at one spot in <code>analysis.complex</code>, and then all of these examples are instant. I think this is the correct setup. I'll PR this in a sec.</p>

#### [ Sebastien Gouezel (Oct 31 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136859630):
<p>Thanks a lot!</p>

#### [ Kevin Buzzard (Oct 31 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136859919):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> maybe it's about time you went through all of mathlib changing all <code>assumption</code>s to what they are supposed to say?</p>

#### [ Kenny Lau (Oct 31 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136859956):
<p>good idea</p>

#### [ Kenny Lau (Oct 31 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136859973):
<p>but why am I the only one to make mathlib faster?</p>

#### [ Johan Commelin (Oct 31 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136861850):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> maybe it's about time you went through all of mathlib changing all <code>assumption</code>s to what they are supposed to say?</p>
</blockquote>
<p>What is this? <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I really think we should improve the system. These things should be solved by making the computer smarter, instead of making our proofs more explicit. Automation is good.</p>

#### [ Kevin Buzzard (Oct 31 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136861889):
<p>But <code>assumption</code> will never be as fast as <code>exact H57</code> ;-)</p>

#### [ Johan Commelin (Oct 31 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136861957):
<p>It should be fast enough that we don't have to care. And caching should make sure that we also don't need to care about 10s proofs.</p>

#### [ Mario Carneiro (Nov 01 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136887687):
<p>I think this is a major problem for Sebastien's proof style, which uses <code>&lt;x ≤ ε /2&gt;</code> in place of <code>h1</code> all over the place, and avoids labeling hypotheses. This is turned into <code>show x ≤ ε /2, by assumption</code> and hence can be very slow if there are "similar" hypotheses that require a lot of unfolding. This is one of the reasons I prefer naming hypotheses - it's shorter, and faster.</p>

#### [ Mario Carneiro (Nov 01 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136887835):
<p>The short answer is "<code>assumption</code> considered harmful". This is why stuff like <code>rw [...], refl</code> sometimes succeeds where <code>rw [...]</code> fails, because <code>rw</code> tries to close with reflexivity but it doesn't try very hard for performance reasons. <code>assumption</code> has no such limiter.</p>

#### [ Johan Commelin (Nov 01 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136903475):
<p>I am really unhappy with "<code>assumption</code> considered harmful". Is this a theoretical problem? Or could someone with enough skills and free time write a faster version of <code>assumption</code>?</p>

#### [ Andrew Ashworth (Nov 01 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136903672):
<p>you could potentially write a "dumber" version of assumption that doesn't do as much definitional unfolding, and that would indeed be faster, but also potentially less useful</p>

#### [ Kenny Lau (Nov 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136907300):
<p>... or we can dovetail it?</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136907364):
<p>Isn't <code>assumption</code> being asked to do the impossible? The claim is that there's a term in the local context whose type is that of the goal. A human might go through each of the terms and say "no, no, maybe, no, no, no, ...ooh! Yes!"</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136907406):
<p>but Lean gets interested in the "maybe" and what can you do?</p>

#### [ Kenny Lau (Nov 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136907846):
<p>we can dovetail it.</p>

#### [ Johan Commelin (Nov 01 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136909675):
<p>I think this is a good idea. But I have no idea how to implement the dovetailing in Lean. (For those who don't know what dovetailing is: basically just look at all the assumptions in parallel, if one works, stop looking at the others.)</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136909782):
<p>Ha ha, and then the one tactic which I understand the Lean code for will be gone :-)</p>

#### [ Mario Carneiro (Nov 01 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136910450):
<p>Yes it's possible to do <code>assumption</code> in parallel, but it's overkill</p>

#### [ Mario Carneiro (Nov 01 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136910504):
<p><code>assumption</code> is one of the oldest and simplest tactics, and I think its simplicity is turning out to not be a good thing</p>

#### [ Mario Carneiro (Nov 01 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136910540):
<p>The easy solution is just not to use full defeq in <code>assumption</code></p>

#### [ Mario Carneiro (Nov 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136910568):
<p>just set <code>md := semireducible</code> like all the newer tactics</p>

#### [ Reid Barton (Nov 01 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136920250):
<p>The slow examples above aren't really specific to <code>le</code>, by the way--this one is also slow</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">8</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">+</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
</pre></div>

#### [ Reid Barton (Nov 01 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136920384):
<p>With bigger numbers, even addition is slow.</p>

#### [ Floris van Doorn (Nov 01 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136923924):
<blockquote>
<p>just set <code>md := semireducible</code> like all the newer tactics</p>
</blockquote>
<p>Looking at the implementation, it seems like <code>assumption</code> is already calling <code>unify</code> with the (implicit) argument <code>md := semireducible</code>.</p>

#### [ Floris van Doorn (Nov 01 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20of%20%60assumption%60/near/136923989):
<p>I think a whole lot more should be irreducible, like <code>add</code>, <code>neg</code>, <code>mul</code> and <code>inv</code> for <code>cau_seq.completion</code>.</p>


{% endraw %}
