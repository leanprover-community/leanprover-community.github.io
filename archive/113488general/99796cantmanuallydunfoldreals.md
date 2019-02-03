---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99796cantmanuallydunfoldreals.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [can't manually `dunfold` reals](https://leanprover-community.github.io/archive/113488general/99796cantmanuallydunfoldreals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 21 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148102409):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="c1">-- from data.real.basic</span>
<span class="c1">-- def real := @cau_seq.completion.Cauchy ℚ _ _ _ abs _</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">real</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">completion</span><span class="bp">.</span><span class="n">Cauchy</span> <span class="n">ℚ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">abs</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- fails</span>



<span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">real</span><span class="bp">.</span><span class="n">equations</span> <span class="c1">-- equations lemmas for real numbers</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">real</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span>

<span class="c1">-- real.equations._eqn_1 : ℝ = cau_seq.completion.Cauchy</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">real</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">@[_refl_lemma]</span>
<span class="cm">theorem real.equations._eqn_1 : ℝ = cau_seq.completion.Cauchy :=</span>
<span class="cm">eq.refl ℝ</span>

<span class="cm">-/</span>

<span class="c1">-- this fails too</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">real</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">@</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">completion</span><span class="bp">.</span><span class="n">Cauchy</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span> <span class="mi">0</span><span class="o">}</span> <span class="n">rat</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span> <span class="n">rat</span> <span class="n">rat</span><span class="bp">.</span><span class="n">comm_ring</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">abs</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">rat</span> <span class="n">rat</span><span class="bp">.</span><span class="n">decidable_linear_ordered_comm_group</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">abs_is_absolute_value</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">rat</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span><span class="o">))</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">ℝ</span> <span class="c1">-- fails</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- ⊢ real</span>
  <span class="n">rw</span> <span class="n">real</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span><span class="o">,</span>
  <span class="c1">-- this works, and changes goal to</span>
  <span class="c1">-- ⊢ @cau_seq.completion.Cauchy.{0 0} rat rat.discrete_linear_ordered_field rat rat.comm_ring</span>
  <span class="c1">--  (@abs.{0} rat rat.decidable_linear_ordered_comm_group)</span>
  <span class="c1">--  (@abs_is_absolute_value.{0} rat rat.discrete_linear_ordered_field)</span>
  <span class="n">exact</span> <span class="mi">37</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Are the reals not definitionally equal to their definition? Have I done something silly? I can't reconstruct the proof of the equation lemma.</p>

#### [ Keeley Hoek (Nov 21 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148102574):
<p>Does it have anything to do with <code>real</code> being marked <code>irreducible</code> here?: <a href="https://github.com/leanprover/mathlib/blob/9f5099ec2cd933822ba3d422e74189d3508e5d0e/data/real/basic.lean#L198" target="_blank" title="https://github.com/leanprover/mathlib/blob/9f5099ec2cd933822ba3d422e74189d3508e5d0e/data/real/basic.lean#L198">https://github.com/leanprover/mathlib/blob/9f5099ec2cd933822ba3d422e74189d3508e5d0e/data/real/basic.lean#L198</a></p>

#### [ Rob Lewis (Nov 21 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148102599):
<p>It does. It will work if you add <code>local attribute [semireducible] real</code>.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148102968):
<p>So irreducibility even stops <code>rfl</code> working?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148103274):
<p>It seems like a <em>really</em> good idea from the point of mathematics to have <code>real</code> treated as a constant. There is more than one way to implement it (Dedekind cuts, Cauchy sequences) and hence mathematicians should not care about the implementation. I noticed that even <code>set_option pp.all true</code> would not unfold it. This seems like "correct" behaviour. I understand that <code>rat</code> is treated as a constant -- from Lean's point of view it <em>is</em> a constant, right? It's an inductive type. <code>real</code> is the only odd one out, I think -- all the rest are inductive types I guess.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148103486):
<p>So what does <code>set_option pp.all true</code> unfold? I see I can change its output changing with <code>dunfold</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- ⊢ real</span>
  <span class="n">rw</span> <span class="n">real</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span><span class="o">,</span>
  <span class="c1">-- ⊢ @cau_seq.completion.Cauchy.{0 0} rat rat.discrete.blah...</span>
  <span class="n">dunfold</span> <span class="n">cau_seq</span><span class="bp">.</span><span class="n">completion</span><span class="bp">.</span><span class="n">Cauchy</span><span class="o">,</span>
  <span class="c1">-- ⊢ @quotient.{1} (@cau_seq.{0 0} rat...</span>
  <span class="n">dunfold</span> <span class="n">quotient</span><span class="o">,</span>
  <span class="c1">-- ⊢ @quot.{1} (@cau_seq.{0 0} rat...</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 21 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148103518):
<p>I thought <code>pp.all</code> unfolded as much as it could. But these definitions like <code>cau_seq.completion.Cauchy</code> don't seem to be tagged with anything in particular.</p>

#### [ Sebastian Ullrich (Nov 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148103809):
<p><code>pp.all</code> doesn't unfold anything. It just shows information that is usually omitted, but always there in the term</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148104280):
<p>Aah! So when one gets huge expansion in term length after switching <code>pp.all</code> on -- as often happens to me -- this is perhaps often due to type class inference, which is always there in the term because it "works via <code>@</code>" rather than working by unfolding definitions.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148104837):
<p>So what's going on here?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">theorem</span> <span class="n">hard</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="c1">-- 13 lines of output; excerpts below.</span>

  <span class="c1">-- ⊢ ... @has_add.add.{0} real ...</span>
  <span class="n">unfold</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="c1">-- ⊢ ... @distrib.add.{0} real ...</span>
  <span class="n">unfold</span> <span class="n">distrib</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="c1">-- ⊢ ... @ring.add.{0} real real.ring ...</span>
  <span class="n">unfold</span> <span class="n">ring</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="c1">-- ... @comm_ring.add.{0} real real.comm_ring ...</span>
  <span class="n">unfold</span> <span class="n">comm_ring</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="c1">-- ... @comm_ring.add.{0} real real.comm_ring_aux ...</span>
  <span class="c1">-- next line fails</span>
  <span class="n">unfold</span> <span class="n">comm_ring</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span> <span class="c1">-- simplify tactic failed to simplify</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Nov 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148104929):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L198" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L198">https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L198</a></p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148104956):
