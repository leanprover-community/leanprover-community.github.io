---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31254equationhasnotbeenusedinthecompilation.html
---

## Stream: [general](index.html)
### Topic: [equation has not been used in the compilation](31254equationhasnotbeenusedinthecompilation.html)

---


{% raw %}
#### [ Sean Leather (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002534):
<p>This is the first time I've seen the error below. What does it mean? What might be causing it?</p>
<div class="codehilite"><pre><span></span><span class="n">error</span><span class="o">:</span> <span class="n">equation</span> <span class="n">compiler</span> <span class="n">error</span><span class="o">,</span> <span class="n">equation</span> <span class="bp">#</span><span class="mi">2</span> <span class="n">has</span> <span class="n">not</span> <span class="n">been</span> <span class="n">used</span> <span class="k">in</span> <span class="n">the</span> <span class="n">compilation</span> <span class="o">(</span><span class="n">possible</span> <span class="n">solution</span><span class="o">:</span> <span class="n">delete</span> <span class="n">equation</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002547):
<p>you have a match branch that was not used</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002559):
<div class="codehilite"><pre><span></span>def f : ℕ → ℕ
| n := n + 1
| 0 := 0
</pre></div>

#### [ Mario Carneiro (Sep 15 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002576):
<p>It is often caused by a constant in your pattern actually being interpreted as a variable and thus being more generic than it is supposed to be</p>

#### [ Mario Carneiro (Sep 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002617):
<div class="codehilite"><pre><span></span>def f : ℕ → ℕ
| zero := 1 -- zero is a variable since it should be nat.zero
| (n+1) := n -- not used
</pre></div>


{% endraw %}
