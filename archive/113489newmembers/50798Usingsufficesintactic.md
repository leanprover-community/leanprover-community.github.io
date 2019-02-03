---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50798Usingsufficesintactic.html
---

## Stream: [new members](index.html)
### Topic: [Using suffices in tactic](50798Usingsufficesintactic.html)

---


{% raw %}
#### [ Ken Roe (Jul 29 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20suffices%20in%20tactic/near/130509641):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
    <span class="o">(</span><span class="n">f</span><span class="o">,</span><span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span><span class="bp">=</span><span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
   <span class="n">do</span> <span class="o">{</span>
       <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
       <span class="n">trace</span> <span class="n">t</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
       <span class="n">suffices</span> <span class="n">xx</span><span class="o">:(</span><span class="mi">1</span><span class="bp">==</span><span class="mi">2</span><span class="o">),</span><span class="n">admit</span>
   <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


<p>Can someone correct the syntax of the above.  I would like to use "suffices" rather than "change" for a tactic.  I get the following error:</p>
<div class="codehilite"><pre><span></span><span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">13</span><span class="o">:</span><span class="mi">26</span><span class="o">:</span> <span class="n">error</span>
<span class="n">invalid</span> <span class="n">expression</span><span class="o">,</span> <span class="err">&#39;</span><span class="k">by</span><span class="err">&#39;</span><span class="o">,</span> <span class="err">&#39;</span><span class="k">begin</span><span class="err">&#39;</span><span class="o">,</span> <span class="err">&#39;</span><span class="o">{</span><span class="err">&#39;</span><span class="o">,</span> <span class="n">or</span> <span class="err">&#39;</span><span class="k">from</span><span class="err">&#39;</span> <span class="n">expected</span>
<span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">13</span><span class="o">:</span><span class="mi">26</span><span class="o">:</span> <span class="n">error</span>
<span class="n">invalid</span> <span class="n">suffices</span><span class="bp">-</span><span class="n">expression</span><span class="o">,</span> <span class="n">term</span>
  <span class="n">admit</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="mi">1</span> <span class="bp">==</span> <span class="mi">2</span> <span class="o">:</span> <span class="kt">Prop</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20suffices%20in%20tactic/near/130510012):
<p><span class="user-mention" data-user-id="121304">@Ken Roe</span> what are your imports?</p>

#### [ Ken Roe (Jul 29 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20suffices%20in%20tactic/near/130510199):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">monad</span>
<span class="kn">open</span> <span class="n">expr</span>
<span class="kn">open</span> <span class="n">smt_tactic</span><span class="bp">.</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20suffices%20in%20tactic/near/130510202):
<p>...</p>

#### [ Simon Hudon (Jul 29 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20suffices%20in%20tactic/near/130514795):
<p>those are not imports, they are open statements</p>


{% endraw %}
