---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60330localrecursivefunction.html
---

## Stream: [general](index.html)
### Topic: [local recursive function](60330localrecursivefunction.html)

---


{% raw %}
#### [ Reid Barton (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133958735):
<p>Can you define a recursive function with a <code>let</code> inside a <code>do</code> block (in a <code>meta</code> definition)?</p>

#### [ Sebastian Ullrich (Sep 14 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133962580):
<p>No</p>

#### [ Sebastian Ullrich (Sep 14 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133962812):
<p>Well, you could write a meta <code>fix</code>, but that's still not very ergonomical</p>

#### [ Chris Hughes (Sep 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964819):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">do</span> <span class="k">let</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">n</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="mi">1</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exact</span> <span class="bp">_</span><span class="n">match</span> <span class="n">n</span> <span class="bp">+</span> <span class="bp">_</span><span class="n">match</span> <span class="n">n</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="n">return</span> <span class="n">m</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">foo</span> <span class="mi">4</span> <span class="c1">-- some 16</span>
</pre></div>

#### [ Chris Hughes (Sep 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964837):
<p>I had to do <code>by exact</code> for some reason</p>

#### [ Sebastian Ullrich (Sep 14 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964901):
<p>Now that's just terrible :P</p>


{% endraw %}
