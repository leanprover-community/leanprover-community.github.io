---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34718propertyappliestoallelementsoflist.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [property applies to all elements of list](https://leanprover-community.github.io/archive/116395maths/34718propertyappliestoallelementsoflist.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Apr 30 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884050):
<p>Is there another, convenient way one might specify this given what exists in mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">allp</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">allp</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">},</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">allp</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">allp</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span>
</pre></div>


<p>Or, alternatively:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">allp</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">h</span><span class="o">)</span> <span class="n">true</span>
</pre></div>

#### [ Mario Carneiro (Apr 30 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884097):
<p>The standard way to write <code>allp</code> is <code>\forall x \in l, p x</code></p>

#### [ Sean Leather (Apr 30 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884291):
<p>I see. That uses the recursive of <code>list.mem</code> to accomplish the recursion of <code>allp</code>.</p>
<p>Are there existing equivalent theorems to these?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">allp_singleton</span> <span class="o">(</span><span class="n">pa</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">allp</span> <span class="n">p</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">allp_append</span> <span class="o">:</span> <span class="n">allp</span> <span class="n">p</span> <span class="n">l₁</span> <span class="bp">→</span> <span class="n">allp</span> <span class="n">p</span> <span class="n">l₂</span> <span class="bp">→</span> <span class="n">allp</span> <span class="n">p</span> <span class="o">(</span><span class="n">l₁</span> <span class="bp">++</span> <span class="n">l₂</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">allp_nil</span> <span class="o">:</span> <span class="n">allp</span> <span class="n">p</span> <span class="o">[]</span> <span class="bp">↔</span> <span class="n">true</span>
<span class="kn">theorem</span> <span class="n">allp_cons</span> <span class="o">:</span> <span class="n">allp</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">allp</span> <span class="n">p</span> <span class="n">l</span>
</pre></div>

#### [ Sean Leather (Apr 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884299):
<p>In the core library?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">ball_nil</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">@</span><span class="n">nil</span> <span class="n">α</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span>
<span class="kn">lemma</span> <span class="n">ball_cons</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">),</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">p</span> <span class="n">a</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 30 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884401):
<p>There are <code>forall_mem_nil</code> and <code>forall_mem_cons</code>, but the append theorem is not there. You can probably get the singleton theorem by simp</p>


{% endraw %}
