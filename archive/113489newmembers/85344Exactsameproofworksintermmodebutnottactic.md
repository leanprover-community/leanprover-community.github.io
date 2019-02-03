---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/85344Exactsameproofworksintermmodebutnottactic.html
---

## Stream: [new members](index.html)
### Topic: [Exact same proof works in term mode but not tactic](85344Exactsameproofworksintermmodebutnottactic.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838170):
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">abs_of_pos</span> <span class="n">two_pos</span>
</pre></div>


<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">apply</span> <span class="n">abs_of_pos</span><span class="o">,</span> <span class="n">exact</span> <span class="n">two_pos</span> <span class="kn">end</span>
</pre></div>


<p>This doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">apply</span> <span class="n">abs_of_pos</span> <span class="o">(</span><span class="n">two_pos</span><span class="o">)</span> <span class="kn">end</span>
</pre></div>


<p>This doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">apply</span> <span class="bp">@</span><span class="n">abs_of_pos</span> <span class="bp">_</span> <span class="bp">_</span> <span class="mi">2</span> <span class="o">(</span><span class="n">two_pos</span><span class="o">)</span> <span class="kn">end</span>
</pre></div>


<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">rw</span> <span class="n">abs_of_pos</span><span class="o">,</span> <span class="n">exact</span> <span class="n">two_pos</span> <span class="kn">end</span>
</pre></div>


<p>This doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">rw</span> <span class="n">abs_of_pos</span> <span class="o">(</span><span class="n">two_pos</span><span class="o">)</span> <span class="kn">end</span>
</pre></div>


<p>Why? What's going on?</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838350):
<p>Oh, and this works: </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">lemma</span> <span class="n">DUH</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">exact</span> <span class="n">abs_of_pos</span> <span class="o">(</span><span class="n">two_pos</span><span class="o">)</span> <span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838487):
<p>I can understand there may be some "metavariables make things weird" explanation for <code>exact</code> working where <code>apply</code> doesn't, but I really don't get why the two rewrites have different results.</p>

#### [ Patrick Massot (Nov 16 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839688):
<p>This all about elaboration</p>

#### [ Patrick Massot (Nov 16 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839772):
<p>The elaborator needs to guess the type of 2 in 2 &gt; 0 (which is the statement of <code>two_pos</code>). When it tries to do that too early this fails</p>

#### [ Patrick Massot (Nov 16 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839801):
<p>You could probably save all attempts by type ascribing this two_pos using <code>(two_pos : (2 : R) &gt; 0)</code></p>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839856):
<p>Ah yes, it seems <code>apply @abs_of_pos ℝ _ 2 (two_pos)</code> works too.</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839979):
<p>But how does that explain <code>exact</code> working where <code>apply</code> doesn't?</p>

#### [ Mario Carneiro (Nov 16 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840032):
<p>apply needs to guess how many pis the result type has</p>

#### [ Mario Carneiro (Nov 16 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840095):
<p><code>apply x</code> is basically the same as <code>refine x _ _ _</code> where the number of underscores depends on the type of <code>x</code></p>

#### [ Mario Carneiro (Nov 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840125):
<p>This means that when elaborating <code>x</code> we don't know what type it is yet, while with <code>refine</code> or <code>exact</code> we know the type of <code>x</code> is the type of the goal</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840325):
<p>That makes sense. Thanks.</p>


{% endraw %}
