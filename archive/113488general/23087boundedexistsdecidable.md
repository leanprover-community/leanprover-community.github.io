---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23087boundedexistsdecidable.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [bounded exists decidable](https://leanprover-community.github.io/archive/113488general/23087boundedexistsdecidable.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567139):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">nat</span><span class="bp">.</span><span class="n">decidable_bexists_lt</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">k</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">P</span> <span class="n">n</span> <span class="n">h</span><span class="o">)],</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">IH</span><span class="bp">;</span> <span class="n">intro</span><span class="bp">;</span> <span class="n">resetI</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">not_lt_zero</span> <span class="bp">_</span> <span class="n">h</span><span class="o">)</span> <span class="o">},</span>
  <span class="n">cases</span> <span class="n">IH</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">k</span> <span class="n">h</span><span class="o">,</span> <span class="n">P</span> <span class="n">k</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_of_lt</span> <span class="n">h</span><span class="o">))</span> <span class="k">with</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">by_cases</span> <span class="n">p</span> <span class="o">:</span> <span class="n">P</span> <span class="n">n</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="n">n</span><span class="o">),</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">is_true</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="n">n</span><span class="o">,</span> <span class="n">p</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">is_false</span><span class="o">,</span>
      <span class="n">intro</span> <span class="n">hk</span><span class="o">,</span>
      <span class="n">rcases</span> <span class="n">hk</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_iff_lt_or_eq</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hk1</span> <span class="k">with</span> <span class="n">hk</span> <span class="n">hk</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">exact</span> <span class="n">h</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">subst</span> <span class="n">hk</span><span class="o">,</span> <span class="n">exact</span> <span class="n">p</span> <span class="n">hk2</span> <span class="o">}</span> <span class="o">}</span> <span class="o">},</span>
  <span class="n">apply</span> <span class="n">is_true</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_of_lt</span> <span class="n">hk1</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span>
<span class="kn">end</span>

<span class="kn">instance</span> <span class="n">nat</span><span class="bp">.</span><span class="n">decidable_exists_fin</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
  <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">i</span><span class="o">,</span> <span class="n">P</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">decidable_of_iff</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">k</span> <span class="n">h</span><span class="o">,</span> <span class="n">P</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span>
<span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">⟨⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk1</span><span class="o">,</span> <span class="n">hk2</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567143):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> nao penso que isso e em mathlib agora</p>

#### [ Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567144):
<p>would you include them inside?</p>

#### [ Chris Hughes (Apr 23 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125569210):
<p>Not sure, but I think they might be there for generic fintypes.</p>


{% endraw %}
