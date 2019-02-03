---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/52070liftingofvariables.html
---

## Stream: [new members](index.html)
### Topic: [%% lifting of variables](52070liftingofvariables.html)

---


{% raw %}
#### [ Ken Roe (Jul 22 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%25%25%20lifting%20of%20variables/near/130095457):
<p>I've discovered that %% automatically lifts bound variables as shown in the following example:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">test_dummy</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">{</span>
     <span class="n">test</span> <span class="err">←</span> <span class="n">some</span> <span class="bp">``</span><span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span><span class="n">v</span><span class="bp">=</span><span class="err">%%</span><span class="o">(</span><span class="bp">@</span><span class="n">var</span> <span class="n">tt</span> <span class="mi">1</span><span class="o">))</span> <span class="mi">3</span><span class="o">),</span>
     <span class="n">trace</span> <span class="n">test</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
     <span class="n">admit</span>
   <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">dummy</span> <span class="o">:</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">test_dummy</span>
<span class="kn">end</span>
</pre></div>


<p>The trace generates the following output:</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">v</span> <span class="n">default</span> <span class="o">[</span><span class="n">macro</span> <span class="n">annotation</span> <span class="o">(</span><span class="n">const</span> <span class="n">nat</span> <span class="o">[])]</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="o">[</span><span class="n">macro</span> <span class="n">annotation</span> <span class="o">(</span><span class="n">const</span> <span class="n">eq</span> <span class="o">[])]</span> <span class="o">(</span><span class="n">var</span> <span class="mi">0</span><span class="o">))</span> <span class="o">[</span><span class="n">macro</span> <span class="n">annotation</span> <span class="o">(</span><span class="n">var</span> <span class="mi">2</span><span class="o">)]))</span> <span class="o">[</span><span class="n">macro</span> <span class="n">prenum</span><span class="o">])</span>
</pre></div>


<p>Notice that the @var tt 1 in the "trace" has become (var 2).  Is there a way to prevent this lifting of variables?</p>

#### [ Simon Hudon (Jul 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%25%25%20lifting%20of%20variables/near/130101029):
<p>I recommend you not to use <code>var</code> directly because much of the Lean API assumes that your expressions are closed (not <code>var</code> without their binders). What you can do is:</p>
<div class="codehilite"><pre><span></span><span class="n">do</span> <span class="n">my_var</span> <span class="bp">&lt;-</span> <span class="n">mk_local_def</span> <span class="bp">`</span><span class="n">my_var</span> <span class="bp">`</span><span class="o">(</span><span class="n">nat</span><span class="o">),</span>
   <span class="n">e</span> <span class="bp">&lt;-</span> <span class="n">to_expr</span> <span class="bp">``</span><span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span><span class="n">v</span><span class="bp">=</span><span class="err">%%</span><span class="n">my_var</span><span class="o">)</span> <span class="mi">3</span><span class="o">),</span>
   <span class="n">return</span> <span class="err">$</span> <span class="n">lambdas</span> <span class="o">[</span><span class="n">my_var</span><span class="o">]</span> <span class="n">e</span>
</pre></div>


<p>It also works with Pi-binders:</p>
<div class="codehilite"><pre><span></span>   <span class="c1">-- ...</span>
   <span class="n">return</span> <span class="err">$</span> <span class="n">pis</span> <span class="o">[</span><span class="n">my_var</span><span class="o">]</span> <span class="n">e</span>
</pre></div>


{% endraw %}
