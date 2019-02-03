---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38425isleftidrwmystery.html
---

## Stream: [general](index.html)
### Topic: [is_left_id rw mystery](38425isleftidrwmystery.html)

---


{% raw %}
#### [ Patrick Massot (Apr 23 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570810):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">op</span> <span class="n">nil</span> <span class="n">a</span><span class="o">)</span> <span class="o">[</span><span class="n">is_left_id</span> <span class="n">R</span> <span class="n">op</span> <span class="n">nil</span><span class="o">]</span> <span class="o">:</span> <span class="n">op</span> <span class="n">nil</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">is_left_id</span><span class="bp">.</span><span class="n">left_id</span>
</pre></div>


<p>errors with:</p>
<div class="codehilite"><pre><span></span><span class="n">rewrite</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">did</span> <span class="n">not</span> <span class="n">find</span> <span class="kn">instance</span> <span class="n">of</span> <span class="n">the</span> <span class="n">pattern</span> <span class="k">in</span> <span class="n">the</span> <span class="n">target</span> <span class="n">expression</span>
  <span class="err">?</span><span class="n">m_1</span> <span class="err">?</span><span class="n">m_2</span> <span class="err">?</span><span class="n">m_3</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">op</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span><span class="o">,</span>
<span class="n">nil</span> <span class="o">:</span> <span class="n">out_param</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">is_left_id</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="n">op</span> <span class="n">nil</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="n">op</span> <span class="n">nil</span> <span class="n">a</span><span class="o">)</span> <span class="n">a</span>
</pre></div>

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570848):
<p>I know I could use <code>is_left_id.left_id _ _</code> in place of the rw</p>

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570853):
<p>But in my real use case I want to rewrite</p>

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570855):
<p>(or simp would be even better)</p>

#### [ Kenny Lau (Apr 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570941):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">op</span> <span class="n">nil</span> <span class="n">a</span><span class="o">)</span> <span class="o">[</span><span class="n">is_left_id</span> <span class="n">R</span> <span class="n">op</span> <span class="n">nil</span><span class="o">]</span> <span class="o">:</span> <span class="n">op</span> <span class="n">nil</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">is_left_id</span><span class="bp">.</span><span class="n">left_id</span> <span class="n">op</span> <span class="n">a</span>
</pre></div>

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571019):
<p>interesting</p>

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571036):
<p>doesn't explain why unification fails though</p>

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571042):
<p>probably because that is a higher-order unification</p>

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571047):
<p><a href="https://en.wikipedia.org/wiki/Unification_(computer_science)#Higher-order_unification" target="_blank" title="https://en.wikipedia.org/wiki/Unification_(computer_science)#Higher-order_unification">https://en.wikipedia.org/wiki/Unification_(computer_science)#Higher-order_unification</a></p>

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571048):
<p>it is undecidable</p>

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571051):
<p>Oh I think you're right</p>

#### [ Patrick Massot (Apr 23 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571140):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is this part of why you don't believe in the new algebraic hierarchy? Or is it possible to recover a working simp lemma here?</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125575939):
<p>Yes, this is the main problem with the new alg hierarchy. To be fair to Leo, he's been aware of this problem since the start, and the <code>algebra</code> attribute is part of a plan to fix it, but it requires more lean support than it currently gets. It should be a part of lean 4</p>

#### [ Patrick Massot (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125576476):
<p>Ok, it makes sense. Do you agree that the new hierarchy seems more suitable if we want a big_op library that is really operator centric as in mathcomp?</p>


{% endraw %}
