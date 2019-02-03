---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63555simptheoremifftrue.html
---

## Stream: [general](index.html)
### Topic: [simp theorem iff true](63555simptheoremifftrue.html)

---


{% raw %}
#### [ Sean Leather (May 18 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744334):
<p>What's the difference in <code>simp</code> behavior (if any) between these two theorems for <code>p : Prop</code>? Is one or the other preferable?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">t₁</span> <span class="o">(</span><span class="bp">...</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">t₂</span> <span class="o">(</span><span class="bp">...</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Gabriel Ebner (May 18 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744745):
<p>There is a difference if <code>p</code> is an equation or another simp relation.</p>

#### [ Sean Leather (May 18 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744833):
<p>Can you expand on that? I'm not sure what “another simp relation” is. Is there an example?</p>

#### [ Gabriel Ebner (May 18 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745082):
<p>Good question! If you have a relation <code>R</code> that is reflexive and transitive (as tagged with <code>@[refl]</code> and <code>@[trans]</code>), then you can use the simplifier to get proofs of <code>R x ?m_1</code> where <code>?m_1</code> is the simplified version of <code>x</code>.  For example think of equivalence relations such as equality modulo k in the integers.</p>

#### [ Gabriel Ebner (May 18 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745137):
<p>In mathlib it is used for the equivalence relation on types, where types are equivalent if they are equinumerous (have a bijection between them).  Then you can simplify <code>a ⨉ unit</code> to <code>a</code> for example.</p>

#### [ Sean Leather (May 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745205):
<p>Okay. Suppose I have these:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">t₁</span> <span class="o">(</span><span class="bp">...</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">t₂</span> <span class="o">(</span><span class="bp">...</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>I would intuitively write <code>t₂</code> and not <code>t₁</code> because I know <code>=</code> is a <code>simp</code> relation, right? What happens if you have <code>t₁</code> instead of <code>t₂</code>?</p>

#### [ Gabriel Ebner (May 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745206):
<p><a href="https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/data/equiv.lean#L166-L177" target="_blank" title="https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/data/equiv.lean#L166-L177">https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/data/equiv.lean#L166-L177</a></p>

#### [ Gabriel Ebner (May 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745209):
<blockquote>
<p>What happens if you have t₁ instead of t₂?</p>
</blockquote>
<p>Then simp won't be able to solve <code>b = a</code>, for instance.  It will only rewrite <code>a = b</code> to true.</p>

#### [ Sean Leather (May 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745224):
<p>Right, makes sense.</p>

#### [ Sean Leather (May 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745275):
<p>And if <code>p</code> is not a <code>simp</code> relation, is there any difference between the two?</p>

#### [ Gabriel Ebner (May 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745277):
<p>I don't think so.</p>

#### [ Sean Leather (May 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745343):
<p>In mathlib, I see these:</p>
<div class="codehilite"><pre><span></span><span class="err">$</span> <span class="n">git</span> <span class="n">grep</span> <span class="s2">&quot;↔ true&quot;</span>
<span class="n">data</span><span class="bp">/</span><span class="n">finset</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">theorem</span> <span class="n">forall_mem_empty_iff</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">data</span><span class="bp">/</span><span class="n">set</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span>  <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">imp_self</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">→</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span> <span class="n">iff_true_intro</span> <span class="n">id</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">imp_true_iff</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">forall_true_iff</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">theorem</span> <span class="n">forall_true_iff&#39;</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">↔</span> <span class="n">true</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">forall_2_true_iff</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">β</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span>  <span class="o">(</span><span class="bp">∀</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="n">a</span><span class="o">),</span> <span class="n">γ</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">forall_prop_of_false</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">logic</span><span class="bp">/</span><span class="n">basic</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="kn">theorem</span> <span class="n">ball_true_iff</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">true</span> <span class="o">:=</span>
</pre></div>

#### [ Sean Leather (May 18 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745409):
<p>I suppose the <code>→</code>/<code>Π</code> is special, thus <code>theorem forall_true_iff : (α → true) ↔ true</code>.</p>

#### [ Gabriel Ebner (May 18 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745419):
<p>Yes, without the iff true, those would be conditional simp lemmas.</p>

#### [ Sean Leather (May 18 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745473):
<p>Right. So, with these few exceptions, we should write <code>@[simp] theorem t₂ (...) : p := ...</code>.</p>

#### [ Sean Leather (May 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745495):
<p>(where <code>t₂</code> may or may not be conditional)</p>


{% endraw %}
