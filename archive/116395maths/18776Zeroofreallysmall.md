---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18776Zeroofreallysmall.html
---

## Stream: [maths](index.html)
### Topic: [Zero of really small](18776Zeroofreallysmall.html)

---


{% raw %}
#### [ Patrick Massot (Jan 19 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453113):
<p>Where do we find <code>lemma zero_of_abs_lt_all (x : ℝ) (h : ∀ ε, ε &gt; 0 → |x| &lt; ε) : x = 0</code>?</p>

#### [ Chris Hughes (Jan 19 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453250):
<p>I think something like <code>eq_of_forall_abs_sub_lt</code> is in there.</p>

#### [ Patrick Massot (Jan 19 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453442):
<p><a href="https://github.com/leanprover/mathlib/search?q=eq_of_forall_abs_sub_lt&amp;unscoped_q=eq_of_forall_abs_sub_lt" target="_blank" title="https://github.com/leanprover/mathlib/search?q=eq_of_forall_abs_sub_lt&amp;unscoped_q=eq_of_forall_abs_sub_lt">https://github.com/leanprover/mathlib/search?q=eq_of_forall_abs_sub_lt&amp;unscoped_q=eq_of_forall_abs_sub_lt</a> <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Patrick Massot (Jan 19 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453462):
<p>Do you have any idea where something like this could be?</p>

#### [ Patrick Massot (Jan 19 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454123):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">zero_of_abs_lt_all</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">eq_zero_of_abs_eq_zero</span> <span class="err">$</span> <span class="n">eq_of_le_of_forall_le_of_dense</span> <span class="o">(</span><span class="n">abs_nonneg</span> <span class="n">x</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span> <span class="n">le_of_lt</span> <span class="o">(</span><span class="n">h</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Jan 19 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454138):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Should I PR that, or is it already in?</p>

#### [ Patrick Massot (Jan 19 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454184):
<p>with weaker assumptions of course</p>

#### [ Patrick Massot (Jan 19 2019 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454188):
<p>(I mean replacing real numbers with something more general)</p>

#### [ Mario Carneiro (Jan 19 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454377):
<p>is this a theorem of normed groups or do you want a different abstraction</p>

#### [ Patrick Massot (Jan 19 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454434):
<p>I think normed groups is enough for me, but <code>eq_of_le_of_forall_le_of_dense</code> has more exotic type classes</p>

#### [ Patrick Massot (Jan 19 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454452):
<p>But I don't want you to think too hard about this when you could be hitting that merge button on <a href="https://github.com/leanprover/mathlib/pull/610" target="_blank" title="https://github.com/leanprover/mathlib/pull/610">https://github.com/leanprover/mathlib/pull/610</a></p>

#### [ Patrick Massot (Jan 19 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454640):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">zero_of_norm_lt_all</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">normed_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="err">∥</span><span class="n">x</span><span class="err">∥</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">norm_eq_zero</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">eq_of_le_of_forall_le_of_dense</span> <span class="o">(</span><span class="n">norm_nonneg</span> <span class="n">x</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span> <span class="n">le_of_lt</span> <span class="o">(</span><span class="n">h</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">zero_of_abs_lt_all</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">zero_of_norm_lt_all</span> <span class="n">x</span> <span class="n">h</span>
</pre></div>


<p>does work</p>

#### [ Patrick Massot (Jan 19 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454642):
<p>of course we could also prove them the other way around</p>


{% endraw %}
