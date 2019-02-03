---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27081Leavetermmodecalconceyouenterit.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Leave term mode/calc once you enter it?](https://leanprover-community.github.io/archive/113489newmembers/27081Leavetermmodecalconceyouenterit.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604247):
<p>Part of my proof involved calc, but now I want to return to tactic mode to complete my proof. How do I do this?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604263):
<p>The way I've done this in the past is to do the term mode in a separate lemma.</p>

#### [ Andrew Ashworth (Oct 11 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604665):
<p>just type <code>begin</code> <code>end</code> again</p>

#### [ Mario Carneiro (Oct 11 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604690):
<p>depends on how you have set it up. You could have the calc block inside tactic mode, or you could have a tactic block in one of the steps of a calc block</p>

#### [ Kevin Buzzard (Oct 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135605855):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">show</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">5</span><span class="o">,</span>
  <span class="n">exact</span> <span class="k">calc</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">3</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
        <span class="bp">...</span>        <span class="bp">=</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
        <span class="bp">...</span>        <span class="bp">=</span> <span class="mi">5</span>     <span class="o">:</span> <span class="k">begin</span>
             <span class="k">show</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span><span class="o">,</span>
             <span class="c1">-- I&#39;m not getting anywhere</span>
             <span class="n">sorry</span>
        <span class="kn">end</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span>  -- post a MWE if what I said doesn't help.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607561):
<p>Here's the code:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">definition</span> <span class="n">cong_mod_37</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="mi">37</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span>

<span class="kn">theorem</span> <span class="n">cong_mod_37_equiv_reln</span> <span class="o">:</span> <span class="n">equivalence</span> <span class="n">cong_mod_37</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">reflexive</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">cong_mod_37</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">sub_self</span><span class="o">,</span>
    <span class="n">fapply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
      <span class="n">exact</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">symmetric</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">HXY</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">cong_mod_37</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">cong_mod_37</span> <span class="n">at</span> <span class="n">HXY</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">HXY</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
    <span class="n">fapply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
      <span class="n">exact</span> <span class="bp">-</span><span class="n">n</span><span class="o">,</span>
    <span class="k">show</span> <span class="mi">37</span> <span class="bp">*</span> <span class="bp">-</span><span class="n">n</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">exact</span> <span class="k">calc</span> <span class="mi">37</span> <span class="bp">*</span> <span class="bp">-</span><span class="n">n</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">(</span><span class="mi">37</span><span class="bp">*</span><span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">neg_mul_eq_mul_neg</span>
          <span class="bp">...</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">(</span><span class="n">x</span> <span class="bp">-</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">Hn</span>
          <span class="bp">...</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">x</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">neg_sub</span>
<span class="c1">--split,</span>
    <span class="n">rw</span> <span class="n">transitive</span><span class="o">,</span>

    <span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607593):
<p>I did what you said, but that doesn't work.</p>

#### [ Rob Lewis (Oct 11 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607681):
<p>You need a comma at the end of the <code>calc</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607719):
<p>Oh... thanks. Yep, now it's working.</p>


{% endraw %}
