---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45525tacticnoobie.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic noobie](https://leanprover-community.github.io/archive/113488general/45525tacticnoobie.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947182):
<p>I'm taking a stab at the <code>tfae</code> tactic. This is what I have so far:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tfae_have</span>
  <span class="o">(</span><span class="n">p₁</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">small_nat</span><span class="o">)</span>
  <span class="o">(</span><span class="n">re</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(((</span><span class="n">tk</span> <span class="s2">&quot;→&quot;</span> <span class="bp">&lt;|&gt;</span> <span class="n">tk</span> <span class="s2">&quot;-&gt;&quot;</span><span class="o">)</span> <span class="bp">*&gt;</span> <span class="n">return</span> <span class="n">tt</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span> <span class="o">((</span><span class="n">tk</span> <span class="s2">&quot;↔&quot;</span> <span class="bp">&lt;|&gt;</span> <span class="n">tk</span> <span class="s2">&quot;&lt;-&gt;&quot;</span><span class="o">)</span> <span class="bp">*&gt;</span> <span class="n">return</span> <span class="n">ff</span><span class="o">)))</span>
  <span class="o">(</span><span class="n">p₂</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">small_nat</span><span class="o">)</span>
  <span class="o">(</span><span class="n">discharger</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">solve_by_elim</span> <span class="bp">&lt;|&gt;</span> <span class="n">tauto</span> <span class="bp">&lt;|&gt;</span> <span class="n">using_smt</span> <span class="o">(</span><span class="n">smt_tactic</span><span class="bp">.</span><span class="n">intros</span> <span class="bp">&gt;&gt;</span> <span class="n">smt_tactic</span><span class="bp">.</span><span class="n">solve_goals</span><span class="o">)))</span> <span class="o">:</span>
  <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">do</span>
    <span class="n">g</span> <span class="bp">&lt;-</span> <span class="n">get_goals</span><span class="o">,</span>
</pre></div>


<p>Now I would like to loop over my goals, and check if any of them has the form <code>tfae [P, Q, ..., bla]</code>. How do I do that?</p>

#### [ Reid Barton (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947374):
<p>maybe we can cocalc this?</p>

#### [ Johan Commelin (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947386):
<p>Sure!</p>

#### [ Johan Commelin (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947393):
<p>Just in the big project?</p>

#### [ Reid Barton (Sep 14 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947467):
<p>Seems easiest</p>

#### [ Johan Commelin (Sep 14 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947471):
<p>I'm there</p>

#### [ Reid Barton (Sep 14 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947610):
<p>Maybe working on the main goal (<code>target</code>) is good enough. I'm looking at the split_ifs code and that is what it does</p>

#### [ Reid Barton (Sep 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947696):
<p>I think this is going to need the tfae stuff to be defined already</p>


{% endraw %}
