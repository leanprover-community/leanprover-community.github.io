---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06147underhandedlean.html
---

## Stream: [general](index.html)
### Topic: [underhanded lean](06147underhandedlean.html)

---


{% raw %}
#### [ Mario Carneiro (Dec 27 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/underhanded%20lean/near/152579911):
<p>wow, I didn't expect this to work:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span>

<span class="bp">@</span><span class="o">[</span><span class="n">user_command</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">my_print</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">parse</span> <span class="err">$</span> <span class="n">tk</span> <span class="s2">&quot;#print&quot;</span><span class="o">)</span> <span class="o">:</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">tk</span> <span class="s2">&quot;axioms&quot;</span> <span class="bp">&gt;&gt;</span> <span class="n">ident</span> <span class="err">$</span><span class="bp">&gt;</span> <span class="n">trace</span> <span class="s2">&quot;totally ok&quot;</span> <span class="o">()</span><span class="bp">.</span>

<span class="bp">@</span><span class="o">[</span><span class="n">user_command</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">my_def</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">parse</span> <span class="err">$</span> <span class="n">tk</span> <span class="s2">&quot;def&quot;</span><span class="o">)</span> <span class="o">:</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">ident</span> <span class="bp">&gt;&gt;</span> <span class="n">tk</span> <span class="s2">&quot;:&quot;</span> <span class="bp">&gt;&gt;</span> <span class="n">texpr</span> <span class="bp">&gt;&gt;</span> <span class="n">tk</span> <span class="s2">&quot;:=&quot;</span> <span class="bp">&gt;&gt;</span> <span class="n">ident</span> <span class="err">$</span><span class="bp">&gt;</span> <span class="n">trace</span> <span class="s2">&quot;looks good to me&quot;</span> <span class="o">()</span><span class="bp">.</span>

<span class="n">def</span> <span class="n">contradiction</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sure</span> <span class="c1">-- looks good to me</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">contradiction</span> <span class="c1">-- totally ok</span>
</pre></div>


<p>Apparently you can override basically all lean command tokens, including <code>section</code>, <code>namespace</code>, <code>def</code> and <code>end</code></p>

#### [ Keeley Hoek (Dec 27 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/underhanded%20lean/near/152597048):
<p>Yep<br>
At one point I tried a sneaky 'begin' override, but the problem is you can never close a block you open</p>


{% endraw %}
