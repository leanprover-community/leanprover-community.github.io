---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27899creatinglambdawithouttactic.html
---

## Stream: [general](index.html)
### Topic: [creating lambda without tactic](27899creatinglambdawithouttactic.html)

---


{% raw %}
#### [ Zesen Qian (Jul 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130588564):
<p>meta programming problem: So I have a function body represented as <code>expr -&gt; expr</code>, which receives a reference to the argument, and return the body. Is it possible to abstract the argument away(that is, wrap it with a lambda) and get the anonymous function back as <code>expr</code>?</p>

#### [ Zesen Qian (Jul 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130588588):
<p>I might have been blur about <code>expr</code> and <code>pexpr</code>, but I hope that won't cause too much confusion.</p>

#### [ Jeremy Avigad (Jul 30 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130599168):
<p>Look in <code>init/meta/expr.lean</code>. The trick is to create an <code>expr</code> with a local constant, use <code>abstract_local</code> to replace it by an index, and then bind it.</p>
<p>My experiments follow. In the first example, I used a local variable in the context. For some reason, <code>bind_lambda</code> didn't work in that case (the abstracted variable did not get the right type), so I did it by hand. In the second example, I made a fresh local variable.</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span>
<span class="n">f&#39;</span> <span class="err">←</span> <span class="n">get_local</span> <span class="bp">`</span><span class="n">f</span><span class="o">,</span>
<span class="n">x&#39;</span> <span class="err">←</span> <span class="n">get_local</span> <span class="bp">`</span><span class="n">x</span><span class="o">,</span>
<span class="k">let</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">f&#39;</span> <span class="n">x&#39;</span><span class="o">,</span>
<span class="n">trace</span> <span class="n">e</span><span class="o">,</span>  <span class="c1">-- e is the expression f x</span>
<span class="c1">-- let e&#39; := expr.bind_lambda e x&#39;, -- this didn&#39;t work</span>
<span class="n">nt</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="n">nat</span><span class="o">),</span>
<span class="k">let</span> <span class="n">e&#39;</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="bp">`</span><span class="n">x</span> <span class="n">binder_info</span><span class="bp">.</span><span class="n">default</span> <span class="n">nt</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">abstract_local</span> <span class="n">x&#39;</span><span class="bp">.</span><span class="n">local_uniq_name</span><span class="o">),</span>
<span class="n">trace</span> <span class="n">e&#39;</span><span class="o">,</span>  <span class="c1">-- e&#39; is the expression λ (x : ℕ), f x</span>
<span class="n">exact</span> <span class="n">e&#39;</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span>
<span class="n">f&#39;</span> <span class="err">←</span> <span class="n">get_local</span> <span class="bp">`</span><span class="n">f</span><span class="o">,</span>
<span class="n">nt</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="n">nat</span><span class="o">),</span>
<span class="n">x&#39;</span> <span class="err">←</span> <span class="n">mk_local&#39;</span> <span class="bp">`</span><span class="n">x</span> <span class="n">binder_info</span><span class="bp">.</span><span class="n">default</span> <span class="n">nt</span><span class="o">,</span>
<span class="n">e</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="err">%%</span><span class="n">f&#39;</span> <span class="err">%%</span><span class="n">x&#39;</span><span class="o">),</span>
<span class="n">trace</span> <span class="n">e</span><span class="o">,</span>  <span class="c1">-- e is the expression f x</span>
<span class="k">let</span> <span class="n">e&#39;</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">bind_lambda</span> <span class="n">e</span> <span class="n">x&#39;</span><span class="o">,</span>
<span class="n">trace</span> <span class="n">e&#39;</span><span class="o">,</span>  <span class="c1">-- e&#39; is the expression λ (x : ℕ), f x</span>
<span class="n">exact</span> <span class="n">e&#39;</span>
</pre></div>

#### [ Zesen Qian (Jul 30 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130599995):
<p>Thank you jeremy. But it seems <code>tactic</code> is still used in both cases? Specifically, you used <code>mk_local</code>. It seems quite hard to do this without tactic monad?</p>

#### [ Zesen Qian (Jul 30 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600130):
<p>yeah I think I shouldn't be bother by using <code>tactic</code>.</p>

#### [ Zesen Qian (Jul 30 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600142):
<p>I looked in the definition of <code>mk_local</code> and really, <code>mk_fresh_name</code> is all I need from the <code>tactic</code>.</p>

#### [ Simon Hudon (Jul 30 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600826):
<p>Why is it important to not have the tactic monad?</p>

#### [ Zesen Qian (Jul 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600984):
<p>because this is a proof that in principle can be exclusively derived from a data structure, without looking at the environment.</p>

#### [ Zesen Qian (Jul 30 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130601087):
<p>but anyway, the current solution is good enough, I only need a fresh name from the <code>tactic</code>monad, so that's minimal side effect.</p>

#### [ Jeremy Avigad (Jul 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130608722):
<p>If you are building expressions entirely from scratch, you can make up your own unique name if you want. But <code>expr</code> is <code>meta</code>, so if you want to stay entirely within the logic, you have to define your own type of expressions.</p>

#### [ Zesen Qian (Jul 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130608796):
<p>I'm actually thinking about using <code>pexpr.var : nat -&gt; pexpr</code> which is de-bruijn index. So I don't have to worry about all the details of <code>local_const</code>.  I plan to construct the <code>pexpr</code> as a pure function of the LSEC proof, and elaborate the huge proof altogether.</p>

#### [ Zesen Qian (Jul 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130609160):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> yeah but if I do that we still need a conversion from my custom expr to the lean <code>expr</code>.</p>

#### [ Jeremy Avigad (Jul 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130609351):
<p>If you are building Lean expressions, don't hesitate to use the tactic framework. You will probably need constants from the environment anyway, and your code will be easier to debug if you elaborate expressions piece by piece.</p>


{% endraw %}
