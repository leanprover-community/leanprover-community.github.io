---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16734typeclasstracedump.html
---

## Stream: [general](index.html)
### Topic: [type class trace dump](16734typeclasstracedump.html)

---


{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20trace%20dump/near/131025671):
<p>Is this expected behaviour?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>

<span class="kn">instance</span> <span class="n">foobar</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>I won't copy-paste the trace here, it is pretty long.</p>


{% endraw %}
