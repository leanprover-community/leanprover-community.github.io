---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42283intersections.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [intersections](https://leanprover-community.github.io/archive/113488general/42283intersections.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129031496):
<p>Do we have a better way to do</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="o">(</span><span class="n">a</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span> <span class="n">x</span> <span class="bp">;</span> <span class="n">split</span> <span class="bp">;</span> <span class="n">finish</span>
</pre></div>

#### [ Patrick Massot (Jul 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129031518):
<p>Of course I'm not asking for the magic sequence of rewrite, I want Lean to figure it out.</p>

#### [ Sean Leather (Jul 04 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129068018):
<p>It would be nice if there was. I run into something similar with conjunction  (e.g. <code>a ∧ b ∧ (a ∧ c) = a ∧ b ∧ c</code>) all the time.</p>

#### [ Simon Hudon (Jul 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129068883):
<p>does <code>cc</code> help?</p>

#### [ Patrick Massot (Jul 04 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129073167):
<p>no</p>

#### [ Patrick Massot (Jul 04 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129083986):
<p>A related question is: can anyone bring <a href="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html" target="_blank" title="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html">https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html</a> up to date with current Lean?</p>

#### [ Reid Barton (Jul 04 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086682):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> for <code>a ∧ b ∧ (a ∧ c) ↔ a ∧ b ∧ c</code>, <code>tauto</code> works.</p>

#### [ Sean Leather (Jul 04 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086756):
<p>Yeah, that may be true for that example. But I've run into others where <code>tauto</code> didn't work.</p>

#### [ Reid Barton (Jul 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086829):
<p>Yes, <code>tauto</code> is good at failing frustratingly close to the goal</p>

#### [ Sean Leather (Jul 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086836):
<p><code>true</code><span class="emoji emoji-2757" title="exclamation">:exclamation:</span></p>

#### [ Simon Hudon (Jul 04 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090032):
<blockquote>
<p>Yes, <code>tauto</code> is good at failing frustratingly close to the goal</p>
</blockquote>
<p>Excellent, that's what I wrote it for</p>

#### [ Simon Hudon (Jul 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090080):
<p>But seriously, any examples of what it can't handle?</p>

#### [ Reid Barton (Jul 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090724):
<p>as alluded to above, <code>example (p : Prop) : p ∧ true ↔ p := by tauto</code></p>

#### [ Reid Barton (Jul 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090747):
<p>Somewhat less trivially, I often find it gets stuck needing to prove <code>a = b</code> when <code>b = a</code> is available as a hypothesis</p>

#### [ Simon Hudon (Jul 04 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090994):
<p>The latter should be getting better. <span class="user-mention" data-user-id="110087">@Scott Morrison</span> recently submitted a patch to consider the symmetry of relations in <code>solve_by_elim</code> which <code>tauto</code> uses.</p>

#### [ Simon Hudon (Jul 04 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091055):
<p>As for the first, <code>true</code> is probably the culprit. That's an easy fix, I can submit a PR right away</p>

#### [ Simon Hudon (Jul 04 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091070):
<p>While I'm at it, I'll also take care of <code>false</code> in the assumptions.</p>

#### [ Simon Hudon (Jul 04 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091736):
<p>Done: <a href="https://github.com/leanprover/mathlib/pull/175" target="_blank" title="https://github.com/leanprover/mathlib/pull/175">https://github.com/leanprover/mathlib/pull/175</a></p>

#### [ Patrick Massot (Jul 04 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091823):
<p>Simon, what is the relation between this <code>tauto</code> and <a href="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html" target="_blank" title="https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html">https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html</a> Would you be able to update the later?</p>

#### [ Simon Hudon (Jul 04 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092168):
<p>I haven't looked closely but that should be doable.</p>

#### [ Simon Hudon (Jul 04 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092252):
<p>I'll take a look</p>

#### [ Simon Hudon (Jul 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092447):
<p>By the way, don't despair, I haven't forgotten your request for tutorials</p>

#### [ Simon Hudon (Jul 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092479):
<p>I'm preparing a talk about Lean tactics that I'll give at the DeepSpec summer school. That should be the seed for a useful tutorial</p>

#### [ Patrick Massot (Jul 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092537):
<p>Nice!</p>

#### [ Simon Hudon (Jul 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092543):
<p>I think I'll present the <code>transportable</code> problem that <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> brought in a few months ago</p>

#### [ Kevin Buzzard (Jul 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129093692):
<p>+1 from me -- as I've probably said 100 times, this is something which mathematicians do subconsciously.</p>

#### [ Johan Commelin (Jul 04 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129094956):
<p>(And that is <em>subconsciously</em>, with big fat capital letters <span class="emoji emoji-1f609" title="wink">:wink:</span>)</p>

#### [ Sean Leather (Jul 05 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129120435):
<p>Reid:</p>
<blockquote>
<p>Somewhat less trivially, I often find it gets stuck needing to prove <code>a = b</code> when <code>b = a</code> is available as a hypothesis</p>
</blockquote>
<p>Same here! That's the main reason I gave up on using <code>tauto</code>.</p>
<p>Simon:</p>
<blockquote>
<p>The latter should be getting better. Scott Morrison recently submitted a patch to consider the symmetry of relations in <code>solve_by_elim</code> which <code>tauto</code> uses.</p>
</blockquote>
<p>Cool. I'll have to try it out again.</p>

#### [ Simon Hudon (Jul 05 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129121112):
<p>Also, Mario merged my PR today. The one thing <code>tauto</code> doesn't do well still is proving disjunction. I didn't want to do back tracking out of fear that it would get slow but maybe I should do it anyway</p>

#### [ Patrick Massot (Jul 05 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145707):
<p>Here is what I can currently do on this topic:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">c</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>


<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="o">(</span><span class="n">a</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="bp">→</span>  <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="bp">→</span>  <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp_inter</span>
</pre></div>

#### [ Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145771):
<p>This is based on the <code>destruct_conjunctions</code> tactic from PIL and then poor's man tactic writing</p>

#### [ Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145780):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">monad</span> <span class="n">expr</span>
<span class="c">/-</span><span class="cm">- Recursively destructs all hypotheses that are conjunctions. From programming in Lean. -/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">destruct_conjunctions</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">repeat</span> <span class="o">(</span><span class="n">do</span>
  <span class="n">l</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="n">first</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">ht</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span> <span class="bp">&gt;&gt;=</span> <span class="n">whnf</span><span class="o">,</span>
    <span class="k">match</span> <span class="n">ht</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">and</span> <span class="err">%%</span><span class="n">a</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
      <span class="n">n</span> <span class="err">←</span> <span class="n">get_unused_name</span> <span class="bp">`</span><span class="n">h</span> <span class="n">none</span><span class="o">,</span>
      <span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">a</span><span class="o">,</span>
      <span class="n">n</span> <span class="err">←</span> <span class="n">get_unused_name</span> <span class="bp">`</span><span class="n">h</span> <span class="n">none</span><span class="o">,</span>
      <span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">right</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">b</span><span class="o">,</span>
      <span class="n">clear</span> <span class="n">h</span>
    <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">failed</span>
    <span class="kn">end</span><span class="o">))</span>

<span class="c">/-</span><span class="cm">- Simplify proving intersection and conjunctions goals -/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">simp_inter</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="bp">`</span><span class="o">[</span>  <span class="n">destruct_conjunctions</span><span class="o">,</span>
    <span class="n">try</span> <span class="o">{</span> <span class="n">ext</span> <span class="o">}</span> <span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">split</span> <span class="o">}</span> <span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">intros</span> <span class="o">}</span><span class="bp">;</span> <span class="n">destruct_conjunctions</span><span class="o">,</span>
    <span class="n">all_goals</span> <span class="o">{</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">split</span> <span class="o">}</span> <span class="bp">;</span> <span class="n">assumption</span> <span class="o">}]</span>
</pre></div>

#### [ Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145791):
<p>Any cleaner and more general way to do this is welcome <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Jul 05 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145823):
<p>Note that all examples below should really be solved by the general purpose <code>come_on</code> tactic.</p>

#### [ Simon Hudon (Jul 05 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145893):
<p>Haha! Have you tried <code>tauto</code> since Mario merged my PR yesterday?</p>

#### [ Patrick Massot (Jul 05 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146378):
<p>No. I thought you only changed stuff is <code>true</code> or <code>false</code> appears explicitly.</p>

#### [ Patrick Massot (Jul 05 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146385):
<p>I'm upgrading</p>

#### [ Simon Hudon (Jul 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146505):
<p>In your case, it should already work, you're right</p>

#### [ Simon Hudon (Jul 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146519):
<p>but recently, there's been added support for symmetric relations and <code>true</code> and <code>false</code> appearing in formulas</p>

#### [ Patrick Massot (Jul 05 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146827):
<p><code>tauto</code> solves none of my examples</p>

#### [ Patrick Massot (Jul 05 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146833):
<p>even with updated mathlib</p>

#### [ Simon Hudon (Jul 05 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146933):
<p>and with <code>ext; tauto</code>?</p>

#### [ Patrick Massot (Jul 05 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147034):
<p>no luck</p>

#### [ Patrick Massot (Jul 05 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147044):
<p>you can try my examples, they depend on nothing else but mathlib</p>

#### [ Simon Hudon (Jul 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147374):
<p>Ok got it</p>

#### [ Simon Hudon (Jul 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147387):
<p>first <code>import data.set.basic</code>. That's where set extensionality is declared</p>

#### [ Simon Hudon (Jul 05 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147402):
<p>Next:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">c</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">dsimp</span><span class="bp">;</span> <span class="n">tauto</span>


<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">dsimp</span><span class="bp">;</span> <span class="n">tauto</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="o">(</span><span class="n">a</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">dsimp</span><span class="bp">;</span> <span class="n">tauto</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="err">∩</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span> <span class="bp">→</span>  <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="bp">→</span>  <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span> <span class="err">∩</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span>
</pre></div>

#### [ Simon Hudon (Jul 05 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147417):
<p>Unfortunately, you need to unfold set notation for <code>tauto</code> to work</p>

#### [ Simon Hudon (Jul 05 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147498):
<p>And I'm not sure that adding <code>dsimp</code> to <code>tauto</code> would be a good idea.</p>

#### [ Simon Hudon (Jul 05 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147588):
<p>What I could do is match on hypotheses and goal using definitional equality instead of pattern matching</p>

#### [ Simon Hudon (Jul 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147667):
<p>Then the first proof would become:</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">tauto</span>
</pre></div>


<p>I'm wondering if that would make <code>auto</code> slower. Maybe we could enable this feature with <code>tauto!</code></p>

#### [ Simon Hudon (Jul 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147699):
<p>(In French, that would sound like you're insulting someone, with the exclamation mark)</p>

#### [ Simon Hudon (Jul 05 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129148500):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I managed to add support for disjunction but it requires <code>tactic.interactive</code> to import <code>logic.basic</code>. I think the creation of <code>tactic.cache</code> would fix that situation. Should I submit that change in a separate PR? (separate from the traversable PR) If you need more time to review the traversable PR, I think that would be a good way to move forward</p>

#### [ Patrick Massot (Jul 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150374):
<p>It does look like one could define </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">come_one</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">try</span> <span class="o">{</span> <span class="n">ext</span> <span class="bp">;</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span><span class="o">},</span> <span class="n">try</span> <span class="o">{</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">tauto</span><span class="o">}]</span>
</pre></div>


<p>or something like this. It looks much better, thanks!</p>

#### [ Simon Hudon (Jul 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150498):
<p>:) At your service</p>

#### [ Simon Hudon (Jul 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150550):
<p>I would advise you to call it <code>COME_ON</code>. And you may want to add three exclamation marks, to communicate impatience ;-)</p>

#### [ Simon Hudon (Jul 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150584):
<p>Consider:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">COME_ON</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;!&quot;</span><span class="o">))</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Patrick Massot (Jul 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161526):
<p>The version is used currently is at <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/tactic/easy.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/tactic/easy.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/tactic/easy.lean</a> It passes both the tests I had for <code>simp_inter</code> and the <code>tauto</code> tests from mathlib.</p>

#### [ Patrick Massot (Jul 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161810):
<p>Oh, it doesn't work in my real use case :(</p>

#### [ Patrick Massot (Jul 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161817):
<p><code>failed to prove recursive application is decreasing, well founded relation</code></p>

#### [ Reid Barton (Jul 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162109):
<p>Do you have a <code>_let_match</code> or similar in the tactic state?</p>

#### [ Patrick Massot (Jul 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162191):
<p>I don't know what is similar to <code>_let_match</code> since I have no idea what it means</p>

#### [ Patrick Massot (Jul 05 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162291):
<p>The full error is:</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">prove</span> <span class="n">recursive</span> <span class="n">application</span> <span class="n">is</span> <span class="n">decreasing</span><span class="o">,</span> <span class="n">well</span> <span class="n">founded</span> <span class="n">relation</span>
  <span class="bp">@</span><span class="n">has_well_founded</span><span class="bp">.</span><span class="n">r</span>
    <span class="o">(</span><span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">),</span>
       <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_well_founded_of_has_sizeof</span>
       <span class="o">(</span><span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">),</span>
          <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">)</span>
       <span class="o">(</span><span class="n">default_has_sizeof</span>
          <span class="o">(</span><span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">),</span>
             <span class="bp">@</span><span class="n">smooth_compatible</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">)))</span>
<span class="n">Possible</span> <span class="n">solutions</span><span class="o">:</span>
  <span class="bp">-</span> <span class="n">Use</span> <span class="err">&#39;</span><span class="n">using_well_founded&#39;</span> <span class="n">keyword</span> <span class="k">in</span> <span class="n">the</span> <span class="kn">end</span> <span class="n">of</span> <span class="n">your</span> <span class="kn">definition</span> <span class="n">to</span> <span class="n">specify</span> <span class="n">tactics</span> <span class="n">for</span> <span class="n">synthesizing</span> <span class="n">well</span> <span class="n">founded</span> <span class="n">relations</span> <span class="n">and</span> <span class="n">decreasing</span> <span class="n">proofs</span><span class="bp">.</span>
  <span class="bp">-</span> <span class="n">The</span> <span class="n">default</span> <span class="n">decreasing</span> <span class="n">tactic</span> <span class="n">uses</span> <span class="n">the</span> <span class="err">&#39;</span><span class="n">assumption&#39;</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">thus</span> <span class="n">hints</span> <span class="o">(</span><span class="n">aka</span> <span class="n">local</span> <span class="n">proofs</span><span class="o">)</span> <span class="n">can</span> <span class="n">be</span> <span class="n">provided</span> <span class="kn">using</span> <span class="err">&#39;</span><span class="k">have</span><span class="err">&#39;</span><span class="bp">-</span><span class="n">expressions</span><span class="bp">.</span>
<span class="n">The</span> <span class="n">nested</span> <span class="n">exception</span> <span class="n">contains</span> <span class="n">the</span> <span class="n">failure</span> <span class="n">state</span> <span class="n">for</span> <span class="n">the</span> <span class="n">decreasing</span> <span class="n">tactic</span><span class="bp">.</span>
<span class="n">nested</span> <span class="n">exception</span> <span class="n">message</span><span class="o">:</span>
<span class="n">invalid</span> <span class="n">apply</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">unify</span>
  <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">0</span>
<span class="k">with</span>
  <span class="err">?</span><span class="n">m_1</span> <span class="bp">&lt;</span> <span class="err">?</span><span class="n">m_1</span> <span class="bp">+</span> <span class="err">?</span><span class="n">m_2</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">X</span><span class="o">,</span>
<span class="n">φ</span> <span class="n">ψ</span> <span class="n">χ</span> <span class="o">:</span> <span class="n">chart</span> <span class="n">X</span><span class="o">,</span>
<span class="n">open_triple_intersection</span> <span class="o">:</span>
  <span class="o">(</span><span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">smooth_compatible</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">),</span> <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">)</span> <span class="bp">→</span>
  <span class="n">is_open</span> <span class="o">(</span><span class="err">⇑</span><span class="n">φ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">)),</span>
<span class="n">op_φ_ψ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">,</span>
<span class="n">smooth_φ_ψ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">,</span>
<span class="n">op_ψ_φ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">,</span>
<span class="n">smooth_ψ_φ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">,</span>
<span class="n">op_ψ_χ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">,</span>
<span class="n">smooth_ψ_χ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">smooth_compatible</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">χ</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">0</span>
</pre></div>

#### [ Patrick Massot (Jul 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162377):
<p>Replacing <code>meta def easy : tactic unit := `[try { ext } , try { dsimp at * }, all_goals { tauto }]</code> by <code>meta def easy : tactic unit := `[try { ext } , try { dsimp }, all_goals { tauto }]</code> make it work in this case but fail in others. Somehow the <code>try</code> is not enough to prevent the error.</p>

#### [ Simon Hudon (Jul 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162807):
<p>Well-foundedness is only checked at the end of the proof I believe which means that it won't make individual tactics fail.</p>

#### [ Simon Hudon (Jul 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162845):
<p>You may just need to add a <code>have : _ &lt; _, from _</code> expression to state and prove that some quantity decreases in your recursive function</p>

#### [ Patrick Massot (Jul 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162858):
<p>I don't have any recursive function</p>

#### [ Patrick Massot (Jul 05 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162902):
<p>I have no idea what Lean is talking about</p>

#### [ Simon Hudon (Jul 05 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162947):
<p>Can you show the goal prior to calling the tactic? There might be a way of saying "I'm not trying to bring in the curse of recursion"</p>

#### [ Patrick Massot (Jul 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162972):
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">X</span><span class="o">,</span>
<span class="n">φ</span> <span class="n">ψ</span> <span class="n">χ</span> <span class="o">:</span> <span class="n">chart</span> <span class="n">X</span><span class="o">,</span>
<span class="n">open_triple_intersection</span> <span class="o">:</span>
  <span class="n">smooth_compatible</span> <span class="n">φ</span> <span class="n">ψ</span> <span class="bp">→</span>
  <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">φ</span> <span class="bp">→</span> <span class="n">smooth_compatible</span> <span class="n">ψ</span> <span class="n">χ</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⇑</span><span class="n">φ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">)),</span>
<span class="n">op_φ_ψ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">,</span>
<span class="n">smooth_φ_ψ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">φ</span> <span class="n">ψ</span><span class="o">,</span>
<span class="n">op_ψ_φ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">,</span>
<span class="n">smooth_ψ_φ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">ψ</span> <span class="n">φ</span><span class="o">,</span>
<span class="n">op_ψ_χ</span> <span class="o">:</span> <span class="n">is_open_intersection</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">,</span>
<span class="n">smooth_ψ_χ</span> <span class="o">:</span> <span class="n">is_smooth_transition</span> <span class="n">ψ</span> <span class="n">χ</span><span class="o">,</span>
<span class="n">op</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⇑</span><span class="n">ψ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">)),</span>
<span class="n">this</span> <span class="o">:</span> <span class="err">⇑</span><span class="n">ψ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">)</span> <span class="err">⊆</span> <span class="err">⇑</span><span class="n">ψ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span><span class="o">),</span>
<span class="n">op</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">transition</span> <span class="n">ψ</span> <span class="n">φ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="err">⇑</span><span class="n">ψ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">))),</span>
<span class="n">h</span> <span class="o">:</span>
  <span class="n">transition</span> <span class="n">ψ</span> <span class="n">φ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="err">⇑</span><span class="n">ψ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">))</span> <span class="bp">=</span>
    <span class="err">⇑</span><span class="n">φ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span> <span class="bp">=</span> <span class="n">φ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">ψ</span><span class="bp">.</span><span class="n">domain</span> <span class="err">∩</span> <span class="n">χ</span><span class="bp">.</span><span class="n">domain</span>
</pre></div>

#### [ Simon Hudon (Jul 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163052):
<p>Is the lemma that you're trying to prove  <code>open_triple_intersection</code>? If so, try <code>clear open_triple_intersection</code> before calling the tactic.</p>

#### [ Patrick Massot (Jul 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163058):
<p>Note that <code>ext, dsimp, tauto</code> works here, but I want a tactic which also works when you need to <code>dsimp</code> something from context</p>

#### [ Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163081):
<p>Indeed, this is what I'm proving</p>

#### [ Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163083):
<p>and clearing this works</p>

#### [ Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163084):
<p>WTF?</p>

#### [ Patrick Massot (Jul 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163128):
<p>Is it because I have pattern matching?</p>

#### [ Patrick Massot (Jul 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163133):
<p><a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean#L185" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean#L185">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean#L185</a></p>

#### [ Patrick Massot (Jul 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163174):
<p>Indeed</p>

#### [ Patrick Massot (Jul 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163191):
<p>If I remove the matching  and start with </p>
<div class="codehilite"><pre><span></span>  <span class="n">intros</span> <span class="n">h</span> <span class="n">h&#39;</span> <span class="n">h&#39;&#39;</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">op_φ_ψ</span><span class="o">,</span> <span class="n">smooth_φ_ψ</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h&#39;</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">op_ψ_φ</span><span class="o">,</span> <span class="n">smooth_ψ_φ</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h&#39;&#39;</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">op_ψ_χ</span><span class="o">,</span> <span class="n">smooth_ψ_χ</span><span class="bp">⟩</span><span class="o">,</span>
</pre></div>


<p>Then <code>easy</code> works</p>

#### [ Patrick Massot (Jul 05 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163245):
<p>Do you understand what happens?</p>

#### [ Patrick Massot (Jul 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163297):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  We really need a hybrid of <code>intros</code> and <code>rcases</code> that would allow writing <code>intros ⟨op_φ_ψ, smooth_φ_ψ⟩ ⟨op_ψ_φ, smooth_ψ_φ⟩ ⟨op_ψ_χ, smooth_ψ_χ⟩</code></p>

#### [ Patrick Massot (Jul 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163310):
<p>instead of the four lines of the previous code block</p>

#### [ Simon Hudon (Jul 05 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163364):
<p>The situation is that pattern matching and recursion are rooted in the same machinery</p>

#### [ Simon Hudon (Jul 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163423):
<p>When you pattern match, Lean gives you the opportunity to make a recursive call. It gives you more than you need and once you're done with the proof, it checks whether you introduced recursion / induction and makes sure that it's well-founded</p>

#### [ Simon Hudon (Jul 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163442):
<p>Tactics don't see the difference between assumptions that are in fact a recursive call and the rest</p>

#### [ Patrick Massot (Jul 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163950):
<p>Thanks</p>

#### [ Patrick Massot (Jul 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163980):
<p>I'll forget about matching and patiently wait for <code>rintros</code> to land in mathlib.</p>

#### [ Patrick Massot (Jul 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129164000):
<p>And I'll go sleeping.</p>

#### [ Simon Hudon (Jul 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129164449):
<p>You could do something like <code>clear_rec</code> that you call after pattern matching</p>

#### [ Mario Carneiro (Jul 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183277):
<blockquote>
<p>I managed to add support for disjunction but it requires tactic.interactive to import logic.basic. I think the creation of tactic.cache would fix that situation. Should I submit that change in a separate PR? (separate from the traversable PR) If you need more time to review the traversable PR, I think that would be a good way to move forward</p>
</blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I think this is a good idea. Splitting up the different unrelated parts will make it easier to merge things</p>

#### [ Simon Hudon (Jul 06 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183346):
<p>Nice, I hadn't thought of it that way but we'll kill two birds with one stone. I can pull a few more PRs from <code>traversable</code></p>

#### [ Simon Hudon (Jul 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183658):
<p>What's your opinion about using lemmas in tactics that require predicates to be decidable? Would you just let it fail if some predicate is not decidable or would you silently use <code>prop_decidable</code>?</p>

#### [ Mario Carneiro (Jul 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183777):
<p>Depends on the use case. I think <code>by_cases</code> will fail, but adding <code>prop_decidable</code> as a local instance fixes this, so this seems sufficiently flexible</p>

#### [ Simon Hudon (Jul 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183969):
<p>That's straightforward. With <code>tauto</code>, <code>decidable</code> constraints can come from a lot of different sources and become relevant without obvious reasons</p>

#### [ Mario Carneiro (Jul 06 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184379):
<p>It would be nice if the tactic reports the decidability problem in the error, that way the user can decide what to do about it</p>

#### [ Simon Hudon (Jul 06 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184508):
<p>That's true. Unfortunately, <code>tauto</code> can keep going for a while once it has failed to find a <code>decidable</code> instance</p>

#### [ Simon Hudon (Jul 06 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184704):
<p>I'm thinking that <code>tauto!</code> could add <code>prop_decidable</code> as a local instance right from the start. Then when you're not sure why <code>tauto</code> failed, you can try that and move on.</p>

#### [ Mario Carneiro (Jul 06 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187322):
<blockquote>
<p>I'll forget about matching and patiently wait for <code>rintros</code> to land in mathlib.</p>
</blockquote>
<p>Your wish is my command...</p>

#### [ Simon Hudon (Jul 06 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187353):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Tag, you're it! <a href="https://github.com/leanprover/mathlib/pull/178" target="_blank" title="https://github.com/leanprover/mathlib/pull/178">https://github.com/leanprover/mathlib/pull/178</a></p>

#### [ Patrick Massot (Jul 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187470):
<p>I love that! My next wish is you answer my Wednesday email <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Jul 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187481):
<p>And I'm sure this <code>rintro</code> tactic will soon be all over the place.</p>

#### [ Simon Hudon (Jul 06 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187492):
<p>What is this <code>rintro</code> thing?</p>


{% endraw %}
