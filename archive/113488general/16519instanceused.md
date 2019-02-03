---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16519instanceused.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [instance used](https://leanprover-community.github.io/archive/113488general/16519instanceused.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Nov 18 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922878):
<p>is there some way to show which instance (of a class) is actually used in a definition? If I use <code>set_option trace.class_instances true</code>, it lists lots of possible instances, but I only want the actual instance used</p>

#### [ Mario Carneiro (Nov 18 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922929):
<p>I sometimes grep the output to remove lines immediately followed with <code>failed defeq</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922937):
<p>but of course you can always just look at the term</p>

#### [ petercommand (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922940):
<p>just look at the term?</p>

#### [ petercommand (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922941):
<p>yeah, I can grep the output</p>

#### [ Mario Carneiro (Nov 18 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922984):
<p>Just trigger the instance search manually. For example:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">implicit</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">int</span><span class="o">)</span>
<span class="c1">-- @partial_order.to_preorder ℤ</span>
<span class="c1">--   (@ordered_comm_group.to_partial_order ℤ</span>
<span class="c1">--      (@ordered_ring.to_ordered_comm_group ℤ</span>
<span class="c1">--         (@linear_ordered_ring.to_ordered_ring ℤ</span>
<span class="c1">--            (@linear_ordered_comm_ring.to_linear_ordered_ring ℤ</span>
<span class="c1">--               (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring ℤ</span>
<span class="c1">--                  int.decidable_linear_ordered_comm_ring))))) :</span>
<span class="c1">--   preorder ℤ</span>
</pre></div>

#### [ petercommand (Nov 18 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922996):
<p>Ah..that works great! Thanks!</p>

#### [ Kenny Lau (Nov 18 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147923628):
<p>alternatively:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">implicit</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">infer_instance</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">int</span><span class="o">)</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">@infer_instance (preorder ℤ)</span>
<span class="cm">  (@partial_order.to_preorder ℤ</span>
<span class="cm">     (@ordered_comm_group.to_partial_order ℤ</span>
<span class="cm">        (@ordered_ring.to_ordered_comm_group ℤ</span>
<span class="cm">           (@linear_ordered_ring.to_ordered_ring ℤ</span>
<span class="cm">              (@linear_ordered_comm_ring.to_linear_ordered_ring ℤ</span>
<span class="cm">                 (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring ℤ</span>
<span class="cm">                    int.decidable_linear_ordered_comm_ring)))))) :</span>
<span class="cm">  preorder ℤ</span>
<span class="cm">-/</span>
</pre></div>


{% endraw %}