<p>but I can presumably keep going somehow? Is there an equation lemma I can use?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148105101):
<p>got it</p>

#### [ Rob Lewis (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148105102):
<p>You can <code>rw real.comm_ring_aux</code>. Or, in general, you can use <code>#print prefix</code> to look for specific equation lemmas. <code>#print prefix real.comm_ring_aux</code></p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148105109):
<div class="codehilite"><pre><span></span>  <span class="n">rw</span> <span class="n">real</span><span class="bp">.</span><span class="n">comm_ring_aux</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">comm_ring</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
</pre></div>


<p>So again irreducibility stopped me from proceeding.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148105127):
<p>But it was difficult for me to guess that the problem was with <code>real.comm_ring_aux</code> -- I just thought <code>comm_ring.add</code> was being silly.</p>

#### [ Mario Carneiro (Nov 21 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148106480):
<p>if you really really want to unfold <code>real</code>, you can use <code>delta</code></p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107368):
<p>I am confused about whether one should regard <code>real</code> and <code>@cau_seq.completion.Cauchy ℚ _ _ _ abs _</code> as definitionally equal. They are equal by definition, but <code>rfl</code> will not prove it.</p>

#### [ Patrick Massot (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107369):
<p>Kevin, could you explain what you are trying to do? I didn't manage to guess from messages in this thread.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107378):
<p>This is not mathematics.</p>

#### [ Patrick Massot (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107379):
<p>What would be a realistic lemma you'd want to prove?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107386):
<p>I am trying to understand equality better; I was thinking of making a blog post about it.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107395):
<p>Every time I think about it, I understand it a little more.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107469):
<p>Sometimes when I was just completely stuck at Lean in the early days, it was because I didn't understand equality well enough. As you know Patrick, computer science equality is far harder than mathematics equality. I was trying to write some post where I explain this to mathematicians, but then I realised I didn't really understand it well enough to explain it myself.</p>

#### [ Sebastian Ullrich (Nov 21 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148107546):
<p>The short answer is: the kernel says they are defeq, but the elaborator says they are not. Because the elaborator respects reducibility hints for efficiency reasons.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%27t%20manually%20%60dunfold%60%20reals/near/148108095):
<p>Sebastian many thanks for your succinct but extremely helpful contributions to this thread.</p>


{% endraw %}
