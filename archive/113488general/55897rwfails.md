---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55897rwfails.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rw fails](https://leanprover-community.github.io/archive/113488general/55897rwfails.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 24 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286611):
<p>What have I done wrong here?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">class</span> <span class="n">real</span><span class="bp">.</span><span class="n">nat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span>

<span class="n">class</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">q</span><span class="o">)</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="kn">check</span> <span class="n">true</span>
<span class="kn">instance</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat_of_nat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">nat</span> <span class="n">r</span><span class="o">]</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat</span> <span class="n">r</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="o">(</span><span class="n">H</span><span class="bp">.</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">),</span><span class="k">begin</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="n">pf</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H2</span><span class="o">,</span> <span class="c1">-- fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">  rewrite tactic failed, motive is not type correct</span>
<span class="cm">nested exception message:</span>
<span class="cm">check failed, application type mismatch (use &#39;set_option trace.check true&#39; for additional details)</span>
<span class="cm">state:</span>
<span class="cm">r : ℝ,</span>
<span class="cm">H : real.nat r,</span>
<span class="cm">H2 : r = ↑(nat.n r)</span>
<span class="cm">⊢ r = ↑↑(nat.n r)</span>
<span class="cm">-/</span>
  <span class="n">sorry</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>


<p>Setting <code>trace.check</code> to <code>true</code> tells me</p>
<div class="codehilite"><pre><span></span>[check] application type mismatch at
  nat.n _a
argument type
  real.nat r
expected type
  real.nat _a
</pre></div>

#### [ Kenny Lau (Nov 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286682):
<p>well the second <code>r</code> is also being rewrited</p>

#### [ Chris Hughes (Nov 24 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286695):
<p><code>H</code> is an implicit argument in the rhs of <code>H2</code>, and it will have the wrong type after the <code>r</code> on the rhs is rewritten.</p>

#### [ Kenny Lau (Nov 24 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286760):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">class</span> <span class="n">real</span><span class="bp">.</span><span class="n">nat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span>

<span class="n">class</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">q</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat_of_nat</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">nat</span> <span class="n">r</span><span class="o">]</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat</span> <span class="n">r</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">H</span><span class="bp">.</span><span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">rat</span><span class="bp">.</span><span class="n">cast_coe_nat</span> <span class="n">H</span><span class="bp">.</span><span class="n">n</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">H</span><span class="bp">.</span><span class="n">pf</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (Nov 24 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286776):
<p>Are there simp-lemmas that reduce these double coercions?</p>

#### [ Kenny Lau (Nov 24 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286819):
<p>sure</p>

#### [ Johan Commelin (Nov 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286956):
<p>So, <code>by simpa using H.pf</code>?</p>

#### [ Kenny Lau (Nov 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20fails/near/148286967):
<p>je kant het proberen... toch</p>


{% endraw %}
