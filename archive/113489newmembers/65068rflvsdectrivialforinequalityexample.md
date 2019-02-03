---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65068rflvsdectrivialforinequalityexample.html
---

## Stream: [new members](index.html)
### Topic: [rfl vs dec_trivial for inequality example](65068rflvsdectrivialforinequalityexample.html)

---


{% raw %}
#### [ Joseph Corneli (Jan 24 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rfl%20vs%20dec_trivial%20for%20inequality%20example/near/156766507):
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">one_plus_one_alt</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>


<p>This doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p><span aria-label="confused" class="emoji emoji-1f615" role="img" title="confused">:confused:</span></p>

#### [ Rob Lewis (Jan 24 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rfl%20vs%20dec_trivial%20for%20inequality%20example/near/156767066):
<p>Look at the type of <code>rfl</code>? It proves equality, not inequality.</p>

#### [ Rob Lewis (Jan 24 2019 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rfl%20vs%20dec_trivial%20for%20inequality%20example/near/156767129):
<p>You might be looking for <code>le_refl</code>.</p>


{% endraw %}
