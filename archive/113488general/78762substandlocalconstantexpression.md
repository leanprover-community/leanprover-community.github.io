---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78762substandlocalconstantexpression.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subst and local constant expression](https://leanprover-community.github.io/archive/113488general/78762substandlocalconstantexpression.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Feb 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034490):
<p>Why does <code>subst</code> need its expression argument to be a local constant? I would like to be able to do something like <code>subst &lt;expr&gt;</code> with an arbitrary <code>&lt;expr&gt;</code>, but this results in:</p>
<div class="codehilite"><pre><span></span>error: subst tactic failed, given expression is not a local constant
</pre></div>


<p>Instead, I have to do:</p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">&lt;</span><span class="n">expr</span><span class="bp">&gt;</span><span class="o">,</span> <span class="n">subst</span> <span class="n">this</span>
</pre></div>


<p>Is it because <code>subst</code> always <code>clear</code>s the argument? Should there be a version of <code>subst</code> that doesn't <code>clear</code>?</p>

#### [ Mario Carneiro (Feb 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034493):
<p>yeah I petitioned for this but leo said no</p>

#### [ Mario Carneiro (Feb 27 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034533):
<p>it's an expr so you can use the french quotes to select a variable from the context by type</p>

#### [ Mario Carneiro (Feb 27 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034544):
<p>You can do mostly the same thing with <code>cases e</code> where <code>e : a = b</code></p>

#### [ Simon Hudon (Feb 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20and%20local%20constant%20expression/near/123034636):
<p>Otherwise, you may need to do <code>generalize</code> first and then <code>subst</code>.</p>


{% endraw %}
