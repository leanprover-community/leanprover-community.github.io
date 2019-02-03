---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97540statementlinter.html
---

## Stream: [general](index.html)
### Topic: [statement linter](97540statementlinter.html)

---


{% raw %}
#### [ Patrick Massot (Jul 26 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130305793):
<p>I have a new challenge in the same style as the <code>print_names</code> command, but harder. We all know how to produce the list of everything defined in the current Lean file. Now we want to filter the result, keeping only lemmas or theorems whose input contains two instances for the same type class. For instance, running this command in <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean">https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean</a> must return (among others) <code>is_closed_diagonal</code> since:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">is_closed_diagonal</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">is_closed_diagonal :</span>
<span class="cm">  ∀ {α : Type u_1} [_inst_1 : topological_space α] [_inst_4 : topological_space α] [_inst_5 : t2_space α],</span>
<span class="cm">    is_closed {p : α × α | p.fst = p.snd}</span>
<span class="cm">-/</span>
</pre></div>


<p>(this is due to instance explicitly asked for in the statement but already present as variables).</p>

#### [ Reid Barton (Jul 26 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130308512):
<p>oops!</p>

#### [ Simon Hudon (Jul 26 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130312325):
<p>Hint: if <code>t</code> is the type of <code>is_closed_diagonal</code>, <code>t.is_pi</code> will return <code>tt</code> (true) because <code>t</code> is a pi type (the assumptions are basically function arguments). <code>t.binding_domain</code> will gives you the type of the first assumption or variable  (i.e. <code>Type u_1</code>) and <code>t.binding_body</code> will be the rest (i.e. <code>∀ [_inst_1 : topological_space α] [_inst_4 : topological_space α] [_inst_5 : t2_space α], is_closed {p : α × α | p.fst = p.snd}</code>). Look at their definition and write a <code>arguments : expr → tactic (list expr)</code> function. This will bring you closer to a solution.</p>

#### [ Patrick Massot (Jul 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20linter/near/130328113):
<p>Thank you very much, I'll try to work on this exercise soon (but not right now).</p>


{% endraw %}
