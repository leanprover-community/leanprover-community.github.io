---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95622proofbyinductiononZ.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [proof by induction on Z](https://leanprover-community.github.io/archive/113488general/95622proofbyinductiononZ.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 09 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232278):
<p>Why is a thing like this not possible?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">theorem</span> <span class="n">map_gsmul</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">B</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span> <span class="n">f</span> <span class="o">(</span><span class="n">gsmul</span> <span class="n">n</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">gsmul</span> <span class="n">n</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_of_nat</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="n">f</span><span class="o">]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_of_nat</span><span class="o">,</span> <span class="n">succ_smul</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">add</span> <span class="n">f</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">map_gsmul</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span><span class="n">n</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_neg</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">neg</span> <span class="n">f</span><span class="o">],</span>
  <span class="n">exact</span> <span class="n">map_gsmul</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Dec 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232459):
<p>That's a funny well founded relation.</p>

#### [ Johan Commelin (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232508):
<p>I wouldn't say it's funny. I think it's very natural.</p>

#### [ Johan Commelin (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232522):
<p>I'm just nesting the inductive property of <code>int</code> and <code>nat</code>.</p>

#### [ Chris Hughes (Dec 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232523):
<p>But you haven't told lean what it is. I would just prove <code>map_smul</code> first for naturals</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232531):
<p>I think you need to be more explicit about the well founded relation</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232532):
<p>or use lemmas like chris says</p>

#### [ Chris Hughes (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232534):
<p>You could do <code>using_well_founded</code> but proving <code>map_smul</code> first is more sensible</p>

#### [ Johan Commelin (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232535):
<p>But why can't I just nest inductive properties?</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232537):
<p>because that's not what you did</p>

#### [ Johan Commelin (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232579):
<p>Hmm, so what did I do?</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232580):
<p>you call <code>(n+1)</code> case from <code>-[1+n]</code> case</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232584):
<p>that's not structurally well founded</p>

#### [ Johan Commelin (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232587):
<p>Sure, but <code>n+1</code> is an <code>of_nat</code>, and I had proven those already.</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232588):
<p>that's called a lemma</p>

#### [ Johan Commelin (Dec 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232591):
<p>/me sighs...</p>

#### [ Mario Carneiro (Dec 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232598):
<p>when you write it all in one big induction lean has no choice but to assume everything depends on everything else</p>

#### [ Johan Commelin (Dec 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232655):
<p>But don't you think this is a typical strategy for proving things about Z? Does this deserve special support?</p>

#### [ Johan Commelin (Dec 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232663):
<p>Or should I prove <code>map_smul</code> for add_monoid homs? (Btw, I think there is no instance from <code>add_group_hom</code>s to <code>add_monoid_hom</code>s).</p>

#### [ Kenny Lau (Dec 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151232711):
<blockquote>
<p>But don't you think this is a typical strategy for proving things about Z? Does this deserve special support?</p>
</blockquote>
<p>I think the typical strategy is to use <code>int.induction_on</code></p>

#### [ Chris Hughes (Dec 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151233000):
<p>Here's a horrible proof using <code>using_well_founded</code></p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">map_gsmul</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">B</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span> <span class="n">f</span> <span class="o">(</span><span class="n">gsmul</span> <span class="n">n</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">gsmul</span> <span class="n">n</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_of_nat</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="n">f</span><span class="o">]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:=</span>
  <span class="k">have</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">with_top</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="k">from</span> <span class="n">with_top</span><span class="bp">.</span><span class="n">coe_lt_coe</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_</span><span class="o">),</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_of_nat</span><span class="o">,</span> <span class="n">succ_smul</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">add</span> <span class="n">f</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="n">map_gsmul</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span><span class="n">n</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">have</span> <span class="o">((</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">with_top</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="err">⊤</span><span class="o">,</span> <span class="k">from</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">gsmul_neg</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">neg</span> <span class="n">f</span><span class="o">],</span>
  <span class="n">exact</span> <span class="n">map_gsmul</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
<span class="kn">end</span>
<span class="n">using_well_founded</span>
  <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">@</span><span class="n">inv_image</span><span class="bp">.</span><span class="n">wf</span> <span class="bp">ℤ</span> <span class="o">(</span><span class="n">with_top</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">_</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">i</span> <span class="n">coe</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="err">⊤</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">with_top</span> <span class="bp">ℕ</span><span class="o">)</span>
      <span class="o">(</span><span class="n">with_top</span><span class="bp">.</span><span class="n">well_founded_lt</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_wf</span><span class="o">)</span><span class="bp">⟩</span><span class="o">],</span>
  <span class="n">dec_tac</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Dec 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20by%20induction%20on%20Z/near/151233113):
<p>I understand why you suggest the other strategy...</p>


{% endraw %}
