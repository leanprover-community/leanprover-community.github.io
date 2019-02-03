---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98059constructingexprlam.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [constructing expr.lam](https://leanprover-community.github.io/archive/113488general/98059constructingexprlam.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 09 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600290):
<p>How do I construct <code>expr.lam</code> terms? In particular, I have  an expression <code>e_1</code> that already has a <code>var n</code> inside it, and another <code>e_2</code>, and I want to construct the <code>expr</code> representing <code>lam x, e_1 = e_2</code>.</p>

#### [ Scott Morrison (Sep 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600338):
<p>I tried to use <code>to_expr ``(%%e_1 = %%e_2)</code>, but that chokes because <code>e_1</code> has a <code>var</code> inside it.</p>

#### [ Simon Hudon (Sep 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600394):
<p>It's kind of ugly but I recommend </p>
<div class="codehilite"><pre><span></span><span class="n">feq</span> <span class="bp">&lt;-</span> <span class="n">mk_const</span> <span class="bp">`</span><span class="n">eq</span><span class="o">,</span>
<span class="n">v</span> <span class="bp">&lt;-</span> <span class="n">mk_mvar</span><span class="o">,</span>
<span class="k">let</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">lam</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">t</span> <span class="o">(</span><span class="n">feq</span> <span class="n">v</span> <span class="n">e_1</span> <span class="n">e_2</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Sep 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600442):
<p>the downside is that you're postponing type checking. If you don't want to postpone type checking, you have to take the long way around, instantiate your <code>var</code> with <code>local_const</code>, type check, then use <code>lambdas</code></p>

#### [ Scott Morrison (Sep 09 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600976):
<p>Ah, I see. Turning my <code>var</code> into a <code>local_const</code> is maybe not so bad, in any case. How does one construct the <code>expr.lam</code> then?</p>

#### [ Simon Hudon (Sep 09 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601026):
<div class="codehilite"><pre><span></span><span class="n">v</span> <span class="bp">&lt;-</span> <span class="n">mk_local_def</span> <span class="n">n</span> <span class="n">t</span><span class="o">,</span>
<span class="n">e</span> <span class="bp">&lt;-</span> <span class="n">mk_app</span> <span class="bp">`</span><span class="n">eq</span> <span class="o">[</span><span class="n">e_1</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">v</span><span class="o">,</span> <span class="n">e_2</span><span class="o">],</span>
<span class="n">lambdas</span> <span class="o">[</span><span class="n">v</span><span class="o">]</span> <span class="n">e</span><span class="o">,</span>
</pre></div>

#### [ Scott Morrison (Sep 09 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601300):
<p>Thanks!</p>

#### [ Simon Hudon (Sep 09 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601301):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>


{% endraw %}
