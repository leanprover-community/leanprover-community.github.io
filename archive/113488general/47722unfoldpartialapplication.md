---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47722unfoldpartialapplication.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unfold partial application](https://leanprover-community.github.io/archive/113488general/47722unfoldpartialapplication.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Pablo Le Hénaff (Jun 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766659):
<p>Hey.<br>
I'm trying to unfold my own definition which is only applied partially, e.g.<br>
in a goal</p>
<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">my_function</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">something_else</span>
</pre></div>


<p>where</p>
<div class="codehilite"><pre><span></span><span class="n">my_function</span> <span class="o">:</span> <span class="n">some_type</span> <span class="bp">-&gt;</span> <span class="n">α</span> <span class="bp">-&gt;</span> <span class="n">some_comm_monoid_type</span>
</pre></div>


<p>In that case, dunfold/unfold doesn't work and I need to specify</p>
<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="n">my_function</span> <span class="n">b</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">something_else</span>
</pre></div>


<p>for the tactic to work. Is there a workaround for this to be done automatically ? Thanks.</p>

#### [ Mario Carneiro (Jun 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766782):
<p>You can define <code>my_function</code> with the second argument right of the colon</p>

#### [ Mario Carneiro (Jun 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766787):
<p>i.e. write <code>my_function (s : some_type) : α -&gt; some_comm_monoid_type := λa, ...</code></p>

#### [ Mario Carneiro (Jun 08 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20partial%20application/near/127766794):
<p>assuming you always want to unfold this function in such a partially applied environment</p>


{% endraw %}
