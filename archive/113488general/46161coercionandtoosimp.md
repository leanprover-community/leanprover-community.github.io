---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46161coercionandtoosimp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [coercion and too simp](https://leanprover-community.github.io/archive/113488general/46161coercionandtoosimp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Jun 07 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703649):
<p>I keep running into the problem of <code>simp</code> reducing something to <code>p = ff</code> when I really want <code>¬↥p</code>. I then end up doing a <code>rw</code> explicitly, which is a pain. Is there any way to work around this issue with <code>simp</code>?</p>

#### [ Kevin Buzzard (Jun 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703860):
<p>You can often do <code>suffices : &lt;what you want&gt;, simpa using this</code> or <code>...simp [this]</code> or similar. You want something neater than this though?</p>

#### [ Sean Leather (Jun 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703975):
<p>I was hoping for something like <code>simp [-&lt;theorem&gt;]</code>, disabling a particular rewrite but still using only <code>simp</code>. I'm not sure those other options are any better than the <code>rw</code> that I do now.</p>

#### [ Sean Leather (Jun 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703996):
<p>Or, even better, remove the <code>simp</code> attribute locally for my whole file. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Sean Leather (Jun 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704359):
<p>Ah, found it: <code>simp [-eq_ff_eq_not_eq_tt]</code>. I just had to look at the <code>simp</code> rules with <code>set_option trace.simplify.rewrite true</code>.</p>

#### [ Sean Leather (Jun 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704372):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">eq_ff_eq_not_eq_tt</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">b</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="n">b</span> <span class="bp">=</span> <span class="n">ff</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Jun 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704392):
<p>Not the rule I expected.</p>

#### [ Sean Leather (Jun 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704475):
<p>But I guess it makes sense due to this instance and defeq:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="kn">instance</span> <span class="n">coe_sort_bool</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="n">bool</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="kt">Prop</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">tt</span><span class="bp">⟩</span>
</pre></div>


{% endraw %}
