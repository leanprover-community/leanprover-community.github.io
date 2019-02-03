---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07922reflectbool.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [reflect bool](https://leanprover-community.github.io/archive/113488general/07922reflectbool.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Aug 03 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130821232):
<p>I'm running the following code:</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">eval_expr</span> <span class="n">bool</span> <span class="o">(</span><span class="n">reflect</span> <span class="n">tt</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span>
</pre></div>


<p><code>bool</code> has an instance of <code>has_reflect</code> and the above is type correct but when I run it I get the following error:</p>
<div class="codehilite"><pre><span></span>VM does not have code for &#39;bool.tt&#39;
</pre></div>


<p>What can I do?</p>

#### [ Mario Carneiro (Aug 03 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830241):
<p>There is definitely a bug somewhere in the workings of <code>eval_expr</code></p>

#### [ Mario Carneiro (Aug 03 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830284):
<p>workaround:</p>
<div class="codehilite"><pre><span></span>run_cmd eval_expr bool (reflect (id tt)) &gt;&gt;= trace
</pre></div>

#### [ Minchao Wu (Aug 03 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830305):
<p>looks like magic</p>

#### [ Simon Hudon (Aug 03 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130839532):
<p>Thanks! I was able to use this trick with <code>user_attribute.get_param_untyped</code> to replace <code>user_attribute.get_param</code></p>

#### [ Simon Hudon (Aug 03 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130839561):
<p>(by wrapping the return with <code>id</code>: <code>to_expr ``(id %%r)</code>)</p>


{% endraw %}
