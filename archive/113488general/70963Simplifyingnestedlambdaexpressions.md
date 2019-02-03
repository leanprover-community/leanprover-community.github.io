---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70963Simplifyingnestedlambdaexpressions.html
---

## Stream: [general](index.html)
### Topic: [Simplifying nested lambda expressions](70963Simplifyingnestedlambdaexpressions.html)

---


{% raw %}
#### [ Ken Roe (Jan 12 2019 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958159):
<p>It appears that "simp" is not completely robust.  How do I get the following simplification to work?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">beta_r</span> <span class="o">{</span><span class="n">y</span><span class="o">:</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">q</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Jan 12 2019 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958482):
<p>The simp seems to work for me. What version of lean are you using / what else do you have in the file?</p>

#### [ Bryan Gin-ge Chen (Jan 12 2019 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154958593):
<p>The <code>squeeze_simp</code> tactic in mathlib's <code>tactic.squeeze</code> tells me that <code>simp only [eq_self_iff_true]</code> ought to work too.</p>

#### [ Ken Roe (Jan 12 2019 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154959050):
<p>I'm using Lean 3.4.1.  Should I update?</p>

#### [ Ken Roe (Jan 12 2019 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifying%20nested%20lambda%20expressions/near/154959131):
<p>It does work--I realized I need to type a "," after the "simp" to see the reduction show up in the editor.</p>


{% endraw %}
