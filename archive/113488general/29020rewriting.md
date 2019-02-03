---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29020rewriting.html
---

## Stream: [general](index.html)
### Topic: [rewriting](29020rewriting.html)

---


{% raw %}
#### [ Pablo Le Hénaff (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773629):
<p>Hey again,<br>
I'm stuck with this rewriting issue, I don't understand why it won't match :'(</p>

#### [ Pablo Le Hénaff (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773672):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">V</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">finset</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">:</span> <span class="n">V</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">a</span> <span class="o">:</span> <span class="n">V</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">↔</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">this</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jun 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773904):
<p>use <code>simp</code> instead. <code>rw</code> does not rewrite bound variables. You need congruence lemmas for that and <code>simp</code> can access them.</p>

#### [ Chris Hughes (Jun 08 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792061):
<p>How come <code>simp</code> can handle rewriting the type of the <code>decidable_pred</code> instance?</p>

#### [ Simon Hudon (Jun 08 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792184):
<p>rewriting <code>decidable</code> is tricky because of how dependent those types are</p>

#### [ Simon Hudon (Jun 08 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792303):
<p>Sorry, I misread. You're asking why it can?</p>

#### [ Chris Hughes (Jun 08 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127793688):
<p>Yes. I always have this problem with fintype.</p>


{% endraw %}
