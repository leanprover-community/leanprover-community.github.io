---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21625TopologyonRn.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Topology on R^n](https://leanprover-community.github.io/archive/116395maths/21625TopologyonRn.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528202):
<p>I have the following code</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>
<span class="kn">open</span> <span class="n">classical</span>

<span class="kn">definition</span> <span class="n">type_pow</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span>
<span class="bp">|</span> <span class="n">α</span> <span class="mi">0</span>       <span class="o">:=</span> <span class="n">unit</span>
<span class="bp">|</span> <span class="n">α</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">type_pow</span> <span class="n">α</span> <span class="n">n</span> <span class="bp">×</span> <span class="n">α</span>

<span class="kn">instance</span> <span class="n">type_pow_instance</span> <span class="o">:</span> <span class="n">has_pow</span> <span class="kt">Type</span><span class="bp">*</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">type_pow</span><span class="bp">⟩</span>

<span class="kn">definition</span> <span class="n">sum_in_Rn</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">ℝ</span><span class="err">^</span><span class="n">n</span> <span class="bp">→</span> <span class="n">ℝ</span>
<span class="bp">|</span> <span class="mi">0</span>      <span class="n">x</span>    <span class="o">:=</span>  <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">sum_in_Rn</span> <span class="n">m</span> <span class="n">x</span><span class="o">)</span> <span class="bp">+</span> <span class="n">y</span>

<span class="kn">definition</span> <span class="n">standard_simplex</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">ℝ</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">sum_in_Rn</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span>

<span class="kn">namespace</span> <span class="n">standard_simplex</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>

<span class="kn">definition</span> <span class="n">topology_Rn</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">ℝ</span><span class="err">^</span><span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">topological_space</span> <span class="n">unit</span><span class="o">,</span> <span class="n">apply_instance</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">topological_space</span> <span class="o">(</span><span class="bp">_</span> <span class="bp">×</span> <span class="bp">_</span><span class="o">),</span>
 <span class="k">have</span> <span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">type_pow</span> <span class="n">ℝ</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">add</span> <span class="n">n</span> <span class="mi">0</span><span class="o">))</span> <span class="o">:=</span> <span class="n">topology_Rn</span> <span class="n">n</span><span class="o">,</span>
 <span class="k">have</span> <span class="n">t₂</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">ℝ</span><span class="o">,</span> <span class="k">begin</span> <span class="n">apply_instance</span> <span class="kn">end</span><span class="o">,</span>
 <span class="n">exact</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="n">t₁</span> <span class="err">⊔</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="n">t₂</span><span class="o">,</span>
 <span class="kn">end</span>

