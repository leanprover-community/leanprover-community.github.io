---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78605arrayinduction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [array induction](https://leanprover-community.github.io/archive/113488general/78605arrayinduction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Aug 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096387):
<p>Given a theorem statement involving an <code>array</code>, what might I use in the proof where I would normally use induction if the <code>array</code> were instead a <code>list</code>?</p>

#### [ Sean Leather (Aug 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096647):
<p>In particular, I have <code>array.to_list</code> in the statement. It seems like I might use induction on the <code>nat</code> size of the array, since the core of <code>array.to_list</code> is <code>d_array.rev_iterate_aux</code>.</p>

#### [ Sean Leather (Aug 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096728):
<p>Or: not the size but the index into the <code>d_array</code>.</p>

#### [ Mario Carneiro (Aug 14 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099746):
<p>It depends on the statement</p>

#### [ Mario Carneiro (Aug 14 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099801):
<p>If you can have the array length vary, it might be easier to prove by induction over all vectors of any length</p>

#### [ Mario Carneiro (Aug 14 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099817):
<p>If the array is fixed, then you may need to do induction on the index, which is messier</p>

#### [ Sean Leather (Aug 14 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099938):
<p>So, I've got this:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">to_list_zero</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">array</span> <span class="mi">0</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">to_list</span> <span class="bp">=</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>And I'm looking at this:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">to_list_succ</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">array</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span><span class="bp">.</span><span class="n">to_list</span> <span class="bp">=</span> <span class="n">a</span><span class="bp">.</span><span class="n">read</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="n">n</span><span class="bp">⟩</span> <span class="bp">::</span> <span class="n">a</span><span class="bp">.</span><span class="n">pop_back</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">:=</span> <span class="bp">_</span>
</pre></div>


<p>But I think <code>to_list</code> does a reverse fold, which means the above is not true.</p>

#### [ Mario Carneiro (Aug 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101671):
<p><code>to_list</code> produces a list in the same order as the index</p>

#### [ Mario Carneiro (Aug 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101681):
<p><code>rev_list</code> produces a list in reverse order (which turns out to be a bit easier to define)</p>

#### [ Mario Carneiro (Aug 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101744):
<p>so I think you want that statement to be on <code>rev_list</code></p>

#### [ Minchao Wu (Aug 14 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118289):
<p>This reminds me something: do we have an eliminator for <code>finset</code> that eliminates a <code>s : finset</code> to any <code>Sort</code>?</p>

#### [ Minchao Wu (Aug 14 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118300):
<p>Somewhere in mathlib?</p>

#### [ Mario Carneiro (Aug 14 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118802):
<p>If it is going all the way back to lists under permutation, it's easier to just do cases on the finset and the <code>quot.lift</code>, i.e. define it via multiset</p>

#### [ Mario Carneiro (Aug 14 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118810):
<p>what would the type of such an eliminator be?</p>

#### [ Mario Carneiro (Aug 14 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118881):
<p>Plus, if you are doing dependent elimination over a quotient the compatibility hypothesis is a mess to work with</p>

#### [ Minchao Wu (Aug 14 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132119121):
<p>Right, I just looked into the <code>multiset.lean</code> and saw your comments on the dependent recursor</p>


{% endraw %}
