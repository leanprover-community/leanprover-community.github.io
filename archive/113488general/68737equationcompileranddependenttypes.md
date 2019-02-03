---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68737equationcompileranddependenttypes.html
---

## Stream: [general](index.html)
### Topic: [equation compiler and dependent types](68737equationcompileranddependenttypes.html)

---


{% raw %}
#### [ Patrick Massot (Dec 23 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434275):
<p>Is there any way to use the equation compiler with a dependent output? The following works (although I wish the proof part could be <code>by linarith</code>):</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">euclid</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="o">{</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="o">}</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="k">then</span>
           <span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">m</span><span class="o">)</span>
         <span class="k">else</span>
           <span class="k">have</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">n</span><span class="bp">.</span><span class="n">property</span><span class="o">,</span>
           <span class="k">have</span> <span class="n">m</span> <span class="bp">-</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt</span> <span class="bp">;</span> <span class="n">linarith</span><span class="o">,</span>
           <span class="k">let</span> <span class="bp">⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">euclid</span> <span class="o">(</span><span class="n">m</span><span class="bp">-</span><span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="k">in</span> <span class="bp">⟨</span><span class="n">q</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span>
</pre></div>


<p>But now suppose I want the output type to be <code>{ p : ℕ × ℕ | m = n*p.1 + p.2 ∧ p.2 &lt; n}</code>. Is something like this possible? Of course here Lean complains it doesn't know who are <code>m</code> and <code>n</code>, which will appear only after matching. Of course I also wish I could write <code>{ (q, r) : ℕ × ℕ | m = n*q + r ∧ r &lt; n}</code> (or with angle brackets)instead of those ugly <code>p.1</code> and <code>p.2</code>, but at least this is not blocking.</p>

#### [ Patrick Massot (Dec 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434681):
<p>Sorry about this stupid question</p>

#### [ Patrick Massot (Dec 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434684):
<p>I can use a Pi type instead</p>

#### [ Patrick Massot (Dec 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434942):
<p>Note for next time I ask: one possible answer is</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">euclid</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="o">{</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="o">}),</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">*</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">∧</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="k">then</span>
           <span class="bp">⟨</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">m</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">*⟩</span>
         <span class="k">else</span>
           <span class="k">have</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">n</span><span class="bp">.</span><span class="n">property</span><span class="o">,</span>
           <span class="k">have</span> <span class="n">m</span> <span class="bp">-</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt</span> <span class="bp">;</span> <span class="n">linarith</span><span class="o">,</span>
           <span class="k">let</span> <span class="bp">⟨⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩⟩</span> <span class="o">:=</span> <span class="n">euclid</span> <span class="o">(</span><span class="n">m</span><span class="bp">-</span><span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="k">in</span>
             <span class="bp">⟨</span><span class="o">(</span><span class="n">q</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">r</span><span class="o">),</span>
              <span class="bp">⟨</span><span class="k">begin</span>
                <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_eq_iff_eq_add</span> <span class="o">(</span><span class="n">le_of_not_lt</span> <span class="n">h</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
                <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">],</span> <span class="n">ring</span><span class="o">,</span>
               <span class="kn">end</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩⟩</span>
</pre></div>


{% endraw %}
