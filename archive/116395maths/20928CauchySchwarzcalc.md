---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/20928CauchySchwarzcalc.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Cauchy-Schwarz calc](https://leanprover-community.github.io/archive/116395maths/20928CauchySchwarzcalc.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 29 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276213):
<p>Sometimes when someone new comes here to ask maths questions, I wonder if we have a new mathematician interested in Lean. So I googled <span class="user-mention" data-user-id="117987">@Patrick Stevens</span>  and found <a href="https://www.patrickstevens.co.uk/cauchy-schwarz-proof/" target="_blank" title="https://www.patrickstevens.co.uk/cauchy-schwarz-proof/">https://www.patrickstevens.co.uk/cauchy-schwarz-proof/</a></p>

#### [ Patrick Massot (May 29 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276218):
<p>So I thought: good opportunity to try again to compute with Lean</p>

#### [ Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276275):
<p>And of course I'm disappointed</p>

#### [ Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276280):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>


<span class="kn">lemma</span> <span class="n">key</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">real</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span>  <span class="n">y</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">x</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">x_pos</span> <span class="n">y_pos</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">add_pos_of_pos_of_nonneg</span> <span class="n">x_pos</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">y_pos</span><span class="o">),</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">x</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">y</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">div_le_of_le_mul</span> <span class="bp">;</span> <span class="n">assumption</span>  <span class="o">},</span>
  <span class="n">apply</span> <span class="n">le_of_sub_nonneg</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">le_of_mul_le_mul_right</span> <span class="bp">_</span> <span class="n">x_pos</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">le_of_mul_le_mul_right</span> <span class="bp">_</span> <span class="n">y_pos</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mul_sub_right_distrib</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mul_sub_right_distrib</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="bp">-</span><span class="o">((</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">b</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">/</span> <span class="n">y</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">],</span>
  <span class="n">conv</span>
  <span class="o">{</span> <span class="n">to_rhs</span><span class="o">,</span>
    <span class="n">congr</span><span class="o">,</span>
    <span class="n">skip</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">mul_assoc</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">mul_assoc</span><span class="o">,</span>
    <span class="n">congr</span><span class="o">,</span>
    <span class="n">skip</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">right_distrib</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">mul_assoc</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">x_pos</span><span class="o">),</span>
    <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="n">b</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">/</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">/</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">y</span><span class="bp">*</span><span class="n">x</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span><span class="o">[</span><span class="n">mul_comm</span><span class="o">]),</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">mul_assoc</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">y_pos</span><span class="o">)</span> <span class="o">},</span>
  <span class="k">have</span> <span class="o">:</span> <span class="bp">-</span><span class="o">((</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">b</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span><span class="bp">*</span><span class="n">y</span><span class="bp">-</span><span class="n">b</span><span class="bp">*</span><span class="n">x</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="o">:=</span>
    <span class="k">begin</span>
      <span class="n">ring</span><span class="o">,</span><span class="n">ring</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">x</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">pow_succ</span><span class="o">,</span>
    <span class="n">finish</span> <span class="o">},</span>
  <span class="n">apply</span> <span class="n">mul_self_nonneg</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276289):
<p>It's not only about the banana phone issue</p>

#### [ Patrick Massot (May 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276311):
<p>Everything has been painful</p>

#### [ Patrick Massot (May 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276316):
<p>How should I write such proofs?</p>

#### [ Patrick Stevens (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276375):
<p>That's quite a collection - it's a direct conversion of the one I linked, isn't it, which is very slick for human consumption</p>

#### [ Patrick Stevens (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276383):
<p>Presumably there are easier proofs to transcribe for Lean</p>

#### [ Andrew Ashworth (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276389):
<p>someday, <a href="https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition" target="_blank" title="https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition">https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition</a> might show up in Lean</p>

#### [ Patrick Massot (May 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276393):
<p>only the key lemma "Naturally, this lemma is trivial — once it is conceived."</p>

#### [ Patrick Massot (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276408):
<p>My interest was not in proving Cauchy-Schwarz. It was this sentence "Naturally, this lemma is trivial — once it is conceived."</p>

#### [ Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276413):
<p>use better theorems</p>

#### [ Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276424):
<p>e.g. you can use <code>add_pos</code> instead of that business</p>

#### [ Patrick Massot (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276425):
<p>I did the exercise on paper in 30 seconds and thought I would try in Lean</p>

#### [ Kenny Lau (May 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276433):
<p><code>add_pos_of_pos_of_nonneg x_pos (le_of_lt y_pos)</code></p>

#### [ Kenny Lau (May 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276482):
<p>and e.g. there is a theorem linking <code>(x+y)^-1</code> to <code>x^-1</code> and <code>y^-1</code></p>

#### [ Patrick Massot (May 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276498):
<p>I couldn't find add_pos because I was looking for add_pos_of_pos_of_pos</p>

#### [ Patrick Massot (May 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276519):
<p>The question is: I stare at my paper proof, how can I get a Lean proof?</p>

#### [ Kenny Lau (May 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276524):
<p>a lot of training and familiarity with existing theorems</p>

#### [ Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276578):
<p>I did that as training indeed</p>

#### [ Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276580):
<p>But probably Andrew is right</p>

#### [ Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276581):
<p>We need more automation</p>

#### [ Patrick Massot (May 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276583):
<p>nothing else is viable</p>

#### [ Patrick Massot (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276598):
<p>Note that the situation would be much worse without <code>ring</code></p>

#### [ Andrew Ashworth (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276621):
<p>there are limits to algorithms such as the above though. they will take forever to run if you have a particularly giant set of real inequalities since the time it takes to run increases exponentially vs the number of terms</p>

#### [ Kenny Lau (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276622):
<p>I disagree</p>

#### [ Kenny Lau (May 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276626):
<p>but I don't have time to disprove your claim</p>

#### [ Patrick Massot (May 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276696):
<p>I should be sleeping anyway (of course I thought this calculation would be shorter...)</p>

#### [ Patrick Stevens (May 30 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276810):
<p>Of course, "expand and clear denominators" should be mechanically easy, right? Is there some reason why an "expand" tactic couldn't exist? and "clear denominators" likewise, though that requires a bit of casewise am-i-negative reasoning in general</p>

#### [ Andrew Ashworth (May 30 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276908):
<p>if you stuck the same equation into Sage math, what would its simplifier spit out?</p>

#### [ Patrick Stevens (May 30 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127276986):
<p>Mathematica:</p>
<div class="codehilite"><pre><span></span>In[43]:= (a + b)^2/(x + y) &lt;= a^2/x + b^2/y //
 FullSimplify[#, x &gt; 0 &amp;&amp; y &gt; 0] &amp;

Out[43]= (b x - a y)^2 &gt;= 0
</pre></div>

#### [ Patrick Stevens (May 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277039):
<p>simplifies to True under the additional assumption that a,b are real</p>

#### [ Patrick Stevens (May 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277050):
<p>don't know about sage, i'm afraid</p>

#### [ Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277668):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">lemma</span> <span class="n">key</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hx</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">x</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">y</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">((</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">x</span><span class="bp">*</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">))</span> <span class="bp">≤</span> <span class="o">((</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">x</span><span class="bp">*</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">x</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">y</span><span class="o">),</span>
<span class="k">from</span> <span class="k">calc</span> <span class="o">((</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">x</span><span class="bp">*</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">((</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">))</span>
    <span class="bp">=</span> <span class="n">x</span><span class="bp">*</span><span class="o">(</span><span class="n">y</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">mul_div_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span><span class="o">]</span><span class="bp">;</span>
  <span class="k">from</span> <span class="n">ne_of_gt</span> <span class="o">(</span><span class="n">add_pos</span> <span class="n">Hx</span> <span class="n">Hy</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="n">x</span><span class="bp">*</span><span class="o">(</span><span class="n">y</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span><span class="bp">*</span><span class="n">y</span><span class="bp">-</span><span class="n">b</span><span class="bp">*</span><span class="n">x</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">*</span><span class="n">y</span><span class="bp">-</span><span class="n">b</span><span class="bp">*</span><span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">le_add_of_nonneg_right</span> <span class="err">$</span> <span class="n">mul_self_nonneg</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">y</span><span class="bp">*</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">x</span><span class="bp">*</span><span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">x</span><span class="bp">*</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">x</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_div_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_div_cancel&#39;</span> <span class="bp">_</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">Hy</span><span class="o">),</span> <span class="n">mul_div_assoc</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span> <span class="bp">_</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">Hx</span><span class="o">)],</span>
<span class="n">le_of_mul_le_mul_left</span> <span class="n">H</span> <span class="err">$</span> <span class="n">mul_pos</span> <span class="o">(</span><span class="n">mul_pos</span> <span class="o">(</span><span class="n">add_pos</span> <span class="n">Hx</span> <span class="n">Hy</span><span class="o">)</span> <span class="n">Hx</span><span class="o">)</span> <span class="n">Hy</span>
</pre></div>

#### [ Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277669):
<p>ok I did use <code>ring</code></p>

#### [ Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277672):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277675):
<p>and I just burnt a lot of my time</p>

#### [ Kenny Lau (May 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127277676):
<p>I'm busy</p>

#### [ Mario Carneiro (May 30 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127278096):
<div class="codehilite"><pre><span></span>import tactic.ring data.real.basic

theorem pow_two_nonneg {α} [linear_ordered_ring α] (a : α) : 0 ≤ a ^ 2 :=
by rw pow_two; exact mul_self_nonneg _

lemma key (a b x y : ℝ) (x0 : 0 &lt; x) (y0 : 0 &lt; y) : (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
begin
  apply (div_le_iff (add_pos x0 y0)).2,
  apply (mul_le_mul_left (mul_pos x0 y0)).1,
  apply sub_nonneg.1,
  refine calc x * y * ((a ^ 2 / x + b ^ 2 / y) * (x + y)) - x * y * (a + b) ^ 2
       = ((x / x * a ^ 2 * y + y / y * b ^ 2 * x) * (x + y)) - x * y * (a + b) ^ 2 : by ring
   ... = ((a ^ 2 * y + b ^ 2 * x) * (x + y)) - x * y * (a + b) ^ 2 : by simp [ne_of_gt x0, ne_of_gt y0]
   ... = (b * x - a * y) ^ 2 : by ring; ring
   ... ≥ 0 : pow_two_nonneg _
end
</pre></div>

#### [ Mario Carneiro (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127278173):
<p>Since <code>ring</code> can handle everything except the divisions, I insert a step in the middle for <code>simp</code> to cancel the <code>x/x</code> terms, but otherwise this is all <code>ring</code></p>

#### [ Mario Carneiro (May 30 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127278788):
<p>or with a bit more up front cross multiplication:</p>
<div class="codehilite"><pre><span></span>lemma key (a b x y : ℝ) (x0 : 0 &lt; x) (y0 : 0 &lt; y) : (a+b)^2/(x+y) ≤ a^2/x + b^2/y :=
begin
  rw [div_add_div _ _ (ne_of_gt x0) (ne_of_gt y0),
    div_le_iff (add_pos x0 y0), div_mul_eq_mul_div, le_div_iff (mul_pos x0 y0),
    ← sub_nonneg],
  refine calc 0 ≤ (b * x - a * y) ^ 2 : pow_two_nonneg _
   ... = (a ^ 2 * y + x * b ^ 2) * (x + y) - (a + b) ^ 2 * (x * y) : by ring; ring
end
</pre></div>

#### [ Andrew Ashworth (May 30 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127279233):
<p>^. I feel like whenever I have a complicated thing like this, <code>calc</code> is the way to go. And I solve the whole thing by hand on scratch paper, like I time-traveled back to high-school algebra class...</p>

#### [ Kenny Lau (May 30 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127279240):
<p>throwbacks</p>

#### [ Andrew Ashworth (May 30 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127279293):
<p>but if this stuff is super obvious, and you dislike proving it, why not use <code>sorry</code>?</p>

#### [ Patrick Massot (May 30 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294574):
<p>Thank you very much Kenny and Mario. Kenny's proof is exactly what I don't want to do (and nobody should have to do if proof assistants want to become tools for mathematicians). Mario's proof is what I wanted to do (clear denominators and use ring). I think the most important thing I missed was:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span> <span class="bp">/</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span>  <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span> <span class="bp">*</span><span class="n">x</span> <span class="bp">/</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span>
</pre></div>


<p>I thought that, in such a case, <code>ring</code> would see <code>(a^2 / x)</code> as atomic and fail. It makes it even harder for me to understand why <code>ring</code> couldn't be extended to do the whole computation, searching for <code>x &gt; 0</code> or <code>x ≠ 0</code> in context</p>

#### [ Johan Commelin (May 30 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294647):
<p><code>ring</code> doesn't know anything about orders, right? So it doesn't know what to do with <code>x &gt; 0</code>.</p>

#### [ Patrick Massot (May 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294690):
<p>it could try to apply <code>ne_of_gt</code> and <code>ne_of_lt</code> on all hypotheses</p>

#### [ Patrick Massot (May 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294714):
<p>One more question for Mario: why did you use <code>refine</code> instead of <code>exact</code>, which also works and is more explicit?</p>

#### [ Johan Commelin (May 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294715):
<p>Buth it isn't meant to be a generic tactic. It only uses ring axioms.</p>

#### [ Patrick Massot (May 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294762):
<p>Then give another name to the more general tactic</p>

#### [ Johan Commelin (May 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294765):
<p>But you would want to do something like <code>by schoolkid using ring</code> or something like that</p>

#### [ Johan Commelin (May 30 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294825):
<p>We want a <code>schoolkid</code> tactic that does the completely easy stuff, and it should have a feature that you can give it a specialised tactic like <code>ring</code> as a hint, so that all of a sudden the schoolkid is lord of the rings.</p>

#### [ Patrick Massot (May 30 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294906):
<p>What about building a <code>clear_denominator</code> tactic? It would search for all divisions in the goal, generate sub-goals saying denominators are non-zero, try to discharge these goals using assumptions (and <code>ne_of_gt</code> and <code>ne_of_lt</code> of assumptions), check whether the goal is equality or inequality and apply <code>mul_le_mul_left</code> and its friend, followed by <code>ring</code> to simplify, and <code>simp [all stuff ≠ 0 gathered so far]</code></p>

#### [ Patrick Massot (May 30 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294965):
<p>We really need to get back Simon</p>

#### [ Patrick Massot (May 30 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127294967):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> where are you?</p>

#### [ Johan Commelin (May 30 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127295049):
<p>Right. A clear denominator tactic makes sense as well.</p>

#### [ Johan Commelin (May 30 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127295106):
<p>So, here is a proposal for <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> 's next "Live Zulip": walk through a tactic file, and teach mathematicians how to write tactics (-;</p>

#### [ Simon Hudon (May 30 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303161):
<p>Hey <span class="user-mention" data-user-id="110031">@Patrick Massot</span>! I haven't completely disappeared. Is it just me or has there been a whole lot more activity in here? It's getting hard to follow part time!</p>

#### [ Simon Hudon (May 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303262):
<p>I'm not sure I get what <code>clear_denominator</code> would do exactly. How does <code>mul_le_mul_left</code> help with division?</p>

#### [ Sean Leather (May 30 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303516):
<blockquote>
<p>Is it just me or has there been a whole lot more activity in here?</p>
</blockquote>
<p>It's not just you. Even being away from Zulip for a weekend leaves one with thousands of messages to either wade through or mark as read. <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Simon Hudon (May 30 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303597):
<p>I thought the Zulip threads would help keeping track of stuff. I'm not sure what would make it easier</p>

#### [ Simon Hudon (May 30 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303640):
<p>The plus side is, it's awesome that Lean is getting used like this</p>

#### [ Patrick Massot (May 30 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303852):
<p>We have trouble with thread discipline</p>

#### [ Patrick Massot (May 30 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127303855):
<p>But we try</p>

#### [ Simon Hudon (May 30 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127305130):
<p>Yeah? What kind of trouble? It seems like specific threads are getting created for the right subjects. The problem might just be in the number of threads. I don't know if we need to categorize them better or something else</p>

#### [ Patrick Massot (May 30 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127305822):
<p>Many thread actually mix different topics</p>

#### [ Mario Carneiro (May 30 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306593):
<p>I think Kevin should speak in complete sentences</p>

#### [ Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306602):
<p>instead of fragments</p>

#### [ Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306607):
<p>of sentences</p>

#### [ Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306617):
<p>that create tons of messages and fill</p>

#### [ Mario Carneiro (May 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306622):
<p>my screen</p>

#### [ Simon Hudon (May 30 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127306911):
<p>Yeah I noticed that too. Also, write one message with one self contained question and wait for an answer. Right now, when I see his messages I don't know when he's going to be done writing and I eventually just stop reading. One message would help me (and I suspect others) decide whether the question is something I can help with</p>

#### [ Patrick Massot (May 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127312365):
<p>Why did you provoked him?!</p>

#### [ Simon Hudon (May 30 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315830):
<p>Provoke how?</p>

#### [ Patrick Massot (May 30 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315894):
<p>Did you see how many times he hit return in the middle of a sentence since you posted that message?</p>

#### [ Patrick Massot (May 30 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315903):
<p>That's all your fault <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Simon Hudon (May 30 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315921):
<p>Haha! I'm secretly a terrorist!</p>

#### [ Simon Hudon (May 30 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315925):
<p>Sorry typo: theorist</p>

#### [ Simon Hudon (May 30 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127315967):
<p>I don't follow that thread so I didn't suffer the consequences of that carnage</p>

#### [ Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317785):
<blockquote>
<p>So, here is a proposal for <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> 's next "Live Zulip": walk through a tactic file, and teach mathematicians how to write tactics (-;</p>
</blockquote>
<p>So I was just catching up in this thread, and you and Patrick were talking about tactics and "maybe Simon can write us a tactic" -- and who is the only mathematician who knows how to write tactics? I reckon it's <span class="user-mention" data-user-id="110087">@Scott Morrison</span> . Scott -- how did you learn to write tactics? I don't want to keep pestering Simon. I see dumb stuff like the proof that pnat is a comm_monoid, and the proof of every axiom is "it's true for nat so done"</p>

#### [ Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317833):
<p>and that happened to me several times myself when doing comm_ring stuff with schemse</p>

#### [ Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317842):
<p>"I've got to prove this direct limit satisfies all the ring axioms"</p>

#### [ Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317843):
<p>"let's see what this entails"</p>

#### [ Kevin Buzzard (May 30 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317850):
<p>"it entails invoking that same axiom for that other ring"</p>

#### [ Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317866):
<p>It's about time I learnt to automate that. It comes up a lot.</p>

#### [ Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317878):
<p>When we start on perfectoid spaces we'll be proving limits of topological rings are topological rings</p>

#### [ Kevin Buzzard (May 30 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317892):
<p>there's going to be a lot of "this proof is obvious but not rfl" stuff</p>

#### [ Kevin Buzzard (May 30 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127317937):
<p>and this can surely be done with tactics</p>

#### [ Simon Hudon (May 30 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127320901):
<p>I actually enjoy getting your automation challenges. I admit (sorry!) that I'm not as quick to address them as I'd like. And lately, I've only gotten slower as I took a part time job and stepped up my writing efforts</p>

#### [ Sebastien Gouezel (May 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127322540):
<p>Just for fun, I checked it in Isabelle to see where next-level automation can get you. It did not work directly, but almost:</p>
<div class="codehilite"><pre><span></span>lemma
  fixes a b x y::real
  assumes &quot;x &gt; 0&quot; &quot;y &gt; 0&quot;
  shows &quot;(a+b)^2/(x+y) ≤ a^2/x + b^2/y&quot;
proof -
  have &quot;(a * y - b * x)^2 ≥ 0&quot; by simp
  then show ?thesis
    using assms by (simp add: algebra_simps divide_simps power2_eq_square)
qed
</pre></div>


<p>I first tried to show the goal just by applying <code>simp</code> with <code>divide_simps</code> and  <code>algebra_simps</code> (simplification rules which clear out divisors, and apply associativity, commutativity), but square expansion is not automatic so I had to add it simp. It reduced everything to something which clearly was equivalent to the positivity of <code>(ay-bx)^2</code>, so I added it as an intermediate step, and done. No piece of paper, no computation on my side (and no fancy tactic such as <code>ring</code> or <code>omega</code>, everything was done by the simplifier). I really hope Lean can do the same in the near future!</p>

#### [ Mario Carneiro (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127322647):
<p>The main problem with using <code>simp</code> for ring equalities is that simp isn't good with cancelling negatives</p>

#### [ Sebastien Gouezel (May 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127323145):
<p>To be honest, <code>simp</code> in Isabelle is in fact <code>simp</code> on steroids: it has built-in "simprocs" that will cancel out negatives, group together common factors, and things like that. I guess it makes <code>by (simp add: algebra_simps)</code> as powerful as the <code>ring</code>tactic in Lean. If I understand correctly, Johannes is working on simprocs for Lean, right?</p>

#### [ Johannes Hölzl (May 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127323497):
<p>Yes, I'm working on a simplifier tactic with simp proc support.</p>

#### [ Johan Commelin (May 30 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127323678):
<p>Is there a one-line explanation of what "simpprocs" are?</p>

#### [ Johannes Hölzl (May 30 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy-Schwarz%20calc/near/127324193):
<p>instead of simp rules, it is a tactic which gets invoced by the simplifier. E.g. canellation would be a simproc which is called on a pattern of the form <code>_ = _</code> where the type of _  has a cancellative monoid, then it tries to find common elements on both sides of the equation and remove them.</p>


{% endraw %}
