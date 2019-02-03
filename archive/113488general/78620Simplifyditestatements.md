---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78620Simplifyditestatements.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Simplify dite statements](https://leanprover-community.github.io/archive/113488general/78620Simplifyditestatements.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rob Lewis (Aug 10 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233579):
<p>I've noticed the following:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span> <span class="k">then</span> <span class="mi">10</span> <span class="k">else</span> <span class="mi">0</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">10</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">dif_pos</span><span class="o">,</span> <span class="n">hn</span><span class="o">,</span> <span class="n">p</span><span class="o">]</span> <span class="kn">end</span> <span class="c1">-- works</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">dif_neg</span><span class="o">,</span> <span class="n">hn</span><span class="o">,</span> <span class="n">p</span><span class="o">]</span> <span class="kn">end</span> <span class="c1">-- fails</span>
</pre></div>


<p>What additional simp lemmas are needed to solve the second example? And is there a tactic in Mathlib with roughly this behavior, reducing dite statements where the positive or negative proof is in the context?</p>

#### [ Gabriel Ebner (Aug 10 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233746):
<p>There is <code>split_ifs</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">split_ifs</span>

<span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span> <span class="k">then</span> <span class="mi">10</span> <span class="k">else</span> <span class="mi">0</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">10</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">p</span><span class="bp">;</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">refl</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">p</span><span class="bp">;</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Mario Carneiro (Aug 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233821):
<p>interestingly, this works:</p>
<div class="codehilite"><pre><span></span>example (n : ℕ) (hn : ¬n &gt; 5) : p n = 0 :=
begin simp only [dif_neg hn, p] end
</pre></div>

#### [ Kenny Lau (Aug 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233827):
<p>is it so interesting that it works?</p>

#### [ Mario Carneiro (Aug 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233877):
<p>it is interesting that <code>simp</code> won't connect the two parts together in the original version</p>

#### [ Mario Carneiro (Aug 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233890):
<p>I suppose it is because <code>¬n &gt; 5</code> is not in simp normal form, so it gets rewritten and then the assumption <code>hn</code> doesn't match</p>

#### [ Rob Lewis (Aug 10 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233938):
<p>No? What is its simp normal form?</p>

#### [ Rob Lewis (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233988):
<p>It still fails if you make the &gt; a &lt;.</p>

#### [ Rob Lewis (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234002):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Thanks, that's useful! Somehow I assumed <code>split_ifs</code> did something different based on its name.</p>

#### [ Mario Carneiro (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234008):
<p>in mathlib it will rewrite to <code>n &lt;= 5</code></p>

#### [ Rob Lewis (Aug 10 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234091):
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">A</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="kn">constant</span> <span class="n">had</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="n">A</span>
<span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">had</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">A</span> <span class="n">n</span> <span class="k">then</span> <span class="mi">10</span> <span class="k">else</span> <span class="mi">0</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="n">A</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">10</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">dif_pos</span><span class="o">,</span> <span class="n">hn</span><span class="o">,</span> <span class="n">p</span><span class="o">]</span> <span class="kn">end</span> <span class="c1">-- works</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">A</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">dif_neg</span><span class="o">,</span> <span class="n">hn</span><span class="o">,</span> <span class="n">p</span><span class="o">]</span> <span class="kn">end</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Gabriel Ebner (Aug 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234151):
<p>Even better, it works without <code>only</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">p</span><span class="o">,</span> <span class="n">hn</span><span class="o">]</span>
</pre></div>

#### [ Gabriel Ebner (Aug 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234161):
<p>It needs one extra lemma:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">5</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">p</span><span class="o">,</span> <span class="n">hn</span><span class="o">,</span> <span class="n">dif_neg</span><span class="o">,</span> <span class="n">not_false_iff</span><span class="o">]</span>
</pre></div>

#### [ Rob Lewis (Aug 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234265):
<p>Aha! Thanks.</p>


{% endraw %}
