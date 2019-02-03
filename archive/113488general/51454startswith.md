---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51454startswith.html
---

## Stream: [general](index.html)
### Topic: [startswith](51454startswith.html)

---


{% raw %}
#### [ Patrick Massot (Jan 04 2019 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412396):
<p>Do we have something like <code>string.startswith : string -&gt; string -&gt; bool</code> somewhere?</p>

#### [ Mario Carneiro (Jan 04 2019 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412486):
<p>There are <code>&lt;:+</code> and <code>&lt;+:</code> for comparing lists, you could use that</p>

#### [ Gabriel Ebner (Jan 04 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412836):
<p>Omg. Did you get these hieroglyphs from Haskell or from Scala?</p>

#### [ Patrick Massot (Jan 04 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412845):
<p>I currently use</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">string</span><span class="bp">.</span><span class="n">startswith</span> <span class="o">(</span><span class="n">s</span> <span class="n">s&#39;</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="o">(</span><span class="n">s&#39;</span><span class="bp">.</span><span class="n">to_list</span><span class="o">)</span><span class="bp">.</span><span class="n">is_prefix_of</span> <span class="n">s</span><span class="bp">.</span><span class="n">to_list</span>

<span class="kn">instance</span> <span class="o">(</span><span class="n">s</span> <span class="n">s&#39;</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">string</span><span class="bp">.</span><span class="n">startswith</span> <span class="n">s</span> <span class="n">s&#39;</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">string</span><span class="bp">.</span><span class="n">startswith</span> <span class="bp">;</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Patrick Massot (Jan 04 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412905):
<p>I guess one of your hieroglyphs stands for <code>list.is_prefix_of</code></p>

#### [ Patrick Massot (Jan 04 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412913):
<p>But my hope was really that all this should be there already</p>

#### [ Mario Carneiro (Jan 04 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412954):
<p>the hieroglyphs were a terrible idea that I now regret</p>

#### [ Mario Carneiro (Jan 04 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413617):
<p>I agree that we should have this function already defined. In particular, you can make a more efficient implementation by working with string iterators instead of lists</p>

#### [ Mario Carneiro (Jan 04 2019 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413665):
<p>I should load up the docs for strings in haskell or java and copy everything I see</p>

#### [ Patrick Massot (Jan 04 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413755):
<p>I vote for doing that as soon as all topology and commutative algebra PR will be merged!</p>

#### [ Mario Carneiro (Jan 04 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413832):
<p>I'm working on <a href="https://github.com/leanprover/mathlib/issues/464" target="_blank" title="https://github.com/leanprover/mathlib/issues/464">#464</a>, making good progress</p>

#### [ Mario Carneiro (Jan 04 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413893):
<p>what commutative algebra PRs?</p>

#### [ Patrick Massot (Jan 04 2019 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413934):
<p>I'm joking, keep going on analysis. You'll have many nights in Amsterdam for algebra</p>

#### [ Sebastien Gouezel (Jan 04 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154431401):
<blockquote>
<p>I'm working on <a href="https://github.com/leanprover/mathlib/issues/464" target="_blank" title="https://github.com/leanprover/mathlib/issues/464">#464</a>, making good progress</p>
</blockquote>
<p>Btw, I updated the PR two days ago, but if you started working on the previous version you can of course disregard the modifications I made.</p>

#### [ Mario Carneiro (Jan 04 2019 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154431693):
<p>yeah, I noticed and have already incorporated your changes</p>


{% endraw %}