<span class="kn">definition</span> <span class="n">inclusion</span> <span class="o">:</span> <span class="n">standard_simplex</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">standard_simplex</span> <span class="n">n</span><span class="o">)</span>
 <span class="o">:=</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="n">inclusion</span> <span class="o">(</span><span class="bp">@</span><span class="n">topology_Rn</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>

<span class="kn">end</span> <span class="n">standard_simplex</span>
</pre></div>

#### [ Johan Commelin (May 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528205):
<p>I get red squiggles under <code>topology_Rn</code>, in its definition</p>

#### [ Johan Commelin (May 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528226):
<p>The error is: <code>rec_fn_macro only allowed in meta definitions</code></p>

#### [ Johan Commelin (May 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528267):
<p>So, two questions: how do I get lean to automatically deduce the topology on R^n on the second line of the induction? There is already an instance of <code>topological_space (α × β)</code>...</p>

#### [ Johan Commelin (May 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528272):
<p>The second is, how did I get this error, if I only copied a line from the proof of <code>topological_space (α × β)</code>...?</p>

#### [ Johannes Hölzl (May 14 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528752):
<p>It looks like you need to mark your definition<code>noncomputable</code> (or your entire theory).</p>
<p>But in general I would not advice to use this type construction. I think for <code>R ^ n</code>there are two options: Use <code>vec n R</code> (define the canonical topology on lists using <code>lfp</code>, and then use subtype for <code>vec</code>), or use <code>fin n -&gt; R</code> and use the topological space construction on function spaces.</p>

#### [ Johannes Hölzl (May 14 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528822):
<p>The advantage of seeing <code>R^n</code> as a function space is that you can do a lot of proofs assuming arbitrary functions, and no induction is necessary on your type itself.</p>

#### [ Gabriel Ebner (May 14 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528935):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> You stumbled upon this bug: <a href="https://github.com/leanprover/lean/issues/1890" target="_blank" title="https://github.com/leanprover/lean/issues/1890">https://github.com/leanprover/lean/issues/1890</a>  The unsoundness issue was fixed last year, but apparently there are still cases where you can accidentally use general recursion in non-meta definitions.  The culprit is the <code>begin apply_instance end</code>, which defines t₂ in terms of itself.</p>

#### [ Johan Commelin (May 14 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528991):
<p>So.. how do I fix it?</p>

#### [ Johan Commelin (May 14 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528995):
<p>I some how wish I could skip those <code>have</code>-lines anyway</p>

#### [ Johan Commelin (May 14 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529047):
<p>The system should figure that out itself..., although maybe the first <code>have</code>-line is to hard for it.</p>

#### [ Johannes Hölzl (May 14 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529049):
<blockquote>
<p>So.. how do I fix it?</p>
</blockquote>
<p>Seriously: Use another type!</p>

#### [ Johan Commelin (May 14 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529069):
<p>Like what? (Confused newbie behind this keyboard...)</p>

#### [ Johannes Hölzl (May 14 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529144):
<p>Use <code>fin n -&gt; R</code>, the topological space is already setup, i.e. it only needs the instance for <code>α → β</code> where <code>β</code> has a topological space.</p>

#### [ Johan Commelin (May 14 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529208):
<p>Ok, I'll try that</p>

#### [ Gabriel Ebner (May 14 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529325):
<blockquote>
<p>So.. how do I fix it?</p>
</blockquote>
<p>Aside from "don't do it" as Johannes already said, the main thing you can try if you see this bug is to move the <code>have</code> statements out of the begin-end block.  In this case, it is enough if you move just the <code>have t₁</code> before the begin.</p>

#### [ Johan Commelin (May 14 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530333):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Ok, so now I have <code>fin n \to \R</code>, but how do I get a topology on it? Because I can't find the instance that you just described...</p>

#### [ Johannes Hölzl (May 14 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530364):
<p>Hm, works here:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="n">def</span> <span class="n">test</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">}</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply_instance</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">def test : Π {α : Type u_1} {n : ℕ} [t : topological_space α], topological_space (fin n → α) :=</span>
<span class="cm">λ {α : Type u_1} {n : ℕ} [t : topological_space α], Pi.topological_space</span>
<span class="cm">-/</span>
</pre></div>

#### [ Johannes Hölzl (May 14 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530429):
<p>Or more specific</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">test</span> <span class="o">{</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">noncomputable def test : Π {n : nat}, topological_space.{0} (fin n → real) :=</span>
<span class="cm">λ {n : nat},</span>
<span class="cm">  @Pi.topological_space.{0 0} (fin n) (λ (a : fin n), real)</span>
<span class="cm">    (λ (a : fin n),</span>
<span class="cm">       @uniform_space.to_topological_space.{0} real (@metric_space.to_uniform_space&#39;.{0} real real.metric_space))</span>
<span class="cm">-/</span>
</pre></div>


<p>Don't forget <code>noncomputable</code> Maybe you want to setup it for your theory: use <code>noncomputable theory</code>  at the beginning (after the imports)</p>

#### [ Johan Commelin (May 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530805):
<p>Ok, that helped.</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">topology_Rn</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">ℝ</span><span class="err">^</span><span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intros</span> <span class="n">n</span><span class="o">,</span> <span class="k">show</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">apply_instance</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (May 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530844):
<p>Not term-mode, but I don't care too much (-;</p>


{% endraw %}
