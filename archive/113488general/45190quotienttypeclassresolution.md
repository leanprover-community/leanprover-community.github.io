---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45190quotienttypeclassresolution.html
---

## Stream: [general](index.html)
### Topic: [quotient typeclass resolution](45190quotienttypeclassresolution.html)

---


{% raw %}
#### [ Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182192):
<p>here is a working example:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">coset</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>

<span class="n">class</span> <span class="n">group_action</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fn</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">fn</span> <span class="mi">1</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span><span class="o">,</span> <span class="n">fn</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">h</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">fn</span> <span class="n">g</span> <span class="o">(</span><span class="n">fn</span> <span class="n">h</span> <span class="n">x</span><span class="o">))</span>

<span class="kn">variable</span> <span class="o">[</span><span class="n">group_action</span> <span class="n">G</span> <span class="n">X</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">g</span> <span class="n">h</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="err">●</span> <span class="bp">`</span><span class="o">:</span><span class="mi">100</span> <span class="o">:=</span> <span class="n">group_action</span><span class="bp">.</span><span class="n">fn</span> <span class="c1">-- \ci</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">G</span> <span class="n">X</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span> <span class="n">y</span><span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">one_act</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">G</span><span class="o">)</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">group_action</span><span class="bp">.</span><span class="n">one</span> <span class="n">G</span> <span class="n">x</span>

<span class="kn">lemma</span> <span class="n">mul_act</span> <span class="o">:</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">h</span><span class="o">)</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">●</span> <span class="n">h</span> <span class="err">●</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">group_action</span><span class="bp">.</span><span class="n">mul</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span>

<span class="kn">lemma</span> <span class="n">act_act</span> <span class="o">:</span> <span class="n">g</span> <span class="err">●</span> <span class="n">h</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">h</span><span class="o">)</span> <span class="err">●</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">group_action</span><span class="bp">.</span><span class="n">mul</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span>

<span class="kn">lemma</span> <span class="n">inv_act</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">g</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span><span class="bp">⁻¹</span> <span class="err">●</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">H</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">act_act</span><span class="o">]</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">G</span> <span class="n">X</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>

<span class="n">def</span> <span class="n">stab</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">g</span> <span class="bp">|</span> <span class="n">g</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">mem_stab_iff</span> <span class="o">:</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">stab</span> <span class="n">G</span> <span class="n">X</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">g</span> <span class="err">●</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">iff</span><span class="bp">.</span><span class="n">rfl</span>

<span class="kn">instance</span> <span class="n">stab</span><span class="bp">.</span><span class="n">is_subgroup</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">stab</span> <span class="n">G</span> <span class="n">X</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g1</span> <span class="n">g2</span> <span class="n">hg1</span> <span class="n">hg2</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">hg1</span> <span class="n">hg2</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_act</span><span class="o">,</span> <span class="n">hg1</span><span class="o">,</span> <span class="n">hg2</span><span class="o">],</span>
  <span class="n">one_mem</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">inv_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span> <span class="n">inv_act</span> <span class="n">hg</span> <span class="o">}</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets</span> <span class="o">(</span><span class="n">stab</span> <span class="n">G</span> <span class="n">X</span> <span class="n">x</span><span class="o">))</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">L</span> <span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182195):
<p>working but not minimalized</p>

#### [ Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182198):
<p>the error is on the last line</p>

#### [ Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182199):
<p>I cannot use <code>quotient.induction_on</code> because apparently Lean doesn't know that <code>left_cosets (stab G X x)</code> is a quotient</p>

#### [ Kenny Lau (Apr 17 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182246):
<p>error message:</p>
<div class="codehilite"><pre><span></span>[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : setoid G := @left_rel ?x_1 ?x_2 ?x_3 ?x_4
[class_instances] (1) ?x_2 : group G := _inst_1
[class_instances] (1) ?x_4 : @is_subgroup G _inst_1 _inst_1 ?x_3 := @stab.is_subgroup ?x_5 ?x_6 ?x_7 ?x_8 ?x_9
[class_instances] (2) ?x_6 : group G := _inst_1
[class_instances] (2) ?x_8 : @group_action G _inst_1 ?x_7 := _inst_2
[class_instances] trying next solution, current solution has metavars
@left_rel G _inst_1 (@stab G _inst_1 X _inst_2 ?x_9) _
[...]
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182252):
<p>what is this supposed to mean</p>

#### [ Kenny Lau (Apr 17 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182316):
<p>I think the <code>x</code> messed up everything</p>

#### [ Kenny Lau (Apr 17 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182318):
<p>How do i solve this problem?</p>

#### [ Mario Carneiro (Apr 17 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125183528):
<p><code>left_rel</code> is a bad instance, because it depends on <code>s</code> which is not in the output. I made it a <code>def</code> and used <code>local instance</code> for the proofs in that file. With this modification, you have to write</p>
<div class="codehilite"><pre><span></span>example (L : left_cosets (stab G X x)) : false :=
by letI := left_rel (stab G X x); exact
quotient.induction_on L _
</pre></div>


<p>but then it works</p>


{% endraw %}
