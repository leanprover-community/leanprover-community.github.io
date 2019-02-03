---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72607Useifconditionwithinthenoutput.html
---

## Stream: [new members](index.html)
### Topic: [Use "if" condition within "then" output](72607Useifconditionwithinthenoutput.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 28 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749574):
<p>I'm trying to write something like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">bob</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">rad</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>
<span class="o">(</span>
  <span class="n">hc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="bp">-</span><span class="n">rad</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">rad</span> <span class="bp">→</span> <span class="n">is_cau_seq</span> <span class="n">abs</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">a</span> <span class="n">k</span> <span class="bp">*</span> <span class="n">x</span> <span class="err">^</span> <span class="n">k</span><span class="o">))</span>
<span class="o">)</span>
<span class="o">(</span>
  <span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
  <span class="k">if</span> <span class="o">(</span><span class="n">hr</span> <span class="o">:</span> <span class="bp">-</span> <span class="n">rad</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">rad</span><span class="o">)</span> <span class="k">then</span>
    <span class="n">cau_seq</span><span class="bp">.</span><span class="n">lim</span> <span class="o">((</span><span class="bp">⟨λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">k</span><span class="o">,</span> <span class="n">a</span> <span class="n">k</span> <span class="bp">*</span> <span class="n">x</span> <span class="err">^</span> <span class="n">k</span><span class="o">)</span> <span class="o">,</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">hc</span> <span class="n">x</span> <span class="n">hr</span><span class="o">)</span>   <span class="bp">⟩</span><span class="o">)</span> <span class="o">:</span> <span class="n">cau_seq</span> <span class="n">ℝ</span> <span class="n">abs</span><span class="o">)</span>
  <span class="k">else</span> <span class="mi">0</span>
<span class="o">)</span>
<span class="o">:</span> <span class="n">sorry</span>
</pre></div>


<p>Of course, this doesn't work because I can only put a proposition in the if condition, not a proof -- but shouldn't there be some way of achieving this -- of referring to the condition for the <code>if</code> in the output for <code>then</code>?</p>
<p>French brackets don't work either because the condition isn't recorded as an assumption at all.</p>
<p>Is this where <code>dite</code> comes in?</p>

#### [ Reid Barton (Nov 28 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749758):
<p>try deleting those parentheses?</p>

#### [ Reid Barton (Nov 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749765):
<p>around <code>hr : - rad &lt; x ∧ x &lt; rad</code></p>


{% endraw %}
