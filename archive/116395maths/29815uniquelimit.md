---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29815uniquelimit.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [unique limit](https://leanprover-community.github.io/archive/116395maths/29815uniquelimit.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jan 19 2019 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/unique%20limit/near/156454309):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I looked at <a href="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean">https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean</a> There is a comment saying you don't know how to use <code>wlog</code>. I think what you were looking for is:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">limits_aux</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">m</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">hl</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">l</span><span class="o">)</span>
<span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">by_contradiction</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">wlog</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">,</span>
  <span class="o">{</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">lt_trichotomy</span> <span class="n">l</span> <span class="n">m</span><span class="o">,</span> <span class="n">tauto</span><span class="o">,</span> <span class="o">},</span>
</pre></div>


<p>and then put the proof exactly as it was (and remove "_aux" from the name of the lemma since it's now directly proving what you want)</p>

#### [ Patrick Massot (Jan 19 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/unique%20limit/near/156454331):
<p>But your proof is rather contrived. Why not doing:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">zero_of_abs_lt_all</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">eq_zero_of_abs_eq_zero</span> <span class="err">$</span> <span class="n">eq_of_le_of_forall_le_of_dense</span> <span class="o">(</span><span class="n">abs_nonneg</span> <span class="n">x</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span> <span class="n">le_of_lt</span> <span class="o">(</span><span class="n">h</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">limits_are_unique</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">m</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">hl</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">l</span><span class="o">)</span>
<span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">eq_of_sub_eq_zero</span> <span class="o">(</span><span class="n">zero_of_abs_lt_all</span> <span class="bp">_</span> <span class="n">this</span><span class="o">),</span>
  <span class="n">intros</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hl</span> <span class="o">(</span><span class="n">ε</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">linarith</span><span class="o">)</span> <span class="k">with</span> <span class="n">Nl</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hm</span> <span class="o">(</span><span class="n">ε</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">linarith</span><span class="o">)</span> <span class="k">with</span> <span class="n">Nm</span> <span class="n">H&#39;</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">N</span> <span class="o">:=</span> <span class="n">max</span> <span class="n">Nl</span> <span class="n">Nm</span><span class="o">,</span>
  <span class="n">specialize</span> <span class="n">H</span>  <span class="n">N</span> <span class="o">(</span><span class="n">le_max_left</span>  <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">specialize</span> <span class="n">H&#39;</span> <span class="n">N</span> <span class="o">(</span><span class="n">le_max_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">exact</span> <span class="k">calc</span> <span class="bp">|</span><span class="n">l</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">≤</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">m</span><span class="bp">|</span> <span class="bp">+</span> <span class="bp">|</span><span class="n">a</span> <span class="n">N</span> <span class="bp">-</span> <span class="n">l</span><span class="bp">|</span> <span class="o">:</span> <span class="n">triangle&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
   <span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="bp">+</span> <span class="n">ε</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:</span> <span class="n">add_lt_add</span> <span class="n">H&#39;</span> <span class="n">H</span>
   <span class="bp">...</span> <span class="bp">=</span> <span class="n">ε</span> <span class="o">:</span> <span class="k">by</span> <span class="n">ring</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>which seems to obey your stylistic constraints?</p>


{% endraw %}
