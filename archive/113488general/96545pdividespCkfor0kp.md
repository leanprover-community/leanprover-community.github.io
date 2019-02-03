---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96545pdividespCkfor0kp.html
---

## Stream: [general](index.html)
### Topic: [p divides pCk for 0<k<p](96545pdividespCkfor0kp.html)

---


{% raw %}
#### [ Kenny Lau (Oct 14 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135785763):
<p>Do we have this already?</p>

#### [ Kevin Buzzard (Oct 14 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135785907):
<p>I don't know, but we have p-adic valuations and all the lemmas that go with them, and the easiest proof nowadays might be to compute the p-adic valuation of all the factorials. Another proof is to give a free action of Z/pZ on the set of subsets of Z/pZ of size k (addition) but no doubt this would be much more painful in Lean</p>

#### [ Chris Hughes (Oct 14 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787440):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">choose</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>
<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">lemma</span> <span class="n">dvd_fact_of_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">k</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hk</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="n">hkn</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">≤</span> <span class="n">n</span><span class="o">),</span> <span class="n">k</span> <span class="err">∣</span> <span class="n">fact</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">k</span> <span class="mi">0</span>     <span class="n">hk0</span> <span class="n">hkn</span> <span class="o">:=</span> <span class="n">absurd</span> <span class="n">hk0</span> <span class="o">(</span><span class="n">not_lt_of_le</span> <span class="n">hkn</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">k</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">hk0</span> <span class="n">hkn</span> <span class="o">:=</span> <span class="o">(</span><span class="n">lt_or_eq_of_le</span> <span class="n">hkn</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">hkn</span><span class="o">,</span> <span class="n">dvd</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">dvd_fact_of_le</span> <span class="n">hk0</span> <span class="o">(</span><span class="n">le_of_lt_succ</span> <span class="n">hkn</span><span class="o">))</span> <span class="bp">⟨</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">mul_comm</span> <span class="bp">_</span> <span class="bp">_⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">hkn</span><span class="o">,</span> <span class="n">hkn</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="bp">⟨</span><span class="n">n</span><span class="bp">.</span><span class="n">fact</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">prime_dvd_fact_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">prime</span> <span class="n">p</span><span class="o">),</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">n</span><span class="bp">.</span><span class="n">fact</span> <span class="bp">↔</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="n">p</span> <span class="n">hp</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pos_iff_ne_zero</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hp</span><span class="bp">.</span><span class="n">pos</span><span class="o">,</span> <span class="n">ne</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">ne_of_lt</span> <span class="n">hp</span><span class="bp">.</span><span class="n">gt_one</span><span class="o">)]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">p</span> <span class="n">hp</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">fact_succ</span><span class="o">,</span> <span class="n">hp</span><span class="bp">.</span><span class="n">dvd_mul</span><span class="o">,</span> <span class="n">prime_dvd_fact_iff</span> <span class="n">hp</span><span class="o">],</span>
  <span class="n">exact</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">le_of_dvd</span> <span class="o">(</span><span class="n">succ_pos</span> <span class="bp">_</span><span class="o">))</span> <span class="n">le_succ_of_le</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">lt_or_eq_of_le</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="err">∘</span> <span class="n">le_of_lt_succ</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">])</span><span class="bp">⟩</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hk</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="n">hkp</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">&lt;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">prime</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">choose</span> <span class="n">p</span> <span class="n">k</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">hp</span><span class="bp">.</span><span class="n">dvd_mul</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="k">show</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">choose</span> <span class="n">p</span> <span class="n">k</span> <span class="bp">*</span> <span class="o">(</span><span class="n">fact</span> <span class="n">k</span> <span class="bp">*</span> <span class="n">fact</span> <span class="o">(</span><span class="n">p</span> <span class="bp">-</span> <span class="n">k</span><span class="o">)),</span>
  <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">choose_mul_fact_mul_fact</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">hkp</span><span class="o">)]</span><span class="bp">;</span>
    <span class="n">exact</span> <span class="n">dvd_fact_of_le</span> <span class="n">hp</span><span class="bp">.</span><span class="n">pos</span> <span class="o">(</span><span class="n">le_refl</span> <span class="bp">_</span><span class="o">)))</span><span class="bp">.</span><span class="n">resolve_right</span>
      <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">hp</span><span class="bp">.</span><span class="n">dvd_mul</span><span class="o">,</span> <span class="n">prime_dvd_fact_iff</span> <span class="n">hp</span><span class="o">,</span>
          <span class="n">prime_dvd_fact_iff</span> <span class="n">hp</span><span class="o">,</span> <span class="n">not_or_distrib</span><span class="o">,</span> <span class="n">not_le</span><span class="o">,</span> <span class="n">not_le</span><span class="o">]</span><span class="bp">;</span>
        <span class="n">exact</span> <span class="bp">⟨</span><span class="n">hkp</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt_self</span> <span class="n">hp</span><span class="bp">.</span><span class="n">pos</span> <span class="n">hk</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Oct 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787707):
<p>The annoying thing about this proof, is that nothing in mathlib imports <code>data.nat.choose</code> and <code>data.nat.prime</code> at the moment.</p>

#### [ Kenny Lau (Oct 14 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787893):
<p>thank you <span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Chris Hughes (Oct 14 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135788049):
<p>PRed</p>


{% endraw %}
