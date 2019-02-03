---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99190isthistruewithoutdecidable.html
---

## Stream: [general](index.html)
### Topic: [is this true without decidable](99190isthistruewithoutdecidable.html)

---


{% raw %}
#### [ Johan Commelin (Sep 07 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509753):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hnat</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≠</span> <span class="n">j</span><span class="o">)</span>
<span class="o">(</span><span class="n">hR</span> <span class="o">:</span> <span class="o">((</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="n">j</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">:</span>
<span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">R</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Sep 07 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509865):
<p>If it is true, what is the one-line proof?<br>
If it is not true, what is the one-line proof assuming <code>[decidable_eq R]</code>?</p>

#### [ Johan Commelin (Sep 07 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133509993):
<p>Never mind. This is completely false.</p>

#### [ Johan Commelin (Sep 07 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510050):
<p>/me needs to relearn modular arithmetic</p>

#### [ Johan Commelin (Sep 07 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510142):
<p>I thought this was my goal state. But it's not. <code>i</code> and <code>j</code> are coerced somewhere else. But I don't know where.</p>

#### [ Johan Commelin (Sep 07 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20true%20without%20decidable/near/133510154):
<p>/me needs to look at the <code>pp.all true</code> variant of the goal state.</p>


{% endraw %}
