---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02074exprpis.html
---

## Stream: [general](index.html)
### Topic: [expr.pis](02074exprpis.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 14 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711391):
<p>Why doesn't <code>#reduce expr.pis [expr.local_const  ` A `A binder_info.default `(Sort 1)] `(Sort 1)</code>terminate?</p>

#### [ Kevin Buzzard (Mar 14 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711636):
<p>In an ideal world you would go to the set_option docs and look at the section "how do I track down an excessive memory consumption error?"</p>

#### [ Gabriel Ebner (Mar 14 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711953):
<p><span class="user-mention" data-user-id="110789">@Jakob von Raumer</span> You should use <code>#eval</code> since <code>expr.pis</code> is meta.</p>

#### [ Gabriel Ebner (Mar 14 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712203):
<p>And I think the following should explain why kernel reduction fails on this example:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">raw</span> <span class="bp">`</span><span class="n">A</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">name.mk_string</span>
<span class="cm">  (string.str string.empty</span>
<span class="cm">     (char.of_nat</span>
<span class="cm">        (@bit1.{0} nat nat.has_one nat.has_add</span>
<span class="cm">           (@bit0.{0} nat nat.has_add</span>
<span class="cm">              (@bit0.{0} nat nat.has_add</span>
<span class="cm">                 (@bit0.{0} nat nat.has_add</span>
<span class="cm">                    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))))))</span>
<span class="cm">  name.anonymous</span>
<span class="cm">-/</span>
</pre></div>

#### [ Gabriel Ebner (Mar 14 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712256):
<p>(I just tried all subterms of the example, and already <code>#reduce `A</code> fails.)</p>

#### [ Jakob von Raumer (Mar 14 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712261):
<p>Thanks :)</p>

#### [ Jakob von Raumer (Mar 14 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712357):
<p>But for <code>#eval</code> I'm getting a "result type does not have an instance of type class 'has_repr', dumping internal representation"?</p>

#### [ Gabriel Ebner (Mar 14 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712411):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">instance</span><span class="o">:</span> <span class="n">has_repr</span> <span class="n">expr</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">expr</span><span class="bp">.</span><span class="n">to_string</span><span class="bp">⟩</span>
</pre></div>


<p><span class="emoji emoji-1f604" title="smile">:smile:</span> I'm not sure if Leo would like a PR though...</p>


{% endraw %}
