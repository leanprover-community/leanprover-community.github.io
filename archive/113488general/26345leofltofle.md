---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26345leofltofle.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [le_of_lt_of_le](https://leanprover-community.github.io/archive/113488general/26345leofltofle.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Apr 25 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693526):
<p>Should we prove <code>le_of_lt_of_le</code> so this stuff works?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h</span>
   <span class="bp">...</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₁</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">le_of_lt_of_le</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h</span>
   <span class="bp">...</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₁</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693595):
<p>I've run into that before</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693597):
<p>You have to remember to apply le_of_lt before starting the calc :-)</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693605):
<p>I like the idea.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693695):
<p>dammit I want the proof to be <code>le_of_lt $ lt_of_lt_of_le</code></p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693696):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693709):
<p><code>λ x y, le_of_lt $ lt_of_lt_of_le x y</code> looks like you're missing a trick</p>


{% endraw %}
