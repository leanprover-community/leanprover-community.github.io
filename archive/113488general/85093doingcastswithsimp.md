---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85093doingcastswithsimp.html
---

## Stream: [general](index.html)
### Topic: [doing casts with `simp`](85093doingcastswithsimp.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631368):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="n">m</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works fine</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="n">m</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">]</span> <span class="c1">-- fails</span>
</pre></div>


<p>Is there a way of getting the second example to work which doesn't involve (a) reverting H or (b) looking up the name of the lemma which <code>simp</code> is using to do the cast [i guess it's going to be <code>cardinal.nat_cast_inj</code>, maybe I'm supposed to know that]. Neither (a) nor (b) look "idiomatic" to me (is that the right word?)</p>

#### [ Rob Lewis (Aug 23 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631720):
<p><code>simpa using H</code>?</p>

#### [ Kenny Lau (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631805):
<p>why are you doing cardinals? <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631817):
<p>Richard Thomas asked a question about the number 3</p>

#### [ Kevin Buzzard (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631823):
<p>but then complained when I assumed it was finite</p>


{% endraw %}
