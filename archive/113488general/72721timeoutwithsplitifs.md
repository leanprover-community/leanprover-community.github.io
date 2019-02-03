---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72721timeoutwithsplitifs.html
---

## Stream: [general](index.html)
### Topic: [timeout with split_ifs](72721timeoutwithsplitifs.html)

---


{% raw %}
#### [ Kenny Lau (Jul 28 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130454443):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fin</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>

<span class="n">def</span> <span class="n">fin</span><span class="bp">.</span><span class="n">fall</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">),</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">n</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">i</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">fin</span><span class="bp">.</span><span class="n">descend</span> <span class="o">(</span><span class="n">pivot</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">),</span> <span class="n">i</span> <span class="bp">≠</span> <span class="n">pivot</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">n</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">i</span> <span class="n">H</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">pivot</span><span class="bp">.</span><span class="mi">1</span>
  <span class="k">then</span> <span class="n">i</span><span class="bp">.</span><span class="n">fall</span> <span class="o">(</span><span class="n">lt_of_lt_of_le</span> <span class="n">h</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">pivot</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>
  <span class="k">else</span> <span class="n">i</span><span class="bp">.</span><span class="n">pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H1</span><span class="o">,</span> <span class="n">H</span> <span class="err">$</span> <span class="k">by</span> <span class="n">subst</span> <span class="n">H1</span><span class="bp">;</span>
    <span class="n">replace</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">eq_zero_of_le_zero</span> <span class="o">(</span><span class="n">le_of_not_gt</span> <span class="n">h</span><span class="o">)</span><span class="bp">;</span>
    <span class="k">from</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fin</span><span class="bp">.</span><span class="n">ascend</span> <span class="o">(</span><span class="n">pivot</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">if</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">pivot</span><span class="bp">.</span><span class="mi">1</span> <span class="k">then</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span> <span class="k">else</span> <span class="n">i</span><span class="bp">.</span><span class="n">succ</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">fin</span><span class="bp">.</span><span class="n">descend_ascend</span> <span class="o">(</span><span class="n">pivot</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
  <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">pivot</span><span class="bp">.</span><span class="n">ascend</span> <span class="n">i</span> <span class="bp">≠</span> <span class="n">pivot</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">pivot</span><span class="bp">.</span><span class="n">descend</span> <span class="o">(</span><span class="n">pivot</span><span class="bp">.</span><span class="n">ascend</span> <span class="n">i</span><span class="o">)</span> <span class="n">H</span> <span class="bp">=</span> <span class="n">i</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">fin</span><span class="bp">.</span><span class="n">descend</span> <span class="n">fin</span><span class="bp">.</span><span class="n">ascend</span><span class="o">,</span>
  <span class="n">split_ifs</span> <span class="c1">-- (deterministic) timeout</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130454446):
<p>I've used <code>split_ifs</code> quite a lot but it just happens to timeout here</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455338):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">fin</span><span class="bp">.</span><span class="n">descend</span> <span class="n">fin</span><span class="bp">.</span><span class="n">ascend</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">P</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ite</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">pivot</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">i</span><span class="o">))</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">pivot</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">dP</span> <span class="o">:</span> <span class="n">decidable</span> <span class="n">P</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span> <span class="c1">-- fails</span>
</pre></div>


<p>Is <code>P</code> decidable? It looks decidable to me.</p>

#### [ Kenny Lau (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455339):
<p>it should be decidable</p>

#### [ Kenny Lau (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455342):
<p>but Lean is not very intelligent</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455351):
<p>Is there some missing instance <code>decidable.dite</code>?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455871):
<blockquote>
<p>Is there some missing instance <code>decidable.dite</code>?</p>
</blockquote>
<p><code>P</code> is just the statement that some nat is less than some other nat, right? But <code>example (a b : ℕ) : decidable (a &lt; b) := by apply_instance </code> works fine</p>

#### [ Kevin Buzzard (Jul 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456027):
<p>Oh I'm being an idiot. I've used <code>have</code> instead of <code>let</code> again.</p>

#### [ Gabriel Ebner (Jul 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456430):
<p><a href="https://github.com/leanprover/mathlib/pull/224" target="_blank" title="https://github.com/leanprover/mathlib/pull/224">https://github.com/leanprover/mathlib/pull/224</a></p>

#### [ Kevin Buzzard (Jul 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456434):
<p>Nice one Gabriel.</p>

#### [ Gabriel Ebner (Jul 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456474):
<p>Apparently <code>simp</code> cannot simplify the second ite.</p>

#### [ Kenny Lau (Jul 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456480):
<p>thanks</p>


{% endraw %}
